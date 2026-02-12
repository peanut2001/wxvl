#  【安全圈】Apple 紧急修复在野零日漏洞：dyld 组件被用于“高度复杂”定向攻击  
 安全圈   2026-02-12 11:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
安全漏洞  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGSNjgjqcLEZw0Ax7EGFdVUYHskht3yjmH7TPLpyTQo6HxqiaZheoTVibPb5BcHNDdTSPR8pgFnzgzvfxTDmvPFWXuSK5IBSNsOw/640?wx_fmt=png&from=appmsg "")  
  
苹果发布 iOS 26.3、iPadOS 26.3 以及 macOS Tahoe 26.3，修复数十个安全漏洞。其中最受关注的是一个已被真实利用的零日漏洞——CVE-2026-20700。苹果确认，该漏洞曾被用于针对特定个人的“高度复杂攻击”。  
  
这是一次典型的高价值漏洞修复，涉及系统底层核心组件。  
  
**零日漏洞直击 dyld，影响 iPhone、iPad 和 Mac**  
  
CVE-2026-20700 影响的是动态链接器 dyld。该组件负责在系统运行时加载和链接可执行代码与系统库，是操作系统最底层、最关键的模块之一。  
  
漏洞源于内存损坏问题。如果攻击者具备内存写入能力，可能借此执行任意代码。由于 dyld 位于系统核心层，一旦成功利用，攻击者有机会绕过安全边界，获得对设备的广泛控制。  
  
该漏洞由 Google 威胁分析团队（TAG）报告。值得注意的是，苹果此前在 2025 年 12 月修复的两个 WebKit 零日漏洞（CVE-2025-14174、CVE-2025-43529）也来自同一调查。苹果暗示，这些漏洞可能属于同一攻击链的一部分。  
  
**不止一个漏洞：本次更新修复范围广泛**  
  
除了零日漏洞，本次更新还修复了大量涉及核心组件的问题，包括：  
- 内核漏洞（可能导致本地权限提升或网络流量拦截）  
  
- CoreServices 竞态条件和路径校验问题（可能获取 root 权限）  
  
- 多个 Sandbox 逃逸漏洞（如 CVE-2026-20628、CVE-2026-20667）  
  
- WebKit 多个内存处理缺陷（可能导致崩溃或拒绝服务）  
  
其中多项漏洞具备“链式利用”价值：攻击者可先通过浏览器或应用触发代码执行，再利用 Sandbox 逃逸和权限提升漏洞，实现完整控制。  
  
这类组合攻击近年来已成为高端间谍软件和定向攻击的常见模式。  
  
**隐私相关漏洞同样值得关注**  
  
本次更新还修复了多项涉及隐私的数据访问问题，包括 Spotlight、StoreKit、Siri、Photos、UIKit 以及辅助功能模块中的缺陷。  
  
部分问题甚至可能在设备锁定状态下，通过授权或界面状态管理缺陷泄露敏感信息。这类漏洞虽然未必被大规模利用，但对高价值目标同样具有吸引力。  
  
**苹果未披露攻击细节，建议立即更新**  
  
按照一贯做法，苹果未公布 CVE-2026-20700 的技术细节，以防在用户完成更新前被进一步武器化。  
  
但从官方用词“extremely sophisticated attack”来看，这并非普通漏洞利用，而是具备较强资源与能力背景的定向行动。  
  
对于用户来说，处理方式很明确：立即更新。  
  
iPhone / iPad：设置 → 通用 → 软件更新  
Mac：系统设置 → 通用 → 软件更新  
  
在当前移动终端成为高价值情报载体的背景下，零日漏洞往往只针对少数目标，但补丁缺失却会扩大攻击面。系统更新不仅是功能升级，更是风险止损。  
  
这次修复再次提醒我们——底层组件漏洞一旦被利用，其影响远超浏览器或应用层问题。对安全而言，及时更新依然是最有效的防线。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】CVE-2026-1868：GitLab AI Gateway 严重漏洞（CVSS 9.9），可致远程代码执行](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=1&sn=72e574f6313d73bd75cec9f20e036c27&scene=21#wechat_redirect)  
  
  
  
[【安全圈】假 AI 助手暗藏木马：恶意“ClawdBot”插件潜伏 VS Code](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=2&sn=35bf2ad947c8809281fbfe2d1b3ccd9a&scene=21#wechat_redirect)  
  
  
  
[【安全圈】印度最高法院裁定：WhatsApp 不得以数据共享侵蚀用户隐私](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=3&sn=ebfc6c6db3752b75c2267fac40b20c6d&scene=21#wechat_redirect)  
  
  
  
[【安全圈】法国全面弃用 Zoom 和 Teams：主权视频平台“Visio”落地，数字主权进入实战阶段](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=4&sn=d1170311a7623b6060a3294af3b28da2&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
