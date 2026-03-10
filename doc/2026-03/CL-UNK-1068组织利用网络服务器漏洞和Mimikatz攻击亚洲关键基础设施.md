#  CL-UNK-1068组织利用网络服务器漏洞和Mimikatz攻击亚洲关键基础设施  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-03-10 01:01  
  
**导****读**  
  
  
  
南亚、东南亚和东亚的高价值组织成为威胁组织长达数年的攻击目标。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyLnrcCIq7pOevs4Mia4aH4spyxpIPG9ZpkM09gVDQuVR2ryKpFXhn1lib8NNOLUHLHzcvFRv1FkfjevpzJ7rWKWcSTmXbhwQZxTw/640?wx_fmt=png&from=appmsg "")  
  
  
该活动影响航空、能源、政府、执法、制药、技术和电信行业，Palo Alto Networks 42   
Unit   
将其归咎于一个此前未被记录在案的威胁组织，该组织被命名为CL-UNK-1068。  
  
  
“CL”指的是“集群”，“UNK”指的是未知动机。  
  
  
Palo Alto Networks 42   
Unit   
以“中等到高度的信心”评估认为，此次攻击活动的主要目标是网络间谍活动。  
  
  
安全研究员汤姆·法克特曼表示： “我们的分析揭示了一套多方面的工具，包括定制恶意软件、修改后的开源实用程序和本地资源利用二进制文件（LOLBIN）。这些工具为攻击者提供了一种简单有效的方法，使其能够在目标环境中保持持久存在。”  
  
  
这些工具旨在攻击 Windows 和 Linux 环境，攻击者依赖于开源实用程序和恶意软件家族（如Godzilla、ANTSWORD、Xnote 和 Fast Reverse Proxy ( FRP )）的组合，所有这些已被各种黑客组织使用。  
  
  
Godzilla 和 ANTSWORD 都以 Web Shell 的形式运行，Xnote 是一个 Linux 后门，自 2015 年以来一直在野外被发现，并被一个名为Earth Berberoka（又名GamblingPuppet ）的敌对组织部署，用于攻击在线赌博网站。  
  
  
典型的攻击链包括利用 Web 服务器提供 Web Shell 并横向移动到其他主机，然后尝试从 Windows Web 服务器的“c:\inetpub\wwwroot”目录中窃取与某些扩展名匹配的文件（“web.config”、“.aspx”、“.asmx”、“.asax”和“.dll”），可能是为了窃取凭据或发现漏洞。  
  
  
CL-UNK-1068 收集的其他文件包括网页浏览器历史记录和书签、桌面和用户目录中的 XLSX 和 CSV 文件，以及 MS-SQL 服务器中的数据库备份 (.bak) 文件。  
  
  
该威胁组织使用 WinRAR 归档相关文件，通过执行 certutil -encode 命令对归档文件进行 Base64 编码，然后运行   
  
type 命令，通过 web shell 将 Base64 内容打印到屏幕上。攻击者将存档文件编码为文本并打印到屏幕上，从而在不实际上传任何文件的情况下窃取了数据。  
  
  
这些攻击中使用的技术之一是使用合法的 Python 可执行文件（“python.exe”和“pythonw.exe”）发起 DLL 侧加载攻击，并悄悄执行恶意 DLL，包括用于持久访问的 FRP、PrintSpoofer和名为 ScanPortPlus 的基于 Go 的自定义扫描器。  
  
  
据称，CL-UNK-1068 早在 2020 年就使用名为 SuperDump 的自定义 .NET 工具进行侦察活动。最近的入侵活动已转向一种新方法，即使用批处理脚本来收集主机信息并绘制本地环境图。  
  
  
攻击者还利用各种工具来窃取凭证：  
- 使用 Mimikatz 从内存中导出密码  
- 使用LsaRecorder将LsaApLogonUserEx2连接到 WinLogon 密码记录器。  
- 使用DumpItForLinux和Volatility Framework从内存中提取密码哈希值  
- SQL Server Management Studio 密码导出工具，用于提取“sqlstudio.bin”的内容，该文件存储 Microsoft SQL Server      Management Studio (SSMS) 的连接信息。  
  
