#  OpenClaw安全事件全解析：从RCE漏洞到供应链投毒，AI智能体为何频爆安全问题？  
天唯科技
                    天唯科技  天唯信息安全   2026-03-09 09:25  
  
****  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNbU68NXCNH8sw9R1wBYiaT6icvH7moZbnkDB7UPWcP57YnEr5sDNDh6pssbCmuxvzQERZeMhN6Dknw/640?wx_fmt=png "")  
  
  
****  
来源：本文综合自新浪财经、腾讯新闻、网易新闻、安全客等权威媒体公开报道  
## 一夜爆红的"龙虾"，为何沦为安全重灾区？  
  
2026年的开年，AI智能体领域出现了一个令人瞩目的"爆款"——OpenClaw。这款开源AI智能体工具因其强大的自动化能力和灵活的定制化特性，迅速在开发者群体中走红，被超过10万开发者信任和使用。然而，伴随着热度而来的，是一系列触目惊心的安全事件。  
  
从2025年12月至2026年2月，OpenClaw生态系统遭遇了全方位、多维度的安全挑战。远程代码执行漏洞、供应链投毒、大规模数据泄露、公网暴露等问题相继爆发，引发了全球网络安全界的密切关注。工信部网络安全威胁和漏洞信息共享平台更是专门发布预警，直指OpenClaw存在的系统性安全风险。一时间，这款曾经被寄予厚望的AI智能体工具，沦为了网络安全领域的"过街老鼠"。  
  
本文将带您深入了解OpenClaw近期遭遇的系列安全事件，剖析其背后的技术根源，并探讨AI智能体领域面临的安全挑战。  
## 一、CVE-2026-25253：一键远程代码执行漏洞  
### 1.1 漏洞概述  
  
2026年2月，深度安全研究团队depthfirst General Security Intelligence发现，OpenClaw存在一个高危漏洞，该漏洞已被武器化为可“一键触发”的远程代码执行攻击。攻击者仅需通过一个恶意链接即可完全控制受害者系统，无需任何用户交互。  
  
这一漏洞的发现震惊了整个安全社区。CVSS评分高达9.8+，属于极度危险的安全漏洞。OpenClaw架构赋予AI Agent“上帝模式”权限，可访问消息应用、API密钥并无限制控制本地计算机。在这种高权限环境中，安全容错空间极其有限，一旦被攻破，后果不堪设想。  
### 1.2 漏洞技术原理  
  
该漏洞的根源在于OpenClaw架构中的三个组件存在串联缺陷：  
  
**不安全URL参数处理：**  
app-settings.ts模块未经验证直接接收URL中的gatewayUrl参数，并将其存入localStorage。这意味着攻击者可以通过精心构造的恶意链接，将受害者的网关地址指向攻击者控制的服务器。  
  
**跨站WebSocket劫持：**  
app-lifecycle.ts立即触发connectGateway()，将敏感的authToken自动打包发送至攻击者控制的网关服务器。攻击者利用WebSocket源验证缺失的漏洞，通过受害者浏览器建立本地连接，从而窃取令牌。  
  
**自动连接机制：**  
系统在设置网关后立即触发连接行为，且在连接过程中自动传输认证令牌，完全绕过了用户的安全感知。  
### 1.3 攻击链详解  
  
整个攻击过程可以分为六个阶段，每一个环节都充分利用了OpenClaw的安全缺陷：  
  
**第一阶段：访问。**  
用户访问攻击者控制的恶意网站。  
  
**第二阶段：加载。**  
页面中的JavaScript加载带有恶意gatewayUrl参数的OpenClaw组件。  
  
**第三阶段：泄露。**  
authToken被自动发送给攻击者控制的服务器。  
  
**第四阶段：连接。**  
攻击者通过WebSocket连接到受害者的localhost。  
  
**第五阶段：绕过。**  
安全防护机制被禁用，攻击者获得系统访问权限。  
  
**第六阶段：执行。**  
攻击者可以在受害者主机上运行任意命令。  
  
值得注意的是，整个攻击过程不需要任何用户交互，受害者只需访问一个网页链接即可中招。这种“零点击”的攻击方式极大的降低了攻击门槛，使得普通用户面临严重威胁。  
### 1.4 影响范围与官方回应  
  
OpenClaw开发团队在收到漏洞报告后迅速行动，于2026年1月底发布了紧急修复版本v2026.1.29，主要措施包括：增加网关URL确认弹窗、取消自动连接行为等。官方同时建议v2026.1.24-1之前版本的用户立即升级，并要求管理员轮换认证令牌、审计命令执行日志。  
  
