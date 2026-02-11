#  紧急修复！Windows 记事本漏洞可致远程代码执行  
看雪学苑
                    看雪学苑  看雪学苑   2026-02-11 09:59  
  
微软于近日修补了 Windows 系统中的“记事本”（Notepad）应用中的一个高危漏洞。该漏洞可能允许攻击者通过网络，诱使用户打开特制的 Markdown 文件，从而在受害者计算机上远程执行恶意代码。  
  
  
此漏洞编号为  
CVE-2026-20841，  
被归类为命令注入问题。其在通用  
漏洞评分系统（CVSS v3.1）中获得8.8 分（  
满分10分），危险等级评定为“重要”。  
  
  
漏洞影响与攻击原理  
  
此次漏洞主要  
影响通过Microsoft Store获取的现代版 Windows 记事本应用。  
攻击者可以精心构造一个包含恶意链接的 Markdown (.md) 文件。当用户使用受影响的记事本版本打开此文件并点击其中的链接时，应用可能会未经充分验证即处理非常规的网络协议。  
  
  
这一过程可被利用来从攻击者控制的服务器获取远程文件并执行，最终导致任意命令在用户设备上运行。命令将在当前登录用户的权限下执行，这意味着如果用户拥有管理员权限，攻击者可能获得同等级别的系统控制权，带来数据泄露、系统破坏等更高风险。  
  
  
修复与应对措施  
  
微软已通过 Microsoft Store 为记事本应用发布了安全更新（版本号 11.2510及以上）。  
用户需要手动检查并更新应用，或确保系统已开启 Microsoft Store 应用的自动更新功能。  
  
  
用户应采取以下措施进行防护：  
  
1.立即更新：  
前往 Microsoft Store，检查并更新“记事本”应用至最新版本。  
  
2.谨慎处理文件：  
不要随意打开来源不明的 Markdown (.md) 文件，尤其避免点击此类文件中的链接。  
  
3.启用安全防护：  
确保操作系统更新至最新，并使用具备行为检测功能的杀毒软件。  
  
  
安全启示  
  
此次事件提醒我们，即使是记事本这类看似简单的日常应用，随着功能日益丰富（如支持 Markdown 预览），也可能引入新的安全攻击面。保持软件更新至最新版本，是防范此类威胁最基本且有效的手段。  
  
  
参考来源：本报道基于微软官方发布的安全更新通告、通用漏洞披露（CVE）系统及国家漏洞数据库（NVD）的相关条目、以及行业广泛报道的软件安全更新信息综合撰写。  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
