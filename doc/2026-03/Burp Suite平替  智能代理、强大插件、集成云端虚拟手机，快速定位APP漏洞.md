#  Burp Suite平替 | 智能代理、强大插件、集成云端虚拟手机，快速定位APP漏洞  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-03-09 05:18  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
# 免责声明  
## 工具介绍  
  
**SwordfishSuite**  
 是一款受 Burp Suite 启发而开发的现代化 Web 安全测试平台。它集成了智能代理、流量拦截、负载扫描以及强大的插件系统，致力于为安全研究人员和渗透测试工程师提供一款高效、可定制的应用工具。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKakic4250oOqtgrKFAEbpQ3wicVKnVd8z9fE1xs3HJ6rUz32fohcBnm2sU5f2iaXNb53n9fFGHzGHhE5gvXZMicCwslTGxtVrNiaiaA/640?wx_fmt=png&from=appmsg "")  
## 核心特性  
- **智能拦截代理**  
：能够无缝拦截、查看与修改 HTTP/HTTPS 流量，支持多种客户端，操作流畅且直观。  
  
- **集成APP分析**  
：可集成云手机平台，直接在 SwordfishSuite 中查看并分析手机 APP 流量（此功能暂未开放）。  
  
- **可扩展插件系统**  
：基于 Python 构建了完整的插件生态，允许您轻松编写自定义的扫描检查器与数据分析工具。  
  
- **GUI界面操作**  
：提供了用户友好的图形化界面（GUI），以满足交互式测试的需求。  
  
- **流量数据转发**  
：支持将流量进行二次转发（包括原始流量和 HAR 格式），方便进行各种扩展操作。  
  
## 工具使用  
### 前置要求  
  
在运行 SwordfishSuite 之前，如果您需要启用插件功能：  
- **Python**  
 3.10 或更高版本  
  
- 使用 pip  
 包管理工具安装以下依赖： pip install grpcio grpcio-tools protobuf numpy  
  
### 安装  
1. **从 GitHub 下载 Release 版本压缩包：**```
下载地址：https://github.com/threehammers-group/SwordfishSuite/releases解压文件cd Swordfish./Swordfish.exe
```  
  
  
### 如何使用  
1. **启动应用：**  
  
1. **GUI 模式（推荐）：**```
./Swordfish.exe 或直接鼠标双击即可
```  
  
  
1. **安装证书**  
：首次启动程序时，请点击工具栏中的“安装证书”按钮，以安装 CA 证书来支持 HTTPS 解密（证书存储位置 -> 本地计算机 -> 指定下列存储 -> 受信任的根证书颁发机构 -> 完成）。  
  
1. **开始探索！**  
 点击工具栏的“开始”按钮，即可拦截流量、重放请求、使用负载测试器，或者开发新插件来定制专属功能。  
  
**主界面**  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMLwLfNljiaUIf2uACUSVN07jg1jDHiaAp6HMFia11gDJ0ZuXicZicmbwdTgnAK4MH9KXznLa8cpwDJTcM0gXaqgpB9zF2yMsjJXRqUM/640?wx_fmt=png&from=appmsg "")  
  
  
**数据重发**  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMK7VpHHOJCZbibJjugbYVhgtzTPqQOOEooVAESBGYQJDCRIGJM3xZNt9ZcSsmmianAdvhcA94bZa14xrU2ucichJBqIf8SCt6BTog/640?wx_fmt=png&from=appmsg "")  
  
  
**负载测试**  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJgS7iboQqkyd6ooGCLp7ia2DyrXV9w8sKib4fspVgUoLhpFAhrTBSXtB5BraYuVRDg9wBnd47EfypprhTVQHsJLYiaVZTZa4m2pZE/640?wx_fmt=png&from=appmsg "")  
  
  
**数据包拦截**  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJOCnlEI8NQyzFnjdpVWYyhb5icg6wibO47znicZT3eXIKg3xOR4BYpBo5B61ZLIpreIh1F0g9QiaAZlZ0auTO7E1FZ7kTSQuPPULU/640?wx_fmt=png&from=appmsg "")  
  
  
**APP实时抓包**  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKYsQbrjEy34EsB6yzGGwtzDWL9ZW6RNVL73hwwcSZs6mcWXczymXsG3sr7NmQuYMTCiaMlIndIHTd26iapAZPdJFXoaveWsazzY/640?wx_fmt=png&from=appmsg "")  
  
  
**Python 自开发插件示例**  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJephdz0ugB2reIRHuaAbOOXbeqy4yaiaE0CBRke6Uzrgod1Bhpn2RpnhZ99QKsYXniaqdFia65tIialzWJUhcX0J9ox90cHdShteM/640?wx_fmt=png&from=appmsg "")  
  
  
关注微信公众号后台回复“**20260309**  
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
  
- 免杀火绒6.0内存防护加载器**BypassMemLoader**  
  
后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/libkMqMibKDtW5WBx6ZIXpMjZK0aNNj2IcaQgbhGibBChbThqeY4nseco92Q6t7EiaFbOnydXUl3w72B2UvialRN3A82G56kYjC2pyWH1pPynnAk/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "image")  
  
  
