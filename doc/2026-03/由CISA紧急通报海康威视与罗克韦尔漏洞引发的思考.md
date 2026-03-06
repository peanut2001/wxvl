#  由CISA紧急通报海康威视与罗克韦尔漏洞引发的思考  
原创 千里
                    千里  东方隐侠安全团队   2026-03-06 12:17  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
引言  
  
01  
  
  
🔴 核心观点：别以为老漏洞没事，攻击者还在用！  
  
就在昨天，美国网络安全和基础设施安全局（CISA）再次敲响了安全警钟。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiaUnRibtCHCIDacc87hoDMeF9syNVZiaWpet0eAe8ScNlQfHAC8icOE1hibcia6Hy7KiaF3u2qzGxAFK6n9700hoS3Y2clB5Iec6zlSg/640?wx_fmt=png&from=appmsg "")  
  
  
2026年3月5日，CISA在其著名的"已知被利用漏洞目录"（Known Exploited Vulnerabilities Catalog，简称KEV）中新增了5个严重漏洞，其中最引人关注的，是两个CVSS评分高达9.8分的关键基础设施漏洞——海康威视（Hikvision）身份认证绕过漏洞和罗克韦尔（Rockwell）凭证保护不足漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNhWQpspiacZkXtkKwEMXcl5iaiaOCRdvuO7HpJBjUicAP6sibic9tNAdSOBskWcU2rhQCpTAOUAUdvDFLEeMfIE0EHXibkoggicicib7ympg/640?wx_fmt=jpeg&from=appmsg "")  
  
这两个漏洞，一个2017年就披露了，一个2021年就披露了——但都被列入了CISA的"必须修复"目录。为什么？因为攻击者到现在还在用！  
  
2025年10月，SANS Internet Storm Center就检测到了针对海康威视摄像机的漏洞利用尝试。这些"老掉牙"的漏洞，早已被武器化，成为攻击者的日常工具。  
  
这就是我们今天最想说的一句话：  
别以为老漏洞没事，说不定攻击者还在用！  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
海康威视漏洞：CVE-2017-7921  
  
02  
  
漏洞概述  
  
CVE-2017-7921，这是海康威视（Hikvision）多款IP摄像机产品中的一个严重的身份认证绕过漏洞，CVSS评分高达9.8分，属于"严重"级别。  
  
⚠️ 重要提醒：CVE-2017-7921 是一个2017年披露的"老"漏洞！但就在2025年10月，SANS Internet Storm Center检测到了针对海康摄像机的漏洞利用尝试。2026年3月，CISA将其列入KEV目录——这意味着：9年后的今天，攻击者仍在使用这个漏洞！  
  
受影响产品  
  
这个漏洞影响的海康威视产品线非常广泛，包括但不限于：  
- DS-2CD2系列网络摄像机  
  
- DS-2CD3系列网络摄像机  
  
- DS-2CD4系列网络摄像机  
  
- DS-2CD5系列网络摄像机  
  
- DS-2DF系列高速球机  
  
- DS-2VS系列云台摄像机  
  
- 以及其他运行旧版固件的IP摄像机产品  
  
漏洞技术分析  
  
从技术角度来说，CVE-2017-7921的漏洞机制并不复杂，但正是这种"简单"使其更加危险。  
  
攻击原理：  
1. 攻击者首先需要确定目标摄像机的IP地址，这在当今互联网环境下并不困难——Shodan、ZoomEye等搜索引擎可以轻松列出全球数百万台在线的IP摄像机。  
  
1. 攻击者向摄像机的Web管理界面发送特制的HTTP请求，通过构造特殊的认证头或利用认证逻辑缺陷，绕过后台的身份验证机制。  
  
1. 一旦成功利用，攻击者可以：  
  
- 绕过身份认证：无需任何有效凭据即可访问摄像机  
  
- 权限提升：获取管理员级别的设备控制权  
  
- 敏感数据泄露：下载摄像机配置信息、用户数据库  
  
- 设备完全控制：实时视频监控、PTZ云台控制、存储内容窃取  
  
漏洞危害的深层思考：  
  
这个漏洞最可怕的地方在于它的"零门槛"特性。攻击者不需要提前获取任何凭据，不需要物理接触设备，不需要高深的技术能力——网上已经有公开的利用代码。  
  
历史攻击案例  
  
事实上，这并不是一个"新鲜"的漏洞。CVE-2017-7921早在2017年就被披露，但真正让其臭名昭著的是随后几年大规模爆发的"HiatusRAT"攻击活动。  
  
![New HiatusRAT router malware covertly spies on victims - Lumen Blog](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiakke1PGm8lVTVKrvgaHloDj4lRXodemyGhJRx0MV74PzqvfQCwxGpFAYXLf5OQtLhCUxf10jS0u9pSftsgLx0WmPH0iaM1h2mA/640?wx_fmt=png&from=appmsg "")  
  
根据FBI的公开警告，HiatusRAT是一个专门针对海康威视和Dahau摄像机的远程访问木马（RAT）攻击活动。攻击者利用CVE-2017-7921漏洞批量入侵全球各地的IP摄像机，建立僵尸网络，用于间谍活动、数据窃取、僵尸网络和勒索。  
  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
罗克韦尔漏洞：CVE-2021-22681  
  
