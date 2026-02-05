#  工信部：关于防范Microsoft Office安全功能绕过高危漏洞的风险提示；网络攻击新手法：签名合法驱动被利用，59款EDR/防护软件遭终止| 牛览  
 安全牛   2026-02-05 03:58  
  
**点击蓝字 关注我们**  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBal13S24uhmJl8yJA8ushe4TJGWtdFDzT8bic4PfVUhMFWB6nqZRDJaSCavgHkXZib91QNIE3sBItA/640?wx_fmt=png&from=appmsg "")  
  
  
新闻速览  
  
- 工信部：关于防范Microsoft Office安全功能绕过高危漏洞的风险提示  
  
  
- Avast推出Deepfake Guard：在普通PC上实时拦截AI诈骗视频  
  
  
- 全国网络安全标准化技术委员会秘书处发布网络数据标签标识技术要求实践指南通知  
  
  
- Chrome浏览器曝侧信道漏洞：扩展可通过时序攻击窃取任意标签页完整URL  
  
  
- 8分钟接管云环境：AI正在把云入侵变成“流水线作业”  
  
  
- 当恶意软件“寄生”AI平台：多态安卓RAT滥用Hugging Face窃密  
  
  
- 网络攻击新手法：签名合法驱动被利用，59款EDR/防护软件遭终止  
  
  
- Docker AI助手变“后门”？DockerDash漏洞致远程代码执行  
  
  
- 特朗普政府网络安全新进展：六大支柱战略与AI安全协作体系  
  
  
- Gartner警告：AI失控、量子威胁与合规压力并行，2026年六大安全挑战重塑防御策略  
  
特别关注  
  
  
**工信部：关于防范Microsoft Office安全功能绕过高危漏洞的风险提示**  
  
近日，工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）监测发现，Microsoft Office存在安全功能绕过高危漏洞，已被用于网络攻击。  
  
  
Microsoft Office是美国微软公司开发的一套办公软件，提供文档处理、电子表格计算、演示制作等功能。由于Office在安全决策环节错误依赖不可信输入数据，攻击者可构造恶意Office文件并诱使用户打开，绕过本地安全功能，进而执行恶意代码。受影响版本包括32位和64位的Microsoft Office 2016/2019、Microsoft Office LTSC 2021/2024、Microsoft 365 Apps for Enterprise。  
  
  
目前，微软官方已修复该漏洞并发布更新公告（URL链接:https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21509），建议相关单位和用户立即开展隐患排查，及时升级至最新安全版本，或采取修改注册表（针对Office 2016和2019）、重启Office应用程序（针对Office 2021及后续版本）等临时措施，防范网络攻击风险。  
  
  
原文链接：  
  
https：//www.secrss.com/articles/87611  
  
  
热点观察  
  
  
**全国网络安全标准化技术委员会秘书处发布网络数据标签标识技术要求实践指南通知**  
  
依据《网络安全法》《数据安全法》《个人信息保护法》《网络数据安全管理条例》等法律法规要求，为指导网络数据处理者使用网络数据标签标识技术提高网络数据安全管理水平，秘书处组织编制了《网络安全标准实践指南——网络数据标签标识技术要求》。  
  
  
本《实践指南》提出了网络数据标签标识技术的术语和定义、属性格式、生成规则、打标规则、验标规则、日志留存要求、安全防护要求等内容，可用于帮助网络数据处理者对数据进行标签标识，在此基础上重点对重要数据和个人信息进行分类分级保护，加强数据全周期全过程溯源管理。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/1S6DmVR-G9s7wAeskLcp5A  
  
  
**8分钟接管云环境：AI正在把云入侵变成“流水线作业”**  
  
