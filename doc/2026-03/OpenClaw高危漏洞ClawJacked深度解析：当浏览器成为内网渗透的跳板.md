#  OpenClaw高危漏洞ClawJacked深度解析：当浏览器成为内网渗透的跳板  
点击关注👉
                    点击关注👉  马哥网络安全   2026-03-03 09:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55PjxpoPFYtgKd65wuUpOVX4uhlurdxiaSDmM0c3SQQTziaHjs8pFm96cNXJLC71y0VyuHkacU2TAEzdwmn1xHt1gDjTUmhAvyRg/640?wx_fmt=png&from=appmsg "")  
  
**导语**  
：一个未配置速率限制的WebSocket端点，一次静默的设备注册，竟能让恶意网站获得你本地AI Agent的完全控制权。这不是科幻，而是OpenClaw曝光的高危漏洞ClawJacked的真实攻击图景。当AI Agent成为企业基础设施的核心组件，它们的安全边界究竟在哪里？  
## 一、漏洞原理：本地信任陷阱的致命漏洞  
  
ClawJacked漏洞的核心在于**本地信任模型的设计缺陷**  
。让我们拆解这个攻击链条：  
### 1.1 WebSocket跨域访问的"灰色地带"  
  
OpenClaw网关默认在本地的TCP端口（如18789）运行WebSocket服务，绑定到localhost  
并设置密码保护。开发者普遍误认为"localhost+密码"的双重保护已足够安全。然而，他们忽略了一个关键事实：**浏览器的同源策略（SOP）并不限制WebSocket连接的目标**  
。  
  
正如安全研究员Oasis Security所指出的："任何你访问的网站都可以向你的localhost建立WebSocket连接。与常规HTTP请求不同，浏览器不会阻止这些跨域连接。"这意味着，当你在浏览器中打开一个看似无害的网页时，页面中嵌入的JavaScript代码可以静默尝试连接你的本地OpenClaw网关。  
### 1.2 暴力破解的温床：缺失的速率限制  
  
ClawJacked的第二个关键缺陷是**本地连接缺乏速率限制机制**  
。通常情况下，远程服务的认证端点会实施严格的速率限制以防止暴力破解攻击。但在ClawJacked场景中，攻击者的恶意脚本可以在短时间内发送大量密码猜测请求，而网关对此毫无防备。  
  
这使得攻击者可以使用字典攻击或穷举法快速尝试常见密码组合，直到成功认证。  
### 1.3 自动设备注册的致命信任  
  
成功认证后，攻击面临的最大障碍通常是设备配对确认——正常情况下，新设备连接时用户需要手动确认。然而，OpenClaw对来自localhost  
的连接给予了**过度信任**  
：  
- 新设备自动注册为受信任设备  
  
- 无需用户提示或确认  
  
- 直接获得管理员级别的权限  
  
Oasis Security的研究揭示了这一设计的危险之处："这种错位的信任带来了真实的后果。网关为本地连接放宽了多项安全机制，包括静默批准新设备注册而不提示用户。"  
## 二、攻击场景：从浏览器到内网的渗透链条  
### 场景一：水坑攻击（Watering Hole）  
  
攻击者可以针对特定开发者群体（如AI工程师）常访问的技术博客、论坛或文档站点植入恶意代码。当受害者在日常工作中访问这些被攻陷的网站时，攻击在后台静默执行：  
1. 恶意JavaScript加载并检测目标是否运行OpenClaw  
  
1. 自动发起WebSocket连接到localhost:18789  
  
1. 启动暴力破解循环尝试常见密码  
  
1. 成功认证后，自动注册为受信任设备  
  
1. 向攻击者的C2服务器报告成功入侵  
  
整个攻击过程用户毫无感知，直到敏感数据泄露或被进一步横向移动。  
### 场景二：供应链攻击的延伸  
  
针对OpenClaw生态的供应链攻击已有先例——Trend Micro近期披露的攻击显示，恶意技能被上传至ClawHub市场，用于传播macOS信息窃取器Atomic Stealer。ClawJacked漏洞可以与这类攻击形成组合拳：  
1. 开发者下载并安装被植入后门的技能  
  
1. 技能代码探测本地OpenClaw配置  
  
1. 一旦发现ClawJacked漏洞存在，立即利用  
  
1. 获得持久化访问通道  
  
### 场景三：APT级别的定向攻击  
  
对于具有高级的持续威胁（APT）组织而言，ClawJacked提供了一个理想的初始访问向量：  
- 通过鱼叉式钓鱼诱导目标访问恶意网站  
  
- 利用ClawJacked获得OpenClaw网关控制  
  
- 通过AI Agent枚举连接的节点和服务  
  
- 将AI Agent转化为内网横向移动的跳板  
  
