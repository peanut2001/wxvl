#  DragonForce勒索软件技术分析  
原创 ZM
                    ZM  暗镜   2026-02-13 00:17  
  
DragonForce 自 2023 年 12 月以来一直活跃在网络犯罪领域，并已成为一个强大的实体。该组织采用复杂的勒索软件即服务 (RaaS) 模式，积极将自己包装成“卡特尔”，以巩固权力和影响力。这种战略定位使他们能够吸引广泛的附属机构网络，同时将他们的行动与标准的犯罪组织区分开来。  
  
他们的崛起伴随着策略的不断演变，这使他们成为全球组织持续的威胁。为了支持其扩张，DragonForce 利用 BreachForums、RAMP 和 Exploit 等知名暗网论坛进行招募和推广。他们通过提供独特的工具（例如“RansomBay”）来区分自己的服务，该工具可以生成定制的有效载荷，以及专门的骚扰电话服务来向受害者施压。  
  
这些操作手段旨在最大限度地对目标实体造成心理和经济影响，从而确保更高的支付成功率。  
  
他们提供数据分析支持和团队协调工具，提供了一套可与成熟的合法软件企业相媲美的综合解决方案。  
  
S2W 分析师在最初出现后 发现，该组织在 2023 年 12 月至 2026 年 1 月期间瞄准了 363 家公司。  
  
这些袭击事件的发生频率呈现持续上升的趋势，在 2025 年 12 月达到顶峰，一个月内公布了 35 名受害者的案例。  
  
这些数据凸显了该组织日益增长的行动能力，以及他们扩大攻击范围、针对更广泛行业的意图。  
  
除了标准攻击之外，DragonForce 还积极与竞争对手的勒索软件组织建立对抗关系，偶尔会对竞争对手发起基础设施级别的攻击。  
  
反之，他们也寻求结盟以巩固自身在生态系统中的地位。这种错综复杂的互动网络表明，他们的野心不仅在于参与市场，更在于通过合作与冲突并存的方式主导RaaS经济。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zdwoicOrrJb0eXT7gNA26BlDpArktPEknicsxKCySHStNpFewzYO2otAgMuc3H4upiaM3JQ5iagj84AMWicQnFUjlskGg86luISd2or0ZReAcqDU/640?wx_fmt=png&from=appmsg "")  
  
  
最近对DragonForce Windows二进制文件的技术评估表明，虽然核心加密例程和进程终止方法保持一致，但结构上已进行了重大更新。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zdwoicOrrJb32W4cpDpk0LHPHGcwls9hcy4kl1Ta01sCCuLpbEutibEOnmyFCn9Q2DLPooT26MJID9hPAHdGmUvCuTCvZtoUF1V2rZZVzjjRg/640?wx_fmt=png&from=appmsg "")  
  
该勒索软件继续采用自带漏洞驱动程序 (BYOVD) 技术来破坏安全进程，从而确保加密成功。然而，附加到加密文件的元数据结构已被修改。“加密比率”字段从 1 个字节扩展到 4 个字节，使元数据总大小增加到 537 字节。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zdwoicOrrJb29cumPof4mDNAkWQc2ECibVyUdQOafs2ugiaicxBsbq757ktcUib4Qrv6388rAB1RQcNdktibiae6xu4ib1rPzy7YrUdR2mYBgtfm2wU/640?wx_fmt=png&from=appmsg "")  
  
此外，最新构建器版本包含一个名为“encryption_rules”的测试版功能，允许操作员覆盖特定文件扩展名的加密模式。  
  
如果没有定义具体规则，恶意软件会根据文件大小应用完全加密、部分加密或基于标头的加密。执行时，勒索软件会使用 ChaCha8 算法解密其嵌入的配置，然后再启动这些例程。这种新的配置选项使攻击者能够精确控制不同数据类型受到的影响，并根据受害者的环境优化加密过程的速度和严重程度。  
  
  
