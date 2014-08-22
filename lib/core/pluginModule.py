'''
'''
from prettyPrint import *
from prettyPrint import prettyPrint as pp
from exploitModule import *
from os import path,system

class pluginModule:
    '''NSS plugin's class'''
    def __init__(self,pluginPath):
        '''exec plugin code'''
        fp = open(pluginPath).read()
        exec(fp)
        code = '\n'
        for opt in NSSPlugin.opts:
            key = opt[0]
            value = opt[1]
            code += 'global %s\n'%key
            code += '%s="%s"\n'%(key ,value)
        code += "global plugin\n"
        code += "plugin = NSSPlugin()\n"
        exec(fp+code)

    def info(self):
        '''display plugin infos'''
        pp.prettyPrint("\n",GREY)
        pp.prettyPrint("    PLUGIN INFOS" ,YELLOW)
        pp.prettyPrint("    ============" ,GREY)
        pp.prettyPrint("        PARAMETER       VALUE" ,YELLOW)
        pp.prettyPrint("        "+"-"*15 + " " + "-"*20 ,GREY)
        for info in plugin.infos:
            param = info[0]
            value = info[1]
            pp.prettyPrint("        %-15s"%param ,CYAN ,0)
            pp.prettyPrint("%-s"%value ,PURPLE)
        pp.prettyPrint("\n",GREY)

    def getOptions(self):
        options = []
        for opt in plugin.opts:
            options.append(opt[0])
        return options

    def showOptions(self):
        '''display plugin options'''
        pp.prettyPrint("\n",GREY)
        pp.prettyPrint("    PLUGIN OPTS" ,YELLOW)
        pp.prettyPrint("    ===========" ,GREY)
        pp.prettyPrint("        %-15s %-20s %-40s"%("PARAMETER" ,"VALUE" ,"DESCRIPTION") ,YELLOW)
        pp.prettyPrint("        %-15s %-20s %-40s"%("-"*15 ,"-"*20 ,"-"*40) ,GREY)
        for opt in plugin.opts:
            param = opt[0]
            value = opt[1]
            desc = opt[2]
            pp.prettyPrint("        %-15s"%param ,CYAN ,0)
            pp.prettyPrint("%-20s"%value, PURPLE, 0)
            pp.prettyPrint("%-20s"%desc , GREEN)
        pp.prettyPrint("\n",GREY)

    def setParam(self ,param ,value):
        '''set plugin par value'''
        param = param.upper()
        pp.prettyPrint("[*] SET %s=>%s"%(param ,value) ,YELLOW)
        code  = 'global %s\n'%param
        code += '%s="%s"'%(param ,value)
        exec(code)

    def getOption(self,option):
        '''get plugin opt'''
        res = 'FALSE'
        option = option.upper()
        for opt in plugin.opts:
            param = opt[0]
            value = opt[1]
            desc = opt[2]
            if option == param:
                res = value
        return res.upper()

    def checkParam(self,param):
        res = False
        param = param.upper()
        for opt in plugin.opts:
            if param == opt[0]:
                res = True
                break
        return res

    def exploit(self):
        '''start exploit !!'''
        try:
            global exploitModule 
            exploitModule = exploitModule()
        except:
            pass
        pp.prettyPrint("[*] Start exploit.." ,YELLOW)
        plugin.exploit()

    def pluginHelp(self):
        '''plugin help menu'''
        pp.prettyPrint("\n",GREY)
        pp.prettyPrint('   PLUGIN HELP MENU' ,YELLOW)
        pp.prettyPrint('   ================' ,GREY)
        pp.prettyPrint('        Command         Description' ,YELLOW)
        pp.prettyPrint('        -------         -----------' ,GREY ,0)
        pp.prettyPrint('''
        help            Displays the plugin menu
        info            Displays the plugin info
        show            Displays the plugin options
        set             Configure the plugin parameters
        exploit         Exploit the target
        cls             Clear the screen
        back            Back to NSS Main''' ,CYAN)
        pp.prettyPrint('    PLUGIN SET HELP' ,YELLOW)
        pp.prettyPrint('    ===============' ,GREY)
        pp.prettyPrint('        Command         Description' ,YELLOW)
        pp.prettyPrint('        -------         -----------' ,GREY,0)
        pp.prettyPrint('''
        <PARAMETER>     Set parameter''' ,CYAN)
        pp.prettyPrint("\n",GREY)

    def cls(self):
        '''clear the screen'''
        if  name == 'nt':
            system("cls")
        else:
            system("clear")

if __name__ == '__main__':
    print __doc__

