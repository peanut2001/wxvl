#  CISA警告称，最高严重级别的n8n漏洞正在被恶意利用  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-03-13 01:00  
  
**导****读**  
  
  
  
美国网络安全和基础设施安全局 (CISA) 已确认，黑客正在利用工作流自动化平台 n8n 中最高级别的远程代码执行 (RCE) 漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyKTTUvuhSWW3BcGbjebIvTalQICyXcLGJffc1SjKiaeuicWYr6JSgkLoAsicCxSF6hXT3q14Br4QsMSNDOqrjS0U1EJ7W6scLAoII/640?wx_fmt=png&from=appmsg "")  
  
  
CISA 敦促所有联邦民事行政部门 (FCEB) 机构立即修补 CVE-2025-68613，因为它具有近乎完美的 9.9 漏洞评分。  
  
  
该漏洞最早于 12 月披露， Resecurity等供应商表示，n8n 约 23 万活跃用户中，超过 10.3 万用户似乎存在漏洞。  
  
  
CVE-2025-68613 可能导致开源工作流自动化平台上的远程代码执行，潜在后果从简单的数据盗窃到全面的供应链破坏不等。  
  
  
该漏洞影响 n8n 及其表达式求值引擎，它们通常用于自动化跨系统的操作任务。  
  
  
n8n 的公告指出，在某些情况下，经过身份验证的攻击者可以将有效载荷注入表达式中，然后这些表达式会在未经验证的情况下执行。  
  
  
“成功利用该漏洞可能导致受影响实例完全被攻陷，包括未经授权访问敏感数据、修改工作流程以及执行系统级操作。”声明中写道。  
  
  
简单来说，这意味着  
拥有低权限帐户的攻击者可以控制整个 n8n 实例，并滥用该实例来访问密码等机密信息，或者通过修改工作流程推送恶意代码，以及其他恶意行为。  
  
  
n8n 在 v1.122.0 中修复了该漏洞，美国联邦各机构必须在 3 月 25 日之前确保运行的是安全版本。  
  
  
自 CVE-2025-68613 首次披露以来，项目维护者们经历了数周的艰难时期。尽管针对 9.9 级漏洞的补丁奏效了，但在 Cyera 研究人员通知他们存在一个被命名为“ ni8mare ”的 10.0 级严重漏洞后，该项目不得不花费时间制定其他修复方案。  
  
  
CVE-2026-21858 (10.0) 是今年年初披露的另一个 RCE 漏洞，尽管由于 webhook 处理不当，该漏洞允许攻击者在无需身份验证的情况下自由控制 n8n 实例。  
  
  
随后在 2 月初出现了一系列漏洞，这些漏洞被追踪到同一个 CVE 标识符 CVE-2026-25049 (CVSS 9.4)。  
  
  
n8n 表示，这些缺陷与 CVE-2025-68613 更为相似，提供了利用该平台表达式求值引擎的更多方法。  
  
  
n8n在一份公告中 表示： “根据 CVE-2025-68613，已发现并修复了 n8n 表达式评估中的其他漏洞。”  
  
  
“已通过身份验证且拥有创建或修改工作流权限的用户，可能会滥用工作流参数中精心构造的表达式，在运行 n8n 的主机上触发意外的系统命令执行。”  
  
  
n8n  
官方安全公告：  
  
https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp  
  
  
新闻链接：  
  
https://www.theregister.com/2026/03/12/cisa_n8n_rce/  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
黑客利用Claude漏洞攻击多个墨西哥政府机构  
  
https://www.cysecurity.news/2026/03/hackers-exploit-claude-to-target.html  
  
  
黑客利用伪装成战争新闻的后门攻击卡塔尔  
  
https://hackread.com/china-hackers-qatar-backdoor-fake-war-news/  
  
  
APT28 使用定制恶意软件对乌克兰军队进行长期间谍活动  
  
https://securityaffairs.com/189230/apt/apt28-conducts-long-term-espionage-on-ukrainian-forces-using-custom-malware.html  
  
  
中东地区的电子战攻击对货运物流和地图应用造成严重干扰  
  
https://www.wired.com/story/gps-attacks-near-iran-are-wreaking-havoc-on-delivery-and-mapping-apps/  
  
  
Lazarus Hackers 利用虚假 LinkedIn 面试攻击 AllSecure CEO  
  
