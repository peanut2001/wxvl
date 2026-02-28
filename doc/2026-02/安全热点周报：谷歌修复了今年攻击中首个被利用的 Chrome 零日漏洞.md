#  安全热点周报：谷歌修复了今年攻击中首个被利用的 Chrome 零日漏洞  
 奇安信 CERT   2026-02-28 08:10  
  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 4px solid rgb(68, 117, 241);visibility: visible;"><th align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;background: rgb(254, 254, 254);max-width: 100%;box-sizing: border-box !important;font-size: 20px;line-height: 1.2;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgb(68, 117, 241);visibility: visible;"><strong style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 17px;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">安全资讯导视 </span></span></strong></span></th></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">社会救助法草案二审稿加强个人隐私和个人信息保护</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">未履行网络安全保护义务，快手被罚1.191亿元</span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border-bottom: 1px solid rgb(180, 184, 175);visibility: visible;"><td valign="middle" align="center" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 0px none;max-width: 100%;box-sizing: border-box !important;font-size: 14px;visibility: visible;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">• </span><span leaf="">黑客滥用Claude发动网络攻击，窃取墨西哥政府150GB敏感数据</span></p></td></tr></tbody></table>  
  
**PART****0****1**  
  
  
**漏洞情报**  
  
  
**1.Microsoft Windows记事本远程代码执行漏洞安全风险通告**  
  
  
2月12日，奇安信CERT监测到官方修复Microsoft Windows记事本远程代码执行漏洞(CVE-2026-20841)，该漏洞源于应用程序在处理Markdown文件中的超链接时，未能对特殊协议或命令元素进行充分的中和与验证。攻击者可利用该漏洞构造特制的恶意Markdown文件，诱骗用户打开文件并点击其中的恶意链接，进而在受害者设备上执行任意恶意代码。目前该漏洞PoC和技术细节已公开，建议客户尽快做好自查及防护。  
  
  
**2.微信Linux版本命令执行漏洞安全风险通告**  
  
  
2月11日，奇安信CERT监测到微信Linux版本命令执行漏洞(QVD-2026-7687)，该漏洞源于微信Linux版文件名校验不严格，攻击者可诱导用户打开恶意文件名的文件从而导致命令执行，获取系统权限。目前该漏洞PoC已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。  
  
  
**PART****0****2**  
  
  
**新增在野利用**  
  
  
**1.Cisco SD-WAN vManage 身份验证绕过漏洞(CVE-2026-20127)******  
  
  
2月25日，思科宣布一名“技术高超”的网络威胁行为者一直在利用思科 Catalyst SD-WAN 控制器（以前称为 vSmart）中的零日身份验证绕过漏洞(CVE-2026-20127)。  
  
澳大利亚信号局的澳大利亚网络安全中心报告了这一漏洞，并表示一旦该漏洞被利用，恶意行为者会添加一个恶意对等体，并最终获得根访问权限，从而在 SD-WAN 中建立长期持久性。思科在随附的安全公告中解释说称，出现此漏洞的原因是受影响系统中的对等身份验证机制无法正常工作。  
  
攻击者可以通过向受影响系统发送精心构造的请求来利用此漏洞。成功利用此漏洞后，攻击者可以以内部高权限非root用户帐户登录到受影响的 Cisco Catalyst SD-WAN 控制器。利用此帐户，攻击者可以访问 NETCONF，进而操纵 SD-WAN 网络架构的网络配置。  
  
在另一篇博客文章中，思科的 Talos 威胁情报团队将此次攻击和入侵后活动与一个名为“UAT-8616”的组织联系起来。在发现该零日漏洞已被积极利用后，思科找到了证据表明恶意活动至少可以追溯到三年前（2023年）。情报合作伙伴的调查显示，攻击者很可能是通过软件版本降级来获取 root 权限的。据报道，攻击者随后利用了 CVE-2022-20775 漏洞，之后又恢复到原始软件版本，从而有效地获得了root权限。UAT-8616 的攻击尝试表明，网络威胁行为者持续将目标对准网络边缘设备，试图在高价值组织（包括关键基础设施 (CI) 部门）中建立持久的立足点。  
  
思科强烈建议升级到已修复的软件版本，并表示目前没有办法完全缓解该问题。  
  
  
参考链接：  
  
https://www.helpnetsecurity.com/2026/02/25/cisco-sd-wan-zero-day-cve-2026-20127/  
  
  
**2.Google Chrome CSS 释放后重用漏洞(CVE-2026-2441)******  
  
  
2月16日，谷歌发布了紧急更新，修复了 Chrome 浏览器的一个高危漏洞，该漏洞曾被零日攻击利用。这是自今年年初以来首次修复此类安全漏洞。  
  
