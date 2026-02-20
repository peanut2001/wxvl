#  Fortinet SSO漏洞已被积极利用，用于入侵防火墙并获取管理员权限  
 TtTeam   2026-02-19 16:28  
  
Fortinet FortiGate 防火墙的单点登录 (SSO) 功能中存在一个严重漏洞，编号为CVE-2025-59718，目前正被积极利用。  
  
攻击者利用此漏洞创建未经授权的本地管理员帐户，从而授予暴露于互联网的设备完全的管理权限。  
  
CVE-2025-59718 会影响 FortiOS 中的 FortiCloud 单点登录 (SSO) 机制。它允许远程攻击者通过恶意 SSO 登录进行身份验证，从而绕过标准控制措施。  
  
尽管打了补丁，但该漏洞仍然存在，使得在使用 SAML 或 FortiCloud SSO 进行管理员身份验证的防火墙上可以提升权限。  
  
目前尚未公布 CVSS 评分，但实际影响十分严重：攻击者可以创建类似“helpdesk”这样的后门账户，并拥有完整的系统权限。要利用此漏洞，设备必须面向互联网且启用了单点登录 (SSO)。  
  
野外利用  
  
Reddit 用户 u/csodes 和其他用户详细描述了 FortiGate 7.4.9（例如 FGT60F 型号）的安全事件。来自同一 IP 地址的恶意 SSO 登录触发了本地管理员账户的创建，该事件通过 SIEM 警报检测到。受害者确认该设备部署于 2025 年 12 月下旬，排除了早期版本的可能性。  
  
一家机构指出：“我们的本地接入策略脚本失败，但设备仍可通过互联网访问。”另一家使用 SAML 的机构报告了“帮助台”账户的问题。目前已开通支持工单，Fortinet 的开发团队正在确认问题持续存在。PSIRT 的 Carl Windsor 正在领导取证工作。  
  
这些协同攻击表明，有威胁行为者针对未打补丁的 FortiGate 设备发起攻击活动。Fortinet 承认该问题在 7.4.10 版本中仍然存在，并计划在后续版本中修复。  
  
12 月中旬，Shadowserver 发现超过 25,000 台Fortinet 设备可在网上公开访问，值得注意的是，其中许多设备都激活了 FortiCloud 单点登录 (SSO) 功能。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB12TK1TY95XXHmmicMYSSusdicznQog7fVYgK4FWOhEe7pemuolPAsRQ04MxFU7Zibd1ggayf3dUib93w/640?wx_fmt=png&from=appmsg "")  
  
  
