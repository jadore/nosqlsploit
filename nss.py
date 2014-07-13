#!/usr/bin/python2.7
#coding:utf-8

#author:jadore
#create:2014-07-07 
#version:v1.0
#mail:jadore@jadore.wang
#last update:2014-07-09 14:33

"""
"""

from cmd import *
from lib.utils.tools import *
from lib.utils.banner import *
from lib.utils.db import *
from lib.utils.prettyPrint import *
from lib.utils.prettyPrint import prettyPrint as pp
from lib.core.loadPlugin import *


class NSS(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "NSS >"
        self.tools = tools()
        self.banner = banner()
        self.db = DB()

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

    def do_show(self,arg):
        if arg :
            self.db.showPlugins(arg)
        else:
            self.tools.usage('show')
    
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
