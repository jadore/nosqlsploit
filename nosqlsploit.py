#!/usr/bin/python2.7
#coding:utf-8

#author::jadore
#date::2014.07.07
#version::v1.0
#mail::jadore@jadore.wang

from cmd import *
from lib.utils.tools import tools
from lib.utils.banner import banner
from lib.utils.db import DB
from lib.utils.prettyPrint import *
from lib.utils.prettyPrint import prettyPrint as pp

db = DB()
banner = banner()

class NoSqlSploit(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "NoSqlSploit>"
        self.tools = tools
        self.banner = banner
        tools.start()
        db.initDB()
        banner.main()
    #def preloop(self):
    #    print "print this msg before entering into the cmd line"

    #def postloop(self):
    #    print "print this msg line after leaving the loop"

    #def precmd(self,line):
    #    print "print this line msg before do a command"
    #    return Cmd.precmd(self,line)

    #def postcmd(self,stop,line):
    #    print "pring this line msg after do a command"

    #def do_test(self,line):
    #    print "test command,just print the arguments"
    #    if line == 'exit':
    #        exit()
    #    else:
    #        print line

    def do_help(self,line):
        print line
        tools.mainHelp()

    def do_exit(self,arg):
        tools.mainExit()

    def do_cls(self,arg):
        tools.cls()

    def do_use(self,arg):
        if arg:
            loadModule.load(arg)
        else:
            tools.usage('use')

    def do_show(self,arg):
        if arg in ["mongodb","all"]:
            db.showPlugins(arg)
        else:
            tools.usage('show')
    
    def do_search(self,arg):
        if arg == "":
            tools.usage('search')
        else:
            db.search(arg)


    def do_banner(self,arg):
        banner.main()
                                     
if __name__ == '__main__':
    #main()
    try:
        noSqlSploit = NoSqlSploit()
        noSqlSploit.cmdloop()
    except KeyboardInterrupt:
        tools.mainExit()
    except Exception,e:
        tools.errmsg(e)
