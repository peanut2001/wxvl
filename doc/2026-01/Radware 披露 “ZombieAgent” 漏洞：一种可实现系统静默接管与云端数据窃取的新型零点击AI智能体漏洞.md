#  Radware 披露 “ZombieAgent” 漏洞：一种可实现系统静默接管与云端数据窃取的新型零点击AI智能体漏洞  
 睿伟网络科技   2026-01-27 05:00  
  
**Radware发现新型零点击间接提示词注入（IPI）漏洞——ZombieAgent。**  
该漏洞主要针对OpenAI的 ChatGPT模型，可能导致企业面临隐蔽的数据窃取、持续的智能体劫持以及能够绕过企业安全控制的服务端恶意执行风险。  
  
  
**持久化内存操控与自主传播**  
  
ZombieAgent在初始阶段与Radware此前披露的ShadowLeak漏洞类似，均表现为利用间接提示词注入技术来影响AI智能体的行为。  
  
然而，**Radware研究人员进一步发现了ZombieAgent更高级的攻击阶段：能够将恶意规则直接植入智能体的长期记忆或工作笔记中。**  
这使得攻击者无需再次接触目标即可建立持久化控制。此后，每次使用该智能体时，它都会执行隐藏的恶意操作，随着时间推移悄无声息地收集敏感信息。此外，该漏洞还具备攻击传播能力，能够将其影响扩散至其他联系人或电子邮件收件人。  
  
**因此，一封恶意邮件就可能成为攻击的起点，最终在企业内部乃至外部演变成一个不断扩散、自动化、类似蠕虫的传播活动。**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/k8mFfEmdQe0icibsuu7pdyBxy0BqszFMlXLgvq22oz9WkQbk7lGUh6psgZDxgLQVtpibc00sqxGAAEu5SGMiafH3OdicWztqqOXkK/640?wx_fmt=svg&from=appmsg "")  
  
  
  
ZombieAgent揭示了当前自主AI平台中一个关键的结构性弱点，企业依赖这些智能体进行决策和访问敏感系统，却无法洞察它们是如何解析不可信内容的，也无从知晓它们在云端执行了哪些操作。这形成了一个危险的盲区，而攻击者已经开始利用这一点。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/k8mFfEmdQe0icibsuu7pdyBxy0BqszFMlXQZVuow3LKVTO0TlOnriaV10TicvKZ6sXVokrYoK2WicSqicucwU8j9hnUg0suVSJibMBM/640?wx_fmt=svg&from=appmsg "")  
  
——Radware威胁情报主管 Pascal Geenens  
  
  
**利用隐蔽指令实现零点击攻击**  
  
Radware威胁情报研究团队借鉴了此前发现ShadowLeak漏洞的经验，在用于防护提示词注入漏洞的安全护栏中发现了这一新缺陷。攻击者可以将隐藏的指令嵌入日常的电子邮件、文档或网页中。当AI智能体处理这些内容时，便会将其中隐藏的指令视为合法命令来执行。一旦被激活，被入侵的智能体便能够收集邮箱数据、访问敏感文件并与外部服务器通信。**整个攻击过程无需用户进行任何交互，也无需 任何“点击”操作即可触发。**  
  
**ZombieAgent的一个决定性特征是，所有恶意行为都发生在OpenAI的云基础设施内部，而非用户设备或企业的IT环境中。**  
因此，终端日志不会记录该活动，网络流量也不会经过企业的安全防护堆栈。诸如安全Web网关、端点检测与响应（EDR）系统或防火墙等传统安全工具，均无法侦测到此次敏感数据窃取。所以，没有任何传统告警会向用户提示系统已遭入侵。**这种发生在云端的隐蔽性，使得企业极难利用现有控制手段来发现或阻止ZombieAgent攻击。**  
  
**ZombieAttack的发现建立在Radware早前关于“ShadowLeak”的研究基础之上，进一步揭示了攻击者能如何轻易地利用正在快速扩张的 “自主智能体威胁界面” ——在这个界面上，AI智能体自主阅读邮件、与企业系统交互、发起工作流程并做出决策。Radware已根据责任披露协议向OpenAI报告了此漏洞。**  
  
  
  
**关于Radware**  
  
  
  
Radware®（NASDAQ: RDWR）是多云环境应用安全和交付解决方案的全球领导者。该公司的云应用程序、基础设施和API安全解决方案使用人工智能驱动的算法，可提供精确、无操作、即时的防护，免受复杂的网络、应用程序、DDoS攻击、API滥用和恶意机器人的攻击。全球的企业和运营商依靠Radware解决方案来应对不断变化的网络安全挑战，并在降低成本的同时保护品牌和业务运营。  
  
欲知详情，请访问：https://cn.radware.com/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/UicD0GtT0eekkWsBpqvEEpiaVbqGLWzI5FYb3Hfxqc9wEicaqgicqsb0ezdD4Uiaw8uoeWGXBbh7DN1kpo4SWPMfgqg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
  
  
