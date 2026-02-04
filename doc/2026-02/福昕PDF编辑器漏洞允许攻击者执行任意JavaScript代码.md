#  福昕PDF编辑器漏洞允许攻击者执行任意JavaScript代码  
 网安百色   2026-02-04 10:40  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo71tc38iaYLhA7wE5ggjJjJza7qPt7MkWpVpqXEibI2qUkymAV3GHbt8SicmnibRric7aCEic0Ex0PEZnOw/640?wx_fmt=jpeg&from=appmsg "")  
  
**安全更新解决了Foxit PDF Editor Cloud中的关键跨站脚本(XSS)漏洞，这些漏洞可能允许攻击者在用户浏览器中执行任意JavaScript代码。**  
  
这些漏洞是在应用程序的**文件附件列表**  
和**图层面板**  
中发现的，由于**输入验证不足**  
和**输出编码不当**  
，为恶意代码执行创造了路径。  
  
已发现两个相关的跨站脚本漏洞，并被分配了**CVE-2026-1591**  
和**CVE-2026-1592**  
。  
  
这两个漏洞源于**相同的根本原因**  
：**图层名称和附件文件名中用户输入的净化不足**  
。  
  
当用户通过**文件附件列表**  
或**图层面板**  
与精心构造的载荷进行交互时，漏洞就会被触发。  
<table><thead><tr style="-webkit-font-smoothing: antialiased;"><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">CVE ID</span></span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">漏洞类型</span></span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">CVSS 评分</span></span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">严重性</span></span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">影响</span></span></span></th></tr></thead><tbody><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">CVE-2026-1591</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">跨站脚本(CWE-79)</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">6.3</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">中等</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">任意JavaScript执行</span></span></span></td></tr><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">CVE-2026-1592</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">跨站脚本(CWE-79)</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">6.3</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">中等</span></span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf=""><span textstyle="" style="font-size: 15px;">任意JavaScript执行</span></span></span></td></tr></tbody></table>  
该应用程序在将**不受信任的输入**  
嵌入HTML结构之前**未能正确编码**  
，从而在用户浏览器上下文中实现**任意JavaScript执行**  
。  
  
这些漏洞被归类为**CWE-79(跨站脚本)**  
，并带有**CVSS 3.0评分6.3**  
，表明**中等严重性**  
。  
  
攻击向量为**基于网络(AV:N)**  
，攻击复杂度**低(AC:L)**  
，需要**低权限(PR:L)**  
 和**用户交互(UI:R)**  
。  
  
影响评估显示**机密性风险高**  
，**完整性影响有限**  
，**无可用性影响**  
。  
  
攻击者利用这些漏洞可以访问**经过身份验证的用户可见的敏感信息**  
，包括**文档内容**  
和**会话数据**  
。  
  
由于需要**用户交互**  
和**经过身份验证的访问**  
，攻击面受到一定限制，因为攻击者必须首先**诱骗用户打开恶意文档**  
或**说服他们与精心构造的文件进行交互**  
。  
  
然而，**中等严重性评级**  
反映了这些XSS漏洞在**广泛使用的PDF编辑应用程序**  
中构成的**现实威胁**  
。  
### 修复与响应  
  
福昕已作为**2026年2月3日更新**  
的一部分，发布了针对这两个漏洞的安全补丁。**云版本**  
无需用户操作，因为更新会**自动部署**  
。运行**桌面版本**  
的用户应通过应用程序的更新机制检查可用更新。使用Foxit PDF Editor的组织应验证其安装是否正在运行**最新修补版本**  
。  
  
安全响应团队建议根据组织的安全策略，**审查文件处理实践**  
并**适当限制用户对PDF编辑功能的访问**  
。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
