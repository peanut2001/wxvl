#  iOS攻击工具包Coruna利用23个漏洞入侵数千台iPhone设备  
 FreeBuf   2026-03-05 10:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0wYVEkK3hQQ4mjs4CIQSJA0hU7Z8TIo4zZ2HpV7o7msm7K2BBR30gOQTPAtaEbenMHnPXicKIKrID1V7Z7NGv7Ejhb6vapodsc/640?wx_fmt=png&from=appmsg "")  
##   
  
谷歌威胁情报小组（GTIG）近日曝光了Coruna——一个包含23个漏洞利用的复杂iOS攻击工具包，该工具包通过五条完整攻击链在2025年期间入侵了数千台运行iOS 13.0至17.2.1系统的iPhone设备。  
  
  
Coruna是GTIG发现的一款模块化高级iOS攻击框架，攻击范围覆盖从2019年9月发布的iOS 13.0到2023年12月发布的iOS 17.2.1系统的苹果iPhone机型。  
  
  
该工具包的名称是在某威胁攻击者错误部署调试版本框架时暴露的，内部代码名称和工具包身份因此泄露。  
  
  
其漏洞利用文档均采用地道英文撰写，最先进的组件利用了非公开的漏洞利用技术和防护绕过手段，具有国家级攻击工具的典型特征。  
##   
  
**Part01**  
## 三阶段攻击时间线  
  
  
GTIG追踪发现Coruna在2025年间流经三个不同的威胁攻击者生态圈，这为了解精英级漏洞利用工具如何从商业监控供应商扩散到国家资助的间谍组织，最终落入以经济利益为目的的犯罪分子手中提供了罕见窗口。  
  
- 2025年2月 - 商业监控客户：GTIG首次捕获到通过前所未见的JavaScript框架传送的iOS攻击链组件，该框架采用独特混淆技术，先对设备进行指纹识别以确定iPhone型号和iOS版本，再加载相应的WebKit远程代码执行（RCE）漏洞利用程序及指针验证码（PAC）绕过工具。  
  
- 2025年夏季 - 俄罗斯间谍活动（UNC6353）：相同的JavaScript框架被发现托管在cdn.uacounter[.]com上，以隐藏iFrame形式注入数十个遭入侵的乌克兰网站，涉及工业、零售和电子商务领域。漏洞利用程序根据地理位置选择性投放给iPhone用户。GTIG已通知乌克兰计算机应急响应小组（CERT-UA）清理所有受影响网站。  
  
- 2025年末 - 金融诈骗（UNC6691）：完整的漏洞利用工具包从大量假冒的金融和加密货币网站网络中获取，这些网站专门诱骗iOS用户。其中一个假冒的WEEX加密货币交易所网站会弹出窗口，特别提示用户通过iPhone访问。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX06404Zy3Olgs8l10sZETylIlPH3DPKmFFQicAw6s0BV85afaFeNgMEpZZOWZaBSTBHMvkU5IHAicH8wNRQwkqe70neOkCPQ8Vfw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
23个漏洞利用程序构成五条完整攻击链，可实现WebKit RCE、PAC绕过、沙箱逃逸、权限提升（PE）和页面保护层（PPL）绕过。关键CVE包括：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1CFz7cQm7iaGQyQficMOY13YahNN8N37qs3XdIrNI03odZOhznTlWxNZFofsKEwC4Acg41aAavxR3pfMoKtN63ibfSXUl1Yz8VlI/640?wx_fmt=png&from=appmsg "")  
  
  
其中Photon和Gallium两个漏洞利用程序针对的漏洞曾在2023年卡巴斯基发现的iOS间谍活动"三角测量行动"中被使用过。  
  
  
**Part02**  
## PlasmaLoader：金融窃密载荷  
  
  
在攻击链末端，名为PlasmaLoader（追踪编号PLASMAGRID）的分阶段二进制文件会使用com.apple.assistd作为伪装标识，将自身注入iOS根级守护进程powerd中。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0ia2DyCNq1bFR9qzvSWH8nNmA9OuHoSzuG42uYDNItHg9UsaDGlk5vgiaUhpD1YwRibxn3rP0eibrjAoFDrgXiael23nxzQMBh7wxE/640?wx_fmt=png&from=appmsg "")  
  
  
该载荷通过挂钩函数窃取敏感数据，针对包括MetaMask、BitKeep和Phantom在内的18款加密货币钱包应用。它还能扫描Apple Notes中的BIP39助记词和"备份短语"、"银行账户"等关键词。所有日志字符串和代码注释均使用中文撰写，且有证据表明注释结构由大语言模型生成，强烈指向中文开发者。  
  
  
网络通信采用HTTPS协议和AES加密，同时基于字符串"lazarus"的自定义域名生成算法（DGA）会生成15个字符的备用.xyz域名，并通过谷歌公共DNS解析器进行验证。  
  
  
GTIG已将识别出的所有域名和网站添加到谷歌安全浏览服务中。Coruna漏洞利用工具包对最新版iOS无效。安全团队和用户应采取以下措施：  
  
- 立即将所有iPhone更新至最新iOS版本  
  
- 若无法更新则启用锁定模式——Coruna在检测到锁定模式时会主动退出  
  
- 避免通过移动版Safari访问未经认证的金融/加密货币网站  
  
- 监控对.xyz域名的异常网络请求或HTTP标头sdkv和x-ts等潜在C2指标  
  
**参考来源：**  
  
Coruna Exploit Kit With 23 Exploits Hacked Thousands of iPhones  
  
https://cybersecuritynews.com/coruna-ios-exploit-kit/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
