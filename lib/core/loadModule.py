'''
'''
from prettyPrint import *
from prettyPrint import prettyPrint as pp
from pluginModule import *
from os import system
from cmd import *
class loadModule(Cmd):
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
        Type = pp.set_cmd_text_color(WHITE,self.pluType)
        Name = pp.set_cmd_text_color(RED,self.pluName)
        self.prompt = "NSS %s[%s]>"%(Type,Name)

    
    def preloop(self):
        if self.pluPath:
            self.pluginModule = pluginModule("plugins/%s.py"%self.pluPath)
        else:
            self.loadError()

    def loadError(self):
        pp.prettyPrint("[!] NO THIS PLUGIN !",RED)

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

    def do_set(self,arg):
        args = arg.split(" ")
        if(len(args) == 2):
            param = args[0]
            value = args[1]
            if len(param) and len(value):
                res = self.pluginModule.checkParam(param)
                if res:
                    self.pluginModule.setParam(param ,value)
                else:
                    pp.prettyPrint("[!] ERR:invalid set param" ,YELLOW)
        else:
            pp.prettyPrint("[?] USAGE:set <PARAM> <VALUE>" ,YELLOW)

    def complete_set(self,text,line,begidx,endidx):
        USE_ARG = self.pluginModule.getOptions()
        if not text:
            completions = USE_ARG[:]
        else:
            completions = [i for i in USE_ARG if i.startswith(text.upper())]
        return completions

    def do_EOF(self):
        return True

    do_back = do_exit

if __name__ == '__main__':
    try:
        loads = loadPlugin(arg)
        loads.cmdloop()
    except KeyboardInterrupt:
        pp.prettyPrint("\n[!] CTRL+C EXIT !",RED)
    except Exception,e:
        pp.prettyPrint("[!] ERR:%s"%e,RED)
