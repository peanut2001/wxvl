#  新Shiro反序列化漏洞一站式综合利用工具  
FightingLzn9
                    FightingLzn9  夜组安全   2026-01-22 00:02  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**NightCTI**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
## 工具介绍  
  
ShiroExploit，是一款Shiro反序列化漏洞一站式综合利用工具。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5foWCe1dVSqyYExiaDCq98ehsYiakG9ib6SibKda50SeSEY0ibsI8zR7XrDg/640?wx_fmt=png&from=appmsg "")  
## 工具功能  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s59bcsf5gscc7TIj5ajN5GxeaIz1T9L3gyalk0g2WNywTcyhKNHXibicqA/640?wx_fmt=png&from=appmsg "")  
  
1、区分ShiroAttack2，采用分块传输内存马，每块大小不超过4000。  
  
2、可打JDK高版本的shiro，确保有key、有gadget就能rce。  
  
3、依托JavaChains动态生成gadget，实现多条利用链，如CB、CC、Fastjson、Jackson。  
  
4、通过魔改MemshellParty的内存马模板，使其回显马通信加密，去除一些典型的特征。  
  
5、借助JMG的注入器，加以魔改，实现无侵入性，同一个容器可同时兼容多种类型的内存马。  
  
6、对内存马和注入器类名进行随机化和Lambda化处理，规避内存马主动扫描设备的检测。  
  
7、可以更改目标配置，如改Key、改TomcatHeaderMaxSize。  
  
8、采用URLDNS链和反序列化炸弹的方式来探测指定类实现利用链的探测。  
  
9、缺点是流量相对大一些。  
## 功能演示  
  
JDK18场景下实现命令执行和打入多种内存马。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5kUhkgZhRdicibKicTSGAFmicgzIa7P5MfEMF7QCLhfplLJxK2YZu6Twmsg/640?wx_fmt=png&from=appmsg "")  
  
跑key。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5foWCe1dVSqyYExiaDCq98ehsYiakG9ib6SibKda50SeSEY0ibsI8zR7XrDg/640?wx_fmt=png&from=appmsg "")  
  
探测利用链。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5flLMUcPYVm63myssLiaR8icBfVIaEkicRmWQibvFpZRrbDFZ5ux5aziahWA/640?wx_fmt=png&from=appmsg "")  
  
命令执行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5nOYaTbsVbIt8DccULa0wxk6lKOhENdv6ssZUUH2uzOJtKQuRlpcopA/640?wx_fmt=png&from=appmsg "")  
  
打入Godzilla内存马（支持Behinder内存马）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5icibNlSFD9BHLtmWRGXQvFArTFiaZbr2BQvsgu4MjtLZrBwQCv1etiaI8A/640?wx_fmt=png&from=appmsg "")  
  
打入SUO5V2内存马。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5UvIHSM9bzQmfmJZqQKqlUrxic1Ciana4zkGGuic48ZliaCZRCFqKoLUBnQ/640?wx_fmt=png&from=appmsg "")  
  
支持Tomcat10及以上的内存马。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIRDCPwyvn1Vg58IfWQ0s5SBqUY8ickcmUUgp3gWZVUQZxG7Aiae23yXg5fibGd60boXzLYZ37elsSA/640?wx_fmt=png&from=appmsg "")  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260122  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[【红队】一款专业的多协议漏洞利用与攻击模拟平台2026-01-21](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496145&idx=1&sn=38b1287a667573c09ed4f056afc64b4c&scene=21#wechat_redirect)  
[流量之眼 - 智能被动漏洞扫描平台2026-01-20](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496127&idx=1&sn=b2e9109847a88c84ac808305babaeb8a&scene=21#wechat_redirect)  
[XSS 漏洞练习靶场，覆盖反射型、存储型、DOM 型、SVG、CSP、框架注入、协议绕过等多种场景2026-01-19](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496120&idx=1&sn=f2153c748593255cb40ae6f8e50a3ab8&scene=21#wechat_redirect)  
[一款自动化403/401绕过工具 | 请求头注入、谓词篡改等多种实战技巧2026-01-16](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496113&idx=1&sn=6e48fa8ac465f65cffbe9753de1b9c7f&scene=21#wechat_redirect)  
[Burp Suite插件 | 高级HTTP头修改安全头来绕过安全限制、不同来源或设备的请求2026-01-12](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496101&idx=1&sn=731e9d4fa9782a4bfdcc8622d4bf16b9&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
