#  新型 Kerberos 中继攻击利用 DNS CNAME 绕过缓解措施——POC已发布  
原创 ZM
                    ZM  暗镜   2026-01-20 00:08  
  
身份验证存在严重缺陷，这大大扩大了 Active Directory 环境中凭据中继攻击的攻击面。  
  
通过滥用 Windows 客户端在 Kerberos 服务票证请求期间处理 DNS CNAME 响应的方式，攻击者可以胁迫系统请求攻击者控制的服务的票证，从而绕过传统的保护措施。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCStibAvvfq7ob445u4G6ibc2lhSotUMhiaXEdU5BHEdDLoMKgk73jURFah9cICkohMMX2AckeTXXZPb1KA/640?wx_fmt=png&from=appmsg "")  
# 攻击向量  
  
该漏洞的核心在于一个基本行为：当 Windows 客户端收到，它会跟随别名。它会使用 CNAME 主机名作为服务主体名称 (SPN) 来构建票据授予服务 (TGS) 请求。  
  
攻击者若能部署在拦截 DNS 流量的路径上，便可利用此漏洞迫使受害者为攻击者选择的目标请求服务票据。  
  
该技术要求攻击者通过 ARP 投毒、DHCPv6 投毒 (MITM6) 或类似方法建立 DNS  
  
当受害者尝试访问合法的域名资产时，恶意 DNS 服务器会响应一个指向攻击者控制的主机名的 CNAME 记录，以及一个解析到攻击者 IP 地址的 A 记录。  
  
这会导致受害者使用原本用于攻击者目标服务的票据，对攻击者的基础设施进行身份验证。  
  
攻击能力和影响  
：  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">影响区域</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">描述</span></font></font></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">RCE</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">通过 ADCS Web 注册进行远程代码执行 (ESC8)</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">中继攻击</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">跨协议中继（HTTP→SMB，HTTP→LDAP）</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">横向移动</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">未经授权的访问和网络传播</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">冒充</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">无需密码即可冒充用户</span></font></font></td></tr></tbody></table>  
  
、Windows Server 2022 和 Windows Server 2025 的默认配置下均可生效。  
  
当未强制执行签名或通道绑定令牌 (CBT) 时，该攻击可成功攻击未受保护的服务，包括 SMB、HTTP 和 LDAP。该漏洞已于 2025 年 10 月负责任地披露给微软。  
  
DNS投毒会将受害者重定向到恶意目标，强制发起Kerberos TGS请求。（来源：Cymulate）  
  
作为回应，微软为 HTTP.sys 实施了 CBT 支持。它在 2026 年 1 月的安全更新中发布了针对受支持的 Windows Server 版本的补丁，跟踪编号为。  
  
然而，这种缓解措施仅针对 HTTP 中继场景。底层 DNS CNAME 强制转换机制保持不变，其他协议仍然存在安全漏洞。  
  
上发布了 MITM6 工具的修改版，该版本具备 CNAME 污染功能。该工具支持针对特定域名或所有 DNS 查询的定向 CNAME 污染。  
  
包含用于集成 ARP 欺骗的仅 DNS 模式，并支持关键基础设施连接的透传。利用此漏洞需要 Python 3.x 和操作系统。  
  
![adcs-server.mycorp.local 的记录指向攻击者的 IP 地址 ](https://mmbiz.qpic.cn/mmbiz_jpg/mibm5daOCStibAvvfq7ob445u4G6ibc2lhSNqngZvfibofEn1zymTDfoPqnETeGFlThG2UvWRQIiaVoAwia213uZiaMhA/640?wx_fmt=jpeg&from=appmsg "")  
  
adcs-server.mycorp.local 的记录指向攻击者的 IP 地址（来源：Cymulate）  
  
这项研究强调了一个关键的安全现实：Kerberos 本身并不能从根本上阻止中继攻击。保护措施的实施取决于服务层。  
  
仅仅禁用 NTLM 是不够的；组织必须在每个启用 Kerberos 的服务中明确强制执行防中继保护，才能有效消除中继风险。  
  
