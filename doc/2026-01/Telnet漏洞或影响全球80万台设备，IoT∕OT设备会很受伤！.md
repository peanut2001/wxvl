#  Telnet漏洞或影响全球80万台设备，IoT/OT设备会很受伤！  
 安小圈   2026-01-29 00:45  
  
**安小圈**  
  
  
第846期  
  
![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMBktbWEsll9n00m9KQoFFQnYPRP1dRSHObx4j1kok6vooVTjicyXxkAO7kUbdNKSb6eePhIUg955w/640?wx_fmt=png "")  
  
2026年1月20日以来，网络安全领域接连拉响警报，一个围绕传统Telnet协议的严重漏洞正将全球超过80万台设备置于高危风险之中。安全研究人员、非营利组织及多国网络安全机构发布的数据和分析显示，这不仅是一个简单的端口暴露问题，更涉及一个可导致攻击者直接获取设备最高权限的认证绕过漏洞。  
鉴于可能存在此漏洞的传统设备和嵌入式设备普遍存在，OT（运营技术）环境面临的风险尤为严峻。此外，传统物联网设备和影子物联网设备也构成风险，因为此类设备通常默认启用Telnet功能。  
因此存量IoT/OT设备  
其特性使其正成为攻击的首要目标，一场波及消费领域与关键基础设施的潜在安全危机悄然而至。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUtvfIXIO6LwlTJOthBh95p0R46SbXuM7FfEjY3QXOHZB9ydV8FibFnL4Zzbj9mAFqVd6Zh2ibepOSA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
漏洞影响：从端口暴露到权限失守  
  
综合参考材料，当前围绕Telnet的威胁实际包含两个相互关联的层面，共同推高了风险等级。  
  
**第一层风险：长期存在的暴露与弱口令问题。**  
  
根据Shadowserver基金会持续扫描的数据，目前全球仍有**约80万台设备**  
的Telnet端口（TCP 23）直接暴露在互联网上。这些设备包括企业服务器、网络路由器以及数量庞大的消费级物联网设备。Telnet协议设计于网络早期，其致命缺陷在于**所有通信（包括用户名和密码）均以未加密的明文传输**  
。这使得攻击者可以轻易截获凭证。更严重的是，大量设备在部署后仍使用默认或弱密码，为自动化攻击敞开了大门。Mirai、Persirai和Hajime等僵尸网络恶意软件家族，正是通过持续扫描互联网，利用此类漏洞将设备招募为“肉鸡”，用于发动大规模分布式拒绝服务攻击。  
  
**第二层风险：新曝出的高危认证绕过漏洞（CVE-2026-24061）。**  
  
2026年1月20日，一个更为严重的漏洞被公之于众。该漏洞存在于广泛使用的**GNU InetUtils telnetd服务器软件**  
中，影响自2015年5月发布的1.9.3版至2.7版的所有版本。漏洞本质是**参数注入**  
，源于telnetd未能正确处理用户环境变量。  
  
攻击者可以在Telnet连接协商阶段，发送一个特制的USER  
环境变量，其值为-f root  
（或其他用户名）。由于程序未对参数进行净化处理，-f  
这个本应传递给系统登录进程的选项被恶意利用，导致**服务器完全绕过正常的身份验证流程，自动将攻击者以root身份登录**  
。这意味着，即使设备修改了默认密码，只要运行了受影响版本的telnetd并开启服务，攻击者无需任何凭证即可直接获得最高控制权。  
  
加拿大网络安全中心和美国网络安全与基础设施安全局均已将此漏洞列入已知被利用漏洞目录，并敦促相关机构限期修复，凸显了其严重性。  
## 为何IoT与OT设备成为“重灾区”？  
  
此次危机中，物联网和运营技术设备被视为风险最高的领域，这与其固有的技术特性和运维模式密切相关。  
1. **默认启用与遗留问题**  
：为了方便初始配置和远程维护，Telnet服务在大量传统嵌入式设备和IoT设备上被**默认开启**  
。许多设备在部署后，管理员或因疏忽、或因缺乏安全意识，并未禁用这一不安全服务。此外，大量“影子IoT”设备也可能在不知不觉中运行着Telnet服务。  
  
1. **修补困难与生命周期长**  
：与可频繁更新的服务器和PC不同，许多IoT和OT设备设计为“部署即遗忘”。它们可能缺乏自动更新机制，固件更新需要手动干预，甚至**制造商早已停止提供安全支持**  
。全球技术行业协会指出，制造业、物流和海事等行业风险加剧，部分原因正是其嵌入式系统在部署后从未更新。对于GNU InetUtils telnetd漏洞，修补更为复杂：补丁需要先被集成到各个Linux发行版的软件包中，用户才能方便地更新。在此之前，只能通过修改源代码并自行编译的方式修复，这对普通用户甚至企业管理员来说都门槛极高。  
  
