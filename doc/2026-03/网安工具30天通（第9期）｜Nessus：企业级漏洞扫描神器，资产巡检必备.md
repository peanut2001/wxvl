#  网安工具30天通（第9期）｜Nessus：企业级漏洞扫描神器，资产巡检必备  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-03-06 03:07  
  
## 一、工具核心定位  
  
**Nessus**  
 是全球使用率最高的**企业级全自动漏洞扫描器**  
，也是渗透测试、护网行动、企业资产安全巡检的核心工具。区别于Nmap的端口扫描，Nessus能深度检测端口背后的**服务漏洞、系统漏洞、弱口令、配置缺陷**  
，从底层系统到上层应用，实现全维度的资产安全扫描。  
  
不管是政企内网的资产合规检查，还是CTF靶机的漏洞快速摸排，亦或是SRC挖洞前的资产情报收集，Nessus都能一键输出详细的漏洞报告，标注漏洞等级、利用方式、修复建议，堪称**“资产安全体检仪”**。  
  
核心用途：  
- 主机/服务器系统漏洞扫描（如Windows/MS17-010、Linux内核漏洞）  
  
- 中间件/服务漏洞检测（如Tomcat、Apache、MySQL漏洞）  
  
- 全网资产弱口令批量检测（SSH、FTP、数据库、Web后台）  
  
- 配置合规性检查（如未授权访问、高危端口开放、密码策略过弱）  
  
- 生成标准化漏洞报告，指导安全修复  
  
## 二、核心操作流程（新手一步到位，直接照做）  
### 1. 基础配置（首次使用必做）  
- 安装并激活Nessus（获取激活码，加载漏洞库）  
  
- 新建**Scan（扫描任务）**  
，选择扫描类型：  
  
✅ **Basic Network Scan**  
（基础网络扫描，新手首选）  
  
✅ **Credentialed Scan**  
（带凭证扫描，深度检测，需输入账号密码）  
  
✅ **Web Application Scan**  
（Web应用扫描，对标Web漏洞）  
### 2. 扫描核心设置  
- **Target**  
：填写目标IP/IP段（如10.10.10.0/24，支持批量扫描）  
  
- **Port Scan**  
：选择扫描端口（全端口/常用端口，建议全端口深度扫）  
  
- **Credentials**  
：添加目标凭证（如SSH账号、Windows账号，提升扫描深度）  
  
- **Plugins**  
：勾选需检测的漏洞插件（默认全选，覆盖系统/应用/弱口令）  
  
### 3. 启动扫描&查看结果  
- 点击**Launch**  
启动扫描，等待完成（根据资产数量，耗时数分钟到数小时）  
  
- 扫描结束后，在**Vulnerabilities**  
页面查看结果，按**Critical（高危）、High（高）、Medium（中）、Low（低）**  
 分级筛选  
  
- 点击单个漏洞，查看**详细信息**  
：漏洞描述、危害等级、利用POC、修复建议、受影响资产  
  
### 4. 导出报告（实战/工作必备）  
- 点击**Report**  
，选择导出格式（PDF/HTML/CSV，企业常用PDF）  
  
- 报告包含：资产清单、漏洞统计、详细漏洞信息、修复方案，可直接用于安全整改  
  
## 三、经典CTF真题实战  
### 真题名称：未设防的服务器  
### 靶机信息  
- 开放端口：22（SSH）、135（RPC）、445（SMB）、3306（MySQL）  
  
- 系统：Windows Server 2008 R2，存在经典高危漏洞  
  
- 目标：通过Nessus快速定位高危漏洞，利用漏洞拿到flag  
  
- 考点：Nessus漏洞扫描、高危漏洞识别、基础漏洞利用思路  
  
## 四、完整解题流程（Nessus全程指引，零基础可复现）  
### 步骤1：新建基础网络扫描，添加靶机IP  
  
打开Nessus，新建**Basic Network Scan**  
，Target填写10.10.10.90  
，其余默认配置，点击**Launch**  
启动扫描。  
### 步骤2：扫描结果分析，定位高危漏洞  
  
扫描完成后，筛选**Critical（高危）**  
 漏洞，发现核心高危漏洞：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyNkKx6lojWibfJ5rfKxKNuA9J8BvvM1a3YyebqaHNiaLKSZX2HdJUqicYGc9pf93h7zlrXPGC3u68DunGOaNyLOswrBolgOkdwdGQ/640?wx_fmt=png&from=appmsg "")  
  
同时检测出**MySQL弱口令**  
：root/123456  
（Low等级，辅助利用）  
### 步骤3：利用高危漏洞，获取系统权限  
  
根据Nessus提供的漏洞信息，确认靶机存在MS17-010永恒之蓝漏洞，通过MSF加载对应漏洞模块：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOVIomMbesia10ZtNaIMufc6ICTibE4pG03PPtqFdAaEVoNLknRCicH3FLOyErgeiabVSvWmVBMTdjI48RAaM9dWqq6rf311Bk4n54/640?wx_fmt=png&from=appmsg "")  
  
一键执行后，直接获取**Windows系统SYSTEM权限**  
（最高权限）。  
### 步骤4：读取flag，完成解题  
  
在MSF的shell中，执行命令查找并读取flag：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyNPhIVjBibpmFAWS3vNu6BHkZxcVmHLxga6Fg2wolMRLm1mCwoXjBtxicibD7ZkNC9AyPg3njicWjo5UblBpfobb3om6w6BgttbB9Q/640?wx_fmt=png&from=appmsg "")  
  
得到flag：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyPlYTiakb6fHNgUIhzdKiaNuq3rLDRm8fHtLSuwicsIqfMJibcwrvy4PlcicWrTcbEhp07Ujrt8NT2GCVWKt2B5q6djJswW8qom3GNU/640?wx_fmt=png&from=appmsg "")  
  
## 五、实战复盘（工具价值落地，扫漏/挖洞通用）  
1. **Nessus是“漏洞发现神器”，而非漏洞利用工具**  
：它能快速定位漏洞，但利用漏洞仍需配合MSF、EXP等工具，这是扫漏的核心逻辑。  
  
1. **带凭证扫描是关键**  
：无凭证扫描仅能检测表面漏洞，添加目标账号密码后，Nessus可深度检测系统内部漏洞、配置缺陷，漏扫率大幅降低。  
  
1. **CTF/挖洞/护网的不同用法**  
：  
  
1. CTF：快速摸排靶机高危漏洞，找到突破口；  
  
1. SRC挖洞：扫描目标资产段，定位弱口令、未授权访问、高危漏洞，精准挖洞；  
  
1. 护网/企业巡检：批量扫描全网资产，生成标准化报告，指导安全整改。  
  
1. **漏洞等级优先原则**  
：扫描结果先看**Critical/High**  
等级漏洞，这类漏洞往往是直接突破口，低危漏洞可作为辅助利用点。  
  
## 六、福利领取：全系列资料合集  
  
为了感谢大家的一路跟随，整理了 **「200节攻防教程资源包」**  
这是我整理的精华内容，覆盖网安所有核心知识点，后台回复“  
学习  
”即可获取：  
  
全套学习资源，可以  
点击文末  
阅读原文  
领取200节攻防教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
## 下期预告（第10期）  
  
**每日1工具1真题，网安工具30天通持续更新**  
  
明日工具：**Wireshark**  
——网络抓包分析神器，看透网络流量本质，排查网络漏洞、分析攻击流量的核心工具！  
  
