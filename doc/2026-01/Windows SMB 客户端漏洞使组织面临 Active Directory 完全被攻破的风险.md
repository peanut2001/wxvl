#  Windows SMB 客户端漏洞使组织面临 Active Directory 完全被攻破的风险  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-01-20 01:00  
  
**导****读**  
  
  
  
Windows Server 消息块 (SMB) 客户端身份验证中的一个严重漏洞已成为 Active Directory 环境的重大威胁。  
  
  
CVE-2025-33073 是 NTLM 反射处理中的一个逻辑缺陷，它使经过身份验证的攻击者能够提升到 SYSTEM 级别的权限并攻破域控制器，从而有可能接管整个 Active Directory 林。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHxuoPiaMxtsN1yIwmHlnF00Op798XugoUz2kf7WIkrMeVZPLTj68PctJ1KKM9JB9iaTbbic3h163CicQ/640?wx_fmt=png&from=appmsg "")  
  
### 漏洞概述  
  
  
微软将该漏洞描述为“Windows SMB中不正确的访问控制”。然而，安全研究人员发现，该漏洞的危险性远超最初的描述。  
   
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHxuoPiaMxtsN1yIwmHlnF00N3URuZv0mgj7ibXAslicZ0AXM5YZ4L6R5USzVr6o6kDqul5CA4icpAUSg/640?wx_fmt=png&from=appmsg "")  
  
成功利用 CVE-2025-33073 漏洞进行 SMB->SMB 中继（来源：Depth Security）  
  
  
该漏洞利用了 NTLM 本地身份验证机制，允许攻击者以 SYSTEM 权限将来自受感染机器的身份验证转发回自己，从而绕过传统的 SMB 签名保护。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHxuoPiaMxtsN1yIwmHlnF00MUUibP0NULp0EYWSk0uzg1teibB2MK0WemiaCv7wxndjE4y6pTiaUVEcibg/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞利用了一种复杂的凭证强制技术。攻击者注册包含特制、序列化目标信息的 DNS 记录（例如，srv1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAWbEAYBAAAA），并使用 PetitPotam 等强制方法迫使计算机向攻击者控制的服务器进行身份验证。  
    
  
  
当目标检测到精心构造的 DNS 名称时，Windows SMB 客户端库会剥离序列化信息，只留下主机名（例如，srv1）。  
  
  
然后，SMB 客户端向服务器发出信号，要求执行本地 NTLM 身份验证。这会触发一个严重漏洞：LSASS（本地安全授权子系统服务）会将其 SYSTEM 令牌复制到共享的身份验证上下文中。  
    
  
  
当攻击者将此身份验证转发回目标机器时，他们无需禁用 SMB 签名即可继承 SYSTEM 权限。  
  
  
攻击之所以成功，是因为漏洞存在于 SMB 客户端的身份验证协商过程中，而不是签名强制执行过程中。  
    
  
  
即使启用了 SMB 签名的机器，在通过部分消息完整性代码 (MIC) 删除技术  
  
向 LDAP、LDAPS 和其他协议中继时，仍然容易受到攻击，这些技术利用了协议特定的身份验证处理。   
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHxuoPiaMxtsN1yIwmHlnF00ChLnibAwdfYzdshCpNf9QTL71BOTBP095UJjeC8gT78L58POmibWOaHw/640?wx_fmt=png&from=appmsg "")  
  
身份验证绕过（来源：Depth Security）  
  
  
安全研究人员已经证明，CVE-2025-33073 能够实现以前认为不可能的跨协议中继攻击。  
  
  
攻击者通过剥离特定的 NTLMSSP 标志（协商签名、协商密封），同时保留 MIC，可以将 SMB 身份验证转发到域控制器上的 LDAP 和 LDAPS 服务。  
  
  
这使得攻击者可以直接修改 Active Directory 对象，例如将受损帐户添加到特权组、修改访问控制，或者执行 DCSync 攻击以提取整个凭据数据库。  
  
  
该漏洞还会导致 Kerberos 反射攻击，即使在强化的环境中也会产生多种攻击途径。  
  
  
研究表明，这些技术可以在强制执行通道绑定和签名的环境中发挥作用，使得传统的防御措施不足。  
  
  
公开披露七个月后，大多数组织仍未修复受影响的系统。渗透测试人员不断在企业网络中发现存在漏洞的主机，从工作站到域控制器和零层服务器均有涉及。  
    
  
  
利用 ntlmrelayx.py 等公开可用的工具，通过部分移除 MIC 的修改，即可轻松实现对环境的完全入侵。  
  
  
根据深度安全评估，立即补救措施需要安装 Microsoft 安全更新，并在所有加入域的系统中强制执行 SMB 签名。  
    
  
  
组织还必须在 LDAP 和 LDAPS 服务上实施通道绑定强制执行，将 DNS 记录注册限制为仅限管理帐户，并对广播域进行分段，以防止网络级攻击。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHxuoPiaMxtsN1yIwmHlnF00OyQmr1g8fdIPK7yHp9v7YIySXSIWSPgLrwjYBYlK4CAJ75ibW5icpbSg/640?wx_fmt=png&from=appmsg "")  
  
“成功”（未成功）的带签名功能的 SMB->SMB 中继（来源：Depth Security）  
  
  
此外，阻止所有 NetNTLMv1 身份验证并强制使用 Kerberos 可以减少攻击面。  
    
  
  
但是，各组织应该注意，如果没有适当的防御措施，Kerberos 反射攻击也会带来重大风险。  
  
  
该漏洞代表了 NTLM 反射缓解措施的根本缺陷，而不是简单的签名绕过，因此需要立即加强全面的身份验证。  
  
  
详细漏洞分析：  
  
《利用 NTLM 反射控制 Active Directory (CVE-2025-33073)》  
  
https://www.depthsecurity.com/blog/using-ntlm-reflection-to-own-active-directory/  
  
  
新闻链接：  
  
https://gbhackers.com/windows-smb-client-vulnerability/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
