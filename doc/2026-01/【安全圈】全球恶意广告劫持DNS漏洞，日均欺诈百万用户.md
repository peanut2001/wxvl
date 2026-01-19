#  【安全圈】全球恶意广告劫持DNS漏洞，日均欺诈百万用户  
 安全圈   2026-01-19 11:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
DNS劫持  
  
  
![banner](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgbTKe7RgQTtMibFtEGpUY6Xf3BiaaUglEdYDCNWspngu6xlpgDxG91Il06H7ReibDN30MPTgdrJiaic5w/640?wx_fmt=jpeg&from=appmsg "")  
  
Infoblox研究人员揭露了一个庞大的欺诈性推送通知网络，展示了薄弱的DNS管理规范与"坐以待毙"（Sitting Ducks）漏洞如何助长全球欺诈广告生态。最新报告详细记录了研究团队如何"黑吃黑"——通过控制被遗弃的域名来监听数百万条恶意通知。  
## 漏洞利用与域名劫持  
  
调查始于名为"坐以待毙"的攻击漏洞，威胁行为者通过认领已被原所有者放弃但仍保持活跃DNS委派的域名来实施攻击。Infoblox研究人员发现，某大型推送通知运营商遗留了大量存在此漏洞的域名。  
  
"我们采用DNS技术，通过在DNS提供商处简单认领就控制了被威胁行为者遗弃的域名...这并非中间人（AiTM）攻击，我们实际上是从侧面介入了威胁行为者的运营。"研究人员解释道。  
## 海量数据收集与分析  
  
注册这些被忽视的域名后，研究人员被动接收了大量仍试图连接攻击者基础设施的受害设备流量。"一天之内，我们的收集范围从一个域名扩展到近120个，"报告指出，"数千台受害设备连接到我们的服务器，每秒产生30MB的日志数据。"  
  
两周内收集的5700多万条日志数据，揭示了一个旨在用欺诈诱饵轰炸用户的自动化运营体系。受害者主要为Android Chrome用户，平均每天收到140条通知。  
## 全球分布与欺诈手法  
  
虽然活动覆盖全球60多种语言，但目标明显偏向南亚地区。"孟加拉国、印度、印尼和巴基斯坦占全部流量的50%，"分析显示。  
  
这些通知内容极具欺骗性，利用恐惧、贪婪和"点击诱饵"诱骗用户。"通知主题运用欺骗、恐惧和希望诱导用户点击链接，包括冒充Bradesco、Sparkasse、Recibiste、万事达卡、Touch 'n Go和GCash等正规金融服务。"  
  
其他诱饵更具掠夺性，包括虚假病毒警报（"您的设备已被入侵"）、涉及埃隆·马斯克等公众人物的捏造新闻丑闻，以及成人内容诈骗链接。  
## 低效却持续的黑产运营  
  
尽管垃圾信息数量庞大，该运营的盈利能力却出奇低下。研究人员估计，攻击者从观测流量中每日仅获利约350美元。点击率（CTR）更是惨淡，平均仅为六万分之一。  
  
"其目标并非向更可能参与的用户投放广告，而是试图欺骗人们...让广告商网站流量看似增长，"报告指出。  
## DNS管理的重要警示  
  
这项研究不仅揭示了联盟欺诈广告的阴暗世界，也为基础设施管理敲响警钟。"坐以待毙"漏洞仍是攻击者的有力工具，使其能够劫持合法声誉用于恶意目的。  
  
"虽然我们'解救'了这些恶意域名，但其他恶意行为者每天都在使用相同技术从合法组织获取休眠域名。"研究人员强调，这不仅关乎诈骗者，合法组织若未能清理DNS记录同样面临风险。  
  
报告总结道："从技术上讲，DNS管理是域名所有者的责任。这就像有人把玩具遗落在人行道上，被别人捡走了。这该怪谁呢？"  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】入侵网站盗数据、跨境牟利触法网！两名犯罪嫌疑人被云南网警抓获](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073771&idx=1&sn=f40e6765178c09dd4319da1c93330a83&scene=21#wechat_redirect)  
  
  
  
[【安全圈】潜伏 5 年、装机量超 84 万！这款浏览器恶意插件竟靠一张图片瞒天过海](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073771&idx=2&sn=b7cb1159c7de9fcf266ecd01456c42cc&scene=21#wechat_redirect)  
  
  
  
[【安全圈】32 万人信息遭泄露！这所大学曝重大数据窃密案，黑客潜伏近两周竟无人察觉](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073771&idx=3&sn=3f6177eb95fabe01904baf7439660f0e&scene=21#wechat_redirect)  
  
  
  
[【安全圈】男子利用购物平台漏洞窃取用户信息并骗取佣金1878万被判刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073757&idx=1&sn=b7baabf15c246b7188cec3311d4fcb74&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
