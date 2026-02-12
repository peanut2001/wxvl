#  必备漏洞挖掘工具！聚合 XRAY/AWVS/vulmap，批量搞定漏洞挖掘与验证  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-02-12 00:32  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
### 0x01 工具简介  
  
在渗透测试和漏洞挖掘领域，整合各类扫描工具并批量处理目标，是提升工作效率的关键。QingScan 作为一款广受欢迎的聚合型漏洞挖掘工具（GitHub 星标超过 1.8k），有效地解决了工具分散、操作复杂的问题。它并非单一功能的扫描器，而是深度集成了 XRAY、AWVS、vulmap 等 30 余款主流工具，能够覆盖 Web 漏洞扫描、主机探测、子域名收集、目录扫描、POC 批量验证、SSH 测试等全方位的安全检测场景。用户仅需添加目标，该工具便能自动协调并执行扫描任务，并将所有结果集中展示，省去了在不同工具间手动切换的麻烦。  
### 0x02 功能概述  
  
✨ 核心特性  
#### 聚合多款工具，实现全场景联动扫描  
- 无需手动切换多种扫描工具，在添加目标后，系统会自动调用 XRAY、AWVS、vulmap、nmap 等 30 余款主流扫描器。  
  
- 覆盖范围包括 Web 漏洞扫描、系统漏洞探测、子域名收集、目录扫描、主机发现、组件识别、URL 爬虫、POC 批量验证、SSH 批量测试等全面的安全检测维度，满足渗透测试全流程的需求。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVjXHS40icicZibPIkricT7ycYB1PPiafTkMKESaXS8vogjSkvAib4mib7okpotgT5Kd8s7YY7XR6l3CkUbleaeqA5DMhsXylIgq9Ee1g/640?wx_fmt=png&from=appmsg "")  
#### 自动化任务调度，显著提升工作效率  
- 只需录入目标资产，工具即可自动完成多维度的扫描任务调度，无需人工干预。  
  
- 扫描结果会自动录入平台并聚合展示，统一整理来自不同工具的检测数据，避免了分散查看与重复分析，极大地降低了人工处理成本。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVk8iaMld8aPN0qF7VY4na6L9YhrpUPVUc1aiccichCTgzTR7K14K4g2YGcgRjRNdMMuPJFw8KjBsmtTBXOVOmlNAF48s39Cn9Zlw/640?wx_fmt=png&from=appmsg "")  
#### 灵活的工具管理方式  
- 支持精细化的工具安装：可通过 PHP 命令查看可安装的工具列表，按需安装指定工具（如 nmap）或一键安装全部工具。  
  
- 适配 Ubuntu 22.04 系统，提供自动安装脚本，简化部署流程，降低了使用门槛。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAX3l5VqbvgK2QVYU7zaiaCT1YwLiaxBf8p4nibBUZxy3msGPmeR0OfiaFMDvkFuicRJ2ZugVqhmUlvxkGuedUicX4QVM4rNHc8qQtu1A/640?wx_fmt=png&from=appmsg "")  
#### 可视化的 Web 管理界面  
- 基于 PHP 搭建了轻量级的 Web 管理页面，无需命令行即可完成目标添加、扫描任务管理和结果查看。  
  
- 扫描结果分类清晰，有助于快速定位高风险漏洞，提升漏洞分析与处置的效率。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUf6z8zWqicbdicm2BsFOa4qLMkMMcOLWz9e4uXu1aEFiaGsODLInRBX6RicvTYqMEy7JK8oJAb2TskPMIYDYthGpUqJOc57AcTkgo/640?wx_fmt=png&from=appmsg "")  
#### 高度可扩展，支持定制化开发  
- 平台本身不限制扫描能力边界，可以灵活适配并整合新增的扫描工具。  
  
- 提供私人订制服务，支持二次开发以满足企业或个人在漏洞挖掘方面的个性化场景需求。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVdNPHd3sEgk4SxwO9ggTQXTicSdV1LNo0jQZpVicbPYhEicmKqb6YukDcuWpuGBdkbabZm6CvZ4xCPFWqPZ0lbeV0g3vBJSx2UgY/640?wx_fmt=png&from=appmsg "")  
### 0x04 使用指南  
  
📦 安装步骤  
  
视频教程  
  
需要在 Ubuntu 22.04 系统下安装，其他系统请自行适配安装。  
1. 安装 PHP 扩展和项目依赖  
  
-   
```
apt install php php-xml php-gd php-mysqli php-dom php-cli php-zip unzip php-curl composercd QingScan/code && composer install  
```  
1. 使用 PHP 启动项目 Web 页面  
  
php think run -p 80  
1. 新建数据库，并导入数据表，SQL 文件位于 deploy  
 目录下的 qingscan.sql  
。  
  
1. 访问 Web 页面  
  
http://127.0.0.1/[1]  
1. 启动调用脚本  
  
./script.sh  
### 工具安装  
  
QingScan 提供了两种方式来安装所需的扫描工具：  
#### 方法一：使用 PHP 命令安装（推荐）  
```
# 查看可安装的工具列表
```  
  
    php think install list     # 安装所有工具     php think install all     # 安装指定工具     php think install nmap  
  
关注微信公众号后台回复“**20260212**  
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
  
  
