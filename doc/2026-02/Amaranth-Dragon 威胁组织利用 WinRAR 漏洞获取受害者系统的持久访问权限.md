#  Amaranth-Dragon 威胁组织利用 WinRAR 漏洞获取受害者系统的持久访问权限  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-06 01:15  
  
**导****读**  
  
  
  
一个名为Amaranth-Dragon的复杂威胁组织对东南亚敏感目标发起一系列极具针对性的攻击，利用诱饵文件渗透敏感网络。  
  
  
该组织利用广泛使用的 WinRAR 压缩软件中的一个关键漏洞进行武器化攻击。  
  
该漏洞编号为 CVE-2025-8088，它利用路径遍历漏洞，允许攻击者通过构造恶意归档文件在受害者系统上执行任意代码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyLzDeYA0icsrETDPbtb3l8U3xsdTc5FeSbJicPzqhuTiaB5IWTJefw4HM2j4dbO4QJDbJDwf8EcY17T3jtX3PrHeyFu5icIYZ3w8oI/640?wx_fmt=png&from=appmsg "")  
  
通过利用这一弱点，攻击者可以绕过传统的安全措施，并在敏感的政府网络中建立立足点，有效地将标准管理工具变成绕过标准安全协议的入侵途径。  
  
  
感染过程通常始于传播这些带有恶意 RAR 文件的压缩包，很可能是通过鱼叉式网络钓鱼电子邮件传播，目的是诱使受害者打开附件。  
  
  
一旦归档文件被处理，该漏洞就会触发一系列操作，将恶意脚本直接放入系统的启动文件夹中。这样可以确保恶意软件在受害者每次重启计算机时自动执行，从而使攻击者无需管理员权限即可持久存在。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyKk2p9OzvlEkubNiay6D7ul2l69P4XEpyLAlVchplv4vB53rsYiadzBicrajtOiczdZVJnEPoqShOPGXJrglPaJwrmGfCHFKlak5KM/640?wx_fmt=png&from=appmsg "")  
  
  
在首次入侵成功后，攻击者部署了一种名为 Amaranth Loader 的自定义有效载荷。  
  
  
该加载器负责从命令与控制服务器检索加密的有效载荷，这些服务器通常受到 Cloudflare 等合法服务的保护，以逃避检测。  
  
  
最终目标是部署 Havoc 框架，这是一个开源的后渗透工具，它赋予攻击者持久的远程控制权和窃取敏感数据的能力。  
  
  
该攻击的技术执行很大程度上依赖于对 RAR 压缩包内文件路径的精确操控。当用户尝试提取恶意文件时，CVE-2025-8088 漏洞无法正确清理目标路径。这一漏洞使得攻击者能够将文件写入预期提取文件夹之外的地方。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyLQXD750P51G3brdXnv0rSJP4hKP5C1YoFiaM0NYIGGicmySDwDk3ianMVnKSrIdBnmqRjsQw82fWcf9IPWgDHul0EjvC42QEekiaY/640?wx_fmt=png&from=appmsg "")  
  
  
恶意批处理文件或命令文件一旦植入，就会一直处于休眠状态，直到下次系统重启。  
  
  
重启后，该脚本会执行并通过合法的可执行文件侧载 Amaranth Loader，从而有效地掩盖恶意活动，使其不被普通观察者发现，并允许威胁行为者保持长期访问权限。  
  
  
为了抵御这些有针对性的威胁，各组织必须优先立即修补WinRAR 漏洞。  
  
  
技术报告：  
  
《Amaranth Loader  
  
将 CVE-2025-8088 武器化用于东南亚的定向间谍活动》  
  
https://research.checkpoint.com/2026/amaranth-dragon-weaponizes-cve-2025-8088-for-targeted-espionage/  
  
  
新闻链接：  
  
https://cybersecuritynews.com/amaranth-dragon-exploiting-winrar-vulnerability/  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
曹县APT  
37   
利用LNK文件部署复杂的恶意软件针对专注于半岛事务的专业人士  
  