谷歌在其发布的安全公告中表示，意识到 CVE-2026-2441 漏洞已被利用。根据 Chromium 的提交历史记录，这个释放后重用漏洞（由安全研究员 Shaheen Fazim 报告）是由于 Chrome 实现的 CSS 字体特征值库 CSSFontFeatureValuesMap 中存在迭代器失效错误造成的。成功利用此漏洞可能导致浏览器崩溃、渲染问题、数据损坏或其他未定义行为。  
  
提交信息还指出，CVE-2026-2441 补丁解决了“当前的问题”，但指出 bug 483936078 中跟踪了“剩余的工作” ，这表明这可能是一个临时修复，或者相关问题仍需解决。该补丁在多个提交中被标记为“cherry-picked”（或“backported”），这表明它非常重要，应该包含在稳定版本中，而不是等到下一个主要版本（可能是因为该漏洞正在被实际利用）。尽管谷歌发现了攻击者利用此零日漏洞进行攻击的证据，但并未分享有关这些事件的更多细节。在大多数用户都获得修复程序之前，谷歌可能会限制对错误详情和链接的访问。如果错误存在于其他项目同样依赖但尚未修复的第三方库中，他们也将继续保留这些限制。  
  
谷歌现已修复了稳定桌面渠道用户的该漏洞，未来几天或几周内，新版本将陆续推送 Windows、macOS（145.0.7632.75/76）和 Linux 用户（144.0.7559.75）上线。如果不想手动更新，也可以让 Chrome 自动检查更新，并在下一次发布后安装。  
  
  
参考链接：  
  
https://www.bleepingcomputer.com/news/security/google-patches-first-chrome-zero-day-exploited-in-attacks-this-year/  
  
**PART****0****3**  
  
  
**安全事件**  
  
  
**1.黑客滥用Claude发动网络攻击，窃取墨西哥政府150GB敏感数据**  
  
  
2月25日彭博社消息，据网络安全公司Gambit Security披露，一名身份不明的黑客诱导Anthropic旗下AI产品Claude生成用于网络攻击的恶意代码，针对多个墨西哥政府系统发起网络攻击，利用至少20个存在于老旧系统中的漏洞，窃取了总计150GB敏感数据，涉及纳税人记录、选民档案、政府员工凭证和公民登记文件等。墨西哥政府机构反应不一，部分否认遭受入侵，还有称正在评估情况。据悉，该黑客扮演成参与模拟漏洞赏金计划的安全测试员，用西班牙语诱导Claude扮演"顶级黑客"。起初Claude拒绝请求，但在反复诱导下最终"缴械投降"，不仅生成数千份详细攻击指南，甚至直接输出可执行攻击代码。事件曝光后，Anthropic迅速封禁相关账户，为最新Claude Opus 4.6模型增加实时滥用行为监控。  
  
  
原文链接：  
  
https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data  
  
  
**2.OpenClaw失控：Meta安全总监工作邮箱所有邮件被删除**  
  
  
2月24日Business Insider消息，科技巨头Meta专门研究“怎么让AI听话”的AI对齐总监Summer Yue在X上透露，她把最近火爆的AI智能体OpenClaw接上了自己的工作邮箱处理任务，结果AI当场失控，疯狂删除邮件，喊停三次全部无视。据介绍，AI在处理200多封未读邮件时，执行压缩上下文操作过程中忘记了之前设定的“未经批准不得操作”的指令，自行决定并执行了删除一周前的邮件。事后AI回复称：“我知道你说了不让删，但我还是删了，你生气是对的。”  
  
  
原文链接：  
  
