#  疑似俄罗斯背景APT28组织利用最新漏洞及云C2基础设施发起隐蔽攻击  
原创 BaizeSec
                    BaizeSec  白泽安全实验室   2026-02-06 01:00  
  
近日，网络安全机构发现疑似俄罗斯背景的网络威胁组织APT28（又称Fancy Bear或UAC-0001）发起了一场针对多国军事和政府机构的网络攻击活动，该组织在微软Office漏洞CVE-2026-21509公开披露仅24小时内便迅速利用其发起攻击。这次攻击活动主要聚焦于波兰、斯洛文尼亚、土耳其、希腊、阿联酋和乌克兰等国的国防部、运输物流运营商以及外交机构，旨在窃取敏感情报数据。  
  
本次攻击活动始于2026年1月28日至30日的72小时密集鱼叉式网络钓鱼行动，APT28组织通过被入侵的政府账户（如罗马尼亚、玻利维亚和乌克兰的邮箱）发送至少29封定制化电子邮件。这些邮件以地缘政治敏感话题为诱饵，包括武器走私警报、军事训练邀请、外交磋商以及气象紧急通报，诱导收件人打开附件。附件多为RTF或DOC格式的文件，如名为“BULLETEN_H.doc”的文档，一旦打开即触发CVE-2026-21509漏洞。该漏洞允许攻击者绕过微软Office的OLE安全限制，嵌入Shell.Explorer ActiveX控件，无需宏或用户交互即可自动执行代码，通过WebDAV协议从攻击者控制的基础设施下载外部木马程序。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/HBRznhxajkZKic5l6EYTd8XwTagm8GZQBqBScsyUNsBrWibevvcXq2Fiash7n4n2MISzZcs9D7qlwiaBVibNicgNQkiaDb9ibAzOhLaWPLsKU8sgQ6U/640?wx_fmt=png&from=appmsg "")  
  
图   
1 APT28组织采用的多阶段感染链  
  
技术分析显示，这次攻击采用多阶段感染链。初始漏洞利用后，系统会下载恶意LNK快捷方式与第一阶段加载器SimpleLoader，为后续多阶段感染奠定基础。SimpleLoader采用三种不同的XOR加密方案保障隐蔽性：单字节XOR（密钥0x43）用于互斥体生成；交替字节XOR结合空填充处理路径字符串；76字符轮换XOR密钥则用于解密嵌入式载荷。在BeardShell感染路径中，加载器会创建单实例互斥体并执行投放程序，向磁盘写入三个关键文件：主载荷EhStoreShell.dll（存放于% PROGRAMDATA%\USOPublic\Data\User\目录）、计划任务配置XML（用户临时目录），以及伪装成OneDrive安装文件的加密载荷PNG图像（SplashScreen.png）。为实现持久化，攻击者通过劫持CLSID为{D9144DCD-E998-4ECA-AB6A-DCD83CCBA16D}的COM对象，并创建名为“OneDriveHealth”的计划任务——该任务在注册后60秒触发，执行终止并重启explorer.exe的命令以加载劫持的COM对象，随后自行删除以清除痕迹，确保EhStoreShell.dll成功注入explorer.exe进程并与[filen.io] 建立C2通信。  
  
BeardShell变体（EhStoreShell.dll）内置多重反分析机制，包括3秒睡眠并验证执行时间（阈值≥2.9秒）以检测沙箱环境的时间加速，以及验证进程名称确保仅在explorer.exe中运行。其通过单字节XOR（密钥0x43）解密嵌入式字符串，并通过基于哈希值的查找解析10个Windows API。在完成环境验证后，BeardShell会解析此前投放的SplashScreen.png，该恶意软件内置完整的PNG解码器（含10个专用函数，涵盖IHDR头解析、PLTE调色板提取、IDAT块zlib解压、霍夫曼表构建及Adam7隔行扫描等功能），最终从图像数据块中提取出.NET 加载器shellcode。提取的shellcode作为无文件.NET程序集引导机制，通过遍历进程环境块（PEB）动态解析API以绕过导入地址表（IAT），加载MSCOREE.DLL与OLEAUT32.DLL，并调用CLRCreateInstance在被劫持的explorer.exe进程中初始化.NET运行时，实现完全无文件执行。  
  
