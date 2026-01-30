#  安全热点周报：微软 Office 零日漏洞允许恶意文档绕过安全检查  
 奇安信 CERT   2026-01-30 09:34  
  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 4px solid rgb(68, 117, 241);visibility: visible;"><th align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;background: rgb(254, 254, 254);max-width: 100%;box-sizing: border-box !important;font-size: 20px;line-height: 1.2;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgb(68, 117, 241);visibility: visible;"><strong style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 17px;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">安全资讯导视 </span></span></strong></span></th></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">国家网信办《金融信息服务数据分类分级指南》公开征求意见</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">波兰电网险遭大停电细节披露：数十处电站通信设备被攻击瘫痪</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">高端运动品牌安德玛7200万用户个人信息疑似泄露，官方称正在调查</span></p></td></tr></tbody></table>  
  
**PART****0****1**  
  
  
**漏洞情报**  
  
  
**1.Fortinet多款产品身份认证绕过漏洞安全风险通告**  
  
  
1月28日，奇安信CERT监测到Fortinet 多款产品身份认证绕过漏洞(CVE-2026-24858)在野利用，该漏洞源于FortiCloud单点登录（SSO）功能中的身份验证逻辑缺陷，当设备启用FortiCloud SSO认证时，攻击者可利用自身合法的FortiCloud账户及已注册设备，绕过正常身份认证机制，直接登录到其他用户账号下注册的设备。尽管SSO功能默认关闭，但在管理员通过设备 GUI 注册FortiCare服务时，若未手动禁用“Allow administrative login using FortiCloud SSO”选项，该功能将自动启用。成功利用此漏洞后，可获取目标设备的管理员权限，执行下载设备配置文件、创建本地管理员账号等恶意操作，进而实现对内部网络的深度渗透。目前该漏洞已发现在野利用。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。  
  
  
**2.SmarterTools SmarterMail远程代码执行漏洞安全风险通告**  
  
  
1月28日，奇安信CERT监测到官方修复SmarterTools SmarterMail远程代码执行漏洞(CVE-2026-24423)，该漏洞源于ConnectToHub API接口未对访问者进行身份验证。攻击者可通过构造特定请求，诱导SmarterMail服务器指向恶意HTTP服务器，进而向SmarterMail返回恶意操作系统命令。攻击者可以远程执行任意命令，完全控制受影响的系统，导致数据泄露、服务中断等严重后果。奇安信鹰图资产测绘平台数据显示，该漏洞关联的全球风险资产总数为40581个，关联IP总数为19693个。目前该漏洞PoC和技术细节已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。  
  
  
**3.Microsoft Office安全功能绕过漏洞安全风险通告**  
  
  
1月27日，奇安信CERT监测到官方修复Microsoft Office安全功能绕过漏洞(CVE-2026-21509)，该漏洞产生的原因是Microsoft Office在进行安全决策时依赖了不可信的输入数据。该漏洞存在于Microsoft Office的OLE（对象链接与嵌入）安全缓解措施中，攻击者可以通过构造恶意Office文档绕过用于保护用户免受脆弱COM/OLE控件侵害的安全机制。目前该漏洞已存在在野利用。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。  
  
  
**PART****0****2**  
  
  
**新增在野利用**  
  
  
**1.Ivanti Endpoint Manager Mobile 代码注入漏洞(CVE-2026-1281、CVE-2026-1340)******  
  
  
1月30日，Ivanti 披露了 Ivanti Endpoint Manager Mobile (EPMM) 中的两个严重漏洞，编号分别为 CVE-2026-1281 和 CVE-2026-1340，这些漏洞已被用于零日攻击。  
  
这两个漏洞均属于代码注入漏洞，允许远程攻击者在未经身份验证的情况下在易受攻击的设备上执行任意代码，从而使攻击者能够访问存储在该平台上的各种信息。此信息包括管理员和用户名、用户名和电子邮件地址，以及有关受管移动设备的信息，例如电话号码、IP 地址、已安装的应用程序和设备标识符（如 IMEI 和 MAC 地址）。如果启用位置跟踪，攻击者还可以访问设备位置数据，包括 GPS 坐标和最近的基站位置。CVSS 评分均为 9.8，被评为严重级别。Ivanti 警告称，目前只知道极少数客户的解决方案在披露时遭到了利用。  
  