安全研究团队Sysdig披露了一起由AI辅助完成的云环境入侵事件，攻击者从发现暴露的AWS凭证到获得完整控制权，仅用了约8分钟。事件发生于2025年11月28日，攻击起点是一组意外暴露在公网S3存储桶中的测试凭证，该凭证虽仅具备ReadOnlyAccess权限，但已足以用于环境侦察。  
  
  
攻击者利用该权限快速枚举数据库、IAM角色和密钥信息，并通过代码注入劫持AWS Lambda函数，最终创建并接管名为“frick”的管理员账户，实现权限升级。Sysdig分析认为，攻击流程高度自动化，代码生成速度远超人工操作，且包含塞尔维亚语注释，显示攻击者可能借助大语言模型（LLM）执行攻击步骤。  
  
  
在取得控制权后，攻击者进一步滥用受害者账户运行Claude 3.5 Sonnet等高成本AI模型，并尝试部署名为“stevan-gpu-monster”的GPU实例，单月潜在成本超过1.8万英镑。同时，攻击者通过IP轮换和多重身份隐藏行踪，并尝试跨账户横向移动。  
  
  
研究人员指出，凭证暴露仍是根本问题，但AI显著压缩了攻击时间窗口，企业需加强IAM最小权限控制、密钥管理及异常行为监测，以应对“AI加速型”云攻击的新常态。  
  
  
原文链接：  
  
https://hackread.com/8-minute-takeover-ai-hijack-cloud-access/  
  
  
**当恶意软件“寄生”AI平台：多态安卓RAT滥用Hugging Face窃密**  
  
Bitdefender研究人员披露，一起针对安卓用户的恶意攻击活动正在滥用AI协作平台Hugging Face分发远程访问木马（RAT）。攻击者将恶意载荷托管在Hugging Face数据集之中，借助其可信声誉绕过传统安全检测，形成新型供应链式攻击路径。  
  
  
该恶意程序通常伪装为名为TrustBastion或Premium Club的应用，并模拟Google Play Store更新界面诱导用户安装。应用运行后会从Hugging Face下载真正的间谍组件，从而在初始安装阶段避开静态扫描。研究显示，攻击者采用服务器端多态技术，每15分钟生成不同的APK版本，使样本哈希持续变化，显著降低杀毒引擎命中率。  
  
  
在权限获取阶段，恶意软件伪装成“手机安全组件”，诱导用户授予辅助功能权限。一旦授权，RAT即可执行屏幕监控、按键记录、短信与银行凭证窃取等操作，并实现远程控制。  
  
  
研究人员指出，攻击并非利用Hugging Face本身的漏洞，而是滥用其开放托管与内容审核不足的特点。随着AI与开源平台成为开发和协作基础设施，安全团队需将此类平台纳入威胁建模与监控范围，防止“可信平台被劫持”成为常态化攻击手段。  
  
  
原文链接：  
  
https://securityonline.info/ai-hub-hijacked-polymorphic-android-rat-abuses-hugging-face-to-steal-data/  
  
  
**特朗普政府网络安全新进展：六大支柱战略与AI安全协作体系**  
  
美国特朗普政府近期在联邦网络安全政策上发布了多项重要进展，涵盖国家战略、法规修订与行业协作等关键领域。报道称，白宫正推进一份包含六大支柱的国家网络安全战略，重点包括塑造对手行为、优化监管环境、强化联邦系统与关键基础设施安全、提升新兴技术防护能力，以及缓解人才短缺等方向。  
  
  
在实施层面，Cybersecurity and Infrastructure Security Agency（CISA）将推出《关键基础设施网络事件报告法案（CIRCIA）》的最终规则，要求跨行业实体在攻击发生后72小时内向CISA报告网络事件。该规则的最终发布时间已从2025年10月推迟至2026年5月，引发业界关注。  
  
  
此外，政府正推动建立AI-ISAC（人工智能信息共享与分析中心），旨在联邦与行业间共享AI安全威胁情报，避免政府与私营部门间出现重复或孤岛式情报通道。国家网络总监办公室还在制定AI安全政策框架，强调在推动AI创新的同时将安全机制纳入基础架构。  
  
  
总体来看，这些举措反映出美国在国家网络安全布局上正从单一监管向战略导向、跨部门协作和技术融合转变，业界需持续关注法规落地时间表与实施细则。  
  
  
原文链接：  
  