- 利用Agent的既有权限访问企业敏感数据  
  
## 三、影响范围：远超单个终端的安全风险评估  
### 3.1 受影响版本与修复状态  
  
OpenClaw官方已在**2026.2.25版本**  
中修复此漏洞，响应时间不到24小时。但问题的严峻性在于：  
- 大量开发者可能未及时更新  
  
- 某些生产环境可能因稳定性考虑延迟升级  
  
- 企业内部网关可能由IT部门统一部署，更新周期较长  
  
### 3.2 复合风险的累积效应  
  
ClawJacked并非孤立事件。近期OpenClaw面临的漏洞风暴令人担忧：  
<table><thead><tr><th style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;text-align: center;font-weight: bold;color: rgb(72, 112, 172);background: rgb(247, 247, 247);"><section><span leaf="">漏洞类型</span></section></th><th style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;text-align: center;font-weight: bold;color: rgb(72, 112, 172);background: rgb(247, 247, 247);"><section><span leaf="">CVE编号</span></section></th><th style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;text-align: center;font-weight: bold;color: rgb(72, 112, 172);background: rgb(247, 247, 247);"><section><span leaf="">影响</span></section></th><th style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;text-align: center;font-weight: bold;color: rgb(72, 112, 172);background: rgb(247, 247, 247);"><section><span leaf="">修复版本</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">远程代码执行</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">CVE-2026-25593</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">高</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">2026.1.20</span></section></td></tr><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">命令注入</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">CVE-2026-24763</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">高</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">2026.1.29</span></section></td></tr><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">SSRF</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">CVE-2026-25157</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">中</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">2026.2.1</span></section></td></tr><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">认证绕过</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">CVE-2026-25475</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">高</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">2026.2.2</span></section></td></tr><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">日志投毒</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">GHSA-g27f-9qjv-22pm</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">中</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">2026.2.13</span></section></td></tr><tr><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><strong style="color: rgb(72, 112, 172);"><span leaf="">ClawJacked</span></strong></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><section><span leaf="">待分配</span></section></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><strong style="color: rgb(72, 112, 172);"><span leaf="">高</span></strong></td><td style="border: 1px solid rgb(217, 223, 228);padding: 9px 12px;font-size: 0.75em;line-height: 22px;vertical-align: top;"><strong style="color: rgb(72, 112, 172);"><span leaf="">2026.2.25</span></strong></td></tr></tbody></table>  
这一连串的漏洞暴露了一个根本问题：**AI Agent框架的安全模型与传统软件有本质区别，但安全评估方法未能同步演进**  
。  
### 3.3 企业级影响的多米诺效应  
  
OpenClaw的AI Agent通常被赋予广泛的系统访问权限：  
- 集成Git仓库、CI/CD管道  
  
- 连接企业通讯工具（Slack、Discord、邮件）  
  
- 访问数据库、API端点、云平台  
  
- 执行代码、部署服务、管理基础设施  
  
一旦被攻破，攻击者可以利用Agent的既有权限实现：  
- **数据泄露**  
：窃取源代码、API密钥、客户数据  
  
- **供应链污染**  
：在构建过程中植入后门  
  
- **权限提升**  
：利用Agent凭证横向移动  
  
- **持久化控制**  
：修改Agent配置或安装恶意技能  
  
Endor Labs的研究一针见血地指出："每个集成服务都在扩大攻击范围（blast radius），可以被转化为武器。"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Nx04DBFicyic8uUjiaiauib3w8GSyibAyERVFw7GHFhqQQzcKsUIfN1yBB1Fa3d92iabCwBSIKMmaia3zXEwdhibXPtB2EibicRre7cQM0rI/640?wx_fmt=jpeg&from=appmsg#imgIndex=1 "")  
## 四、修复建议与技术防御措施  
### 4.1 紧急响应措施  
  
**对于OpenClaw用户**  
：  
1. **立即升级**  
到2026.2.25或更高版本  
  
1. 清理**已授权设备列表**  
，检查是否存在异常注册  
  
1. 启用**双因素认证**  
（如果可用）  
  
1. 修改网关密码为**强随机字符串**  
（建议使用密码管理器生成）  
  
**对于企业安全团队**  
：  
1. 评估内部OpenClaw实例的暴露面  
  
1. 在网络层实施**出向流量监控**  
，检测异常的WebSocket连接  
  
1. 审查**非人类身份（NHIs）**的治理策略和访问权限  
  
1. 建立**AI Agent安全审计**  
的常规流程  
  
### 4.2 纵深防御策略  
  
**网络层防护**  
：  
- 使用防火墙规则限制OpenClaw端口的访问来源  
  
- 考虑将OpenClaw网关部署在隔离的网络段  
  
- 监控localhost  
端口的异常连接模式  
  
