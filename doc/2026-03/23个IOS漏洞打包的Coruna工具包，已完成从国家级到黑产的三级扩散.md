#  23个IOS漏洞打包的Coruna工具包，已完成从国家级到黑产的三级扩散  
 利刃信安   2026-03-04 23:36  
  
本报告整合谷歌威胁情报小组（GTIG）与 iVerify 安全团队对**Coruna**  
 iOS漏洞利用工具包的独立研究成果，完整还原该工具包的技术架构、攻击链全流程、漏洞利用矩阵、扩散路径与恶意行为特征。  
  
Coruna 是一款具备国家级攻击能力的 iOS 漏洞利用工具包，内部代号亦被称为 CryptoWaters，  
包含**5 条完整的漏洞利用链、共计 23 个漏洞利用程序**  
，可覆盖攻击 iOS 13.0（2019 年 9 月发布）至 iOS 17.2.1（2024 年 1 月发布）的全系列 iPhone 设备，同时兼容 arm64 与 arm64e 架构。  
  
该工具包是移动安全领域高复杂度攻击能力扩散的典型案例：  
  
其最初由商业监控厂商的客户用于定向攻击，随后被国家级背景的威胁组织用于地缘政治相关攻击，最终扩散至网络犯罪团伙手中，被用于针对普通用户的大规模加密货币窃取攻击。  
  
关于该工具包可能来自美国政府开发的说法，目前持保留意见，当然最准确的说法便是：  
与 Coruna 工具包本身相比，这些后续新增的窃取数据的代码“编写得非常糟糕”。Coruna 工具包本身设计精良，模块化程度高。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoovXHaP6UbMwufXw2TNYAoyZQFkYa3fjIsNiboHTFmGHVSvycCIMqo9zmKEEDlmwmwbEjH2lhvZLofPx7mAKES8GSib4NBkWVmM/640?wx_fmt=png&from=appmsg "")  
  
这一扩散路径印证了商业间谍软件能力向黑灰产领域快速流转的行业风险，也标志着曾经仅用于针对高价值目标的攻击工具，  
已成为威胁普通 iOS 用户安全的常态化风险。  
  
Coruna 工具包的攻击活动呈现清晰的三级扩散特征，从定向高价值攻击逐步演变为大规模无差别攻击，完整时间线与攻击主体如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqmLGiaUSQe4ZYEwdWpQoZ4S8ZQU0nALdwQqnG3reibSRq7szTRlsfwWQ5L9dp599G9OKzk6WtmM4oH7CT9ckzWWPKnrtoib38rP0/640?wx_fmt=png&from=appmsg "")  
  
2024 年 1 月 22 日，苹果在 iOS 17.3 版本中修复了 WebKit 远程代码执行漏洞 CVE-2024-23222，未提及该漏洞已在野被利用。  
  
2025 年 2 月，GTIG 首次截获一家商业监控公司客户使用的 iOS 漏洞利用链部分代码，该代码被集成到一个具备独特混淆技术的 JavaScript 框架中，这是 Coruna 工具包的首次野外捕获。  
  
同期，iVerify 团队也监测到该框架的野外活动，内部将其命名为 CryptoWaters。  
  
该阶段的攻击具备强定向性，攻击者通过框架内置的指纹识别模块，仅对匹配目标特征的设备投放漏洞利用程序，核心利用的漏洞包括 CVE-2024-23222，同时配套了完整的 PAC 绕过与权限提升能力。  
  
2025 年夏季，GTIG 与 CERT-UA 联合监测到，  
疑似俄罗斯背景的间谍组织 UNC6353 将 Coruna 工具包用于针对乌克兰用户的水坑攻击。  
攻击者入侵了乌克兰大量工业设备、零售服务、本地电商相关网站，在页面中植入隐藏 iFrame 加载恶意框架cdn.uacounter[.]com/stat[.]html  
，仅对乌克兰境内的特定 iPhone 用户推送漏洞利用程序。  
  
在此阶段，研究人员捕获到该工具包新增的多个 WebKit 漏洞利用程序，包括 CVE-2022-48503、CVE-2023-43000，形成了覆盖更多 iOS 版本的完整利用链，工具包的模块化架构已完全成熟。  
  
2025 年底至 2026 年初，GTIG 与 iVerify 团队均在全球范围内发现大量虚假金融、加密货币相关网站中，存在 Coruna 工具包的大规模滥用，相关攻击由以经济利益为目标的威胁组织 UNC6691 主导。  
  
