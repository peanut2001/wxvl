#  【红队必备】info_scan集成30+工具的集成化漏洞扫描平台(从资产发现到漏洞验证的闭环管理)  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-21 03:38  
  
# info_scan  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
> 注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
"  
**0xSecDebug**  
"  
**设为****星标**  
**⭐️**  
"  
**否****则可能就看不到了啦！**  
> **项目地址在文章底部哦**  
  
  
## 工具简介  
  
info_scan是集成30+安全工具的自动化漏洞扫描系统，支持Docker部署与资产闭环管理，适合企业安全团队进行批量漏洞发现与资产安全评估。  
## 🚀 一句话优势  
  
集成30+安全工具的开箱即用漏洞扫描与资产安全管理平台。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-transform: uppercase;min-width: 85px;text-align: left;"><section><span leaf="">功能名称</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-transform: uppercase;min-width: 85px;text-align: left;"><section><span leaf="">一句话说明</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">多引擎漏洞扫描</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">集成Nuclei/Xray/Fscan等30+扫描器</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">资产自动发现</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">支持Fofa/Shodan/子域名多源采集</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">未授权专项检测</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">覆盖Redis/MongoDB/Docker等10类服务</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">目录与指纹识别</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">自动识别高危资产并分类标记</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">态势感知大屏</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">可视化展示整体安全风险态势</span></section></td></tr></tbody></table>  
## ✨ 核心亮点  
  
**1. 工具链深度集成**  
  
无需逐个安装配置，平台已预置Struts2、WebLogic、Shiro、SpringBoot、ThinkPHP等专项扫描器，以及Nuclei、Xray、Fscan、Crawlergo等通用工具。你通过Web界面勾选即可调用，避免了工具间的格式转换和参数适配问题。实际测试中，从资产导入到批量扫描启动可在3分钟内完成。  
  
**2. 资产闭环管理**  
  
系统不仅发现漏洞，更管理资产全生命周期。通过Fofa/Shodan接口自动采集资产后，支持资产优化（按关键字过滤）、高危资产识别（基于指纹规则）、全局白名单配置（避免误扫）。2025年12月版本更新的态势感知大屏，可实时展示资产分布与风险趋势，适合企业定期汇报场景。  
  
**3. 企业级辅助功能**  
  
平台内置JWT密钥爆破、网络诊断（检测扫描器到目标网络连通性）、代理轮切（支持节点随机切换与响应时间查询）等实用功能。Docker版本采用平台与数据库分离架构，通过自定义网络通信，支持版本对应管理（V0.4.3需搭配V0.1.3数据库），确保环境一致性。  
## ✨ 工具使用  
## 系统首页  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwDZxmXuvbKKBxWok9d1YfXxmgYUfFXT7DTLyU2co8sNorHjOsfice91JQ4hdjNIoKTrzqibtpImG2zLJbaj2EMFVsB6FodqZrJw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyRCdRVxx0SeZQbdJauElCzPAgDRic0GqrmvFYwNT6BXViaicW7ghmAZXQHmSoFJ3kaCETcHVxFas22hsBIXzibBscvQMkZsBqhYlY/640?wx_fmt=png&from=appmsg "")  
### 态势感知大屏  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyvcGIWmmv2HOf1WtakWtC3TB95EsJsicUKaCOJ2U5QqoSEibMLeqNkWFzZrBS3q7alRLibkHQKnmSROz5NLZaDmTlaticaeBjVJgk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzdjCcCKDSLmMSgljXWKeGZJvSEvbOibOibS00cZOUnBIUB1JicvgNsnrmekpIqEKwpv4mXIZxjY2Viaia6Sr73WTbafXa5JkfSlllA/640?wx_fmt=png&from=appmsg "")  
### IP基础信息查询  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxSjvrn3MfSAZ94ZGDGcvbiccLYVlWMUVlqDM6UFYu4Jr2FicOh1hasmmic3uMHfqoB9CNQTYWYiaDquLSwYibcLbm2yk1WEYbickZ3M/640?wx_fmt=png&from=appmsg "")  
### 目录扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxkMwqzYpEExXCTVJAEmRIjdG09CT8PTz6zVmGQTHb4bpNt7xdkzb8a5V5UwWLnuy1aSSoXOrPf6grHiakmgBxxianypdsYiccCro/640?wx_fmt=png&from=appmsg "")  
### 资产收集  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzGnBic2Bm0sAIeoIpogCodBuSLQPx83VsE8Nv7k1DRYL1KmZoEbNVLkyXDbNIMHNE5y4hE0D7qcx5X1GRrm9Tv0jkfhzsVibK3s/640?wx_fmt=png&from=appmsg "")  
### 批量扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwAjBkscwLVo7xibSn9vz7avTibdjvQ9veJZduNt1D2zoZFPAK89xlBdyvSUbFyPcAUmXWTibC0atNPNwWuVrQw6Lf6KYhC5wLE64/640?wx_fmt=png&from=appmsg "")  
### 剩余的其他功能  
1. JNDI服务管理  
  
