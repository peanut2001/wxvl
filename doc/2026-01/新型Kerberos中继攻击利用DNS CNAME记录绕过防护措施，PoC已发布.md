#  新型Kerberos中继攻击利用DNS CNAME记录绕过防护措施，PoC已发布  
 FreeBuf   2026-01-20 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibO6LkQfeNnUaf9R26BHTnQwLULlQ2ypSBGWSbDFuMLAz3hib5sHyV1tw/640?wx_fmt=png&from=appmsg "")  
  
  
Windows Kerberos认证中存在一个关键漏洞，该漏洞显著扩大了Active Directory环境中凭据中继攻击的攻击面。攻击者通过滥用Windows客户端在Kerberos服务票据请求期间处理DNS CNAME响应的方式，可以诱使系统为攻击者控制的服务器请求票据，从而绕过传统防护措施。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibJHcFJNwXRjAWicNCp77XMQDsS3wfPa3nMyGFmiaN8ibw2wcJMk5srfgrg/640?wx_fmt=jpeg&from=appmsg "")  
  
攻击流程图（来源：Cymulate）  
  
  
**Part01**  
## 攻击向量分析  
  
  
该漏洞的核心在于一个基本行为：当Windows客户端收到DNS CNAME记录时，它会遵循别名。客户端使用CNAME主机名作为服务主体名称（SPN）来构造票据授予服务（TGS）请求。能够拦截DNS流量的攻击者可以利用这一点，迫使受害者向攻击者选择的目标请求服务票据。  
  
  
这种技术需要攻击者通过ARP欺骗、DHCPv6欺骗（MITM6）或类似方法建立DNS中间人攻击能力。  
  
  
![受害者被重定向到攻击者的服务器，服务器返回401强制Kerberos认证](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibDcyiaPLibpTHOeGyronppLn0hibOd8vibErfLicWQLM6iaVvicfTNkSHKxGLA/640?wx_fmt=jpeg&from=appmsg "")  
  
受害者被重定向到攻击者的服务器，服务器返回401强制Kerberos认证（来源：Cymulate）  
  
  
当受害者尝试访问合法域资产时，恶意DNS服务器会返回一个指向攻击者控制主机名的CNAME记录，以及一个解析为攻击者IP地址的A记录。这导致受害者使用为攻击者目标服务准备的票据向攻击者基础设施进行认证。  
  
  
**Part02**  
## 攻击能力与影响  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ib0WTicNicwsw0gRcfZEJxbBJqjZ8OfVMK1KuZ4d6lzyKiaomnN8Motw0Bw/640?wx_fmt=png&from=appmsg "")  
  
  
测试证实，该漏洞在Windows 10、Windows 11、Windows Server 2022和Windows Server 2025的默认配置下均可成功利用。当未强制执行签名或通道绑定令牌（CBT）时，攻击可成功针对SMB、HTTP和LDAP等未受保护的服务。该漏洞已于2025年10月向微软负责任的披露。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibGWfWVafp3mgFDM4NGAVfkue6PcmQPo09ErhqkNfZsTwTvd4b9CA3mg/640?wx_fmt=jpeg&from=appmsg "")  
  
DNS投毒将受害者重定向到恶意目标，强制发起Kerberos TGS请求（来源：Cymulate）  
  
  
作为回应，微软为HTTP.sys实现了CBT支持，并在2026年1月的安全更新中为支持的Windows Server版本发布了补丁（CVE-2026-20929）。然而，这种缓解措施仅解决了HTTP中继场景，底层的DNS CNAME强制原语仍未改变，其他协议仍然存在漏洞。  
  
  
**Part03**  
## 概念验证  
  
  
研究人员在GitHub上发布了具有CNAME投毒能力的MITM6工具修改版。该工具支持针对特定域或所有DNS查询的定向CNAME投毒，包含用于ARP欺骗集成的纯DNS模式，并支持关键基础设施连接的直通功能。利用该工具需要Python 3.x和Linux操作系统。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibOxbGm2RIWgdic93eREflyIwpBzicMAynQcX0ic1ag4xlSJUH3smRI9xjg/640?wx_fmt=jpeg&from=appmsg "")  
  
adcs-server.mycorp.local的A记录指向攻击者IP（来源：Cymulate）  
  
  
Cymulate研究实验室建议组织采取分层防御措施：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibNAvt2dxuia0DHBsoic92WK3wLUMdcclCNldwqkiaDoSxMVdiao371xRbzA/640?wx_fmt=png&from=appmsg "")  
  
  
这项研究揭示了一个关键的安全现实：Kerberos本身并不能防止中继攻击，防护措施的实施取决于服务级别。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibxFOsAVvZjZ7ibNx0NTcC9ibjQxgnFoWoHVAYKnWmRSFytx4ZAXoDOQtW9EMIfRcF5EupvSLtqgRLg/640?wx_fmt=jpeg&from=appmsg "")  
  
DNS投毒后，受害者连接到攻击者的恶意HTTP或SMB服务器（来源：Cymulate）  
  
  
仅禁用NTLM是不够的，组织必须明确地在每个支持Kerberos的服务上强制执行反中继保护，才能有效消除中继风险。  
  
  
**参考来源：**  
  
New Kerberos Relay Attack Uses DNS CNAME to Bypass Mitigations – PoC Released  
  
https://cybersecuritynews.com/kerberos-relay-attack-uses-dns-cname/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
###   
### 电台讨论  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
