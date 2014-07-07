#!/usr/bin/python2.7
#coding:utf-8

#author::jadore
#date::2014.07.07
#version::v1.0
#mail::jadore@jadore.wang

from libs.MstUpdate import update
from libs.MstCache  import cache

def main():
    cache.start()
    try:
        while True:
            cache.printmst()
            cmd=raw_input('>')
            if   cmd == 'help':
                cache.mainhelp()
            elif cmd == 'exit':
                cache.mainexit()
            elif cmd == 'cls' :
                cache.cls()
            elif cmd == 'use':
                cache.usage("use")
            elif cmd == 'show':
                cache.usage("show")
            elif cmd == 'search':
                cache.usage("search")
            elif cmd == 'banner':
                cache.banner()
            elif cmd == 'update':
                update.start()
            elif len(cmd.split(" ")) == 2:
                cnd = cmd.split(" ")
                c   = cnd[0]
                g   = cnd[1]
                if    c == 'search':
                    if len(g)>0 and len(g.split(" "))>0:
                        cache.search(g)
                    else:
                        cache.usage("search")
                elif  c == 'show':
                    if   g == 'exploit':
                        cache.showplus('exploit')
                    elif g == 'payload':
                        cache.showplus('payload')
                    elif g == 'multi':
                        cache.showplus('multi')
                    elif g == 'all':
                        cache.showplus('all')
                    else:
                        cache.usage("show")
                elif  c == 'use':
                    if len(g) > 0 or len(g.split(" ")) > 0:
                        cache.load(g)
                    else:
                        cache.usage("use")
                elif  len(cmd) > 0:
                    cache.execmd(cmd)
            elif len(cmd) > 0:
                cache.execmd(cmd)
    except KeyboardInterrupt:
            cache.mainexit()
    except Exception,e:
            cache.errmsg(e)
                                     
if __name__=='__main__':
    main()
