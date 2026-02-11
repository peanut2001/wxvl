#  upload_forge--专业文件上传漏洞扫描器  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-02-11 05:47  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
## 0x01 工具介绍  
  
Upload Forge 是一款功能强大的生产级安全工具，用于检测与利用 Web 应用程序中的文件上传漏洞。该工具专为渗透测试人员和安全研究人员打造，能够自动化测试文件上传表单，并对多种绕过技术进行针对性测试。  
### 主要特性  
- **🚀 异步扫描**  
： 采用 httpx  
 与 asyncio  
 驱动的高性能扫描引擎。  
  
- **🕵️ 高级检测逻辑**  
：  
  
- **扩展名绕过**  
：支持双重扩展（如 .php.jpg  
）、大小写敏感（如 .pHp  
）和罕见扩展（如 .phtml  
、.php5  
）。  
  
- **幻数伪造**  
：可生成带有虚假文件头（例如 PNG、GIF89a）的载荷，以绕过内容类型检测。  
  
- **空字节注入**  
：能够检测针对旧版本后端系统的漏洞（例如 shell.php%00.jpg  
）。  
  
- **多语言支持**  
：可创建包含可执行代码的有效图像文件。  
  
- **🖥️ 现代图形界面**  
：基于 PySide6 构建的深色主题图形界面，便于配置与实时监控。  
  
- **💻 功能丰富的 CLI**  
：提供具备进度条、表格和详细日志的命令行界面。  
  
- **📊 报告功能**  
：可生成专业的 HTML 与 JSON 格式报告。  
  
- **🛡️ 漏洞验证**  
：通过尝试访问与执行上传的文件，自动验证漏洞是否存在。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWKOeGRxt7g3cfOaGoChXcvcx9W67fZcDAR5MEYqERNtjy2FWL37dBicdicwbWqbicJBS6HPsbqCPnHzDdltGTYiaibbOM23tN7AtFo/640?wx_fmt=png&from=appmsg "")  
  
关注微信公众号后台回复“**20260211**  
 ”，即可获取项目下载地址  
  
关注微信公众号后台回复**入群**  
 即可加入星夜AI安全交流群  
## 圈子介绍  
  
现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。  
  
已产出的安全工具及成果包括：  
- 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）  
  
- XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）  
  
- 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）  
  
- NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）  
  
- WinDump_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）_  
  
- _DumpBrowser_V1_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）  
  
- fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）  
  
- RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）  
  
- 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）  
  
- 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）  
  
- 一键Kill 火绒 defender 工具 **HDKiller**  
（包含源码）  
  
- win11 一键kill 360工具 **InjectKill**  
（包含源码）  
  
- win11 一键kill defender工具**win11_df-killer**  
（包含源码）  
  
后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasdfdJ3seRZVv5nUsD4kpZ1pEAHxBE7tkkgIEULhQXZciaYanCribseulg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "image")  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2nhghttp9mQhic3LJWsCj8Jb4QWibnjmRqic7M9W746srJZlLKQg6mmV7cKrwhWCOauLlJPzLzry0iaRQ/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=7 "image")  
  
  
