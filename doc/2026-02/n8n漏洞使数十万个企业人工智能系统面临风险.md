#  n8n漏洞使数十万个企业人工智能系统面临风险  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-06 01:15  
  
**导****读**  
  
  
  
n8n 平台的一个缺陷允许任何经过身份验证的用户完全控制底层服务器，从而暴露企业环境中的凭据、密钥和 AI 驱动的工作流程。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyKMZjCzicOf3SDOykicjCicrgrKR0vxlUdDiaj1qDcViaFdt26ibxPOSiaGhvCgBTiccia6YQqUDy8WYOdV2AtYXqib5A4jLZpEGoxCotMUw/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞的CVSS 评分为 10.0，允许攻击者突破 n8n 的 JavaScript 沙箱执行任意命令，从而有效地将常规工作流程逻辑转换为对系统的完全控制。  
  
  
“这些平台在不知不觉中成为了核心资产。每一个敏感的工作流程、每一个人工智能提示、每一份凭证——它们都通过编排层进行处理。”Pillar 的研究人员在给 eSecurityPlanet 的电子邮件中写道。  
  
  
他们补充道：“真正的风险不在于任何单一系统，而在于连接这些系统的环节。展望未来，人工智能代理很快就能自主构建和修改这些工作流程。一个代理破坏另一个代理的编排层——这才是我们现在应该着手设计防御措施的攻击链，而不是等到攻击发生之后才去应对。”  
  
  
n8n 被广泛用于自动化核心业务流程，并日益成为企业中 AI 驱动工作流的编排层。 各组织依靠它将内部系统、云服务和大型语言模型连接成端到端的自动化管道。  
  
  
因此，一次严重安全漏洞不仅会影响一个集成或工作流程，还可能暴露云凭证、数据库和人工智能管道，这些管道通常会处理敏感的业务和客户数据。  
  
  
风险既存在于自托管的 n8n 部署中，也存在于 n8n 云中。  
  
  
在云环境中，n8n 的共享多租户架构显著增加了潜在的爆炸半径，使得单个受损租户有可能威胁到相邻的服务或数据。  
   
  
  
问题的核心在于 n8n 的表达式引擎，它允许用户使用={{ }}语法将 JavaScript 直接嵌入到工作流中。  
  
  
这一特性是该平台灵活性的主要原因，它能够实现动态数据转换和高级人工智能编排。 然而，这也意味着用户提供的 JavaScript 代码会在服务器端进行执行。  
  
  
为了降低固有风险，n8n 依赖于基于抽象语法树 (AST) 的沙箱，旨在防止访问危险的 JavaScript 对象和运行时原语。  
  
  
Pillar 安全研究人员发现，这个沙箱可以被完全绕过。  
  
  
任何经过身份验证的用户，只要能够创建或编辑工作流（即使没有管理权限），都可以逃出沙箱，并在 n8n 服务器上实现远程代码执行 (RCE)。  
  
  
一旦利用成功，攻击者就可以读取环境变量、访问文件系统并提取N8N_ENCRYPTION_KEY。  
  
  
有了这个密钥，他们就可以解密所有存储的凭证，包括云提供商访问密钥、OAuth 令牌、数据库密码以及 OpenAI 和 Anthropic 等 AI 服务的 API 凭证。  
  
  
最初的漏洞链，被追踪为CVE-2026-25049，源于 n8n 的 AST 清理逻辑中的漏洞。  
  
  
研究人员结合了多种 JavaScript 行为——模板字面量属性访问、V8 Error.prepareStackTrace钩子和箭头函数作用域——来访问沙箱之外的真正全局对象。  
  
  
尽管 n8n 在 2025 年 12 月发布了补丁，但研究人员在 24 小时内就发现了使用Object.defineProperty() 的绕过方法。  
  
  
该清理器过于关注属性访问语法，而忽略了可以在不直接访问成员的情况下修改对象属性的 JavaScript API。  
  
  
这两种情况下，结果都是一样的：从看似正常的流程表达式内部执行完整的远程代码。  
  
  
最终在 2.4.0 版本中发布了全面的修复程序，该程序解决了更广泛的 AST 分析缺陷，而不是针对个别的绕过技术。  
  
  
详细漏洞分析：  
  
《n8n沙箱逃逸：n8n的关键漏洞使数十万个企业人工智能系统面临被接管的风险》  
  
https://www.pillar.security/blog/n8n-sandbox-escape-critical-vulnerabilities-in-n8n-exposes-hundreds-of-thousands-of-enterprise-ai-systems-to-complete-takeover  
  
  
新闻链接：  
  
https://www.esecurityplanet.com/threats/n8n-flaw-puts-hundreds-of-thousands-of-enterprise-ai-systems-at-risk/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
