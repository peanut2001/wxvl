#  国家漏洞库CNNVD：关于Microsoft Office安全漏洞的通报；韩国公共系统全面沦陷：模拟攻击揭示安全防护重大缺陷| 牛览  
 安全牛   2026-01-29 04:19  
  
**点击蓝字 关注我们**  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAojS2Pvx0MnMjiakPQUkjUj5CdSZ2wicqWySWfdM0dEsAKFgCNAj339oHVyAl9ibkyVm017UZzicrK0w/640?wx_fmt=png&from=appmsg "")  
  
  
新闻速览  
  
- 国家漏洞库CNNVD：关于Microsoft Office安全漏洞的通报  
  
  
- 韩国公共系统全面沦陷：模拟攻击揭示安全防护重大缺陷  
  
  
- 黑产团伙劫持AI算力转卖获利，35000次攻击瞄准LLM端点  
  
  
- 77%员工将公司信息输入AI工具，企业数据隐私面临双重风险  
  
  
- FBI查封RAMP论坛，最后的勒索软件公开交易平台覆灭  
  
  
- 边缘计算市场年增32%，AI驱动下的十大发展趋势值得关注  
  
  
- OpenAI 推出免费 AI 科研写作平台 Prism，集成 GPT-5.2 模型  
  
  
- eScan 更新服务器遭入侵，恶意文件通过官方渠道分发  
  
  
- WhatsApp推出"严格账户设置"功能，阻止自动下载遏制恶意软件传播  
  
  
- CISA高官竟将敏感政府文件喂给ChatGPT，AI滥用敲响安全警钟  
  
特别关注  
  
  
**国家漏洞库CNNVD：关于Microsoft Office安全漏洞的通报**  
  
国家信息安全漏洞库(CNNVD)近日发布预警，Microsoft Office存在安全漏洞(CNNVD-202601-4359、CVE-2026-21509)，攻击者可利用该漏洞绕过用户保护机制执行恶意代码。  
  
  
该漏洞源于Microsoft Office未对不受信任的输入进行有效验证，攻击者通过构造恶意Office文档即可触发漏洞。受影响版本覆盖范围广泛，包括Microsoft Office 2016、Microsoft Office 2019、Microsoft Office LTSC 2021、Microsoft Office LTSC 2024以及Microsoft 365 Apps for Enterprise等主流版本。  
  
  
由于Office办公软件在企事业单位中使用极为广泛，该漏洞一旦被利用可能造成大规模安全事件。攻击者可通过钓鱼邮件等方式传播恶意文档，用户在打开文档时即可能遭受攻击，导致敏感信息泄露或系统被控制。  
  
  
目前微软官方已发布安全补丁修复该漏洞，CNNVD建议用户立即确认产品版本并部署补丁。企业用户应通过集中补丁管理系统尽快完成更新，个人用户可访问微软安全更新指南获取修复程序。  
  
  
原文链接：  
  
https://www.secrss.com/articles/87400  
  
  
热点观察  
  
  
**77%员工将公司信息输入AI工具，企业数据隐私面临双重风险**  
  
在数据隐私日之际，一项企业AI安全报告揭示了严峻现实：77%的员工曾将公司信息粘贴到AI或LLM服务中，其中82%使用个人账号操作。这给企业带来双重风险。  
  
  
首先，员工输入LLM的提示词可能包含敏感企业数据。尽管AI公司设有安全防护，但攻击者已发现通过提示注入(prompt injection)绕过防护的方法——利用伪装成合法查询的恶意指令操纵代码，诱使AI泄露不应公开的数据。  
  
  
其次，使用ChatGPT、Claude、Gemini等个人AI账号意味着企业信息被传输到安全团队无法监控的系统中。这些敏感数据若留存在员工个人邮箱或云存储中，一旦账号被攻击将直接导致企业数据泄露。  
  
  
Accenture网络安全负责人Kamran Ikram强调，企业必须建立完整的数据清单，"如果不知道数据是否存在，就无法得知它是否被使用"。Cisco的Chris Gow建议企业为员工提供AI工具的企业版本，并通过培训指导员工识别不当使用行为。技术控制结合员工教育，才能在AI时代构建有效的数据隐私防护体系。  
  
  
原文链接：  
  
