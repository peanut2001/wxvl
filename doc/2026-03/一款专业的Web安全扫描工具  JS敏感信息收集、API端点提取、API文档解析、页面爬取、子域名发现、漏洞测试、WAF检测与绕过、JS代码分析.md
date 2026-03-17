#  一款专业的Web安全扫描工具 | JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析  
ROOT4044
                    ROOT4044  夜组安全   2026-03-17 00:01  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**NightCTI**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
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
  
- --full  
 模式下如未指定 --dnslog  
，将自动跳过盲SSRF测试（避免交互式输入卡住）  
  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260317  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[Burpsuite | API 越权测试、快速收集目标网站的所有 API2026-03-16](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496484&idx=1&sn=edfc70dfc69e40995b0b4b42aa66f8a6&scene=21#wechat_redirect)  
[AK47  | 一款跨平台的漏洞利用与安全评估工具，内置高级引擎与多种安全扩展模块2026-03-13](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496471&idx=1&sn=5561530750d9fa8f5389935b2a893aea&scene=21#wechat_redirect)  
[一款无需编译的Java静态应用程序安全测试 (SAST) 工具 | AI 辅助审计2026-03-12](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496448&idx=1&sn=dbe268da1368e1ad5a3ff8623c4292e2&scene=21#wechat_redirect)  
[Burp Suite 越权检测辅助插件2026-03-11](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496435&idx=1&sn=fbf97cd4446ff47282718de0bc8ec2bb&scene=21#wechat_redirect)  
[哥斯拉反射自定义 AES 通信插件加密器，基于Data-Flow Break与动态回调伪装的webshell生成器2026-03-10](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496423&idx=1&sn=6e2bc0d8f5180c5edde1ebcbb88df257&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
