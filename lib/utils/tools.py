# -*- coding: utf-8 -*-

from prettyPrint import prettyPrint as pp
from prettyPrint import *
from os import listdir,system

class tools:
    def __init__(self):
        self.logo = 'NoSqlSploit'

    def printLogo(self):
        '''print nosqlspoit logo..'''
        pp.prettyPrint(self.logo,GREY,0)
        
    def exeCMD(self,cmd):
        '''run system command'''
        pp.prettyPrint('[*] EXEC:%s'%cmd,RED)
        system(cmd)
        
    def cls(self):
        '''clear'''
        if name == 'nt':
            system("cls")
        else:
            system("clear")

    def errmsg(self,msg):
        '''show error msg'''
        pp.prettyPrint("[!] Err:%s"%msg,RED)
        
    def mainExit(self):
        '''exit app'''
        pp.prettyPrint("\n[*] GoodBye :)",RED)
        exit(0)

    def start(self):
        pp.prettyPrint("[*] Start NoSqlSploit ..",GREEN)
        
    def mainHelp(self):
        '''show help'''
        pp.prettyPrint('NoSqlSploit HELP MENU',YELLOW)
        pp.prettyPrint('=============',GREY)
        pp.prettyPrint('        COMMAND         DESCRIPTION',YELLOW)
        pp.prettyPrint('        -------         -----------',GREY,0)
        pp.prettyPrint('''
        help            Displays the help menu
        exit            Exit the MstApp
        cls             Clear the screen
        show            List the plugins
        search          Search plugins
        use             Use the plugin
        update          Update mst|plugins''',CYAN)
        pp.prettyPrint('MST HELP::SHOW',YELLOW)
        pp.prettyPrint('==============',GREY)
        pp.prettyPrint('        COMMAND         DESCRIPTION',YELLOW)
        pp.prettyPrint('        -------         -----------',GREY,0)
        pp.prettyPrint('''
        exploit         List the exploit plugins
        payload         List the payload plugins
        multi           List the multi plugins
        all             List all the plugins''',CYAN)

    def usage(self,c):
        '''show usage'''
        def ius(c):
            pp.prettyPrint('[?] USAGE:%s'%c,YELLOW)
        if   c == "search":
            ius('search <plugin>')
        elif c == "show":
            ius('show <exploit|payload|multi|all>')
        elif c == "use":
            ius('use <plugin|pluginID>')
        elif c == "update":
            ius('update <mst|plugins>')

if __name__=='__main__':
    print __doc__
else:
    tools = tools()
