#  Jenkins 存在严重漏洞导致建环境易受 XSS 攻击  
原创 ZM
                    ZM  暗镜   2026-02-20 23:00  
  
安全公告揭示了 Jenkins Core 中的多个漏洞，包括一个存储型跨站脚本 (XSS) 漏洞，该漏洞可能使构建环境面临严重的安全风险。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb3koLHiayXic1jpl69K2q4StO2qQwcLAekGOgyChaw2roKUEwLYUBwnqUcb1mQjOJdbRibmtLawGnjc2hDYOicQXeh5Rr9uiaJGBvRs/640?wx_fmt=png&from=appmsg "")  
  
  
这些问题被确定为 CVE-2026-27099 和 CVE-2026-27100，并根据欧盟委员会赞助的Jenkins漏洞赏金计划进行了负责任的披露。  
  
其中最严重的一个漏洞，编号为 CVE-2026-27099，是一个高危存储型 XSS 漏洞，会影响 Jenkins 2.550 及更早版本，以及 LTS 2.541.1 及更早版本。  
  
该缺陷源于 Jenkins 处理“离线原因描述”的方式，该描述解释了构建节点离线的原因。  
  
自 2.483 版本起，这些描述允许 HTML 内容，但在易受攻击的版本中，输入内容没有被正确转义。  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE ID</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVSS评分</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">描述</span></font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">受影响版本</span></font></font></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE-2026-27099</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">高的</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">节点离线原因描述中存储的 XSS 漏洞</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">詹金斯 ≤ 2.550，LTS ≤ 2.541.1</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">CVE-2026-27100</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">中等的</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">通过运行参数披露构建信息</span></font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);text-align: left;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">詹金斯 ≤ 2.550，LTS ≤ 2.541.1</span></font></font></td></tr></tbody></table>  
拥有 Agent/Configure 或 Agent/Disconnect 权限的攻击者可以将恶意 JavaScript 注入到离线原因描述中，从而可能危及其他用户的会话。  
  
Jenkins 版本 2.551 和 LTS 2.541.2 通过转义用户提供的输入来解决此问题。  
  
此外，在 Jenkins 2.539 及更高版本上强制执行内容安全策略 (CSP) 的实例 可以部分抵御这些攻击。  
  
第二个漏洞 CVE-2026-27100，严重程度为中等，会影响 Jenkins 处理运行参数值的方式。  
  
在受影响的 2.550 及更早版本（以及 LTS 2.541.1）中，用户可以查询他们没有权限访问的构建或作业。  
  
这使得攻击者能够确定是否存在特定的项目或构建，从而可能导致 Jenkins 环境中的信息泄露。  
  
Jenkins 2.551 和 LTS 2.541.2 现在可以正确拒绝未经授权的运行参数值，从而防止此类数据泄露。  
  
强烈建议 Jenkins 管理员更新至最新版本 2.551 或 LTS 2.541.2，以缓解这两个漏洞。依赖旧版本的构建仍然存在脚本注入和构建信息未经授权泄露的风险。  
  
