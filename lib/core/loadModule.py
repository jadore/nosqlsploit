'''
'''
from MstColor  import *
from MstPlugin import *
from os        import system
from cmd import *
class loadModule(Cmd):
    '''load plugins'''
    def __init__(self,pluginPath):
        Cmd.__init__(self)
        plu = pluginPath.split("/")
        if pluginPath:
            self.pluPath = pluginPath
            self.pluType = plu[0]
            self.pluName = plu[1]
        else:
            self.pluPath = pluginPath
            self.pluType = ""
            self.pluName = ""
        self.prompt = "NoSqlSploit %s[%s]>"%(self.pluType,self.pluName)

    
    def preloop(self):
        if self.pluPath:
            self.mm=m("plugins/%s.py"%self.pluPath)
            self.mm.printp(self.pluType,self.pluPath)
        else:
            self.loadError(1)

    def loadError(self,flag):
        if flag:
            color.cprint("[!] NO THIS PLUGIN !",RED)
        else:
            color.cprint("[!] IT'S A PAYLOAD !",RED)

    def do_exit(self,arg):
        return True

    def do_help(self,arg):
        self.mm.pluHelp()

    def do_cls(self,arg):
        self.mm.cls()

    def do_info(self,arg):
        self.mm.info()

    def do_show(self,opts):
        self.mm.opt()

    def do_exploit(self,arg):
        self.mm.exploit()

    def do_set(self,param,value):
        if len(param) and len(value):
            self.mm.setp(param,value)
        else:
            color.cprint("[?] USAGE:set <PARAM> <VALUE>",YELLOW)

    def do_EOF(self):
        return True

if __name__ == '__main__':
    try:
        loads = loadModule(arg)
        loads.cmdloop()
    except KeyboardInterrupt:
        color.cprint("\n[!] CTRL+C EXIT !",RED)
    except Exception,e:
        color.cprint("[!] ERR:%s"%e,RED)
