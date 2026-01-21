#  iOS 和 iPadOS 的新漏洞使数百万部 iPhone 面临风险  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-01-21 01:04  
  
**导****读**  
  
  
  
iOS   
和  
iPadOS   
的  
 WebKit   
存在严重漏洞，可能导致数百万台  
 iPhone   
和  
 iPad   
被悄无声息地控制。苹果敦促用户立即更新。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaHtrzQIySgMxEiaiamfLk9ISn2n0aBmSyh4BHICHkSMVlibuZ3N870pM2b700kicnOwhMSjQ0oAhkbWdw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
无需点击。无需警告。完全设备访问权限。  
  
  
苹果公司确认两个影响数百万部 iPhone 和 iPad 的严重 WebKit 漏洞。利用 CVE-2025-43529 和 CVE-2025-14174 漏洞，攻击者可以获得设备的完全访问权限，包括密码和财务数据。  
  
  
根据这份 iOS 和 iPadOS安全文档，这两个漏洞都源于 WebKit 的两个漏洞，攻击者可以利用这些漏洞在 Safari 中执行恶意代码，从而进一步访问设备。  
  
  
利用过程如下：  
- 攻击者将恶意代码隐藏在被入侵的网页中。  
- 页面加载时，WebKit 内存处理不当。  
- 该漏洞允许恶意代码在浏览器中运行。  
- 第二个漏洞可以实现更深层次的访问权限，从而暴露设备数据。  
这种漏洞被称为“零点击漏洞”，无需用户任何操作即可触发。如果同时存在这两种漏洞，用户只需访问一个网站就可能发生安全漏洞。  
  
  
Hacker News 报道称，在苹果发现并修复这些漏洞之前，它们都是已经广泛传播的  
0day  
漏洞。该修复程序已包含在 iOS 26.2 中，因此大多数旧款 iPhone 和 iPad 无法获得更新。  
  
  
苹果公司敦促所有用户升级系统，尤其是以下设备的用户：  
- iPhone 11 及更新机型。  
- iPad Pro 12.9  英寸，第三代及更新机型。  
- iPad Pro 11 英寸，第一代及更新机型。  
- iPad Air，第三代及更新机型。  
- iPad，第八代及更新机型。  
- iPad mini，第五代及更新机型。  
据福克斯新闻报道，这份清单上的设备类别比其他设备类别更容易受到攻击。  
  
  
苹果还发布了 iOS 18.7.3 来解决 iPhone XS、XS Max 和 XR 上的这两个 WebKit 漏洞，以及适用于 iPad（第七代）的 iPadOS 18.7.3。  
  
  
福克斯新闻援引的研究表明，攻击者正针对特定个人。这些个人的身份尚未公开。类似的定向网络攻击表明，政治人物和公众人物很可能是攻击目标。  
  
  
对许多苹果用户来说，设备更新似乎只是增加了一些外观设计和动画效果；然而，其真正的价值在于核心安全修复。设备更新对于安全至关重要，能够保护用户免受漏洞的侵害，例如那些被自动利用的漏洞。  
  
  
新闻链接：  
  
https://www.techrepublic.com/article/news-ios-ipad-os-flaws-iphones-at-risk/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
