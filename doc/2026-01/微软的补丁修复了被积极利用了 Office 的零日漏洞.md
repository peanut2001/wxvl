#  微软的补丁修复了被积极利用了 Office 的零日漏洞  
原创 ZM
                    ZM  暗镜   2026-01-27 00:32  
  
微软已发布紧急带外安全更新，以修复已被攻击者利用的高危 Microsoft Office 零日漏洞。  
  
该安全功能绕过漏洞（编号为CVE-2026-21509）会影响多个 Office 版本，包括 Microsoft Office 2016、Microsoft Office 2019、Microsoft Office LTSC 2021、Microsoft Office LTSC 2024 和 Microsoft 365 企业应用版（该公司的云订阅服务）。  
  
但是，正如今天的公告中所述，Microsoft Office 2016 和 2019 的安全更新尚未发布，我们将尽快发布。  
  
虽然预览窗格不是攻击途径，但未经身份验证的本地攻击者仍然可以通过需要用户交互的低复杂度攻击成功利用该漏洞。  
  
微软解释说：“在 Microsoft Office 的安全决策中依赖不受信任的输入，使得未经授权的攻击者能够绕过本地安全功能。攻击者必须向用户发送恶意 Office 文件，并诱骗他们打开该文件。”  
  
“此次更新修复了一个漏洞，该漏洞绕过了 Microsoft 365 和 Microsoft Office 中的 OLE 缓解措施，而这些措施旨在保护用户免受易受攻击的 COM/OLE 控件的侵害。”  
  
“使用 Office 2021 及更高版本的客户将通过服务端更改自动受到保护，但需要重新启动 Office 应用程序才能使更改生效，”声明补充道。  
  
尽管 Office 2016 和 2019 没有立即修复针对攻击的漏洞，但微软提供了一些令人困惑的缓解措施，这些措施可能会“降低攻击的严重性”。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCStibYuEpiatibYr8eEYztDZHUoRHK19A9LEhhibXBYpgSek6xnxrfvhUoBWDr1csIicxaKAvGe2dqZP9ibtQ/640?wx_fmt=png&from=appmsg "")  
  
  
我们已尝试通过以下说明来澄清这个问题：  
1. 关闭所有 Microsoft Office 应用程序。  
1. 创建Windows 注册表的备份，因为错误地编辑注册表可能会导致操作系统出现问题。  
1. 打开 Windows 注册表编辑器 (regedit.exe)，方法是单击“开始”菜单，键入**regedit，**然后在搜索结果中出现时按 Enter 键。  
1. 打开后，使用顶部的地址栏查看是否存在以下注册表项之一：```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\16.0\Common\COM Compatibility\ (for 64-bit Office, or 32-bit Office on 32-bit Windows)

HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Office\16.0\Common\COM Compatibility\ (for 32-bit Office on 64-bit Windows)

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\ClickToRun\REGISTRY\MACHINE\Software\Microsoft\Office\16.0\Common\COM Compatibility\

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\ClickToRun\REGISTRY\MACHINE\Software\WOW6432Node\Microsoft\Office\16.0\Common\COM Compatibility\
```  
  
如果上述注册表项之一不存在，请右键单击“Common”，然后选择“新建”-> “项”，在该注册表路径下创建一个新的“ **COM Compatibility ”项。**********  
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\16.0\Common\
```  
  
1. 现在右键单击现有或新建的**COM 兼容性**项，选择**“新建**”-> **“项”**，并将其命名为**{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}**。  
1. 创建新的**{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}**后，右键单击它，选择**“新建”->“DWORD（32 位）值”**。将新值命名为**“兼容性标志”**。  
1. **创建兼容性标志**值后，双击该值，确保“基本”选项设置为**“十六进制”**，并在“值”数据字段中输入**400 。**  
执行这些步骤后，下次启动 Office 应用程序时，该缺陷将被缓解。  
  
微软尚未透露是谁发现了这个漏洞，也没有透露任何关于如何利用该漏洞的细节。今天早些时候，BleepingComputer 联系微软发言人时，发言人也未能立即置评。  
  
本月初，作为2026 年 1 月“补丁星期二”活动的一部分，微软发布了针对 114 个漏洞的安全更新，其中包括一个已被积极利用的漏洞和两个已公开披露的零日漏洞。  
  
本月修复的另一个正在被积极利用的零日漏洞是桌面窗口管理器中的信息泄露漏洞，微软将其标记为“重要严重性”，该漏洞可能允许攻击者读取与远程 ALPC 端口关联的内存地址。  
  
上周，微软还发布了多个 Windows 紧急更新，以修复 1 月份“周二补丁日”更新引发的关机和云 PC 漏洞，以及另一组紧急更新，以解决导致经典 Outlook 电子邮件客户端冻结或卡顿的问题。  
  
  
