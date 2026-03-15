#  Zyxel警告称，十几款路由器存在严重远程代码执行漏洞  
Rhinoer
                    Rhinoer  犀牛安全   2026-03-15 16:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vO1zY1O9p8JYIEaRfwJUt7g1dtpVbeeeDp7O2af8R4llBiau07dJykOwnd2J8nFLwdP1Iqb1M0ID4WRZG1qic6On11ibG7pKGuqW8ZNCxbicdSc/640?wx_fmt=png&from=appmsg "")  
  
台湾网络设备供应商 Zyxel 发布了安全更新，以解决影响十几种路由器型号的严重漏洞，该漏洞可能允许未经身份验证的攻击者在未打补丁的设备上执行远程命令。  
  
该命令注入安全漏洞被追踪为 CVE-2025-13942，在 Zyxel 4G LTE/5G NR CPE、DSL/以太网 CPE、光纤 ONT 和无线扩展器的 UPnP 功能中发现。  
  
Zyxel 表示，未经身份验证的远程攻击者可以利用此漏洞，通过恶意构造的 UPnP SOAP 请求在受影响的设备上执行操作系统 (OS) 命令。  
  
然而，CVE-2025-13942 攻击可能比严重性评级所暗示的要有限，因为成功利用该漏洞需要启用 UPnP 和 WAN 访问，而后者默认情况下是禁用的。  
  
Zyxel公司表示： “需要注意的是，这些设备的广域网访问默认是禁用的，只有同时启用广域网访问和存在漏洞的UPnP功能，才能进行远程攻击。强烈建议用户安装补丁程序以保持最佳防护效果。”  
  
周二，Zyxel 还修复了两个高危身份验证后命令注入漏洞（CVE-2025-13943和CVE-2026-1459），这两个漏洞允许威胁行为者使用被盗用的凭据执行操作系统命令。  
  
互联网安全监管机构 Shadowserver 目前追踪近 120,000 台暴露在互联网上的 Zyxel 设备，其中包括超过 76,000 台路由器。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vO1zY1O9p8JXu28iagJJTibotNGufrl8ta766lqgIdca1TdQ0cLBH5eiaUlXPR3xZvBx6wyGthJx2ic4CuuYe9e93HRFXE7HRQj9F0tLbLk10qY/640?wx_fmt=png&from=appmsg "")  
  
由于全球许多互联网服务提供商在激活新的互联网服务合同时都将 Zyxel 设备作为默认的开箱即用设备提供，因此 Zyxel 设备经常成为攻击目标。  
  
美国网络安全和基础设施安全局 (CISA) 目前正在追踪 12 个影响 Zyxel 路由器、防火墙和 NAS 设备的漏洞，这些漏洞已经或仍在被积极利用。  
  
本月初，Zyxel公司发出警告，称其没有计划修复两个零日安全漏洞（CVE-2024-40891和CVE-2024-40891）。这两个漏洞已被攻击者积极利用，并影响到仍在网络销售的已停产路由器。该公司“强烈建议”客户更换路由器，使用固件已修复漏洞的新产品。  
  
Zyxel公司表示：“VMG1312-B10A、VMG1312-B10B、VMG1312-B10E、VMG3312-B10A、VMG3313-B10A、VMG3926-B10B、VMG4325-B10A、VMG4380-B10A、VMG8324-B10A、VMG8924-B10A、SBG3300和SBG3500均为老旧产品，已停产多年。因此，我们强烈建议用户更换为新一代产品，以获得最佳防护效果。”  
  
Zyxel 声称，其网络产品已在全球 150 个市场拥有超过 100 万家用户。  
  
  
信息来源：B  
leepingComputer  
  