这类恶意网站通常伪装成加密货币交易所、空投活动页面，页面中明确标注   
“本页面仅适配 iOS 设备，请使用 iPhone 或 iPad 访问  
”，诱导 iOS 用户访问。无论用户地理位置如何，只要使用存在漏洞的 iOS 设备访问，页面就会注入隐藏 iFrame，无差别投放 Coruna 漏洞利用工具包。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpzP9YTps73Mkq3aicXDOdWTIPa0ekR2IcvkGlianSyGCI2OQrDaq7vRvx7BO81fjMKKzOzlKGLicZj5mmrUAnNthWIokted82Hu8/640?wx_fmt=png&from=appmsg "")  
  
在此阶段，研究人员获取了 Coruna 工具包的完整样本、调试版本与最终恶意载荷，确认了其内部代号为 Coruna，同时捕获到数百个相关恶意样本，完整还原了 5 条全版本覆盖的漏洞利用链。iVerify 团队也通过独立分析，发现了该工具包的完整分发基础设施、载荷模块与攻击痕迹，与 GTIG 的研究成果形成相互印证与补充。  
  
Coruna 工具包采用高度模块化的设计架构，各攻击组件解耦且可灵活适配不同 iOS 版本，完整攻击链分为 8 个核心阶段，全流程无需用户交互，属于典型的 “一键式” 无文件攻击。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDo06cPQLFe5F49T2aVDTwickQGBXMZPhrv3fuE8QwY9w6AxEN3K3Yth34HibwNVV1mZuBvOicEwIE2XYCwY5Ilic7tWJSUJf5cqIqA/640?wx_fmt=png&from=appmsg "")  
### （一）初始访问：水坑投放与恶意页面加载  
  
攻击者通过入侵正规网站植入 iFrame、搭建虚假钓鱼网站两种方式，实现初始访问投放。核心恶意入口为 HTML 加载器页面（典型路径为/static/analytics.html  
、/group.html  
），当用户使用 Safari 浏览器访问该页面时，自动触发后续攻击流程。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDogan9XDSvpia18WoicWicQkbxeC8eR6QZiayiaOeoKhYZI1vxwqlBiaX7aaZpvoyHVPBufd8IV8MUeF0s39ugf1V9yRodhm5A5SPTGI/640?wx_fmt=png&from=appmsg "")  
  
该工具包无定向访问限制，任何使用存在漏洞的 iOS 版本设备访问恶意页面，均可被重复感染，这一特征与传统国家级定向攻击完全不同，更符合网络犯罪团伙的大规模攻击需求。  
### （二）环境指纹校验：攻击前置筛选  
  
恶意页面加载后，首先执行 JavaScript 指纹识别模块，对目标环境进行多轮校验，仅当匹配目标环境时才会继续执行漏洞利用，规避分析环境与安全设备：  
1. **系统与浏览器校验**  
确认设备运行 iOS 系统、使用 Safari 浏览器，校验Navigator.platform  
、navigator.userAgent  
、WebSQL 支持等特征；  
  
1. **安全模式校验**  
检测设备是否开启锁定模式（LockdownMode）、是否处于隐私浏览模式，若开启则直接退出攻击流程；  
  
1. **虚拟环境校验**  
检测是否处于 Corellium 等 iOS 虚拟化分析环境，通过检查/usr/libexec/corelliumd  
文件是否存在实现；  
  
1. **版本匹配校验**  
采集设备 iOS 版本、芯片架构信息，匹配对应的漏洞利用链。  
  
  
### （三）WebKit 远程代码执行（RCE）：初始突破  
  
根据目标设备的 iOS 版本，框架自动加载对应的 WebKit RCE 漏洞利用程序，实现 Safari WebContent 进程内的任意代码执行。该工具包为每个 iOS 大版本配套了专属的 WebKit 读写漏洞利用程序，覆盖 iOS 13 至 17.2.1 全版本。  
  
该阶段的漏洞利用代码采用独特的 JavaScript 混淆技术，通过异或编码的方式对字符串、整数进行加密，仅在运行时动态解码，规避静态检测。同时，漏洞利用程序内置了完整的异常处理机制，若利用失败会自动清理崩溃日志，避免留下攻击痕迹。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqL7mqDuh1hDdQkoACgUyjsEQszcgk23F3Nw8daCIp9zTp49B7vCQnKEzjoJ2PticLNMMv4XPEVGIialbWgd2vdxk3Hjicvib5NJ3Q/640?wx_fmt=png&from=appmsg "")  
### （四）PAC 绕过与沙盒逃逸：突破缓解机制  
  