1. **直接暴露于互联网**  
：许多消费级路由器、摄像头等设备直接通过宽带连接互联网，如果未配置正确的防火墙规则，其管理接口（包括Telnet）便可能直接面向全球网络。Shadowserver的数据显示，暴露的设备主要集中在亚洲和南美洲。其中，**中国的暴露情况尤为突出，约有13万台设备位列全球第一**  
，其次为巴西（约11.9万台）、美国（约5万台）、日本（约4.1万台）、墨西哥（约3万台）和印度（约2.7万台）。这一分布反映了全球互联网设备存量、网络架构及安全实践水平的差异。  
  
![该图片无替代文字](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUtvfIXIO6LwlTJOthBh95p2mj95s4ZpSHsEBwBjD2aJ4hrAA2VS2GXFvR9NwNpMzIs5xQsAE5lcg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
1. **对OT环境的极端威胁**  
：网络安全公司Inversion6的CISO伊恩·桑顿-特朗普警告，此漏洞是“寻求在OT系统上持久存在的国家级威胁行为体的绝对礼物”。OT环境中充斥着大量遗留且难以更新的设备，一旦被入侵，攻击者获得的root权限可能直接导致物理进程中断、敏感数据泄露，甚至引发安全事故。  
  
## 威胁已至：攻击活动实录与战术分析  
  
警报并非空穴来风。在漏洞细节公开后不到24小时，针对性的攻击便已开始。安全研究团队发布了一份对约18小时攻击活动的详细分析，为我们提供了观察威胁的微观视角：  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icUtvfIXIO6LwlTJOthBh95pz6BzEiahT6zPicEzFSiaKEQs5ib2lpdI71bxyo7v7kP3kzy0howAuvV2nw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "")  
- **攻击规模与速度**  
：研究人员的蜜罐在短时间内记录了来自**18个独特源IP地址的60次攻击尝试**  
。其中一个蜜罐在**不到60分钟**  
内即被成功入侵。攻击呈现“机会主义扫描”与“针对性利用”相结合的特点。  
  
- **利用手法**  
：所有攻击均尝试利用CVE-2026-24061漏洞。攻击流量严格遵循Telnet协议协商流程，注入恶意的USER=-f root  
（或尝试nobody  
， daemon  
等用户）环境变量以绕过认证。  
  
- **攻击者画像与后续行为**  
：分析发现，攻击者技术水平参差不齐。大部分使用自动化脚本进行扫描和初步入侵。成功获取shell访问后，攻击者的行为包括系统侦察、建立SSH密钥持久化后门、部署僵尸网络或挖矿程序等恶意软件，并立即开始横向扫描更多目标。这些实录证明，漏洞利用链已完全武器化，威胁迫在眉睫。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icUtvfIXIO6LwlTJOthBh95pHb4Lfv859Y08KeXum8sGTBJLG4Kwr2x4AXhQNDbyaGM9aXWA5fe3Kw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
缓解与加固措施  
  
面对如此严峻的威胁，个人用户、企业及组织必须立即采取行动。防御策略应遵循以下层次：  
1. **根本措施：禁用与替换**  
  
1. **立即禁用Telnet服务**  
：这是最有效的方法。在所有非绝对必需的设备上，彻底停止并禁用Telnet服务。  
  
1. **启用加密替代方案**  
：使用**SSH（安全外壳协议）**  
 进行远程管理。SSH提供加密通信，能有效防止凭证窃听和中间人攻击。  
  
1. **紧急缓解：隔离与管控**  
  
1. **严格网络访问控制**  
：如果因特殊原因暂时无法禁用Telnet，必须使用防火墙规则，**将Telnet端口（23）的访问限制在绝对必要的、可信的管理IP地址范围内**  
，严禁将其暴露于互联网。  
  
1. **网络分段**  
：将管理网络、IoT设备网络与核心业务网络进行隔离，防止攻击者横向移动。  
  
1. **漏洞管理：修补与更新**  
  
1. **尽快应用补丁**  
：对于受CVE-2026-24061影响的系统，应尽快升级到已修复的GNU InetUtils版本（2.8及以上），或应用供应商提供的安全补丁。  
  
1. **更新设备固件**  
：为所有IoT和网络设备安装最新的官方固件。  
  
1. **安全实践：审计与监控**  
  
1. **全面资产清查与扫描**  
：使用工具扫描内部网络，识别所有开启Telnet服务的设备，特别是那些未知的“影子IoT”设备。  
  
1. **强化认证**  
：对于任何必须保留的远程访问服务，**立即修改所有默认用户名和密码**  
，使用高强度、唯一的密码。  
  
1. **启用日志与监控**  
：检查防火墙和系统日志，关注对端口23的异常连接尝试和身份验证失败记录。  
  
## 结论  
  
