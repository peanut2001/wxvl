#  Web 化被动漏洞扫描平台FlowEye（流量之眼）  
0xSecDebug
                    0xSecDebug  0xSecDebug   2026-01-24 00:00  
  
# Web 化被动漏洞扫描平台FlowEye（流量之眼）  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
  
  
## 📖 项目简介  
  
**FlowEye（流量之眼）**  
 是一款专为安全测试人员打造的 Web 化被动漏洞扫描平台。通过与 Burp Suite 无缝集成，FlowEye 能够实时接收并分析 HTTP 流量，自动进行多维度漏洞检测，帮助安全研究人员高效发现 Web 应用安全风险。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAALOzLMmX3C4TCQsGG1HAvsy9nCHxTV7TS8N6sqDLeDqlCJu2hhdzpVg/640?wx_fmt=png&from=appmsg "")  
### 为什么选择 FlowEye？  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">特性</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">描述</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">🎯 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">精准识别</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">内置 1000+ 指纹规则，自动识别目标技术栈</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">🧠 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">智能调度</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">根据指纹结果智能选择扫描引擎，避免无效扫描</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">⚡ </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">高效扫描</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">多引擎并行，支持 Shiro/Struts2/SQL注入/XSS 等漏洞检测</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">🖥️ </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">现代界面</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">React + TailwindCSS 构建的精美 Web UI</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">📦 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">开箱即用</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">单文件可执行，无需复杂配置</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">🇨🇳 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">中文界面</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Burp 插件完整中文汉化</span></section></td></tr></tbody></table>  
  
## ✨ 功能特性  
  
### 核心功能  
- ✅ **零配置启动**  
 - 无需任何配置文件，开箱即用  
  
- ✅ **完全嵌入**  
 - 前端 UI + 字典 + 规则全部内置到二进制  
  
- ✅ **智能指纹识别**  
 - 自动识别 Spring/Shiro/Struts2 等框架（1000+ 规则）  
  
- ✅ **多引擎扫描**  
 - SQLi/XSS/RCE/目录扫描/反序列化等  
  
- ✅ **实时监控**  
 - WebSocket 实时推送扫描结果  
  
- ✅ **漏洞去重**  
 - 智能过滤重复漏洞  
  
- ✅ **Webhook 告警**  
 - 支持飞书/钉钉/企业微信/Slack  
  
### 扫描引擎  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">引擎</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">功能</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">规则数</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">fingerprint</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">指纹识别</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">1000+</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">dirscan</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">敏感路径扫描</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">内置字典</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">shiro</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Apache Shiro 反序列化</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">100+ keys</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">spring</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Spring 框架漏洞</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">CVE-2018-1273, CVE-2022-22965</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">struts2</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Struts2 RCE</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">多个 CVE</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">sqli-fuzz</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">SQL 注入检测</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">100+ payloads</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">xss-fuzz</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">XSS 跨站脚本</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">80+ payloads</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">lfi-fuzz</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">本地文件包含</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">50+ payloads</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">nuclei</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Nuclei 模板引擎</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">可扩展</span></section></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAANekbOsiauK6bH0YG8zd5UqUQ7qWxjkOBZIkViaiahEerenfSyGpJazVicw/640?wx_fmt=png&from=appmsg "")  
## 🚀 快速开始  
### 0. 视频教程  
  
https://www.bilibili.com/video/BV1KorLBREcd  
### 1. 下载  
  
前往 Releases 页面下载最新版本：  
```
floweye-v0.1.0-final.tar.gz
```  
  
解压后包含：  
- 多平台可执行文件（macOS/Linux/Windows）  
  
- Burp Suite 插件  
  
- 使用文档  
  
### 2. 启动服务  
```
# macOS Apple Silicon./floweye-darwin-arm64# macOS Intel./floweye-darwin-amd64# Linux./floweye-linux-amd64# Windowsfloweye-windows-amd64.exe
```  
  
启动后访问：**http://localhost:8080**  
### 3. Burp Suite 集成  
1. 打开 Burp Suite  
  
1. 进入 **Extensions**  
 → **Installed**  
  
1. 点击 **Add**  
，选择 floweye-burp-plugin-1.0.0.jar  
  
1. 确认插件加载成功  
  
1. 通过 Burp 浏览目标网站，FlowEye 自动接收流量并扫描  
  
## 📚 使用教程  
### 基础配置  
  
FlowEye 支持零配置启动，如需自定义配置，在可执行文件同目录创建 config.yaml  
：  
```
server:  port: 8080# 服务端口host: "0.0.0.0"# 监听地址filter:domain_whitelist:# 域名白名单    - "*.example.com"    - "api.target.com"enable_dedup: true# 启用去重webhook:enabled: trueprovider: feishu# 飞书/钉钉/企业微信webhook_url: "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"min_severity: high# 最低告警级别
```  
### Webhook 告警配置  
  
支持多种告警平台：  
  
**飞书**  
```
webhook:  enabled: true  provider: feishu  webhook_url: "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"  secret: "your-secret"  min_severity: high
```  
  
**钉钉**  
```
webhook:  enabled: true  provider: dingtalk  webhook_url: "https://oapi.dingtalk.com/robot/send?access_token=xxx"  secret: "your-secret"  min_severity: high
```  
  
**企业微信**  
```
webhook:  enabled: true  provider: wecom  webhook_url: "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"  min_severity: high
```  
### 引擎管理  
  
在 Web UI 的 **扫描引擎**  
 页面可以：  
- 启用/禁用特定引擎  
  
- 查看引擎统计信息  
  
- 调整扫描参数  
  
## 📊 界面预览  
### 仪表盘  
  
实时统计流量、漏洞、指纹识别结果  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAAwMqzcAwP3Rr3cu7pNAwySjfcBeEsdgVU96HWicU2cx2jXQ5Vluvc8CQ/640?wx_fmt=png&from=appmsg "")  
### 流量监控  
  
查看所有 HTTP 流量，支持搜索和过滤  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAA8rJGQSnXm9UC95PaIQ8RbjicCbxpnuy9VdkyJttUBkySBzrdPcnyCZg/640?wx_fmt=png&from=appmsg "")  
### 漏洞管理  
  
漏洞列表、详情、复测、导出报告  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAAc9bDdxHicfVVl1ic1BBPM2kYycuILGmicd2ibZysVVgDMSI4suuXEnwpmw/640?wx_fmt=png&from=appmsg "")  
### 指纹识别  
  
查看识别到的技术栈和框架  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAA0fmlBe39ve8HyviafWaGCBvFHpuZibVddR1vym80HMqIWdnsfAQGvVGg/640?wx_fmt=png&from=appmsg "")  
### 扫描引擎配置和管理漏洞检测核心组件  
  
  
### 系统设置  
  
配置 Webhook、白名单、引擎参数  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFsGp6KrYsYyb7Be5T39lAAwh7cxT4jiaNribyWKdm2qTNC6JapaoVlzjkKdpibSFqymiafYeZhuI5RqA/640?wx_fmt=png&from=appmsg "")  
  
  
## 📖 项目地址  
```
https://github.com/YingxueSec/Floweye-yyyxxx.cc/tree/main
```  
## 💻 威胁情报推送群  
>   如果师傅们想要第一时间获取到**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
>  如果师傅们想要获取  
**网络安全相关知识内容**  
，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**  
。  
  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg "")  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
  
