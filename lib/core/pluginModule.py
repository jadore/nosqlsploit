'''
'''
from prettyPrint import *
from prettyPrint import prettyPrint as pp
from exploitModule import *
from os         import path,system

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
        pp.prettyPrint("PLUGIN INFOS" ,YELLOW)
        pp.prettyPrint("============" ,GREY)
        pp.prettyPrint("PARAMETER       VALUE" ,YELLOW)
        pp.prettyPrint("-"*15 + " " + "-"*20 ,GREY)
        for info in plugin.infos:
            param = info[0]
            value = info[1]
            pp.prettyPrint("%-15s"%param ,CYAN ,0)
            pp.prettyPrint("%-s"%value ,PURPLE)

    def showOptions(self):
        '''display plugin options'''
        pp.prettyPrint("PLUGIN OPTS" ,YELLOW)
        pp.prettyPrint("===========" ,GREY)
        pp.prettyPrint("%-15s %-20s %-40s"%("PARAMETER" ,"VALUE" ,"DESCRIPTION") ,YELLOW)
        pp.prettyPrint("%-15s %-20s %-40s"%("-"*15 ,"-"*20 ,"-"*40) ,GREY)
        for opt in plugin.opts:
            param = opt[0]
            value = opt[1]
            desc = opt[2]
            pp.prettyPrint("%-15s"%param ,CYAN ,0)
            exec('pp.prettyPrint("%-20s"%' + "%s"%param + ', PURPLE, 0)')
            pp.prettyPrint("%-40s"%desc ,GREEN)
        if self.checkPayload(PAYLOAD) == "TRUE":
            pp.prettyPrint("PAYLOAD OPTS" ,YELLOW)
            pp.prettyPrint("============" ,GREY)
            pp.prettyPrint("%-15s %-40s"%("PARAMETER" ,"DESCRIPTION") ,YELLOW)
            pp.prettyPrint("%-15s %-40s"%("-"*15 ,"-"*40) ,GREY)
            code = open("plugins/payload/" + PAYLOAD + ".py").read()
            exec(code)
            try:
                exec("global NSSPayload")
            except:
                pass
            for opt in NSSPayload.opts:
                param = opt[0]
                desc = opt[1]
                pp.prettyPrint("%-15s"%param ,CYAN ,0)
                pp.prettyPrint("%-40s"%desc ,PURPLE)

    def setParam(self ,param ,value):
        '''set plugin par value'''
        param = param.upper()
        if param == 'PAYLOAD':
            if value.upper() == "FALSE":
                code  = 'global PAYLOAD;PAYLOAD="false";'
                exec(code)
                pp.prettyPrint("[*] Disabled PAYLOAD !" ,YELLOW)
            elif self.checkPayload(value) == 'TRUE' and self.getOption("PAYLOAD") != "FALSE":
                pp.prettyPrint("[*] SET PAYLOAD=>%s"%value ,YELLOW)
                code  = 'global PAYLOAD\n'
                code += 'PAYLOAD="%s"'%value
                exec(code)
            else:
                pp.prettyPrint("[!] SET PAYLOAD FALSE !" ,RED)
        else:
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
            global run 
            run = exploitModule()
        except:
            pass
        pp.prettyPrint("[*] Start exploit.." ,YELLOW)
        plugin.exploit()

    def checkPayload(self,payload):
        '''check payload exists'''
        ok = 'no'
        payloadFile = "plugins/payload/%s.py"%payload
        if payload == '' or payload.upper() == 'FALSE':
            ok = 'false'
        if path.exists(payloadFile):
            ok = 'true'
        return ok.upper()

    def pluginHelp(self):
        '''plugin help menu'''
        pp.prettyPrint('PLUGIN HELP MENU' ,YELLOW)
        pp.prettyPrint('================' ,GREY)
        pp.prettyPrint('        Command         Description' ,YELLOW)
        pp.prettyPrint('        -------         -----------' ,GREY ,0)
        pp.prettyPrint('''
        help            Displays the plugin menu
        back            Back to NSS Main
        cls             Clear the screen
        info            Displays the plugin info
        show            Displays the plugin options
        set             Configure the plugin parameters
        exploit         Start plugin to exploit''' ,CYAN)
        pp.prettyPrint('PLUGIN SET HELP' ,YELLOW)
        pp.prettyPrint('===============' ,GREY)
        pp.prettyPrint('        Command         Description' ,YELLOW)
        pp.prettyPrint('        -------         -----------' ,GREY,0)
        pp.prettyPrint('''
        PAYLOAD         Set payload
        <PARAMETER>     Set parameter''' ,CYAN)

    def cls(self):
        '''clear the screen'''
        if  name == 'nt':
            system("cls")
        else:
            system("clear")

if __name__ == '__main__':
    print __doc__