该组织主要利用开源工具、社区共享的恶意软件和批处理脚本，成功地在渗透关键组织的同时保持了隐蔽行动。  
  
  
这一系列活动展现了其在Windows和Linux环境下的多功能性，并针对不同的操作系统使用了不同版本的工具集。虽然其主要目标是窃取凭证和从关键基础设施和政府部门窃取敏感数据，这强烈暗示了间谍活动的动机。  
  
  
技术报告：  
  
《对多年来针对高价值行业的未被发现的活动调查》  
  
https://unit42.paloaltonetworks.com/cl-unk-1068-targets-critical-sectors/  
  
  
新闻链接：  
  
https://thehackernews.com/2026/03/web-server-exploits-and-mimikatz-used.html  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
与伊朗有关联的黑客将目标对准美国关键基础设施  
  
https://cybersecuritynews.com/iran-linked-hackers-target-u-s-critical-infrastructure/  
  
  
亲伊朗黑客组织与其他  
APT  
组织联手，攻击美国、以色列  
  
https://securityboulevard.com/2026/03/pro-iranian-hacktivists-join-nation-state-groups-in-targeting-u-s-israel-others/  
  
  
曹县UNC4899 黑客攻击加密货币相关公司  
  
https://thehackernews.com/2026/03/unc4899-used-airdrop-file-transfer-and.html  
  
  
Transparent Tribe（APT36）正从传统的现成工具转向  
AI  
辅助的恶意软件模型  
  
https://gbhackers.com/transparent-tribes-vibeware/  
  
  
网络间谍组织CL-UNK-1068以利用网络服务器漏洞和Mimikatz攻击亚洲关键基础设施  
  
https://thehackernews.com/2026/03/web-server-exploits-and-mimikatz-used.html  
  
  
CheckPoint  
报告：APT 组织在中东地区的活动有所增加  
  
https://blog.checkpoint.com/research/china-nexus-activity-against-qatar-observed-amid-expanding-regional-tensions/  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
恶意 Chrome 扩展程序针对 imToken 钱包用户  
  
https://www.esecurityplanet.com/threats/malicious-chrome-extension-targets-imtoken-wallet-users/  
  
  
BoryptGrab窃取器通过虚假GitHub仓库传播，窃取浏览器和加密钱包数据  
  
https://cybersecuritynews.com/boryptgrab-stealer-spreads-via-fake-github-repositories/  
  
  
MaaS VIP键盘记录器攻击活动利用隐写术和内存执行技术大规模窃取凭证  
  
https://cybersecuritynews.com/maas-vip-keylogger-campaign-uses-steganography/  
  
  
虚假 CleanMyMac 网站诱骗 macOS 用户安装 SHub Stealer 恶意软件  
  
https://hackread.com/fake-cleanmymac-site-clickfix-shub-stealer-macos/  
  
  
虚 Claude Code 安装页面会利用信息窃取程序攻击 Windows 和 Mac 用户  
  
https://www.malwarebytes.com/blog/news/2026/03/fake-claude-code-install-pages-hit-windows-and-mac-users-with-infostealers  
  
  
MaaS VIP键盘记录器攻击活动利用隐写术大规模窃取凭证  
  
https://gbhackers.com/maas-vip-keylogger-campaign/  
  
  
恶意 npm 包伪装成 OpenClaw 安装程序，部署远程访问木马 (RAT)，窃取 macOS 凭据  
  
https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html  
  
  
AI 对战 AI：智能体仅用两小时就入侵了麦肯锡的聊天机器人，并获得了完整的读写权限  
  
https://www.theregister.com/2026/03/09/mckinsey_ai_chatbot_hacked/  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
AVideo零点击漏洞使攻击者能够劫持直播流  
  
https://www.esecurityplanet.com/threats/avideo-zero-click-flaw-lets-attackers-hijack-live-streams/  
  
  
研究人员发现 Foxit 和 Apryse PDF 平台存在严重  
0day  
漏洞  
  
https://www.cysecurity.news/2026/03/researchers-find-critical-zero-day.html  
  
  
Apache ZooKeeper漏洞将敏感数据暴露给攻击者  
  
https://gbhackers.com/apache-zookeeper-flaw/  
  
  
ExifTool漏洞允许恶意图片触发macOS代码执行  
  
https://gbhackers.com/exiftool-vulnerability/  
  
****  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
