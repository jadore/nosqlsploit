# -*- coding: utf-8 -*-
'''
MstCache=>class
For main's some func or other~
update:2013/10/26
'''

from MstColor import *
from sqlite3 import *
from os import listdir,system
from random import choice
from MstLoad import load
from banner.banner   import banner

class DB:
    def __init__(self):
        self.conn = connect('db/nosqlsploit.db')
        self.plugin = 'plugins'
        self.mongodb = 'mongodb'

    def initDB(self):        
        self.execSQL("create table if not exists nosqlsploit(id integer primary key,type text,path text)")
        self.execSQL("delete from nosqlsploit")
        self.insertToDB(self.getPlugins(self.mongodb),self.mongodb)

    def insertToDB(self,plugins,dbType):
        '''insert data to DB'''
        for plugin in plugins:
            plugin = plugin[:len(plugin)-3]
            self.execSQL('insert into nosqlsploit(type,path) values("%s","%s/%s")'%(dbType,dbType,plugin))

    def execSQL(self,sql):
        '''execute a sql'''
        conn.execute(sql)
        conn.commit()
        
    def getplugins(self,path):
        '''get plugins list'''
        return listdir(self.plugin+path)
    
    def fetchAll(self,sql):
        '''sqlite3=>cur.fetchall()'''
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res
    
    def searchPlugin(self,keyword):
        '''search plugins'''
        sql = 'select * from nosqlsploit where path like "%'+keyword+'%"'
        result = self.fetchAll(sql)
        msg = "SEARCH '%s'"%keyword
        color.cprint(msg,YELLOW)
        color.cprint("="*len(msg),GREY)
        self.showSearchResult(result)
        
    def showSearchResult(self,result):
        '''format print results'''
        color.cprint("%5s %-60s %-7s"%("ID","PATH","TYPE"),YELLOW)
        color.cprint("%5s %-60s %-7s"%("-"*5,"-"*60,"-"*7),GREY)
        for res in result:
            pluginId = res[0]
            pluginType = res[1]
            pluginPath = res[2]
            if len(pluginPath)>70:
                pluginPath = pluginPath[:68]+".."
            color.cprint("%5s %-60s %-7s"%(pluginId,pluginPath,pluginType),CYAN)
        color.cprint("="*74,GREY)
        color.cprint("COUNT [%s] RESULTS (*^_^*)"%len(result),GREEN)
        
    def showPlugins(self,pluginType):
        '''show plugins'''
        pliginStr = ("show %s plugins"%pluginType).upper()
        color.cprint(pluginStr,YELLOW)
        color.cprint("="*len(pluginStr),GREY)
        if pluginType.lower() == 'all':
            sql = 'select * from nosqlsploit'
        else:
            sql = "select * from nosqlsploit where type='%s'"%pluginType
        self.showSearchResult(self.fetchAll(sql))
                
    def getPluginNums(self,pluginType):
        '''get plugins nums'''
        if pluginType == 'all':
            return len(self.fetchAll('select * from nosqlsploit'))
        else:
            return len(self.fetchAll('select * from nosqlsploit where type="%s"'%pluginType))

