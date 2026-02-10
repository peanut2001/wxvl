#  【威胁监测】微信 for Linux存在RCE执行风险  
原创 威胁监测
                    威胁监测  Gaobai文库   2026-02-10 07:51  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sCWibOw4q81QHMibHl2cM21YT2F75aVEPWGVVFGWD6pBVsTicKGiaZHIrErT6xiaa84eiaphMwpPZtzLgpXYr9DLrSJfS14leY0CJVa755Jsga3Bs/640?wx_fmt=png&from=appmsg "")  
  
*本文所述技术内容仅供安全研究与学习交流之用，任何操作均与本公众号及作者无关。信息来源于互联网公开渠道整理  
## 0x00 事件背景  
  
           
微信Linux版存在文件名处理不当引发的RCE命令执行漏洞，攻击者可通过恶意文件名实现命令执行。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sCWibOw4q81Rsg7e7HxNrE1icHIUNv3m1ptMTejoibYrUMCQxI4NHZTt8VupH2y9HKgicAG2xAlcKIcZSvOu5mB1opky3VDQP8PUJl2JmicEwndQ/640?wx_fmt=png&from=appmsg "")  
  
*图片来源公开信息查询  
## 0x01 影响版本  
- ****  
**【未知】**  
  
## 0x02 复现详情  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/sCWibOw4q81Smj4eVaHShrM3Z1veKuehwFm1ogFsAseZkeIu1VnokRiclGicgpjMjvdJaLKnVqQc4be4fj6CdVCA418vVFSeL8CdtYaGeAl4Cs/640?wx_fmt=png&from=appmsg "")  
  
*特殊符号包裹构造的文件名，可直接造成执行效果  
  
## 关注及时推送最新安全威胁资讯！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I1c6evzliamKaSak4bn0ryE59PT2Tgiad7LnLT0HgErDab57xElwBDClPxFHFdkHxWxMz4BeSVuicKmAwOR6cYFxw/640?wx_fmt=png&from=appmsg "")  
**「由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责，EXP 与 POC 仅仅只供对已授权的目标使用测试，对未授权目标的测试本文库不承担责任，均由本人自行承担。本文库中的漏洞均为公开的漏洞收集，若文库中的漏洞出现敏感内容产生了部分影响，请及时联系作者删除漏洞。」**  
  
