#  HPE：严重的 AOS-CX 漏洞可导致管理员密码重置  
Sergiu Gatlan
                    Sergiu Gatlan  代码卫士   2026-03-11 12:17  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**HPE****（慧与公司）公司已修复Aruba Networking AOS-CX操作系统中的多个安全漏洞，其中包括若干身份验证与代码执行问题。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
AOS-CX是慧与子公司Aruba Networks为其CX系列园区和数据中心交换机设备开发的云原生网络操作系统。在这些漏洞中，最严重的是一个严重的身份验证绕过漏洞（CVE-2026-23813），可导致未经授权的攻击者在低复杂度攻击中利用该漏洞重置管理员密码。  
  
HPE表示：“已发现AOS-CX交换机基于Web的管理界面存在一个漏洞，可能允许未经认证的远程攻击者绕过现有的身份验证控制。在某些情况下可能导致管理员密码被重置。截至该安全公告发布之日，尚未发现针对该漏洞的任何公开讨论或利用代码。”  
  
无法立即应用安全更新修复易受攻击交换机的IT管理员可采取以下缓解措施：  
  
- 将所有管理接口的访问权限限制在专用二层网段或VLAN中，以隔离管理流量。  
  
- 在三层及以上层面实施严格策略控制管理接口访问，仅允许授权且可信的主机进行连接。  
  
- 在无需管理访问的交换虚拟接口和路由端口上禁用HTTP(S)接口。  
  
- 实施控制平面访问控制列表以保护支持REST/HTTP的管理接口，确保仅允许可信客户端连接至HTTPS/REST端点。  
  
- 对所有管理接口活动启用全面的记账、日志记录和监控，以便检测并响应未授权访问尝试。  
  
  
  
HPE尚未发现公开的概念验证利用代码，也无证据表明攻击者正在野外利用这些漏洞。  
  
2025年7月，该公司还就Aruba Instant On接入点中存在硬编码凭据发出警告，攻击者可利用这些凭证绕过标准设备身份验证。在此一个月前，HPE 修复了StoreOnce磁盘备份与重复数据删除解决方案中的八个漏洞，其中包括另一个严重级别的身份验证绕过漏洞和三个远程代码执行漏洞。今年1月份，美国网络安全和基础设施安全局（CISA）提醒称 HPE OneView中的一个满分漏洞已在攻击中被利用。  
  
HPE在全球拥有超过61000名员工，2024年财报显示营收达301亿美元，为全球超过55000家企业客户提供服务与产品，其中包括90%的财富500强公司。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[HPE：Aruba Networking 访问点中存在严重的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521429&idx=1&sn=8d164e84c96d33be487787e9f3024b73&scene=21#wechat_redirect)  
  
  
[HPE 发布严重的 RCE 0day 漏洞，影响服务器管理软件 SIM，无补丁](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499209&idx=2&sn=c481c08557d40e5796397f548beee4fc&scene=21#wechat_redirect)  
  
  
[只要29个字符 “A”，HPE iLO4 服务器认证轻松绕](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487566&idx=3&sn=402304d9804967f02a7a5c6555dcef8f&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/microsoft-hackers-abusing-ai-at-every-stage-of-cyberattacks/  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
