#  Web安全扫描工具 | JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析  
ROOT4044
                    ROOT4044  夜组安全   2026-03-06 00:00  
  
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
  
FLUX v3.0 是一款专业的Web安全扫描工具，JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析等功能。，新增完整规则库、美观HTML报告、可视化统计等功能。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMKAzKEegY6IjMbkiashUvfbbyFwvPGlHicRWUwC1kRYmKdecJYjeXsD77bqQJRG2rtOQDDAovegR8Z4Liaj7jCeQWxx1AiciaCRWPkc/640?wx_fmt=png&from=appmsg "")  
  
**核心特性:**  
- 🔍 25,000+ 指纹库  
  
- 🛡️ 40+种WAF检测与绕过（含国产厂商）  
  
- 🎯 一键全功能扫描  
  
- 📊 美观HTML报告  
  
- 🤖 智能速率限制与流量伪装  
  
- 🔐 CSRF Token自动提取与Cookie持久化  
  
**作者:**  
 ROOT4044  
## 功能特性  
###   
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMI7N1ibe41rjvLITyZCxic3RgENnGSeDSS6mQkpqia1fcZmSzziahG2FOx0sWRz2Cf3G3x8GcwMtqZ270kQg1QMBjHzkMOPac1cMus/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMIujHvwnvgDrjozrSRUpgcl1h06WnX3PaLMgDk9HdjMoK0Kt5qR8rBySuPiagiazIQa7aeSGoXLjicQOvcmNYLjqCc20GNHvXicJCY/640?wx_fmt=png&from=appmsg "")  
## 工具使用  
```
pip install -r requirements.txt
```  
### 一键全功能扫描（推荐）  
```
# 基础全功能扫描（自动跳过DNSLog盲测）python flux.py https://example.com --full -o report.html# 全功能扫描 + DNSLog盲测（推荐用于SSRF检测）python flux.py https://example.com --full --dnslog xxx.dnslog.cn -o report.html
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMIXx2Kk3h9rWJrc5xibE2FYCynAkDDicz9QpEq0zVOzLI6omJb8lnUuYChMH2OTnibk7QnZd9ISd2L9s4PXkPNd2NuMbQZmheutAw/640?wx_fmt=png&from=appmsg "")  
  
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
 不包含DELETE测试，如需测试DELETE接口请额外添加 --test-delete  
 参数  
  
- --full  
 模式下如未指定 --dnslog  
，将自动跳过盲SSRF测试（避免交互式输入卡住）  
  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260306  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[跨平台自动化安全应急响应数据采集与分析工具 |  应急响应、入侵排查、挖矿病毒溯源2026-03-05](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496388&idx=1&sn=6c8481d1353a47b05e4cdc9a2ff00644&scene=21#wechat_redirect)  
[银河麒麟OS安全检测工具 | 资产清点、合规检查、漏洞扫描和报告生成一体化2026-03-04](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496374&idx=1&sn=ce539b27c456cd9de061db0ed14415f5&scene=21#wechat_redirect)  
[漏洞报告处理平台 - 支持Nuclei/Xray/自定义txt报告导入，AI驱动的安全漏洞管理与分析系统2026-03-03](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496368&idx=1&sn=c40c9187ca8b190e3b088cae3cb1f8b8&scene=21#wechat_redirect)  
[漏洞管理平台 | 支持Excel格式的漏洞扫描报告导入、智能关联资产、漏洞可视化管理2026-03-02](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496361&idx=1&sn=e640bdb2795d33f2a32945b4aed1d3d6&scene=21#wechat_redirect)  
[渗透测试Payload速查平台 | XSS/SQLi/SSRF/RCE | React+TypeScript2026-02-28](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496352&idx=1&sn=7b8ed88d924b2cfb098dba470262be32&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