https://www.businessinsider.com/meta-ai-alignment-director-openclaw-email-deletion-2026-2  
  
  
**3.用户除夕夜遭遇AI辱骂，腾讯元宝致歉**  
  
  
2月24日华商报消息，西安一名市民在除夕夜使用腾讯元宝App生成拜年图片时，遭遇AI无故辱骂，原本的祝福标语被替换成低俗辱骂文字。据当事人介绍，他当时先后向元宝AI下达了约5次生成指令，全程未使用任何违禁词或诱导性表述，仅因对生成效果不满意多次修改。起初AI生成的图片虽不理想但内容正常，直至最后一次修改后，图片中原有的祝福标语，被替换成了“你妈个X”辱骂文字。腾讯元宝后续在当事人帖子下回复道：“非常抱歉给您带来不好的体验。经核实，该情况是由模型在处理多轮对话时输出的异常结果导致。目前，我们已紧急校正了相关问题并优化体验。”值得注意的是，这已非元宝首次被曝“骂人”。早在今年1月，就有网友反映在修改代码时遭其回复“滚”“浪费别人时间”等攻击性语言。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/c_t95mr-lVSc7mh5ZdGdhg  
  
  
**4.澳大利亚鸡肉加工龙头被黑后停产一周，多地鸡肉供应短缺**  
  
  
2月23日ABC Australia消息，澳大利亚维多利亚州大型鸡肉加工商Hazeldenes在19日遭受网络攻击，被迫关闭厂区的Wi-Fi系统，导致该州各地的酒吧、肉店等商户出现鸡肉短缺。据专业人士表示，由于无法对产品进行包装，该公司未能完成部分订单。生产受影响达一周，直到25日后才开始分阶段恢复生产。这一事件已在维多利亚州全州范围内造成了供应链问题，大量商户都出现了供应困难，部分地区甚至出现供应中断。Hazeldenes表示，正与网络安全调查人员及相关部门合作，以查明此次网络攻击的原因。  
  
  
原文链接：  
  
https://www.abc.net.au/news/2026-02-23/cyber-attack-takes-major-chicken-processor-hazeldenes-offline/106376184  
  
  
**5.因供应商被黑，沃尔沃集团发生数据泄露**  
  
  
2月10日Bleeping Computer消息，沃尔沃集团北美公司披露了一起间接数据泄露事件。由于外包公司Conduent在一年前被黑，该公司公司1.7万名员工/客户的个人信息遭到泄露。Conduent是一家美国业务流程外包（BPO）公司，其在2024年10月21日至2025年1月13日期间遭遇安全事件，威胁行为者窃取了大量个人的姓名、社会安全号码、出生日期、健康保险保单信息、身份证件号码及医疗信息。Conduent尚未确认受影响个人的确切数量，但此前披露称，该事件影响了俄勒冈州的1050万人以及德克萨斯州的1550万人。目前，该公司正代表其客户向受影响方发送通知，并向沃尔沃集团北美公司的客户和员工提供至少1年的免费身份监控服务，包括信用监控、暗网监控以及身份恢复服务。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/volvo-group-north-america-customer-data-exposed-in-conduent-hack/  
  
  
**6.澳大利亚金融机构泄露客户敏感数据，被罚超1200万元**  
  
  
2月9日iTnews消息，澳大利亚证券和投资委员会（ASIC）已成功申请，对金融公司FIIG Securities在2023年发生的一起数据泄露事件进行处罚。澳大利亚联邦法院已裁定对FIIG Securities处以250万澳元（约合人民币1227万元）罚金，并令其支付50万澳元（约合人民币245万元）诉讼费用。这是澳大利亚首个金融服务持牌者因网络安全漏洞被罚的罚单。据调查，FIIG Securities在过去长达4年时间里未能实施充分的网络安全措施，导致约385GB、涉及1.8万名客户的敏感数据被泄露至互联网，该机构在2023年6月向客户告知了此次泄露事件。安全研究人员认为，ALPHV勒索软件组织是此次攻击的幕后黑手。  
  
  
原文链接：  
  
https://www.itnews.com.au/news/fiig-penalised-25m-for-cyber-security-failures-623490  
  
  
**7.美国电子支付平台BridgePay遭勒索攻击，大量商户刷卡支付中断逾3天**  
  
  
2月7日Bleeping Computer消息，美国主要电子支付平台BridgePay披露，遭受了一起勒索软件攻击，导致关键系统离线，全国电子支付服务大面积中断，并且该公司事件公告页面已连续3天无恢复进展。事件发生后，许多商户和机构开始告知客户，由于刷卡处理服务宕机，他们只能接受现金支付。BridgePay表示：“初步取证结果表明，没有支付卡数据遭到泄露。”并补充称，任何被访问的文件均已被加密，目前“没有可用数据暴露的证据”。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/payments-platform-bridgepay-confirms-ransomware-attack-behind-outage/  
  
  
**8.未履行网络安全保护义务，快手被罚1.191亿元**  
  
  
2月6日网信北京消息，针对近期快手平台出现大量色情低俗内容直播问题，在国家互联网信息办公室指导下，北京市互联网信息办公室依法对北京快手科技有限公司涉嫌违法行为进行立案调查。经查实，快手平台未履行网络安全保护义务，未及时处置系统漏洞等安全风险，未对用户发布的违法信息立即采取停止传输、消除等处置措施，情节严重，影响恶劣。2月6日，北京市互联网信息办公室依据《中华人民共和国网络安全法》《中华人民共和国行政处罚法》等法律法规，对北京快手科技有限公司处警告、1.191亿元人民币罚款处罚，同时责令其限期改正、依法依约处置账号、从严处理责任人。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/DpT1l5RSN-CBCIYbRnONxA  
  
  
**9.米兰冬奥会开幕前，爆发多起未遂网络攻击**  
  
  
2月5日The Record消息，意大利外交部长安东尼奥·塔亚尼表示，意大利近期成功挫败了一系列“来自俄罗斯”的网络攻击，被攻击对象包括该国海外外交使团、即将举行的米兰冬季奥运会相关设施与网站。据悉，约有120个目标受到影响，其中包括位于华盛顿、悉尼、多伦多和巴黎的领事馆，冬奥会运动员在科尔蒂纳丹佩佐住宿的酒店等，但这些攻击并未造成严重破坏。亲俄黑客组织NoName057(16)宣称对此负责，并称此次行动是对意大利支持乌克兰的报复。俄罗斯政府官员尚未就意大利最新的指控公开发表评论。本届冬奥会于2月6日至22日在米兰及附近的科尔蒂纳丹佩佐地区举行。  
  
  
原文链接：  
  
