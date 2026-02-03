#  一键Clawdbot漏洞：启动恶意远程代码执行攻击  
O安全研究员
                    O安全研究员  O安全研究员   2026-02-02 12:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzucz9n0R5nibtXMzxAviaLyNc5VJh1N5SfiaESxC4pDl58g4cKVWV15ia8TNfMqFc5mWrz0nPiccqCHSQ/640?wx_fmt=png&from=appmsg "")  
  
  
OpenClaw——这款被超过10万开发者信赖的开源AI个人助手——中的一个关键漏洞已被发现并被武器化，成为一项毁灭性的一键远程代码执行漏洞。  
  
  
depthfirst通用安全情报公司的安全研究人员发现了一个逻辑缺陷，结合其他漏洞，可能引发连锁反应。  
  
  
允许攻击者通过单一恶意链接完全控制受害者系统，无需用户作。  
  
## 漏洞概览：技术攻击机制  
  
  
OpenClaw 的架构赋予 AI 代理“神模式”访问消息应用、API 密钥以及对本地计算机的无限制控制权。  
  
  
尽管社区对该平台的热情推动了快速采用，但在如此高特权环境下，安全容错空间变得极其有限。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzucz9n0R5nibtXMzxAviaLyNFic3iaYXJBqJAOv3b6pzwpp20z9coyhbZ9n1Isz2j0KiajWtibdolbEGsg/640?wx_fmt=png&from=appmsg "")  
  
  
新披露的漏洞利用了三个独立的组件，这些组件是依次工作的：不安全的URL参数摄取、无需验证即可立即连接网关，以及自动传输认证令牌。  
  
  
利用链从三个看似无害的作开始，这些作在代码库中独立发生。  
  
  
app-settings.ts模块盲目接受 URL 中的 gatewayUrl 查询参数，无需验证，然后直接存储在 localStorage。  
  
  
在设置应用后，app-lifecycle.ts会立即触发connectGateway（），该命令会自动将安全敏感的authToken捆绑到攻击者控制的网关服务器的连接握手中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzucz9n0R5nibtXMzxAviaLyN787A2KaEOKXZNn3N2dzWkmagzUfSbowB8tA3hZXjELuDMnxMUQeAFg/640?wx_fmt=png&from=appmsg "")  
  
  
这种模式造成了关键信息披露的漏洞。杀链还利用了WebSocket起源验证的一个额外漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzucz9n0R5nibtXMzxAviaLyNudA7UYPRU3JiadWiamoRzc0G4JYl9mYbzrzJJ6n9MwpUSsvliaWOWGUSw/640?wx_fmt=png&from=appmsg "")  
  
  
当受害者访问恶意网页时，攻击者注入的JavaScript会在其浏览器上下文中执行，建立与受害者在localhost：18789上运行的OpenClaw实例的本地连接。  
  
  
与标准 HTTP 连接不同，浏览器 WebSocket 实现不强制执行同源策略保护;相反，它们依赖服务器端起源头部验证，而 OpenClaw 完全省略了这一点。  
  
  
这种跨站WebSocket劫持（CSWSH）使攻击者能够通过受害者的浏览器作为代理进行转换。  
  
  
一旦通过被盗令牌认证，攻击者就会利用操作员。行政和操作员岗位。批准，以及关闭安全机制的范围。  
  
  
执行 aponce.set 请求会关闭用户确认提示，而配置则是补丁请求将 tools.exec.host 设置为“网关”，强制命令直接在主机上执行，而非容器化沙箱内。  
  
  
最终有效载荷调用节点。用任意的bash命令调用，实现系统完全被攻破。  
  
## 缓解措施  
  
  
OpenClaw 开发团队迅速修复了该漏洞，实现了网关 URL 确认模态，消除了导致攻击的无提示自动连接行为。  
  
  
DepthFirst 建议所有运行 v2026.1.24-1 之前版本的用户仍处于风险状态，应立即升级。  
  
  
管理员应轮换认证令牌，并审计命令执行日志是否有可疑活动。  
  
  
此事件凸显了在未经过配置变更和网络连接的稳健验证的情况下，向AI代理提供无限制系统访问所带来的安全风险。  
  
  
部署 OpenClaw 的组织应实现额外的网络分段，限制 AI 代理进程的出站 WebSocket 连接，并严格维护认证令牌使用和权限修改的审计日志。  
  
