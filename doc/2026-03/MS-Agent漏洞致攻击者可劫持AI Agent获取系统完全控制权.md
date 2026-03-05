#  MS-Agent漏洞致攻击者可劫持AI Agent获取系统完全控制权  
 FreeBuf   2026-03-05 10:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3dlvOic01lexiat65Uq0BxTUHUtb3UpNoxzwUlPpy2TnIcoaJh3pEF1omJOEVXuZjokMOD6b1f03eHAJauO358JulibMlzQqRVhY/640?wx_fmt=png&from=appmsg "")  
##   
  
**Part01**  
## 漏洞概述  
  
  
研究人员在用于实现 AI Agent 自主执行任务的轻量级框架中发现一个高危安全漏洞（CVE-2026-2256）。根据 CERT/CC 发布的漏洞公告，攻击者可利用该漏洞诱骗 AI 执行恶意命令，从而可能完全控制系统。  
  
  
**Part02**  
## 技术细节  
  
  
该漏洞源于 MS-Agent 框架处理外部不可信输入的方式。其内置的"Shell 工具"允许 AI 运行操作系统命令来完成任务，但研究人员发现该工具在执行前未能正确净化处理内容。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0jY7ic70CJuDVOqkMNPUNDTHG1zPfDxFxzsmIv5SGuFhh2fLiaBqK88XajCpicRKs8X5nbYqR8Nrws7yzdjEySwokhTnY0lX6eG4/640?wx_fmt=png&from=appmsg "")  
  
  
**Part03**  
## 攻击原理  
  
  
攻击者可通过"提示注入"技术利用该漏洞，即在正常文本中隐藏精心构造的指令。当 AI Agent 处理包含恶意命令的文档或外部代码时，会不加甄别地将这些命令转发给 Shell 工具执行。  
  
  
虽然框架通过 check_safe() 过滤器尝试拦截危险命令，但 CERT/CC 报告指出这种基于"拒绝列表"的防御机制极易被绕过。攻击者通过命令混淆或替代语法即可使恶意代码绕过检测直达执行层。  
  
  
**Part04**  
## 潜在影响  
  
  
成功利用该漏洞的攻击者可在受害者机器上以 MS-Agent 进程权限执行任意操作系统命令，可能导致：  
  
- 窃取 AI Agent 可访问的敏感数据  
  
- 修改或删除关键系统文件  
  
- 建立持久化机制或安装后门  
  
- 横向移动渗透企业网络其他资产  
  
**Part05**  
## 缓解措施  
  
  
目前厂商尚未发布安全补丁，建议采取以下防护措施：  
  
- 沙箱隔离：在高度隔离环境中运行 MS-Agent 框架  
  
- 最小权限：仅授予 Agent 执行任务所需的最低系统权限  
  
- 内容验证：仅在可完全信任外部内容的环境中部署该框架  
  
- 强化过滤：用严格的白名单机制替代脆弱的拒绝列表过滤  
  
**参考来源：**  
  
MS-Agent Vulnerability Let Attackers Hijack AI Agent to Gain Full System Control  
  
https://cybersecuritynews.com/ms-agent-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
