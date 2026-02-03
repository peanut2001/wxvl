#  APT28的“Neusploit”行动：俄罗斯黑客利用Microsoft Office零日漏洞展开间谍活动  
原创 萧瑶
                    萧瑶  Alfadi组织   2026-02-03 08:42  
  
在网络安全领域，国家支持的威胁行为者不断演化其战术，以渗透敏感目标。2026年2月3日，随着Microsoft发布紧急补丁后仅几天，俄罗斯相关的先进持久威胁（APT）组APT28（又称Fancy Bear）已被曝光通过“Operation Neusploit”行动积极利用一个Microsoft Office零日漏洞。该漏洞允许攻击者在受害者系统中建立持久 foothold，并窃取敏感数据。本文将深入剖析这一行动的技术细节、影响以及防御策略，基于多家安全研究机构的最新报告。行动概述：从披露到活跃利用APT28 是俄罗斯军事情报机构GRU的附属组织，以针对西方政府、军事和外交目标的间谍活动闻名。该组自2008年以来活跃，曾参与2016年美国大选干扰和针对世界反兴奋剂机构（WADA）的攻击。  
  

 在“Operation Neusploit”中，APT28 利用CVE-2026-21509，这是一个Microsoft Office RTF文件中的安全功能绕过漏洞，CVSS分数为7.8。  
  

 Microsoft于2026年1月26日披露该漏洞并发布带外补丁，但攻击者早在披露前就已开始利用。  
  

Zscaler ThreatLabz的研究人员将这一行动命名为“Neusploit”，并在1月29日观察到活跃样本。  
  

 攻击链以鱼叉式网络钓鱼开始，诱饵文件包括“Consultation_Topics_Ukraine(Final).doc”、“Courses.doc”等，内容涉及乌克兰相关主题，使用英语、罗马尼亚语、斯洛伐克语和乌克兰语，以针对中欧和东欧用户。  
  
乌克兰CERT-UA报告称，攻击者针对乌克兰政府机构和欧盟组织，伪装成官方通信。  
  

技术剖析：多阶段感染链“Neusploit”的感染过程高度复杂，分为两个变体，均从武器化RTF文件开始，利用CVE-2026-21509实现远程代码执行（RCE）。  
  

变体1：部署MiniDoor后门初始阶段：受害者打开RTF文件后，漏洞被触发，从攻击者控制的服务器（如freefoodaid[.]com）下载恶意DLL（例如“2_2.d”）。
  
  
部署阶段：DLL解密并安装MiniDoor，这是一个基于VBA的Outlook宏窃取器。MiniDoor监控Outlook事件（如MAPILogonComplete和Application_NewMailEx），窃取收件箱、RSS订阅、垃圾邮件和草稿文件夹中的邮件，并转发至硬编码邮箱（如ahmeclaw2002@outlook.com）。
  
  
持久化：通过修改注册表键（HKCU\Software\Microsoft\Office\16.0\Outlook\Security\Level = 1）启用宏并禁用安全提示。  
  

MiniDoor是APT28先前NotDoor变体的简化版，专注于电子邮件窃取，而非全功能后门。 
  
  

@blackorbird
  
  

变体2：PixyNetLoader与Covenant Grunt初始阶段：类似变体1，RTF触发下载PixyNetLoader DLL（例如“table.d”）。
  
  
部署阶段：PixyNetLoader创建互斥体（asagdugughi41），然后使用滚动XOR密钥（shfioehh243t3dcwechortjbo6k7pjl8lop7ku45ht3u4grywefdyehriobjojko5k65iyh）解密并投放加密负载到路径如%programdata%\Microsoft OneDrive\setup\Cache\SplashScreen.png。
  
  
持久化与加载：通过COM劫持EhStorShell.dll（合法的Windows增强存储壳扩展）实现持久化，设置注册表键以加载恶意DLL。同时创建一个名为“OneDriveHealth”的计划任务，使用schtasks.exe重启explorer.exe触发劫持。
  
  
壳代码执行：EhStoreShell.dll在explorer.exe中加载，检查沙箱环境（通过Sleep API时间差>2.9秒检测）。然后从SplashScreen.png中使用最低有效位（LSB）隐写术提取壳代码。
  
  
最终负载：壳代码加载.NET程序集，部署Covenant Grunt植入物，这是一个基于.NET的命令与控制（C2）代理。  
  

Covenant Grunt使用Filen云存储API（UUID: fe644d8c-2601-46ea-bf7d-3db110aa08d4）作为C2桥梁，与APT28之前的“Phantom Net Voxel”行动类似。  
  

 这允许攻击者通过合法云服务路由流量，规避检测。回避技术与基础设施APT28在“Neusploit”中采用多种回避手段：服务器端过滤：仅向特定区域和User-Agent的请求提供DLL。
  
  
字符串混淆：使用单字节XOR（0x3a）或滚动XOR密钥。
  
  
API解析：EhStoreShell.dll使用DJB2哈希动态解析API。
  
  
隐写与互斥：壳代码隐藏在PNG中，互斥体防止多实例。
  
  
基础设施：域名如freefoodaid[.]com和wellnesscaremed[.]com，同日注册并使用，显示快速循环。  
  

这些技术与APT28的TTP一致，包括MITRE ATT&CK中的T1566.001（鱼叉附件）、T1203（客户端执行利用）和T1546.015（COM劫持）。  
  

影响与受害者“Neusploit”针对乌克兰中央政府机构、欧盟成员国组织，焦点是情报窃取。CERT-UA警告称，由于更新惰性和用户抵抗，攻击可能持续。  
  

 CISA已将CVE-2026-21509添加到已知利用漏洞目录，要求联邦机构在2月16日前修补。  
  
潜在影响包括数据泄露、持久访问和进一步横向移动。X平台上的讨论显示，安全社区迅速响应，如用户@RigneySec  
  
和@evanderburg
  
  
分享了The Register的报道，强调漏洞从披露到利用仅几天。 
  
  

防御策略立即修补：应用Microsoft补丁，覆盖Office 2016、2019、LTSC 2021/2024和Microsoft 365。  
  

监控与阻挡：监视Filen相关流量，或直接阻挡。启用沙箱检测异常文件行为。
  
  
用户教育：警惕乌克兰或欧盟主题的附件，使用宏禁用设置。
  
  
高级防护：部署EDR工具检测COM劫持、隐写负载和异常Outlook活动。定期审计注册表和计划任务。
  
  
情报共享：参考IOCs，如文件哈希（e.g., 95e59536455a089ced64f5af2539a449 for RTF）和域名（freefoodaid[.]com）。 
  
  

zscaler.com
  
  

“Operation Neusploit”突显了零日漏洞的快速武器化，以及国家行为者对供应链和办公软件的持续兴趣。企业应优先考虑补丁管理和威胁狩猎，以缓解此类风险。
  
  

  
  
