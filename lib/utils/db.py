# -*- coding: utf-8 -*-

from prettyPrint import *
from sqlite3 import *
from os import listdir,system

class DB:
    def __init__(self):
        self.db = 'db/nss.db'
        self.plugin = 'plugins'
        self.mongodb = 'mongodb'
        self.sep = "/"


    def initDB(self):        
        self.execSQL("create table if not exists nss(id integer primary key,type text,path text)")
        self.execSQL("delete from nss")
        self.insertToDB(self.getPlugins(self.mongodb),self.mongodb)

    def insertToDB(self,plugins,dbType):
        '''insert data to DB'''
        for plugin in plugins:
            plugin = plugin[:len(plugin)-3]#去掉.py
            self.execSQL('insert into nss(type,path) values("%s","%s/%s")'%(dbType,dbType,plugin))

    def execSQL(self,sql):
        '''execute a sql'''
        conn = connect(self.db)
        conn.execute(sql)
        conn.commit()
        conn.close()
        
    def getPlugins(self,path):
        '''get plugins list'''
        return listdir(self.plugin+self.sep+path)
    
    def fetchAll(self,sql):
        '''sqlite3=>cur.fetchall()'''
        conn = connect(self.db)
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        return res
    
    def searchPlugin(self,keyword):
        '''search plugins'''
        sql = 'select * from nss where path like "%'+keyword+'%"'
        result = self.fetchAll(sql)
        msg = "SEARCH '%s'"%keyword
        prettyPrint.prettyPrint(msg,YELLOW)
        prettyPrint.prettyPrint("="*len(msg),GREY)
        self.showSearchResult(result)
        
    def searchPluginByPid(self,pid):
        cur = self.cursor()
        sql = "select * from nss where id = %s"%pid
        res = cur.execute(sql).fetchone()
        cur.close()
        return res

    def showSearchResult(self,result):
        '''format print results'''
        prettyPrint.prettyPrint("%5s %-60s %-7s"%("ID","PATH","TYPE"),YELLOW)
        prettyPrint.prettyPrint("%5s %-60s %-7s"%("-"*5,"-"*60,"-"*7),GREY)
        for res in result:
            pluginId = res[0]
            pluginType = res[1]
            pluginPath = res[2]
            if len(pluginPath)>70:
                pluginPath = pluginPath[:68]+".."
            prettyPrint.prettyPrint("%5s %-60s %-7s"%(pluginId,pluginPath,pluginType),CYAN)
        prettyPrint.prettyPrint("="*74,GREY)
        prettyPrint.prettyPrint("total [%s] results found "%len(result),GREEN)
        
    def showPlugins(self,pluginType):
        '''show plugins'''
        pluginStr = ("show %s plugins"%pluginType).upper()
        prettyPrint.prettyPrint(pluginStr,YELLOW)
        prettyPrint.prettyPrint("="*len(pluginStr),GREY)
        if pluginType.lower() == 'all':
            sql = 'select * from nss'
        else:
            sql = 'select * from nss where type like "%'+pluginType+'%"'
        self.showSearchResult(self.fetchAll(sql))
                
    def getPluginNums(self,pluginType):
        '''get plugins nums'''
        if pluginType.lower == 'all':
            return len(self.fetchAll('select * from nss'))
        else:
            return len(self.fetchAll('select * from nss where type like "%'+pluginType+'%"'))

if __name__=='__main__':
    print __doc__
else:
    db = DB()
