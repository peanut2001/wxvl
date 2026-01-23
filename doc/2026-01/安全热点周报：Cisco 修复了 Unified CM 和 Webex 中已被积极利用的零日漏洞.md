#  安全热点周报：Cisco 修复了 Unified CM 和 Webex 中已被积极利用的零日漏洞  
 奇安信 CERT   2026-01-23 09:30  
  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 4px solid rgb(68, 117, 241);visibility: visible;"><th align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;background: rgb(254, 254, 254);max-width: 100%;box-sizing: border-box !important;font-size: 20px;line-height: 1.2;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgb(68, 117, 241);visibility: visible;"><strong style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 17px;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">安全资讯导视 </span></span></strong></span></th></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">欧盟拟立法禁止外国高风险ICT供应商，实现关基行业“自主可控”</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">MuddyWater组织针对我国政企机构实施网络攻击，工信部发布预警</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">上市公司立讯精密疑遭勒索攻击，苹果大量产品模型、项目资料或被窃取</span></p></td></tr></tbody></table>  
  
**PART****0****1**  
  
  
**漏洞情报**  
  
  
**1.SmarterMail身份认证绕过漏洞在野利用风险通告**  
  
  
1月22日，奇安信CERT监测到SmarterMail身份认证绕过漏洞(QVD-2026-4572)在野利用，该漏洞源于系统管理员（IsSysAdmin=true）的密码重置路径未验证OldPassword字段的有效性，仅依赖用户输入的Username和NewPassword即可直接修改系统管理员账户密码。远程攻击者可通过构造特定请求，任意重置已知用户名的系统管理员账户密码，进而执行任意操作系统命令，最终实现远程代码执行。奇安信鹰图资产测绘平台数据显示，该漏洞关联的全球风险资产总数为39923个，关联IP总数为19564个。目前该漏洞PoC和技术细节已公开。鉴于该漏洞已发现在野利用，建议客户尽快做好自查及防护。  
  
  
**2.GNU InetUtils telnetd远程身份认证绕过漏洞安全风险通告**  
  
  
1月21日，奇安信CERT监测到官方修复GNU InetUtils telnetd远程身份认证绕过漏洞(QVD-2026-4408)，telnetd在调用系统/usr/bin/login程序时，未对从客户端USER环境变量传入的用户名做过滤，直接拼接到login命令行。未经授权的远程攻击者可利用该缺陷，在无需任何口令的情况下直接获取目标主机的root shell，造成完全控制权泄露、敏感信息被窃取或进一步横向移动。该漏洞PoC和技术细节已公开，目前观察到的受影响设备以NAS设备为主。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。  
  
  
**PART****0****2**  
  
  
**新增在野利用**  
  
  
**1.Cisco Unified Communications Manager 远程代码执行漏洞(CVE-2026-20045)******  
  
  
1月21日，思科已修复了统一通信和 Webex Calling 的一个严重远程代码执行漏洞（编号为 CVE-2026-20045），该漏洞已被积极利用为零日攻击。  
  
该漏洞编号为 CVE-2026-20045，影响 Cisco Unified Communications Manager (Unified CM)、Unified CM Session Management Edition (SME)、Unified CM IM & Presence、Cisco Unity Connection 和 Webex Calling Dedicated Instance。  
  
思科在其安全公告中警告称，该漏洞是由于对 HTTP 请求中用户提供的输入验证不当造成的。攻击者可以通过向受影响设备的基于 Web 的管理界面发送一系列精心构造的 HTTP 请求来利用此漏洞。 成功利用漏洞可能使攻击者获得底层操作系统的用户级访问权限，然后提升权限至 root。虽然该漏洞的 CVSS 评分为 8.2，但思科将其评为“严重”级别，因为利用该漏洞可获得服务器上的 root 权限。  
  
这家网络设备巨头还表示，“已注意到有人试图利用此漏洞”，并敦促客户升级到已修复的软件版本以解决此问题。目前尚无其他解决方法。据悉，该漏洞是由一位匿名外部研究人员发现并报告的。该公司还表示，除了安装更新之外，没有其他方法可以缓解该漏洞。  
  
美国网络安全和基础设施安全局 (CISA) 已将 CVE-2026-20045 添加到其已知利用漏洞 (KEV) 目录中，思科“强烈建议”客户尽快通过升级到已修复的软件版本或应用补丁文件来修复此漏洞。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/cisco-fixes-unified-communications-rce-zero-day-exploited-in-attacks/  
  