https://www.infosecurity-magazine.com/news-features/data-privacy-day-ai-rise-protect/  
  
  
**黑产团伙劫持AI算力转卖获利，35000次攻击瞄准LLM端点**  
  
Pillar Security研究人员披露了一起名为"Bizarre Bazaar"的大规模LLM劫持(LLMjacking)攻击行动。在40天内，研究人员的蜜罐系统记录到超过35000次攻击会话，攻击者专门针对配置不当或认证薄弱的LLM服务端点。  
  
  
该行动涉及三个协同作战的威胁行为者:第一个使用机器人扫描互联网上的LLM和MCP端点;第二个验证发现并测试访问权限;第三个运营名为"silver[.]inc"的商业服务，在Telegram和Discord上转卖API访问权限，收取加密货币或PayPal付款。该服务宣称提供50多个主流AI模型的访问能力。  
  
  
攻击者主要利用自托管LLM环境、未认证的Ollama端点(端口11434)、OpenAI兼容API(端口8000)等漏洞，用于窃取算力进行加密货币挖矿、在暗网转卖API访问、窃取对话历史数据，甚至通过Model Context Protocol服务器横向渗透内网系统。研究人员已将此行动归因于使用"Hecker""Sakuya""LiveGamer101"等别名的特定威胁行为者。截至发稿，该攻击行动仍在持续。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/hackers-hijack-exposed-llm-endpoints-in-bizarre-bazaar-operation/  
  
  
**韩国公共系统全面沦陷：模拟攻击揭示安全防护重大缺陷**  
  
韩国审计与监察委员会（BAI）在对七个公共部门系统进行模拟网络攻击测试中发现，所有系统均被黑客成功侵入，暴露出政府保护大量个人数据方面的严重漏洞。此次渗透测试由白帽黑客、国家安全研究所以及网络作战司令部联合执行，针对的是由个人信息保护委员会（PIPC）指定的123个需重点管理的公共系统中的七个。  
  
  
测试结果显示，在一个系统中，可以查询到约5000万公民的居民登记号码及其他信息；另一个系统中，黑客仅用20分钟就窃取了1000万会员的数据。此外，还存在关键信息未加密的情况，导致拥有管理员权限的黑客可轻易获取13万人的敏感信息。尽管已通知相关机构负责人并完成整改措施，但为避免进一步风险，具体受测系统名称及方法未公开。  
  
  
原文链接：  
  
https://koreajoongangdaily.joins.com/news/2026-01-27/national/socialAffairs/Hackers-breach-all-tested-publicsector-systems-in-Korean-audit-boards-simulated-cyberattack/2509650  
  
  
安全事件  
  
  
**eScan 更新服务器遭入侵，恶意文件通过官方渠道分发**  
  
MicroWorld Technologies 证实，其 eScan 杀毒软件的一台区域更新服务器在1月20日遭到入侵，攻击者利用未授权访问在更新分发路径中植入恶意文件。该文件在两小时窗口期内被推送给从该服务器集群下载更新的部分客户。  
  
  
受影响用户可能遭遇更新服务失败通知、系统 hosts 文件被篡改以阻止连接 eScan 更新服务器、无法接收新的安全定义更新等异常行为。  
  
  
安全厂商 Morphisec 的技术分析显示，攻击者通过修改 eScan 更新组件 Reload.exe 实现多阶段恶意软件部署。该文件虽带有 eScan 代码签名证书，但签名状态显示为无效。Reload.exe 被用于建立持久化、执行命令、修改 Windows HOSTS 文件并连接 C2 基础设施下载后续载荷。最终投放的 CONSCTLX.exe 充当后门和持久化下载器，通过名为"CorelDefrag"的计划任务维持驻留。  
  
  
eScan 已发布修复更新并隔离重建受影响基础设施，同时建议客户封禁相关 C2 服务器。值得注意的是，2024年朝鲜黑客曾利用 eScan 更新机制在企业网络植入后门，此类供应链攻击风险持续存在。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/escan-confirms-update-server-breached-to-push-malicious-update/  
  
  
**FBI查封RAMP论坛，最后的勒索软件公开交易平台覆灭**  
  
