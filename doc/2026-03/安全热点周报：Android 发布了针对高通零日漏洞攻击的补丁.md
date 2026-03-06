#  安全热点周报：Android 发布了针对高通零日漏洞攻击的补丁  
 奇安信 CERT   2026-03-06 08:05  
  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 4px solid rgb(68, 117, 241);visibility: visible;"><th align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;background: rgb(254, 254, 254);max-width: 100%;box-sizing: border-box !important;font-size: 20px;line-height: 1.2;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgb(68, 117, 241);visibility: visible;"><strong style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 17px;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">安全资讯导视 </span></span></strong></span></th></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">美以联合空袭期间伊朗遭遇大规模网络攻击，朝拜APP被篡改“呼吁投降”</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">爆料！美军想用AI自动化攻击我国关基设施，电网是重点目标</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">境外黑客攻击我国某电商平台数据库，窃取敏感信息数据</span></p></td></tr></tbody></table>  
  
**PART****0****1**  
  
  
**漏洞情报**  
  
  
**1.Cisco Catalyst SD-WAN身份验证绕过漏洞安全风险通告**  
  
  
3月5日，奇安信CERT监测到官方修复Cisco Catalyst SD-WAN身份验证绕过漏洞(CVE-2026-20127)，该漏洞源于对等身份验证逻辑的实现错误，未经身份验证的攻击者可利用该漏洞向受影响系统发送精心构造的请求，绕过身份验证机制获得高权限的非root访问权限，进而访问NETCONF接口，对SD-WAN网络架构的配置进行任意篡改，严重破坏网络的完整性和可用性。目前该漏洞PoC已公开。鉴于该漏洞已发现在野利用，建议客户尽快做好自查及防护。  
  
  
**2.青龙面板身份认证绕过漏洞安全风险通告**  
  
  
3月2日，奇安信CERT监测到官方修复青龙面板身份认证绕过漏洞(QVD-2026-10895)，该漏洞源于青龙面板存在多个认证绕过漏洞，攻击者可通过路径大小写变体（如/API/替代/api/）绕过认证访问受保护接口，通过/open/user/init路径在已初始化的系统上绕过认证并重置用户凭证，从而获得未授权访问权限，并在服务器上执行任意系统命令，最终完全控制目标设备。目前该漏洞PoC和技术细节已公开。鉴于该漏洞已发现在野利用，建议客户尽快做好自查及防护。  
  
  
**PART****0****2**  
  
  
**新增在野利用**  
  
  
**1.Qualcomm Chipsets 内存破坏漏洞(CVE-2026-21385)******  
  
  
3月3日，谷歌发布了安全更新，修复了129个 Android 安全漏洞，其中包括高通显示组件中一个已被积极利用的零日漏洞。  
  
该公司在其发布的 Android 安全公告中表示，有迹象表明 CVE-2026-21385 可能正在被有限的、有针对性的利用。虽然谷歌没有提供关于目前针对此漏洞的攻击的任何进一步信息，但高通在另一份安全公告中透露，该漏洞是 Graphics 子组件中的整数溢出或回绕，本地攻击者可以利用此漏洞触发内存损坏。  
  
高通表示，谷歌安卓安全团队于12月18日向其通报了这一高危漏洞，并于2月2日通知了客户。根据其2月份发布的安全公告（该公告尚未将 CVE-2026-21385 标记为已被利用的攻击），该安全漏洞影响 235 款高通芯片组。  
  
在本月的 Android 安全更新中，谷歌修复了系统、框架和内核组件中的10个严重安全漏洞，攻击者可以利用这些漏洞远程执行代码、提升权限或触发拒绝服务攻击。这些问题中最严重的是系统组件中的一个关键安全漏洞，该漏洞可能导致远程代码执行，而无需额外的执行权限。利用该漏洞无需用户交互。  
  
Android 安全公告包含两个补丁级别——2026-03-01 和 2026-03-05，后者包含了第一批补丁的所有修复程序，以及针对闭源第三方组件和内核子组件的补丁，这些补丁可能不适用于所有安卓设备。虽然谷歌 Pixel 设备可以立即收到安全更新，但其他厂商通常需要更长时间进行测试和调整，以适应特定的硬件配置。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/google-patches-android-zero-day-actively-exploited-in-attacks/  
  
  
**2.VMware Aria Operations 命令注入漏洞(CVE-2026-22719)******  
  
  
3月3日，美国网络安全和基础设施安全局 (CISA) 已将 VMware Aria Operations 漏洞（编号为 CVE-2026-22719）添加到其已知利用漏洞目录中，并标记该漏洞已被用于攻击。Broadcom 公司也警告称，他们已经注意到有报道称该漏洞已被利用，但表示无法独立证实这些说法。  
  
