# -*- coding: utf-8 -*-

from prettyPrint import *
from tools import *
from os import listdir,system
from random import choice
from db import DB

class banner:
    def __init__(self):
        self.version = '1.0'
        self.mongodb = 'mongodb'

    def ban1(self):
        '''banner 1'''
        prettyPrint.prettyPrint('''
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
        prettyPrint.prettyPrint('''
                                                                    
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
        prettyPrint.prettyPrint('''
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
        prettyPrint.prettyPrint('''
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

    def main(self):
        '''nss banner '''
        db = DB()
        mongodbNum = db.getPluginNums(self.mongodb)
        choice([self.ban1,self.ban2,self.ban3,self.ban4])()
        print '          =[',
        prettyPrint.prettyPrint('NSS::NoSqlSploit ',GREEN)                  
        print '        -+=[',
        prettyPrint.prettyPrint('VER::%s'%self.version,CYAN)                
        print '    + -- +=[',
        prettyPrint.prettyPrint('PLUGINS::%s::%s'%(self.mongodb,mongodbNum),YELLOW)
        
if __name__=='__main__':
    print __doc__
else:
    ban = banner()