然而，安全研究人员很快发现，尽管官方发布了修复补丁，但全球仍有大量OpenClaw实例运行着存在漏洞的旧版本，为攻击者提供了大量的潜在目标。  
## 二、ClawJacked漏洞：恶意网站可劫持本地AI智能体  
### 2.1 漏洞发现  
  
就在RCE漏洞被披露后不久，安全公司Oasis Security又发现了另一个高严重性安全漏洞——ClawJacked。该漏洞存在于OpenClaw的核心系统本身，不涉及插件、应用商店或用户安装的扩展程序，即使是严格按照官方文档部署的OpenClaw网关同样存在风险。  
  
Oasis Security在其报告中指出：“我们发现的漏洞存在于核心系统本身——不涉及插件、应用商店或用户安装的扩展程序——仅仅是按文档运行的OpenClaw网关。”  
### 2.2 攻击过程分析  
  
ClawJacked漏洞的攻击过程令人防不胜防。其威胁模型假设开发人员在其笔记本电脑上设置并运行OpenClaw，网关是一个本地WebSocket服务器，绑定到localhost并受密码保护。当开发人员通过社会工程或其他方式访问攻击者控制的网站时，攻击就会启动。  
  
**第一步：建立连接。**  
网页上的恶意JavaScript在OpenClaw网关端口上打开到localhost的WebSocket连接。与常规HTTP请求不同，浏览器不会阻止这些跨源连接，用户访问的任何网站都可以打开到其本地OpenClaw网关的连接。  
  
**第二步：暴力破解。**  
脚本利用缺失的速率限制机制，以每秒数百次的频率暴力破解网关密码。由于没有输入次数限制，攻击者可以在短时间内尝试大量密码组合。  
  
**第三步：静默注册。**  
在获得管理员级别权限的身份验证后，脚本悄悄注册为受信任设备。网关会自动批准新设备注册而无需用户提示，这是专为本地连接设计的“便利”功能。  
  
**第四步：完全控制。**  
攻击者获得对AI智能体的完全控制权，可以与其交互、转储配置数据、枚举连接的节点并读取应用程序日志。  
### 2.3 本地连接的“双刃剑”特性  
  
ClawJacked漏洞之所以如此危险，关键在于OpenClaw为本地连接放宽了多种安全机制。通常情况下，当新设备连接时，用户必须确认配对。但从localhost连接时，这一确认机制被跳过了，系统自动批准新设备。  
  
Oasis Security安全专家对此评论道：“您访问的任何网站都可以打开到您localhost的连接。与常规HTTP请求不同，浏览器不会阻止这些跨源连接。因此，当您浏览任何网站时，该页面上运行的JavaScript可以静默地打开到您本地OpenClaw网关的连接，用户看不到任何提示。”  
### 2.4 官方修复与建议  
  
在收到Oasis Security的漏洞报告后，OpenClaw团队在不到24小时内推送了修复程序，于2026年2月26日发布了版本2026.2.25。官方同时建议用户尽快应用最新更新，并对授予AI智能体的访问权限进行定期审核。  
  
此外，安全专家还建议：在完全隔离的环境中部署OpenClaw（如专用虚拟机），使用专用的非特权凭据运行，并对非人类（智能体）身份实施适当的治理控制。  
## 三、ClawHub供应链投毒：恶意插件大规模入侵  
### 3.1 事件概述  
  
如果说RCE漏洞和ClawJacked漏洞是OpenClaw自身代码的安全问题，那么ClawHub供应链投毒事件则暴露了OpenClaw生态系统的深层安全隐患。  
  
2026年2月9日，慢雾安全团队披露了OpenClaw插件中心ClawHub供应链投毒事件。平台审核机制不足，导致大量恶意skill（插件）混入，用于传播恶意代码或有害内容。这一事件将OpenClaw的安全问题从技术层面延伸到了供应链层面，引发了对整个AI智能体生态安全性的深度担忧。  
### 3.2 攻击规模与特征  
  
