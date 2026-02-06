#  安全热点周报：SolarWinds 严重远程代码执行漏洞已被积极利用  
 奇安信 CERT   2026-02-06 09:10  
  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 4px solid rgb(68, 117, 241);visibility: visible;"><th align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;background: rgb(254, 254, 254);max-width: 100%;box-sizing: border-box !important;font-size: 20px;line-height: 1.2;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgb(68, 117, 241);visibility: visible;"><strong style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 17px;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">安全资讯导视 </span></span></strong></span></th></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">《网络犯罪防治法（征求意见稿）》公开征求意见</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">工信部等八部门印发《汽车数据出境安全指引（2026版）》</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">美军在“午夜之锤行动”中使用网络武器干扰伊朗防空系统</span></p></td></tr></tbody></table>  
  
  
**PART****0****1**  
  
  
**新增在野利用**  
  
  
**1.SolarWinds Web Help Desk 反序列化漏洞(CVE-2025-40551)******  
  
  
2月3日，CISA 将影响 SolarWinds Web Help Desk (WHD) 的一个严重安全漏洞添加到其已知利用漏洞 ( KEV ) 目录中，并标记为在野利用。  
  
该漏洞编号为 CVE-2025-40551（CVSS 评分：9.8），SolarWinds Web Help Desk 存在反序列化不受信任数据漏洞，可能导致远程代码执行，从而使攻击者能够在主机上运行命令。即使未经身份验证，该漏洞也可能被利用。  
  
Web Help Desk 是一款在政府机构、大型企业、医疗机构和教育机构中广受欢迎的服务台管理软件。SolarWinds 声称，其 IT 管理产品在全球拥有超过30万客户。CISA 规定的三天修复期限表明了潜在攻击的严重性。  
  
CVE-2025-40551 由 Horizon3.ai 的 Jimi Sebree 发现，是 SolarWinds Web Help Desk 中发现的四个严重漏洞之一，供应商已于1月28日通过更新修复了该漏洞。  
  
其余三个漏洞由 watchTowr 的 Piotr Bazydlo 发现。CVE-2025-40553 的描述与 CVE-2025-40551 完全相同：反序列化不受信任数据远程代码执行漏洞。CVE-2025-40552 是一个身份验证绕过漏洞，攻击者可以利用该漏洞执行本应受身份验证保护的操作和方法。CVE-2025-40554 也是一个身份验证绕过漏洞，但如果被利用，攻击者可以利用该漏洞在 Web Help Desk 中执行特定操作。  
  
这四个漏洞的 CVSS 评分均为 9.8，目前只有 CVE-2025-40551 正在被积极利用。  
  
攻击者可以将 CVE-2025-40552 或 CVE-2025-40554 与 CVE-2025-40551 或 CVE-2025-40553 连接起来，从而完全控制目标系统，进行横向移动、数据窃取和勒索软件攻击。  
  
目前尚无公开报告说明该漏洞如何被用于攻击、攻击目标是谁，以及攻击规模有多大。这再次表明，网络威胁行为者正以惊人的速度利用新披露的漏洞。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/cisa-flags-critical-solarwinds-rce-flaw-as-actively-exploited/  
  
**PART****0****2**  
  
  
**安全事件**  
  
  
**1.美军在“午夜之锤行动”中使用网络武器干扰伊朗防空系统**  
  
  
2月5日The Record消息，据知情美国官员透露，美军在针对伊朗的“午夜之锤行动”中对伊朗的防空导弹系统实施了网络攻击。美国网络司令部对与福尔道、纳坦兹和伊斯法罕核设施相连的独立军事系统实施了网络攻击，从而阻止伊朗向进入伊朗领空的美国战机发射地对空导弹。军事系统通常依赖于一系列复杂的组件，所有组件都必须正常运作，任何一个环节的漏洞或弱点都可能被用来破坏整个系统。美国网络司令部对所谓的“目标点”实施了打击，即计算机网络上的映射节点，如路由器、服务器或其他外围设备。据悉，“午夜之锤行动”中的数字部分，是美国网络司令部近16年内对伊朗采取的最复杂的行动之一。  
  
  
原文链接：  
  
https://therecord.media/iran-nuclear-cyber-strikes-us  
  
  
**2.近万名警员信息遭泄露，英国地方警察局赔偿超11亿元**  
  
  
2月4日The Register消息，英国北爱尔兰警察局日前推出了一项价值1.19亿英镑（约合人民币11.23亿元）的和解计划，对受影响的警员每人赔偿7500英镑（约合人民币7.08万元），希望了结2023年一起数据泄露事件引发的大量诉讼案件。受到特别严重影响者如不愿接受该计划，还可继续起诉以争取更好的权益保障。据悉，北爱尔兰警察局当年在回应一个信息公开问询时，不慎将一份全体员工详细资料的表格发布到网上，涉及近一万名警员和文职人员的姓氏、名字首字母缩写、职级、工作地点和部门等信息。由于当地曾长期存在民族冲突，形势较为紧张，这一泄露事件可能危及警员人身安全，被认为是英国警务领域最严重的数据泄露事件。  
  
  
原文链接：  
  
