#  国家信息安全漏洞库发布人工智能重要安全漏洞通报；维基百科遭自传播JavaScript蠕虫攻击，XSS漏洞如何被武器化 | 牛览  
 安全牛   2026-03-06 05:38  
  
**点击蓝字 关注我们**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzEuDVUZocRvycrvVqlmBYCIduicbLicR8YzicGqS4VFT82VMcn64jibUPNHhqaVhXu4alDbFoOh8WXwBwLuBGdtep7dBRibiaq88V5sY/640?wx_fmt=png&from=appmsg "")  
  
  
新闻速览  
  
- 国家信息安全漏洞库发布人工智能重要安全漏洞通报  
  
  
- 2025年恶意广告激增42% 广告供应链成网络攻击重灾区  
  
  
- 你的企业早已被黑客“扫描”千遍：别再误以为自己不值得攻击  
  
  
- ThreatLocker扩展零信任版图，MSP可降低钓鱼凭证失陷风险  
  
  
- 维基百科遭自传播JavaScript蠕虫攻击，XSS漏洞如何被武器化  
  
  
- 谷歌报告：企业设备零日漏洞利用占比达 48% 防护设备成重灾区  
  
  
- Luma 推出多模态 AI 智能体，重构创意领域端到端工作流程  
  
  
- Bing AI 搜索遭投毒，假冒 OpenClaw 安装包分发信息窃密木马  
  
  
- 埃森哲12亿美元收购Ookla，强化网络性能与安全管控能力  
  
  
- 警惕GitHub恶意仓库：BoryptGrab窃取器借免费工具传播，多 payload 窃取核心数据  
  
特别关注  
  
  
**国家信息安全漏洞库发布人工智能重要安全漏洞通报**  
  
国家信息安全漏洞库（CNNVD）报送 Langflow 远程代码执行漏洞（CNNVD-202602-4530、CVE-2026-27966），该漏洞 CVSS 评分 9.8 为高危级别，Langflow 所有 1.8.0 之前的版本均受影响，目前官方已发布 1.8.0 版本完成补丁修复。  
  
  
Langflow 是开源的 AI 智能体与工作流可视化构建平台，此次漏洞根源为其 CSVAgent 节点在代码中硬编码allow_dangerous_code=True，导致 LangChain 的python_repl_ast工具被自动启用，且无 UI 开关和环境变量可禁用该行为。攻击者可通过提示注入触发该工具，执行任意 Python 代码和系统命令，无需权限、无需用户交互即可实现远程代码执行，甚至完全接管服务器。  
  
  
针对该漏洞，CNNVD 建议所有 Langflow 用户立即核查自身产品版本，尽快升级至 1.8.0 及以上的 patched 版本，及时采取修补措施，防范服务器被恶意攻击。  
  
  
原文链接：  
  
https://www.cnnvd.org.cn/home/warn  
  
  
热点观察  
  
  
**2025年恶意广告激增42% 广告供应链成网络攻击重灾区**  
  
据The Media Trust《全球数字信任、广告完整性及人员保护报告》显示，恶意广告（Malvertising）正通过在线广告基础设施加速传播，诈骗活动、恶意重定向及恶意软件分发与正常营销流量混杂，威胁持续升级。  
  
  
2025年相关损失与威胁数据显著攀升：美国消费者和企业因恶意软件、诈骗及广告欺诈损失超125亿美元；70%的成年人在过去12个月内遭遇过数字诈骗或钓鱼攻击；恶意广告事件同比激增42%，为2019年以来最大增幅。  
  
  
威胁呈现三大特征：一是诈骗活动通过广告流量传播，身份盗窃最为常见，购物诈骗、虚假发票等频发；二是AI被广泛应用，63%的品牌仿冒广告使用AI生成图像或文本；三是恶意重定向软件持续扩散，如GhostCat家族已渗透48个广告网络，52%的相关恶意软件以勒索、敲诈为目的。  
  
  
全球数字广告支出2025年超7400亿美元，广告覆盖网站、移动应用等多场景，尤其是联网电视广告支出超400亿美元，扩大了攻击面。目前全球广告欺诈损失约410亿美元，仅39%消费者信任数字广告，广告完整性直接影响用户信任与企业营收。  
  
  
原文链接：  
  
https://www.helpnetsecurity.com/2026/03/05/the-media-trust-ad-malware-risks-report/  
  
  
**你的企业早已被黑客“扫描”千遍：别再误以为自己不值得攻击**  
  
