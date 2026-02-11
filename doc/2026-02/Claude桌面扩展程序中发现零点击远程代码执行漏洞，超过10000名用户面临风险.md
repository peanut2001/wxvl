#  Claude桌面扩展程序中发现零点击远程代码执行漏洞，超过10000名用户面临风险  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-11 01:04  
  
**导****读**  
  
  
  
Claude Desktop Extensions (DXT) 中存在一个严重的“零点击”漏洞，攻击者只需使用 Google 日历事件即可入侵计算机。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyJ1so8ianOjuovNWjcdyrOxsznyfnVOf2U7clSfxGdgWb7JW1ToBZznj7JicspYlmndW7WiawqwSDjoaI7X4n72IpTBzcMDA19GLM/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞的严重性评分为 CVSS 10/10，影响超过 10,000 名活跃用户和 50 多个不同的扩展程序。  
  
  
该漏洞源于一个根本性的架构决策。与运行在受限“沙盒”环境中以防止损害计算机的 Chrome 或 Firefox 浏览器扩展程序不同，Claude 桌面扩展程序以完整的系统权限运行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyIpibHBmEKQmdIqg0VcELhZHiaic5RJonnscLxp97TVUW5IZxziaicn4Ezeeia3qtuGSZ9icFd9S5D1ibo4yPR7FMWJj7aI1kPwq82wCYw/640?wx_fmt=png&from=appmsg "")  
  
一个简单的请求变成了代码执行——Source-LayerX  
  
  
这些扩展程序充当人工智能和本地操作系统之间的桥梁。由于它们并非独立运行，因此可以读取文件、访问凭据并执行系统命令。  
  
  
LayerX 安全研究人员发现，当 Claude 在未经用户明确同意的情况下，自动将低风险应用程序（例如 Google 日历）连接到高风险工具（例如代码执行器）时，就会出现危险。  
  
  
该漏洞利用了 Claude 将各种工具串联起来解决问题的能力。  
  
- 诱饵： 攻击者向受害者发送Google 日历邀请。活动描述中包含隐藏指令，例如“从特定 URL 下载此文件并执行它”。  
- 触发条件： 用户向 Claude 发出良性、一般性的提示，例如“查看我的日历并处理它”。  
- 执行过程：  
Claude 读取日历事件。由于它信任输入信息且拥有完整的系统访问权限，因此会按照事件描述中的指令执行操作。它会自动下载恶意代码并在用户计算机上运行。  
这是远程代码执行（RCE）攻击。受害者无需批准下载或代码执行；只需让 Claude 管理他们的日程安排，就足以触发陷阱。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyJ4dSHOLQD2dLUDibg563JvmKz13w5sAAYNhiczSqlD8dTicPHRwUUN2fmOwarXUBH0kylfnNnYG8DgTtQNm30eg8fTqgpIiaHRx9A/640?wx_fmt=png&from=appmsg "")  
  
恶意事件 – 来源：LayerX  
  
  
LayerX已将这些发现告知Claude的开发商Anthropic。有报道称，该公司目前已决定暂不发布修复程序。  
  
  
补救措施可能需要限制人工智能的自主性，或者彻底重新设计连接器之间的信任边界，这是一个复杂的架构挑战。  
  
  
由于这是一个尚未修复的漏洞，涉及“信任边界违规”，安全专家建议格外谨慎。  
  
  
避免在包含敏感数据或安全关键型工作流程的系统上使用 MCP 连接器。  
  
  
在添加安全措施之前，来自无害来源（例如日历）的数据可能会被用来触发危险的本地命令。  
  
  
正如 LayerX 所总结的那样，一个简单的日历事件绝不应该危及整个端点，但在当前的架构下，这种情况却有可能发生。  
  
  
技术报告：  
  
https://layerxsecurity.com/blog/claude-desktop-extensions-rce/  
  
  
新闻链接：  
  
https://gbhackers.com/0-click-rce-found-in-claude-desktop-extensions/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