**运行时防护**  
：  
```
// 示例：浏览器层面的安全增强// 使用CSP限制WebSocket连接的源Content-Security-Policy: connect-src 'self'https:;
```  
- 在浏览器扩展或企业策略中限制对localhost  
端口的WebSocket访问  
  
- 使用本地代理前置请求，实施速率限制和异常检测  
  
**配置强化**  
：  
```
# OpenClaw配置建议gateway:rate_limit:enabled:truerequests_per_minute:10max_failed_attempts:5block_duration:300sdevice_registration:require_explicit_approval:trueauto_approve_localhost:false# 关键参数audit_logging:level:debugdestination:secure_log_server
```  
### 4.3 长期安全治理框架  
  
**针对AI Agent特有风险的治理**  
：  
1. **最小权限原则**  
：授予Agent完成特定任务所需的最小权限集  
  
1. **零信任架构**  
：即使来自localhost  
的请求也需要验证  
  
1. **持续监控**  
：实施Agent行为的基线分析和异常检测  
  
1. **技能安全审查**  
：建立ClawHub技能的安全审计流程  
  
1. **应急响应计划**  
：制定Agent被入侵后的快速隔离和恢复方案  
  
**安全开发生命周期（SDL）改进**  
：  
- 将AI Agent框架纳入漏洞管理计划  
  
- 定期进行AI特定的安全评估（如提示注入测试）  
  
- 建立Agent行为的可观测性和可审计性  
  
## 五、行业反思：AI原生时代的安全范式转移  
  
ClawJacked漏洞揭示了一个更深层次的命题：**当我们将越来越多的系统权限委托给AI Agent时，我们是否已经充分理解了新的攻击面？**  
  
传统的安全边界（网络分段、防火墙、VPN）在AI Agent时代面临重构。一个被赋予跨系统访问权限的Agent，本身就是一个高价值的攻击目标。Bitsight和NeuralTrust的研究都指出，暴露在互联网上的OpenClaw实例显著扩大了攻击面。  
  
Oasis Security的发现尤其值得警惕：**漏洞存在于核心系统本身，而非插件、市场或用户安装的扩展**  
。这意味着即使是最小化的默认安装也存在被攻击的风险。  
  
在AI native时代，安全团队需要重新审视：  
- **信任边界**  
的定义：本地是否等于可信？  
  
- **身份管理**  
的复杂性：如何管理非人类身份的生命周期？  
  
- **检测能力**  
的演进：如何识别AI Agent层面的异常行为？  
  
- **响应速度**  
的要求：AI驱动的攻击链条是否要求自动化响应？  
  
ClawJacked的24小时修复窗口展示了开源社区的反应能力，但社区修复并不等于用户安全。真正的安全在于**将AI Agent视为关键基础设施组件**  
，实施与之相称的安全投资和治理。  
  
**参考来源**  
：  
- Oasis Security Research Report: https://www.oasis.security/blog/openclaw-vulnerability[1]  
  
- OpenClaw Security Advisory: https://github.com/openclaw/openclaw/releases/tag/2026.2.25[2]  
  
- The Hacker News Original Coverage  
  
本文仅供技术交流和安全教育目的，请勿用于非法用途。相关漏洞已修复，建议读者及时更新系统。  
### 引用链接  
  
[1]  
https://www.oasis.security/blog/openclaw-vulnerability  
  
[2]  
https://github.com/openclaw/openclaw/releases/tag/2026.2.25  
  
内容转自黑白之道，侵删  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1 "")  
  
  
**今日福利**  
  
为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套**【2026最新网安资料】**  
网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！  
  
Web安全  
👇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
渗透测试  
👇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
安全面试题  
👇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFgrmaDLaYT1yV5lst9tKC72QrYjd5I8IN7kcOZIZSfQJJz8MdX6a1uA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
代码审计  
👇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFxmUkTNP1iagssZL5zkjID8hibpZsRCj1OnEb4x7ZYWqpiaymSjc8O7vSQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
红队笔记  
👇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVZS1mB4MKAo4FoMBGyVSzq38ZXEKJCjZVaTsFtLE7tIJ3zbRWF5xeA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
入门视频👇  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgxtiaXGtk7loXV41e8AXiaORJMhqFbrtcfHvJWTia6ME2oSI9msVYJu79uCicb7foufuibEHaVg32XnWw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
以上所有资料获取请扫码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAmQO922RsJH8oNVNo28hujdEqkbnrZTKI5IXibkbQGT3Es1s6wruZu9giczEsvg0Qr6G06ldEuVGFPg/640?wx_fmt=png&from=appmsg "")  
  
识别上方二维码  
  
备注：  
**2026安全合集**  
  
100%免费领取  
  
（是扫码领取，不是在公众号后台回复，别看错了哦）  
  
  