2026 年 3 月 5 日安全研究显示，即便非大型企业或金融机构，只要系统在线，就已被黑客持续扫描。现代网络攻击高度自动化，攻击门槛持续降低，中小机构因安全投入普遍不足，反而更易成为目标。  
  
  
黑客发现目标并非随机选择，而是依靠自动化工具全网探测开放端口、过期软件、云配置错误等漏洞。一旦系统被标记，攻击者便会从弱口令、未补丁插件、暴露数据库等低难度入口突破，同时通过 AI 生成高度仿真钓鱼邮件，针对员工实施攻击。  
  
  
传统杀毒软件与防火墙已不足以防御。凭据填充、商业邮件欺诈、应用程序代码缺陷等手段，可轻易绕过常规防御，实现权限提升与数据窃取。  
  
  
企业无需顶级资源即可构建基础防御：梳理核心敏感资产，严格按岗位分配权限，全面启用多因素认证；加固终端与云环境，仔细核查云配置；部署日志审计、告警与异常检测系统，实现早期发现；常态化开展员工安全培训，提升钓鱼识别与风险上报意识。  
  
  
安全的核心在于主动防御。自动化扫描与新型攻击无处不在，企业只有建立多层防御、持续监测与人员安全意识，才能大幅降低被攻击概率，避免成为黑客的易攻目标。  
  
  
原文链接：  
  
https://www.cm-alliance.com/cybersecurity-blog/why-your-business-is-already-on-hackers-radars-a-cybersecurity-check  
  
  
**谷歌报告：企业设备零日漏洞利用占比达 48% 防护设备成重灾区**  
  
谷歌最新发布的报告显示，其去年追踪的零日漏洞中，48% 被用于攻击企业设备，创下历史新高，黑客正将攻击重心大幅转向大型企业以窃取数据。零日漏洞指软件被利用时开发者尚未知晓的漏洞，此次涉企零日漏洞中，约半数竟针对企业网络防护类设备，凸显企业安全防线的核心短板。  
  
  
报告指出，Cisco、Fortinet 的防火墙，Ivanti、VMware 的 VPN 及虚拟化平台成为黑客主要攻击目标，四家厂商均证实近期旗下产品在客户网络中遭漏洞利用。黑客主要利用输入验证缺陷、授权流程不完善等常见漏洞突破防护，这类漏洞利用门槛较低，且仅能通过软件更新修复。  
  
  
其余涉企零日漏洞则波及各类企业软件，典型案例如 Clop 勒索组织针对 Oracle E-Business Suite 的攻击，导致哈佛大学、美国航空子公司 Envoy、《华盛顿邮报》等数十家机构的人力资源数据遭窃取。  
  
  
报告同时提及，剩余 52% 的零日漏洞针对消费级产品，微软、谷歌、苹果的系统均受波及，其中操作系统为主要重灾区，移动设备零日漏洞数量也同比上升。此外，谷歌发现监控厂商相关零日漏洞占比已超过传统政府背景的间谍组织，反映出政府获取黑客工具的渠道正发生转变。  
  
  
原文链接：  
  
https://techcrunch.com/2026/03/05/google-says-half-of-all-zero-days-it-tracked-in-2025-targeted-buggy-enterprise-tech/  
  
  
**警惕GitHub恶意仓库：BoryptGrab窃取器借免费工具传播，多 payload 窃取核心数据**  
  
近日，研究人员发现新型窃取器BoryptGrab，其可窃取浏览器数据、加密货币钱包信息、系统信息，还能捕获截图、提取Telegram信息及Discord令牌。该恶意软件通过上百个伪造GitHub仓库传播，以免费工具为诱饵，借助SEO关键词吸引受害者，最早可追溯至2025年4月。  
  
  
感染链始于受害者从伪造GitHub下载页面下载ZIP文件，存在两种主要传播路径：一是通过DLL侧载加载加密载荷，经XOR和AES-CBC解密后下载BoryptGrab；二是通过VBS脚本下载启动器，部分脚本还会设置微软 defender 排除项。  
  
  
攻击中还会投递TunnesshClient后门（PyInstaller可执行文件），通过反向SSH隧道与攻击者通信并充当SOCKS5代理，同时可能投递经过代码混淆的Vidar窃取器变体。恶意代码及日志含俄语注释，关联IP位于俄罗斯，暗示攻击者可能有俄罗斯背景。  
  
  
BoryptGrab具备反分析能力，可检测虚拟机环境，其窃取范围覆盖多款浏览器及数十种加密货币钱包，收集指定后缀文件后归档上传。该攻击利用开发者对GitHub的信任，规模庞大且变体众多，对用户数据安全构成严重威胁，需重点防范伪造免费工具下载。  
  
  
原文链接：  
  
