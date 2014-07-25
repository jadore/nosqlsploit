#!/usr/bin/python2.7
#coding:utf-8

#author:jadore
#create:2014-07-07 
#version:v1.0
#mail:jadore@jadore.wang
#last update:2014-07-09 14:33

"""
"""

from os import name
from cmd import *
from lib.utils.tools import *
from lib.utils.banner import *
from lib.utils.db import *
from lib.utils.prettyPrint import *
from lib.utils.prettyPrint import prettyPrint as pp
from lib.core.loadModule import *

class NSS(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        prompt = "NSS >"
        self.prompt = prompt
        self.tools = tools()
        self.banner = banner()
        self.db = DB()
        self.SHOW_ARG = ["all","mongodb","multi"]

    def preloop(self):
        self.tools.start()
        self.db.initDB()
        self.banner.main()

    def do_help(self,line):
        self.tools.mainHelp()

    def do_exit(self,arg):
        self.tools.mainExit()

    def do_cls(self,arg):
        self.tools.cls()

    def do_use(self,arg):
        if arg:
            loadModule(arg).cmdloop()
        else:
            self.tools.usage('use')

    def complete_use(self,text,line,begidx,endidx):
        import readline
        USE_ARG = self.db.getPluginPath()
        readline.set_completer_delims(' \n\t`~!@#$%^&*()-=+[{]}\\|;:\'<>?')#重新设置completer_delims，将"/"剔除，从而优化自动不全
        if not text:
            completions = USE_ARG[:]
        else:
            completions = [i for i in USE_ARG if i.startswith(text)]
        return completions

    def do_show(self,arg):
        if arg :
            self.db.showPlugins(arg)
        else:
            self.tools.usage('show')

    def complete_show(self,text,line,begidx,endidx):
        if not text:
            completions = self.SHOW_ARG[:]
        else:
            completions = [i for i in self.SHOW_ARG if i.startswith(text)]
        return completions

    
    def do_search(self,arg):
        if arg == "":
            self.tools.usage('search')
        else:
            self.db.searchPlugin(arg)

    def do_banner(self,arg):
        self.banner.main()

if __name__ == '__main__':
    tool = tools()
    try:
        nss = NSS()
        nss.cmdloop()
    except KeyboardInterrupt:
        tool.mainExit()
    except Exception,e:
        tool.errmsg(e)