全球80万台设备的暴露与高危认证绕过漏洞的结合，是一次严峻的警告。它揭示了在万物互联时代，**遗留技术安全债务的广泛性与危险性**  
。Telnet这一过时的明文协议，已成为网络安全链条中最脆弱的环节之一。  
  
中国有超过13万台设备暴露，凸显了问题的普遍性与紧迫性。风险不仅在于单个设备被控，更在于其可能成为攻击关键基础设施、扰乱网络秩序的跳板。  
  
防御措施清晰明确：**立即禁用或严格隔离Telnet服务，全面转向SSH等加密协议，并对所有联网设备实施持续的资产管理与漏洞修补**  
。这需要设备制造商、服务提供商、企业及终端用户的共同重视与协作。  
  
  
参考资源  
  
1、  
https://www.ctrlaltnod.com/news/800k-devices-at-risk-open-telnet-ports-invite-cyber-threats/  
  
2、  
https://www.govinfosecurity.com/telnet-flaw-800000-servers-at-risk-amid-active-attacks-a-30604  
  
3、  
https://www.linkedin.com/posts/the-shadowserver-foundation_cybercivildefense-cybersecurity-activity-7421503456991141888-aHv6/  
  
4、  
https://www.cyber.gc.ca/en/alerts-advisories/al26-002-vulnerability-affecting-gnu-inetutils-telnetd-cve-2026-24061  
  
5、  
https://www.cisa.gov/news-events/alerts/2026/01/26/cisa-adds-five-known-exploited-vulnerabilities-catalog  
  
6、  
https://www.labs.greynoise.io/grimoire/2026-01-22-f-around-and-find-out-18-hours-of-unsolicited-houseguests/index.html  
  
  
END  
  
  
  
**【以上内容**  
**来源自：网空闲话plus】**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOugegrykhydnkHibcSWjpibT2K6EwRCniasJ7zopLbBxIz6DUTwPYApdKXaUBXK5sGLSdSdKb9rBZNg/640?wx_fmt=jpeg "")  
![](https://mmbiz.qpic.cn/mmbiz_gif/0YKrGhCM6DbI5sicoDspb3HUwMHQe6dGezfswja0iaLicSyzCoK5KITRFqkPyKJibbhkNOlZ3VpQVxZJcfKQvwqNLg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550839&idx=1&sn=41654142b38ee39e63d341d0117ef036&scene=21#wechat_redirect)  
  
[某国产操作系统资深开发者，因不穿西装被开除](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550839&idx=1&sn=41654142b38ee39e63d341d0117ef036&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550771&idx=1&sn=b106bb0574435dd5698a74aa50938488&scene=21#wechat_redirect)  
  
  
[看完本文再也不怕网安通报“明文传输” “TLS版本低”漏洞了](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550771&idx=1&sn=b106bb0574435dd5698a74aa50938488&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550766&idx=1&sn=823d3fdd86bc69edcd337e03d89768eb&scene=21#wechat_redirect)  
**两名网络安全专家利用勒索软件攻击企业 委托自己联系自己谈赎金**  
****  
**聊一聊网络安全公司的内部争斗国家出手！网络安全产业低价中标乱象能否终结？ 网络安全行业还会好起来吗?**  
  
**《网络安全法》完成修改，自2026年1月1日起施行网络安全法修改了哪些内容？（附详细对照表）全球三大网络安全巨头同时被黑网安：亏损 TOP 10中国联通DNS故障敲响警钟：DNS安全刻不容缓全球超120万个医疗系统公网暴露：患者数据或遭窃取 中国亦受影响个人信息保护负责人信息报送系统填报说明（第一版）全文高度警惕：不明黑客组织攻击中国国防、能源、航空、医疗、网安等重点行业攻防演练在即：如何开展网络安全应急响应【攻防演练】中钓鱼全流程梳理[一文详解]网络安全【攻防演练】中的防御规划与实施攻防必备 | 10款国产“两高一弱”专项解决方案【干货】2024 攻防演练 · 期间 | 需关注的高危漏洞清单攻防演练在即，10个物理安全问题不容忽视红队视角！2024 | 国家级攻防演练100+必修高危漏洞合集(可下载)【攻防演练】中钓鱼全流程梳理攻防演练在即：如何开展网络安全应急响应【零信任】落地的理想应用场景：攻防演练网安同行们，你们焦虑了吗？网安公司最后那点体面，还剩下多少？突发！数万台 Windows 蓝屏。。。。广联达。。。惹的祸。。。权威解答 | 国家网信办就：【数据出境】安全管理相关问题进行答复全国首位！上海通过数据出境安全评估91个，合同备案443个沈传宁：落实《网络数据安全管理条例》，提升全员数据安全意识频繁跳槽，只为投毒【2025】常见的网络安全服务大全（汇总详解）AI 安全 |《人工智能安全标准体系(V1.0)》(征求意见稿)，附下载**  
  
