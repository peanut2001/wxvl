#  成果分享 | 智能体漏洞检测 [ASE'25, Security'25/26, BlackHat EU]  
 信息网络安全杂志   2026-02-21 09:00  
  
**智能体**  
  
**漏洞检测**  
  
成果分享  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1fBQuSQnHibaibTq8pH3Sj4IVYdvYfDicewQpoAMCDPFlQDPgtB1vIU1gA/640?wx_fmt=gif&from=appmsg "")  
  
  
  
  
**前言**  
  
  
2025 年被业界广泛称为“智能体（AI Agent）元年”。智能体以前所未有的速度融入移动终端、具身系统等数字与物理场景。然而，其能力跃升伴随而来的安全挑战日益严峻，OpenAI、微软等厂商接连曝出严重安全漏洞。  
  
针对这一问题，我们首次系统梳理了智能体的漏洞根因与修复难点，并提出两款工具用于高效、精准地发现智能体潜在安全风险。相关成果已被 **ASE'25、Security'25、Security'26、BlackHat EU'25、GeekCon'25**  
等国际顶级学术会议（CCF-A 类）与行业会议接收。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**智能体及其安全现状**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
**智能体**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
智能体（Agent）是一种能够感知环境并自主决策、执行行动以完成特定目标的智能系统。其工作流程如图所示：  
1. 用户发出指令  
  
1. 智能体拼接用户与系统指令并发给大模型  
  
1. 智能体解析大模型返回并调用相应工具  
  
1. 最终将执行结果返回给用户  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1iaDjvaF62ISTaP7ZRibiaG2dPGd2ta6Elp3BrrRTvKbE6A3UIzNZXqdaw/640?wx_fmt=png&from=appmsg "")  
  
智能体工作流  
  
  
**智能体安全风险严峻**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
近年来，OpenAI、微软[1][2]等国内外厂商的智能体系统中频繁曝出严重安全漏洞。攻击者只需要发送一封邮件，便能在用户毫无感知的情况下窃取隐私信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1mv0rMHPka4V6iaMDicyTgU86OnNGaNE1bZ4Pibf6nDWWYwhDMJVAe4G2A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j14TgoReqdaLGAUhH5ib2qfScvw7jAcrxzAzibE7QoxFyo7Knia1yMvO31w/640?wx_fmt=png&from=appmsg "")  
  
国内外智能体厂商爆出严重漏洞  
  
不同于传统软件系统由开发者预先定义功能逻辑、仅接收特定结构的输入，智能体面对的是高度开放的自然语言输入空间，其功能边界和行为模式在开发阶段往往难以被完整刻画，而是交由大模型根据用户意图动态规划和执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1ydmibqWtVgpZQTXZhxoeFf1IoOmTNh1kX5BCfoqUrPM4zqcHNJfAXQg/640?wx_fmt=png&from=appmsg "")  
  
智能体不同功能深度耦合  
  
然而现有漏洞检测方案高度依赖明确、稳定的功能边界假设，难以有效刻画和覆盖智能体的动态行为，从而难以对其潜在安全漏洞进行有效检测。  
  
针对这一问题，我们首次系统分析了智能体漏洞的形成机制及其修复难题，并提出了两种自动化检测工具，在主流开源应用新发现70+漏洞（0-day）。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**智能体漏洞根因与修复难题**  
  
**ASE'25**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞现状  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们对 50 个主流智能体应用进行了系统分析，共收集到 221 个已公开安全漏洞。其中 74.1% 被评定为高危或致命级漏洞。  
  
进一步分析表明，注入类漏洞（如代码注入、命令注入）是当前智能体系统中危害性最强、风险最高的漏洞类型。  
  
**漏洞根因**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们发现，当前智能体开发实践中普遍存在**对LLM输出结果的过度信任问题**  
。由于 LLM 生成内容本身缺乏安全性保证，其输出在未经过充分校验与过滤的情况下，往往被直接传递给具备高权限的敏感工具。  
  
攻击者可通过诱导 LLM 调用存在安全缺陷的工具，从而在智能体执行阶段触发漏洞并造成安全影响。  
  
**修复难题**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们进一步发现，智能体开发面临显著的安全与效率权衡困境。一方面，为提升系统能力与实用性，智能体需要被赋予更强功能和更高执行权限；另一方面，安全设计应遵循最小权限原则，而权限的增加不可避免地扩大攻击面，加剧整体安全风险。  
  
目前，我们针对智能体漏洞分析的工作[3]已被软工领域国际顶会**ASE'25**  
接收。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**智能体注入类漏洞检测**  
  
**Security'25**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
智能体中的注入类漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
下图展示了智能体系统中一种典型的注入类漏洞，攻击者可借此在智能体环境中实现任意代码执行。其攻击流程为：  
1. 攻击者构造对抗性提示以绕过指令约束（蓝色部分），诱导智能体执行任意指令  
  
1. 攻击者在提示中嵌入特定语义触发条件（红色部分），促使智能体调用 TaskOutputHandler 组件  
  
1. 精心构造的恶意载荷（绿色部分）被传递至敏感函数（第 6 行），从而触发任意代码执行漏洞。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1abOnT8TrN0FKnLzibU3wAUE6V4acicfZpgicHSe1ibJ5nu1NhNtThql56A/640?wx_fmt=png&from=appmsg "")  
  
智能体中注入类漏洞示例  
  
**AgentFuzz**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们首次提出了一种面向智能体注入类漏洞的自动化检测工具 AgentFuzz。如下图所示，AgentFuzz 借助LLM生成初始测试指令，并基于语义相似度、执行轨迹距离等多维指标评估指令的漏洞触发潜力。在此基础上，AgentFuzz 优先选择高质量候选指令，对其功能语义与约束绕过能力进行迭代优化，逐步逼近漏洞触发条件，从而高效发现代码执行等注入类漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j18RdodtXDDjbVSnxZLP7ppjKBTMniaLap5JLg0SXa1467pxP4fFiaiaogw/640?wx_fmt=png&from=appmsg "")  
  
