# -*- coding: utf-8 -*-
'''
MstCache=>class
For main's some func or other~
update:2013/10/26
'''

from os import listdir,system
from random import choice
from MstLoad import load

class loadModule:
    def loadError(self,res):
        if res:
            color.cprint("[!] NO THIS PLUGIN !",RED)
        else:
            color.cprint("[!] IT'S A PAYLOAD !",RED)
    def load(self,plugin):
        '''load plugins'''
        try:
            pid=int(plugin)
            if len(self.sql_all('select * from mst where id=%s'%pid))==0:
                noload()
            else:
                plu=getplu(pid)
                if len(plu)>0:
                    pt=plu.split("/")[0]
                    load.start(pt,plu)
                else:
                    noload(1)
        except:
            if len(self.sql_all('select * from mst where path="%s"'%plugin))==0:
                noload()
            else:
                pt=plugin.split("/")[0]
                load.start(pt,plugin)

if __name__=='__main__':
    print __doc__
else:
    loadModule = loadModule()
