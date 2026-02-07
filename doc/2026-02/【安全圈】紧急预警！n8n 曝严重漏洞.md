#  【安全圈】紧急预警！n8n 曝严重漏洞  
 安全圈   2026-02-07 07:19  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
n8n漏洞  
  
  
近日，工作流自动化平台 n8n 被披露存在一个严重安全漏洞，攻击者若成功利用该漏洞，可通过构造恶意工作流执行任意系统命令，入侵服务器、窃取敏感数据，风险极高。  
  
**一、漏洞核心信息（据n8n官方公告、安全研究团队披露）**  
  
1.  漏洞编号：**CVE-2026-25049**  
  
2.  风险等级：严重（CVSS 评分：9.4）  
  
3.  漏洞根源：清理机制不足，导致绕过了此前修复 CVE-2025-68613（CVSS 评分：9.9，2025年12月已修复）的安全措施，本质是同一漏洞的绕过型利用。  
  
4.  漏洞原理：TypeScript 编译时类型检查与 JavaScript 运行时行为不匹配，攻击者在运行时构造恶意表达式，传递非字符串值（如对象、数组），可完全绕过清理检查，逃离 n8n 表达式沙箱机制。  
  
5.  发现者：包括报告 CVE-2025-68613 的 Fatih Çelik 在内，共10位安全研究人员（来自 Endor Labs、Pillar Security、SecureLayer7 等机构）因发现该漏洞受到表彰。  
  
**二、漏洞影响范围与攻击手法**  
  
**▌受影响版本**  
（已明确修复版本，速查对照）  
  
- n8n < 1.123.17（已在 1.123.17 版本中修复）  
  
- n8n < 2.5.2（已在 2.5.2 版本中修复）  
  
**▌攻击条件**  
  
已获得认证、且有权创建或修改工作流的用户，即可滥用工作流参数中精心构造的表达式，触发系统命令执行；若结合 n8n 的 webhook 功能，攻击难度大幅降低、影响范围显著扩大。  
  
**▌具体攻击手法**  
  
据 SecureLayer7 披露，攻击者只需创建包含“未启用身份验证的公开可访问 webhook”的工作流，添加一行使用解构语法的 JavaScript 代码，即可滥用该工作流执行系统级命令。  
  
一旦 webhook 暴露，互联网上的任何人都可触发该 webhook，远程运行系统命令——正如 Pillar Security 的 Eilon Cohen 所说：“这种攻击不需要任何特殊技巧，只要你能创建一个工作流，就能控制服务器。”  
  
**三、漏洞危害（严重且直接）**  
  
成功利用该漏洞，攻击者可实现多重恶意操作，危害极大：  
  
1.  入侵服务器，执行任意系统命令，安装持久后门，实现长期控制；  
  
2.  窃取敏感凭据，包括 API 密钥、云提供商密钥、数据库密码、OAuth 令牌等；  
  
3.  访问服务器文件系统和内部系统，泄露核心敏感数据；  
  
4.  攻击连接的云帐户，劫持人工智能（AI）工作流程；  
  
5.  结合 webhook 功能可实现大范围远程攻击，影响更多关联系统。  
  
**四、紧急修复与临时防护方案（必做）**  
  
**▌优先修复方案（最有效，立即执行）**  
  
立即将 n8n 升级至对应修复版本，杜绝漏洞被利用：  
  
- 1.x 版本用户：升级至 1.123.17 及以上版本；  
  
- 2.x 版本用户：升级至 2.5.2 及以上版本；  
  
升级后重启 n8n 服务，确保修复生效。  
  
**▌临时变通方法（无法立即升级时，降低风险）**  
  
1.  严格权限管控：仅允许完全信任的用户创建和编辑工作流，禁用非必要用户的工作流操作权限；  
  
2.  强化部署环境：在操作系统权限、网络访问权限受限的强化环境中部署 n8n，减少漏洞利用后的危害范围；  
  
3.  临时关闭公开 webhook：若无需使用，暂时关闭未启用身份验证的公开 webhook，避免被攻击者利用。  
  
**▌安全启示**  
  
Endor Labs 提醒：该漏洞凸显多层验证的重要性，即使 TypeScript 类型检查看似强大，处理不受信任输入时，仍需添加额外的运行时检查；代码审查中，需重点关注清理函数，排查未在运行时强制执行的输入类型假设。  
  
**五、n8n 同步披露的其他 11 个漏洞（速查，按需修复）**  
  
除 CVE-2026-25049 外，n8n 还同步发布了11个漏洞的安全警报，其中5个为“严重”等级，均已推出修复版本，建议一并检查升级：  
  
1.  CVE-2026-21893（CVSS 9.4，严重）：命令注入漏洞，已在 1.120.3 版本修复；  
  
2.  CVE-2026-25051（CVSS 8.5，高）：跨站脚本（XSS）漏洞，已在 1.123.2 版本修复；  
  
3.  CVE-2026-25052（CVSS 9.4，严重）：TOCTOU 文件访问漏洞，已在 2.5.0、1.123.18 版本修复；  
  
4.  CVE-2026-25053（CVSS 9.4，严重）：Git 节点命令注入漏洞，已在 2.5.0、1.123.10 版本修复；  
  
5.  CVE-2026-25054（CVSS 8.5，高）：存储型 XSS 漏洞，已在 2.2.1、1.123.9 版本修复；  
  
6.  CVE-2026-25055（CVSS 7.1，中高）：路径遍历漏洞，已在 2.4.0、1.123.12 版本修复；  
  
7.  CVE-2026-25056（CVSS 9.4，严重）：合并节点 SQL 漏洞，已在 2.4.0、1.118.0 版本修复；  
  
8.  CVE-2026-25115（CVSS 9.4，严重）：Python 代码节点沙箱突破漏洞，已在 2.4.8 版本修复；  
  
9.  CVE-2026-25631（CVSS 5.3，中）：凭据域验证不当漏洞，已在 1.121.0 版本修复；  
  
10. CVE-2025-61917（CVSS 7.7，中高）：敏感信息泄露漏洞，已在 1.114.3 版本修复；  
  
11. CVE-2025-62726（CVSS 8.8，高）：Git Node 远程代码执行漏洞，已在 1.113.0 版本修复。  
  
**温馨提示**  
：n8n 作为常用工作流自动化平台，其漏洞可能影响大量企业的业务正常运行，建议相关运维人员、技术人员立即核查自身使用的 n8n 版本，优先完成升级修复；非技术人员请及时联系公司运维团队，确认防护措施已落实。  
  
  
   END    
  
  
阅读推荐  
  
  
[【安全圈】阿里30亿红包分发首日，千问App“崩了”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=1&sn=ead70ffd5a7c58f34ac096e34ec29ba1&scene=21#wechat_redirect)  
  
  
  
[【安全圈】微软Azure突发10小时全球宕机！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=2&sn=e9b040f68282d54490efb0d48044e63e&scene=21#wechat_redirect)  
  
  
  
[【安全圈】罗马大学遭网络攻击：欧洲最大规模大学之一，计算机系统瘫痪数日](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=3&sn=a8f0fda81433b96cf1cb3c6bd236587c&scene=21#wechat_redirect)  
  
  
  
[【安全圈】豆瓣又双叒叕崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074026&idx=1&sn=6a635141041422657df1a74a69f50b77&scene=21#wechat_redirect)  
  
  
  
[【安全圈】迅雷下载暗藏猫腻：用户ISO镜像遭替换，捆绑大量推广软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074026&idx=2&sn=5f13d39252450f325b253834a3a767c2&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