https://hackread.com/fake-linkedin-interview-lazarus-hackers-allsecure-ceo/  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
Hive0163 利用人工智能辅助的 Slopoly 恶意软件在勒索软件攻击中实现持久访问  
  
https://thehackernews.com/2026/03/hive0163-uses-ai-assisted-slopoly.html  
  
  
Storm-2561 利用搜索引擎优化 (SEO) 投毒技术传播虚假 VPN 客户端，窃取用户凭证  
  
https://www.microsoft.com/en-us/security/blog/2026/03/12/storm-2561-uses-seo-poisoning-to-distribute-fake-vpn-clients-for-credential-theft/  
  
  
爱立信美国公司披露数据泄露事件——黑客窃取员工和客户数据  
  
https://cybersecuritynews.com/ericsson-data-breach/  
  
  
黑客利用 Cloudflare 的反机器人功能窃取 Microsoft 365 凭据  
  
https://cybersecuritynews.com/cloudflare-anti-bot-features-microsoft-365/  
  
  
KadNap恶意软件入侵超过14000台边缘设备，运行隐藏代理僵尸网络  
  
https://www.cysecurity.news/2026/03/kadnap-malware-compromises-over-14000.html  
  
  
基于 Rust 的 VENON 恶意软件攻击 33 家巴西银行，利用其凭证窃取技术进行攻击  
  
https://thehackernews.com/2026/03/rust-based-venon-malware-targets-33.html  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
微软Office严重漏洞（CVE-2026-26110）可导致远程代码执行攻击  
  
https://cybersecuritynews.com/microsoft-office-vulnerability-enables-rce-attack/  
  
  
Active Directory 漏洞 (CVE-2026-25177) 导致 SYSTEM 权限提升  
  
https://www.esecurityplanet.com/threats/active-directory-flaw-enables-system-privilege-escalation/  
  
  
Chrome 安全更新 – 修复 29 个允许远程代码执行的漏洞  
  
https://cybersecuritynews.com/chrome-security-update-29-vulnerabilities/  
  
  
Veeam警告称，备份服务器存在严重缺陷，可能遭受远程代码执行攻击  
  
https://www.bleepingcomputer.com/news/security/veeam-warns-of-critical-flaws-exposing-backup-servers-to-rce-attacks/  
  
  
苹果修复了 Coruna WebKit 漏洞  
  
https://www.cybermaterial.com/p/apple-patches-coruna-webkit-exploit  
  
  
联发科芯片存在严重漏洞，攻击者可在45秒内窃取安卓手机PIN码  
  
https://cybersecuritynews.com/mediatek-vulnerability-android-phone/  
  
  
Ally WordPress插件漏洞使超过20万个网站面临攻击风险  
  
https://www.securityweek.com/ally-wordpress-plugin-flaw-exposes-over-200000-websites-to-attacks/  
  
  
超过4000台路由器因KadNap恶意软件利用漏洞而受到感染  
  
https://gbhackers.com/kadnap-malware/  
  
  
Splunk远程代码执行漏洞  
(  
CVE-2026-20163  
)  
允许攻击者执行任意Shell命令  
  
https://cybersecuritynews.com/splunk-rce-vulnerability-2/  
  
  
SolarWinds Web Help Desk 反序列化漏洞可导致命令执行  
  
https://cybersecuritynews.com/solarwinds-web-help-desk-deserialization-vulnerability/  
  
  
Cisco IOS XR 软件漏洞允许攻击者以 root 权限执行命令  
  
https://cybersecuritynews.com/cisco-ios-xr-software-vulnerability-root/  
  
  
GitLab 安全更新 – 修复 XSS 和 API DoS 漏洞  
  
https://cybersecuritynews.com/gitlab-security-update-2/  
  
  
CISA警告称，最高严重级别的n8n漏洞正在被恶意利用  
  
https://www.theregister.com/2026/03/12/cisa_n8n_rce/  
  
  
N8n 两个关键漏洞可导致服务器被接管  
  
https://www.securityweek.com/critical-n8n-vulnerabilities-allowed-server-takeover/  
  
****  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
