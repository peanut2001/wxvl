#  Nuclei 漏洞扫描图形化工具 | POC 管理、FOFA/Hunter/Shodan 资产测绘、AI 辅助分析、漏洞报告生成  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-02-24 05:10  
  
📌各位可以将公众号设为星标⭐  

  
📌这样就不会错过每期的推荐内容啦~  

  
📌这对我真的很重要！  

  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
    

  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  

  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  

  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  

## 工具介绍  

  
**Nuclei GUI Scanner** 是一款基于 PyQt5 开发的 Nuclei 漏洞扫描图形化工具。它提供了友好的可视化界面，并集成了 POC 管理、资产搜索、AI 辅助分析等多种实用功能。  

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKSagHLpYpbeZQ7wH8LRib3YWxc5xoKAiaItSibicJzjpktKG4rurLkRoInIMJDIsDIaXnJIbeWp4ZWmhwHUatu9L8ibApDVMLdMfO4/640?wx_fmt=png&from=appmsg "")  

## 功能截图  

  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKsEdWVDarKuYiccOicB3arsgdhSrxNboPyV81cv6quJ5VNuZMbutfNCTLuQkOKVuasqVCXrkp9umEnlwEVYAVXHE2uJdYOCRiax8/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMIs3pNvOmyHPaIpibicdTVZibnu1dgFkHYbqdibuExdQ6B8rVfhU8ZvZ9P9CD0ksw2IpH1XW73SHwMvl4WGwliblWKupV7t8R7nBE3w/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESML15r87BTpicVujuTNYxeGfvXmek6jszESz3BLpB2XQwa84qUhoCAnxhZn3SibLxCU1nxbJpK2YLvjibasM9nxzvFRR2sfIOhqxsM/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKI3ciasiaxnSQ9Tfrt8eYjbiacauibMvIqWX86l0hgNSPWpiboAgh3a5hGPdAWHpjAOeicL1yrMZ1xfUcxZVsDEW9aau3GtUZ9YK7PU/640?wx_fmt=png&from=appmsg "")  

## 功能介绍  

### 1. 仪表盘  

- 扫描统计概览（总扫描次数、发现漏洞数、POC 数量）  
  
- 漏洞趋势图表  
  
- 最近扫描历史记录  
  
- 漏洞严重程度分布图  
  

### 2. 漏洞扫描  

- 支持对单个或多个目标进行批量扫描  
  
- 可从多个 POC 模板中进行选择  
  
- 实时显示扫描进度与结果  
  
- 支持暂停、恢复或取消扫描任务  
  
- 扫描结果可导出为 CSV 或 HTML 格式  
  

### 3. 任务队列管理  

- 支持多任务排队执行  
  
- 可设置任务优先级（紧急/高/普通/低/后台）  
  
- 支持断点续扫功能  
  
- 实时监控任务状态  
  
- 显示任务的创建时间、开始时间及执行耗时  
  

### 4. POC 管理  

- 浏览和搜索 POC 列表  
  
- 按严重程度或标签进行筛选  
  
- 支持从文件或目录导入 POC  
  
- 支持在线同步 POC（从 nuclei-templates 官方仓库）  
  
- 内置 POC 编辑器（支持语法高亮）  
  
- 可对 POC 进行快速测试  
  
- 提供 POC 收藏管理功能  
  

### 5. 资产搜索  

  
集成了多个资产搜索引擎：  

<table>
<thead>
<tr>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">引擎</th>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">FOFA</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">国内主流资产搜索引擎</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Hunter</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">奇安信鹰图平台</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Quake</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">360 网络空间测绘</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Shodan</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">国际知名搜索引擎</td>
</tr>
</tbody></table>
- 可将搜索结果直接导入为扫描目标  
  
- 保存搜索历史记录  
  

### 6. AI 助手  

  
支持 OpenAI 兼容接口（如 DeepSeek、通义千问、GPT 等）：  

<table>
<thead>
<tr>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">功能</th>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">FOFA 语法生成</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">根据漏洞描述生成 FOFA 搜索语法</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">POC 生成</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">根据漏洞描述生成 Nuclei YAML POC</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">漏洞分析</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">深入分析漏洞原理并提供修复建议</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">智能推荐</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">根据目标特征推荐适用的 POC</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">漏洞报告生成</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">生成符合 SRC 提交格式的漏洞报告</td>
</tr>
</tbody></table>
### 7. 漏洞报告生成  

  
支持对扫描结果一键生成 AI 漏洞报告：  

- 符合补天/SRC 提交的报告格式  
  
- 包含详细技术分析的报告  
  
- 简要漏洞说明报告  
  
- 修复建议报告  
  

### 8. 设置  

- **扫描参数**：超时设置、并发数、重试次数、代理配置  
  
- **FOFA 配置**：API URL、邮箱、API Key  
  
- **AI 配置**：支持多预设配置、模型选择、API 测试  
  
- **主题设置**：经典蓝、深邃蓝、清新绿、优雅紫  
  

## 快捷键  

<table>
<thead>
<tr>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">快捷键</th>
<th align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);">功能</th>
</tr>
</thead>
<tbody><tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+N</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">新建扫描</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+S</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">保存设置</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+E</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">导出结果</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+F</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">聚焦到搜索框</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+L</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">显示日志</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">F5</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">刷新 POC 列表</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Escape</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">停止扫描</td>
</tr>
<tr>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">Ctrl+1~6</td>
<td align="left" style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;">快速切换页面</td>
</tr>
</tbody></table>
## 配置说明  

### Nuclei配置  

```
将官方Nuclei放入bin目录下  
在程序设置中将扫描参数设置选择“跳过探测”和“详细日志”进行打勾  

```  
### AI 配置  

  
支持任何 OpenAI 兼容接口：
    API URL: https://api.deepseek.com[1] (或其他兼容接口)    API Key: 你的 API Key    模型: deepseek-chat / gpt-4o / qwen-turbo 等    

### FOFA 配置  

```
API URL: https://fofa.info  
Email: 你的 FOFA 邮箱  
API Key: 你的 FOFA API Key  

```  
### 代理设置  

  
支持 HTTP/SOCKS5 代理：
    http://127.0.0.1:7890[2]    socks5://127.0.0.1:1080  

  
关注微信公众号后台回复“**20260224** ”，即可获取项目下载地址  

  
关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群  

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
  
- 一键Kill 火绒 defender 工具 **HDKiller**（包含源码）  
  
- win11 一键kill 360工具 **InjectKill**（包含源码）  
  
- win11 一键kill defender工具**win11_df-killer**（包含源码）  
  

  
后续将不断更新到内部圈子中 欢迎加入圈子  

  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2nhghttp9mQhic3LJWsCj8Jb4QWibnjmRqic7M9W746srJZlLKQg6mmV7cKrwhWCOauLlJPzLzry0iaRQ/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=7 "image")  

### 引用链接  
  
[1]  
https://api.deepseek.com  
  
[2]  
http://127.0.0.1:7890  
  
