#  Windows记事本漏洞可导致攻击者远程执行代码  
 FreeBuf   2026-02-12 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0p3KcEdU2SBIoFcyMHO7OhQpbciaF6jBRSkibOVOhibHOZKOgLzXfxAsAGBqclHLCaL6nyv5JrfG3DibS3zUsF8aECzHVayg92CFs/640?wx_fmt=jpeg&from=appmsg "")  
  
  
微软已修复Windows记事本应用中的一个关键远程代码执行（RCE）漏洞（CVE-2026-20841），该漏洞可能允许攻击者在受害者机器上运行恶意代码。  
  
  
该漏洞于2026年2月10日微软补丁星期二更新中披露，源于命令中特殊元素处理不当（CWE-77：命令注入），CVSS v3.1基础评分为8.8/10，评级为"重要"。  
  
  
**Part01**  
## 漏洞利用方式与危害  
  
  
此漏洞影响通过微软商店提供的现代版Windows记事本应用。未经授权的攻击者可通过网络诱骗用户打开特制的Markdown（.md）文件进行利用。  
  
  
文件加载后，其中的恶意链接会促使应用处理未经验证的协议。点击该链接将触发记事本获取并执行远程文件，在未经适当清理的情况下注入任意命令。  
  
  
攻击者使用自定义方案（例如模仿安全协议但指向攻击者控制的服务器）制作带有超链接的Markdown文件。当用户在记事本中打开文件并点击链接时，应用会直接处理该链接，导致命令注入。  
  
  
有效载荷将在登录用户的安全上下文中执行，授予攻击者相同的权限——如果用户具有管理员权限，则可能从文件访问升级到权限提升。  
  
  
**Part02**  
## 漏洞修复措施  
  
  
补丁已通过微软商店为记事本（版本11.2510+）推出，包含完整的发布说明和直接安全更新链接。由于需要用户操作，用户必须手动更新或启用自动更新。微软感谢独立研究人员Delta Obscura（delta.cyberm.ca）和"chen"的协调披露。  
  
  
此漏洞凸显了处理富文本（如Markdown）的日常应用中的风险，特别是随着记事本从基本编辑器发展为功能丰富的工具。虽然传统Notepad.exe不受影响，但商店版本的流行扩大了暴露面。  
  
  
**Part03**  
## 安全缓解建议  
  
- 立即从微软商店更新记事本  
  
- 在Windows设置中启用自动应用更新  
  
- 避免打开不受信任的Markdown文件或点击其中的链接  
  
- 使用具有基于行为检测功能的杀毒软件来检测异常的协议处理程序  
  
**参考来源：**  
  
Windows Notepad Vulnerability Allows Attackers to Execute Malicious Code Remotely  
  
https://cybersecuritynews.com/windows-notepad-rce-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
