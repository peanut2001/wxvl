#  StealC恶意软件面板中的安全漏洞使研究人员能够监视威胁行为者的行动  
 TtTeam   2026-02-17 06:11  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB12TK1TY95XXHmmicMYSSusdPpmMPUBY27Dwh2nmIdJDyy06qyrs83JXedouibTswtxA19HQkNnXhuA/640?wx_fmt=png&from=appmsg "")  
  
网络安全研究人员披露了 StealC 信息窃取程序运营商使用的基于 Web 的控制面板中存在跨站脚本 (XSS) 漏洞，使他们能够收集有关在其行动中使用该恶意软件的威胁行为者之一的关键信息。  
  
CyberArk 研究员 Ari Novick在上周发布的一份报告中表示： “通过利用它，我们能够收集系统指纹、监控活动会话，并且不出所料从旨在窃取 cookie 的基础设施中窃取 cookie。”  
  
StealC 是一款信息窃取程序，于 2023 年 1 月首次以恶意软件即服务 (MaaS) 模式出现，允许潜在客户利用 YouTube 作为主要机制（一种被称为YouTube 幽灵网络的现象）来分发恶意程序，将其伪装成流行软件的破解程序。  
  
过去一年中，人们还发现窃取程序通过恶意Blender 基金会文件和一种名为FileFix 的社会工程攻击手段进行传播。与此同时，StealC 也进行了更新，新增了 Telegram 机器人集成功能，可用于发送通知，增强了有效载荷的传递，并重新设计了控制面板。更新后的版本代号为 StealC V2。  
  
几周后，该恶意软件管理面板的源代码被泄露，这为研究界提供了一个机会，可以识别威胁行为者的计算机特征，例如一般位置指示符和计算机硬件详细信息，以及从他们自己的机器中检索活动会话 cookie。  
  
为了防止开发者堵住漏洞，或者防止其他模仿者利用泄露的面板来尝试推出自己的窃取型 MaaS 产品，面板中 XSS 漏洞的具体细节尚未公开。  
  
一般来说，XSS漏洞是一种客户端注入攻击，攻击者可以利用它让易受攻击的网站在受害者计算机的浏览器中执行恶意JavaScript代码。XSS漏洞的出现是由于网站未能验证和正确编码用户输入，从而使攻击者能够窃取cookie、冒充用户并访问敏感信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB12TK1TY95XXHmmicMYSSusdA1sXNDN0tlibx5YAiaSCjS8BtaJWDiaIcvxbJBH5icwj5cyB5DwgP6Xcjw/640?wx_fmt=png&from=appmsg "")  
  
“鉴于 StealC 组织的核心业务是窃取 cookie，你可能会认为 StealC 的开发者应该是 cookie 专家，并且会实现一些基本的 cookie 安全功能，例如httpOnly，以防止研究人员通过 XSS 攻击窃取 cookie，”诺维克说道。“讽刺的是，一个以大规模窃取 cookie 为核心的组织，竟然没能保护自己的会话 cookie 免受教科书式的攻击。”  
  
CyberArk 还披露了 StealC 的一位名为 YouTubeTA（“YouTube Threat Actor”的缩写）的客户的详细信息。该客户广泛利用谷歌的视频分享平台 YouTube 传播窃取程序，通过推广破解版的 Adobe Photoshop 和 Adobe After Effects 来进行攻击，积累了超过 5000 条日志，其中包含 39 万个被盗密码和超过 3000 万个被盗 cookie。经评估，大部分 cookie 为追踪 cookie 和其他非敏感 cookie。  
  
据怀疑，这些举措使攻击者能够控制合法的 YouTube 账户，并利用这些账户推广破解软件，从而形成一种自我延续的传播机制。此外，还有证据表明，攻击者使用类似ClickFix的虚假验证码诱饵来传播 StealC，这表明其传播途径并非仅限于 YouTube。  
  
进一步分析表明，该控制面板允许运营者创建多个用户，并区分管理员用户和普通用户。以 YouTubeTA 为例，该控制面板仅显示一个管理员用户，据称该用户使用一台搭载苹果 M3 处理器的电脑，语言设置为英语和俄语。  
  
威胁行为者犯了一个可被视为操作安全失误的错误：大约在2025年7月中旬，由于其忘记通过虚拟专用网络（VPN）连接到StealC控制面板，其真实IP地址暴露无遗，该地址与一家名为TRK Cable TV的乌克兰有线电视运营商相关联。调查结果表明，YouTubeTA是一个独狼式攻击者，其活动地点位于一个以俄语为主要语言的东欧国家。  
  
  
  
  
  
