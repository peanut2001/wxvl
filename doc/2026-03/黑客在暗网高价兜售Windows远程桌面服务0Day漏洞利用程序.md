#  黑客在暗网高价兜售Windows远程桌面服务0Day漏洞利用程序  
 FreeBuf   2026-03-09 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2kN2pVJkpDwvdB4d0WdjOfl62EeVxMnmhfaDFXsF6rnKNSwBnoKgDM3XI2oJH4Td1S4ZFChTNG8g90Jl3jIkGRTXqhWVlQxyo/640?wx_fmt=png&from=appmsg "")  
##   
  
据称，某威胁行为者正在暗网论坛上以高达22万美元的价格出售Windows远程桌面服务权限提升漏洞（CVE-2026-21533）的0Day漏洞利用程序。该高价漏洞利用程序通过不当的权限管理机制，可使攻击者获得本地管理员控制权限。  
  
  
网络安全地下社区发现，暗网论坛上出现了一份高风险交易清单，新注册用户Kamirmassabi正在拍卖CVE-2026-21533的漏洞利用程序。该威胁行为者于2026年3月3日创建账户，并在"[Virology] - malware, exploits, bundles, AZ, crypt"版块发布了相关信息。  
  
  
Dark Web Informer发现的广告明确将该漏洞标注为"0day"，定价22万美元，要求有意购买者通过私信联系进行交易反馈。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0m9RfXoWWo6a7n95aU7LLNKzdG19FxgQr5Pwiahy39owh2qibticz1wnrkSj1Fe3F4hAzKRAxYG2fKfibwse3bh00rWDDGM6LKyuI/640?wx_fmt=jpeg&from=appmsg "")  
  
  
虽然微软已于2026年2月披露CVE-2026-21533漏洞，但功能完备的武器化漏洞利用程序的出现，对企业环境构成了严重威胁。高昂的价格表明该漏洞利用程序可靠性极高，可能针对不同Windows架构的大量未打补丁系统。可视化证据证实了这一漏洞利用程序的活跃交易，凸显了网络犯罪地下市场中关键漏洞的快速商业化趋势。  
##   
  
**Part01**  
## 漏洞技术细节  
  
  
CVE-2026-21533是一个严重的权限提升（EoP）漏洞，根源在于Windows远程桌面服务中存在不当的权限管理机制。该漏洞产生的原因是产品未能正确分配、修改、跟踪或检查参与者的权限，从而产生非预期的控制范围。若成功利用，拥有标准用户权限的授权攻击者可在受感染系统上本地提升权限，可能获得完全管理控制权。  
  
  
该漏洞影响大量微软操作系统，包括Windows 10、Windows 11的多个版本，以及从2012版到最新2025版的Windows Server系列产品。  
  
  
**Part02**  
## 风险缓解措施  
  
  
该漏洞CVSSv3评分为7.8，属于高危漏洞，被列入CISA已知被利用漏洞目录，凸显了立即修复的紧迫性。为缓解此威胁，企业必须立即在所有受影响终端和服务器上应用最新的微软安全补丁。若无法立即实施缓解措施，管理员还应遵循适用的CISA BOD 22-01云服务指南，或禁用远程桌面服务。  
  
  
建议管理员在非必要情况下禁用RDS服务，将访问限制在可信网络范围内，并部署端点检测与响应（EDR）解决方案，以监控异常的注册表变更和权限提升尝试。  
  
  
**参考来源：**  
  
Hackers Allegedly Selling Exploit for Windows Remote Desktop Services 0-Day Flaw  
  
https://cybersecuritynews.com/windows-remote-desktop-services-0-day/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335724&idx=1&sn=2d144482a43dfe8583cb475e06c7dd4e&scene=21#wechat_redirect)  
  
  
### 电报讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
