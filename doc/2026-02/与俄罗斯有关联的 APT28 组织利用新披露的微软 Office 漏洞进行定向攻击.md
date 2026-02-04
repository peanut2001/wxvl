#  与俄罗斯有关联的 APT28 组织利用新披露的微软 Office 漏洞进行定向攻击  
原创 zm
                    zm  暗镜   2026-02-04 00:22  
  
与俄罗斯有关联的组织APT28（又名 UAC-0001、  Fancy Bear、  Pawn Storm、  Sofacy Group、  Sednit、BlueDelta 和 STRONTIUM）是“Neusploit 行动”的幕后黑手，该行动利用了新披露的 Microsoft Office 漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCStib0QBo7Xm5wsDC4F71k4ZiaNfLjsy78fkqpa5FZtUiaffmnCjCOz61CVhkTS3WHO2NsPiatZqoVaP9kg/640?wx_fmt=png&from=appmsg "")  
  
  
APT28组织 至少从2007年就开始活跃，其攻击目标包括世界各地的政府机构、军队和安全组织。该组织还参与了针对2016年美国总统大选的 一系列攻击活动 。  
  
该组织隶属于俄罗斯总参谋部情报总局（GRU）第85主要特勤中心（GTsSS）第26165军事单位。  
  
2026年1月，Zscaler ThreatLabz 揭露了针对中欧和东欧的“Neusploit”行动。攻击者利用漏洞CVE-2026-21509，使用恶意 RTF 文件和本地化诱饵部署了 MiniDoor、PixyNetLoader 和 Covenant Grunt 等植入程序。  
  
1月26日，微软发布了紧急安全更新，以解决一个已被积极利用的Office零日漏洞，该漏洞的编号为CVE-2026-21509。Zscaler于2026年1月29日报告称，该漏洞已被实际利用。  
  
该问题是安全功能绕过漏洞，会影响多个 Office 版本，包括 Microsoft Office 2016、Microsoft Office 2019、Microsoft Office LTSC 2021、Microsoft Office LTSC 2024 和 Microsoft 365 企业应用版。  
  
该安全公告指出：“在 Microsoft Office 的安全决策中依赖不受信任的输入，使得未经授权的攻击者能够绕过本地安全功能。” 公告 还证实，该漏洞已被恶意利用。“攻击者必须向用户发送恶意 Office 文件，并诱骗他们打开该文件。”  
  
该更新修复了一个绕过 Microsoft 365 和 Office 中的 OLE 安全保护的缺陷，该缺陷会使用户面临易受攻击的 COM/OLE 控件的风险。  
  
微软已确认 Office 预览窗格不受影响，不能被用作攻击途径。然而，这家科技巨头并未透露利用此漏洞进行攻击的技术细节。  
  
Zscaler发布的报告指出： “2026年1月，ThreatLabz发现 APT28利用CVE-2026-21509 漏洞攻击  中欧和东欧用户，包括乌克兰、斯洛伐克和罗马尼亚。攻击者使用英语和当地语言（罗马尼亚语、斯洛伐克语和乌克兰语）精心制作社交工程诱饵，以针对这些国家的用户。”  
  
研究人员详细描述了“Neusploit 行动”中的两条攻击链，这两条攻击链都始于利用 CVE-2026-21509 漏洞的武器化 RTF。其中一条路径会投放 MiniDoor，这是一个恶意 Outlook VBA 项目，它会降低宏的安全性，并悄悄地将受害者的电子邮件转发到攻击者控制的地址。  
  
报告指出：“MiniDoor 的主要目标是窃取用户的电子邮件并将其转发给攻击者。”  
  
第二条链更为复杂，它部署了 PixyNetLoader，通过 COM 劫持和计划任务设置持久性，然后加载一个伪造的 EhStorShell.dll。  
  
报告指出：“与第一个投放器变种类似，在成功利用 CVE-2026-21509 后，攻击链会下载 ThreatLabz 命名为 PixyNetLoader 的工具，该工具会在终端上投放恶意组件，并设置 Windows 环境以启动感染链。”  
  
该 DLL 使用隐写术从 PNG 中提取隐藏的 shellcode，绕过沙箱，并在内存中运行 .NET Covenant Grunt 植入程序，滥用合法 API 进行命令和控制。  
  
ThreatLabz 高度确信此次攻击活动与俄罗斯支持的 APT28 组织有关。攻击目标与 APT28 以往专注于中欧和东欧的策略相符，使用了罗马尼亚语、乌克兰语和英语作为诱饵。攻击工具包括 MiniDoor（一种简化的 NotDoor 变种，与 APT28 有关），而基础设施则复用了 APT28 早期行动中出现的 Filen API C2 服务器。PixyNetLoader 攻击链也与之前的攻击活动类似，结合了 COM 劫持、DLL 代理、XOR 加密字符串和嵌入 PNG 的 Covenant Grunt shellcode。  
  
报告总结道：“与俄罗斯有关联的APT28组织此次攻击活动的目标是中欧和东欧国家，他们利用精心构造的RTF文件攻击CVE-2026-21509漏洞，导致MiniDoor和PixyNetLoader恶意软件的部署。”报告还指出：“ThreatLabz的研究表明，APT28不断改进其战术、技术和程序（TTP），利用微软Office等常用应用程序中的最新漏洞进行攻击。”  
  
  
