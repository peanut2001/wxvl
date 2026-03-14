#  苹果发布iOS 15.8.7紧急更新以抵御"Coruna"漏洞利用工具包  
 网安百色   2026-03-14 10:29  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvb6R05V2TJcX18dPkuXwxdXJ9REFcGfDFYKoZkRiaTIVwtb6KNqpJ8lY0Uj1p8HjnOB5okwCGJUca8amJjyaWpXSD0LvaLGw3Q/640?wx_fmt=jpeg&from=appmsg "")  
  
苹果公司已紧急发布安全更新 **iOS 15.8.7 和 iPadOS 15.8.7**  
，旨在保护旧款设备免受名为 **“Coruna”漏洞利用工具包**  
 的严重威胁。  
  
该关键补丁于 **2026年3月11日**  
 发布，将新版本 iOS 的修复程序**回传至旧版系统**  
，确保使用老旧硬件的用户不会暴露于高级网络攻击之下。  
  
**“Coruna”漏洞利用工具包**  
 通过**链式利用多个漏洞**  
攻击苹果设备：  
- 同时针对设备**核心操作系统（内核）**  
 与 **WebKit 浏览器引擎**  
  
- 攻击者仅需诱使用户访问恶意网站，即可**完全控制**  
受影响的 iPhone 或 iPad  
### 更新背景  
- 苹果此前已于 **2023年7月至2024年1月**  
 间在 iOS 16 和 iOS 17 中修复了这些漏洞。  
- 但威胁行为者正通过 **“Coruna”工具包**  
 积极**将遗留漏洞武器化**  
。  
- 本次更新是苹果为**无法升级至最新系统**  
的旧设备推送的必要关键补丁。  
### 受影响设备  
  
iPhone 6s、iPhone 7、iPhone SE（第一代）、iPad Air 2、iPad mini（第四代）、iPod touch（第七代）  
### 修复的四大安全漏洞  
<table><thead><tr style="-webkit-font-smoothing: antialiased;"><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">漏洞类型</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE 编号</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">技术细节</span></span></th></tr></thead><tbody><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">内核漏洞</span></span></strong></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE-2023-41974</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">研究员 Félix Poulin-Bélanger 发现的</span></span><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">释放后重用内存问题</span></span></strong><span style="-webkit-font-smoothing: antialiased;"><span leaf="">。恶意应用可借此以</span></span><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">最高系统权限执行任意代码</span></span></strong><span style="-webkit-font-smoothing: antialiased;"><span leaf="">。修复方式：改进内存管理。</span></span></td></tr><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">WebKit 类型混淆</span></span></strong></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE-2024-23222</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">WebKit 渲染引擎漏洞，用户处理恶意网页内容时</span></span><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">可执行任意代码</span></span></strong><span style="-webkit-font-smoothing: antialiased;"><span leaf="">。修复方式：实施更严格的验证检查。</span></span></td></tr><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">WebKit 内存损坏</span></span></strong></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE-2023-43000</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">WebKit 中的</span></span><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">释放后重用漏洞</span></span></strong><span style="-webkit-font-smoothing: antialiased;"><span leaf="">，解析恶意网页时导致内存损坏。修复方式：增强内存管理技术。</span></span></td></tr><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><strong style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">WebKit 内存损坏</span></span></strong></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE-2023-43010</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">恶意网页内容触发的另一严重 WebKit 问题，同样导致内存损坏。修复方式：优化内存处理协议。</span></span></td></tr></tbody></table>### 风险说明  
- 由于 **“Coruna”依赖网页攻击**  
，用户仅需**浏览网页或点击短信链接**  
即面临风险。  
- **WebKit 漏洞（初始访问）**  
 与 **内核漏洞（权限提升）**  
 的组合构成**高度关键威胁**  
。  
### 行动要求  
  
**所有受影响设备的用户必须立即通过设备设置下载并安装 iOS 15.8.7 或 iPadOS 15.8.7 更新**  
，以防御已知漏洞利用。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