FBI已查封臭名昭著的RAMP网络犯罪论坛，该平台是少数公开允许推广勒索软件业务的地下论坛之一。目前该论坛的名ramp4u[.]io均显示FBI查封通知，域名服务器已切换至ns1.fbi.seized.gov和ns2.fbi.seized.gov。  
  
  
RAMP论坛于2021年7月由代号Orange(真名Mikhail Matveev)创建，起因是俄语黑客论坛Exploit和XSS在Colonial Pipeline事件后禁止勒索软件推广。Orange曾是Babuk勒索软件团伙管理员，利用该团伙此前使用的Tor洋葱域名搭建RAMP，使其成为勒索团伙招募成员、买卖网络访问权限的重要平台。  
  
  
此次查封由FBI与佛罗里达南区联邦检察官办公室及司法部计算机犯罪和知识产权部门联合实施。执法部门现已掌握论坛用户的电子邮件地址、IP地址、私信等大量关键数据，未遵循操作安全(opsec)规范的威胁行为者面临被识别和逮捕风险。  
  
  
Matveev已于2023年被美国司法部起诉，指控其参与Babuk、LockBit、Hive等多个勒索软件行动，攻击目标包  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/fbi-seizes-ramp-cybercrime-forum-used-by-ransomware-gangs/  
  
  
**CISA高官竟将敏感政府文件喂给ChatGPT，AI滥用敲响安全警钟**  
  
据《独立报》报道，美国总统Donald Trump任命的网络安全与基础设施安全局（CISA）代理局长Madhu Gottumukkala，于2025年夏季将标记为“仅限官方使用”（For Official Use Only， FOUO）的敏感合同文件上传至公共版ChatGPT，触发政府内部安全警报，并引发美国国土安全部（DHS）的专项审查。  
  
  
尽管这些材料未被列为国家机密，但FOUO标识意味着其包含不宜公开的敏感信息。公共版ChatGPT由OpenAI开发，用户输入的数据可能被用于模型训练或在其他用户的提示中泄露，存在潜在外泄风险。知情人士透露，Gottumukkala此前曾主动争取并获得DHS特批权限——当时绝大多数DHS员工被禁止使用该工具。一名官员批评其“迫使CISA同意他使用ChatGPT，随后却滥用了这一权限”。  
  
  
CISA公共事务主任Marci McCarthy回应称，Gottumukkala的使用属“短期且受限”，最后一次使用时间为2025年7月中旬，并强调CISA默认屏蔽ChatGPT访问，仅在例外情况下经授权开放。目前尚不清楚此次上传是否造成实际安全损害，相关内部审查结果未公开。  
  
  
值得注意的是，Gottumukkala自2025年5月起担任CISA代理局长，期间已卷入多起争议，包括其本人申请并通过的测谎测试结果存疑，导致至少六名CISA员工被停职。此事件凸显了生成式AI在政府敏感场景中的使用风险，也暴露出权限管理与数据分类制度在执行层面的漏洞。  
  
  
原文链接：  
  
https://www.independent.co.uk/news/world/americas/us-politics/trump-cyber-security-sensitive-materials-chatgpt-b2909704.html  
  
  
产业动态  
  
  
**边缘计算市场年增32%，AI驱动下的十大发展趋势值得关注**  
  
Accenture预测，边缘计算市场将以年均32.2%的速度增长，2030年达22亿美元。这一增长背后，企业需求已从成本优化转向AI运营化——实时决策、数据主权和低延迟AI推理成为核心驱动力。  
  
  
技术层面呈现三大突破。首先，边缘设备性能显著提升，Nvidia Jetson系列等AI专用芯片将复杂推理能力带到能效更高的小型设备上。其次，边缘MLOps平台日趋成熟，支持数千个AI端点的统一管理。第三，AI PC配备神经处理单元(NPU)，使强大的AI分析能力在笔记本层面实现，拓展了边缘计算的应用边界。  
  
  
然而挑战同样严峻。Allianz 2025报告指出，分散部署的边缘设备增加了攻击面，设备异构性加剧安全漏洞。攻击类型涵盖无线接入网络(RAN)嗅探、多接入边缘计算(MEC)攻击、供应链攻击等多个层面。  
  
  
Forrester将边缘计算细分为企业边缘、运营边缘、交互边缘和提供商边缘四类，每类适配不同技术栈和场景。Everest Group指出，成功的边缘架构需在AI推理、实时控制与数据驻留需求间取得平衡，这要求企业从基础设施安全性、可扩展性和混合云协同三方面系统性规划。  
  
  
原文链接：  
  