1. fofa语法日志  
  
1. 字典配置  
  
1. 超级管理员复核  
  
1. DNS日志  
  
1. 系统配置  
  
1. 网站导航  
  
1. icon_hash计算  
  
1. 资产优化  
  
1. 服务重启  
  
1. 识别高危资产，得到高危资产  
  
1. 高危资产特征录入系统  
  
1. 全局资产白名单配置  
  
1. 代理配置  
  
1. JWT爆破  
  
1. 网络诊断  
  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-transform: uppercase;min-width: 85px;text-align: left;"><section><span leaf="">技术/特性</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-transform: uppercase;min-width: 85px;text-align: left;"><section><span leaf="">说明</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-transform: uppercase;min-width: 85px;text-align: left;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">Docker容器化</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">平台与MySQL分离部署</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">版本严格对应，避免环境冲突，支持快速扩容</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">Python/Flask后端</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">主服务与目录扫描服务分离</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">模块解耦，单个服务崩溃不影响整体运行</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">Nginx反向代理</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">支持自定义端口映射与401认证</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">可配置访问控制，增强Web界面安全性</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">开源工具生态</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">集成Nuclei、Xray、Crawlergo等</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;text-align: left;"><section><span leaf="">复用成熟POC库，保持检测规则持续更新</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">MySQL数据持久化</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">资产、配置、扫描结果结构化存储</span></section></td><td style="font-size: 16px;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;text-align: left;"><section><span leaf="">支持历史数据查询与趋势分析</span></section></td></tr></tbody></table>  
## 📖 使用指南  
  
**① 准备工作**  
  
Docker部署需严格匹配平台与数据库版本（如V0.4.3平台搭配V0.1.3数据库），拉取镜像后创建自定义网络使容器互通。启动后必须进入"系统配置-账号配置"完成API密钥等参数设置，否则功能无法正常使用。  
  
**② 核心操作**  
  
通过Web界面导入资产（支持手动输入、Fofa/Shodan接口导入或文件上传），在"重点资产"模块确认高危目标识别结果，勾选所需扫描器（漏洞扫描/目录扫描/未授权检测等），配置线程与端口范围后批量启动任务。  
  
**③ 结果查看**  
  
扫描完成后在"态势感知大屏"查看风险概览，点击具体项目查看CVSS评分的详细报告，支持导出资产列表与漏洞详情。目录扫描结果自动保存，可通过浏览器插件FindSomething联动分析原始响应文件。  
  
## 📖 项目地址  
```
https://github.com/huan-cdm/info_scan?tab=readme-ov-file
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
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyqn6yBXpWohu1pzB77GClqRpdqHnp4ZCqIxicGWm59nen3Nwd7Gz9r1EYibvbRgLT3o7XIXvtR1zpUiaHx1wIDJOVxJTodeYia9so/640?wx_fmt=png&from=appmsg "")  
  
  
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
  
