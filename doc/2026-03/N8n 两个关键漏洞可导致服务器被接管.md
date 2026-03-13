#  N8n 两个关键漏洞可导致服务器被接管  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-03-13 01:00  
  
**导****读**  
  
  
  
Pillar Security 报告称，n8n 中的两个严重漏洞可能被利用进行未经身份验证的远程代码执行 (RCE) 和沙箱逃逸，从而暴露存储在 n8n 数据库中的所有凭据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyKTTUvuhSWW3BcGbjebIvTalQICyXcLGJffc1SjKiaeuicWYr6JSgkLoAsicCxSF6hXT3q14Br4QsMSNDOqrjS0U1EJ7W6scLAoII/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞被追踪为 CVE-2026-27493（CVSS 评分为 9.5），第一个漏洞被描述为影响开源工作流自动化平台表单节点的二阶表达式注入问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyI0YyplEnqJwTen1X0iaMfDVe1QDBgicOwVRZAwKDO5WuWklbzMgIW2QC9Y2YmCBUF6wl51sicFFD63aJ5J8o2xbHOA6nvDv5bhcg/640?wx_fmt=png&from=appmsg "")  
  
成功利用此漏洞可能允许未经身份验证的攻击者向名称字段注入任意命令，并接收已执行命令的输出。  
  
  
该安全缺陷的出现是因为 n8n 依赖于两次表达式求值过程来评估用户的提交内容，攻击者的有效载荷在第二次求值过程中被评估为一个新表达式。  
  
  
Pillar 解释说，该漏洞可能与第二个严重缺陷（编号为 CVE-2026-27577，CVSS 评分为 9.4）联动，从而逃逸 n8n 沙箱并在主机上执行命令。  
  
  
安全团队表示，该漏洞允许恶意有效载荷绕过沙箱保护并执行，因为易受攻击的节点在编译阶段运行，早于运行时清理程序。  
  
  
这两个安全缺陷已于 2 月下旬在 n8n 版本 2.10.1、2.9.3 和 1.123.22 中得到解决。该补丁移除了第二次表达式求值过程和某些先前接受的参数，将几个全局标识符添加到沙箱的阻止标识符列表中，并加强了 AST 感知标识符分析。  
  
  
据 Pillar 称，这两个漏洞会影响自托管和云部署，并可能被利用来从 n8n 数据库中提取所有凭证，包括 AWS 密钥、密码、OAuth 令牌和 API 密钥。  
  
  
Pillar指出：“n8n本质上是一个凭证库。它存储着与其连接的每个系统的密钥。一次沙箱逃逸就会暴露n8n实例及其连接的每个系统。”  
  
  
安全公司指出，由于表单端点旨在从互联网访问，因此任何人只需提交一个表单并发出一个 GET 请求即可利用 CVE-2026-27493。  
  
  
Pillar指出：“对于n8n Cloud和多租户部署而言，其影响远不止于单个实例。正如之前所展示的，n8n Cloud上的沙箱逃逸会授予对共享基础设施的访问权限，从而造成跨租户风险：一个租户工作流程中的一个公共表单就可能成为攻击入口。”  
  
  
n8n 是一款开源、可视化、可自托管的工作流自动化平台，主打无代码 / 低代码拖拽 + 代码扩展。  
  
  
n8n 应用非常广泛，已从开源工具成长为全球主流的工作流自动化平台之一，覆盖个人、中小企业与大型企业，横跨 IT、运营、营销、金融、制造、AI 等多个领域。  
  
  
详细漏洞公告：  
  
https://www.pillar.security/blog/zero-click-unauthenticated-rce-in-n8n-a-contact-form-that-executes-shell-commands  
  
  
新闻链接：  
  
https://www.securityweek.com/critical-n8n-vulnerabilities-allowed-server-takeover/  
  
  
****  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