**PART****0****3**  
  
  
**安全事件**  
  
  
**1.MuddyWater组织针对我国政企机构实施网络攻击，工信部发布预警**  
  
  
1月22日网络安全威胁和漏洞信息共享平台消息，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）近日监测发现，MuddyWater组织近期针对政府、军事、电信、能源等机构实施网络攻击，窃取系统凭证、机密文件等敏感数据。攻击者通过鱼叉邮件投递两类伪装载荷，攻击载荷成功在内存部署后门后，会写入注册表实现自动启动，采用动态C2连接策略，收集主机名、工作组、系统版本及用户名等数据，加密回传至服务端，最终建立对目标主机的远程控制。建议相关单位及用户立即禁用Office宏执行策略，阻断恶意文档释放攻击载荷；部署邮件网关动态沙箱，深度检测伪装PDF的可执行文件及带宏文档；实时监控注册表路径HKCU\Software\...\UserShellFolders\Startup异常写入，清除后门持久化项。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/-32LwWiWwAA9aAhaLGvW4A  
  
  
**2.国台办：2025年查处来自台湾方向网络攻击事件年增25%**  
  
  
1月21日中新社消息，国务院台办发言人彭庆恩在北京表示，民进党当局频频指使军情机构和网军对大陆实施网络攻击破坏，传播散布违法有害信息。据统计，2025年，有关部门共调查处置来自台湾方向的网络攻击事件近四千起，较2024年增长25%。其行为重点针对大陆交通、金融、科技、能源等重要行业领域开展攻击窃密。彭庆恩说，有关部门之前已侦破并公布台湾军方“心战大队”、台湾王氏研创艺术公司、“匿名者64”等涉事组织对大陆实施网络攻击的犯罪事实。  
  
  
原文链接：  
  
https://www.chinanews.com.cn/gn/2026/01-21/10556322.shtml  
  
  
**3.上市公司立讯精密疑遭勒索攻击，苹果大量产品模型、项目资料或被窃取**  
  
  
1月19日Cybernews消息，国内知名上市公司、苹果供应商立讯精密疑似遭受勒索软件攻击，攻击者声称窃取了苹果、英伟达、LG等大量客户机密数据。RansomHub勒索软件组织在其暗网门户上称，去年12月15日成功实施了攻击，窃取了3D产品模型、工程设计数据、零部件制造图纸、电子设计文档、印刷电路板制造数据和参与项目的员工身份信息等敏感数据，威胁立讯精密联络以索要赎金。Cybernews分析攻击者放出的示例数据，认为真实性较高。  
  
  
原文链接：  
  
https://cybernews.com/security/luxshare-apple-iphone-assembler-breach/  
  
  
**4.伊朗国家电视台卫星信号遭劫持，播放反政府视频**  
  
  
1月19日The Record消息，伊朗国家电视台多个频道在18日（星期日）遭到劫持，正常节目被中断，转而播放抗议及一名流亡反对派人物的画面。未经授权的播出持续了约10分钟。受影响的频道通过Badr卫星进行传输，该卫星被伊朗国家广播机构用于向全国多个省级电视台传送信号。肇事组织尚未得到立即确认，伊朗当局也未就此事件公开发表评论。据悉，伊朗自去年12月下旬以来持续处于动荡之中，政府自8日起对互联网和移动通信实施了“全国范围”的断网，已持续近2周。  
  
  
原文链接：  
  
https://therecord.media/iran-state-television-reported-hack-opposition  
  
  
**PART****0****4**  
  
  
**政策法规**  
  
  
**1.欧盟拟立法禁止外国高风险ICT供应商，实现关基行业“自主可控”**  
  
  
1月20日，欧盟委员会发布《网络安全法案》修订版提案，旨在提高网络安全能力和韧性。该提案拟对（NIS2指令规定的18个）欧盟关键领域的供应链实施去风险化，要求欧盟国家切断与来自第三国、构成较高网络安全风险的信息通信技术（ICT）供应商的合作关系。根据提案，欧盟委员会将开展行业评估，并与欧盟国家协作，共同列出对欧盟安全构成风险的外国国家。这些风险可能源于以往的网络事件、恶意活动，或缺乏司法监督或民主制衡机制等因素。后续，欧盟委员会将指定相关外国国家的特定供应商名称，欧盟国家必须采取措施缓解相关风险，包括可能逐步将特定实体排除在ICT供应链之外。  
  
  
原文链接：  
  
https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-eu-cybersecurity-act  
  
  
**2.水利部发布《水利数据分类分级规则》行业标准**  
  
  
1月16日，水利部近日发布2026年第1号公告，批准发布7项水利行业标准，将于2026年4月4日起实施，其中包括《水利数据分类分级规则》（SL/T 864—2026）。该标准为新制订，共含8章、4个附录。本标准主要内容包括原则、数据分类规则、数据分级规则、数据分类分级流程、分类分级动态更新等，适用于水利部、流域管理机构、省（自治区、直辖市）、新疆生产建设兵团、计划单列市、各级直属单位、水利工程单位等各级水利部门工作中处理的非涉密数据的分类分级。该标准发布实施将进一步规定水利数据安全保护工作中的数据分类分级原则和方法，构建统一的水利数据分类体系，实施分级管理，切实强化数据安全防护，促进数据有序流通，对水利行业开展数据管理、数据安全保护提供技术依据。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/v7NDbtcda5CnVwH2QcjOkA  
  
  
**往期精彩推荐**  
  
  
[【在野利用】SmarterMail 身份认证绕过漏洞(QVD-2026-4572)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504524&idx=1&sn=b7a52d0ad7bb616eb4bbb3a6c823386f&scene=21#wechat_redirect)  
  
  
[【已复现】GNU InetUtils telnetd 远程身份认证绕过漏洞(QVD-2026-4408)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504514&idx=1&sn=0618a3503e959cd2c19d6d581a8f7994&scene=21#wechat_redirect)  
  
  
[Oracle 2026年1月补丁日多产品高危漏洞安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504501&idx=1&sn=e5729e9e83c6d610ae05b054ac747d4c&scene=21#wechat_redirect)  
  
  
  
  
本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！  
  
  
  
  
  
  
  
