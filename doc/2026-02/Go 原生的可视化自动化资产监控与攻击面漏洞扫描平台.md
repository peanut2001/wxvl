#  Go 原生的可视化自动化资产监控与攻击面漏洞扫描平台  
 sec0nd安全   2026-02-22 02:54  
  
# CyberRay：Go 构建的资产监控与攻击面扫描系统  
  
  
⚠️  
  
    请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。  
**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**  
  
⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"  
**0xSecDebug**  
"设为星标⭐️"否则可能就看不到了啦！  
  
**💡项目地址在文章底部哦！**  
  
  
## 📖 项目/工具简介  
  
CyberRay 是基于 Go 语言重构的现代化资产安全管理平台，致力于实现资产探测自动化与风险可视化。它无缝集成**子域名枚举、端口扫描、指纹识别及 Nuclei 漏洞检测能力**  
，配合 FOFA 情报聚合与数据大屏，帮助安全从业者快速梳理攻击面。  
## 🚀 一句话优势  
  
Go 原生重构资产安全引擎，集成 FOFA 情报与 Nuclei 实现攻击面自动化梳理。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">端口服务探测</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">基于 Naabu SDK 实现 SYN/CONNECT 高速扫描</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">指纹识别</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">集成 Httpx 自动识别 Web 服务技术栈</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">漏洞检测</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">内置 Nuclei v3 SDK，兼容数千社区模板</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">资产监控</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">基于 FOFA 语法周期性监控增量变化</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">数据大屏</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">ECharts 实时展示漏洞分布与资产统计</span></section></td></tr></tbody></table>  
## 🛠️ 工具使用  
  
##   
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section style="text-align: center;"><span leaf="">登录页面</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section style="text-align: center;"><span leaf="">数据大屏</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="img.png" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002812" data-ratio="0.5675925925925925" data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyTHAUXbTmxHSDfSGt5nrpgeH9ic87x1UwSoy1JljOgJxeAyt17kKcxg07vWO1dVKxONibxnDU73N1bhycJ4z2NEpicX3ib3YCndPw/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxJ9OPUVkQia56LDE3qFpCda4CPVic1OyC35z7wQfzhSp6ceXSHhJSRUKDA59bs9PgErKxA9BNJrdyBPjfakPtCLds6kIrib6WNR0/640?wx_fmt=png&amp;from=appmsg" alt="img_1.png" class="rich_pages wxw-img" data-ratio="0.5675925925925925" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002813" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section style="text-align: center;"><span leaf="">任务列表</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section style="text-align: center;"><span leaf="">漏洞详情</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="img_2.png" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002814" data-ratio="0.5675925925925925" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyM9nKySQ5dWd0mxcEaaMb7FloL4davib9UcjnQ8glgtDibzbic5Dm98YvpyMn324awABbSqAvfotz3NrOcf0icaHHviaP3NMF0GVMA/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyAzm6RAkgkhtzZFc6wBQ3XUSfa3DwMrjC1hHHTTXrd9otdZiaicV8ic4aRwR1dBa1kfHMAib9zoRwhibB3BCTsBYX91REc9pY5OOMg/640?wx_fmt=png&amp;from=appmsg" alt="img_3.png" class="rich_pages wxw-img" data-ratio="0.5675925925925925" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002816" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section style="text-align: center;"><span leaf="">FOFA查询</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section style="text-align: center;"><span leaf="">监控管理</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="img_2.png" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002815" data-ratio="0.5074074074074074" data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxNQb3h4U7Sxulkq10c1NGN7XoDI4qkvQickThMjo6d0Jbns7JBxiaThzSFDLZ3UPXftzYt0WPfsLaJ4cclNCDhqkqMiaPibCHyIJw/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwv8bTFjMb6G2Iz0ocGdIdX80QvAPlNyXJnWL4Avgwck5rrA4VCHsZQMVG35oqr11DOoz8D4J31cPGQ1FGGZVv8trJjIEkoPVA/640?wx_fmt=png&amp;from=appmsg" alt="img_3.png" class="rich_pages wxw-img" data-ratio="0.5083333333333333" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002817" data-aistatus="1"/></section></td></tr></tbody></table>  
  
## ✨ 核心亮点  
  
### 1. Go 原生高性能引擎  
  
CyberRay 采用 Go 语言重构核心扫描引擎，基于 Naabu SDK 实现 SYN 级无状态端口扫描，单机可并发处理数千目标。相比传统 Python 工具，内存占用降低 60%，扫描速度提升 5 倍以上。无需安装 Nmap 或 Python 环境，单个二进制文件即可在裸金属服务器或容器内直接运行。  
### 2. FOFA 情报驱动的资产监控  
  
系统内置 FOFA API 集成，支持将语法查询结果一键转化为扫描任务。更重要的是提供**周期性资产监控能力**  
，基于 Hourly/Daily 策略自动比对历史快照，发现新上线资产或开放端口时通过 SMTP 自动告警。这种增量检测机制让安全团队能第一时间**感知攻击面变化**  
，避免人工周期性盘点的遗漏。  
### 3. 无缝的漏洞验证闭环  
  
深度集成 Nuclei v3 SDK，不仅支持数千种社区 POC 模板，更提供完整的 Request/Response 数据包查看功能。发现漏洞后无需切换工具，直接在界面中查看原始流量包进行复现验证。配合层级化的资产管理视图（任务->主机->端口->漏洞  
），形成从发现到验证的完整闭环。  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Go 原生实现</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Gin 框架 + GORM</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">单二进制部署，无 Python/Nmap 依赖</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">SYN 无状态扫描</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">基于 Naabu SDK</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持万级并发，防火墙友好</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Nuclei v3 SDK</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">深度集成而非命令行调用</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">内存级交互，避免进程开销</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Vue 3 + TS</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">前端架构</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">类型安全，组件化维护成本低</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">MariaDB 10.11</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">关系型存储</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持复杂关联查询，稳定可靠</span></section></td></tr></tbody></table>  
## 📖 使用指南  
  
**① 准备工作**  
  
Docker 环境下直接执行 docker-compose up -d  
 启动；源码部署需安装 libpcap-dev  
 并下载 Nuclei 模板至 ~/nuclei-templates  
。  
  
**② 核心操作**  
  
登录 Web 界面创建扫描任务，可选择子域名枚举、端口扫描或 FOFA 情报导入，配置并发数后启动。资产监控任务需设置 FOFA 语法与检测周期（Hourly/Daily）。  
  
**③ 结果查看**  
  
在数据大屏查看资产统计与漏洞分布  
趋势，通过层级化资产管理树逐层下钻至具体端口和漏洞详情，支持原始请求包查看与 Excel 导出。  
  
## 📖 项目地址  
```
https://github.com/MiaCTFer/CyberRay
```  
## 💻 技术交流与学习  
  
      
如果师傅们想要第一时间获取到  
**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
  
    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，  
**内容还在持续整理中......**  
。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzPNweL1oOUEucY0N5qKrqzZCVqHq6jTWpY9iaKrRRdYYuxMQ72Phq4dfFLaf1R73eaoiaYSg74LKXtVsRr7pKrr30T0FjkkDfHM/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