https://www.theregister.com/2026/02/04/psni_breach_compensation/  
  
  
**3.全球17.5万台Ollama主机曾公网暴露，中国占比约三成**  
  
  
1月30日SecurityWeek消息，据美国安全厂商SentinelOne和Censys统计发现，大约近一年内，全球17.5万台Ollama主机在公网暴露过，其中2.3万台长期在线，许多都满足可公网访问、无鉴权、长期在线的条件，可随时被攻击者滥用成为“肉鸡”，部分主机还支持工具调用、RAG、图片识别等能力，具备更高的滥用价值。据悉，这17.5万台暴露主机中，中国约三成占比第一，美国、德国等紧随其后，占比分别为约20%、13%。  
  
  
原文链接：  
  
https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/  
  
  
**4.泄露超3000万客户个人隐私数据，美国电信巨头Comcast赔偿超8.1亿元**  
  
  
1月23日The Inquirer消息，就美国电信巨头康卡斯特（Comcast）2023年数据泄露事件引发的集体诉讼，美国宾州东区联邦法院法官日前批准了一项金额达1.175亿美元（约合人民币8.16亿元）的和解协议，受影响的客户预计可获得3年的金融监测和身份盗窃保护服务，并可自由选择最高1万美元的费用报销或50美元现金补偿。据悉，此次攻击发生在2023年10月中旬，该公司内部使用的思杰系统（Citrix Systems）产品公告公布了一个漏洞，但其未能及时修复，数天后遭到攻击者利用，超3000万客户的用户名、密码、姓名、联系方式、隐私问题及答案、社会安全号码后4位数字等数据泄露。  
  
  
原文链接：  
  
https://www.inquirer.com/business/comcast/comcast-citrix-data-breach-settlement-20260123.html  
  
  
**PART****0****3**  
  
  
**政策法规**  
  
  
**1.《网络安全技术 软件物料清单数据格式》国家标准发布**  
  
  
2月6日，国家市场监督管理总局、国家标准化管理委员会近日发布2026年第4号《中华人民共和国国家标准公告》，由全国网络安全标准化技术委员会归口的GB/T 47020—2026《网络安全技术 软件物料清单数据格式》国家标准正式发布，将于2026年8月1日起正式实施。该标准规定了软件物料清单（SBOM）的数据格式，包括其组成结构、文件格式要求、元素定义及各元素的属性与属性值格式，适用于指导软件供应链相关方生成、共享和使用软件物料清单信息。  
  
  
原文链接：  
  
https://www.tc260.org.cn/portal/article/2/267e851caadf4d7f834ede5e39a7e3cf  
  
  
**2.国家网信办等11部门联合印发《关于提升境外人员入境数字化服务便利性的实施意见》**  
  
  
2月5日，国家网信办、国家发展改革委、教育部、工业和信息化部、人力资源社会保障部、交通运输部、商务部、文化和旅游部、中国人民银行、国家移民局、中国贸促会等11部门联合印发《关于提升境外人员入境数字化服务便利性的实施意见》。该文件明确了5方面14条工作举措，在加强网络和数据安全保障方面，实施强化网络安全防护能力、提升数据安全与个人信息保护水平等工作举措。该文件要求，完善跨境支付、在线预约等境外人员高频使用场景的安全标准规范。加强数据分类分级保护，强化数据收集、存储、使用等全流程管理，防范身份证件、健康档案等敏感信息泄露滥用。  
  
  
原文链接：  
  
https://www.cac.gov.cn/2026-02/05/c_1772021797529524.htm  
  
  
**3.《数据安全技术 个人信息保护合规审计要求》等3项网络安全国家标准发布**  
  
  
2月4日，国家市场监督管理总局、国家标准化管理委员会近日发布2025年第38号《中华人民共和国国家标准公告》，由全国网络安全标准化技术委员会归口的3项国家标准正式发布。其中，《数据安全技术 基于个人请求的个人信息转移要求》规定了基于个人信息主体请求的个人信息转移的适用范围、前提要求、流程要求以及特定情形的其他要求，适用于指导个人信息处理者响应个人信息主体转移个人信息的请求，也适用于监管部门、第三方评估机构的相关监督、管理等工作。《网络安全技术 网络空间安全图谱要素表示要求》规定了网络空间安全图谱要素分类、代码与图形符号表达，适用于网络安全监管者、行业主管者、网络运营者和网络服务提供者开展网络空间安全图谱构建和可视化表达。《数据安全技术 个人信息保护合规审计要求》提出了个人信息保护合规审计原则，规定了个人信息保护合规审计的总体要求、实施流程、内容和方法，适用于个人信息处理者和专业机构开展个人信息保护合规审计活动。  
  
  
原文链接：  
  
