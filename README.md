nosqlsploit
===========

nosql attack platform

首先感谢MST与nosqlmap的作者


这个框架，重构了MST的代码，让操作尽可能的方便些
在nosqlmap的基础上，对mongodb的审计模块化，使其操作方便。
类似msf的操作，更容易被人接受

安装：
  需要安装一下模块：
  mongodb
  pymongo
  ipcalc

模块介绍：
1.mongodb scanner：
  扫描一个ip端或者一个ip文件，检测是否安装mongodb服务
2.mongodb net attack：
  针对一个mongodb做安全配置的审计
  
开发起源于这篇文档http://drops.wooyun.org/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/2470