class banner:
    def __init__(self):
        self.version = '1.0'
        self.mongodb = 'mongodb'

    def ban1(self):
        '''banner 1'''
        color.cprint('''
             ,,          ,      r22r   r::,,:iii   
             B@B       ,@@2   @B@GB@@ rB@B@B@B@B   
             @H@s      @X@s  @B           X@       
             @:,@,    @G Bs  i@B:         GB       
             @r M@   GB  @s    XB@Br      G@       
             Bs  B@ iB,  @s       sB@     MB       
             @s   BSBs   @s        2Bi    M@       
             B9   ;B@   ,BH  B@BMG@BG     @B       
             :     ,     :    ,r22i       ,:
            ''',RED)

    def ban2(self):
        color.cprint('''
                                                                    
                                   ,i77SSXrr,     ,ii               
                            7aWMMMMMMMMMMMMMMMMMMMMMMM              
                        7@MMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                        WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                        ,MMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                         ,MMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                          @MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                          XMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           BMMMMMMMMMMMMMMMMMMMMMMMMMMr             
                           SMMMMMMMMMMMMMMMMMMMMMMMMMMM             
                           iMMMMMMMMMMMMMMMMMMMMMMMMMMMX         7; 
                            MMMMM@B8Z2SXXr;;;:,.,,. . . ,;XZBMMMMMM:
                            S7,.   ..::ii;;7XXX2ZBB@MMMMMMMMMMMMMMMi
                      .:;72aZ8B@MMMMMMMMMMMMMMMMMMMMMMMMMMBaXi.     
              BMMMMMMMMMMMMMMMMMMMMM8a22SXrr;i,:rZZZi               
              XMMMMMWB0Za2X;,:MMMMMWS          7WM.             
                 
''',BLUE)

    def ban3(self):
        color.cprint('''
                                        ,-,                     
                                   -x#######=                   
                                =########XX##+                  
                             .x#########XxXx#x=                 
                            X###########XxxXX#=-                
                          .##########X####Xxxxx=                
                          =###XXxX+xX#X##########x=-            
                          +#XxxX#######################=.       
                         -###########X++x+--;+x###########-     
                       =#########X;.  .         ;-X#########.   
                     +#########+,    ,      ,   .  ;#########   
                   -#########- .    -      -.   ..  ;+#######,  
                  =########+,      =;.    --     -  ..=#####+   
                 .########-    .; =;    ,+- .   X ;  ,.X##x     
                 +#######+ ;   -.-.    =+.    .#. = , .#x       
                 ,#######----  = ,   ;+,    .x# ,X, - ;x#       
                  .#######+--= =    ==   ;=-,, -X#===.x=##      
                     ;+X#=-x+=;-  X#+,.,+++X=-#;  ,;;x+#-.-     
                        -   ####x#==--+-., X-.X;=#+; =x#        
                       .; -+-##. -  X##=   =  .,X#+  -#,        
                        =     x   +       ,.   ;     x=         
                         ;-,, +    -;...,.       ..;-x          
                            .##=                     x          
                             +  =                   -;          
                                 +                -+.           
                                  =X+,.        ,==,   
                                           ''',CYAN)

    def ban4(self):
        color.cprint('''
                             .;+it+;+tt=:                       
                          .iYi;=YY   .IXXXI;                    
                        :IXV,     iX   t+iRBV,                  
                       IVItY  ,#; =#     ,  Y#=                 
                     .XIttIt,  Mi.XV#I ,; ,.  :i                
                     RttYI,  .   :###Y  ,;..., +:               
                    YItI=  .,,:    .           =: :::           
                    Xtt+ ...             :=Y#I .i;,,:+,         
                    RtI      ,=itYRM#########   V     I         
                    XIt  ::#################;  ;R,   =;         
                    iYI    B###BRXVYVVVVBW#X   tVItiV.          
                     VIi    +BBRVVVVVVYVVBI    ItttB:           
                  ::,.YY;     +XWMMRRRRBB;    tttiVi            
                ,+,. ,:iV=       ;iIIIII:,IM##XtiYY             
                t.    ,tXBt.       :IRMt=XR,  tIYI              
                ,+.   +titIYt;=RW#WRt;:;;M=    Vt .;::          
                 .;;=YRItittttXBX:     ,:::   ,;V,,..,+;        
                      ,iYVItttitt             ;,=      +;       
                         ,iYVItiI ,           :         t       
                            .;Ytt; ;        .,.t        =:      
                              :VtI; ...   ..,:IY        i.      
                              ;YttII=;:::;=iIIIIt      :+       
                             = ItittttIIIIIYXVYYVY=:::==        
                            :; tIttttttIYXI=,      ,,,          
                            =:  tYIIIIVI=                       
                            ,+   .,:.i,                         
                             ==     ;,                          
                              ,;;;;:                            
''',PURPLE)

    def banner(self):
        '''nosqlsploit banner :)'''
        mongodbNum = self.getPluginNums(self.mongodb)
        choice([self.ban1,self.ban2,self.ban3,self.ban4])()
        print '          =[',
        color.cprint('NSS::nosqlsploit ',GREEN)                  
        print '        -+=[',
        color.cprint('VER::%s'%self.version,CYAN)                
        print '    + -- +=[',
        color.cprint('PLUGINs::%s::%s'%(self.mongodb,mongodbNum),YELLOW)
        
class nosqlTools:
    def __init__(self):
        self.logo = 'NoSqlSploit'

    def printLogo(self):
        '''print mst..'''
        color.cprint(self.logo,GREY,0)
        
    def exeCMD(self,cmd):
        '''run system command'''
        color.cprint('[*] EXEC:%s'%cmd,RED)
        system(cmd)
        
    def cls(self):
        '''clear'''
        if name == 'nt':
            system("cls")
        else:
            system("clear")

    def errmsg(self,msg):
        '''show error msg'''
        color.cprint("[!] Err:%s"%msg,RED)
        
    def mainexit(self):
        '''exit app'''
        color.cprint("\n[*] GoodBye :)",RED)
        exit(0)

    def start(self):
        '''start cache'''
        color.cprint("[*] Start mst ..",GREEN)
        self.banner()
        
            
    #以上是获取payload的路径并写入数据库
    def load(self,plugin):
        '''load plugins'''
        def getplu(pid):
            '''pid 2 pluName'''
            conn=connect(mstdb)
            cur=conn.cursor()
            cur.execute('select * from mst where id=%s'%pid)
            tmp=cur.fetchone()
            cur.close()
            conn.close()
            pat=tmp[2]
            pty=tmp[1]
            if pty == 'payload':
                return ''
            else:
                return pat
        def noload(p=0):
            '''no this plugin | plugin is payload'''
            if p == 0:
                color.cprint("[!] NO THIS PLUGIN !",RED)
            else:
                color.cprint("[!] IT'S A PAYLOAD !",RED)
        try:
            pid=int(plugin)
            if len(self.sql_all('select * from mst where id=%s'%pid))==0:
                noload()
            else:
                plu=getplu(pid)
                if len(plu)>0:
                    pt=plu.split("/")[0]
                    load.start(pt,plu)
                else:
                    noload(1)
        except:
            if len(self.sql_all('select * from mst where path="%s"'%plugin))==0:
                noload()
            else:
                pt=plugin.split("/")[0]
                load.start(pt,plugin)

    def mainhelp(self):
        '''show mainhelp'''
        color.cprint('MST HELP MENU',YELLOW)
        color.cprint('=============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        help            Displays the help menu
        exit            Exit the MstApp
        cls             Clear the screen
        show            List the plugins
        search          Search plugins
        use             Use the plugin
        update          Update mst|plugins''',CYAN)
        color.cprint('MST HELP::SHOW',YELLOW)
        color.cprint('==============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        exploit         List the exploit plugins
        payload         List the payload plugins
        multi           List the multi plugins
        all             List all the plugins''',CYAN)

    def usage(self,c):
        '''mst=>usage'''
        def ius(c):
            '''def's def =.='''
            color.cprint('[?] USAGE:%s'%c,YELLOW)
        if   c == "search":
            ius('search <plugin>')
        elif c == "show":
            ius('show <exploit|payload|multi|all>')
        elif c == "use":
            ius('use <plugin|pluginID>')
        elif c == "update":
            ius('update <mst|plugins>')

if __name__=='__main__':
    print __doc__
else:
    cache=cache()
