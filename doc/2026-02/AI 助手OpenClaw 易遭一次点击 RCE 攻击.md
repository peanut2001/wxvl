#  AI 助手OpenClaw 易遭一次点击 RCE 攻击  
Eduard Kovacs
                    Eduard Kovacs  代码卫士   2026-02-04 10:11  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**OpenClaw****的开发人员最近修复了一个严重漏洞CVE-2026-25253。攻击者可利用该漏洞诱骗用户访问恶意网站，劫持该热门AI助手。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
OpenClaw（此前被称为“Clawdbot” 和 “Moltbot”）是一款开源的自托管AI智能体，可自动执行终端命令、管理文件系统以及协调通讯应用之间的复杂工作流。  
  
安全公司 DepthFirst 的研究员最近发现，OpenClaw 受该漏洞影响，可导致攻击者获得用户的认证令牌，从而连接到受害者的 OpenClaw 实例。该漏洞已在最近发布的版本2026.1.29中修复。  
  
OpenClaw 公司的开发人员在一份安全公告中提到，“这是一个令牌盗取漏洞，可导致网关遭完全攻陷。它影响用户在 Control UI上经过身份认证的任何 Moltbot 部署。攻击者获得了对该网关API的操作权限，因此能够在网关主机上执行任意配置变更和代码执行。”  
  
研究人员已详细解释了该攻击的运行流程。  
  
攻击者只需诱骗受害者访问一个恶意网站就能启动攻击。该攻击的站点只在受害者浏览器中执行 JavaScript，获得OpenClaw 认证令牌并将其发送给攻击者。该攻击者站点还执行代码以建立与本地主机的 WebSocket 连接，通过被盗令牌启用身份验证。之后攻击者可禁用沙箱隔离，通过用户确认危险命令的执行。  
  
由于OpenClaw 在系统上提权并获得访问数据和应用的权限，因此攻击者可获得对受害者有价值信息的访问权限并利用该 AI 助手执行任意命令并控制主机。  
  
虽然 OpenClaw 仅诞生几个月，但这并非它首次出现的安全问题。1月下旬，Jamieson O’Reilly 演示表明威胁行动者可利用 OpenClaw 访问高度敏感信息、在主机系统上执行命令并操纵用户。思科安全研究员也从中发现了严重漏洞并提醒企业称 OpenClaw 可能是一个“安全噩梦”。  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[数百个 Clawdbot 网关遭暴露，API密钥和私密聊天受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524977&idx=2&sn=8f7733539478a46d48f67a834dddcfc4&scene=21#wechat_redirect)  
  
  
[众多AI 编程工具存在30+漏洞，可导致数据被盗和RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524600&idx=2&sn=10cbb52355fe219ed945912fcd54a0fd&scene=21#wechat_redirect)  
  
  
[OpenAI 编程代理中高危漏洞可用于攻击开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524571&idx=2&sn=e4271fa2e064e2011e1b779ac929f05f&scene=21#wechat_redirect)  
  
  
[第三方供应商导致OpenAI客户数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524535&idx=1&sn=b7fe9e8a785380e376468375bde77bce&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.securityweek.com/vulnerability-allows-hackers-to-hijack-openclaw-ai-assistant/  
  
  
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
  
