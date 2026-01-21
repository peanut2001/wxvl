#  Anthropic官方Git MCP服务器曝链式漏洞，可致文件访问与代码执行  
 FreeBuf   2026-01-21 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqicrdic5icku8cXyORbJUic2vADCQh2TkeaCabVYusWueWJORHE26s2TyJYA47hJftpJ1WmpehSSFDA/640?wx_fmt=png&from=appmsg "")  
  
  
Anthropic PBC的官方Git Model Context Protocol（模型上下文协议）服务器存在多个安全漏洞，可能引发任意文件访问，某些情况下甚至能通过提示词注入（prompt injection）实现完整的远程代码执行。人工智能安全初创公司Cyata Security Ltd今日发布的最新研究报告披露了这一情况。这些漏洞影响mcp-server-git——Anthropic为Git开发的MCP参考实现，该组件旨在向开发者示范如何安全地将Git仓库暴露给基于大语言模型的AI Agent。  
  
  
**Part01**  
## 漏洞影响范围与攻击向量  
  
  
根据Cyata报告，2025年12月18日前发布的所有默认部署版本均受影响。攻击者只需能操控AI助手读取的内容（例如恶意README文件、被污染的议题描述或遭篡改的网页）即可利用这些漏洞。研究人员在服务器中发现三个独立漏洞：  
  
- 无限制的git_init功能：允许在任意文件系统路径初始化仓库  
  
- 路径验证绕过漏洞：可访问配置允许列表之外的仓库  
  
- git_diff工具的参数注入缺陷：将未净化的输入传递给Git命令行接口  
  
当这些漏洞被串联利用时，攻击者能够读取或删除任意文件，甚至覆盖主机系统上的文件。  
  
  
**Part02**  
## 参考实现中的安全隐患  
  
  
这些漏洞的特殊性在于，问题代码出现在Anthropic自家的参考实现中。"这是标准的Git MCP服务器，开发者理应效仿的样板，"Cyata联合创始人兼首席执行官Shahar Tal表示，"如果安全边界在参考实现中就已瓦解，说明整个MCP生态系统需要更严格的审查。这些并非边缘案例或特殊配置，而是开箱即用的漏洞。"  
  
  
**Part03**  
## 漏洞评级差异与风险场景  
  
  
不同评分系统对漏洞严重性的评估存在差异：GitHub安全公告根据通用漏洞评分系统4.0（CVSS 4.0）评定为中等严重程度，而GitLab咨询数据库则依据CVSS 3.1将其列为高危。Cyata解释称，这种差异源于GitHub采用的CVSS 4.0采用了更精细的评分方法。漏洞风险程度还取决于Git MCP服务器的使用场景，当与Filesystem MCP服务器共同使用时，风险会显著增加。  
  
  
**Part04**  
## 远程代码执行实现机制  
  
  
在此类混合部署场景中，攻击者可滥用Git的smudge和clean过滤器，通过仓库配置文件中定义的shell命令实现远程代码执行。由于MCP服务器执行大语言模型（LLM）的决策，而LLM又可能通过提示词注入被操控，这意味着整个攻击链无需凭证、shell访问或与目标系统的直接交互即可触发。"这项研究表明，当LLM被置于决策循环中时，关于信任边界的传统假设就会崩塌，"Cyata联合创始人兼首席技术官Baruch Weizman指出，"单独看起来安全的工具，在攻击者控制模型输入时会变得危险。"  
  
  
**Part05**  
## 修复时间线与安全建议  
  
  
Cyata已于去年6月向Anthropic报告这些漏洞，相关修复于12月17日发布，其中包括从Git MCP服务器中彻底移除git_init工具。安全团队建议尚未更新mcp-server-git的组织立即采取行动：将所有MCP工具参数视为不可信输入，限制AI Agent可调用的MCP服务器和工具范围，并从整体而非单个工具角度评估Agent权限。  
  
  
**参考来源：**  
  
Anthropic’s official Git MCP server hit by chained flaws that enable file access and code execution  
  
https://siliconangle.com/2026/01/20/anthropics-official-git-mcp-server-hit-chained-flaws-enable-file-access-code-execution/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
  
### 电台讨论  
###   
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
