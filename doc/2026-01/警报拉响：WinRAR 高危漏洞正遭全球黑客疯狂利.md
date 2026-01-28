#  警报拉响：WinRAR 高危漏洞正遭全球黑客疯狂利  
安世加
                    安世加  安世加   2026-01-28 11:51  
  
新闻  
  
News Today  
  
1 月 28 日消息，谷歌威胁情报小组（GTIG）携手安全公司 ESET 发布报告，现有证据表明全球多个黑客组织正疯狂利用 WinRAR 的高危漏洞（CVE-2025-8088）。  
  
  
谷歌威胁情报小组指出，利用该漏洞的攻击活动最早可追溯至 2025 年 7 月 18 日，且至今仍未停歇。ESET 的研究人员早在 2025 年 8 月初就已发现该漏洞，并指出亲俄黑客组织 RomCom 当时已将其用于零日攻击。  
  
  
WinRAR 已于 2025 年 7 月 30 日发布补丁，并敦促 WinRAR 用户尽快升级到 7.13 及更高版本，以规避安全风险。  
  
  
该漏洞的核心机制在于利用 Windows 系统的“备用数据流”（ADS）特性进行路径遍历攻击。谷歌研究人员解释称，攻击者通常将恶意文件隐藏在压缩包内诱饵文件（如 PDF 文档）的 ADS 中，用户在查看诱饵文档后，WinRAR 会在后台通过目录遍历将恶意载荷（如 LNK、HTA、BAT 或脚本文件）解压并释放到任意位置。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/UZ1NGUYLEFhN90mS9hkx2UN6aaN0YiaOGmSLPSMO3xkfvVzIaLXAFYiaajQFcRRydRgCemqXEqohZHqR4WwOx2oQ/640?wx_fmt=png&from=appmsg "")  
  
  
攻击者最常选择的目标是 Windows 启动文件夹，这样一来，恶意脚本就会在用户下次登录系统时自动运行，从而实现持久化攻击。  
  
  
谷歌的监测数据显示，多个黑客组织正积极利用该漏洞发起攻击。其中，UNC4895（RomCom）通过鱼叉式网络钓鱼向军事单位投放 Snipbot 恶意软件；APT44 和 Turla 则利用诱饵文件分发后续下载器和恶意软件套件。  
  
  
此外，出于经济动机的犯罪分子也加入了这场狂欢，他们利用该漏洞分发 XWorm、AsyncRAT 等远程访问工具及银行窃密插件，甚至部署由 Telegram 机器人控制的后门程序。  
  
本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！  
  
文章转自：IT之家  
  
  
安世加为出海企业提供SOC 2、ISO27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）  
  
[](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)  
  
  
