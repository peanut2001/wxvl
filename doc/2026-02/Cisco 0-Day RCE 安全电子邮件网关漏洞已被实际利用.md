#  Cisco 0-Day RCE 安全电子邮件网关漏洞已被实际利用  
 TtTeam   2026-02-06 09:15  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB1c6r88j06ERjcnuKbAibWZ89ZUcECETjU43IcquCCrQmmViahIODezzV670prMqicRtrJgWialUnGL4A/640?wx_fmt=png&from=appmsg "")  
  
思科已确认其安全电子邮件网关和安全电子邮件及 Web 管理器设备中存在一个严重的零日远程代码执行漏洞，该漏洞正被积极利用。  
  
该漏洞编号为CVE-2025-20393，允许未经身份验证的攻击者通过精心构造的 HTTP 请求向垃圾邮件隔离功能执行任意 root 级命令。  
  
该漏洞源于 Cisco AsyncOS 软件的垃圾邮件隔离功能对 HTTP 请求的验证不足，从而允许在受影响的设备上以 root 权限执行远程命令。  
  
该漏洞被归类为 CWE-20（输入验证不当），其 CVSSv3.1 基准评分最高为 10.0，突出了其网络可访问性、低复杂性以及对机密性、完整性和可用性的全面影响。  
  
攻击目标是启用了垃圾邮件隔离功能并将其暴露在互联网上的设备，通常是通过 6025 端口，这种配置默认情况下未启用，部署指南也不建议这样做。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB1c6r88j06ERjcnuKbAibWZ8SMj2icw8cMj5s226mDD5SBYvz1Q1bicJnBzskj2sgy8qW2r6fXvYgv2Q/640?wx_fmt=png&from=appmsg "")  
  
思科于 2025 年 12 月 10 日发现了这些攻击，并有证据表明攻击行为可以追溯到 2025 年 11 月。  
  
剥削活动和威胁行为者  
  
Cisco Talos 将此次攻击归因于UAT-9686（也称 UNC-9686），这是一个与中国有关联的高级持续威胁组织，根据其工具与 APT41 和 UNC5174 等组织的重叠情况，其置信度为中等。  
  
攻击者部署了一款名为 AquaShell 的基于 Python 的后门程序，用于持久远程访问；同时还使用 AquaTunnel 和 Chisel 等反向 SSH 隧道工具进行内部横向移动；并使用 AquaPurge 清除日志以逃避检测。攻击目标包括电信和关键基础设施行业，其后渗透攻击侧重于间谍活动而非勒索软件。  
  
美国网络安全和基础设施安全局 (CISA)于 2025 年 12 月 17 日将CVE-2025-20393添加到其已知已利用漏洞目录中，并强制要求联邦机构在 2025 年 12 月 24 日之前进行缓解。截至 2026 年 1 月，尚未出现公开的概念验证漏洞利用程序，但自动化扫描有所增加。  
  
入侵指标包括植入的持久化机制、用于远程访问的隐蔽通道；思科建议通过技术支持中心 (TAC) 支持进行验证，并启用远程访问。  
  
缓解措施和修复版本  
  
思科发布了补丁程序来修复此漏洞并移除已知的持久化机制；目前没有其他解决方法。管理员应立即升级，并通过 Web 界面在“网络”>“IP 接口”下确认垃圾邮件隔离状态。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB1c6r88j06ERjcnuKbAibWZ8k1Ik5S2JJS0SyjicTDFjibaSIDftLx7a0ZWDjv0jo2D17zCgCaVZZhicw/640?wx_fmt=png&from=appmsg "")  
  
