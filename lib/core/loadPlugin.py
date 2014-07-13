'''
'''
from prettyPrint import *
from prettyPrint import prettyPrint as pp
from pluginModule import *
from os        import system
from cmd import *
class loadPlugin(Cmd):
    '''load plugins'''
    def __init__(self,pluginPath):
        Cmd.__init__(self)
        plu = pluginPath.split("/")
        if len(plu) == 2:
            self.pluPath = pluginPath
            self.pluType = plu[0]
            self.pluName = plu[1]
        else:
            self.pluPath = pluginPath
            self.pluType = ""
            self.pluName = ""
        self.prompt = "NSS %s[%s]>"%(self.pluType,self.pluName)

    
    def preloop(self):
        if self.pluPath:
            self.pluginModule = pluginModule("plugins/%s.py"%self.pluPath)
            self.pluginModule.printPluginLogo(self.pluType,self.pluName)
        else:
            self.loadError(1)

    def loadError(self,flag):
        if flag:
            pp.prettyPrint("[!] NO THIS PLUGIN !",RED)
        else:
            pp.prettyPrint("[!] IT'S A PAYLOAD !",RED)

    def do_exit(self,arg):
        return True

    def do_help(self,arg):
        self.pluginModule.pluginHelp()

    def do_cls(self,arg):
        self.pluginModule.cls()

    def do_info(self,arg):
        self.pluginModule.info()

    def do_show(self,opts):
        self.pluginModule.showOptions()

    def do_exploit(self,arg):
        self.pluginModule.exploit()

    def do_set(self,param,value):
        if len(param) and len(value):
            self.pluginModule.setParam(param ,value)
        else:
            pp.prettyPrint("[?] USAGE:set <PARAM> <VALUE>" ,YELLOW)

    def do_EOF(self):
        return True

if __name__ == '__main__':
    try:
        loads = loadPlugin(arg)
        loads.cmdloop()
    except KeyboardInterrupt:
        pp.prettyPrint("\n[!] CTRL+C EXIT !",RED)
    except Exception,e:
        pp.prettyPrint("[!] ERR:%s"%e,RED)
