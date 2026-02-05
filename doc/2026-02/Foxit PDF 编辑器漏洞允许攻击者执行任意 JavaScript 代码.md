#  Foxit PDF 编辑器漏洞允许攻击者执行任意 JavaScript 代码  
原创 ZM
                    ZM  暗镜   2026-02-05 00:00  
  
近期Foxit PDF 安全更新修复了 Foxit PDF Editor Cloud 中的关键跨站脚本(XSS) 漏洞，这些漏洞可能允许攻击者在用户的浏览器中执行任意 JavaScript 代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCStib0QBo7Xm5wsDC4F71k4ZiaNAxZL0q72EtZiauvaxV6vGzu2tHgLukOeAbW42qcur7XepCPAMqR83kg/640?wx_fmt=png&from=appmsg "")  
  
  
这些漏洞是在应用程序的文件附件列表和图层面板中发现的，其中输入验证不足和输出编码不当为恶意代码执行提供了途径。  
  
已发现两个相关的跨站脚本漏洞，并分别分配了 CVE-2026-1591 和 CVE-2026-1592。  
  
这两个漏洞都源于同一个根本原因：图层名称和附件文件名中的用户输入清理不足。  
  
当用户通过“文件附件”列表或“图层”面板与精心制作的有效载荷进行交互时。  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE ID</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">漏洞类型</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVSS评分</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">严重程度</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">影响</span></font></font></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE-2026-1591</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">跨站脚本攻击 (CWE-79)</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">6.3</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">缓和</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">任意执行 JavaScript 代码</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE-2026-1592</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">跨站脚本攻击 (CWE-79)</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">6.3</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">缓和</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">任意执行 JavaScript 代码</span></font></font></td></tr></tbody></table>  
该应用程序在将不受信任的输入嵌入到 HTML 结构之前未能正确编码该输入，从而允许在用户的浏览器上下文中执行任意JavaScript代码。  
  
这些漏洞被归类为CWE-79（跨站脚本攻击），CVSS 3.0 得分为 6.3，表明其严重程度中等。  
  
攻击向量是基于网络的（AV:N），攻击复杂度低（AC:L），所需权限低（PR:L）且无需用户交互（UI:R）。  
  
攻击者利用这些漏洞可以访问已认证用户可见的敏感信息，包括文档内容和会话数据。  
  
用户交互和身份验证访问的要求在一定程度上限制了攻击面，因为攻击者必须首先诱骗用户打开恶意文档或说服他们与特制的文件进行交互。  
  
然而，中等严重程度评级反映了这些 XSS 漏洞在广泛使用的PDF 编辑应用程序中构成的实际威胁。  
## 补救和响应  
  
作为 2026 年 2 月 3 日 Foxit PDF Editor Cloud 更新的一部分，Foxit 发布了安全补丁，解决了这两个漏洞。  
  
该公司强调，云版本无需用户操作，更新会自动部署。  
  
使用桌面版软件的用户应通过应用程序的更新机制检查可用更新。  
  
使用 Foxit PDF 编辑器的组织应确认其安装的版本是否为最新补丁版本。  
  
安全响应团队建议审查文件处理规范，并在组织安全策略允许的范围内限制用户对 PDF 编辑功能的访问。  
  
  
  