https：//federalnewsnetwork.com/cybersecurity/2026/02/five-updates-on-the-trump-admins-cybersecurity-agenda/  
  
  
安全事件  
  
  
**网络攻击新手法：签名合法驱动被利用，59款EDR/防护软件遭终止**  
  
近期安全研究发现，攻击者在恶意“EDR Killer”工具中滥用原本属于EnCase取证软件的合法内核驱动，用于绕过并终止终端检测与响应（EDR）及防病毒软件进程。该驱动虽曾获得签名，但证书已被撤销和过期，仍被Windows内核接受，成为攻击者获取内核级权限的跳板。  
  
  
这种工具采用常见的“Bring Your Own Vulnerable Driver（BYOVD）”技术，将旧驱动伪装成固件更新服务安装，并通过其IOCTL接口循环检测与终止目标安全进程，覆盖多达59款EDR/杀软。由于驱动注册为伪造的OEM硬件服务，它能实现重启持久化，并规避Windows如PPL等保护措施。  
  
  
据分析，本次入侵始于远程VPN凭证泄露并缺乏多因素认证，随后攻击者内部横向探测并部署该EDR Killer。防御建议包括：对远程访问启用MFA、强化内核完整性（如HVCI/Memory Integrity）、监控伪装为硬件服务的内核驱动，并利用WDAC/ASR策略阻断可疑签名驱动。  
  
  
如需进一步提升检测能力，企业应结合内核态行为分析与终端威胁狩猎机制，以应对此类利用合法组件的高级规避手法。  
  
  
原文链接：  
  
https：//www.bleepingcomputer.com/news/security/edr-killer-tool-uses-signed-kernel-driver-from-forensic-software/  
  
  
**Docker AI助手变“后门”？DockerDash漏洞致远程代码执行**  
  
近日安全研究机构披露，Docker旗下AI助手Ask Gordon存在关键安全缺陷（代号DockerDash），可导致远程代码执行（RCE）和敏感数据泄露。该漏洞根源于MCP Gateway上下文信任机制的设计缺陷：系统未对来自Docker镜像元数据的指令进行严格验证，导致恶意指令被误认为合法上下文并传递给MCP工具执行。  
  
  
具体来说，攻击者可以将恶意指令隐藏在Docker镜像标签或描述元数据中，当Ask Gordon处理这些信息时，会将其视为正常请求并下发执行命令。对于Docker Desktop或CLI环境，这可能触发远程代码执行；在桌面环境中则可被滥用为数据窃取载体，泄露如构建日志、API密钥和内部网络信息等敏感内容。  
  
  
安全团队指出，此类漏洞反映了AI集成开发工具在供应链威胁面前的脆弱性，传统信任边界、白名单等机制难以应对“元上下文注入（meta-context injection）”攻击。SecurityWeek Docker已在Docker Desktop 4.50.0中修复该问题，通过引入人工确认和执行前验证等措施限制潜在滥用。  
  
  
这一事件提醒安全从业者，在引入AI助手及自动化工具时务必加强输入验证、最小权限控制及供应链风险治理。  
  
  
原文链接：  
  
https://www.securityweek.com/dockerdash-flaw-in-docker-ai-assistant-leads-to-rce-data-theft/  
  
  
攻防技术  
  
  
**Chrome浏览器曝侧信道漏洞：扩展可通过时序攻击窃取任意标签页完整URL**  
  