完成 WebKit RCE 后，工具包自动加载对应版本的 PAC（指针认证码）绕过模块，突破苹果的用户态代码签名缓解机制，实现原生代码的稳定执行。针对不同 iOS 版本，工具包配套了 6 个专属的 PAC 绕过模块，适配 iOS 13 至 17.2.1 的不同缓解策略。  
  
随后，工具包通过沙盒逃逸漏洞，突破 WebContent 进程的沙盒限制，获取系统层面的访问权限，为后续的本地权限提升做准备。  
### （五）本地权限提升（LPE）：获取 Root 权限  
  
该阶段工具包加载内核漏洞利用程序，实现本地权限提升，从普通用户权限突破至 iOS 系统 Root 权限。同时，配套对应的 PPL（页面保护级别）绕过模块，突破苹果内核级的内存保护机制，实现对内核的稳定控制。  
  
在权限提升过程中，工具包会主动扫描并清理过往攻击失败留下的崩溃日志，重点清理com.apple.WebKit.WebContent  
、powerd  
、panic  
相关的崩溃记录，进一步提升攻击隐蔽性。  
### （六）多阶段植入程序加载：权限持久化  
  
完成权限提升后，工具包按顺序加载三级植入程序，实现攻击能力的持久化与模块化扩展，全流程通过注入系统原生进程实现，无独立恶意进程，规避常规进程检测：  
1. **第二阶段植入程序**  
将SamplePayload.dylib  
注入以 Root 权限运行的powerd  
系统进程，该阶段主要负责与 C2 服务器建立初始通信，获取攻击配置文件，同时加载第三阶段核心载荷；  
  
1. **第三阶段核心载荷**  
将CorePayload.dylib  
注入locationd  
系统进程，该模块是整个工具包的核心调度中心，内部代号为 PLASMAGRID，负责 C2 通信、模块管理、数据窃取与热更新；  
  
1. **基础功能模块注入**  
CorePayload 会默认向imagent  
进程注入短信通信模块（sms.js）、向SpringBoard  
进程注入桌面交互模块（helion.js），接管 C2 通信备用通道，实现与系统的深度交互。  
  
  
### （七）功能模块动态加载：定向恶意行为  
  
CorePayload 会从 C2 服务器获取配置文件，扫描目标设备上安装的应用，动态加载对应的恶意功能模块。所有模块均为未签名的 dylib 格式，通过进程注入的方式加载到目标应用中，无需修改应用本身。  
  
模块加载完成后，工具包会建立完整的 C2 通信体系：主通信通道由imagent  
模块接管，与 C2 服务器建立定期心跳通信；  
  
预留 SMS/iMessage 备用通信通道，当主域名无法访问时启用；  
  
同时内置了自定义域名生成算法（DGA），以字符串 “  
lazarus  
” 为种子，生成 15 位字符、.xyz 为后缀的备用域名，使用谷歌公共 DNS 解析验证域名可用性。  
### （八）数据窃取与回传：最终攻击目标  
  
Coruna 工具包的核心攻击目标为窃取加密货币相关的敏感信息，同时具备全设备数据窃取能力，核心恶意功能包括：  
1. 扫描并窃取设备中 20 余款主流加密货币钱包的助记词、私钥、账户信息，包括 MetaMask、imToken、Trust Wallet、TokenPocket 等；  
  
1. 读取并上传设备相册中的所有照片、图片，扫描图片中的二维码并解码，提取加密货币地址、私钥等信息；  
  
1. 读取苹果备忘录全量内容，通过关键词匹配（BIP39 词表、“备份短语”、“银行账户” 等）提取敏感信息并上传；  
  
1. 劫持 WhatsApp 等社交应用的通信数据，窃取聊天记录中的敏感信息；  
  
1. 实时采集设备状态信息，包括系统版本、应用列表、网络环境等，定期回传至 C2 服务器。  
  
##   
  
Coruna 工具包包含 23 个漏洞利用程序，覆盖 WebKit RCE、PAC 绕过、沙盒逃逸、内核权限提升、PPL 绕过全攻击环节，形成了 iOS 13 至 17.2.1 全版本覆盖的完整利用矩阵。  
  
