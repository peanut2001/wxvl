#  还在手动翻漏洞公告？这款工具自动聚合多源情报并生成Markdown简报  
0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-02 02:11  
  
# TL-ICScan 漏洞情报聚合与分析工具  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
> **项目地址在文章底部哦**  
  
  
> **开源安全情报工具**  
 |本地化 |多源聚合 |智能分析  
> 本仓库为 TL-ICScan 的完整开源代码与采集脚本集合。  
> **TL-ICScan 由天禄实验室开发并开源维护。**  
  
## 项目简介  
  
TL-ICScan 是由**天禄实验室**  
开发的一款面向安全研究人员、红队与蓝队的**本地化漏洞情报聚合与分析工具**  
。  
  
**一句话原理解析：**  
> **Python 负责“进货”，Rust 负责“管库”。**  
> Python （采集端）：像勤劳的采购员，去 NVD、GitHub、Exploit-DB 等网站抓取最新的漏洞情报，并把它们“翻译”成统一格式。Rust （核心库）：像高效的仓库管理员，负责把 Python 抓回来的海量数据快速存入本地数据库，并提供毫秒级的查询服务。Web UI（展示端）：直接读取本地数据库，为您提供无需联网、随查随用的可视化查询体验。  
  
  
在日常的安全运营与研究中，我们面临着情报源分散（NVD， CISA， 厂商公告， Exploit-DB）、数据格式不统一、以及过度依赖在线查询等痛点。TL-ICS可以旨在解决这些问题：  
- **多源聚合**  
：自动采集并标准化 NVD、CISA KEV、MSRC、Exploit-DB、GitHub PoC 等多方情报。  
  
- **本地私有**  
：所有数据存储于本地 SQLite 数据库，查询无需联网，保障作隐蔽性。  
  
- **智能关联**  
：自动关联漏洞的 PoC 状态、EPSS 评分与厂商公告，提供上帝视角。  
  
- **纯粹情报**  
：专注于“情报”本身，不绑定资产管理，轻量级且易于集成。  
  
- **全平台支持**  
：原生支持 Windows、Linux 与 macOS，提供统一的 CLI作体验。  
  
![TL-ICScan 仪表盘](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFYFysGjO69ozDngwweUfTrCNZQgNwUGRzmQ1SLZIxWdRaWAXo89aGIygwn2N4H5XfTibA8TjBqhHA/640?wx_fmt=png&from=appmsg "")  
## 核心功能  
1. **多源采集 （Collectors）**  
： 模块化 Python 脚本，支持 NVD， CISA KEV， MSRC， Exploit-DB， EPSS， GitHub PoC 等。  
  
1. **数据标准化**  
： 将异构数据清洗为统一的格式 （JSONL）.NormalizedCVE  
  
1. **高性能存储**  
： Rust 核心引擎处理数据入库与索引，支持百万级记录秒级查询。  
  
1. **智能简报 （Digest）**  
： 基于 YAML 配置关注列表 （Watchlist），自动生成 Markdown 格式的每日/每周漏洞简报。  
  
1. **灵活导出**  
： 支持导出为 JSON/CSV 格式，便于导入 Excel 或其他分析工具。  
  
## 最新更新 （v0.6.0）  
  
**发布日期**  
：2025-12-11  
  
本次更新包含重大改进和bug修复：  
### 新特性  
- **统一配置管理**  
： 新增 模块，支持环境变量配置config.py  
  
- **统一日志系统**  
： 所有模块使用标准 logging 模块，支持日志级别控制  
  
- **错误码体系**  
： 新增统一的错误码定义（E001-E999），便于问题排查  
  
- **改进的配置示例**  
: 包含4个详细示例和完整字段说明watchlist.yml  
  
- **单元测试**  
： 新增采集器单元测试，提高代码可靠性  
  
#### 4. 常用命令  
  
所有作通过 CLI 工具完成（假设位于项目根目录）：  
  
**启动 Web UI （可视化仪表盘）**  
```
# 启动 Web 界面，默认访问 http://localhost:8501
streamlit run web_ui/dashboard.py

```  
  
**查询漏洞列表**  
```
# 查询最近 7 天发布的的高危漏洞
./tianlu-intel-core/target/release/tianlu-intel-core list --since 7d --severity HIGH --db tianlu_intel_v2.db

```  
  
**查看漏洞详情**  
```
# 查看特定 CVE 的详细情报（包含描述、CVSS、PoC、参考链接等）
./tianlu-intel-core/target/release/tianlu-intel-core show CVE-2024-12345 --db tianlu_intel_v2.db

```  
  
**生成情报简报**  
```
# 根据 watchlist.yml 生成简报
./tianlu-intel-core/target/release/tianlu-intel-core digest --config watchlist.yml --since 1d --db tianlu_intel_v2.db

```  
## 配置说明 （Watchlist）  
  
通过修改 定制您关注的情报：watchlist.yml  
```
- name: "Windows 核心组件"
  vendors: ["microsoft"]
  products: ["windows_server_2019", "windows_10"]
  severity_min: "HIGH"

- name: "VPN 设备"
  keywords: ["vpn", "firewall", "pulse_secure"]
  epss_min: 0.1 # 仅关注利用概率 > 10% 的漏洞

```  
## 项目状态  
- **开发状态**  
： 活跃维护中  
  
- **稳定性**  
： 生产就绪  
  
- **测试覆盖率**  
：持续改进中  
  
- **文档完整度**  
： 完善  
  
## 数据源  
  
感谢以下项目和组织提供的数据源：  
- NVD——国家漏洞数据库  
  
- CISA KEV——已知被利用的漏洞  
  
- Exploit-DB - 利用数据库  
  
- EPSS - 漏洞预测评分系统  
  
- Microsoft MSRC - Microsoft 安全响应中心  
  
  
  
  
## 📖 项目地址  
```
https://github.com/tianlusec/TL-ICScan?tab=readme-ov-file
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
  
