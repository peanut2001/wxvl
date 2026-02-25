#  ACF插件漏洞使黑客能够获得5万个WordPress网站的管理权限  
Rhinoer
                    Rhinoer  犀牛安全   2026-02-25 16:00  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlibkAjaR8rHFBibnQTUkSKXUgLS1mLlQyHIG7XHicQFdF8ibg43XNctWgia1m0cbFcCHFyAh2TE9YVGCA/640?wx_fmt=png&from=appmsg "")  
  
WordPress 的 Advanced Custom Fields: Extended (ACF Extended) 插件存在严重漏洞，未经身份验证的攻击者可远程利用该漏洞获取管理权限。  
  
ACF Extended 目前已在 10 万个网站上启用，它是一款专门的插件，通过为开发人员和高级网站构建者提供的功能，扩展了 Advanced Custom Fields (ACF) 插件的功能。  
  
该漏洞编号为 CVE-2025-14533，可通过滥用插件的“插入用户/更新用户”表单操作来获取管理员权限，该漏洞存在于 ACF Extended 0.9.2.1 及更早版本中。  
  
该漏洞源于在基于表单的用户创建或更新过程中缺乏对角色限制的强制执行，即使在字段设置中正确配置了角色限制，该漏洞仍然会被利用。  
  
Wordfence解释说：在存在漏洞的插件版本中，表单字段没有任何限制，因此可以任意设置用户的角色，即使是‘管理员’，而不管字段设置如何，只要表单中添加了角色字段 。   
  
研究人员警告说：“与任何权限提升漏洞一样，这可以用于完全控制网站。”  
  
虽然利用此漏洞的后果很严重，但 Wordfence 指出，该问题只能在明确使用映射了角色字段的“创建用户”或“更新用户”表单的网站上利用。  
  
CVE-2025-14533 是由安全研究员 Andrea Bocchetti 发现的，他于 2025 年 12 月 10 日向 Wordfence 提交了一份报告，以验证该问题并将其上报给供应商。  
  
四天后，供应商解决了这个问题，并在 ACF Extended 版本 0.9.2.2 中发布了该修复程序。  
  
根据wordpress.org的下载统计数据，自那时以来，大约有 5 万用户下载了该插件。假设所有下载都是最新版本，那么大约有相同数量的网站将面临攻击风险。WordPress插件枚举活动  
  
尽管目前尚未发现针对 CVE-2025-14533 的攻击，但威胁监控公司GreyNoise 的一份报告显示，大规模 WordPress 插件侦察活动旨在列举潜在的易受攻击的网站。  
  
根据 GreyNoise 的数据，从 2025 年 10 月下旬到 2026 年 1 月中旬，来自 145 个 ASN 的近 1000 个 IP 地址针对 706 个不同的 WordPress 插件发起了超过 40000 次独特的枚举事件。  
  
最受关注的插件包括 Post SMTP、Loginizer、LiteSpeed Cache、Rank Math SEO、Elementor 和 Duplicator。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlibkAjaR8rHFBibnQTUkSKXUqgDZTI4UVbCPvmT1DltrObU8mj9giawe7dXgiapqVFzXiawtMoOHXIib9w/640?wx_fmt=png&from=appmsg "")  
  
Wordfence于 2025 年 11 月初报告称，有人积极利用了 Post SMTP 漏洞 CVE-2025-11833 ，而 GreyNoise 的记录显示，有人集中攻击该漏洞，涉及 91 个 IP 地址。  
  
GreyNoise 敦促管理员修复的另一个缺陷是 CVE-2024-28000，该缺陷会影响 LiteSpeed Cache，并且Wordfence 在 2024 年 8 月将其标记为正在积极利用的漏洞。  
  
  
信息来源：BleepingComputer  
  