VMware Aria Operations 是一个企业监控平台，可帮助组织跟踪服务器、网络和云基础架构的性能和运行状况。该漏洞最初于2026年2月24日披露并修复，作为 VMware VMSA-2026-0001 安全公告的一部分，该公告被评为“重要”，CVSS 评分为 8.1。目前，尚未公开披露任何有关如何利用该漏洞的技术细节。  
  
据 Broadcom 公司称，CVE-2026-22719 是一个命令注入漏洞，允许未经身份验证的攻击者在易受攻击的系统上执行任意命令。恶意未经身份验证的攻击者可能会利用此问题执行任意命令，这可能导致在 VMware Aria Operations 中执行远程代码，而此时支持人员正在协助进行产品迁移。  
  
博通公司发布了安全补丁，并为无法立即应用补丁的组织提供了临时解决方法。缓解措施是一个名为“aria-ops-rce-workaround.sh”的 shell 脚本，必须在每个 Aria Operations 设备节点上以 root 用户身份执行。该脚本会禁用迁移过程中可能被利用的组件，包括删除“/usr/lib/vmware-casa/migration/vmware-casa-migration-service.sh”以及以下 sudoers 条目，该条目允许 vmware-casa-workflow.sh 以 root 用户身份运行而无需密码：NOPASSWD: /usr/lib/vmware-casa/bin/vmware-casa-workflow.sh  
  
在该漏洞正被积极用于攻击的情况下，建议管理员尽快应用可用的 VMware Aria Operations 安全补丁或实施变通方案。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/cisa-flags-vmware-aria-operations-rce-flaw-as-exploited-in-attacks/  
  
**PART****0****3**  
  
  
**安全事件**  
  
  
**1.巴基斯坦多个重点电视台卫星信号遭劫持，播放反军队内容**  
  
  
3月2日Hackread消息，1日晚间，巴基斯坦Geo News、ARY News和Samaa TV等多家收视率最高的电视新闻频道发生严重内容安全事故，正常节目突然被未授权的不当信息打断，令全国观众感到困惑。该事件发生在伊斯兰教斋月期间，信徒晚间开斋后不久，并一直持续到晚间9点的新闻时段，这一时段通常是上述频道观众最多的时候。据当地媒体报道，攻击者成功控制了卫星波束和直播信号，并播放了反巴基斯坦武装部队的文字信息，其中部分内容直接呼吁民众起来反对军方，并指责该机构控制并“摧毁”国家。Geo News发布公告称，近期持续遭受未知攻击者的持续攻击，事件期间播放的不当信息与该机构无关。  
  
  
原文链接：  
  
https://hackread.com/pakistan-news-channels-hacked-anti-military-messages/  
  
  
**2.美以联合空袭期间伊朗遭遇大规模网络攻击，朝拜APP被篡改“呼吁投降”**  
  
  
3月2日路透社消息，多位网络安全专家和观察人士表示，2月28日清晨，在美国与以色列对伊朗境内目标发动联合打击的同时，还发生了一系列由网络手段支持的行动。伊朗境内遭遇大规模网络攻击，伊朗通讯社、塔斯尼姆通讯社及许多关基设施出现中断和内容篡改，该国主要朝拜APP BadeSaba Calendar也被篡改，向大量用户推送了“呼吁投降”类威慑信息。第三方互联网监测平台称，伊朗全国互联网连接出现大幅下降，几乎接近断网。这一打击行动还引发了多国网络空间混战，中东地区网络威胁形势正急剧恶化。  
  
  
原文链接：  
  
https://www.reuters.com/business/media-telecom/hackers-hit-iranian-apps-websites-after-us-israeli-strikes-2026-03-01/  
  
  
**3.境外黑客攻击我国某电商平台数据库，窃取敏感信息数据**  
  
  
3月1日国家安全部公众号消息，国家安全部发文称，部分境外间谍情报机关与网络犯罪团伙瞄准数据托管服务领域，频繁发动网络攻击，企图窃取我敏感数据。境外黑客组织通过大数据分析锁定我国某电商平台数据库，植入木马程序实施“钓鱼”攻击，攻破关键权限，窃取大量用户数据信息，其中包括涉及国家关键基础设施项目采购、高端科研物资购买等敏感信息，对国家安全构成严重威胁。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/ZypIvbMB_D53w-fGyKCDwQ  
  
  
**4.法国超1500万份医疗档案数据泄露，高官病历、敏感病情等遭公开**  
  
  
2月27日France24消息，超1500万法国民众的医院登记信息和医疗记录遭黑客窃取，目前已经在网上公开。法国卫生部表示，该事件发生在2025年末，由于医疗软件厂商Cegedim Sante被黑，导致约1500家使用该公司电子病历软件的医院诊所发生数据泄露，1580万份病人档案文件遭到泄露，病人姓名、电话号码、邮寄地址等个人信息受影响，其中部分档案涉及该国高级官员，还有16.5万份档案包含医生备注的病人病情隐私及性取向等敏感信息。有专家评论称，这可能是“法国医疗领域规模最大的一次数据泄露”，并可能带来“无法弥补的后果”。  
  
  
原文链接：  
  