https://therecord.media/italy-blames-russia-linked-hackers-winter-games-cyberattack  
  
  
**10.罗马尼亚国家石油管道运营商遭勒索攻击：IT设施瘫痪多天 1TB数据疑泄露**  
  
  
2月5日Bleeping Computer消息，罗马尼亚国家石油管道运营商Conpet披露称，在3日遭受网络攻击，导致IT设施瘫痪，官网等系统离线逾一周，目前仍未恢复。不过，公司强调此次攻击并未扰乱其运营，也未影响其履行合同义务的能力。勒索软件组织Qilin声称对此负责，其在暗网门户表示窃取了近1TB内部数据，并给出了十余张财务、护照等内部文件截图作为凭证，Conpet尚未予回应。  
  
  
原文链接：  
  
https://www.bleepingcomputer.com/news/security/romanian-oil-pipeline-operator-conpet-discloses-cyberattack-qilin-ransomware/  
  
  
**PART****0****4**  
  
  
**政策法规**  
  
  
**1.社会救助法草案二审稿加强个人隐私和个人信息保护**  
  
  
2月25日，社会救助法草案2月25日提请全国人大常委会会议二次审议。草案二审稿进一步加强关于保护个人隐私和个人信息方面的规定：社会救助工作应当依法保护个人隐私和个人信息。有关单位和人员处理个人信息应当遵循合法、正当、必要原则，采取有效措施保障个人信息安全，对在社会救助工作中知悉的个人信息等，应当依法予以保密。同时，根据“必要”原则，将申请社会救助时需要报告的信息限定为“与申请社会救助相关的情况”；增加规定泄露个人隐私或者个人信息的法律责任。  
  
  
原文链接：  
  
https://www.news.cn/legal/20260225/be7d69d7b6744518a1546ad740cd8b4f/c.html  
  
  
**2.全球61家政府机构联合发布《关于人工智能生成图像与隐私保护的联合声明》**  
  
  
2月23日，全球主要地区61家数据保护监管机构共同发布《关于人工智能生成图像与隐私保护的联合声明》，中国香港在列，但中国与美国未签署。该文件凝聚了上述机构的共同立场，旨在回应当前社会对人工智能技术的普遍关切：部分AI图像、视频生成系统，在未经当事人知情与同意的情况下，生成可识别特定个人的逼真图像及视频内容，引发严重的隐私与安全风险。该文件期望人工智能相关机构建立健全安全防护机制、确保信息公开透明、建立便捷有效的投诉预处理渠道、强化儿童相关风险的技术与管理防护。  
  
  
原文链接：  
  
https://www.edps.europa.eu/data-protection/our-work/publications/international-conferences/2026-02-23-joint-statement-ai-generated-imagery-and-protection-privacy_en  
  
  
**3.《网络安全技术 网络空间安全可视化表示方法》等3项国家标准公开征求意见**  
  
  
2月11日，全国网络安全标准化技术委员会归口的3项国家标准现已形成标准征求意见稿，现面向社会公开征求意见。其中，《网络安全技术 网络空间安全可视化表示方法》给出了网络空间安全可视化表示的原则、内容和方法，提供了网络空间要素、网络空间关系、网络安全事件和网络安全业务的可视化表示框架；  
  
