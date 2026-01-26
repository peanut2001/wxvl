#  AI Network Security | 某厂商超1.1万台防火墙面临遭自动化漏洞攻击！华为星河AI网络安全已经支持对漏洞攻击检测  
 华为安全   2026-01-26 04:00  
  
近日，在网络安全业内突发预警，某厂商防火墙遭遇新型自动化恶意攻击，攻击者利用预制脚本批量扫描未打补丁的暴露设备，数秒内即可完成后门账户创建、配置文件导出等操作，窃取用户核心敏感信息。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EjJibicwCQS5QibzD3w9lZNmM0ws1jz2GfsO14zDVdRTDPfqWG1h6HKHZLh6hUovoHOlB2HcibGeso3vQKBHNzbX5A/640?wx_fmt=png&from=appmsg "")  
  
  
据网络安全业界人士分析，该攻击是由于该厂商披露严重漏洞导致的。该厂商于2025年12月9日披露了CVE-2025-59718和CVE-2025-59719两个严重漏洞，影响该厂商多款主流产品。该漏洞允许未认证的攻击者绕过SSO单点登录机制，从而直接获得设备的管理员权限。据某些外部安全机构监测数据发现漏洞自2025年12月12日起已被攻击者积极利用，涉及的多款主流产品。  
  
  
全球某网络安全漏洞检测机构公开统计显示，截至目前，仍有约1.1万台互联网暴露的该厂商设备因启用单点登录成为攻击目标。随着2026年1月的新一波自动化攻击出现，攻击者借助预制脚本批量扫描未打补丁的暴露设备，在数秒内完成后门账户创建、配置文件导出等操作，这种规模化攻击模式进一步扩大了漏洞的威胁范围与破坏力度。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EjJibicwCQS5QibzD3w9lZNmM0ws1jz2Gfs1QqSF5mTklvjr3OssE6L9fdRZCYzCAu6HBJ0gnFU62icOfyazH3R6cA/640?wx_fmt=png&from=appmsg "")  
  
  
这两个漏洞的核心问题在于SAML (Security Assertion Markup Language) 协议处理过程中的加密签名验证不当。当设备启用了SSO（Single Sign-On，单点登录）功能时，设备会接收来自管理平台的SAML响应然后处理登录。在存在漏洞的版本中，设备未能正确验证SAML响应的加密签名，导致攻击者可以自行构造恶意SAML响应，伪造管理员身份，绕过认证过程。值得注意的是，虽然SSO功能出厂默认是关闭的，但当管理员通过GUI注册配置设备时，有可能会导致功能自动默认启用，形成隐蔽攻击面。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EjJibicwCQS5QibzD3w9lZNmM0ws1jz2Gfs4ia903mHUrEpOXXHG4lKibePGRhia4k1os6APCYwZhlmqU18DZuSqXacQ/640?wx_fmt=png&from=appmsg "")  
  
  
攻击者一旦通过漏洞获取管理员权限，可实施多重恶意操作。在某监测数据显示，攻击者首先会以admin身份通过SSO登录，随后立即通过GUI界面下载系统配置文件，该文件通常包含哈希密码、VPN配置和网络拓扑等敏感信息。在26年1月的最新攻击中，攻击者还表现出创建本地管理员账户（如cloud-noc、cloud-init、audit、backup等）的行为，这些账户被用于维持持久访问权限。攻击者获取的配置信息可进一步用于横向渗透内部网络，甚至被用于勒索攻击，导致企业面临数据泄露、业务中断等严重后果。  
  
  
此次漏洞引发了全球网络安全界的广泛关注，而这并非该厂商产品首次出现高危漏洞，早在25年1月，另一个漏洞CVE-2024-55591漏洞就已被证实可让攻击者绕过身份验证，直接获取产品的管理员权限。根据安全机构监测，CVE-2024-55591漏洞已被Qilin、RansomHub、LockBit等知名勒索组织积极利用，用于入侵企业网络并部署勒索软件。高危漏洞的反复爆发，边界设备沦为攻击者的入口跳板，这暴露了在自身安全性上的严重不足。  
  
  
华为星河AI网络安全方案  
  
已支持检测和拦截该漏洞  
  
  
针对该事件相关的安全漏洞，华为依托于星河AI网络安全方案能力，快速上线了漏洞签名，目前华为已支持对该漏洞攻击的精准检测与有效拦截。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EjJibicwCQS5QibzD3w9lZNmM0ws1jz2Gfs0WxtaQ6CNBnIPwl1EME5ZSNpibMicYTqicaVlJTZ9wcaiaKgoI77yyicOww/640?wx_fmt=png&from=appmsg "")  
  
  
2025年，华为防火墙、IPS等网络安全产品通过全球权威机构BSI首批漏洞管理体系认证，斩获涵盖ISO/IEC 27001信息安全管理、ISO/IEC 29147漏洞披露及ISO/IEC 30111漏洞处理流程三大国际标准的认证证书，产品安全性与质量获国际权威认可。  
  
  
华为星河AI网络安全产品不仅自身安全可靠，检测与防御能力更领先业界，广泛适配企业、运营商等多行业场景。在企业边界防护中，华为星河AI融合SASE方案集成Emulator微内核脱壳引擎与AI安全检测算法，可对加壳文件实施解密脱壳操作，并对解密后的文件开展动态行为分析，未知威胁检测率达95%，领先业界15个百分点。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHiafr2MLsF0to5jqxZ6yp2gf5JGbAz77HDqm5WV1ProV8icgYfeKWfqwiaaeZPuZlSjMjfIF7vy2Dm5w/640 "")  
  
未来，华为将持续投入AI对抗AI能力建设，为全球用户提供更可靠、更智能的网络安全解决方案和产品。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaRDyoND55HiaXH5T0PpCBxBaLPUictKiceuLyz1shIgvHqRQLS3VLbCfk0eIGdQ3OQiaqDTOykOkDKAnur82wNH8UQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
点击**“阅读原文”**  
，了解更多华为网络安全解决方案！  
  
