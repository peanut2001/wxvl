#  Windows SMB 客户端漏洞使攻击者能够控制 Active Directory  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-01-19 11:16  
  
Windows SMB 客户端身份验证中的一个严重漏洞，攻击者可以利用该漏洞通过 NTLM 反射攻击来入侵Active Directory环境。  
  
该漏洞被归类为不当访问控制漏洞，它允许授权攻击者通过精心策划的身份验证中继攻击，利用网络连接来提升权限。  
  
在 2025 年 6 月安全补丁发布七个月后，研究显示企业基础设施普遍未采用该补丁。  
  
几乎每次渗透测试都会在域控制器、零层服务器和工作站上发现易受攻击的主机。该漏洞利用了Windows NTLM本地身份验证中的一个基本机制。  
  
![成功实现存在缺陷的SMB中继](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKKcwhCITicCAjVfGf1uQS0mID96h3X0PBpjuNutiaZaKKId1X7AbntUfwfxpqvaxYmNmGxjKypnvI3g/640?wx_fmt=jpeg&from=appmsg "")  
  
当客户端收到标记为本地身份验证的 NTLM_CHALLENGE 消息时，系统会创建一个上下文对象，并将上下文 ID 插入到保留字段中。  
  
该机制与 PetitPotam、DFSCoerce 和 Printerbug 等强制技术相结合，迫使 lsass.exe（以 SYSTEM 身份运行）向攻击者控制的服务器进行身份验证。  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">方面</span></font></font></strong></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">细节</span></font></font></strong></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE标识符</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE-2025-33073</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">漏洞类型</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">NTLM 反射/权限提升</span></font></font></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">攻击向量</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">网络（强制+认证中继）</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">补丁发布</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">2025年6月Windows更新</span></font></font></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">主要影响</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">完全</span></font></font><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">入侵活动</span></font></font><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">目录</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">当前状态</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">企业环境中普遍未打补丁</span></font></font></td></tr></tbody></table>  
然后服务器会冒充 SYSTEM 令牌进行后续操作，从而有效地完全控制系统。  
## 攻击需求 和利用途径  
  
利用此漏洞需要要么在 AD DNS 中注册恶意 DNS 记录（默认情况下允许已验证用户这样做），要么在本地网络中执行 DNS 投毒。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKKcwhCITicCAjVfGf1uQS0mI3zz03z9Xiba6yrq1BuVeLo3dTjPjJMVUrMzPdHjDpm0iah0W8nCNm96Q/640?wx_fmt=png&from=appmsg "")  
  
这些低权限要求从根本上增加了攻击面，因为大多数组织没有限制已认证用户在 AD DNS 区域中创建任意 DNS 记录。  
  
传统的缓解措施不足以应对高级攻击手段。  
  
虽然SMB 签名通常可以防止中继攻击，但研究表明，通过强制执行签名和通道绑定，可以成功地从 SMB 到 LDAPS 进行跨协议中继。  
  
这种绕过方法涉及移除特定的 NTLMSSP 标志（始终协商签名、协商密封、协商签名），同时保留消息完整性代码。该技术使攻击者能够同时绕过多个安全控制措施。  
## 超出SMB签名范围的扩展攻击面  
  
该漏洞的影响范围不仅限于传统的 SMB 到 SMB 中继。DepthSecurity 的研究人员证实，通过跨协议中继技术，针对 ADCS 注册服务、MSSQL 数据库和 WinRMS 的攻击已取得成功。  
  
更令人担忧的是，SMB 到 LDAPS 反射攻击允许攻击者直接使用SYSTEM 权限操纵 Active Directory 对象。  
  
通过 DCSync 操作启用组成员身份修改和凭证收集。  
  
基于 RPC 的中继尝试揭示了与 SMB 签名类似的会话密钥加密要求，这表明基本的Windows身份验证机制加剧了该漏洞的影响。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKKcwhCITicCAjVfGf1uQS0mIdF06aLgv6QOa0SBqQMqQduKVSNHTGq2udoHdWW2TfAK8cUicrs1NRQQ/640?wx_fmt=png&from=appmsg "")  
  
攻击者成功通过 RPC 服务进行身份验证，但在后续操作中遇到访问控制，这表明可以通过 Net-NTLMv1 身份验证进行攻击。  
  
根据DepthSecurity 的建议，企业必须立即应用 2025 年 6 月的 Windows 安全更新，作为首要缓解措施。此外，还应在所有协议（不仅限于 SMB）上启用签名和通道绑定强制执行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKKcwhCITicCAjVfGf1uQS0mIx9c7XIN2g0yZFKdtibaAWF6ArSHWSDicVmQKibnRjKwU5mXyfiaHQ1Nc9A/640?wx_fmt=png&from=appmsg "")  
  
重新配置 Active Directory DNS 区域访问控制列表，限制已验证用户创建 DNS 记录，可显著降低被利用的可能性。  
  
安全团队必须优先考虑迅速修补 NTLM 强制技术漏洞，并对整个基础设施中的 NTLM 中继攻击方法进行彻底审计。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKKcwhCITicCAjVfGf1uQS0mIU1kWQCUfSspkkZOlx4yiarOnhX9zuMfdiaH6m2pWDFDqL5tbiabbf9lsw/640?wx_fmt=png&from=appmsg "")  
  
  