安全研究人员在Chrome浏览器中发现一种新型侧信道攻击方法,允许恶意扩展在未获得标签页或网站访问权限的情况下,提取任意打开标签页的完整URL,包括其中的敏感参数。  
  
  
该漏洞利用declarativeNetRequest API的时序特性。该API通常被视为相对安全,仅用于请求拦截规则,不直接读取页面内容。但研究显示,扩展可通过动态规则阻止特定URL模式的请求,利用被阻止请求(返回net：：ERR_BLOCKED_BY_CLIENT,耗时10-30毫秒)与正常加载请求(耗时50-100毫秒以上)的时间差异,配合chrome.tabs.reload和chrome.tabs.onUpdated事件监听,实现URL的逐字符提取。  
  
  
攻击者通过二分查找算法构造正则表达式规则,测试URL每个位置的字符,根据页面重载时间判断规则是否匹配,最终完整还原地址。整个过程无需用户交互且难以察觉。  
  
  
此漏洞可泄露OAuth授权码(如https://accounts.google.com/callback?code=secret)、会话ID、API密钥、密码重置令牌以及Google Drive、Dropbox等私有链接,甚至医疗或金融相关的搜索查询。  
  
  
代码分析显示,问题源于Chromium仓库提交1539dcc828ee,该提交为declarativeNetRequest添加了正则表达式评估功能。漏洞影响Chrome Stable 144.0.7559.97、Beta、Dev和Canary等多个版本,已在Windows 11环境下验证。  
  
  
原文链接：  
  
https：//www.securitylab.ru/news/568934.php  
  
  
产业动态  
  
  
**Gartner警告：AI失控、量子威胁与合规压力并行，2026年六大安全挑战重塑防御策略**  
  
Gartner在2026年网络安全趋势报告中指出，AI快速普及、地缘政治紧张、监管环境不稳定及威胁加速演进，正在重塑企业网络安全格局。首先，Agentic AI与无代码/低代码开发推动AI代理泛滥，带来新的攻击面和合规风险，亟需统一治理与事件响应机制。其次，全球监管波动使网络安全直接关联企业韧性，董事会与高管的合规责任被显著强化。第三，量子计算进展预计2030年前将破坏现有非对称加密体系，组织需提前部署后量子密码，应对“先收集、后解密”攻击。第四，AI代理的兴起要求IAM体系向机器身份、自动凭证和策略授权演进。第五，AI驱动的SOC在提升告警处置效率的同时，也带来人员技能与成本结构变化，需坚持“人机协同”。最后，GenAI正在削弱传统安全意识培训，超过57%的员工使用个人GenAI账号办公，33%输入敏感信息，企业需转向以行为为导向、面向AI场景的安全培训与治理。  
  
  
原文链接：  
  
https：//www.arnnet.com.au/article/4127681/six-trends-that-will-reshape-cyber-security-in-2026-gartner.html  
  
  
新品发布  
  
  
**Avast推出Deepfake Guard：在普通PC上实时拦截AI诈骗视频**  
  
Avast于2026年2月3日宣布,在全球范围内推出移动端Scam Guardian系列产品的同时,正式发布针对Windows PC的Deepfake Guard功能。该AI驱动工具可实时分析并检测视频内容中的恶意音频,标志着Avast诈骗防护生态的重大扩展。  
  
  
根据Gen Threat Labs数据,2025年第四季度共检测到159,378起结合manipulated media和明确诈骗意图的独特深度伪造诈骗实例。YouTube是PC端被拦截深度伪造诈骗视频最多的平台,其次是Facebook和X。值得注意的是,多数深度伪造诈骗以正常观看形式出现,而非下载、附件或链接,使其更难被识别。  
  
  
Deepfake Guard可在设备本地实时检测这些隐蔽的诈骗深度伪造内容并发出预警,提升速度和隐私保护。该功能已集成至Avast Premium Security,支持Facebook、Instagram、TikTok、YouTube等主流平台的英文视频分析。该工具兼容传统高端PC和低端Windows PC,在Intel Core Ultra和Qualcomm Snapdragon X系列AI PC上可启用自动检测功能。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/edr-killer-tool-uses-signed-kernel-driver-from-forensic-software/  
  
  
  
  
  
  
  
  
**联系我们**  
  
合作电话：18610811242  
  
合作微信：aqniu001  
  
联系邮箱：bd@aqniu.com  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkBal13S24uhmJl8yJA8ushe8ibZpwQWWoibRKAOCnHxE0PgyJY9PGYfL3eZDN2YMPPUppOooianv1y6g/640?wx_fmt=gif&from=appmsg "")  
  
  