在后续攻击阶段，感染链条会推进至经过修改的.NET加载器（基于Covenant框架的“Grunt”后门），该加载器通过2048位RSA密钥对与攻击者的C2基础设施完成加密握手：攻击者监控[filen.io]上的指定基础文件夹UUID，检测到新受害者注册后，生成32字节随机AES-256会话密钥，用受害者的RSA公钥加密后上传至专属子文件夹；受害者接收后用自身私钥解密会话密钥，通过挑战-响应交换验证握手合法性，随后下载加密的Covenant Grunt程序集，利用会话密钥解密并通过Assembly.Load ()结合反射调用属性实现执行。改造后的Covenant Grunt植入程序深度整合[filen.io]云服务，包含四大核心组件：FilenApi（支持24个子域名的[filen.io]网关、接收与发送端点完整REST API客户端）、FilenMessenger（实现IMessenger接口，用于轮询和上传加密任务文件）、FilenEncryptor（提供AES-256-GCM加密，含每文件随机数与HMAC-SHA256完整性验证）、GruntExecutor（任务执行引擎，支持.NET程序集加载、PowerShell执行及匿名管道输出流），所有执行结果经AES-256-CBC加密与HMAC-SHA256验证后上传至指定文件夹，供攻击者获取分析。  
  
除BeardShell/Covenant攻击路径外，APT28组织还针对部分目标部署了专注于长期邮件情报收集的Outlook后门“NotDoor”。在SimpleLoader执行后，会通过修改注册表彻底禁用Outlook宏安全控制：将HKCU\Software\Microsoft\Office\16.0\Outlook\Security\Level设为1（信任所有宏且无警告），将LoadMacroProviderOnBoot设为1（强制启动时自动初始化宏提供程序），构建可跨应用重启的持久执行环境。随后，加载器将32768字节的VbaProject.OTM写入%APPDATA%\Microsoft\Outlook目录。该VBA宏通过双重自动触发机制实现邮件监控：Application_MAPILogonComplete在Outlook登录时执行，Application_NewMailEx在新邮件到达时实时触发转发。其数据收集逻辑会系统遍历收件箱、草稿箱、垃圾邮件、RSS订阅四大文件夹，每次执行处理每个文件夹最多10封邮件，对未处理邮件调用Outlook对象模型保存完整消息（含头信息、正文、附件、元数据）为%TEMP%\temp_email.msg，创建新邮件附加该文件后通过标准SMTP发送至两个攻击者控制的邮箱。同时为已处理邮件添加“AlreadyForwarded”自定义属性避免重复发送，并设置DeleteAfterSubmit = True自动清除已发送邮件，该机制对存储敏感政策文档、机密电报的外交与政府邮件系统极具威胁。  
  