https://www.trendmicro.com/en_us/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html  
  
  
安全事件  
  
  
**维基百科遭自传播JavaScript蠕虫攻击，XSS漏洞如何被武器化**  
  
近期，Wikipedia发生一起自传播JavaScript蠕虫事件，攻击代码通过页面编辑传播并篡改多个词条内容，引发社区紧急处置。该事件利用Wikipedia编辑功能中的脚本执行机制，使恶意代码在用户访问或编辑页面时自动传播，形成类似传统蠕虫的扩散效果。  
  
  
攻击者在页面中插入恶意JavaScript代码，当用户打开或编辑被篡改的页面时，脚本会自动执行。该脚本随后通过Wikipedia API继续修改其他页面，将同样的恶意代码写入新的词条，实现“自复制式传播”。受影响页面会被自动篡改内容，例如添加攻击信息或异常文本，从而扩大影响范围。  
  
  
安全研究人员指出，这类攻击本质上利用了Web平台中潜在的Cross-Site Scripting（XSS）风险。当恶意脚本能够在页面渲染或编辑流程中执行时，就可能通过用户行为触发传播机制，进而形成类似“网页蠕虫”的攻击模式。历史上，社交平台和Wiki系统都曾出现类似攻击案例。  
  
  
事件发生后，Wikipedia维护团队迅速回滚受影响页面并清理恶意代码，同时加强过滤规则，以阻止类似脚本再次被写入。由于攻击依赖页面脚本执行能力，其传播范围主要集中在访问受感染页面的用户之间，并未影响Wikipedia核心基础设施。  
  
  
安全专家认为，此事件再次凸显大型开放协作平台在脚本过滤、内容审核和权限控制方面的挑战。对于依赖用户生成内容的平台而言，持续强化输入过滤、脚本隔离以及编辑审计机制，是防止XSS和自传播脚本攻击的关键措施。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/wikipedia-hit-by-self-propagating-javascript-worm-that-vandalized-pages/  
  
  
**Bing AI 搜索遭投毒，假冒 OpenClaw 安装包分发信息窃密木马**  
  
安全厂商 Huntress 披露，攻击者利用 Bing AI 搜索推荐机制，将 GitHub 上的假冒 OpenClaw 安装包推至搜索前列，诱导用户下载执行后，投放信息窃密与代理木马，成为 AI 搜索时代典型的社交工程攻击案例。  
  
  
攻击者注册 openclaw-installer 组织并创建恶意仓库，代码主体拷贝自 Cloudflare 的 moltworker 项目，仅在 Release 中藏匿恶意程序。用户搜索 “OpenClaw Windows” 时，Bing AI 将该假冒仓库列为优先推荐，借助 GitHub 平台可信度大幅降低用户警惕。  
  
  
执行伪装的 OpenClaw_x64.exe 后，Rust 编写的加载器直接在内存中植入多个恶意组件：cloudvideo.exe 为 Vidar 窃密程序，窃取 Telegram、Steam 账号数据；serverdrive.exe 是 GhostSocks 代理木马，将主机转为匿名代理节点用于隐匿攻击。样本中还出现未公开的 stealth packer，具备内存加载、防火墙规则篡改、隐藏计划任务、AntiVM 检测等抗分析能力。  
  
  
GitHub 已删除原恶意仓库，但攻击者快速注册同名克隆仓库持续传播。OpenClaw 生态存在大量未校验扩展与工具，进一步放大供应链投毒风险。  
  
  
原文链接：  
  
https://www.securitylab.ru/news/570047.php  
  
  
产业动态  
  
  
**ThreatLocker扩展零信任版图，MSP可降低钓鱼凭证失陷风险**  
  
