#  黑客利用React Native CLI漏洞提前部署Rust恶意软件  
 FreeBuf   2026-02-04 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icfgFySDVR8vQfO3iablplDYNDDWHLQPicXs9hcv9bKf583S7sXYoHykS5hmcvMPa01dqN7TUDelSBA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part01**  
## 漏洞利用详情  
  
  
攻击者正在积极利用React Native CLI Metro服务器中的高危漏洞（CVE-2025-11953）。该漏洞存在于React Native CLI的Metro开发服务器中，该服务器默认绑定外部接口并暴露命令注入缺陷。未经认证的攻击者可发送POST请求执行任意程序，在Windows系统上还能运行参数完全可控的shell命令。  
  
  
安全公告指出："由React Native社区CLI启动的Metro开发服务器默认会绑定外部接口。该服务器暴露的端点存在操作系统命令注入漏洞，使得未经认证的网络攻击者能够向服务器发送POST请求并运行任意可执行文件。在Windows系统上，攻击者还能执行参数完全可控的任意shell命令。"  
  
  
**Part02**  
## 攻击活动分析  
  
  
Metro是React Native使用的JavaScript打包工具和开发服务器，默认配置会暴露端点，允许攻击者在Windows系统上执行操作系统命令。  
  
  
VulnCheck研究人员发现，在漏洞被广泛披露前数周就已出现持续的实际攻击案例。该机构于2025年12月21日首次观测到CVE-2025-11953（又称Metro4Shell）的实际利用，随后在2026年1月再次发现攻击活动，表明攻击者持续利用该漏洞。尽管存在这些攻击，该漏洞仍未引起广泛关注，EPSS（漏洞利用预测评分系统）评分仅为0.00405。  
  
  
VulnCheck发布的公告强调："在首次野外利用一个多月后，这些攻击活动仍未获得广泛认知。这种已观测到的利用与普遍认知之间的差距值得警惕，特别是对于易于利用且暴露在公共互联网上的漏洞。"  
  
  
**Part03**  
## 恶意软件技术细节  
  
  
VulnCheck确认CVE-2025-11953存在持续活跃的利用行为，表明攻击者已将其投入实际攻击而非测试。攻击者通过cmd.exe投递多阶段Base64编码的PowerShell加载器，禁用Microsoft Defender防护，通过原始TCP获取有效载荷，最终执行下载的二进制文件。该恶意软件为UPX压缩的Rust程序，具备基础的反分析功能。  
  
  
专家指出，攻击者连续数周重复使用相同的基础设施和技术手段。VulnCheck警告称，缺乏公开认知可能导致防御者准备不足，因为漏洞利用往往远早于官方确认时间。  
  
  
**Part04**  
## 攻击网络基础设施  
  
  
以下是涉及的网络基础设施：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icfgFySDVR8vQfO3iablplDYiaPBbGcUlNLxMDgSa5Cj7NUic8IOXnkibAhm9qDbS4uVB5fm8fQDK9ukQ/640?wx_fmt=png&from=appmsg "")  
  
  
报告总结道："CVE-2025-11953的重要性不在于其存在本身，而在于它再次印证了一个防御者需要不断重新认识的模式——可被访问的开发基础设施即刻就会成为生产基础设施，无论其初衷如何。"  
  
  
**参考来源：**  
  
Hackers abused React Native CLI flaw to deploy Rust malware before public disclosure  
  
https://securityaffairs.com/187587/hacking/hackers-abused-react-native-cli-flaw-to-deploy-rust-malware-before-public-disclosure.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
