# -*- coding: utf-8-*-
class NSSPlugin:
    '''Mongodb_scanner'''
    infos = [
        ['Plugin','Mongodb_scanner'],
        ['Author','jadore'],
        ['Update','2014/07/23'],
        ['Site','http://www.jaodre.wang'],
        ]
    opts  = [
        ['RHOSTS','127.0.0.1','Target IPS'],
        ['RPORT','27017','Target Port'],
        ['PING',"true",'Enable/disable host pings before attempting connection'],
        ['IPFILE','','Target IP File'],
        ]
    def exploit(self):
        mongodb = mongodbModule()
        success = []
        ipList = []
        
        subnet = RHOSTS
        port = int(RPORT)
        if PING.lower() == "false":
            ping = False
        else:
            ping = True

        try:
            for ip in ipcalc.Network(subnet):
                ipList.append(str(ip))
        except:
            pp.prettyPrint("Not a valid subnet.",YELLOW)
            return
            
        if IPFILE != "":
            loadPath = IPFILE
            try:
                with open (loadPath) as f:
                        ipList = f.readlines()
            except:
                pp.prettyPrint("Could not open the file",YELLOW)
                return
    
        if ping :
            pp.prettyPrint("[+]Scan will ping host before connection attempt.",GREEN)
        else:
            pp.prettyPrint("[+]Scan will not ping host before connection attempt.",GREEN)

        for target in ipList:
            result = mongodb.accessCheck(target.rstrip(),port,ping)

            if result[0] == 0:
                Str = "Successful default access on " + target.rstrip() + "(Mongo Version: " + result[1] + ")."
                pp.prettyPrint(Str,GREEN)
                success.append(target.rstrip()+","+result[1])
            elif result[0] == 1:
                Str = "MongoDB running but credentials required on " + target.rstrip() + "."
                pp.prettyPrint(Str,GREEN)
                success.append(target.rstrip()+","+"Credentials Required!") #Future use
                
            elif result[0] == 2:
                Str = "Successful MongoDB connection to " + target.rstrip() + " but error executing command."
                pp.prettyPrint(Str,GREEN)
                success.append(target.rstrip()+","+"Failed Exec Command!") #Future use
            
            elif result[0] == 3:
                Str = "Couldn't connect to " + target.rstrip() + "."
                pp.prettyPrint(Str,YELLOW)
            
            elif result[0] == 4:
                Str = target.rstrip() + " didn't respond to ping."
                pp.prettyPrint(Str,YELLOW)
                
        pp.prettyPrint("Discovered MongoDB Servers ",GREEN)
        pp.prettyPrint("IP" + " " + "Status",GREEN)
        saveList = []
        saveList.append("IP Address,MongoDB Version\n")
        outCounter= 1
        for server in success:
            [ip,status] = server.split(",")
            Str = str(outCounter) + "-" + ip + " " + status
            saveList.append(Str)
            pp.prettyPrint(Str+"\n",GREEN)
            outCounter += 1

        exploitModule.writeLog("mongodb_scanner",saveList)
        pp.prettyPrint("[+]Scan results saved!",GREEN)
