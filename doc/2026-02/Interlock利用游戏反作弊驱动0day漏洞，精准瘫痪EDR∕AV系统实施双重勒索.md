#  Interlock利用游戏反作弊驱动0day漏洞，精准瘫痪EDR/AV系统实施双重勒索  
 FreeBuf   2026-02-06 02:13  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2efsicmAGJxPguHiaHSoGriaYkQNC3kndnwL0fvicOXW8SchDskajqLrMAaDf5icSVAvcib3dJjmwM8Js5nQzibRsv48iaFdluGRcNCVM/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Interlock 勒索软件组织已成为网络安全领域一个独特的威胁，主要针对美国和英国的教育机构。与多数采用勒索软件即服务（RaaS）模式的现代勒索软件组织不同，Interlock 是一个规模较小但专注的团队。该组织开发并管理自己的专属恶意软件，控制大部分攻击链条，展现出高度的复杂性和适应性。  
  
  
**Part01**  
## 攻击手法分析  
  
  
攻击通常始于 MintLoader 感染，很可能是通过"ClickFix"社会工程学手段发起。在通过名为 NodeSnakeRAT 的 JavaScript 植入程序获得初始访问权限后，攻击者会在网络中横向移动。他们利用有效账户和系统自带二进制文件建立持久性，并进行广泛的系统探测。  
  
  
Interlock 入侵的影响十分严重，既涉及数据窃取也包含数据加密。该组织被观察到使用 AZcopy 等工具在部署勒索软件前将大量数据外泄至云存储。这种双重勒索策略确保即使受害者拥有备份，攻击者仍能掌握筹码。  
  
  
![Code snippet using dynamic strings (Source - Fortinet)](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbLlHBMrnI9ahXzkByG6WicnHLMLuGR5uqM5niaVolqSeuKe4AalTqLib6Yw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Fortinet 分析师发现，该组织在站稳脚跟后会部署一套独特的工具来禁用安全防御。这使得他们能够在 Windows 终端和 Nutanix 虚拟化环境中不受干扰地执行勒索软件载荷。该组织调整技术手段并利用新漏洞的能力，使其成为全球组织面临的持续威胁，需要提高警惕并采取强有力的防御策略。  
  
  
**Part02**  
## “Hotta Killer”规避工具  
  
  
Interlock 武器库中的关键组件是一个名为"Hotta Killer"的自定义规避工具，专门用于禁用端点检测与响应（EDR）和杀毒（AV）软件。该工具采用复杂的"自带漏洞驱动"（BYOVD）技术，利用了一个合法游戏反作弊驱动中的 0Day 漏洞（原驱动名为 GameDriverx64.sys，CVE-2025-61155）。  
  
  
通过投放该漏洞驱动的重命名版本 UpdateCheckerX64.sys，恶意软件可以在内核空间执行特权命令。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbLmOtJkP0AVPVcDV7OSaQNTNic42sZs6icLI11v79O1kiaAGnbrqv0tDwYQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
"Hotta Killer"工具以名为 polers.dll 的 DLL 文件形式实现，被注入系统进程以隐藏其活动。激活后，它会创建一个符号链接与恶意驱动通信，专门针对安全软件相关进程（如匹配"Forti*.exe"模式的进程）。通过将这些安全工具的进程 ID 传递给驱动，恶意软件会强制内核终止它们，在加密开始前有效致盲组织的防御系统。  
  
  
**Part03**  
## 防御建议  
  
  
为缓解此类威胁，组织应严格阻止未经授权的远程访问软件执行，限制工作站间 SMB 和 RDP 连接。此外，阻止出站 PowerShell 网络连接可以防止恶意载荷的初始下载。  
  
  
**参考来源：**  
  
Interlock Ransomware Actors New Tool Exploiting Gaming Anti-Cheat Driver 0-Day to Disable EDR and AV  
  
https://cybersecuritynews.com/interlock-ransomware-actors-new-tool-exploiting-gaming-anti-cheat-driver-0-day/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334777&idx=1&sn=e052da512a608ee2d0ee20b662e93404&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
