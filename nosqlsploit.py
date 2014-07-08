#!/usr/bin/python2.7
#coding:utf-8

#author::jadore
#date::2014.07.07
#version::v1.0
#mail::jadore@jadore.wang

from lib.utils.tools import tools
from lib.utils.banner import banner
from lib.utils.db import DB
from lib.utils.prettyPrint import *
from lib.utils.prettyPrint import prettyPrint as pp

db = DB()
banner = banner()

def main():
    tools.start()
    db.initDB()
    banner.main()
    try:
        while True:
            cmd = raw_input('>')
            if   cmd == 'help':
                tools.mainHelp()
            elif cmd == 'exit':
                tools.mainExit()
            elif cmd == 'cls' :
                tools.cls()
            elif cmd == 'use':
                tools.usage("use")
            elif cmd == 'show':
                tools.usage("show")
            elif cmd == 'search':
                tools.usage("search")
            elif cmd == 'banner':
                banner.main()
            elif len(cmd.split(" ")) == 2:
                cnd = cmd.split(" ")
                c   = cnd[0]
                g   = cnd[1]
                if    c == 'search':
                    if len(g)>0 and len(g.split(" "))>0:
                        db.search(g)
                    else:
                        tools.usage("search")
                elif  c == 'show':
                    if   g == 'mongodb':
                        db.showPlugins('mongodb')
                    elif g == 'all':
                        db.showPlugins('all')
                    else:
                        tools.usage("show")
                elif  c == 'use':
                    if len(g) > 0 or len(g.split(" ")) > 0:
                        cache.load(g)
                    else:
                        tools.usage("use")
                elif  len(cmd) > 0:
                    tools.exeCMD(cmd)
            elif len(cmd) > 0:
                tools.exeCMD(cmd)
    except KeyboardInterrupt:
            tools.mainExit()
    except Exception,e:
            tools.errmsg(e)
                                     
if __name__ == '__main__':
    main()
