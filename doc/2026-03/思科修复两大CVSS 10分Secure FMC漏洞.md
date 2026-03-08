#  思科修复两大CVSS 10分Secure FMC漏洞  
 FreeBuf   2026-03-08 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
##   
##   
  
**Part01**  
## 漏洞概况  
  
  
思科修复了其Secure Firewall Management Center（FMC，安全防火墙管理中心）中的两个最高危漏洞，攻击者可能借此获取受管理防火墙的root权限。Secure FMC是思科防火墙的集中管理平台，管理员可通过单一Web或SSH界面配置、监控和控制多台防火墙。通过该平台，团队可管理入侵防御（IPS）、应用控制、URL过滤、高级恶意软件防护等策略，以及日志记录、报告和整体网络安全态势。  
  
  
**Part02**  
## CVE-2026-20079：认证绕过漏洞  
  
  
该漏洞存在于Secure FMC的Web界面，允许未经认证的远程攻击者绕过认证机制，通过发送特制HTTP请求执行脚本，最终可能获取底层操作系统的root权限。思科安全公告指出："该漏洞源于系统启动时创建的不当进程。攻击者可向受影响设备发送特制HTTP请求实施利用，成功利用将允许执行多种脚本和命令，从而获取设备root权限。"  
  
  
**Part03**  
## CVE-2026-20131：远程代码执行漏洞  
  
  
该漏洞同样存在于Secure FMC的Web界面，允许未经认证的远程攻击者利用不安全的Java反序列化机制，通过发送特制序列化对象以root身份执行任意代码。公告说明："该漏洞由用户提供的Java字节流反序列化不安全导致。攻击者可向受影响设备的Web管理界面发送特制序列化Java对象实施利用，成功利用将允许在设备上执行任意代码并提升至root权限。"此漏洞同时影响思科Security Cloud Control（SCC）防火墙管理系统。  
  
  
**Part04**  
## 漏洞利用情况  
  
  
思科产品安全事件响应团队（PSIRT）表示尚未发现这两个漏洞被公开披露或主动利用的情况。该公司强调目前没有针对这些漏洞的有效临时解决方案。  
  
  
**参考来源：**  
  
Cisco fixes maximum-severity Secure FMC bugs threatening firewall security  
  
https://securityaffairs.com/188921/security/cisco-fixes-maximum-severity-secure-fmc-bugs-threatening-firewall-security.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
