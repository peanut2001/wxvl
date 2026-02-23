#  SolarWinds 2026 的关键漏洞  
 暗镜   2026-02-22 23:09  
  
SolarWinds 在其 Web Help Desk (WHD) 软件中发现了几个严重漏洞，这些漏洞可能允许攻击者获得未经授权的访问权限并远程执行恶意代码，因此该公司发布了安全更新。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb0BJaqp3eSFQO24ll8PxO4PvVctibHu3enMKiawAROMeMv9Sibiapbnqu296EKglvib8Ml7INpiaFHaO20v4Rs5w3O0iansGq0OsVDZew/640?wx_fmt=png&from=appmsg "")  
  
  
### 分析  
  
**CVE-2025-40551 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H - 9.8**  
  
**CVE-2025-40551** 漏洞源于应用程序接收来自外部源的序列化数据，并在未验证其安全性的情况下对其进行转换。攻击者可以精心构造数据，当服务器反序列化这些数据时，即可触发任意代码的执行。SolarWinds 已发布安全更新修复此漏洞，该漏洞主要影响 SolarWinds Web Help Desk。  
  
**CVE-2025-40552 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H - 9.8**  
  
**CVE-2025-40552**源于一个薄弱的身份验证验证问题（被归类为 CWE-1390），这意味着系统在授予对受保护功能的访问权限之前，未能正确验证凭据。结合同一产品中的其他漏洞，这种绕过方式可能导致更广泛的攻击。建议将 Web Help Desk 更新到已修复的版本。  
  
**CVE-2025-40553 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H - 9.8**  
  
**CVE-2025-40553**被归类为对不受信任的数据进行不安全反序列化，这可能允许攻击者在无需登录的情况下远程执行服务器上的代码。SolarWinds 已发布安全补丁，修复了 Web Help Desk 2026.1 版本中的此漏洞及其他一些严重漏洞。  
  
**CVE-2025-40554 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H - 9.8**  
  
**CVE-2025-40554** 被归类为弱身份验证漏洞 (CWE-1390)，这意味着该软件在允许请求者执行某些功能之前，未能正确验证其身份。拥有网络访问权限的攻击者可以向应用程序发送特制的请求，应用程序会将这些请求视为来自合法用户的请求而接受，从而允许攻击者在无需凭据的情况下调用内部功能。建议将 SolarWinds Web Help Desk 更新到已修复的版本。  
### 参考  
-   
- **https://www.solarwinds.com/trust-center/security-advisories**  
-   
- **https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html**  
-   
- **https://arcticwolf.com/resources/blog/multiple-critical-authentication-bypass-remote-code-execution-vulnerabilities-fixed-in-solarwinds-web-help-desk/**  
-   
- **https://cyberpress.org/solarwinds-bypass-vulnerabilities/**  
-   
-   
-   
-   
