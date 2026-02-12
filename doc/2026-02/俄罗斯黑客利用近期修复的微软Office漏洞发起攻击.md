#  俄罗斯黑客利用近期修复的微软Office漏洞发起攻击  
Rhinoer
                    Rhinoer  犀牛安全   2026-02-12 16:01  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBkrOhnIEU2qdibGwPST8b6krAWsZibjnLl0lnb2RDyuspSMdM3KsdyNxjiabWnnIjSrID5SEoPOZQttQ/640?wx_fmt=png&from=appmsg "")  
  
乌克兰计算机应急响应小组 (CERT) 表示，俄罗斯黑客正在利用 CVE-2026-21509，这是微软 Office 多个版本中最近修复的一个漏洞。  
  
1 月 26 日，微软发布了紧急带外安全更新，将 CVE-2026-21509 标记为正在被积极利用的 0 day 漏洞。  
  
在微软发出警报仅仅三天后，CERT-UA 就检测到了利用该漏洞传播的恶意 DOC 文件，这些文件以欧盟驻乌克兰常驻代表委员会磋商为主题。  
  
这些电子邮件冒充乌克兰水文气象中心，并发送到 60 多个政府相关地址，然而，该机构表示，与该文件相关的原数据显示，该文件是在紧急更新发布一天后创建的。  
  
乌克兰 CERT 将这些攻击归咎于 APT28，这是一个国家级威胁行为组织，也称为 Fancy Bear 和 Sofacy，与俄罗斯总参谋部情报总局 (GRU) 有关联。  
  
打开恶意文档会触发基于 WebDAV 的下载链，该下载链通过 COM 劫持、恶意 DLL (EhStoreShell.dll)、隐藏在图像文件 (SplashScreen.png) 中的 shellcode 以及计划任务 (OneDriveHealth) 安装恶意软件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBkrOhnIEU2qdibGwPST8b6krSt6B5cibNB09GEQj5ZRjeJXw77pJ9Evb8icuDz3exPmfeWtebQ68J2RQ/640?wx_fmt=png&from=appmsg "")  
  
CERT-UA 在报告中指出：“计划任务的执行导致 explorer.exe 进程终止并重新启动，而 explorer.exe 进程通过 COM 劫持等方式确保加载“EhStoreShell.dll”文件。”  
  
该 DLL 从映像文件中执行 shellcode，从而确保在计算机上启动 COVENANT 软件。  
  
这与2025 年 6 月 APT28 攻击中关联的 CERT-UA 恶意软件加载程序相同，该程序利用 Signal 聊天将 BeardShell 和 SlimAgent 恶意软件传播给乌克兰政府机构。  
  
该机构报告称，COVENANT 使用 Filen (filen.io) 云存储服务进行命令与控制 (C2) 操作。监控与该平台相关的连接，或将其完全阻止，应能加强对这种威胁的防御。  
  
后续调查显示，APT28 在针对多个欧盟组织的攻击中使用了另外三份文件，表明该攻击活动的范围已超出乌克兰。在一个案例中，用于支持这些攻击的域名是在同一天注册的。  
  
建议各组织机构为 Microsoft Office 2016、2019、LTSC 2021、LTSC 2024 和 Microsoft 365 应用应用最新的安全更新。对于 Office 2021 及更高版本，请确保用户重启应用程序以应用更新。  
  
如果无法立即进行修补，建议按照我们最初对该漏洞的报道中提供的基于注册表的缓解措施说明进行操作。  
  
微软此前曾表示，Defender 的受保护视图通过阻止来自互联网的恶意 Office 文件来增加额外的防御层。  
  
  
信息来源：BleepingComputer  
  
