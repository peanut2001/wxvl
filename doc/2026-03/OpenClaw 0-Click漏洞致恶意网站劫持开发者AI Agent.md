#  OpenClaw 0-Click漏洞致恶意网站劫持开发者AI Agent  
 FreeBuf   2026-03-01 10:04  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3XEJX8yLkic485jztpnuicARPicQfibo0OONXllgQFZlPjvCLJA2yvjADUVO3mHesOqUlVPTuNvTwMibxiakcA3E1pqH9KmmPbnabd0/640?wx_fmt=png&from=appmsg "")  
##   
  
Oasis安全研究人员在OpenClaw中发现了一个关键的零交互漏洞。作为史上增长最快的开源AI Agent框架之一，该漏洞允许任何恶意网站无需插件、扩展或用户操作即可静默获取开发者AI Agent的完全控制权。  
  
  
OpenClaw（前身为Clawdbot和MoltBot）是一款自托管AI Agent，仅用五天就获得超过10万GitHub星标，现已成为全球数千名开发者的默认个人助手。该工具在开发者笔记本电脑本地运行，可连接消息应用、日历、开发工具和本地文件系统，代表用户执行自主操作——这种广泛访问权限正是该漏洞危害性极高的关键所在。  
##   
  
**Part01**  
## 攻击原理剖析  
  
  
OpenClaw通过绑定到本地主机的WebSocket网关运行，该网关作为Agent的核心协调层。macOS配套应用、iOS设备或其他机器等连接"节点"需向网关注册，并开放包括系统命令执行、文件访问和联系人读取等能力。  
  
  
攻击只需满足一个条件：开发者在浏览器中访问恶意或被入侵网站。  
  
  
完整攻击链如下：  
- 受害者在其常规浏览器中访问攻击者控制的任何网站  
  
- 页面中的JavaScript向本地主机上的OpenClaw网关发起WebSocket连接（由于浏览器不会阻止对环回地址的跨域WebSocket连接，该操作被允许）  
  
- 脚本以每秒数百次尝试暴力破解网关密码（网关的速率限制器完全豁免本地主机连接，意味着失败尝试不会被计数、限制或记录）  
  
- 认证成功后，脚本静默注册为受信任设备（网关自动批准来自本地主机的配对，无需用户确认）  
  
- 攻击者获得Agent的完全管理员级控制权  
  
根本原因在于三个错误的设计假设：本地主机连接本质可信、浏览器发起的流量无法到达本地服务、速率限制无需应用于环回地址——这些假设在现代浏览器环境中均不成立。  
  
  
建立认证会话后，远程攻击者可直接与AI Agent交互，指令其搜索Slack历史记录中的API密钥、读取私密消息、从连接节点窃取文件以及执行任意shell命令。研究人员指出，对于使用典型OpenClaw集成的开发者而言，这等同于通过浏览器标签页实现的工作站完全沦陷，且受害者毫无察觉。  
  
  
Oasis Security的PoC完整演示了端到端攻击链，成功破解网关密码并与实时Agent实例进行交互。  
  
  
**Part02**  
## 缓解措施建议  
  
- 立即升级至OpenClaw 2026.2.25或更高版本  
  
- 清点所有开发者机器上的OpenClaw实例，包括IT可视范围外的隐蔽安装  
  
- 审计并撤销授予Agent实例的不必要凭证、API密钥和节点权限  
  
- 建立AI Agent身份治理策略，采用与人类用户和服务账户相同的严格标准  
  
  
OpenClaw团队将该漏洞评定为高危级别，并在24小时内发布补丁——这对志愿者驱动的开源项目而言值得称赞。但鉴于该工具的快速普及，企业应假设开发者设备中存在未打补丁的实例，并以处理任何关键补丁的同等紧迫性开展修复工作。  
  
  
**参考来源：**  
  
OpenClaw 0-Click Vulnerability Allows Malicious Websites to Hijack Developer AI Agents  
  
https://cybersecuritynews.com/openclaw-0-click-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