Ivanti 称，这两个漏洞都是通过内部应用程序分发和 Android 文件传输配置功能触发的，尝试或成功的利用记录会出现在 Apache 访问日志中/var/log/httpd/https-access_log。攻击者还可以使用 EPMM API 或 Web 控制台对设备进行配置更改，包括身份验证设置。这两个漏洞都被用作零日漏洞利用，但由于已知受影响的客户数量较少，该公司没有可靠的入侵指标（IOC）。  
  
该公司发布了有关检测漏洞利用和漏洞利用后行为的技术指南，管理员可以使用这些指南。应用补丁不需要停机时间，也不会对功能造成影响，因此强烈建议尽快应用这些补丁。不过，热修复程序在版本升级后会失效，如果设备在永久修复程序可用之前升级，则必须重新应用这些热修复程序。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/ivanti-warns-of-two-epmm-flaws-exploited-in-zero-day-attacks/  
  
  
**2.Fortinet 多款产品身份认证绕过漏洞(CVE-2026-24858)******  
  
  
1月27日，Fortinet 已确认存在一个新的、正在被积极利用的 FortiCloud 单点登录 (SSO) 身份验证绕过漏洞，编号为 CVE-2026-24858，并表示已通过阻止运行易受攻击固件版本的设备建立 FortiCloud SSO 连接来缓解零日攻击。  
  
该漏洞允许攻击者滥用 FortiCloud SSO 来获取对其他客户注册的 FortiOS、FortiManager 和 FortiAnalyzer 设备的管理权限，即使这些设备已针对先前披露的漏洞进行了完全修复。  
  
此前， Fortinet 客户于1月21日报告称其 FortiGate 防火墙遭到入侵，攻击者通过 FortiCloud SSO 在运行最新可用固件的设备上创建新的本地管理员帐户。随后，Fortinet 证实了这一消息。最初人们认为这些攻击是通过绕过 CVE-2025-59718 的补丁实现的，CVE-2025-59718 是一个之前被利用的严重 FortiCloud SSO 身份验证绕过漏洞，该漏洞已于2025年12月修复。  
  
Fortinet 管理员报告称，黑客使用电子邮件地址 cloud-init@mail.io 通过 FortiCloud SSO 登录到 FortiGate 设备，然后创建新的本地管理员帐户。受影响客户分享的日志显示了与12月份攻击期间观察到的类似迹象。1月22日，网络安全公司 Arctic Wolf 证实了这些攻击，并表示攻击似乎是自动化的，攻击者在几秒钟内就创建新的恶意管理员账户和启用 VPN 的账户，并窃取了防火墙配置。  
  
Fortinet 的安全公告指出，CVE-2026-24858 漏洞的利用源于两个 FortiCloud 账户，这两个账户已于1月22日被 Fortinet 禁用。但 Fortinet 在1月26日采取了更为严格的措施，暂时禁用了所有账户和设备的 FortiCloud 单点登录功能，以阻止恶意登录。Fortinet 于1月27日重新启用了该功能，但不再支持从运行存在 CVE-2026-24858 漏洞的设备版本登录。该公告指出，目前无需在客户端禁用 FortiCloud SSO 登录。Fortinet 敦促客户将所有运行 FortiOS、FortiManager、FortiAnalyzer、FortiProxy 和 FortiWeb 的设备升级到已修复的版本。根据公告，Fortinet 正在调查 FortiSwitch Manager 是否存在 CVE-2026-24858 漏洞。  
  
Fortinet 建议检查所有管理员帐户，从已知干净的备份中恢复配置，并轮换所有凭据。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/fortinet-blocks-exploited-forticloud-sso-zero-day-until-patch-is-ready/  
  
  
**3.Microsoft Office 安全功能绕过漏洞(CVE-2026-21509)******  
  
  
1月26日，微软针对 Office 中的一个高危零日漏洞发布了紧急补丁，该漏洞允许攻击者绕过文档安全检查，并且正在被恶意文件利用。  
  
微软针对零日漏洞（编号为 CVE-2026-21509）推送了紧急补丁，并将其归类为“Microsoft Office 安全功能绕过漏洞”，CVSS 评分为 7.8 分。该安全功能绕过漏洞（编号为CVE-2026-21509）会影响多个 Office 版本，包括 Microsoft Office 2016、Microsoft Office 2019、Microsoft Office LTSC 2021、Microsoft Office LTSC 2024 和 Microsoft 365 企业应用版（该公司的云订阅服务）。  
  
