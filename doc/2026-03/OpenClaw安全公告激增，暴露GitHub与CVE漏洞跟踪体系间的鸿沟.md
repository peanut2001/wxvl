#  OpenClaw安全公告激增，暴露GitHub与CVE漏洞跟踪体系间的鸿沟  
 FreeBuf   2026-03-11 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3eic92VEmz68QhxIX1JCDialibLgMAlkOJ9EJ6Lea2HjqyqONIRJ0T1xq1MUCcNYy4yZb5cVftxTJcrMxlHAPOKPVrXic9ReGPZfU/640?wx_fmt=png&from=appmsg "")  
##   
## 自托管AI Agent项目OpenClaw在发布数周后便成为GitHub星标最多的代码库，吸引了大量开发者社区和研究人员关注。但没人预料到，其快速增长很快成为全球漏洞跟踪体系的意外压力测试。  
##   
  
**Part01**  
## 安全公告爆发式增长  
  
  
2月下旬，该项目开始以开源项目罕见的速度发布安全公告，迅速暴露出两大主流漏洞识别系统间的结构性割裂。在爆红的三周内，OpenClaw已发布200多份GitHub安全公告（GHSA）。该项目安全公告页面目前列出255项披露，多数涉及命令执行控制、授权检查、允许列表实施和插件边界问题。这些披露的速度远超传统CVE分配流程的处理能力，导致大量公告缺乏对应的CVE编号。  
  
  
![安全公告（来源：Socket.dev）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2NJhIyD45DCD9doA2NGkdpMEAHkSXZvtenpSZR5qr6mngvy2sAFiamhGsGk6Q9OOIaG8GPoLy8ibVeL1WpclLYkHGwJqVUOEUaA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Socket.dev分析师指出，OpenClaw公告的快速积累直接暴露了漏洞披露领域长期存在的碎片化问题，这早在AI驱动开发重塑开源世界之前就已存在。单个项目如此大规模的披露，使得GHSA与CVE跟踪体系间的鸿沟比以往更加明显。  
  
  
**Part02**  
## CVE分配机制遭遇挑战  
  
  
当VulnCheck在CVE项目工作组提交对170个缺乏CVE编号的OpenClaw公告发起"DIBS"请求时，事态进一步升级。DIBS是CVE编号机构间使用的非正式协调信号，表明某组织拟评估漏洞并可能分配CVE编号。VulnCheck研究副总裁Caitlin Condon表示，此举旨在确保漏洞被武器化前获得CVE覆盖。  
  
  
但MITRE的TL-Root予以反驳，指出DIBS设计初衷是标记符合特定标准的单个漏洞，而非将整个项目批量归类。该请求最终被关闭。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2qvob3mLyicI8SBMHn6P68v2OREiaxXcHK5DgvqphlXBs2PT0HmtGQZHDZOyE1ujXic1MeZTz7me0OQQVBpIxhY6pUXZ2CqPpce0/640?wx_fmt=png&from=appmsg "")  
  
  
OpenClaw曾用名Clawdbot和Moltbot的命名历史，进一步加剧了其漏洞在多数据库和公告系统中的索引复杂性。代表用户跨外部服务执行命令的自动化平台往往暴露大量攻击面，当研究人员对此类工具展开系统性审查时，披露数量可能快速增长。  
  
  
**Part03**  
## GHSA与CVE体系的分化加剧  
  
  
GitHub安全公告为维护者提供了更简捷的路径：研究人员报告问题后，维护者可直接发布，无需外部协调。而申请CVE编号需通过CVE编号机构、格式化元数据并等待分配，因此许多项目现在默认仅使用GHSA，完全跳过CVE申请。  
  
  
这对安全团队构成实际盲区，因为包括漏洞扫描器、补丁管理系统、SBOM工具和合规框架在内的大多数企业工具都围绕CVE标识构建，这意味着仅以GHSA披露的漏洞对这些系统完全不可见。  
  
  
加州大学欧文分校2024年调查发现，GitHub公告数据库存有超过21.3万条未审核公告，每日审核量不足6条，按此速度需95年才能完成清理。巴西弗鲁米嫩塞联邦大学2026年研究分析逾28.8万条GHSA后发现，仅8%经过GitHub正式审核，未审核公告不会触发Dependabot警报，下游项目可能永远不知其依赖存在漏洞包。  
  
  
**Part04**  
## 应对建议  
  
  
RogoLabs安全工程师Jerry Gamblin构建了专用跟踪器，每小时交叉比对GitHub公告数据库与CVE项目的cvelistV5代码库中的OpenClaw公告，包含修复版本数据以避免漏洞状态混淆。Anchore安全副总裁Josh Bressers指出，许多组织仍会忽视没有CVE编号的漏洞，这种割裂构成运营风险。  
  
  
依赖AI驱动和自动化平台的安全团队在审查风险暴露时，应交叉比对GHSA和CVE数据库。随着AI加速开发使公告披露速度持续提升，仅依赖单一跟踪源可能导致已知漏洞在部署环境中完全未被检测。  
  
  
**参考来源：**  
  
OpenClaw Advisory Surge Exposes Gap Between GitHub and CVE Vulnerability Tracking  
  
https://cybersecuritynews.com/openclaw-advisory-surge-exposes-gap/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)  
  
  
### 电报讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
