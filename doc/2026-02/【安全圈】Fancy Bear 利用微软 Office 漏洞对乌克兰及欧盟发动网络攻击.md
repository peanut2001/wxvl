#  【安全圈】Fancy Bear 利用微软 Office 漏洞对乌克兰及欧盟发动网络攻击  
 安全圈   2026-02-04 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
黑客  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljRMAYtDftYGPEJRsxwCSatnib08Oysg23ayrhuFBXh69vW0ErbJ8Dicdc7BLJ7ImzQ6ABrwuRS88Cw/640?wx_fmt=png&from=appmsg "")  
  
据报道，与俄罗斯有关联的黑客组织 Fancy Bear（ APT28）利用微软 Office 近期披露的一项漏洞，对乌克兰及欧盟相关组织发起网络攻击。  
  
该预警由乌克兰国家网络威胁情报机构 —— 乌克兰计算机应急响应小组（CERT-UA）于 2 月 2 日发布。  
#### CVE-2026-21509 漏洞在披露前已遭利用  
  
CERT-UA 具体报告称，其在 1 月 29 日发现了一个名为 “Consultation_Topics_Ukraine(Final).doc” 的 Word 文档。该文档包含 CVE-2026-21509 漏洞的利用程序，该漏洞为高危级别（CVSS 3.1 评分 7.8 分），影响微软 Office 2016、2019、长期服务频道 2021 版、长期服务频道 2024 版及微软 365 企业应用版等多个版本。  
  
微软于 1 月 26 披露了该漏洞，其成因是微软 Office **在安全决策环节过度依赖不可信输入**  
。  
  
该漏洞被成功利用后，攻击者**可绕过**  
微软 365 及 Office 中的对象链接与嵌入（OLE）防护机制，而该机制原本用于保护用户免受存在漏洞的组件对象模型（COM）及 OLE 控件的威胁。  
  
微软在其安全公告中确认，已检测到该漏洞存在在野利用的相关证据。该科技企业敦促微软 Office 2016 及 2019 版本用户**务必安装更新以获得防护**  
。  
  
微软 Office 2021 及后续版本用户将通过服务端更新获得自动防护，但需重启 Office 应用程序方可生效。  
  
CERT-UA 在报告中指出：“鉴于用户可能延迟（或无法）更新微软 Office 及落实推荐安全措施，利用该漏洞发起的网络攻击数量或将持续上升。”  
  
**Fancy Bear 针对 CVE-2026-21509 漏洞的攻击链**  
  
乌克兰计算机应急响应小组发现的该 Word 文档，与欧盟常驻代表委员会针对乌克兰局势的磋商相关。  
  
文档元数据显示，其创建时间为 1 月 27 日上午，即微软披露该漏洞的次日。  
  
同日，乌克兰计算机应急响应小组表示，从合作方处收到报告称，出现**疑似来自乌克兰水文气象中心的钓鱼邮件**  
，附件为另一个名为 BULLETEN_H.doc 的文档。  
  
这封邮件被发送给了超过 60 个邮箱地址，收件方主要是乌克兰的中央行政机关。  
  
CERT-UA 的深入分析表明，使用微软 Office 打开该文档后，会通过 WebDAV 协议触发与外部资源的网络连接，随后下载一个伪装成快捷方式（LNK 文件）的恶意文件，该文件含有的恶意代码可实现载荷的下载与执行。  
  
攻击成功执行后，会进行以下操作：  
- 创建名为 “EhStoreShell.dll” 的 DLL 文件（伪装成系统“增强存储外壳扩展”库）。  
  
- 创建包含 Shellcode 的图片文件 “SplashScreen.png”。  
  
- 修改注册表中 CLSID {D9144DCD-E998-4ECA-AB6A-DCD83CCBA16D} 的路径（以此实现 COM 劫持）。  
  
- 创建名为 “OneDriveHealth” 的计划任务。  
  
这些任务执行后，会终止并重启资源管理器进程（explorer.exe），该进程会通过组件对象模型劫持技术加载 EhStoreShell.dll 文件。  
  
该动态链接库文件会执行图片文件中的壳代码，最终在受感染系统中加载 Covenant 攻击框架。  
  
Covenant 是一款基于.NET 框架开发的命令与控制（C2）工具，最初设计用途为网络攻防演练及红队渗透测试。  
  
乌克兰计算机应急响应小组还强调，由于 Covenant 框架将合法云存储服务 Filen 作为命令与控制基础设施，疑似被Fancy Bear组织列为攻击目标的机构，**应封禁该云存储服务节点的网络访问，或至少对相关网络交互进行严密监控**  
。  
  
2026 年 1 月下旬，安全人员还发现了另外三份携带相同漏洞利用代码的文档，其攻击目标指向欧盟国家的组织机构。  
  
乌克兰计算机应急响应小组敦促相关方落实微软安全公告中列明的漏洞缓解措施，**尤其是针对 Windows 注册表配置**  
的相关防护操作。  
  
  
 END    
  
  
阅读推荐  
  
  
[【安全圈】黑客放出新变种病毒针对fnOS升级！官方紧急通告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=1&sn=105dd0887a04a2973f0cb2a46fe6e35a&scene=21#wechat_redirect)  
  
  
  
[【安全圈】海康威视修复DS-3WAP无线接入点命令注入漏洞（CVE-2026-0709）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=2&sn=de21d8160a6914ed983588d94ca30082&scene=21#wechat_redirect)  
  
  
  
[【安全圈】违法违规收集使用个人信息问题，72 款移动应用被通报](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=3&sn=6d05f640425c249524534221f7f14569&scene=21#wechat_redirect)  
  
  
  
[【安全圈】元宝崩了！腾讯回应来了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073971&idx=1&sn=29226d82814e3d9a9807b3bff55702f3&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
  
  
