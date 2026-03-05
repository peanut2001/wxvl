#  【安全圈】思科修复最高危 Secure FMC 漏洞  
 安全圈   2026-03-05 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyEI7VziceWicH1QtvusoJt9jz1ibvXBKPKOB2p8mktCGbX1pHia8fIfLxmjaoq74arrsJS3bhVpiaUeiaNrLWsEE3NmMSw4a8ogwJjKQ/640?wx_fmt=png&from=appmsg "")  
  
思科修复了两个高危 Secure FMC 漏洞，**攻击者可利用其获取受管理防火墙的 root 权限**  
。  
  
思科修复了其 Secure Firewall Management Center（FMC）中的两个**最高危漏洞**  
，可导致攻击者获取 root 权限。思科 Secure FMC 是用于思科防火墙的**集中管理平台**  
。  
  
管理员可通过统一 Web 或 SSH 界面配置、监控和控制多台防火墙。通过 FMC，管理员可统一管理入侵防御（IPS）、应用控制、URL 过滤、高级恶意软件防护、日志、报表及整体网络安全态势。  
  
第一个漏洞编号为 **CVE-2026-20079**  
（CVSS 评分 10.0），属于**认证绕过**  
漏洞。  
  
该漏洞位于思科 Secure FMC 的 Web 界面，允许**未认证远程攻击者**  
绕过认证，发送构造的 HTTP 请求执行脚本，进而获取底层操作系统 root 权限。  
  
安全公告称：“思科 Secure FMC 软件 Web 界面存在漏洞，可允许未认证远程攻击者绕过认证，在受影响设备上执行脚本，获取底层操作系统 root 权限。”“该漏洞源于启动时创建的不当系统进程。攻击者可向受影响设备发送构造的 HTTP 请求利用该漏洞。成功利用可使攻击者执行多种脚本与命令，获取设备 root 权限。”  
  
第二个漏洞编号为 **CVE-2026-20131**  
（CVSS 评分 10.0），属于**远程代码执行**  
漏洞。  
  
该漏洞位于思科 Secure FMC Web 界面，允许未认证远程攻击者利用不安全的 Java 反序列化，发送构造的序列化对象，**以 root 身份执行任意代码**  
。  
  
公告称：“思科 Secure FMC 基于 Web 的管理界面存在漏洞，可允许未认证远程攻击者以 root 身份在受影响设备上执行任意 Java 代码。”“该漏洞源于对用户提供的 Java 字节流进行不安全反序列化。攻击者可向受影响设备的 Web 管理界面发送构造的 Java 序列化对象进行利用。成功利用可使攻击者在设备上执行任意代码，并将权限提升至 root。”  
  
CVE-2026-20131 同时影响思科 Security Cloud Control（SCC）防火墙管理组件。  
  
思科 PSIRT 表示，目前**未发现这两个漏洞的公开 PoC 或在野利用**  
。  
  
该网络设备巨头表示，**这些漏洞无可用缓解方案**  
，必须打补丁。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】伊朗无人机袭击亚马逊海湾数据中心，云服务中断](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074287&idx=1&sn=260b4f8cbb70b130f43948b3866c487c&scene=21#wechat_redirect)  
  
  
  
[【安全圈】暗网泄露：atlasair最大航空 1.2 TB DataBase](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074287&idx=2&sn=fa6ec4d9988a05eccc857183b5138c7a&scene=21#wechat_redirect)  
  
  
  
[【安全圈】伊朗加密货币交易所 Ariomex 遭数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074287&idx=3&sn=5093b797be5a37c8797180001f4f5487&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Chrome 安全漏洞致 Gemini Live 助手遭劫持，可被用于间谍活动](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074287&idx=4&sn=b834869c9992c41a8c629f4ff55b149d&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
