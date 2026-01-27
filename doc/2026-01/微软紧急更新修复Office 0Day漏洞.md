#  微软紧急更新修复Office 0Day漏洞  
 FreeBuf   2026-01-27 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38p1qHebKib5H8RBpPYAibsIczZuxy8AnULDrkic4M7ZwpXy8oZbPiaSQs7IxtuyQ61CSB5mHdiapdyJVQ/640?wx_fmt=png&from=appmsg "")  
  
  
微软已发布紧急安全更新，修复其Office套件中被野外利用的0Day漏洞，该漏洞允许攻击者绕过关键防御措施。编号为CVE-2026-21509的漏洞CVSS评分为7.8分，直击Office处理对象链接与嵌入（OLE）控件的核心机制。  
  
  
**Part01**  
## 漏洞特性分析  
  
  
该漏洞被归类为"安全功能绕过"类型，意味着它不仅会导致系统崩溃，还会悄然打开本应锁闭的安全门。具体而言，它破坏了旨在"保护用户免受易受攻击的COM/OLE控件侵害"的OLE缓解措施。  
  
  
漏洞根源在于经典弱点："安全决策中依赖不可信输入"。通过向系统输入精心构造的恶意数据，攻击者可诱使Microsoft Office降低防护级别，从而在本地执行未授权操作。  
  
  
**Part02**  
## 攻击触发条件  
  
  
值得注意的是，这并非"路过式"攻击（仅浏览网页就会导致设备沦陷）。该漏洞的用户交互评级为"必需"（UI:R）。要触发漏洞利用，"攻击者必须向用户发送恶意Office文件并诱使其打开"。  
  
  
这种对社交工程（钓鱼邮件、欺骗性下载或紧急"发票"附件）的依赖，使得人为因素成为最后防线。需特别说明的是，预览窗格是安全的——在该处查看文件不会触发攻击。  
  
  
**Part03**  
## 修复方案与应对措施  
  
  
微软于2026年1月26日发布修复补丁，涉及Microsoft Office 2016和Microsoft Office 2019版本。强烈建议用户检查构建版本号，安全版本为Build 16.0.10417.20095或更高。用户可通过任意Office应用程序中的"文件>账户>关于"路径验证当前状态。  
  
  
对于无法立即打补丁的组织，可采取手动关闭开关：管理员可通过修改Windows注册表来禁用易受攻击的功能，具体操作为阻止特定COM组件。操作步骤如下：  
  
- 导航至  
  
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\16.0\Common\COM Compatibility\  
  
- 创建名为{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}的子项  
  
- 在该子项内添加名为Compatibility Flags的REG_DWORD值，并设置十六进制数值为400  
  
虽然有效，但手动编辑注册表存在风险。最稳妥的解决方案仍是安装官方补丁。"运行Microsoft Office 2016和2019的客户应确保安装更新，以免受此漏洞影响"。  
  
  
**参考来源：**  
  
Under Attack: Microsoft Patches Office Zero-Day (CVE-2026-21509) Exploited in the Wild  
  
https://securityonline.info/under-attack-microsoft-patches-office-zero-day-cve-2026-21509-exploited-in-the-wild/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334254&idx=1&sn=60c1a1f106cdbab728bc207a35262d08&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
