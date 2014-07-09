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
        '''exit NoSqlSploit'''
        pp.prettyPrint("\nBye ",RED)
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
        exit            Exit the NoSqlSploit
        cls             Clear the screen
        show            List the plugins
        search          Search plugins
        use             Use the plugin''',CYAN)
        pp.prettyPrint('NoSqlSploit HELP::SHOW',YELLOW)
        pp.prettyPrint('==============',GREY)
        pp.prettyPrint('        COMMAND         DESCRIPTION',YELLOW)
        pp.prettyPrint('        -------         -----------',GREY,0)
        pp.prettyPrint('''
        exploit         List the mongodb plugins
        all             List all the plugins''',CYAN)

    def usage(self,keyword):
        '''show usage'''
        def showUsage(tips):
            pp.prettyPrint('[?] USAGE:%s'%tips,YELLOW)
        if  keyword == "search":
            showUsage('search <plugin>')
        elif keyword == "show":
            showUsage('show <mongodb|all>')
        elif keyword == "use":
            showUsage('use <plugin|pluginID>')

if __name__=='__main__':
    print __doc__
else:
    tool = tools()