该漏洞允许攻击者绕过对象链接和嵌入 (OLE) 缓解措施，这些措施旨在阻止 Office 文档中不安全的 COM/OLE 控件。这意味着即使有内置保护措施，恶意附件仍可能感染计算机。  
  
在实际场景中，攻击者会创建包含隐藏“小程序”或特殊对象的伪造 Word、Excel 或 PowerPoint 文件。他们可以在受感染的计算机上运行代码并执行其他操作。通常，Office 具有安全检查功能，会阻止这些小程序，因为它们存在风险。  
  
然而，该漏洞允许攻击者篡改文件结构和隐藏信息，使 Office 误认为文档中隐藏的危险小程序是无害的。因此，Office 会跳过通常的安全检查，允许隐藏代码运行。  
  
由于用于测试绕过漏洞的代码已公开，增加了被利用的风险，因此强烈建议用户尽快应用补丁。  
  
  
参考链接：  
  
https://www.malwarebytes.com/blog/news/2026/01/microsoft-office-zero-day-lets-malicious-documents-slip-past-security-checks  
  
  
**4.GNU InetUtils telnetd 远程认证绕过漏洞(CVE-2026-24061)******  
  
  
1月26日，威胁行为者积极利用影响数十万台 Telnet 服务器的严重漏洞，这种经常被忽视的威胁途径重新成为人们关注的焦点。  
  
该安全问题编号为 CVE-2026-24061，于1月20日报告。该漏洞很容易被利用，并且有多个漏洞利用示例已公开。开源贡献者 Simon Josefsson 解释到，GNU InetUtils 的 telnetd 组件存在远程身份验证绕过漏洞，这是由于在生成“/usr/bin/login”时未清理环境变量处理造成的。该漏洞的产生是因为 telnetd 会将用户控制的 USER 环境变量直接传递给 login(1) 函数，而没有进行任何清理。攻击者可以通过将 USER 设置为-f root并使用 telnet -a 命令连接，从而绕过身份验证并获得 root 权限。  
  
GNU InetUtils 是由 GNU 项目维护的一系列经典网络客户端和服务器工具（telnet/telnetd、ftp/ftpd、rsh/rshd、ping、traceroute），并在多个 Linux 发行版中使用。尽管 Telnet 是一种不安全的旧式组件，并且已被 SSH 基本取代，但许多 Linux 和 Unix 系统仍然保留它，以兼容其他系统或满足特殊用途的需求。由于其简单易用且开销低，Telnet 在工业领域尤其普遍。在传统设备和嵌入式设备上，它可以无需更新运行超过十年，这解释了它在物联网设备、摄像头、工业传感器和运营技术 (OT) 网络中的应用。  
  
威胁监控公司 GreyNoise 报告称，已检测到利用 CVE-2026-24061 漏洞对少量易受攻击的终端进行实际攻击活动。大部分攻击活动似乎是自动化的，但也发现了一些“人工操作”的案例。攻击的终端速度、类型和 X11 DISPLAY 值各不相同，但在 83.3% 的情况下，它们的目标是“root”用户。  
  
虽然此次攻击活动的范围和成功程度似乎有限，但在攻击者优化其攻击链之前，应按照建议对可能受影响的系统进行修补或加固。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-telnetd-auth-bypass-flaw-to-get-root/  
  
  
**5.SmarterMail 身份认证绕过漏洞(CVE-2026-23760)******  
  
  
1月24日，安全研究人员警告称，在 SmarterTools SmarterMail 企业电子邮件和协作服务器的补丁发布后大约两天，威胁行为者就开始利用该服务器中的身份验证绕过漏洞。  
  
该安全缺陷被追踪为 CVE-2026-23760（CVSS 评分为 9.3），它影响应用程序的密码重置 API，并允许攻击者在未经身份验证的情况下重置密码。出现此问题的原因是，强制重置密码功能允许包含用户控制参数的未经身份验证的请求，并且不会验证管理员帐户的旧密码或重置令牌。这使得知道管理员用户名的攻击者无需身份验证即可重置帐户密码，并控制存在漏洞的 SmarterMail 实例。  
  
