'''
Mst=>class=>load::load plugin
Mst=>class=>plug::plugin class
'''
from MstColor  import *
from MstPlugin import *
from os        import system
from cmd import *
class loadModule:
    '''load mst plugin'''
    def __init__(self,sqlRes):
        pluType = sqlRes[1]
        pluPath = sqlRes[2[
        if sqlRes:
            self.pluType = pluType
            self.pluPath = pluPath
        else:
            self.pluType = ""
            self.pluPath = ""
        self.prompt = "NoSqlSploit %s>"%pluType

    
    def preloop(self):
        if self.pluPath:
            self.loadError(1)
        else:
            mm=m("plugins/%s.py"%self.pluPath)
            mm.printp(self.pluType,self.pluPath)

    def loadError(self,flag):
        if flag:
            color.cprint("[!] NO THIS PLUGIN !",RED)
        else:
            color.cprint("[!] IT'S A PAYLOAD !",RED)

    if   pcmd == 'back' or pcmd == 'exit':
        break

    def do_help(self,arg):
        mm.pluHelp()

    def do_cls(self,arg):
        mm.cls()

    def do_info(self,arg):
        mm.info()

    def do_show(self,opts):
        mm.opt()

    def do_exploit(self,arg):
        mm.exploit()
    def do_set(self,param,value):
        if len(param) and len(value):
            mm.setp(ptmp[1],ptmp[2])
        else:
            color.cprint("[?] USAGE:set <PARAM> <VALUE>",YELLOW)
    elif len(pcmd.split(" "))==3:
        ptmp=pcmd.split(" ")
        if ptmp[0] == "set":
            if len(ptmp[1])>0 and len(ptmp[2])>0:
                mm.setp(ptmp[1],ptmp[2])
        else:
            system(pcmd)
    else:
        system(pcmd)
        except KeyboardInterrupt:
            color.cprint("\n[!] CTRL+C EXIT !",RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)


if __name__ == '__main__':
    print __doc__
else:
    load=load()
