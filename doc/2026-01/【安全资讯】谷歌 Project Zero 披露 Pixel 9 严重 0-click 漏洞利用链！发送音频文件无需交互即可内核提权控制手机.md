#  【安全资讯】谷歌 Project Zero 披露 Pixel 9 严重 0-click 漏洞利用链！发送音频文件无需交互即可内核提权控制手机  
原创 360漏洞研究院
                    360漏洞研究院  360漏洞研究院   2026-01-19 09:58  
  
“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg "")  
  
  
Google Project Zero 安全研究团队近日发布重磅安全研究报告，详细披露了一条针对 Google Pixel 9 设备的**完整 0-click（零点击） 漏洞利用链**  
。该攻击链仅需两个漏洞（**CVE-2025-54957**  
 和 **CVE-2025-36934**  
），**攻击者可通过发送恶意构造的音频文件，在用户毫无察觉的情况下，实现从远程代码执行到内核权限提升的全链条攻击，最终完全控制目标设备。**  
  
谷歌已于 2026 年 1 月 5 日发布安全更新修复相关漏洞，该漏洞利用链对整个 Android 生态系统的安全敲响了警钟。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFjmUEKfpJBN08nKPDC2jd8Ptyjom5UuojMH0dTVe4zgvmcliaxTOnNJcGHLvU8zbZOgzaft9qACibyw/640?wx_fmt=png&from=appmsg "")  
  
  
**01**  
  
**两大关键漏洞构成完整攻击链**  
  
  
谷歌 Project Zero 团队在安全公告中明确指出，这条 0-click 漏洞利用链由两个关键漏洞组成：  
  
  
CVE-2025-54957： 位于 **Dolby Unified Decoder**  
（杜比统一解码器，简称 UDC）组件中。UDC 是一个广泛集成于 Android、iOS、Windows 及流媒体设备的音频解码库。研究发现，该组件在处理 EMDF（可扩展元数据传输格式）负载时存在整数溢出漏洞。当负载大小参数设置为极大值时，会导致内存分配计算出现溢出，使攻击者能够在预期边界之外写入数据。  
  
  
CVE-2025-36934： 存在于 Pixel 设备的 **BigWave 驱动程序**  
中。BigWave 是 Pixel SOC 上用于加速AV1解码任务的硬件组件。审计发现，当 ioctl 等待作业完成超时后，若工作线程仍在处理该作业且文件描述符被关闭，会触发一个 UAF 漏洞，可实现约 2KB 级别的受控内核内存写入，最终获取内核级权限。  
  
  
**02**  
  
**AI功能扩展了零点击攻击面**  
  
  
研究团队指出，这条攻击链之所以能够实现“零点击”，与近年来手机上 AI 功能的爆发式增长密切相关。  
  
  
攻击者巧妙利用了 Google Messages 应用中的音频转录功能。该功能会在用户打开消息之前，自动解码接收到的 SMS 和 RCS 音频附件。这意味着，攻击者只需向目标发送一条包含恶意音频的消息，**无需用户任何交互**  
，恶意代码就会被自动执行。  
  
  
**03**  
  
**影响范围波及整个Android生态**  
  
  
该攻击链中的 CVE-2025-54957 漏洞影响范围十分广泛，并不局限于 Pixel 9 设备。由于 Dolby UDC 组件被以二进制“blob”形式提供给大多数 OEM 厂商，并静态链接到共享库中，该组件已集成到当今大多数 Android 设备中。  
  
  
受影响的范围包括：  
- Google Pixel 9设备（本次研究的目标设备）  
  
- 集成Dolby UDC的大多数Android设备（三星等OEM厂商已陆续修复）  
  
- 集成Dolby UDC的Windows设备和流媒体设备  
  
  
  
  
**04**  
  
**修复延迟敲响生态系统安全警钟**  
  
  
研究团队分析指出，这一事件暴露了 Android 生态系统在漏洞响应协同方面的深层次问题。从漏洞报告到首个 Android 设备获得修复耗时 139 天，且 Pixel 的修复比三星晚了近两个月。  
  
  
此外，ASLR 绕过研究揭示了一个自 2016 年以来就存在的 kASLR 失效问题，此前由于修复优先级较低一直未被彻底解决，这大大降低了本次 BigWave 漏洞的利用难度。  
  
  
Project Zero 建议 Android 及 OEM 厂商：  
- 收缩攻击面：移除不常用的解码器，减少零点击触发点。  
  
- 强化沙箱：在关键安全沙箱中实施更严格的 seccomp 策略。  
  
- 内存安全：使用 Rust 等内存安全语言重写高风险驱动。  
  
- 启用编译器保护：采用 -fbounds-safety 等编译器安全标志编译媒体库。  
  
- 推进硬件保护：为用户启用 MTE（内存标记扩展）功能，并加快补丁推送速度。  
  
  
  
  
  
参考来源：  
  
**A 0-click exploit chain for the Pixel 9 Part 1: Decoding Dolby**  
  
https://projectzero.google/2026/01/pixel-0-click-part-1.html  
  
**A 0-click exploit chain for the Pixel 9 Part 2: Cracking the Sandbox with a Big Wave**  
  
https://projectzero.google/2026/01/pixel-0-click-part-2.html  
  
**A 0-click exploit chain for the Pixel 9 Part 3: Where do we go from here?**  
  
https://projectzero.google/2026/01/pixel-0-click-part-3.html  
  
  
  
“洞”悉网络威胁，守护数字安全  
  
  
**关于我们**  
  
  
360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。  
  
  
