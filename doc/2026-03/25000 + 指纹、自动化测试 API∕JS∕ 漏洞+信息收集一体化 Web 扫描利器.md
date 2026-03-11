#  25000 + 指纹、自动化测试 API/JS/ 漏洞+信息收集|一体化 Web 扫描利器  
MY0723
                    MY0723  渗透安全HackTwo   2026-03-11 16:01  
  
0x01 工具介绍  
  
FLUX 是一款面向实战的一体化 Web 安全扫描工具，内置**25000 + 海量指纹库**  
，覆盖主流 CMS、中间件、框架与安全设备。工具集**信息收集、API 自动化测试、JS 敏感信息挖掘、漏洞检测、WAF 识别与绕过**  
于一体，支持 Swagger/OpenAPI 解析、差分验证、智能流量伪装与 HTML 报告生成。凭借低误报、高覆盖、强实战的特性，FLUX 可快速完成资产测绘、接口审计、漏洞探测与风险梳理，为渗透测试工程师与安全运维人员提供一站式、高效率的 Web 安全检测能力。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWAib4T41LnBUdADgpoDVLRw8Ob6cq7offibLHJ8mjh4fHIbeDFaH3SBJI8ewibibibyAFIN3J6eROQsjJvYgRtPc3du9prOaMHJ704/640?wx_fmt=png&from=appmsg "")  
  
注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾 #渗透安全HackTwo**  
  
0x02   
功能介绍  
  
✨主要功能  
### 🔍 信息收集  
- JS 敏感信息收集：云密钥、令牌、硬编码凭据（带熵值验证）  
  
- API 端点提取：自动抽取 JS 中接口路径  
  
- API 文档解析：支持 Swagger/OpenAPI/Postman  
  
- 页面爬取：深度爬取，提取链接与表单子域名发现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAV8tD5ljKzJ5OwDh6kLW8JicENm2UbKlbZwMNYPq4amk5iass6LOHD5pKrN9l4YyIR1HPzdrh2N319ZEdnhx8RzZOic6YRw730ibww/640?wx_fmt=png&from=appmsg "")  
### 🎯 指纹识别（增强版）  
- 指纹库：25000 + 规则，覆盖 CMS、框架、中间件、安全设备等  
  
- 多特征交叉验证、Favicon Hash、置信度评分机制  
  
- 多重匹配 + 强特征校验，大幅降低误报  
  
### 🛡️ 漏洞测试（差分检测）  
- 支持 SQLi、XSS、LFI、RCE、XXE、SSTI、SSRF  
  
- 云安全：Access Key 泄露、存储桶遍历 / 接管 / 未授权访问  
  
- 差分对比测试，误报率降低 80%+  
  
### 🔥 WAF 检测与绕过  
- 识别 40 + 种 WAF，兼容阿里云盾、安全狗、长亭等国产设备  
  
- 支持编码、混淆、注释、HTTP 头绕过等多种策略  
  
### 🤖 智能防护规避  
- 自适应请求限速、浏览器指纹轮换  
  
- 自动提取 CSRF Token、Cookie 持久化、登录态扫描  
  
### 🔬 JS 代码分析  
- 混淆代码还原、DOM XSS 污点分析  
  
- API 参数提取与自动化 Fuzz  
  
### 📊 报告生成  
- HTML 可视化报告、JSON 格式输出  
  
- 完整记录请求响应与漏洞详情  
  
### 0x04 更新介绍  
```
✨ 新增功能 & 优化--verify-endpoints 参数，验证提取的 API 端点是否真实存在（减少误报）
✨ 新增 SQL 注入误报过滤机制，自动识别测试代码/文档中的 SQL 错误
✨ 新增 XSS 误报过滤机制，过滤注释/字符串/示例代码中的 payload
✨ 增强 Swagger/OpenAPI 文档解析，支持更多格式自动发现
✨ 改进漏洞验证逻辑，降低误报率
```  
  
  
0x04 使用介绍  
  
📦安装  
指南  
  
安装python依赖库  
```
pip3 install -r requirements.txt
```  
### 单目标扫描  
```
python flux.py https://example.com
```  
### 批量扫描(逗号分隔)  
```
python flux.py "https://example1.com,https://example2.com"
```  
### 批量扫描(文件)  
```
python flux.py urls.txt
```  
### 深度扫描  
```
python flux.py https://example.com -d 5
```  
### 漏洞主动测试 (SQLi/XSS/LFI/RCE/SSTI/云安全)  
```
python flux.py https://example.com --vuln-test
```  
### 云安全测试  
```
# 基础云安全测试（包含在--vuln-test中）
python flux.py https://example.com --vuln-test -o report.html
# 一键全功能扫描（包含云安全测试）
python flux.py https://example.com --full -o report.html
```  
### 敏感路径fuzzing  
```
python flux.py https://example.com --fuzz-paths
```  
### 生成HTML报告  
```
python flux.py https://example.com -o report.html
```  
### 标准扫描 (推荐)  
```
python flux.py https://example.com --vuln-test -o report.html
```  
### 全面扫描 (深度)除delete测试除外，如需要单独加参数--test-delete  
```
python flux.py https://example.com --full --dnslog xxx.dnslog.cn -o report.html
```  
### 使用代理扫描  
```
python flux.py https://example.com --vuln-test --proxy http://127.0.0.1:8080 -o report.html
```  
### SSRF测试（带DNSLog）  
```
# 方式1: 命令行指定DNSLog域名（推荐，非交互式）
python flux.py https://example.com --vuln-test --dnslog xxx.dnslog.cn -o report.html
# 方式2: 交互式输入（扫描过程中提示输入）
python flux.py https://example.com --vuln-test
# 提示: 请输入DNSLog子域名 (例如: xxx.dnslog.cn):
# 方式3: 一键全功能扫描 + DNSLog
python flux.py https://example.com --full --dnslog xxx.dnslog.cn -o report.html
```  
  
**获取DNSLog域名:**  
1. 访问   
https://dnslog.cn  
  
1. 点击"Get SubDomain"获取子域名（如：  
abc123.dnslog.cn  
）  
  
1. 使用   
--dnslog abc123.dnslog.cn  
 参数运行扫描  
  
1. 扫描完成后回到   
https://dnslog.cn  
 查看DNS解析记录  
  
  
  
**0x05 内部VIP星球介绍-V1.5（福利）**  
  
          
如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，  
**每天更新1day/0day漏洞刷分上分****(2026POC更新至5522+)**  
**，**  
包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**  
。shadon/  
Hunter  
/  
0zone  
/  
Zoomeye  
/Quake/  
Fofa高级会员/  
AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"   
**星球**  
 "有优惠券名额有限先到先得  
**❗️**  
啥都有  
**❗️**  
全网资源  
最新  
最丰富  
**❗️****（🤙截止目前已有2500+多位师傅选择加入❗️早加入早享受）**  
  
****  
最新漏洞情报分享：  
https://t.zsxq.com/VuWGw  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20260312获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.5（AI自动化）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.全新升级BurpSuite2026.2专业(稳定版)**  
  
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
  
  