AgentFuzz 架构  
  
**效果评估**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们使用 AgentFuzz 对 20 款主流开源智能体应用进行了系统化扫描，成功发现 **34 个**  
此前未知的高风险漏洞（0-day），其中 23 个已获得 CVE 编号。这些漏洞共影响 14 款开源智能体应用，其中 7 款在 GitHub 上的 star 数超过 1 万。  
  
目前，我们针对智能体注入类漏洞检测的工作[4-6]已被**USENIX Security'25、 BlackHat EU'25和 GeekCon'25等学术与行业会议**  
接收。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**智能体拒绝服务漏洞检测**  
  
**Security'26**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
智能体中的拒绝服务漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
下图展示了智能体系统中一种典型的资源耗尽类漏洞，攻击者可通过持续消耗内存资源触发拒绝服务（Denial of Service, DoS），造成其他用户无法使用该智能体。其攻击流程为：  
1. 攻击者在提示中嵌入特定语义触发条件（红色部分），诱导智能体执行文件下载操作  
  
1. 攻击者进一步诱导智能体重复下载超大文件 1000 次，由于下载内容在执行过程中被无限制地存储于内存中（第 6 行），最终导致内存耗尽并引发智能体服务不可用。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1d76hufozRjyMKXr4OzgyxoeiaLuavnLDAFumw3pOhq9pAs0ia2jPVwiaQ/640?wx_fmt=png&from=appmsg "")  
  
智能体中拒绝服务漏洞示例  
  
**AgentDoS**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们首次提出了一种面向智能体资源耗尽类漏洞的自动化检测工具 AgentDoS。如下图所示，该工具首先分析智能体执行流程，定位潜在的资源消耗操作，并基于资源生命周期评估其可利用性与利用方式。随后，在动态验证阶段，AgentDoS 首先尝试触发资源消耗行为，随后迭代优化输入指令，增强资源消耗，最终实现资源耗尽漏洞的自动化触发与验证。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1WLdU2ibsLUjP3a8Bfv3Z18uc0icjsbqxZ35lG0qUDcliaZ4NjgEj77E0w/640?wx_fmt=png&from=appmsg "")  
  
AgentDoS架构  
  
效果评估  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1VIfGicW4lcVQFUWPK4WyAPow0zfVRiaV4KHQKibaC5Cxx2z9jX2ZMP1rA/640?wx_fmt=gif&from=appmsg "")  
  
  
我们使用 AgentDoS 对 20 款主流开源智能体应用进行了系统评估，发现**36**  
个此前未知的高风险漏洞（0-day），其中 15 个已获得 CVE 编号。这些漏洞影响 16 款智能体应用，其中 15 款在 GitHub 上的 star 数超过 1 万。  
  
目前，我们针对智能体拒绝服务类漏洞检测的工作[7]已被**USENIX Security'26**  
接收。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**结语**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
通过对公网环境的系统性测绘分析，团队发现上述智能体漏洞并非个案，大量实际部署并处于运行状态的智能体系统普遍存在显著的安全隐患，智能体漏洞检测已成为当前安全领域的迫切需求。为扭转“autonomy comes with costs”这一被动局面，迈向“secure and safe autonomy”的产业发展目标，团队正持续开展研究，构建具备工程可落地性的创新型智能体安全攻防技术体系。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j17BicQRmUT0FabqSGkJfWrRnqDOoJacnq3EPexKqVibaHLOyg8xumucJg/640?wx_fmt=png&from=appmsg "")  
  
**研究团队**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j16KpcTibcnW31t1ibatKyZXv7pvg2AQ1aoVvUPZPzXM9qxswe9ZRTom8w/640?wx_fmt=png&from=appmsg "")  
  
  
戴嘉润老师团队研究方向为智能系统安全，在IEEE S&P、USENIX Security、ACM CCS、NDSS等国际顶级会议上发表多篇论文，面向多类型智能系统研制安全测评、安全攻防与安全治理工具，在大模型智能体、智能设备等关键目标上累计挖掘千余例零天漏洞和缺陷，研究工作得到美国福布斯、英国独立报等媒体报道，获多项国内外安全攻防赛事冠军、上海市技术发明奖一等奖、上海市决策咨询研究成果奖一等奖等奖项，长期服务上海市数字政务系统的安全治理。  
  
**联系邮箱**  
：jrdai@fudan.edu.cn，戴嘉润老师  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RyyHWbbqW87lSF4RXiacKibH2YA5iabF8j1YYkPiaHZyaH7lnLHTDedHvib5zpPtqCgkRnoMsDxckDsVBbQ6ic9icvhsw/640?wx_fmt=gif&from=appmsg "")  
  
**= END =**  
  
[1] https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html  
  
[2] https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html  
  
[3] Security Debt in LLM Agent Applications: A Measurement Study of Vulnerabilities and Mitigation Trade-offs,  ASE 2025  
  
[4] Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents, USENIX Security 2025  
  
[5] Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents, Black Hat Europe 2025  
  
[6] https://geekcon.top/2025  
  
[7] Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents, USENIX Security 2026  
  
  
供稿/排版：罗嘉骐  
  
责编：邬梦莹  
  
审核：戴嘉润、林楚乔、张琬琪  
、洪赓  
  
  
  
  
  
  
复旦白泽战队  
  
一个有情怀的安全团队  
  
  
还没有关注复旦白泽战队？  
  
公众号、小红书  
搜索  
：复旦白泽战队也能找到我们哦~  
  
  
  
  
