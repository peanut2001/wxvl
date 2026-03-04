#  谷歌披露iOS漏洞攻击套件Coruna，数千iPhone用户面临威胁  
看雪学苑
                    看雪学苑  看雪学苑   2026-03-04 09:59  
  
近日，谷歌威胁情报集团（GTIG）披露了一个  
名为Coruna的尖端iOS攻击工具包，  
这个堪称“漏洞军火库”的框架，在2025年间席卷了  
从iOS 13.0到17.2.1几乎横跨四年的所有主流版本。  
  
  
不是单一漏洞，而是“连环计”  
  
Coruna的可怕之处，在于它并非依靠某个单一的漏洞攻破防线，而是  
构建了五条完整的漏洞利用链条，包含了整整23个独立漏洞。  
从浏览器入口到内核控制，每一步都踩在系统安全的痛点上。  
  
  
根据曝光的信息，这套工具包的攻击链  
覆盖了从WebContent读写、沙盒逃逸、权限提升到PPL（页面保护层）绕过等几乎所有环节。  
部分漏洞代码甚至留下了专业的英文注释，显示出其背后开发团队具备国家级的技术储备。  
  
  
其中，Photon和Gallium这两个漏洞组件，更是曾在2023年卡巴斯基曝光的“三角测量行动”中出现过。这意味着，Coruna的开发者很可能在吸收并整合了过往最顶级的攻击技术。  
  
  
一条漏洞链的“三重人生”  
  
谷歌的追踪记录显示，Coruna在短短一年内经历了三个截然不同的“宿主”，完整地勾勒出一条尖端武器从商业公司流向犯罪集团的路径。  
  
  
第一阶段：商业监控（2025年初）  
  
研究人员首次捕获到Coruna的踪迹时，它被包裹在一个高度混淆的JavaScript框架内。这套框架能精准识别iPhone型号和iOS版本，然后动态加载对应的WebKit远程执行漏洞。这是典型的商业监控公司的操作模式——按需定制，精准打击。  
  
  
第二阶段：地缘政治间谍（2025年夏）  
  
很快，这套完全相同的代码框架出现在了一个名为 `uacounter[.]com` 的域名上，并被以隐藏iframe的形式，植入了数十家乌克兰的工业、零售网站。当特定地理位置的iPhone用户访问这些网站时，攻击便会悄然触发。这一次，它的身份是国家背景的间谍组织（UNC6353）。  
  
  
第三阶段：加密货币大盗（2025年底）  
  
到了年末，Coruna的完整工具包又浮现在一个庞大的虚假中国金融和加密货币网站网络中。攻击者搭建了假冒的WEEX交易所等平台，诱导iPhone用户访问。此时，它的目的已从间谍活动，转向了赤裸裸的金融掠夺。  
  
  
直奔你的加密钱包  
  
在攻破系统最后一道防线后，一个名为PlasmaLoader的植入器会注入到系统级的 `powerd` 进程中，伪装成 `com.apple.assistd` 服务，实现长期驻留。  
  
  
它的目标非常明确：18款主流加密货币钱包，包括MetaMask、BitKeep、Phantom等。恶意软件通过钩子函数，直接窃取用户的钱包数据。  
  
  
更可怕的是，它还会  
扫描苹果自带的备忘录，从中寻找BIP39助记词、以及诸如“备份短语”、“银行账户”等关键词。  
对于习惯将重要信息记在备忘录里的用户来说，这无异于将自己的金库钥匙拱手送人。  
  
  
所有被盗数据会通过HTTPS加密外传，其通信代码中包含了中文字符串注释，以及疑似由大语言模型生成的代码结构。  
  
  
该怎么办？  
  
好消息是，Coruna的攻击链  
对最新的iOS版本已经无效  
。这意味着，只要  
及时更新，  
就能有效封堵这些已知漏洞。  
  
  
立即行动：  
  
1.  立刻更新：将你的iPhone升级到最新版本，这是最简单也最有效的防御手段。  
  
2.  开启“锁定模式”：如果因特殊原因无法更新，请务必开启iPhone的“锁定模式”。Coruna在检测到该模式时会主动停止攻击。  
  
3.  警惕陌生网站：避免通过手机Safari访问不明来历的金融、加密货币交易或促销网站。  
  
4.  检查异常流量：留意手机是否有向陌生的 `.xyz` 域名发起的网络请求，或是否捕获到含有 `sdkv`、`x-ts` 等特殊字段的HTTP流量。  
  
  
资讯来源：本文内容综合编译自谷歌威胁情报集团（GTIG）发布的关于Coruna攻击套件的技术报告及相关网络安全媒体分析。  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
