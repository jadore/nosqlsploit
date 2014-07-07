
class mstplugin:
    '''I'm d3'''
    infos = [
        ['NAME','Crack Windows-nt Hash(objectif-securite)'],
        ['AUTHOR','D3'],
        ['UPTIME','20131024'],
        ['WEBSITE','1024 U know :)']
        ]
    opts  = [
        ['HASH','Guest:501:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::','WINDOWS-HASH'],
        ['PAYLOAD','FALSE','NO PAYLOAD :)']
        ]
    def exploit(self):
        url = "http://www.objectif-securite.ch/en/ophcrack.php"
        ntt = HASH.split(":")
        val = {"hash":ntt[2]}
        try:
            
            color.cprint("[+] Crack `%s`"%ntt[0],YELLOW)
            res = fuck.urlpost(url,val).read()
            tmp = fuck.find(r'</td><td><b>.+</b></td></tr>',res)
            ok  = tmp[0][12:(len(tmp)-15)]
            color.cprint("[*] %s"%ok,GREEN)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)