根据Koi Security的扫描数据，此次供应链投毒事件的规模令人震惊：  
<table><thead><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: none;"><th style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);background-image: initial;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;background-color: rgb(245, 245, 247) !important;max-width: 100%;box-sizing: border-box !important;text-align: left;font-weight: 600;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">指标</span></section></th><th style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);background-image: initial;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;background-color: rgb(245, 245, 247) !important;max-width: 100%;box-sizing: border-box !important;text-align: left;font-weight: 600;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">数值</span></section></th></tr></thead><tbody><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: none;"><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">总扫描skill数量</span></section></td><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">2857个</span></section></td></tr><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: none;"><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">识别恶意skill数量</span></section></td><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">341个</span></section></td></tr><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: none;"><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">占比</span></section></td><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">约12%</span></section></td></tr><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: none;"><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">慢雾分析样本IOC</span></section></td><td style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 12px 16px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(224, 224, 224);max-width: 100%;box-sizing: border-box !important;color: rgb(29, 29, 31) !important;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">400+个</span></section></td></tr></tbody></table>  
攻击者呈现明显的团伙化、批量化特征，其IOC（妥协指标）指向少量固定域名和IP地址。攻击手法采用常见的两段式加载：第一阶段进行代码混淆，以躲避安全检测；第二阶段动态拉取payload，实现持续控制和数据窃取。  
### 3.3 典型攻击样本  
  
安全研究人员分析了大量恶意skill，发现了多种典型的攻击模式。其中最具代表性的是"X（Twitter）Trends"skill：  
  
该插件表面上是一个帮助用户追踪Twitter趋势的合法工具，但实际上隐藏了Base64编码的后门程序。用户安装并使用该插件后，恶意代码会悄悄下载并执行程序，用于钓取用户密码，收集敏感文件并上传至攻击者的命令控制（C2）服务器。  
  
此外，安全审计还发现，有单个恶意开发者（用户"hightower6eu"）关联了高达314个恶意技能，这些技能诱导用户从外部平台下载并执行加密脚本，从而植入信息窃取木马如Atomic Stealer。这些木马会系统性盗取浏览器密码、API密钥、加密货币钱包私钥等核心资产。  
### 3.4 明文凭证存储风险  
  
供应链投毒事件的另一个严重后果是凭证泄露。Snyk扫描显示，OpenClaw的ClawHub上有近4000个注册技能，其中7.1%（约283个）存在明文凭证存储缺陷。这些技能在SKILL.md文件中直接嵌入API密钥、密码甚至信用卡号，导致敏感信息经LLM上下文窗口以明文形式流转和日志留存。  
  
受影响的技能包括moltyverse-email、youtube-data及buy-anything等高使用率技能，这意味着大量用户的凭证可能已经暴露在风险之中。  
## 四、大规模公网暴露：13.5万台设备“开门揖盗”  
### 4.1 触目惊心的数字  
  
2026年2月，SecurityScorecard的STRIKE威胁情报团队对其发现的大量互联网暴露OpenClaw实例数量发出警报。截至当时，这个数字已超过135,000个。更令人担忧的是，在安全报告发布后的几小时内，实时监测仪表板上识别出的脆弱系统数量急剧上升。  
  
STRIKE团队在报告中写道：“我们的发现揭示了由大规模安全性差的自动化造成的巨大访问和身份问题。便利驱动的部署、默认设置和薄弱的访问控制已经将强大的智能体变成了攻击者的高价值目标。”  
### 4.2 公网暴露的技术原因  
  
OpenClaw官方默认监听127.0.0.1（本地回环地址），但用户为实现远程访问，常手动修改为0.0.0.0（监听所有网络接口）。若未同步启用强身份验证机制，核心端口18789即成为无防护入口。  
  
奇安信鹰图平台测绘显示，中国境内已有2990台设备对外公开暴露该接口，攻击者可不经漏洞利用直接接管系统。这意味着攻击者无需利用任何复杂的技术漏洞，仅需尝试连接这些暴露的端口，即可获取系统控制权。  
### 4.3 RCE漏洞的广泛影响  
  
STRIKE团队还发现，有12,812个OpenClaw实例容易受到已建立且已修补的远程代码执行漏洞的攻击。截至报告撰写时，易受RCE攻击的实例数量已跳升至50,000多个。  
  
这些暴露在公网的OpenClaw实例一旦被攻破，攻击者可以获取对智能体可以访问的一切的访问权限，无论是凭证存储、文件系统、消息传递平台、网络浏览器，还是其收集的关于用户的各种数据。  
### 4.4 “配置习惯”成最大隐患  
  
安全研究人员指出，此次大规模泄露事件的核心原因并非OpenClaw存在什么安全漏洞，而是很多开发者在部署时为了省事，把服务扔到了公网又忘了设密码。这是典型的“配置习惯”问题，而非工具本身的质量问题。  
  
