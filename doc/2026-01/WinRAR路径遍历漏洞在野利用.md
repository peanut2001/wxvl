#  WinRAR路径遍历漏洞在野利用  
原创 Bill Toulas
                    Bill Toulas  暗镜   2026-01-28 00:32  
  
多个威胁行为者，包括国家支持的和受经济利益驱动的，正在利用 WinRAR 中的 CVE-2025-8088 高危漏洞进行初始访问并投放各种恶意载荷。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt9S9F3EWmsZysfbCfyfpup5FKp6zkTJhcoOzmr9UziaprzmMkzoUsaCpHGvbay8Po0kfPs6vhCRChA/640?wx_fmt=png&from=appmsg "")  
  
该安全问题是一个路径遍历漏洞，它利用备用数据流 (ADS) 将恶意文件写入任意位置。攻击者过去曾利用此漏洞在 Windows 启动文件夹中植入恶意软件，使其在重启后仍然能够存活。  
  
网络安全公司 ESET 的研究人员发现了这一漏洞，并在 2025 年 8 月初报告称，与一直在利用该漏洞进行零日攻击。  
  
谷歌威胁情报小组 (GTIG) 在今天发布的一份报告中称，这种攻击早在 2025 年 7 月 18 日就开始了，并且一直持续至今，攻击者既有国家支持的间谍行为者，也有以经济利益为目的的低级网络犯罪分子。  
  
“攻击链通常涉及将恶意文件隐藏在归档文件中诱饵文件的 ADS 中。  
  
“虽然用户通常会在存档中看到一个诱饵文档（例如 PDF），但其中也包含恶意广告条目，有些包含隐藏的有效载荷，而另一些则是虚拟数据，”谷歌。  
  
打开 WinRAR 时，它会使用目录遍历提取 ADS 有效载荷，通常会生成 LNK、HTA、BAT、CMD 或脚本文件，这些文件会在用户登录时执行。  
  
谷歌研究人员观察到，利用 CVE-2025-8088 漏洞的国家支持型威胁行为者包括：  
  
UNC4895（RomCom/CIGAR）通过鱼叉式网络钓鱼向乌克兰军事单位投放 NESTPACKER（Snipbot）。  
  
APT44（FROZENBARENTS）使用恶意 LNK 文件和乌克兰语诱饵进行后续下载。  
  
TEMP.Armageddon（喀尔巴阡山脉）将 HTA 下载器放入启动文件夹（活动将持续到 2026 年）。  
  
Turla（SUMMIT）利用乌克兰军队主题发布 STOCKSTAY 恶意软件套件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt9S9F3EWmsZysfbCfyfpup5SJuFOQibkyJCFvoqZkyvjaUWY7lLRfmtzJgwQTG0fKBxTqiakfC9cHFA/640?wx_fmt=png&from=appmsg "")  
  
Google 还观察到一些以经济利益为目的的攻击者利用 WinRAR 路径遍历漏洞来分发诸如 XWorm 和 AsyncRAT 之类的通用远程访问工具和信息窃取程序、Telegram 机器人控制的后门以及 Chrome 浏览器的恶意银行扩展程序。  
  
据信，所有这些威胁行为者都从专门的供应商那里获得了可用的漏洞利用程序，例如使用别名“zeroplayer”的供应商，该供应商去年 7 月曾宣传过 WinRAR 漏洞利用程序。  
  
去年，同一威胁行为者还兜售了多个高价值漏洞利用程序，包括据称可逃逸 Microsoft Office 沙箱、入侵企业 VPN、提升 Windows 本地权限以及绕过安全解决方案（EDR、防病毒软件）的零日漏洞，售价在 8 万美元到 30 万美元之间。  
  
谷歌评论说，这反映了漏洞利用开发的商品化，这在网络攻击的生命周期中至关重要，它降低了攻击者的摩擦和复杂性，使他们能够在短时间内攻击未打补丁的系统。  
  