核心漏洞详情如下表所示：  
<table><thead><tr><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">漏洞类型</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">内部代号</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">目标 iOS 版本（含）</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">修复版本</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">关联 CVE 编号</span></span></section></th></tr></thead><tbody><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 读写（RCE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">buffout</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">13 → 15.1.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2021-30952</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 读写（RCE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">jacurutu</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.2 → 15.5</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2022-48503</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 读写（RCE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">bluebird</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.6 → 16.1.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 读写（RCE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">terrorbird</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.2 → 16.5.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2023-43000</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 读写（RCE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">cassowary</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.6 → 17.2.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.7.5、17.3</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2024-23222</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent PAC 绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">breezy</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">13 → 14.x</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">-</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent PAC 绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">breezy15</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15 → 16.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">-</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent PAC 绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">seedbell</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.3 → 16.5.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">-</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent PAC 绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">seedbell_16_6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.6 → 16.7.12</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">-</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent PAC 绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">seedbell_17</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17 → 17.2.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">-</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 沙盒逃逸</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">IronLoader</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.0 → 16.3.1、16.4.0（≤A12）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.7.8、16.5</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2023-32409</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">WebContent 沙盒逃逸</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">NeuronLoader</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.4.0 → 16.6.1（A13-A16）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17.0</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（PE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Neutron</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">13.X</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2020-27932</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（信息泄露）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Dynamo</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">13.X</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.2</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2020-27950</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（PE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Pendulum</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14 → 14.4.x</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.7</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（PE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Photon</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.5 → 15.7.6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.7.7、16.5.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2023-32434</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（PE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Parallax</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.4 → 16.7</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17.0</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2023-41974</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">权限提升（PE）</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Gruber</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.2 → 17.2.1</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.7.6、17.3</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面保护层（PPL）绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Quark</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">13.X</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.5</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面保护层（PPL）绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Gallium</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">14.x</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.7.8、16.6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2023-38606</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面保护层（PPL）绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Carbone</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">15.0 → 16.7.6</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17.0</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无 CVE</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面保护层（PPL）绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Sparrow</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17.0 → 17.3</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.7.6、17.4</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2024-23225</span></span></section></td></tr><tr><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面保护层（PPL）绕过</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">Rocket</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">17.1 → 17.4</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">16.7.8、17.5</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2024-23296</span></span></section></td></tr></tbody></table>  
  
**工具包为每个 iOS 大版本配套了专属的漏洞利用链，可适配 2019 年以来发布的几乎所有 iPhone 设备与 iOS 版本，攻击覆盖范围远超常规野利用工具；**  
  
**内置了可复用的缓解绕过模块，例如**rwx_allocator  
模块可通过多种技术绕过内存保护机制，实现用户空间可读写可执行内存页的分配；内核漏洞利用程序内置了内核模式 PAC 绕过模块，可稳定突破苹果最新的内核安全缓解措施；  
  
工具包复用了曾被用于 “三角行动”（Operation Triangulation）的 Photon、Gallium 相关漏洞，证明高级威胁组织之间存在漏洞利用技术的流转与复用，同时也反映出未及时升级系统的设备面临的长期风险；  
  
研究人员捕获的样本显示，该工具包仍处于活跃开发状态，  
攻击者持续新增模块、优化漏洞利用稳定性，同时适配更多的目标应用与 iOS 版本。  
  
Coruna 工具包的攻击流程会在设备、网络、日志中留下大量可检测的痕迹，以下为多维度的检测方法与完整失陷指标。  
### （一）多维度感染检测方法  
#### 1. 网络流量检测  
  
可通过以下网络特征检测攻击活动：  
- 检测powerd  
、imagent  
、locationd  
等系统进程发起的异常 HTTP/HTTPS 请求，尤其是使用非系统默认的用户代理（User Agent）；  
  
- 检测以下固定静态用户代理的网络请求，该 UA 与设备实际 iOS 版本无关，是 Coruna 植入程序的核心特征：  
  
Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1  
- 检测进程名 + 版本格式的异常 UA，例如imagent/{version} CFNetwork/{version} Darwin/{version}  
，该类 UA 正常情况下不会由对应系统进程发起；  
  
- 检测设备访问本文中披露的恶意域名、漏洞利用页面路径的网络流量。  
  
#### 2. 进程与线程检测  
  
该工具包无独立恶意进程，但会在注入的系统进程中创建带有固定特征的恶意线程与调度队列，可通过系统诊断日志检测：  
- 恶意线程特征名：plasma_supervisor  
、plasma_core_heartbeat_receiver  
、plasma_unified_dispatcher  
、helion_ipc_handler  
等；  
  
