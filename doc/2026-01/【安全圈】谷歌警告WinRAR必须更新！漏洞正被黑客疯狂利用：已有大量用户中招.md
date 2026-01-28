#  【安全圈】谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招  
 安全圈   2026-01-28 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
日前谷歌威胁情报小组（GTIG）发布全球性安全预警，  
**指出去年发现的WinRAR高风险漏洞（CVE-2025-8088）正在被黑客大规模利用，且目前已出现大量中招案例。**  
  
虽然官方已在7.13版本中修复了该问题，但仍有大量用户因未及时更新而面临系统被全面控制的风险。  
  
![谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaWwR1QrX8pvJM6qE2XiaLJK8JeibAKmwKsvJ0I5ptG6BqRRZZR19LX8aUoxMyYlHr0kRfkzKKNEjKA/640?wx_fmt=png&from=appmsg "")  
  
据谷歌介绍，WinRAR 7.12及更早版本存在严重漏洞，攻击者可利用该漏洞在解压时错误地将文件写入系统目录，最终实现恶意代码执行并获取系统控制权，该漏洞在CVSS中的得分为 8.4/10，属于高风险等级。  
  
攻击的核心机制是利用Windows系统的“备用数据流”（ADS）特性进行路径遍历攻击，通常情况下，黑客会将恶意文件隐藏在压缩包内诱饵文件的ADS中。  
  
**当用户查看诱饵文件时，WinRAR会在后台通过目录遍历，将恶意负载（如LNK、HTA、BAT或脚本文件）解压并释放到任意位置。**  
  
黑客最常选择的目标是Windows的 “启动（Startup）”文件夹，从而确保恶意软件在用户下次登录时自动执行，实现长期潜伏。  
  
谷歌指出，目前包括UNC4895（RomCom）、APT44以及Turla在内的多个知名黑客组织正积极利用该漏洞。  
  
攻击者主要通过鱼叉式网络钓鱼，将恶意RAR附件伪装成“求职简历”或“发票”，投放包括Snipbot、Mythic Agent在内的各类后门木马，受害者涵盖金融、制造、国防及物流等多个重要领域。  
  
**由于WinRAR没有自动更新功能，许多用户可能仍在使用易受攻击的旧版本，建议手动将版本升级至WinRAR 7.13或更高版本。**  
  
![谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaWwR1QrX8pvJM6qE2XiaLJK6X8tcrKw3ia4lVZlolrzGIdmNkrKJbiaVu3IAlk03WXoxUSSN1A1iaw4g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】东营网警侦破一起金融借贷领域非法获取公民个人信息案](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073876&idx=1&sn=146711e5f26f23ce33059afd4c20ff37&scene=21#wechat_redirect)  
  
  
  
[【安全圈】千万当心！B站涌现大量新号散播病毒：发视频宣传带毒图吧工具箱](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073876&idx=2&sn=013c66a27179f831a6704ded07785d16&scene=21#wechat_redirect)  
  
  
  
[【安全圈】1.49 亿条 96GB 密码泄露，影响谷歌、苹果、Meta 等公司用户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073876&idx=3&sn=e954a04f42dfe037fa5d18648040521c&scene=21#wechat_redirect)  
  
  
  
[【安全圈】这些密码真别用了！60亿条泄露数据揭示：123456仍居榜首](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073860&idx=1&sn=f951c01f5be15e41b398b6c2495d7191&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
  
  
