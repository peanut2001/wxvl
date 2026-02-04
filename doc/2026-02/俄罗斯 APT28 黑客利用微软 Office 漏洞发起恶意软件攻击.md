#  俄罗斯 APT28 黑客利用微软 Office 漏洞发起恶意软件攻击  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-04 01:01  
  
**导****读**  
  
  
  
俄罗斯黑客组织 Fancy Bear（又名 APT 28）正在利用 CVE-2026-21509，这是一个微软 Office 漏洞，微软上周发布了紧急修复程序。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHWZgtibnXIiaClm1tUdiaBAtctDBoe93aMIxkJGoQvhBJ3d926xzicIL7HdWJNgOuHzDbVUqxCHe9Zug/640?wx_fmt=png&from=appmsg "")  
  
CVE-2026-21509 允许未经授权的攻击者通过创建和诱骗目标打开带有陷阱的 Office 文件，从而绕过本地安全功能（Microsoft 365 和 Microsoft Office 中的 OLE 缓解措施）。  
  
  
2026 年 1 月 29 日，也就是微软发布上述修复程序三天后，Zscaler 研究人员发现一起电子邮件网络钓鱼活动，该活动通过恶意 RTF 文件传播后门。  
  
  
我们观察到了攻击链的两种变体。这两种变体都以一个精心构造的 RTF 文件开始，该文件利用了 CVE-2026-21509 漏洞，并在成功利用后，从攻击者的服务器下载一个恶意投放器 DLL。  
  
  
第一个投放器变体 DLL 负责部署一个名为 MiniDoor 的恶意 Microsoft Outlook Visual Basic for Applications (VBA) 项目。MiniDoor 的主要目标是窃取用户的电子邮件并将其转发给攻击者。  
  
  
第二个投放器变体触发多阶段感染链，该感染链从（以前未记录的）PixyNetLoader 开始。  
  
  
PixyNetLoader 会在目标端点上放置恶意组件，并准备 Windows 环境以下载和执行其他有效载荷，包括与开源 Covenant C2 框架关联的 Grunt 植入程序。  
  
  
Zscaler 称，这些攻击活动的目标是中欧和东欧的用户，包括乌克兰、斯洛伐克和罗马尼亚，电子邮件是用罗马尼亚语、乌克兰语和英语编写。  
  
  
乌克兰计算机应急响应小组（CERT）表示，其中一个被植入恶意文件——Consultation_Topics_Ukraine (Final).doc——创建于1月27日，也就是微软发布紧急修复程序后的第二天。该文件包含与欧盟常驻代表委员会（COREPER）就乌克兰局势进行磋商相关的文本。  
  
  
CERT指出，另一份名为BULLETEN_H.doc的文件被发送到60多个邮箱地址，这些邮箱地址主要属于乌克兰中央行政机关。该邮件据称由乌克兰水文气象中心发出。  
  
  
2026年1月下旬，又发现了三份存在类似漏洞利用的文件。乌克兰计算机应急响应小组（CERT）表示，他们预计利用此漏洞发起的攻击数量将会增加，因为攻击者押注目标系统修复或缓解漏洞的速度较慢（或根本无法修复）。  
  
  
Zscaler 研究人员表示，攻击目标、MiniDoor 后门、Covenant Grunt 样本滥用 Filen（云存储）API 进行 C2 通信，以及攻击中使用的技术，都指向与俄罗斯有关联的威胁组织 APT28 。  
  
  
目前尚不清楚该组织是否在微软修复漏洞之前利用了 CVE-2026-21509，但可能性很大，因为多年来他们一直利用其他  
0day  
漏洞。  
  
  
技术报告：  
  
《APT28 在“新漏洞利用行动”中利用了 CVE-2026-21509 漏洞》  
  
https://www.zscaler.com/blogs/security-research/apt28-leverages-cve-2026-21509-operation-neusploit  
  
  
新闻链接：  
  
https://www.helpnetsecurity.com/2026/02/03/russian-hackers-are-exploiting-recently-patched-microsoft-office-vulnerability-cve-2026-21509/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
