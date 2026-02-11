#  微信Linux版高危漏洞已修复 信创安全防护仍需重点强化  
 火绒安全   2026-02-11 09:04  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/u1Oy5xQ01So1rYa5Osa7ibkNWtqvaDsouhkgswrPLBXfgEMsQCsAcbYkEEdrD3S8UPuNIdINpm2kXbu9iaB0icib07bkxwViaxwyShticgaOicoOibM/640?wx_fmt=gif&from=appmsg "")  
  
  
**近日，火绒安全团队曾复现的微信Linux版1-Click命令注入高危漏洞（CVSS4.0评分8.8）已完成修复。该漏洞作为信创场景中高频使用的Linux端办公工具安全隐患，其修复进展与防护策略备受信创用户关注。**  
  
**情况回顾**  
  
该漏洞源于微信Linux版客户端文件名处理缺陷，攻击者通过构造含反引号或$()等特殊字符的恶意文件名，接收方单次点击即可触发系统命令执行，可能导致设备被控、敏感数据窃取、恶意程序植入等风险，在微信for Linux v4.1版本中已成功复现，若程序以root权限运行还会引发权限提升。目前漏洞 POC、EXP 已公开，虽未发现在野利用，但在信创环境中，因涉及大量关键业务数据与核心设备，此前漏洞风险系数显著高于普通场景。  
  
**修复情况**  
  
**经火绒安全团队验证**  
，腾讯通过“服务端拦截+客户端优化”完成全链条修复：一方面在服务端阻断含漏洞触发字符的恶意文件上传，从源头切断传播路径；另一方面优化客户端文件名过滤机制，即便存在历史残留恶意文件，也无法通过点击触发漏洞，彻底消除信创终端面临的相关安全威胁。  
  
![修复测试.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqToI7AmEwN57fCNY7lnydFtSGV90Lbs2NoCuIDs4kHdlCERhX3qZRXPia8WfUL585IaVwAlAulrMT0jEiaxhicRXmOAh7urhpvJo/640?wx_fmt=png&from=appmsg "")  
  
**修复验证**  
  
作为办公沟通的常用工具，微信Linux版等软件在党政、金融、能源、电信等关键行业的信创终端中广泛应用，而信创场景以麒麟、统信UOS等Linux系操作系统为核心部署底座，涉及大量敏感业务数据与核心业务系统，该漏洞的潜在风险系数显著高于普通使用场景。  
  
**因此针对信创场景的特殊性与安全合规要求，火绒安全专家也为信创用户提出了常态化安全防护建议，筑牢漏洞修复后的安全屏障：**  
  
**验证修复覆盖性**  
  
  
  
针对长期离线运行的信创终端，定期安排联网更新操作，确保终端同步服务端防护规则，实现修复全覆盖；  
  
**严守权限管控底线******  
  
  
  
严格遵循相关原则，禁止以root权限运行微信Linux版，即便出现未知安全漏洞，也能有效限制危害扩散范围；  
  
**保留安全操作流程**  
  
  
  
延续“右键下载文件-保存至隔离目录-人工核查文件名-安全工具扫描后打开”的操作规范，防范历史残留恶意文件或漏洞变种攻击；  
  
**部署信创适配安全工具**  
  
  
  
在信创终端中搭载适配国产架构安全产品，实现对终端异常行为的实时检测与告警，弥补传统防护手段在信创环境中的能力断层；  
  
**建立软件安全台账**  
  
  
  
将办公类工具的漏洞动态、修复情况纳入企业漏洞管理，同步跟踪上游软件安全更新，实现风险提前预警；  
  
**对于普通微信Linux版用户**  
  
  
  
火绒安全专家建议仍需保持良好的网络使用习惯，拒绝点击陌生账号、非认证渠道发送的文件与链接，通过官方渠道获取客户端安装包，并搭配终端安全防护工具，实现对各类恶意攻击的双重防护。  
  
**火绒安全团队后续将持续聚焦信创场景高频工具与核心系统安全，及时跟踪漏洞动态、升级防护能力，为信创生态安全保驾护航。若遇到技术问题，信创用户可通过火绒官方客服（400-998-3555）获取针对性解决方案。**  
  
HUORONG  
  
火绒安全成立于2011年，是一家专注、纯粹的安全公司，致力于在终端安全领域为用户提供专业的产品和专注的服务，并持续对外赋能反病毒引擎等相关自主研发技术。多年来，火绒安全产品凭借“专业、干净、轻巧”的特点收获了广大用户的良好口碑。火绒企业版产品更是针对企业内外网脆弱的环节，拓展了企业对于终端管理的范围和方式，提升了产品的兼容性、易用性，最终实现更直观的将威胁可视化、让管理轻便化，充分达到保护企业信息安全的目的。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4K1e9ubHiaGLicyPrL2TGOQUVuzGfhiavltoNEsaCLCyJXChRib3yHaPTI00hV8oFkSsvwgunn2k0wSg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "")  
  
  
  
求点赞  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN05z6DXwgVYcdZ6RFjwxdDoeAEia9eYdgyJaAJ0LDBJmxTdm2JUhkc4tg/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "")  
  
  
求分享  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0CbyZz9kNTCKcA0puOEWfAYZnT6v6rr3kdBWIFw4TlSh7AgzSdOfAng/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "")  
  
  
求喜欢  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0gBxG1O1Y7YCFGicYGrDUpcBg7iaLgNpCsDzNKcHwHcBgKktMtTSs6ZSA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14 "")  
  
  
****  
  
