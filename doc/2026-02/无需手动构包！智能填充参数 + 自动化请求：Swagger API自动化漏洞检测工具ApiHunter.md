#  无需手动构包！智能填充参数 + 自动化请求：Swagger API自动化漏洞检测工具|ApiHunter  
11firefly
                    11firefly  渗透安全HackTwo   2026-02-02 16:00  
  
0x01 工具介绍  
  
  
Swagger 文档未授权访问是 API 渗透测试的高频突破口，但人工手动构造请求包、填充参数不仅耗时耗力，还极易遗漏关键接口。今天为大家推荐星球成员 @11firefly11 倾力开发的开源利器 ——ApiHunter！它专为解决上述痛点而生，支持 Swagger 2.0/3.0 文档一键解析，无需手动抓包或构包，自动提取所有接口端点、请求方法与参数定义。内置 100 + 敏感信息检测规则，能秒级捕获密钥、Token、数据库连接串等泄露数据，搭配交互式重发功能，让未授权 API 测试效率翻倍，现已在 GitHub 开源，助力数据抓取与 API 测试高效稳定推进！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQlrGt1Ax62pRX5ibbiajUkz5Quqkw9iaMX1BUx0Y5nO2hC0fGTichGAibjQ/640?wx_fmt=png&from=appmsg "")  
  
注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾 #渗透安全HackTwo**  
  
0x02   
功能简介  
  
  
✨ 主要特性  
  
多类型文档一键解析：  
支持 Swagger 2.0/3.0 JSON 文档、ASP.NET Web API Help Page 网页一键导入，自动解析所有接口端点、请求方法及参数定义，省去手动抓包 / 构包的繁琐，覆盖现代前后端分离架构与传统.NET 应用场景。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OmwqKZeElXENWD1JyQW1JPqWLLb0yq2AH9iaicfxADfZaXISy59jSL9og/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OftzEJ0tMyTuXicmibtYjfNW1HiaW7bgIZvNLGFj6rPzuRIRYRAcdHNbrg/640?wx_fmt=png&from=appmsg "")  
  
智能参数填充与多格式测试：  
针对 POST/PUT 请求自动识别 id、email 等参数并填充测试值，同时生成 URL 参数、JSON Body、Form Body 三种格式数据包测试，确保参数传递方式全覆盖，无漏洞遗漏；也支持自定义参数值，适配个性化测试需求。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OeQ6CAhgrknXfIjHbiazrxo2KcChRNzfzeVDibyhm30krfbpTLwicBv8bg/640?wx_fmt=png&from=appmsg "")  
  
自动化漏洞检测能力：  
智能识别 upload/file 等上传接口，自动构造 multipart/form-data 请求并上传 XSS 测试文件、普通文本文件验证上传漏洞；内置 SQL 注入探测引擎，可识别多数据库报错指纹，实现高频漏洞自动化检测。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OnKFyCrgziaVpBOibkkHRzFBm0AsW4w7qbnmSqicZF8gw3GwLKQzQNrydw/640?wx_fmt=png&from=appmsg "")  
  
敏感信息深度扫描：  
内置 100+ 高精度检测规则，覆盖云服务密钥、各类 Token、数据库连接串、手机号 / 身份证等隐私信息，支持自定义规则，敏感信息在响应结果中红色高亮展示，便于快速定位。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OC6KCV8cia5FdgZicYhjmDxhw2b9dHzGMAU1ib3qhHVicQibSHFV5zsicuYdg/640?wx_fmt=png&from=appmsg "")  
  
智能结果去重与过滤：  
基于 “状态码 + 响应长度” 指纹去重，过滤 404/500 等重复无效响应；支持状态码自定义过滤，可屏蔽无价值结果，聚焦差异化高危信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQlrGt1Ax62pRX5ibbiajUkz5Quqkw9iaMX1BUx0Y5nO2hC0fGTichGAibjQ/640?wx_fmt=png&from=appmsg "")  
  
安全防护与灵活适配：  
提供 “安全模式”，自动拦截 DELETE/PUT 等高危方法、过滤高危关键词接口，防止误删数据；支持 HTTP/HTTPS/SOCKS5 代理配置，可自定义请求头（Cookie/Authorization），适配鉴权场景与流量转发需求。  
  
交互式操作与报告导出：  
双击结果即可查看标准 HTTP 格式数据包，支持编辑请求头 / 体并即时重发；响应内容自动格式化高亮，测试结果可导出为 Excel 格式，包含完整请求 / 响应信息，便于报告生成与二次验证。  
###   
  
0x03更新说明  
```
1.增加wsdl,wadl接口文档提取以及测试
2.优化swagger接口提取功能
3.优化变异测试功能
```  
  
  
0x04 使用介绍  
  
📦  
使用指南  
  
### 使用前请确保已获得目标系统的合法授权，本工具仅用于授权的安全测试。  
1. **启动程序**  
  
1. 双击 ApiHunter.exe  
 即可启动，开箱即用。  
  
**开始任务**  
- **方式一（单目标）**  
：输入 URL 和接口路径，点击测试。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4O7onoEVIgN9ItHpQo5gEnS9TWNs6BgNaxEGNTWOFB7jXDIbuH0vLYrg/640?wx_fmt=png&from=appmsg "")  
  
**方式二**  
：切换到“接口文档”区域，输入 Swagger/ASP.NET 地址，点击 [导入]  
，然后点击 [swagger]  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQUhNBvKJC4bX7ancdCjlz30qlT4GDdXBYCpvZNiaBvWLrciagMwXibTRA/640?wx_fmt=png&from=appmsg "")  
1. **查看结果**  
  
1. 扫描结果实时显示，敏感信息红色高亮。  
  
1. 双击行查看详情，右键可导出或复制。  
  
###   
  
  
**0x05 内部VIP星球介绍-V1.4（福利）**  
  
        如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，  
**每天更新1day/0day漏洞刷分上分****(2026POC更新至5112+)**  
**，**  
包含全网一些**付费扫描****工具及内部原创的Burpsuite自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**  
。shadon/Zoomeye/Quake/  
Fofa高级会员，CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"   
**星球**  
 "有优惠券名额有限先到先得  
**❗️**  
啥都有  
**❗️**  
全网资源  
最新  
最丰富  
**❗️****（🤙截止目前已有2400+多位师傅选择加入❗️早加入早享受）**  
  
****  
最新漏洞情报分享：  
https://t.zsxq.com/lFN5j  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.4版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20260203获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.4（AI自动化工具）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.全新升级BurpSuite2025.12专业(稳定版)**  
  
**4. 最新xray1.9.11高级版下载Windows/Linux**  
  
**5. 最新HCL AppScan Standard**  
  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
  
上一篇文章：  
[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)  
  
  