据 WatchTowr 称，该漏洞可被利用通过 SmarterMail 功能进行远程代码执行（RCE），该功能允许系统管理员执行操作系统命令。重置管理员帐户后，攻击者可以在设置菜单中创建一个新卷，并在“卷挂载命令”字段中添加一条命令。由于该命令由底层操作系统执行，攻击者即可实现对主机的完全远程代码执行（RCE）。  
  
WatchTowr 表示，他们已经发现 CVE-2026-23760 漏洞被广泛利用近一周，并推测威胁行为者已经逆向工程破解了该漏洞的修复方法。Huntress 也发出警告，黑客一直在利用该应用程序的系统事件功能，攻击 SmarterMail 身份验证绕过漏洞。  
  
用户应尽快将 SmarterMail 实例更新到已打补丁的版本。鉴于此漏洞的严重性、活跃的利用以及在实际环境中观察到的其他 CVE-2025-52691 漏洞的利用，企业应优先部署 SmarterMail 更新，并检查任何过时的系统是否存在感染迹象。  
  
  
参考链接：  
  
https://www.securityweek.com/fresh-smartermail-flaw-exploited-for-admin-access/  
  
**PART****0****3**  
  
  
**安全事件**  
  
  
**1.敏感气象数据或外流，国家安全部发布警示**  
  
  
1月29日国家安全部消息，国家安全部公众号推文称，部分机构与个人法律意识淡薄，违规设立涉外气象探测站（点）,导致敏感气象数据面临外流风险，给我国家安全带来威胁。某军事基地附近农田片区，突然出现了多个新建气象探测站（点），国家安全机关迅速联合气象部门开展实地调查。据当地民众反映，这些设施是A公司以“助力农业”为名建设，刚刚竣工并投入使用。经核查，这些设备主要用于采集当地全天候的降水量、光照强度、风向风速、土壤水分、空气温度湿度、EC值等数据。该公司系中外合资企业，其所建的气象探测站（点）既未向当地气象主管部门备案，也未按规定汇交探测数据，且其中某台气象探测站（点）设施的供货商为境外某公司，其数据存储服务器搭建于境外，有气象数据外泄风险。经进一步查证，A公司虽没有境外间谍情报机关背景，但其存在违法开展涉外气象探测、违法私立涉外气象探测站（点）等行为。国家安全机关立即联合有关部门依法处置并对所有违建的气象探测站（点）进行拆除。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/9tNrzQkNVSpFO50OZsrA7w  
  
  
**2.波兰电网险遭大停电细节披露：数十处电站通信设备被攻击瘫痪**  
  
  
1月28日Zero Day消息，综合Dragos、ESET等国际安全厂商的事件响应报告显示，去年12月的波兰电网险遭大停电事件，攻击者利用防火墙等边界系统漏洞，突破了可再生能源分布式电站的网络防护，劫持了远程终端单元（RTU）令其无法运行和恢复，导致大约30个电站的通信设备失效，幸运的是并未引发停电或对电力设备造成影响。波兰当局表示，如果攻击成功，可能会导致多达50万名波兰民众断电。该事件带有明显的IT、OT协同攻击特征，相关目标的IT网络还感染了数据擦除器，但不清楚攻击者是否实际启动了擦除功能来清除这些系统。  
  
  
原文链接：  
  
https://www.zetter-zeroday.com/attack-against-polands-grid-disrupted-communication-devices-at-about-30-sites/  
  
  
**3.数百个Clawdbot网关遭暴露，API密钥和私密聊天受影响**  
  
  
1月26日Cyber Security News消息，爆火的开源AI智能体网关Clawdbot正面临日益严峻的安全隐患，目前已有超过900个未设身份验证的实例暴露在互联网上，且其代码存在多处漏洞，可能导致凭据被盗或远程代码执行等后果。有研究员利用Shodan搜索引擎扫描发现，该项目短时间内出现了超过900个网关实例公网暴露，其中多数未配置身份验证机制。攻击者可通过读取权限可获取全部凭据（包括API密钥、OAuth密钥）及附带文件传输记录的完整历史会话。攻击者还能继承智能体权限，发送消息、执行工具操作，甚至通过过滤响应内容来操控用户感知。部分实例以root权限的容器形式运行，使得攻击者无需身份验证即可执行任意主机命令。  
  
  
原文链接：  
  
