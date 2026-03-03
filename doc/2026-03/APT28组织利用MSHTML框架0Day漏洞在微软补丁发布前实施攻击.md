#  APT28组织利用MSHTML框架0Day漏洞在微软补丁发布前实施攻击  
 FreeBuf   2026-03-03 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2PCnfHx1icj2fNu90Lfu0hLwCHeiaEgA291SbjGOfLKMibIJQzaV2A1IlLChzhm8Zy4eyskJLibysAfictLFNzGkcyk7iaYDCicj66b0/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
Akamai最新研究发现，与俄罗斯有关联的国家级威胁组织APT28可能已利用微软近期修补的一个安全漏洞实施攻击。该漏洞编号为CVE-2026-21513（CVSS评分：8.8），属于MSHTML框架安全功能绕过漏洞，危害等级为高危。  
  
  
微软在漏洞公告中指出："MSHTML框架的保护机制失效，可使未经授权的攻击者通过网络绕过安全功能。"微软已在2026年2月补丁星期二更新中修复该漏洞。但微软同时确认，该漏洞在现实攻击中已被作为0Day利用，并感谢微软威胁情报中心（MSTIC）、微软安全响应中心（MSRC）、Office产品组安全团队以及谷歌威胁情报小组（GTIG）的报告。  
##   
  
**Part01**  
## 攻击技术分析  
  
  
在典型攻击场景中，攻击者会诱骗受害者打开通过链接或邮件附件传送的恶意HTML文件或快捷方式（LNK）文件。微软指出，当精心构造的文件被打开后，会操纵浏览器和Windows Shell的处理流程，导致操作系统执行恶意内容，从而使攻击者绕过安全功能并可能实现代码执行。  
  
  
虽然微软未正式公布0Day利用的具体细节，但Akamai表示已识别出2026年1月30日上传至VirusTotal的恶意样本，该样本与APT28关联的基础设施存在联系。值得注意的是，乌克兰计算机应急响应小组（CERT-UA）上月初已将该样本标记为APT28利用另一个微软Office漏洞（CVE-2026-21509，CVSS评分：7.8）实施攻击的关联样本。  
  
  
![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX026OuZ9vVRFick46ot7icsJiaczicicwZVcHAzbEjQYKlQiaXpJMA20BFoc4R9TQxzEydz8xlsKicWHc2s0tHrozkhJuc7Nu3Hrdx0Qs/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part02**  
## 漏洞利用机制  
  
  
Akamai分析指出，CVE-2026-21513漏洞源于"ieframe.dll"中处理超链接导航的逻辑缺陷，由于对目标URL验证不足，导致攻击者控制的输入可到达调用ShellExecuteExW的代码路径，从而在预期浏览器安全上下文之外执行本地或远程资源。  
  
  
安全研究员Maor Dahan表示："该攻击载荷包含一个精心构造的Windows快捷方式（LNK），在标准LNK结构后直接嵌入HTML文件。LNK文件会启动与wellnesscaremed[.]com域名的通信，该域名归属于APT28，已被广泛用于攻击活动的多阶段载荷分发。漏洞利用通过嵌套iframe和多DOM上下文操纵信任边界。"  
  
  
**Part03**  
## 安全防护绕过  
  
  
Akamai强调，该技术可使攻击者绕过网络标记（MotW）和Internet Explorer增强安全配置（IE ESC），导致安全上下文降级，最终通过ShellExecuteExW在浏览器沙箱外执行恶意代码。公司补充说明："虽然已观测到的攻击活动主要利用恶意LNK文件，但任何嵌入MSHTML的组件都可能触发漏洞代码路径。因此，除基于LNK的钓鱼攻击外，还应防范其他可能的传播方式。"  
  
  
**参考来源：**  
  
APT28 Tied to CVE-2026-21513 MSHTML 0-Day Exploited Before Feb 2026 Patch Tuesday  
  
https://thehackernews.com/2026/03/apt28-tied-to-cve-2026-21513-mshtml-0.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
