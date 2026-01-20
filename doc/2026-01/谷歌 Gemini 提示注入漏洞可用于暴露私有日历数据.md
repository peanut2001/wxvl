#  谷歌 Gemini 提示注入漏洞可用于暴露私有日历数据  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-01-20 10:11  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**网络安全研究人员披露称，一个漏洞利用间接提示注入攻击谷歌Gemini，从而绕过授权防护机制，并将谷歌日历用作数据窃取渠道。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Miggo Security公司的研究负责人Liad Eliyahu表示，通过在标准的日历邀请中隐藏一个休眠的恶意载荷，利用该漏洞可绕过谷歌日历的隐私控制，“这种绕过方式使得攻击者能够在无需任何直接用户交互的情况下，未经授权访问私人会议数据并创建具有欺骗性的日历事件。”  
  
该攻击链的起点是威胁行动者精心制作并发送给目标用户的新日历事件。该邀请的描述中嵌入了一个自然语言提示，旨在执行攻击者的指令，从而构成提示注入。  
  
当用户向Gemini询问一个完全无害的日程问题时（例如，“我周二有会议吗？”），攻击便被激活。该询问使人工智能聊天机器人解析上述事件描述中特殊构造的提示，汇总用户特定日期的所有会议，并将这些数据添加到一个新创建的谷歌日历事件中，然后向用户返回一个无害的回应。  
  
Miggo表示，“然而，Gemini在后台创建了一个新的日历事件，并将目标用户的所有私人会议完整摘要写入了该事件的描述中。在许多企业日历配置中，该新事件对攻击者是可见的，从而导致攻击者能够读取窃取的私人数据，而目标用户无需执行任何操作。”  
  
虽然负责任披露后该漏洞已得到修复，但该事件再次表明随着越来越多的组织机构使用AI工具或在内部构建自己的智能体来自动化工作流程，AI原生功能可能会扩大攻击面，并在无意中引入新的安全风险。  
  
Eliyahu指出，“AI应用程序旨在理解语言，但却被语言本身操纵。漏洞不再局限于代码，而是存在于语言、上下文以及AI在运行时的行为中。”几天前，Varonis详细阐述了名为“Reprompt”的攻击活动——攻击者能够一键从Microsoft Copilot等AI聊天机器人中窃取敏感数据，同时绕过企业安全控制。  
  
这些发现表明，需要在关键安全和安全维度上持续评估大型语言模型，测试其产生幻觉、事实准确性、偏见、危害和越狱抵抗的倾向，同时保护AI系统免受传统问题的影响。  
  
就在上周，Schwarz 集团的XM Cyber团队披露了在谷歌云Vertex AI的Agent Engine和Ray内部提升权限的新方法，凸显了企业需要审计附加在其AI工作负载上的每一个服务账户或身份。研究人员提到，“这些漏洞可使权限最低的攻击者劫持高权限的服务代理，有效地将这些‘看不见的’托管身份转变为促进权限提升的‘双重代理’。”  
  
成功利用这些“双重代理”漏洞可使攻击者读取所有聊天会话、读取LLM记忆、读取可能存储在存储桶中的敏感信息，或获得对Ray集群的根访问权限。鉴于谷歌表示这些服务目前“按预期运行”，企业审查具有“查看者”角色的身份并确保部署足够的控制措施以防止未经授权的代码注入至关重要。  
  
与此同时，多个AI系统中发现了多个漏洞和弱点：  
  
- The Librarian中的漏洞：TheLibrarian.io提供的AI个人助手工具存在安全漏洞（CVE-2026-0612、CVE-2026-0613、CVE-2026-0615和CVE-2026-0616），可使攻击者访问其内部基础设施，包括管理员控制台和云环境，最终泄露敏感信息如云元数据、后端运行的进程和系统提示，或登录其内部后端系统。  
  
- 系统提示提取漏洞：该漏洞展示了如何通过提示基于意图的LLM助手以Base64编码格式在表单字段中显示信息来提取其系统提示。Praetorian表示，“如果一个LLM可以执行向任何字段、日志、数据库条目或文件写入数据的操作，那么每个这样的目标都成为一个潜在的数据窃取渠道，无论聊天界面被锁定得多么严格。”  
  
- Anthropic Claude Code插件攻击：该攻击演示了如何利用上传到Anthropic Claude Code应用商店的恶意插件，通过钩子绕过“人机回圈”防护机制，并通过间接提示注入窃取用户的文件。  
  
- Cursor中的严重漏洞：Cursor中存在一个严重漏洞（CVE-2026-22708）。攻击者通过利用智能体IDE处理Shell内置命令时的根本疏忽，可实现通过间接提示注入进行远程代码执行。“通过滥用隐式信任的Shell内置命令，如export、typeset和declare，威胁行动者可以静默地操纵环境变量，随后污染合法开发者工具的行为，”Pillar Security公司表示。“这个攻击链将良性的、用户批准的命令例如git branch`或python3 script.py转变为任意代码执行的载体。”  
  
  
  
对五种Vibe编码IDE（Cursor、Claude Code、OpenAI Codex、Replit和Devin）的安全分析发现，编码智能体擅长避免SQL注入或XSS漏洞，但在处理SSRF问题、业务逻辑以及在访问API时实施适当的授权方面存在困难。更糟糕的是，所有这些工具都缺少CSRF防护、安全头部或登录频率限制。这项测试凸显了当前Vibe编码的局限性，表明人类监督仍然是解决这些差距的关键。  
  
“不能信任编码智能体设计安全的应用程序，” Tenzai公司的研究员Ori David表示，“虽然它们可能（在某些时候）生成安全的代码，但如果没有明确的指导，智能体始终无法实现关键的安全控制。在边界不清晰的地方如业务逻辑工作流、授权规则和其他微妙的安全决策，智能体会犯错。”  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[谷歌Gemini Enterprise存在漏洞，可导致企业数据遭暴露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524630&idx=2&sn=be82a743b4b79c2cc101a8757cb82cc4&scene=21#wechat_redirect)  
  
  
[Google Calendar 邀请被用于劫持 Gemini，泄露用户数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523771&idx=1&sn=202844570d8eb4bdbaf371dc692e7896&scene=21#wechat_redirect)  
  
  
[Gemini CLI AI 编程助手中存在严重漏洞 可导致代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523673&idx=1&sn=e9be201d67d443c5563ef93eab78ef92&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/hackers-now-exploiting-critical-fortinet-fortisiem-vulnerability-in-attacks/  
  
  
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
  
