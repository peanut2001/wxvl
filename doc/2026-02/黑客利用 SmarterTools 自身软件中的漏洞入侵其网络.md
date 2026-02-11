#  黑客利用 SmarterTools 自身软件中的漏洞入侵其网络  
bleeping
                    bleeping  暗镜   2026-02-11 00:00  
  
SmarterTools 上周证实，Warlock 勒索软件团伙在入侵其电子邮件系统后攻破了其网络，但并未影响业务应用程序或帐户数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb1IuZb9zUBDNL73NRz2oDraVPeW2fFdficVOiazh1zL50KRYAWXzAQ65pUygRwzHCz3SRUfxmJxSLwkulXIRCOamUArPZAbuwT6U/640?wx_fmt=png&from=appmsg "")  
  
  
该公司首席商务官德里克·柯蒂斯表示，入侵事件发生在 1 月 29 日，入侵者是通过一名员工设置的单个 SmarterMail 虚拟机 (VM) 发起的。  
  
“在这次安全漏洞事件发生之前，我们的网络中大约有 30 台服务器/虚拟机安装了 SmarterMail，” 柯蒂斯解释说。  
  
“不幸的是，我们并不知道一名员工设置的一台虚拟机没有进行更新。结果，该邮件服务器遭到入侵，最终导致了数据泄露。”  
  
尽管 SmarterTools 保证客户数据没有直接受到此次泄露事件的影响，但经证实，该公司办公网络上的 12 台 Windows 服务器以及用于实验室测试、质量控制和托管的辅助数据中心已被入侵。  
  
攻击者利用基于 Windows 的工具和持久化技术，通过 Active Directory 从那台存在漏洞的虚拟机横向移动。该公司基础设施的大部分由 Linux 服务器组成，但这些服务器并未受到此次攻击的影响。  
  
此次攻击利用的漏洞是CVE-2026-23760，这是 SmarterMail 9518 版本之前的身份验证绕过漏洞，允许重置管理员密码并获得完全权限。  
  
SmarterTools 报告称，这些攻击是由Warlock 勒索软件组织实施的，该组织还使用类似手段影响了客户的机器。  
  
勒索软件运营者在获得初始访问权限后大约等待了一周，最后阶段是对所有可访问的机器进行加密。  
  
然而，据报道，Sentinel One 安全产品阻止了最终有效载荷执行加密，受影响的系统被隔离，数据从新的备份中恢复。  
  
据该公司称，攻击中使用的工具包括 Velociraptor、SimpleHelp 和存在漏洞的 WinRAR 版本，同时还利用启动项和计划任务来实现持久化。  
  
Cisco Talos 此前曾报告称，威胁行为者滥用了开源 DFIR 工具 Velociraptor。  
  
2025 年 10 月，Halcyon 网络安全公司将 Warlcok 勒索软件团伙与一个被追踪为 Storm-2603联系起来。  
  
ReliaQuest 今天早些时候发布了一份报告，以中等到高的置信度证实，该活动与 Storm-2603 有关。  
  
ReliaQuest 表示：“虽然此漏洞允许攻击者绕过身份验证并重置管理员密码，但 Storm-2603 将此访问权限与软件内置的‘卷挂载’功能结合起来，从而获得完全的系统控制权。”  
  
“入侵后，该组织会安装 Velociraptor，这是一款他们曾在之前的攻击活动中使用过的合法数字取证工具，以此来维持访问权限并为勒索软件的入侵做好准备。”  
  
ReliaQuest 还发现了针对 CVE-2026-24423 的探测，这是CISA上周标记的另一个 SmarterMail 漏洞，勒索软件攻击者正在积极利用该漏洞，尽管主要攻击途径是 CVE-2026-23760。  
  
研究人员指出，CVE-2026-24423 提供了一条更直接的 API 路径来实现远程代码执行，但 CVE-2026-23760 的噪音较小，可以融入合法的管理活动中，因此 Storm-2603 可能选择了后者。  
  
为了解决 SmarterMail 产品中最近出现的所有缺陷，建议管理员尽快升级到 Build 9511 或更高版本。  
  
  