https://www.france24.com/en/live-news/20260227-hackers-steal-medical-details-of-15-million-in-france  
  
  
**PART****0****4**  
  
  
**政策法规**  
  
  
**1.《网络安全标准实践指南——网络安全标识 消费类网联摄像头安全要求》公开征求意见**  
  
  
3月3日，全国网络安全标准化技术委员会秘书处组织编制了《网络安全标准实践指南——网络安全标识 消费类网联摄像头安全要求（征求意见稿）》，现面向社会公开征求意见。该文件规定了消费类网联摄像头的安全技术要求和安全保障要求，规定了基础级、增强级、领先级三个等级的安全能力要求，适用于消费类网联摄像头的设计、开发、使用、维护和检测。  
  
  
原文链接：  
  
https://www.tc260.org.cn/sysFile/downloadFile/d366cb897f9e4066bbe584081342f7ef  
  
  
**2.四部门联合发布《关于加快推动科技保险高质量发展 有力支撑高水平科技自立自强的若干意见》**  
  
  
3月2日，科技部、金融监管总局、工业和信息化部、国家知识产权局联合发布《关于加快推动科技保险高质量发展 有力支撑高水平科技自立自强的若干意见》。该文件共七部分内容，提出20项政策举措。其中一项举措为推动网络安全保险创新应用，具体内容包括：持续开展网络安全保险服务试点，发布网络安全保险服务典型方案目录，扩大保险应用范围。围绕电信和互联网、工业领域、金融领域及能源、教育、医疗卫生等重点行业差异化风险管理需求，鼓励保险机构开发多元化网络安全保险产品。支持网络安全企业、专业网络安全测评机构等网络安全保险服务机构，开展网络安全风险评估、监测预警、应急处置等安全技术服务。  
  
  
原文链接：  
  
https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?docId=1250501&itemId=861&generaltype=1  
  
  
**3.国家网信办发布《政务移动互联网应用程序备案工作指南（第一版）》**  
  
  
2月28日，国家网信办编制了《政务移动互联网应用程序备案工作指南（第一版）》，对政务应用程序备案管理的方式、流程和材料等作出了说明。据悉，备案申请表主要包括政务应用程序基本信息、立项审核情况、功能设置情况、运维和安全保障情况、验收情况等。运维和安全方面，需要简述本政务应用程序的运维和安全情况，包括但不限于运维团队情况、运维管理制度、运维技术方案、安全测试情况、网络安全等级保护测评情况、安全管理保障制度等。该文件要求，政务应用程序上线前，主办（使用）单位应根据《政务移动互联网应用程序规范化管理办法》，按照备案工作指南履行备案程序。禁止以任何形式要求用户下载、安装或使用未经备案的政务应用程序。  
  
  
原文链接：  
  
https://www.cac.gov.cn/cms/pub/interact/downloadfile.jsp?filepath=NUtqEIwGiCjGm2Bhl20cvG5MtFfttkkISSUDIkjkM1Z0/2MJ3mR4gI49E5aDdo~otKvC4UqzeN6CUXjPDkxSvXzP3UNlZVBwLZa22rbOam0=&fText=%E6%94%BF%E5%8A%A1%E7%A7%BB%E5%8A%A8%E4%BA%92%E8%81%94%E7%BD%91%E5%BA%94%E  
  
  
**4.《人形机器人与具身智能标准体系（2026版）》发布**  
  
  
2月28日，工业和信息化部人形机器人与具身智能标准化技术委员会发布《人形机器人与具身智能标准体系（2026版）》。该文件包括基础共性、类脑与智算、肢体与部组件、整机与系统、应用、安全伦理等6个部分。安全伦理标准贯穿于人形机器人与具身智能产业全生命周期，为技术演进和发展提供安全与合规保障。这是我国首个覆盖人形机器人与具身智能全产业链、全生命周期的标准顶层设计，标志着相关产业进入规范化发展新阶段。  
  
  
原文链接：  
  
https://www.news.cn/20260228/c27e2dfdb0f4496494c7e4991f2e8c2f/c.html  
  
  
**往期精彩推荐**  
  
  
[【已复现】Cisco Catalyst SD-WAN 身份验证绕过漏洞(CVE-2026-20127)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504685&idx=1&sn=23883cdee93b778e1f2b2d6b719763c6&scene=21#wechat_redirect)  
  
  
[【已复现】青龙面板身份认证绕过漏洞(QVD-2026-10895)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504678&idx=1&sn=d7c2da91f2a4e0a7adf007ff146e80eb&scene=21#wechat_redirect)  
  
  
[安全热点周报：谷歌修复了今年攻击中首个被利用的 Chrome 零日漏洞](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504670&idx=1&sn=598e4ea6c7dc25cee2882cdb3ce26379&scene=21#wechat_redirect)  
  
  
  
  
本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！  
  
  
  
  
  
  
  