03  
  
漏洞概述  
  
CVE-2021-22681，这是罗克韦尔自动化（Rockwell Automation）多款工业控制软件中的严重凭证保护不足漏洞，同样获得9.8分的严重评分。  
  
⚠️ 重要提醒：虽然目前没有公开报道显示CVE-2021-22681已被在野利用，但CISA将其列入KEV目录是一种"预防性措施"。  
  
这同样提醒我们：对于关键基础设施的漏洞，不能等到出事了才重视——必须提前修复！  
  
受影响产品  
  
受CVE-2021-22681影响的罗克韦尔产品包括：  
- Studio 5000 Logix Designer - 罗克韦尔最核心的PLC编程软件  
  
- RSLogix 5000 - 工业界标准的编程工具  
  
漏洞技术分析  
  
攻击原理：  
  
CVE-2021-22681的漏洞本质是"凭证保护不足（Insufficient Protected Credentials）"。攻击者可以通过密钥推断、中间人攻击、凭证重用等方式，冒充合法的编程站与PLC通信，上传恶意程序，修改控制逻辑。  
  
为什么这个漏洞如此可怕？  
  
工业控制系统不同于普通的IT系统，它们直接控制着物理设备。恶意程序上传可能导致化工厂反应釜温度失控、发电厂机组非计划停机、污水处理厂违规排放——乃至更严重的安全事故。  
  
现实威胁场景  
- 商业间谍 - 竞争对手通过漏洞窃取工艺参数和配方  
  
- 勒索攻击 - 勒索软件组织修改PLC程序，威胁支付赎金  
  
- 国家级攻击 - 在冲突中瘫痪对方的关键基础设施（细品）  
  
- ……  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
CISA的强制要求  
  
04  
  
 KEV目录的意义  
  
CISA的KEV目录不是普通的漏洞数据库：  
1. 强制修复：联邦机构必须按照规定的最后期限修复漏洞  
  
1. 已验证在野利用：只有被证实已经在真实攻击中使用的漏洞才会被列入  
  
1. 滚动更新：CISA会持续监控，及时将新发现的在野利用漏洞加入  
  
修复时间表  
  
根据CISA的最新指令，联邦机构必须在2026年3月26日之前修复本次通报的漏洞。  
  
CISA明确指出："这些类型的漏洞是恶意网络行为者的常见攻击向量，对联邦企业构成重大风险。"  
  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
为什么这些漏洞值得关注  
  
05  
  
关键基础设施的特殊性  
  
水利、电力、交通、通信、石油、化工、制造业——这些"关键基础设施"，是现代社会正常运转的基石。  
  
与传统IT系统不同，关键基础设施的系统生命周期往往长达数十年。一个1990年代建设的工业控制系统，可能至今仍在运行——这意味着历史漏洞可能在大量设备上运行。  
  
攻击者的目标在转变  
- 勒索软件：专门针对工厂、医院、能源设施  
  
- 国家级威胁：俄罗斯、朝鲜、中国APT组织都在积极寻找关键基础设施的弱点  
  
- 商业间谍：工业 espionage 日益猖獗  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
借鉴意义  
  
06  
  
5.1 对于企业安全团队  
1. 资产清点 - 梳理所有海康威视、罗克韦尔相关资产  
  
1. 风险评估 - 评估每个受影响资产的业务关键性  
  
1. 修复计划 - 制定补丁测试和部署计划  
  
1. 长期改进 - 建立自动化的补丁管理流程  
  
5.2 对于个人用户  
  
如果你家中有海康威视的摄像机：  
1. 检查固件版本  
  
1. 升级到最新固件  
  
1. 更改默认密码  
  
1. 限制网络访问  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
结语  
  
07  
  
🔴 最后再说一次：别以为老漏洞没事，说不定攻击者还在用！  
  
CVE-2017-7921和CVE-2021-22681——两个"老"漏洞，一个2017年披露，一个2021年披露，却在2026年仍被CISA点名"必须修复"。  
  
因为攻击者到现在还在用！  
- 2025年10月，SANS检测到针对海康威视摄像机的漏洞利用  
  
- 2017年的漏洞，到2025年还能搞事情  
  
- 这不是个案，这是网络安全常态  
  
别再以为"老漏洞没关系"了。攻击者的武器库里，这些"老古董"比新漏洞还好用！  
  
漏洞已经存在，攻击者已经在利用。我们需要做的，是比他们更快。  
  
参考链接  
1. CISA KEV目录通报 (2026-03-05)(https://www.cisa.gov/news-events/alerts/2026/03/05/cisa-adds-five-known-exploited-vulnerabilities-catalog)  
  
1. The Hacker News: Hikvision and Rockwell Automation CVSS 9.8 Flaws(https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html)  
  
1. SANS Internet Storm Center (2025-10) - Hikvision漏洞利用检测(https://isc.sans.edu/)  
  
1. CISA Binding Operational Directive 22-01(https://www.cisa.gov/binding-operational-directive-22-01)  
  
1. CVE-2017-7921 详情(https://www.cve.org/CVERecord?id=CVE-2017-7921)  
  
1. CVE-2021-22681 详情(https://www.cve.org/CVERecord?id=CVE-2021-22681)  
  
  
  
