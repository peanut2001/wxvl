#  你的Windows还安全吗？2月6个零日漏洞正在被大规模利用  
原创 Zero老Z
                    Zero老Z  SecLab安全实验室   2026-02-22 02:25  
  
如果你觉得每个月的“补丁星期二”只是例行更新，那这一次可能要重新认识一下它的分量了。  
  
微软刚刚发布的 2 月安全更新，可以说是“火力全开”——一次性修复了 6 个已经被黑客实际利用的零日漏洞，数量追平了去年 3 月创下的纪录。更让人捏一把汗的是，其中 3 个漏洞在补丁发布前就已经被公开披露，这意味着攻击者早就掌握了关键细节。  
  
一句话总结：补丁刚上线，战场已经打过一轮。  
### 59 个漏洞，6 个正在“实战”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BXRyxzSJEtQSbrmupia2DN9NjFoiapmnCnNDV3qlKiadsKTQyjBicgTwXE17kNFZHxPYPDN8JAdIwB3MiahOS9d2uMvogXLXefD983oz8pUrSgc4/640?wx_fmt=png&from=appmsg "")  
  
  
这次更新共修复了 59 个漏洞，涵盖企业业务系统和底层核心组件。光是“正在被利用”的零日漏洞就占了 10% 以上，比例相当惊人。  
  
Trend Micro 零日计划负责人 Dustin Childs 直言不讳：“正在被攻击的漏洞数量异常之高。”  
  
要知道，上一次出现 6 个在野利用的零日漏洞，还是在去年 3 月。时隔近一年，风险强度再次拉满。  
### 两个 8.8 分高危漏洞：点一下链接，系统就可能沦陷  
  
本次风险等级最高的零日漏洞中，有两个 CVSS 评分高达 8.8：  
- **CVE-2026-21510**  
：影响 Windows Shell  
  
- **CVE-2026-21513**  
：影响 Internet Explorer  
  
它们有一个共同点：**都需要用户“配合”一下——点击。**  
  
听上去门槛不高？问题就在这里。  
  
Action1 总裁兼联合创始人 Mike Walters 指出，CVE-2026-21510 属于保护机制失效漏洞。攻击者只需诱导用户点击一个精心伪造的恶意链接，就能绕过 Windows 的防护机制。  
  
更危险的是，已经存在成熟、可稳定利用的攻击方式。通过特制链接或快捷方式文件，攻击者可以绕过 Windows Shell 以及 SmartScreen 安全提示。  
  
而且——不需要任何额外权限。  
  
换句话说，这几乎是为钓鱼攻击“量身定制”的漏洞。  
### 另外 4 个零日漏洞，同样不容忽视  
  
剩下的零日漏洞同样分布在关键系统组件中：  
- **CVE-2026-21514**  
（CVSS 7.8）：影响 Microsoft Office Word  
  
- **CVE-2026-21519**  
（CVSS 7.8）：影响 Desktop Window Manager  
  
- **CVE-2026-21533**  
（CVSS 7.8）：影响 Windows Remote Desktop  
  
- **CVE-2026-21525**  
（CVSS 6.2）：影响 Windows Remote Access Connection Manager  
  
美国网络安全与基础设施安全局（CISA）已在周二将这 6 个漏洞全部列入“已知被利用漏洞目录”。这通常意味着什么？——优先级拉满，必须尽快修补。  
### 安全提示形同虚设？用户的“习惯”正在被利用  
  
Tenable 高级研究工程师 Satnam Narang 提到，其中三个漏洞（CVE-2026-21510、CVE-2026-21513、CVE-2026-21514）有一个共同特征：**绕过安全功能。**  
  
这些安全功能本来是用来阻止用户打开恶意文件的，比如弹窗警告、风险提示等。  
  
问题是，很多用户早已对这些提示“习以为常”。看到弹窗，下意识就点“继续”。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BXRyxzSJEtTLichxVSeWWpm070LjlaBLdBibyQv1IVvz1t6V9lNFXNqr62x1buibWpf8LWTsuQAkvweddqtfeL5bTDiajmg6Swa9xdJdybcrcgI/640?wx_fmt=png&from=appmsg "")  
  
  
当漏洞可以直接绕开这些防护机制时，风险自然成倍放大。安全感还在，安全却可能已经不在了。  
### 还有两个“爆表级”漏洞：评分 9.8  
  
除了零日漏洞，本月微软还披露了两个 CVSS 评分高达 9.8 的严重漏洞：  
- **CVE-2026-21531**  
：影响 Azure SDK  
  
- **CVE-2026-24300**  
：影响 Azure Front Door  
  
9.8 分几乎接近满分，这类漏洞通常意味着远程攻击、无需复杂条件，影响面也往往更广。  
### 高危漏洞占大多数  
  
在本次修复的 59 个漏洞中：  
- **43 个属于高危级别**  
  
- 其中 **5 个被微软评估为“更可能被利用”**  
  
这已经不是“例行修补”，而更像是一场紧急排雷。  
### 现在该做什么？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BXRyxzSJEtQFDeK0CNQWWt59HYea9DG9kfGSo5flibia0KbY3tXJDRyzrN7CibflsickptA6au9Fiae2178qITn2cNOpmXHBFYy0ib3CLVQgqA5icw/640?wx_fmt=png&from=appmsg "")  
  
  
如果你是企业 IT 管理员，这次补丁优先级不需要讨论——尽快部署。  
  
如果你是普通用户，也别掉以轻心。尤其是涉及 Windows、Office、远程桌面或 Azure 服务的环境，更新越晚，风险窗口越大。  
  
网络攻击从来不是遥远的新闻。很多时候，它只差一个“点击”。  
  
本月完整漏洞清单可在微软安全响应中心查看。  
  
补丁已经发布，选择权在你。  
  
  
