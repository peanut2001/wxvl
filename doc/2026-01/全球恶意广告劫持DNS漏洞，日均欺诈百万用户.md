#  全球恶意广告劫持DNS漏洞，日均欺诈百万用户  
 FreeBuf   2026-01-20 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![banner](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9iblQcFqePkn3BWCdEetLia3PDibiamo4zg6qck5PbCpB1TLb7TLicPpzEr4g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Infoblox研究人员揭露了一个庞大的欺诈性推送通知网络，展示了薄弱的DNS管理规范与"坐以待毙"（Sitting Ducks）漏洞如何助长全球欺诈广告生态。最新报告详细记录了研究团队如何"黑吃黑"——通过控制被遗弃的域名来监听数百万条恶意通知。  
  
  
**Part01**  
## 漏洞利用与域名劫持  
  
  
调查始于名为"坐以待毙"的攻击漏洞，威胁行为者通过认领已被原所有者放弃但仍保持活跃DNS委派的域名来实施攻击。Infoblox研究人员发现，某大型推送通知运营商遗留了大量存在此漏洞的域名。  
  
  
"我们采用DNS技术，通过在DNS提供商处简单认领就控制了被威胁行为者遗弃的域名...这并非中间人（AiTM）攻击，我们实际上是从侧面介入了威胁行为者的运营。"研究人员解释道。  
  
  
**Part02**  
## 海量数据收集与分析  
  
  
注册这些被忽视的域名后，研究人员被动接收了大量仍试图连接攻击者基础设施的受害设备流量。"一天之内，我们的收集范围从一个域名扩展到近120个，"报告指出，"数千台受害设备连接到我们的服务器，每秒产生30MB的日志数据。"  
  
  
两周内收集的5700多万条日志数据，揭示了一个旨在用欺诈诱饵轰炸用户的自动化运营体系。受害者主要为Android Chrome用户，平均每天收到140条通知。  
  
  
**Part03**  
## 全球分布与欺诈手法  
  
  
虽然活动覆盖全球60多种语言，但目标明显偏向南亚地区。"孟加拉国、印度、印尼和巴基斯坦占全部流量的50%，"分析显示。  
  
  
这些通知内容极具欺骗性，利用恐惧、贪婪和"点击诱饵"诱骗用户。"通知主题运用欺骗、恐惧和希望诱导用户点击链接，包括冒充Bradesco、Sparkasse、Recibiste、万事达卡、Touch 'n Go和GCash等正规金融服务。"  
  
  
其他诱饵更具掠夺性，包括虚假病毒警报（"您的设备已被入侵"）、涉及埃隆·马斯克等公众人物的捏造新闻丑闻，以及成人内容诈骗链接。  
  
  
**Part04**  
## 低效却持续的黑产运营  
  
  
尽管垃圾信息数量庞大，该运营的盈利能力却出奇低下。研究人员估计，攻击者从观测流量中每日仅获利约350美元。点击率（CTR）更是惨淡，平均仅为六万分之一。  
  
  
"其目标并非向更可能参与的用户投放广告，而是试图欺骗人们...让广告商网站流量看似增长，"报告指出。  
  
  
**Part05**  
## DNS管理的重要警示  
  
  
这项研究不仅揭示了联盟欺诈广告的阴暗世界，也为基础设施管理敲响警钟。"坐以待毙"漏洞仍是攻击者的有力工具，使其能够劫持合法声誉用于恶意目的。  
  
  
"虽然我们'解救'了这些恶意域名，但其他恶意行为者每天都在使用相同技术从合法组织获取休眠域名。"研究人员强调，这不仅关乎诈骗者，合法组织若未能清理DNS记录同样面临风险。  
  
  
报告总结道："从技术上讲，DNS管理是域名所有者的责任。这就像有人把玩具遗落在人行道上，被别人捡走了。这该怪谁呢？"  
  
  
**参考来源：**  
  
Sitting Ducks and Scammy Notifications: Inside a Global Malvertising Operation  
  
https://securityonline.info/sitting-ducks-and-scammy-notifications-inside-a-global-malvertising-operation/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
###   
### 电台讨论  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
