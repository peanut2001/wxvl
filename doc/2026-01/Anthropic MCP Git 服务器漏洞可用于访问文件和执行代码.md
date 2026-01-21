#  Anthropic MCP Git 服务器漏洞可用于访问文件和执行代码  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-01-21 10:15  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**由 Anthropic 维护的 Git 官方模型上下文协议 (MCP) 服务器中存在三个漏洞，可在一定条件下用于读取或删除任意文件并执行代码。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRdfn8fpKvARTmwBYt7ZAN5DfxeonibgywIJP9UxCvJBwUHOKgER3gBlIJWNY2d3x8dby5PsqmyDDQ/640?wx_fmt=gif&from=appmsg "")  
  
  
生成式AI安全公司Cyata 的研究员 Yarden Porat 提到，“这些漏洞可通过提示注入遭利用，也就是说攻击者如能影响一款AI助手读取（恶意README、投毒的 issue 描述、受陷网页），无需直接访问受害者系统，就能利用这些漏洞。”  
  
Mcp-server-git 是一个 Python 包和一款 MCP 服务器，提供一系列内置工具，通过大语言模型以编程的方式来读取、搜索和操纵 Git 仓库。在2025年6月负责任地披露后，这些漏洞已在 2025.9.25和2025.12.18中修复，具体如下：  
  
- CVE-2025-68143：CVSS 评分8.8（v3）/6.5 (v4)，是一个路径遍历漏洞，因 git_init 工具在仓库创建的过程中未经过验证即接受任意文件系统路径导致（已在 2025.9.25版本中修复）。  
  
- CVE-2025-68144：CVSS 评分8.1（v3）/6.4 (v4)，是一个参数注入漏洞，因 git_diff和git_checkout 函数在未经清理的情况下，直接将受用户控制的参数传给 git CLI 命令导致（已在2025.12.18版本中修复）。  
  
- CVE-2025-68145：CVSS 评分7.1（v3）/6.3 (v4)，是一个路径遍历漏洞，因在使用 –repository 标记将操作限制到一个特定的仓库路径时未验证路径而导致（已在2025.12.18版本中修复）。  
  
  
  
成功利用上述漏洞可导致攻击者将系统上的任意目录转换为 Git 仓库，以空差异覆写任意文件并访问服务器上的任意仓库。  
  
Cyata 公司观察到的一起攻击活动表明，这三个漏洞可与 Filysystem MCP 服务器组合利用，写入 “.git/config” 文件（一般位于隐藏的 .git 目录中）并通过提示注入的方式触发对 git_init 的调用，实现远程代码执行后果：  
  
- 使用 git_init 在可写目录中创建仓库。  
  
- 通过文件系统 MCP 服务器写入包含恶意 clean 过滤器的 .git/config 文件。  
  
- 创建 .gitattributes 文件使过滤器对特定文件生效。  
  
- 写入包含攻击载荷的 shell 脚本。  
  
- 创建触发过滤器的目标文件。  
  
- 调用 git_add 命令激活 clean 过滤器，从而执行攻击载荷。  
  
  
  
Git_init 工具已从该程序包中删除并增加了额外的验证机制，阻止路径遍历原语。建议该 Python 包用户升级至最新版本获得最优防护措施。Cyata 公司的首席执行官兼联合创始人 Shahar Tal 提到，“这是规范的 Git MCP 服务器，是开发人员会参照的标准模板。如果即使在参考实现中安全边界也会被突破，那么意味着需要对整个 MCP 生态系统进行更深入的审计。这并非极端案例或者特殊配置，它们开箱即用。”  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[MCP服务器平台严重漏洞可暴露3000+服务器和数千API密钥](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524251&idx=1&sn=0581723e878fb683f7b1df7fc9c7bda6&scene=21#wechat_redirect)  
  
  
[开源项目mcp-remote 中存在严重漏洞可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523555&idx=2&sn=04a84283c9d2100a95736c652525dcd8&scene=21#wechat_redirect)  
  
  
[React Router严重漏洞可用于访问或修改服务器文件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524857&idx=2&sn=8c1f832d3fbc13cae125177e8f0247af&scene=21#wechat_redirect)  
  
  
[n8n严重漏洞可导致任意代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524734&idx=1&sn=7accfa41ad8e25a3c0a292eb451552af&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html  
  
  
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
  
