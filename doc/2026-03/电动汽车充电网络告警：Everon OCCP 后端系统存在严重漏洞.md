#  电动汽车充电网络告警：Everon OCCP 后端系统存在严重漏洞  
Ddos
                    Ddos  代码卫士   2026-03-06 09:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**网络安全研究人员提醒称，用于管理电动汽车充电站的数字基础设施Everon OCPP 后端系统中存在多个严重漏洞，可导致攻击者劫持充电会话、操纵基础设施数据，或使整个充电网络下线。这些漏洞影响所有版本的 api.everon.io 平台。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
其中最严重的漏洞CVE-2026-26288（CVSS 评分为 9.4）源自WebSocket 端点上完全缺乏正确身份验证机制**。**  
未经身份验证的攻击者可使用任何已知或已发现充电站标识符连接到后端。一旦连接上，攻击者便可以像合法充电器一样发送或接收开放充电点协议命令，从而导致充电基础设施被未经授权控制、权限提升以及报告数据被篡改等后果。  
  
研究人员还发现了另外三个对充电电网安全更具威胁的漏洞：  
  
CVE-2026-24696（CVSS 7.5）是由API 未对身份验证请求的数量进行限制导致的。缺少速率限制使攻击者能够通过压制合法遥测数据来实施暴力破解攻击或引发拒绝服务。  
  
CVE-2026-20748（CVSS 7.3）是因为系统允许多个端点使用相同的会话标识符进行连接，从而导致“会话劫持”或“影子连接”。在这种情况下，恶意连接可能会取代合法充电器，并接收本该发送给该充电站的后端命令。  
  
CVE-2026-27027（CVSS 6.5）源自充电站的身份验证标识符可通过基于网络的地图平台公开获取，从而为攻击者发动上述冒充攻击提供了所需的“钥匙”。  
  
为缓解这些系统性安全风险，Everon 公司并未发布补丁，而是彻底停用该服务，做出了罕见且果断的响应。该公司已于 2025 年 12 月 1 日正式关闭了受影响的平台，从而有效消除了对电动汽车充电生态系统的威胁。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[思科修复已遭利用的 Unified CM RCE 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524955&idx=2&sn=922edf69046bb2a552b3f58f4f21f882&scene=21#wechat_redirect)  
  
  
[思科：速修复已出现 exp 的身份服务引擎漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=1&sn=d0696191628f6b13a09be6edecbbec4d&scene=21#wechat_redirect)  
  
  
[思科修复 Contact Center Appliance 中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524343&idx=2&sn=54f09a81eb6da8e9b06f5a17b8b70644&scene=21#wechat_redirect)  
  
  
[速修复！思科ASA 两个0day漏洞已遭利用，列入 CISA KEV 清单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524078&idx=1&sn=a668c49a8bfda90e1da60201307dc79b&scene=21#wechat_redirect)  
  
  
[思科修复影响路由器和交换机的 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524071&idx=1&sn=31248d9d535baaa71b2ec67ceef617e8&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://securityonline.info/ev-charging-grid-alert-critical-flaws-exposed-in-everon-ocpp-backends/  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