《网络安全技术 可信计算规范 服务器可信支撑平台》确立了服务器可信支撑平台的总体框架，并规定了服务器可信支撑平台的功能要求及其自身安全要求；《数据安全技术 个人信息保护合规审计专业机构能力要求》规定了专业机构开展个人信息保护合规审计服务的能力要求。  
  
  
原文链接：  
  
https://mp.weixin.qq.com/s/7jW2ieF6ep87hSQv8eFWPA  
  
  
**4.国家发改委等八部门印发《关于加快招标投标领域人工智能推广应用的实施意见》**  
  
  
2月10日，国家发展改革委、工业和信息化部、住房城乡建设部、交通运输部、水利部、农业农村部、商务部、国务院国资委等8部门联合印发了《关于加快招标投标领域人工智能推广应用的实施意见》。该文件包括总体目标、加快推进场景应用、规范部署实施和加强组织保障4部分内容。该文件要求，提升安全水平。具体包括：严格落实人工智能模型安全管理要求，强化模型算法、数据资源、基础设施、应用系统等安全能力建设，严格开展算法、模型备案和安全审核。构建数据、算力、算法和系统安全防护体系，确保模型安全可靠，有效防范和应对模型黑箱、幻觉和算法歧视等风险。  
  
  
原文链接：  
  
https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html  
  
  
**5.工信部等五部门印发《关于加强信息通信业能力建设 支撑低空基础设施发展的实施意见》**  
  
  
2月10日，工业和信息化部、中央网信办、中央空管办、国家发展改革委、中国民航局等五部门联合印发《关于加强信息通信业能力建设 支撑低空基础设施发展的实施意见》。该文件包括总体要求、重点任务、组织保障3部分。该文件提出了10项重点任务，其中1项为强化网络和数据安全保障。具体内容包括：探索构建信息类基础设施网络和数据安全保障体系，落实网络安全等级保护、关键信息基础设施安全保护等制度要求，深化信息通信业网络安全防护管理，加强数据分类分级保护，推进网络和数据安全标准研制，开展监测预警、检测评估、应急处置等能力建设，推动相关企业落实安全主体责任。  
  
  
原文链接：  
  
https://www.miit.gov.cn/zwgk/zcwj/wjfb/yj/art/2026/art_d1cb1667897e4c999a303d110b6691dc.html  
  
  
**6.国家数据局等四部门印发《关于培育数据流通服务机构 加快推进数据要素市场化价值化的意见》**  
  
  
2月7日，国家数据局、工业和信息化部、公安部、中国证监会联合印发《关于培育数据流通服务机构 加快推进数据要素市场化价值化的意见》。该文件共4方面16条内容，分别为总体要求、明确功能定位、提升服务能力、强化实施保障。该文件要求，强化数据安全保障。具体包括：牢牢守住数据安全底线，把安全合规贯穿数据供给、流通、使用等全过程，在实践中细化落实数据流通安全治理规则，提升数据安全治理能力，促进数据安全合规高效流通利用。各类数据流通服务机构应落实数据安全相关法律法规要求，加强数据基础设施安全保护，提升数据安全保障效能。  
  
  
原文链接：  
  
https://www.nda.gov.cn/sjj/zwgk/zcfb/0205/20260205185635251370340_pc.html  
  
  
**7.美国CISA发布强制操作指令，降低老旧边缘设备安全风险**  
  
  
2月5日，美国网络安全与基础设施安全局（CISA）发布BOD 26-02强制性操作指令，名为降低已停止支持的边缘设备带来的风险。该文件指出，负载均衡、防火墙、路由器、无线接入点、网络安全设备等边缘设备，在制造商停止支持后将无法进行安全更新和缺陷修复，会给联邦机构信息系统带来巨大的攻击风险，已有APT组织针对这类设备发起大规模的攻击活动。该文件要求，联邦机构利用CISA发布的已停止支持的边缘设备清单，在指令发布后两年内逐步识别并修复该风险。  
  
  
原文链接：  
  
https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices  
  
  
**往期精彩推荐**  
  
  
[【已复现】Microsoft Windows 记事本远程代码执行漏洞(CVE-2026-20841)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504661&idx=1&sn=08fc7397e3412a0f78a9decd0660c052&scene=21#wechat_redirect)  
  
  
[【已复现】微信 Linux版本命令执行漏洞(QVD-2026-7687)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504654&idx=1&sn=be5d240244c4fac1356f33d43539b043&scene=21#wechat_redirect)  
  
  
[微软2月补丁日多个产品安全漏洞风险通告：5个在野利用漏洞](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247504653&idx=1&sn=00b7b70c52946fc115d6caa367bb93fd&scene=21#wechat_redirect)  
  
  
  
  
本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！  
  
  
  
  
  
  
  
