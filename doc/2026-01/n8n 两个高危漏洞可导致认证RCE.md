#  n8n 两个高危漏洞可导致认证RCE  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-01-29 09:51  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**网络安全研究员披露了位于工作流自动化平台n8n 中的两个新漏洞，其中一个严重漏洞可导致远程代码执行后果。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
这两个漏洞的简述如下：  
  
- CVE-2026-1470（CVSS 9.9）：eval 表达式注入漏洞，可导致经过身份验证的用户通过传递特殊构造的 JavaScript 代码，绕过表达式沙箱机制并在 n8n 的主要节点上实现完整的远程代码执行。  
  
- CVE-2026-0863（CVSS 8.5）：eval 表达式注入漏洞，可导致经过身份验证的用户绕过 n8n 的 python-task-executor 沙箱限制并在底层操作系统上运行任意 Python 代码。  
  
  
  
成功利用这些漏洞可导致攻击者劫持整个 n8n 实例，包括在 “内部”执行模式下运行的场景。n8n在文档中提到，在生产环境中使用内部模式可带来安全风险，因此督促用户切换为外部模式，确保 n8n 和任务运行进程之间的适当隔离。  
  
研究人员提到，“随着 n8n 在整个组织机构中实现AI工作流程自动化，它掌握着核心工具、功能及基础设施数据（如LLM API、销售数据和内部内部身份管理系统等）的访问权限。一旦发生安全突破，相当于为黑客提供了开启整个企业系统的‘万能钥匙’。”  
  
为修复这些漏洞，建议用户更新至如下版本：  
  
- CVE-2026-1470：1.123.17、2.4.5或2.5.1  
  
- CVE-2026-0863：1.123.14、2.3.5或2.4.2  
  
  
  
就在几周前，Cyera 研究实验室就详述了位于 n8n 中的一个满分漏洞CVE-2026-21858，可导致未经身份验证的远程攻击者获得对可疑实例的完全控制。  
  
研究人员 Nathan Nehorai 表示，“这些漏洞凸显了安全沙箱隔离动态高级语言如 JavaScript 和 Python 的难度之高。即使部署了多重验证层、禁用清单和基于抽象语法树的控制，细微的语言特性和运行时行为可用于绕过安全假设。在这种情况下，已被弃用或很少使用的语法结构，结合解释器的变更和异常处理机制，足以突破原本严密的沙箱环境，最终实现远程代码执行。”  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[n8n 满分漏洞 Ni8mare 可导致服务器遭劫持](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524822&idx=1&sn=e3ab93e00fc28bdb1a256d94e84507f3&scene=21#wechat_redirect)  
  
  
[n8n严重漏洞可导致任意代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524734&idx=1&sn=7accfa41ad8e25a3c0a292eb451552af&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