然而，这种配置习惯与OpenClaw的高权限特性相结合，构成了极其严重的安全风险。攻击者甚至发现，部分OpenClaw服务器的凭证已经暴露，有的被安全公司标记成了“APT目标”（国家级黑客攻击目标），这意味着可能已经有国家级攻击者介入了这一领域。  
## 五、工信部预警：系统性的安全风险  
### 5.1 官方预警发布  
  
2026年3月，工业和信息化部网络安全威胁和漏洞信息共享平台监测发现，OpenClaw开源AI智能体部分实例在默认或不当配置情况下存在较高安全风险，容易引发网络攻击和信息泄露等安全问题。  
  
工信部在预警中指出，OpenClaw（俗称“龙虾”）是一款开源AI智能体，通过整合多渠道通信能力和大语言模型，构建具备持久记忆和主动执行能力的定制化AI助手，可在本地私有化部署。由于OpenClaw在部署时“信任边界模糊”，并且具备持续运行、自主决策和调用系统及外部资源等特性，在缺乏有效权限控制、审计机制和安全加固的情况下，可能因指令诱导、配置缺陷或被恶意接管而执行越权操作，导致信息泄露和系统受控等一系列安全风险。  
### 5.2 安全专家的警示  
  
网络安全专家对OpenClaw的安全问题表达了深度担忧。有安全专家戏称OpenClaw的权限模型为“安全噩梦”，因为它默认获取系统级高权限，包括文件读写、程序执行和网络访问三大系统级权限，这相当于赋予了AI代理一把电脑的“万能钥匙”。  
  
这种高权限设计虽然让AI能自动化处理复杂任务，比如整理文件或操控浏览器，但也意味着一旦被恶意利用，攻击者可以轻松窃取敏感数据、执行危险命令，甚至完全控制系统。  
### 5.3 央视新闻等权威媒体关注  
  
OpenClaw的安全问题不仅引发了安全圈的担忧，也引起了主流媒体的广泛关注。央视新闻、每日经济新闻等权威媒体相继报道了OpenClaw存在的安全漏洞和风险，向公众发出了警示。  
  
据《每日经济新闻》报道，澳大利亚网络安全公司Dvuln证明了这种风险的存在，该公司发现OpenClaw存在漏洞，攻击者可借此获取用户数月内的私人消息、账户凭证、API密钥等敏感信息。甚至有网络安全专家遭遇了OpenClaw无视其指令、疯狂删除邮箱的离奇事件。  
## 六、OpenClaw安全问题的深层反思  
### 6.1 AI智能体的“双刃剑”困境  
  
OpenClaw安全事件的频发，折射出AI智能体领域面临的普遍困境。一方面，AI智能体需要高权限来执行复杂任务；另一方面，高权限也意味着高风险。一旦AI智能体被攻破或被恶意利用，其后果远比传统软件严重得多。  
  
OpenClaw的定位是“做事”型AI，需要高权限操控本地文件和应用。这种设计理念虽然赋予了AI强大的能力，但也使其成为了攻击者眼中的“高价值目标”。正如安全研究人员所言：“便利驱动的部署、默认设置和薄弱的访问控制已经将强大的智能体变成了攻击者的高价值目标。”  
### 6.2 供应链安全的警钟  
  
ClawHub供应链投毒事件为整个AI智能体行业敲响了供应链安全的警钟。在AI智能体生态中，插件市场、Skill市场扮演着至关重要的角色，但审核机制的缺失使得恶意内容有了可乘之机。  
  
慢雾安全团队的披露显示，攻击者已经形成了团伙化、规模化的攻击模式，利用两段式加载、代码混淆等技术手段躲避安全检测。这提醒我们，在享受AI智能体带来便利的同时，必须高度重视供应链安全。  
### 6.3 配置安全不容忽视  
  
13.5万台OpenClaw实例公网暴露的惊人事实，揭示了配置安全这一常被忽视的问题。很多开发者在追求便利的同时，忽视了安全配置的重要性，将高权限的AI智能体服务暴露在公网，却忘记启用身份认证。  
  
这种配置习惯问题并非OpenClaw独有，而是整个AI智能体领域的通病。安全专家建议，相关单位和用户在部署和应用AI智能体时，应充分核查公网暴露情况、权限配置及凭证管理情况，关闭不必要的公网访问，完善身份认证、访问控制、数据加密和安全审计等安全机制。  
## 七、安全使用建议  
### 7.1 立即采取的防护措施  
  
