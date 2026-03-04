#  漏洞扫描分析平台 对标商业级漏洞扫描器 | 主机探测、端点梳理、资产测绘、POC验证和自动报告  
dragonkeep
                    dragonkeep  李白你好   2026-03-04 00:01  
  
**免责声明：**  
由于传播、利用本公众号李白你好所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号李白你好及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
## 工具介绍  
  
GoAttack 是一款运用Go语言作为后端和Vue 3作为前端开发的现代化网络安全扫描分析平台。它被设计用于对标商业级漏洞扫描器，并提供一系列包括主机探测、端点梳理、资产测绘、漏扫POC验证和自动报告等多位一体的安全分析能力。旨在为安全工程师、红蓝渗透测试人员及安全运维管理团队提供一个精练、高效、可扩展且界面友好的集成式作战平台。作者：dragonkeep  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVv8RarMEtO3Xict277Vu7ll8DdicIxSEj5y2yTwZeFtI9Qh4lMJCsvKdLicNPXoBVOd46sGevbYAxmib8voDcl1KTxqxNOZic7ibPc4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXYw6lpNv3d5aAib0BHQFuZQIJn3rCK02JEP5ib0sibryBdkGSQZmCAiaOPT7Dvw6KEw4RfibXZ2d4Yl8qgBHjD92YXSUicqUseUM39Q/640?wx_fmt=png&from=appmsg "")  
## 核心功能与特性  
- **多维度资源发现与测绘**  
  
- 支持 TCP TOP1000 以及高并发的综合性端口扫描。  
  
- 支持 UDP TOP100 常规协议探测与解析。  
  
- **主机探测**  
 (Alive Scan)：利用 ICMP 快速扫描目标存活状态。  
  
- **端口扫描**  
 (Port Scan)：  
  
- **服务指纹识别**  
：结合自研引擎及 nmap-service-probes  
，精细识别并呈现对应运行的服务名称（Service）、产品（Product）和版本号（Version）。  
  
- **Web 技术栈识别**  
：内置深度重写的高能 Web 探针及 wappalyzer 引擎机制，精准识别 HTTP/HTTPS 协议下的建站程序、框架乃至路由重定向链。  
  
- **目录与子域名爆破**  
：兼容及内联搭载 gobuster  
 插件化组件进行高度配置化的目录枚举，扫描结果无缝链接至资产指纹模块展示。  
  
任务下发与资产测绘界面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNVUkB8J0egnaRDYWU6yRCm3fYePWfVJHcne2Fib89cUI88O23ic1I7cWCslGX0Oa2icZKAQmeeKEpLLxyPc9LhNBlK0dbRZq2k0dc/640?wx_fmt=png&from=appmsg "")  
  
资产搜索引擎集成集成  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXYyusrqB66LzrZzAANiaicg5nvL92lhD5HphqGPfW75yYu2YKZSzooFxHMpQEicad2rCc7wrwVf7YCia4xLMb29bkqCrNfy97YL9U/640?wx_fmt=png&from=appmsg "")  
- **深度安全检查与审计**  
  
- **POC漏洞验证引擎**  
：强力集成 Nuclei 模板体系，自动执行精准匹配的 CVE/CNVD 级漏洞验证及提取证明。  
  
- **弱口令暴破攻击**  
 (Brute-Force)：自带高性能多协议服务口令探测模块，依托 Fscan 的扩展生态完成 SSH, MySQL, PostgreSQL, MSSQL, Redis, FTP, Mongo, RDP, SMB, Oracle, Telnet, VNC, WinRM, ElasticSearch, Jenkins, Tomcat, Weblogic, JBoss, ActiveMQ, RabbitMQ, LDAP 等 20 多项常见核心企业基础服务的密码安全审查。并由资产服务版本指纹智能触发关联。  
  
漏洞资产列表展示  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNUOC2cxyaO8BoX3HF6CQ0ZfzOFFwDZYODOiblvMe7iaZPrqOCLHWRHIiagsib164MX3YWDzicCOaeFibcMOTGU4ZJCYJAAIb3vvnqWLg/640?wx_fmt=png&from=appmsg "")  
  
POC 漏洞验证详情  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNVmvr2GqTZr5vibXxUjzbl1HThGkMNs5PibVRl007ANvlNP7Kd4tLLAibvmSibzymW8TMOZCA3uLDhXV0mEJjjl44AgeFhlP2uPcE8/640?wx_fmt=png&from=appmsg "")  
- **多样化协同与自定义扫描编排**  
  
- 全量扫描：全方位深度扫描（主机 + TCP/UDP + 弱口令 + 目录枚举 + Web指纹 + POC漏洞验证）。  
  
- 快速扫描：精简实用流（主机 + TCP + Web指纹 + POC + 弱口令核心流）。  
  
- 自定义扫描：完全独立的子任务节点按需自勾选编排。  
  
- **三大主力扫描模式**  
：  
  
- **高级选项护航**  
：包含定时任务扫描执行功能与 IP / 域名资产及危险端口双向黑名单。  
  
- **安全数据中枢与展示流**  
  
- **现代管理仪表盘**  
：全盘监控安全数据变化、系统态势及漏洞严重度占比趋势。  
  
- **系统预警与消息**  
：内置红点及动态数值提醒系统，针对高危或致命级新漏洞资产进行实时下发提示。  
  
- **报告中心模块**  
：一键归档与输出支持优质版式排列的 PDF 和 HTML 业务审计安全报告，适应甲乙方多重合规交付。  
  
报告中心与任务归档  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXXMhe9ga2sMpia97fLt6UydSjOMyfXmPiaPmicn4zl3SY0Dyv3IeZXaWSKX8LX3STL7XMnicdtbvYHSIZrj4CpMTciaUWSd6buOgTw/640?wx_fmt=png&from=appmsg "")  
  
精美的 HTML/PDF 漏洞报告详情  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVfJflYkEaKEtntoicWntM7JcSQY860nJTcRpbr6SoyzkDmrSYxxfAicoicGGLb3AdRFNTZanIsM14ysjcVLib2AvsJywaoN8uDWuk/640?wx_fmt=png&from=appmsg "")  
- **动态组件功能池**  
  
- [x] 字典管理：对 password, directory, domain 类别字典的支持、统计与分类。  
  
- [x] 插件化工具池集成支持。  
  
Nuclei POC 模板管理  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNV8Ihkl8ggBedPNQs0yOFBKsCk1ibYEvcsmcNABEpB0bhQs1rCsPezweupDtdGD78fhuxOnTGYXHIia1Mhb94EvEbyUAXQ7rToIo/640?wx_fmt=png&from=appmsg "")  
  
插件化工具集扩展管理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNVN1w5DuoQgCmHbiaN2a5cau06UmAwa0Cu0wj2pibibOoFB4uRphQSEoIqDTEM3BFeGCuZPDDQYKQkD0p5Xlu1RLXf1Cfxm9t4wsI/640?wx_fmt=png&from=appmsg "")  
## 工具下载  
```
https://github.com/dragonkeep/GoAttack
```  
## 网络安全情报攻防站  
  
**www.libaisec.com**  
  
综合性的技术交流与资源共享社区  
  
专注于红蓝对抗、攻防渗透、威胁情报、数据泄露  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWzrnA1gvgnYyzt8ds6ib9ZiaCVhdwbibI45UEmE1erGJ3rqcCxEDL1HS3ibPI2ObpxCHwlWNmlvVQtVSgAJjYXUuOVRLicRKmOg8jw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