- 恶意调度队列特征名：com.plasma.heartbeat.callback  
、com.plasma.photomonitor  
、com.plasma.notes.monitor  
、com.plasma.appruntime.downloadmanager  
等。  
  
以上特征可在 iOS 的 sysdiagnose 系统诊断日志、stacks.ips 堆栈日志、崩溃日志中检测到。  
#### 3. 系统日志检测  
  
设备的统一日志（UnifiedLogs）中会留存明确的感染痕迹，核心检测特征包括：  
  
failed lookup: name = com.plasma.springboard.ipc, flags = 0x1, requestor = locationd[69], error = 3: No such process  
  
同时，com.apple.WebKit.Networking  
、powerd  
、imagent  
进程输出的 TLS 配置相关格式字符串日志，且日志中包含恶意域名，也是核心感染特征。  
#### 4. 文件痕迹检测  
  
可通过以下文件路径检测设备是否被感染：  
- 持久化文件：  
  
/private/var/mobile/Library/Preferences/com.apple.photolibraryd.plist  
（iOS 系统正常情况下不会生成该文件）、/private/var/mobile/Library/Caches/.com.apple.notes.cache.plist  
；  
  
- 临时文件：  
  
/private/var/tmp/pl.sp.exec.guard.lock  
、/private/var/tmp/pl.core.lock  
（设备重启后会被删除，需实时检测）；  
  
- Safari 浏览器历史记录中留存的恶意访问 URL、恶意域名相关的资源加载记录，可从设备加密备份中提取检测。  
  
  
### 用户防护建议  
###   
1. **立即升级 iOS 系统至最新版本**  
Coruna 工具包的所有漏洞均已在最新版 iOS 系统中修复，升级至 iOS 17.5 及以上版本可完全规避该工具包的攻击，这是最核心、最有效的防护措施；  
  
1. **启用 iOS 锁定模式（LockdownMode）**  
若暂时无法升级系统，可在 iPhone 设置中开启锁定模式，该模式会大幅限制 Safari 浏览器的高级功能，可直接阻断 Coruna 工具包的初始 RCE 攻击；  
  
1. **谨慎访问未知链接与网站**  
避免访问非正规的加密货币相关网站、陌生空投活动页面，不点击短信、社交软件中的未知链接，降低接触水坑攻击的风险；  
  
1. **定期进行安全检测**  
可使用黑鸟手机安全检测工具对设备进行安全扫描，检查是否存在 Coruna 感染痕迹；定期查看设备的系统诊断日志与网络流量，发现异常行为及时处置。  
  
IOC信息与检测规则可自行前往来源技术报告获取：  
  
https://iverify.io/blog/coruna-inside-the-nation-state-grade-ios-exploit-kit-we-ve-been-tracking  
  
https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit  
  
  
Coruna 漏洞利用工具包是近年来 iOS 生态中覆盖范围最广、扩散路径最清晰的国家级攻击工具，其从商业监控厂商流向国家级攻击者、最终扩散至网络犯罪团伙的完整路径，揭示了移动威胁态势的核心变化：  
  
曾经仅用于针对高价值目标的间谍软件能力，正在快速向普通用户场景扩散，未及时升级系统的 iOS 设备正面临前所未有的常态化攻击风险。  
  
剩下的关于Coruna黑客工具包的来源探讨。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo2NsD4J8UGXeibzg7xMR7Fpa74SbFuia58biaTia8ECsI1fJlWiciavUndOPiau8UvwWFzzyYN3OEnIIsv7YiaNNa3iaIhUibqnwyAdVfWY/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDq1t5LwFVpia5Ufx5oibK2v0fI4YHn6h4QichbTibiaTNNug6oCTHbQ8fwu26EEJt1R8ZZka0awtIWjoSg0AXgIBtVwNYCBZ3pUYgXg/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq74FoGO7KGHuMOtKHhD3hdKSeSowzxDOa0b4QQ5ZQUicP42Tlcgx13sWVov2za4quORoBw9wHIEkTFjwz9O3mgaJ02W2Xt8eqw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDofKLbgATWYQ6m9ADBxaV0BicbNt1TXy71d2DXt3ehicWIq215MJ6d4XBLVgjuZmqIfLI4LicypeWtlk0ISmDGqSGPhomxHibaFib7o/640?wx_fmt=png&from=appmsg "")  
  