面对OpenClaw频发的安全问题，用户应立即采取以下防护措施：  
  
**版本升级：**  
立即升级OpenClaw到v2026.2.25或更高版本，确保已知漏洞已被修补。官方已在多个版本中修复了60多个安全漏洞，包括高危的远程代码执行问题。  
  
**网络隔离：**  
绝不将服务端口暴露在公网，网关应绑定到127.0.0.1（本地回环地址），绝不要改为0.0.0.0。如需远程访问，应使用SSH隧道或Tailscale等安全方式。  
  
**身份认证：**  
从v2026.1.29开始，OpenClaw已永久移除无认证模式，务必配置并启用token或password强认证，防止未授权访问。  
  
**凭证管理：**  
如果曾安装过来历不明的技能，应视为凭证可能已泄露，立即重置所有API密钥、云平台令牌、SSH密钥等敏感凭证，并开启重要账号的双因素认证（2FA）。  
### 7.2 技能安装注意事项  
  
在安装OpenClaw技能时，用户应遵循以下原则：  
  
**来源审核：**  
仅从官方渠道安装技能，查看ClawHub集成的VirusTotal扫描结果。平台会对新技能进行哈希比对和代码深度分析，结果分为良性、可疑或恶意，应仅安装标记为“良性”的技能。  
  
**代码审查：**  
精读技能说明书（SKILL.md），如果出现curl|bash下载外部脚本、要求全盘文件访问等高风险步骤，应直接判定为恶意并拒绝安装。  
  
**沙箱隔离：**  
在配置中启用沙箱隔离（设置skills.sandbox: true），将技能运行限制在专属目录，阻止越权操作。  
### 7.3 长期安全策略  
  
除了立即采取的防护措施，用户还应建立长期的安全策略：  
  
**持续监控：**  
持续关注官方安全公告和加固建议，及时了解新发现的安全漏洞和修复方案。  
  
**最小权限：**  
遵循最小权限原则，例如在云平台创建API密钥时仅授予必要权限。  
  
**定期审计：**  
定期审计命令执行日志，检查是否有异常行为；定期检查系统配置，确保安全设置未被更改。  
## 结语  
  
OpenClaw安全事件的频发，为整个AI智能体行业敲响了警钟。从技术漏洞到供应链攻击，从配置失误到权限滥用，AI智能体面临的安全挑战是多维度、系统性的。  
  
然而，我们不应因噎废食。AI智能体作为提升生产力的重要工具，其价值不应被否定。关键在于，我们需要在便利性与安全性之间找到平衡，在追求功能强大的同时不忘安全加固。  
  
对于AI智能体开发者而言，OpenClaw的教训提醒他们：安全设计应从一开始就被纳入架构之中，而非事后修补。对于用户而言，选择使用AI智能体意味着承担相应的安全责任，需要投入足够的精力进行安全配置和持续监控。  
  
工信部的预警、主流媒体的关注、安全研究人员的披露，都在推动AI智能体领域向更安全的方向发展。我们期待在未来看到更加安全、可靠的AI智能体产品，为用户提供便利的同时，真正守护好数据和系统的安全。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNbU68NXCNH8sw9R1wBYiaT6icvH7moZbnkDB7UPWcP57YnEr5sDNDh6pssbCmuxvzQERZeMhN6Dknw/640?wx_fmt=png "")  
  
  
  天唯科技专注于中大型组织 IT 基础设施、信息安全、数据资产、AI 大模型及应用解决方案的规划、建设与持续运维服务。通过深度融合前沿技术与行业实践，帮助客户构建全方位的IT基础设施及信息安全防护体系，显著提升安全管控水平与安全运营能力；同时，依托AI技术与数据资产的高效利用，赋能企业突破数字化转型瓶颈，强化业务创新与智能决策能力，助力客户在激烈的市场竞争中保持领先优势，实现可持续的高质量发展。  
  
  我们一直秉承“精兵强将，专业专注”的发展理念。先后在江门、深圳、香港成立分公司，在武汉、长沙成立办事处以及成立广州的服务支撑中心。公司已获得高新技术企业认证、已通过IS09001、IS027001、CCRC信息安全集成服务、CCRC信息安全风险评估、CCRC信息安全应急处理等认证。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNRytkPMNOKYRW452LxR5Ez5Wee8X6KlbhoUMt9XyhhbRxHafKcCLWJic3ib0umJiaH3fl6sOx8KMBiaQ/640?wx_fmt=png "盾牌单图.png")  
  
**END**  
  
****  
  
  
  
