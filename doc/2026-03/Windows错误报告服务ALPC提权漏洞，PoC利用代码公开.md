#  Windows错误报告服务ALPC提权漏洞，PoC利用代码公开  
 FreeBuf   2026-03-03 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0zHVFOa2Ssyr4hgsS5p46qKZsO8nwx6cE1DYt7BJAtvuicyiaBLzTTqFeOQ0ibBQBicGXF6DSqR4bRd1TBxv1G9S1yfjickc7Geq8E/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
随着概念验证（PoC）利用代码的公开，微软 Windows 操作系统中的一个严重本地提权（LPE）漏洞（CVE-2026-20817）浮出水面。该漏洞存在于 Windows 错误报告（WER）服务中，允许低权限认证用户执行任意恶意代码并获取 SYSTEM 级完全权限。  
  
  
安全研究员 @oxfemale（X/Twitter 账号 @bytecodevm）在 GitHub 上发布了详细研究报告及配套的 C++ PoC 利用代码，揭示了 Windows 进程间通信错误报告机制中存在的重大安全缺陷。  
##   
  
**Part01**  
## 漏洞技术原理  
  
  
该漏洞核心涉及高级本地过程调用（ALPC）协议。WER 服务通过名为 \WindowsErrorReportingService 的特定 ALPC 端口与其他进程通信。研究发现，漏洞具体存在于 SvcElevatedLaunch 方法（方法编号 0x0D）中，WER 服务完全未能正确验证调用用户的权限。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2YOVjU5XictXHicoCQfxxGibCMYh0tANtgJmYqGRkmN0MYEWQSlURImxTicnibibWVrXzabm1ZjOibmwYU2WtSvGtfanot0uM3uy94T8/640?wx_fmt=jpeg&from=appmsg "")  
  
  
攻击者可强制服务从共享内存块读取自定义命令行参数来启动 WerFault.exe。由于 WER 服务以高权限运行，新生成的进程将继承 SYSTEM 令牌，该令牌包含 SeDebugPrivilege（允许调试任何进程）和 SeImpersonatePrivilege（允许模拟任何用户）等危险权限。  
  
  
**Part02**  
## 漏洞利用步骤  
  
  
成功触发漏洞需要执行以下操作序列：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2ktVPm4PkGws2wXlOEHOvyEu8ZOjBFGMwj9KsboIxU49yAWeA5yNKahic6bltqibibkhFuo9n0veZ9OhXdvfHQ6SmMCcPhukJxmY/640?wx_fmt=png&from=appmsg "")  
  
  
**Part03**  
## 影响范围与修复建议  
  
  
该漏洞影响包括 2026 年 1 月之前的所有 Windows 10/11 版本，以及运行 Windows Server 2019/2022 的企业服务器环境。微软已在 2026 年 1 月安全更新中修复该漏洞。  
  
  
安全建议：  
  
- 立即应用最新安全补丁  
  
- 监控环境中异常的 WerFault.exe 子进程  
  
- 检测异常的 SYSTEM 令牌行为以识别潜在攻击尝试  
  
**参考来源：**  
  
PoC Exploit Released for Windows Error Reporting ALPC Privilege Escalation  
  
https://cybersecuritynews.com/poc-windows-alpc-privilege-escalation/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
