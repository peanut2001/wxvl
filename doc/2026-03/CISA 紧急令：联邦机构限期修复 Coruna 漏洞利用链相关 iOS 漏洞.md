#  CISA 紧急令：联邦机构限期修复 Coruna 漏洞利用链相关 iOS 漏洞  
ZM
                    ZM  暗镜   2026-03-06 23:56  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb0qyibHgpUZ1m1a5N60F6oJ1Bq5nL0vWgicjicpWvm6nB3NBLvQhv6xkCjmMvmZ9GZ7cicHCKKqbz3ku720JKVrf2JIYtGMwz5qBVU/640?wx_fmt=jpeg "")  
  
继 iVerify 与 Google Threat Intelligence Group 披露 Coruna iOS 漏洞利用框架泄露事件后，美国网络安全和基础设施安全局 (CISA) 于本周四发布紧急指令，要求联邦民事行政部门 (FCEB) 机构在 2026 年 3 月 26 日前修复三个与 Coruna 相关的 iOS 安全漏洞。这是 CISA 首次针对移动操作系统漏洞发布具有约束力的修复指令。  
### 指令内容与适用范围  
  
CISA 将 Coruna 框架 23 个漏洞中的 3 个列入已知利用漏洞 (KEV) 目录，并依据约束性操作指令 (BOD) 22-01 要求联邦机构：  
- **修复期限**  
：2026 年 3 月 26 日前完成漏洞修复  
  
- **处置选项**  
：按供应商说明实施缓解措施、遵循云服务相关 BOD 22-01 指南，或如无法缓解则停止使用该产品  
  
- **风险定级**  
：CISA 明确指出"这类漏洞是恶意网络攻击者常用的攻击途径，对联邦政府构成重大风险"  
  
虽然 BOD 22-01 仅适用于联邦机构，CISA 强烈敦促所有组织——包括私营企业——优先修补这些漏洞。  
### 漏洞技术细节  
  
据 Google Threat Intelligence Group (GTIG) 披露，Coruna 框架通过多个漏洞利用链整合 23 个 iOS 漏洞，其中多个漏洞已在零日攻击中部署。该框架为攻击者提供以下核心能力：  
- **指针认证码 (PAC) 绕过**  
：突破 iOS 内存保护机制  
  
- **沙箱逃逸**  
：从应用沙箱突破至系统级访问  
  
- **PPL（页面保护层）绕过**  
：绕过内核级内存保护  
  
- **权限提升路径**  
：从 WebKit 远程代码执行权限提升至内核权限  
  
GTIG 观察到，去年已有三类不同背景的威胁行为者使用该工具包：  
<table><thead><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><th align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">威胁行为者</span></section></th><th align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">归属背景</span></section></th><th align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">攻击场景</span></section></th></tr></thead><tbody><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">监控供应商客户</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">政府情报机构</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">定向监控活动</span></section></td></tr><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">UNC6353</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">疑似俄罗斯国家支持</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">针对乌克兰用户的地理定向攻击</span></section></td></tr><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">UNC6691</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">经济利益驱动的中国攻击者</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">虚假赌博/加密货币网站，窃取钱包</span></section></td></tr></tbody></table>### 防护有效性验证  
  
GTIG 研究确认，现有防护机制对 Coruna 具有明确阻断效果：  
  
**系统版本防护**  
：Coruna 的漏洞利用方法在最新版本 iOS 上无法生效。Apple 已在 iOS 26 版本中通过安全更新使该框架完全失效。  
  
**功能模式防护**  
：  
- **隐私浏览模式**  
：可阻止漏洞利用链的初始执行  
  
- **锁定模式 (Lockdown Mode)**  
：Apple 的反间谍软件保护功能能有效拦截攻击  
  
这两项发现为高风险用户（政府官员、记者、企业高管等）提供了即时可用的缓解方案，无需等待系统更新。  
### 漏洞利用链的扩散风险  
  
CISA 此次指令的背景是 Coruna 框架已从受控的政府监控工具演变为大规模攻击武器。UNC6691 的攻击活动尤其值得关注——该组织将漏洞部署于虚假加密货币交易平台，通过"建议用户使用 iOS 设备访问"的诱导手段，无差别攻击普通用户，估计已有约 4.2 万台设备遭入侵。  
  
这种从"定向监控"到"大规模犯罪"的工具转化，标志着移动威胁态势的根本性转变。CISA 的紧急响应表明，联邦政府已认识到此类泄露事件对国家级通信安全的系统性威胁。  
### 应对建议  
- 立即清点机构内 iOS 设备版本分布  
  
- 优先更新至 iOS 26 或更高版本  
  
- 对无法立即更新的设备，强制启用锁定模式  
  
- 审查近期 Web 访问日志中是否存在 Coruna 相关 IOC（如特定域名 mxbc-v2.tjbjdod.cn  
、aidm8it5hf1jmtj.xyz  
）  
  
**私营企业**  
- 参照 CISA 建议制定内部修复时间表  
  
- 为高风险岗位人员配置启用锁定模式的设备  
  
- 部署移动威胁检测工具（如 iVerify Basic App、MVT）  
  
**个人用户**  
- 更新至最新 iOS 版本  
  
- 如使用加密货币钱包应用，立即启用锁定模式  
  
- 避免访问非官方应用商店推荐的金融类网站  
  
**此次 CISA 指令标志着移动操作系统漏洞首次被纳入联邦强制修复框架，反映出 iOS 平台在关键基础设施通信中的核心地位，以及 Coruna 级别威胁对国家安全构成的实质性风险。**  
  
  