https://gbhackers.com/chollima-apt-hackers/  
  
  
俄罗斯 APT28 利用微软 Office 漏洞发起恶意软件攻击  
  
https://www.helpnetsecurity.com/2026/02/03/russian-hackers-are-exploiting-recently-patched-microsoft-office-vulnerability-cve-2026-21509/  
  
  
Mustang Panda黑客组织利用虚假外交简报安装监控工具  
  
https://hackread.com/chinese-mustang-panda-briefing-spy-diplomat/  
  
  
Amaranth-Dragon利用 WinRAR 漏洞进行间谍活动  
  
https://thehackernews.com/2026/02/china-linked-amaranth-dragon-exploits.html  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
Interlock勒索软件利用游戏反作弊驱动程序  
0day  
工具，禁用EDR和AV系统  
  
https://cybersecuritynews.com/interlock-ransomware-actors-new-tool-exploiting-gaming-anti-cheat-driver-0-day/  
  
  
PhantomVAI 自定义加载器使用 RunPE 工具攻击用户  
  
https://cybersecuritynews.com/phantomvai-custom-loader/  
  
  
SystemBC僵尸网络劫持了全球1万台设备用于DDoS攻击  
  
https://cybersecuritynews.com/systembc-botnet-hijacked-10000-devices/  
  
  
GreyNoise 发现一个使用 63000 多个住宅代理和 AWS 的双模式 Citrix Gateway 侦察活动  
  
https://securityaffairs.com/187615/hacking/greynoise-tracks-massive-citrix-gateway-recon-using-63k-residential-proxies-and-aws.html  
  
  
ValleyRAT伪装成LINE安装程序攻击用户窃取登录信息  
  
https://cybersecuritynews.com/valleyrat-mimic-as-line-installer-attacking-users/  
  
  
微软报告：信息窃取恶意软件已从 Windows 扩展到 macOS  
  
https://securityaffairs.com/187608/security/microsoft-info-stealing-malware-expands-from-windows-to-macos.html  
  
  
借助  
AI  
辅助，AWS入侵者在不到10分钟的时间内获得管理员权限  
  
https://www.theregister.com/2026/02/04/aws_cloud_breakin_ai_assist/  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
VMware ESXi 中的 CVE-2025-22225 漏洞现已被用于勒索软件攻击  
  
https://securityaffairs.com/187637/security/cve-2025-22225-in-vmware-esxi-now-used-in-active-ransomware-attacks.html  
  
  
Chrome漏洞允许攻击者执行任意代码并导致系统崩溃  
  
https://cybersecuritynews.com/chrome-vulnerabilities-arbitrary-code-2/  
  
  
SolarWinds Web Help Desk 严重漏洞遭受攻击  
  
https://www.theregister.com/2026/02/04/critical_solarwinds_web_help_desk/  
  
  
n8n AI 工作流自动化平台的两大关键缺陷可能导致完全接管  
  
https://www.infosecurity-magazine.com/news/two-critical-flaws-in-n8n-ai/  
  
  
研究人员披露了Docker AI助手的一个已修复漏洞，该漏洞可执行代码  
  
https://www.cysecurity.news/2026/02/researchers-disclose-patched-flaw-in.html  
  
  
ASUSTOR NAS 存在严重安全漏洞，可导致设备完全被控制  
  
https://gbhackers.com/critical-asustor-nas-security-flaw/  
  
  
TP-Link漏洞使黑客能够完全控制设备  
  
https://gbhackers.com/tp-link-vulnerabilities/  
  
  
Ingress-NGINX漏洞可导致任意代码执行攻击  
  
https://gbhackers.com/ingress-nginx-flaw/  
  
  
Django 严重漏洞允许发起拒绝服务攻击和 SQL 注入攻击  
  
https://gbhackers.com/critical-django-flaw/  
  
  
黑客利用 React Native CLI 的漏洞在公开披露前部署了 Rust 恶意软件  
  
https://securityaffairs.com/187587/hacking/hackers-abused-react-native-cli-flaw-to-deploy-rust-malware-before-public-disclosure.html  
  
****  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
