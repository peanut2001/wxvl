#  一款专业的Web安全扫描工具 | JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析  
 黑白之道   2026-03-18 01:54  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
## 工具介绍  
  
FLUX 是一款专业的Web安全扫描工具，支持JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析等功能。  
  
FLUX v3.2.1 是一款专业的Web安全扫描工具，在 v3.2.0 基础上修复了多个关键问题，包括端点URL处理、漏洞测试覆盖、WAF绕过等功能。  
  
**核心特性:**  
- 🔍 25,000+ 指纹库  
  
- 🛡️ 40+种WAF检测与绕过（含国产厂商）  
  
- 🎯 一键全功能扫描 + 单功能独立扫描  
  
- 📊 美观HTML报告 + 扫描进度实时显示  
  
- 💾 过程中自动保存结果（防止意外丢失）  
  
- 🤖 智能速率限制与流量伪装  
  
- 🔐 CSRF Token自动提取与Cookie持久化  
  
- 📥 扫描结果导入（支持 fscan/dddd + Web存活验证）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJyPDGwY4b3ckaRhsKDP9Mmg56bAya0d0TOHHF1flcff4Wr7wsNIXSGZy0tYopsibsu6ibcPTriaAsUXvIOf4ibqibHLKgf1gETbrwg/640?wx_fmt=png&from=appmsg "")  
  
**作者:**  
 ROOT4044  
## 功能特性  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMIjtj8Y2sKicuH83EW6Mn4iazmPV9I3gJS6c1RP447PdpRvgbXwULty1WeEpv8lsbcVAAJP7aiaLETT2nzKa6OvNArxAOWt4tgib3s/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKggSIMdC35icFiboibz42P0Ar6lnKFPwjML6b3UpgPtZcIVoAgHKFcExWZvLmh5CEUmOWE2QteUtM5UCMdQoQ3sxEZiaZKicwEhgWk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJv7yGvxXAuEY6UkQ04qIoNR9ibuPzV9nDzEyibNTYlBVWGQJOLr9tM64ibOvbzUicw1xqcDDK4ptaJ9SSwiceiabbrIMFAtzN0xiaWj0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJf9KaWmBEy3TPnNP9HshZx0hBS1kuzhe3mTemgz62EuZZPqMCZicS8npgjJ38jh0ibkX2gybW6ev4mIEjdYqQaM1TFS99b33fas/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKotEqdmby1DR55zULQLBF0ib6gIxa9HRCns4amic8k8s9zCiaUpfxMsJ9fyH4LWYUd8p5wskD9ULUUXOv1twUsH902t8IZPNh28Q/640?wx_fmt=png&from=appmsg "")  
## 快速开始  
### 一键全功能扫描（推荐）  
```
# 基础全功能扫描（自动跳过DNSLog盲测）python flux.py -t https://example.com --full -o report.html# 全功能扫描 + DNSLog盲测（推荐用于SSRF检测）python flux.py -t https://example.com --full --dnslog xxx.dnslog.cn -o report.html
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMLdg6LWXdTP7RYfFfrOmyH47q1ARKicRXDW1BGtqByXwwiaZL3JH3iaWnZocyqYcKD1AMoVZImoSdaibOF9l6g9KtvSyGLe3FY4AjQ/640?wx_fmt=png&from=appmsg "")  
  
这会自动启用:  
- ✅ 指纹识别 (25,000+ 规则)  
  
- ✅ API文档解析 (Swagger/OpenAPI)  
  
- ✅ 密钥有效性验证  
  
- ✅ 敏感路径Fuzzing  
  
- ✅ 参数Fuzzing  
  
- ✅ 漏洞主动测试 (SQLi/XSS/LFI/RCE/SSTI/SSRF)  
  
- ✅ WAF检测与绕过  
  
**注意:**  
- --full  
 不包含危险操作测试（DELETE），如需进行此类测试需单独开发  
  
-   
- --full  
 模式下如未指定 --dnslog  
，将自动跳过盲SSRF测试（避免交互式输入卡住）  
  
  
  
## 工具获取  
  
  
  
https://github.com/MY0723/FLUX-Webscan/  
  
  
> **文章来源：夜组安全**  
  
  
  
黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！  
  
如侵权请私聊我们删文  
  
  
**END**  
  
  