https://cybersecuritynews.com/clawdbot-chats-exposed/  
  
  
**4.高端运动品牌安德玛7200万用户个人信息疑似泄露，官方称正在调查**  
  
  
1月22日TechCrunch消息，在网络犯罪分子将大量条客户记录公开后，美国知名运动服装和数据公司安德玛（Under Armour）回应称，公司正在调查相关的数据泄露指控。此前数据泄露通知网站Have I Been Pwned获取到一份安德玛泄露数据副本，并通过电子邮件通知7200万名个人其信息已遭泄露。被盗数据集包含姓名、电子邮件地址、性别、出生日期，以及基于邮政编码推断出的客户大致位置等信息。据悉，这些数据源自去年11月发生的一起数据泄露事件，当时Everest勒索软件在其暗网泄密网站上声称对此负责。  
  
  
原文链接：  
  
https://techcrunch.com/2026/01/22/under-armour-says-its-aware-of-data-breach-claims-after-72m-customer-records-were-posted-online/  
  
  
**PART****0****4**  
  
  
**政策法规**  
  
  
**1.国务院办公厅印发《政务移动互联网应用程序规范化管理办法》**  
  
  
1月28日，国务院办公厅印发《政务移动互联网应用程序规范化管理办法》。该文件提出，政务应用程序的主办（使用）单位按照“谁主办谁负责、谁使用谁负责”的原则，履行建设、使用、安全管理等环节的主体责任。该文件要求，各地区各部门应落实网络安全、数据安全、关键信息基础设施安全保护、个人信息保护、密码管理、移动互联网应用程序信息服务管理等有关法律法规规定，依法依规保护数据和个人信息安全等。各地区各部门应严格遵守国家保密法律法规，完善保密自监管措施，定期开展安全保密检查和风险评估，及时发现处置违反保密法律法规行为。  
  
  
原文链接：  
  
https://www.gov.cn/zhengce/zhengceku/202601/content_7056375.htm  
  
  
**2.国家网信办《金融信息服务数据分类分级指南》公开征求意见**  
  
  
1月24日，国家互联网信息办公室会同有关部门组织起草了《金融信息服务数据分类分级指南（征求意见稿）》，现向社会公开征求意见。该文件规定了金融信息服务数据分类分级规则，适用于在中华人民共和国境内从事金融信息服务的金融信息服务提供者开展数据分类分级和重要数据识别工作。该文件提出，金融信息服务数据可按照业务属性进行分类，一级分类分为业务数据、用户数据和企业数据3类，进一步细分为二级分类9类、三级分类66类。文件附录还给出了三级分类数据的分类分级参考示例。  
  
  
原文链接：  
  
https://www.cac.gov.cn/2026-01/24/c_1770812246428118.htm  
  
  
**3.美国白宫发布备忘录，调整政府供应商软硬件产品安全证明要求**  
  
  
1月23日，美国白宫管理与预算办公室（OMB）发布M-26-05《采用基于风险的软件和硬件安全方法》备忘录，撤销了2022年网络安全行政令的一项规定，要求联邦机构使用单一、标准化的自我证明表格，从软件供应商获取网络安全保障情况信息。白宫表示，这一政策妨碍了各机构根据自身系统需求采用合适的安全解决方案。该备忘录要求，联邦机构应改为运用安全开发原则，基于全面的风险评估，来验证供应商的安全性，并允许联邦机构采用软件证明表格或软件物料清单来管理供应链安全。  
  
  
原文链接：  
  
https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf  
  
  
**往期精彩推荐**  
  
  
[年度报告 | 2025年漏洞态势全景复盘！](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504619&idx=1&sn=2b304680299a0a0b75bfeddca8b596ac&scene=21#wechat_redirect)  
  
  
[【已复现】SmarterTools SmarterMail 远程代码执行漏洞(CVE-2026-24423)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504548&idx=1&sn=3ec06d42760edb5b95e85ea6888dae63&scene=21#wechat_redirect)  
  
  
[【在野利用】Fortinet 多款产品身份认证绕过漏洞(CVE-2026-24858)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504548&idx=2&sn=82db7c283ba71172c1615913d7671f48&scene=21#wechat_redirect)  
  
  
  
  
本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！  
  
  
  
  
  
  
  
