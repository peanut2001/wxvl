#  Chrome Gemini漏洞：可致攻击者远程访问用户摄像头和麦克风  
 安小圈   2026-03-06 00:45  
  
**安小圈**  
  
  
第867期  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lwbGZupmpjfahxah5Qgb7toJLsONJiaHAS7VFqHx1z4xt9WPm3za8jum3eLb1VZPTL7Sqwrtfl7IdxLMicrmc05Xfrv0ZcwrdrI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
**高危漏洞曝光**  
  
谷歌Chrome浏览器内置的Gemini AI助手被发现存在一个高危安全漏洞（CVE-2026-0628），攻击者无需用户任何额外操作，仅需用户启动浏览器内置的AI面板，即可实现未经授权的摄像头和麦克风访问、本地文件窃取以及钓鱼攻击。  
  
该漏洞由Palo Alto Networks旗下Unit 42的研究人员发现，并于2025年10月23日向谷歌报告。谷歌确认问题后于2026年1月5日发布补丁。  
  
**特权架构扩大攻击面**  
  
Chrome中的Gemini Live功能属于"AI浏览器"这一新兴类别，这类浏览器将AI助手直接嵌入浏览环境。这些AI助手（包括Edge中的Microsoft Copilot以及Atlas和Comet等独立产品）作为特权侧边栏运行，能够实现实时网页摘要、任务自动化和上下文浏览辅助。  
  
由于这些AI面板需要"多模态"视图才能有效运行，Chrome授予Gemini面板提升的权限，包括访问摄像头、麦克风、本地文件和屏幕截图能力。这种特权架构虽然实现了强大功能，但也显著扩大了浏览器的攻击面。  
  
**漏洞技术细节**  
  
漏洞存在于Chrome处理declarativeNetRequest API的方式中，这是一个标准的浏览器扩展权限，允许扩展拦截和修改HTTPS网络请求和响应。该API广泛用于广告拦截等合法用途。  
  
研究人员发现，Chrome处理hxxps[:]//gemini.google[.]com/app请求时存在关键差异：当该URL在普通浏览器标签页中加载时，扩展可以拦截并向其注入JavaScript，但这不会授予任何特殊权限；而当同一URL在Gemini浏览器面板中加载时，Chrome会以提升的浏览器级权限处理它。  
  
利用这种不一致性，仅具有基本权限的恶意扩展即可向特权Gemini面板注入任意JavaScript代码，从而劫持受信任的浏览器组件并继承其所有提升的访问权限。  
  
**攻击能力与影响**  
  
攻击者通过此技术控制Gemini面板后，仅需受害者点击Gemini按钮即可执行以下操作，无需任何其他用户交互：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9lpJS2UwHjFViciaoY67QTNRic0BLyNd4k7wLbtAum7m3EGy6pmjTT274xv3ZpaaFibONKw8N2PHtibYI1rOE0SDdzDNic5slLooTAVk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
钓鱼攻击风险尤为危险，因为Gemini面板是受信任的浏览器集成组件。其中显示的恶意内容具有独立钓鱼页面所缺乏的固有可信度。  
  
**企业安全风险加剧**  
  
在企业环境中，被入侵的扩展获取员工摄像头、麦克风和本地文件访问权限会带来严重的组织安全风险，可能导致企业间谍活动和数据外泄。  
  
谷歌已于2026年1月5日发布修复补丁。运行最新版Chrome的用户已受到保护。各组织应立即确保所有终端上的Chrome浏览器完成更新。  
  
  
END  
  
  
  
**【以上内容**  
**来源自：e安在线】**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOugegrykhydnkHibcSWjpibT2K6EwRCniasJ7zopLbBxIz6DUTwPYApdKXaUBXK5sGLSdSdKb9rBZNg/640?wx_fmt=jpeg "")  
![](https://mmbiz.qpic.cn/mmbiz_gif/0YKrGhCM6DbI5sicoDspb3HUwMHQe6dGezfswja0iaLicSyzCoK5KITRFqkPyKJibbhkNOlZ3VpQVxZJcfKQvwqNLg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
[Claude Code Security 技术原理全拆解，传统安全扫描工具真扛不住了？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247551742&idx=2&sn=8dd0ca0d0a49131c7bc558bfe52d145e&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247551205&idx=1&sn=07d4be96cce4a42fb01d1aa4d78b9a35&scene=21#wechat_redirect)  
  
[网络安全行业，25家网安上市企业业绩预告分析](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247551205&idx=1&sn=07d4be96cce4a42fb01d1aa4d78b9a35&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550839&idx=1&sn=41654142b38ee39e63d341d0117ef036&scene=21#wechat_redirect)  
  
[某国产操作系统资深开发者，因不穿西装被开除](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550839&idx=1&sn=41654142b38ee39e63d341d0117ef036&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550771&idx=1&sn=b106bb0574435dd5698a74aa50938488&scene=21#wechat_redirect)  
  
  
[看完本文再也不怕网安通报“明文传输” “TLS版本低”漏洞了](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550771&idx=1&sn=b106bb0574435dd5698a74aa50938488&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247550766&idx=1&sn=823d3fdd86bc69edcd337e03d89768eb&scene=21#wechat_redirect)  
**两名网络安全专家利用勒索软件攻击企业 委托自己联系自己谈赎金**  
****  
**聊一聊网络安全公司的内部争斗国家出手！网络安全产业低价中标乱象能否终结？ 网络安全行业还会好起来吗?**  
  
**《网络安全法》完成修改，自2026年1月1日起施行网络安全法修改了哪些内容？（附详细对照表）全球三大网络安全巨头同时被黑网安：亏损 TOP 10中国联通DNS故障敲响警钟：DNS安全刻不容缓全球超120万个医疗系统公网暴露：患者数据或遭窃取 中国亦受影响个人信息保护负责人信息报送系统填报说明（第一版）全文高度警惕：不明黑客组织攻击中国国防、能源、航空、医疗、网安等重点行业攻防演练在即：如何开展网络安全应急响应【攻防演练】中钓鱼全流程梳理[一文详解]网络安全【攻防演练】中的防御规划与实施攻防必备 | 10款国产“两高一弱”专项解决方案【干货】2024 攻防演练 · 期间 | 需关注的高危漏洞清单攻防演练在即，10个物理安全问题不容忽视红队视角！2024 | 国家级攻防演练100+必修高危漏洞合集(可下载)【攻防演练】中钓鱼全流程梳理攻防演练在即：如何开展网络安全应急响应【零信任】落地的理想应用场景：攻防演练网安同行们，你们焦虑了吗？网安公司最后那点体面，还剩下多少？突发！数万台 Windows 蓝屏。。。。广联达。。。惹的祸。。。权威解答 | 国家网信办就：【数据出境】安全管理相关问题进行答复全国首位！上海通过数据出境安全评估91个，合同备案443个沈传宁：落实《网络数据安全管理条例》，提升全员数据安全意识频繁跳槽，只为投毒【2025】常见的网络安全服务大全（汇总详解）AI 安全 |《人工智能安全标准体系(V1.0)》(征求意见稿)，附下载**  
  