https://www.tc260.org.cn/portal/article/2/47a1f06a58a0416f9f7e2696be79d3ce  
  
  
**4.《网络安全标准实践指南——网络数据标签标识技术要求》发布**  
  
  
2月4日，全国网络安全标准化技术委员会秘书处组织编制了《网络安全标准实践指南——网络数据标签标识技术要求》。该文件提出了网络数据标签标识的属性格式、生成规则、打标规则、验标规则、日志留存要求、安全防护要求等内容，可用于帮助网络数据处理者对数据进行标签标识，在此基础上重点对重要数据和个人信息进行分类分级保护，加强数据全周期全过程溯源管理。  
  
  
原文链接：  
  
https://www.tc260.org.cn/sysFile/downloadFile/d097e566ba9643019d00cf935d1d22dc  
  
  
**5.工信部等八部门印发《汽车数据出境安全指引（2026版）》**  
  
  
2月3日，工业和信息化部、国家网信办、国家发展改革委、国家数据局、公安部、自然资源部、交通运输部、市场监管总局等八部门近日联合印发《汽车数据出境安全指引（2026版）》。该文件规定了汽车数据出境活动管理方式和适用条件，提出九类豁免情形，面向研发设计、生产制造、驾驶自动化、软件升级、联网运行等业务场景细化重要数据判定规则，明确开展数据出境安全评估、订立个人信息出境标准合同或者通过个人信息出境认证的工作要求，并从管理制度、技术防护、日志管理、应急处置等方面提出保护要求，指导企业规范开展数据出境活动，提升汽车数据安全保护水平。  
  
  
原文链接：  
  
https://www.miit.gov.cn/cms_files/demo/pdfjs/web/viewer.html?file=/cms_files/filemanager/1226211233/attach/20261/f0dca91f7bfe4722a49e5c231c7b2b6e.pdf  
  
  
**6.《网络犯罪防治法（征求意见稿）》公开征求意见**  
  
  
1月31日，公安部起草了《网络犯罪防治法（征求意见稿）》，现向社会公开征求意见。该文件共7章68条，分别为总则、网络基础资源管理、网络犯罪生态治理、网络犯罪防治义务、跨境网络犯罪防治、法律责任、附则。针对当前网络犯罪的严峻态势，该文件坚持“打防结合、防范为先、生态治理、协同联动”的原则，明确了网络基础资源管理制度、网络犯罪生态治理制度、跨境网络犯罪防治制度和网络犯罪防治义务，着力构建多部门联合、跨地域联动，政府、企业、网民共同参与的网络犯罪综合防治体系。  
  
  
原文链接：  
  
https://www.mps.gov.cn/n2254536/n4904355/c10386242/part/10386265.doc  
  
  
**7.英国国家网络安全中心发布关基设施严重网络威胁应对指南**  
  
  
1月28日，英国国家网络安全中心（NCSC）发布《如何准备并规划组织应对严重网络威胁：关键国家基础设施指南》，提出在地缘政治紧张和高强度对手活动背景下，关基设施组织需提前进入“危机态势准备”，而非仅依赖常规网络防护。该文件强调，网络韧性并非消除所有风险，而是在高压环境下维持运营和快速恢复的能力。该文件指出，严重网络威胁可能直接导致关键服务中断、数据不可恢复性破坏，甚至引发物理系统损害和连锁社会影响，关基设施组织需要将严重网络威胁响应系统性纳入治理、业务连续性和技术架构规划，并通过态势感知强化、防御加固及持续演练，确保在威胁升级时能够迅速切换至更具防御性的运行模式。  
  
  
原文链接：  
  
https://www.ncsc.gov.uk/collection/how-to-prepare-and-plan-your-organisations-response-to-severe-cyber-threat-a-guide-for-cni  
  
  
**往期精彩推荐**  
  
  
[【已复现】Microsoft Office 安全功能绕过漏洞(CVE-2026-21509)安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504636&idx=1&sn=3faa5525b063245cb853d84c65a94254&scene=21#wechat_redirect)  
  
  
[安全热点周报：微软 Office 零日漏洞允许恶意文档绕过安全检查](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504628&idx=1&sn=955e46ed489e26ae537fb66d794ee6c5&scene=21#wechat_redirect)  
  
  
[年度报告 | 2025年漏洞态势全景复盘！](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504619&idx=1&sn=2b304680299a0a0b75bfeddca8b596ac&scene=21#wechat_redirect)  
  
  
  
  
本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！  
  
  
  
  
  
  
  