在Zero Trust World 2026大会上，ThreatLocker宣布推出零信任网络访问（ZTNA）和零信任云访问能力，目标是帮助MSP应对日益严峻的钓鱼攻击、凭证泄露和网络暴露风险。ThreatLockerCEO Danny Jenkins表示，新产品基于其一贯的“deny-by-default（默认拒绝）”理念，并已为此建设14个新数据中心，其中12个位于美国。  
  
  
其中，零信任云访问主要面向Office 365、Salesforce、Jira、ConnectWise等SaaS应用。其核心机制是将访问权限同时绑定到用户身份和经批准的设备，即使攻击者通过钓鱼窃取凭证，也难以直接登录账户。换言之，系统不仅校验账号，还校验设备，从而压缩被盗凭证的可利用空间。  
  
  
在网络访问方面，ThreatLocker的ZTNA方案强调关闭暴露端口，减少对VPN的依赖，使用户能够像在办公室内一样安全访问内部资源。Jenkins称，许多真实攻击都与公网防火墙开放端口或VPN被攻破有关，而新方案通过“不对互联网开放任何入口”来降低被扫描和入侵的概率。  
  
  
性能和体验也是其卖点之一。ThreatLocker并非将全部流量统一回传至数据中心，而是选择性代理流量，例如不转发已完成认证的语音和媒体流量，以降低时延、改善体验。对MSP而言，这意味着可用更低运维负担，为客户手机和云应用快速下发安全访问能力，并将零信任从终端进一步延伸到云和移动设备。  
  
  
原文链接：  
  
https://www.crn.com/news/security/2026/threatlocker-unveils-zero-trust-network-and-cloud-access-5-things-to-know  
  
  
**埃森哲12亿美元收购Ookla，强化网络性能与安全管控能力**  
  
全球 IT 咨询服务巨头埃森哲在巴塞罗那世界移动通信大会上宣布，以 12 亿美元收购数字媒体集团 Ziff Davis 旗下的 Ookla 公司。  
  
  
Ookla 旗下拥有全球知名网络诊断平台SpeedTest.net，每月处理超 2.5 亿次宽带测速请求，同时运营故障监测平台 Downdetector。该公司 2025 年实现营收 2.31 亿美元，占 Ziff Davis 年度总收入的 16%。而 Ziff Davis 在 2014 年收购 Ookla 时仅花费 1500 万美元。  
  
  
埃森哲表示，现代网络已成为关键业务平台，网络性能测量能力对优化用户体验、业务收益与安全防护至关重要。收购 Ookla 将帮助企业与政府客户安全规模化部署 AI，构建可信数据底座，实现稳定、无缝的连接服务。  
  
  
此次收购将显著提升埃森哲在托管服务领域的竞争力，重点强化 5G 和 WiFi 网络优化能力。Ookla 目前拥有 430 名员工，涵盖软件工程、射频工程及数据科学等专业领域。  
  
  
交易预计在未来数月内完成，过渡期内 Ookla 仍由 Ziff Davis 运营。  
  
  
原文链接：  
  
https://securityonline.info/a-1-2-billion-speed-test-why-accenture-just-bet-the-future-of-ai-on-ookla/  
  
  
新品发布  
  
  
**Luma 推出多模态 AI 智能体，重构创意领域端到端工作流程**  
  
AI 视频生成初创企业 Luma 于周四推出 Luma Agents，该产品依托公司 Unified Intelligence 系列模型打造，基于单一模态推理系统训练，可完成文本、图像、视频、音频全链路创意工作，为广告、营销、设计及企业端提供全新工作模式。  
  
  
Luma Agents 基于该系列首款模型 Uni-1 构建，该模型经音频、视频、图像、语言及空间推理训练，具备 “像素级智能” 能力，可协同 Luma Ray3.14、Google Veo3、ByteDance Seedream 等多款 AI 模型完成创作，后续还将解锁更多音视频输出功能。其核心优势在于能跨资产、协作方和创意迭代保持持久上下文，还可通过自评估迭代优化输出结果，无需人工反复调优提示词，仅通过对话即可引导创作方向。  
  
  
目前该平台已向现有客户落地，涵盖阳狮集团、Serviceplan 等国际广告公司，以及 Adidas、Mazda 等品牌。实测中，其能将品牌耗时一年、耗资 1500 万美元的广告战役，在 40 小时内以 2 万美元成本转化为多地区本地化广告，且通过内部质量核验。现阶段 Luma Agents 已通过 API 对外开放，Luma 将逐步放量访问权限，保障服务稳定性。  
  
  
原文链接：  
  
https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/  
  
  
  
  
  
  
  
  
**联系我们**  
  
合作电话：18610811242  
  
合作微信：aqniu001  
  
联系邮箱：bd@aqniu.com  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wKeDC5RjIzH12TO9bmWWicd7s18quvxaAmiaDS2aab1rLcLBDfuhEN0z7iaFliaNv8kkZVZN9K2Kn2lpwTC5AB0oLiaLECQgoByVMZ30q79K1sSA/640?wx_fmt=gif&from=appmsg "")  
  
  