在攻击基础设施与战术层面，APT28组织此次的显著特征是对合法云服务的深度滥用。除核心C2通道[filen.io]外，其历史攻击中还曾使用Koofr、Icedrive等云平台，体现出灵活切换云服务的能力。初始攻击阶段依赖已攻陷或攻击者注册的Web服务器托管恶意文档与LNK文件，部分域名甚至在攻击当天注册，凸显其运营的敏捷性。攻击钓鱼攻击策略上，APT28组织在2026年1月28日至30日的72小时内，向9个东欧国家发送至少29封不同钓鱼邮件，邮件源头为罗马尼亚、玻利维亚、乌克兰等国的已攻陷政府邮箱。攻击目标覆盖国防部（40%）、交通物流运营商（35%）、外交机构（25%），并围绕四大地缘政治相关主题设计文件诱饵：45%为冒充中东欧边境安全机构的“跨国武器走私预警”（伪造“叙利亚经乌克兰转运200枚RPG-7火箭弹”信息）、25%为仿冒区域国防大学的“军事培训项目邀请”（含专业签名与限时报名节点）、20%为伪装高层议会请求的“欧盟/北约外交磋商文件”（涉及乌克兰冲突政策立场征询）、10%为滥用已攻陷国家气象局基础设施的“气象紧急公报”（伪造洪水预警）。所有钓鱼邮件附件均为利用CVE-2026-21509的RTF/DOC文件（如BULLETEN_H.doc、Courses.doc）。诱饵内容高度模仿真实政府公文风格，包含官方信头、双语格式（罗马尼亚语/英语、乌克兰语/英语）、彩色风险地图及部委印章，部分内容疑似基于此前窃取的真实文档制作，旨在利用机构信任规避用户警惕。  
  
目前，研究人员已确认此次攻击涉及至少两个[filen.io]账号。攻击者在攻陷系统后会执行ARP扫描、系统信息查询等侦察操作，并通过注入svchost.exe实现持久化，为横向移动做准备。乌克兰计算机应急响应小组（CERT-UA）已正式将2026年1月的相关攻击归因于UAC-0001（即APT28组织）。技术溯源显示BeardShell变体的10个恶意函数与Sekoia此前报告的参考恶意软件高度匹配，且COM劫持、Outlook宏后门等战术与APT28近期针对欧洲组织的攻击模式完全一致，结合其对乌克兰及北约盟友的长期攻击偏好，进一步印证了该组织的参与。  
  
此次APT28组织的攻击行动再次表明，国家背景黑客组织正以“漏洞武器化加速化”“C2基础设施合法化”“攻击链条无文件化”为趋势，不断升级攻击手段。对于政府、军事及关键基础设施运营方而言，构建覆盖“漏洞管理-威胁检测-应急响应”的纵深防御体系，已成为应对高级持续性威胁的核心需求。  
  
参考链接：  
  
https://strikeready.com/blog/apt28s-campaign-leveraging-cve%E2%80%912026%E2%80%9121509-and-cloud-c2-infrastructure/  
  
往期推荐  
  
  
[LockBit勒索组织发布声明并重建泄露网站——每周威胁情报动态第166期（2.23-2.29）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492114&idx=1&sn=8d7c5643b4d7b9e6ba5fdb73db25f5ac&chksm=e90dc838de7a412e358185c880ff13f5960c816f47faef975adecc92aa229dd947eaed7c1543&scene=21#wechat_redirect)  
  
  
[GoldFactory组织开发针对iOS系统的GoldPickaxe木马病毒——每周威胁情报动态第165期（2.9-2.22）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492108&idx=1&sn=9a94a877d19aae993613beabfed515b9&chksm=e90dc826de7a4130e9c14fbecc4bb470c785600d65f4eca984822a3772b801007188d753444b&scene=21#wechat_redirect)  
  
  
[新APT组织APT-LY-1009针对亚美尼亚政府投递VenomRAT——每周威胁情报动态第164期（02.02-02.07）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492097&idx=1&sn=53ec18ecbac467ab6dddeef971e8630f&chksm=e90dc82bde7a413df05e08bc4d6136b60d4a339310cdb66a046cc0645bb90e447b8564e16180&scene=21#wechat_redirect)  
  
  
[APT28组织对全球多个组织发起NTLMv2哈希中继攻击——每周威胁情报动态第163期（01.26-02.01）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492083&idx=1&sn=2c985de24dfa929181ba8e6ae63b02ab&chksm=e90dcbd9de7a42cf2f738cbe44a3859ab3f78636b84ef2b930dfc29ecbfc05542ae161ab4e16&scene=21#wechat_redirect)  
  
  
