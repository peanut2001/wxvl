#  OpenClaw高危漏洞可一键窃取主密钥，攻击者直通上帝模式  
 FreeBuf   2026-02-03 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38SgoPHsqlGnJqsib3bWOXwJZTdH7CAsKLrCibZutbS7YLnT8YPtEO28VMPjPmEYrjs6D4r2cE5DIiaQ/640?wx_fmt=png&from=appmsg "")  
  
  
深度安全研究团队depthfirst General Security Intelligence发现，开源AI个人助手OpenClaw（被超过10万开发者信任）存在一个高危漏洞，该漏洞已被武器化为可一键触发的远程代码执行攻击。攻击者仅需通过一个恶意链接即可完全控制受害者系统，无需任何用户交互。  
  
  
**Part01**  
## 漏洞技术原理分析  
  
  
OpenClaw架构赋予AI Agent"上帝模式"权限，可访问消息应用、API密钥并无限制控制本地计算机。在这种高权限环境中，安全容错空间极其有限。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38SgoPHsqlGnJqsib3bWOXwJEjJEpcdO2BlRNFQ2q5FMG2G0EsqlwuiajFicYzVS4ZZsprqP3cluTumA/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞利用三个组件的串联缺陷：未经验证的URL参数接收、立即建立网关连接以及自动传输认证令牌。  
  
  
**Part02**  
## 攻击链详解  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38SgoPHsqlGnJqsib3bWOXwJNWSCfZicBFBqDFytd85ic0cOAQzib4QlMW0WJjCq3BhUQJBtHrPWL910Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38SgoPHsqlGnJqsib3bWOXwJdryMrqTeznZa5icDmic1qtX8tuFyz7YX5CdUXib8AtDgUAcdFLwQxZzKg/640?wx_fmt=png&from=appmsg "")  
  
  
攻击者通过以下步骤完成攻击：  
  
- app-settings.ts模块未经验证直接接收URL中的gatewayUrl参数并存入localStorage  
  
- app-lifecycle.ts立即触发connectGateway()，将敏感authToken自动打包发送至攻击者控制的网关服务器  
  
- 利用WebSocket源验证缺失漏洞，通过受害者浏览器建立本地连接  
  
- 窃取令牌后，攻击者关闭安全机制并强制在主机执行命令  
  
**Part03**  
## 缓解措施  
  
  
OpenClaw开发团队已紧急修复该漏洞，主要措施包括：  
  
- 增加网关URL确认弹窗  
  
- 取消自动连接行为  
  
- 建议v2026.1.24-1之前版本用户立即升级  
  
- 管理员应轮换认证令牌并审计命令执行日志  
  
该事件凸显了在缺乏严格配置变更和网络连接验证的情况下，授予AI Agent无限制系统访问权限的安全风险。建议部署OpenClaw的组织：  
  
- 实施额外网络分段  
  
- 限制AI Agent进程的出站WebSocket连接  
  
- 严格审计认证令牌使用和权限变更  
  
**参考来源：**  
  
1-Click Clawdbot Vulnerability Enable Malicious Remote Code Execution Attacks  
  
https://cybersecuritynews.com/1-click-clawdbot-vulnerability-enable-malicious-remote-code-execution-attacks/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