https://www.techtarget.com/searchcio/tip/Top-edge-computing-trends-to-watch-in-2020  
  
  
新品发布  
  
  
**OpenAI 推出免费 AI 科研写作平台 Prism，集成 GPT-5.2 模型**  
  
OpenAI 发布了免费科研写作平台 Prism，旨在解决研究人员在撰写论文时频繁切换工具导致的效率问题。该平台基于 OpenAI 收购的 LaTeX 服务 Crixet 开发，集成了 GPT-5.2 模型，专门针对数学和科学任务优化。  
  
  
Prism 将文本编辑、PDF 阅读、LaTeX 编译、文献管理和 AI 辅助整合到统一的云端工作空间。GPT-5.2 可直接访问文档完整结构，包括公式、引用和上下文，支持假设验证、草稿生成和智能编辑。平台提供 arXiv 文献检索、公式与引用处理、手写内容转 LaTeX 以及语音编辑等功能，所有修改对协作者实时可见。  
  
  
针对跨机构、跨国界的科研协作需求，Prism 不限制协作者数量，无需本地安装 LaTeX 环境。目前所有 ChatGPT 账户用户均可免费使用基础功能，无需订阅付费。未来将推出面向企业和教育机构的高级版本，但核心功能保持开放。  
  
  
该平台试图通过消除工具碎片化问题，提升科研写作效率和协作体验。  
  
  
原文链接：  
  
https://www.securitylab.ru/news/568704.php  
  
  
**WhatsApp推出"严格账户设置"功能，阻止自动下载遏制恶意软件传播**  
  
即时通讯平台已成为网络犯罪分子传播恶意软件的新渠道。黑客利用WhatsApp等平台的文件共享功能，将恶意软件伪装成普通附件通过图片、视频或文档传播，一旦自动下载即可窃取敏感数据或部署间谍软件。  
  
  
为应对这一威胁，Meta旗下的WhatsApp推出名为"严格账户设置"(Strict Account Settings)的新安全功能。该功能可阻止潜在恶意文件的自动下载，限制间谍软件传播。目前该功能正向记者、公众人物等高风险用户试点推送，计划于2026年底向全体用户开放。  
  
  
该功能类似于iOS的Lockdown Mode和Android的Advanced Protection，启用后将限制特定账户功能，核心改变是来自未知联系人的媒体文件将不再自动下载，需用户明确授权。用户可通过"设置>隐私>高级功能"启用此功能。  
  
  
值得关注的是，WhatsApp使用Rust编程语言开发该安全层。Rust以强大的内存安全特性和对常见软件漏洞的抵抗力著称，这一技术选择进一步强化了平台对间谍软件的防御能力。  
  
  
此举是WhatsApp持续打击间谍软件的延续。2021至2022年间，Meta曾与开发Pegasus间谍软件的NSO Group展开法律诉讼，后者在2019年针对1400多名WhatsApp用户(包括记者、活动家及亚马逊CEO Jeff Bezos)发起攻击，最终导致NSO Group在美国的业务受限。  
  
  
原文链接：  
  
https://www.cybersecurity-insiders.com/whatsapp-blocks-automated-downloads-to-curb-malware-spread/  
  
  
  
  
  
  
  
  
**联系我们**  
  
合作电话：18610811242  
  
合作微信：aqniu001  
  
联系邮箱：bd@aqniu.com  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAojS2Pvx0MnMjiakPQUkjUjaDia1Hj4MYj3R5vicURBTCe16tFPyegTWvYiaDyIAdHuWGKibXBp85WJfA/640?wx_fmt=gif&from=appmsg "")  
  
  
