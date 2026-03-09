#  Burp Suite平替 | 智能代理、强大插件、集成云端虚拟手机，快速定位APP漏洞  
threehammers
                    threehammers  夜组安全   2026-03-08 23:57  
  
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
  
**SwordfishSuite**  
 是一款受 Burp Suite 启发的现代化 Web 安全测试平台。它集成了智能代理、流量拦截、负载扫描和强大的插件系统，旨在为安全研究人员和渗透测试工程师提供一款高效、可定制的应用利器。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKakic4250oOqtgrKFAEbpQ3wicVKnVd8z9fE1xs3HJ6rUz32fohcBnm2sU5f2iaXNb53n9fFGHzGHhE5gvXZMicCwslTGxtVrNiaiaA/640?wx_fmt=png&from=appmsg "")  
## 核心特性  
- **智能拦截代理**  
：无缝拦截、查看和修改 HTTP/HTTPS 流量，支持多种客户端，操作流畅直观。  
  
- **集成APP分析**  
：可集成云手机平台，直接在SwordfishSuite查看分析手机APP流量（暂不开放）。  
  
- **可扩展插件系统**  
：基于 Python 的完整插件生态，允许您轻松编写自定义扫描检查器和数据分析工具。  
  
- **GUI界面操作**  
：提供用户友好的图形化界面 (GUI) 以满足交互式测试需求。  
  
- **流量数据转发**  
：支持流量二次转发（原始流量和HAR格式），方便各种扩展。  
  
## 工具使用  
### 前置要求  
  
在运行 SwordfishSuite 之前，如果你需要启用插件：  
- **Python**  
 3.10 或更高版本  
  
- pip  
 包管理工具 pip install grpcio grpcio-tools protobuf numpy  
  
### 安装  
1. **从 GitHub 下载Release版本压缩：**  
  
```
   下载:https://github.com/threehammers-group/SwordfishSuite/releases   解压   cd Swordfish   ./Swordfish.exe
```  
### 如何使用  
1. **启动应用：**  
  
1. **GUI 模式 (推荐):**  
  
```
     ./Swordfish.exe或鼠标双击即可
```  
1. **安装证书：**  
第一次启动程序，点击工具栏安装证书按钮，CA 证书以支持 HTTPS 解密(证书存储位置->本地计算机->指定下列存储->受信任的根证书颁发机构->完成)  
  
1. **开始探索！**  
点击工具栏开始按钮，拦截流量，重放请求，使用负载测试器，或者开发新插件定制自己的专属功能。  
  
主界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMLwLfNljiaUIf2uACUSVN07jg1jDHiaAp6HMFia11gDJ0ZuXicZicmbwdTgnAK4MH9KXznLa8cpwDJTcM0gXaqgpB9zF2yMsjJXRqUM/640?wx_fmt=png&from=appmsg "")  
  
数据重发  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMK7VpHHOJCZbibJjugbYVhgtzTPqQOOEooVAESBGYQJDCRIGJM3xZNt9ZcSsmmianAdvhcA94bZa14xrU2ucichJBqIf8SCt6BTog/640?wx_fmt=png&from=appmsg "")  
  
负载测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJgS7iboQqkyd6ooGCLp7ia2DyrXV9w8sKib4fspVgUoLhpFAhrTBSXtB5BraYuVRDg9wBnd47EfypprhTVQHsJLYiaVZTZa4m2pZE/640?wx_fmt=png&from=appmsg "")  
  
数据包拦截  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJOCnlEI8NQyzFnjdpVWYyhb5icg6wibO47znicZT3eXIKg3xOR4BYpBo5B61ZLIpreIh1F0g9QiaAZlZ0auTO7E1FZ7kTSQuPPULU/640?wx_fmt=png&from=appmsg "")  
  
APP实时抓包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKYsQbrjEy34EsB6yzGGwtzDWL9ZW6RNVL73hwwcSZs6mcWXczymXsG3sr7NmQuYMTCiaMlIndIHTd26iapAZPdJFXoaveWsazzY/640?wx_fmt=png&from=appmsg "")  
  
python自开发插件示例  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJephdz0ugB2reIRHuaAbOOXbeqy4yaiaE0CBRke6Uzrgod1Bhpn2RpnhZ99QKsYXniaqdFia65tIialzWJUhcX0J9ox90cHdShteM/640?wx_fmt=png&from=appmsg "")  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260309  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[Web安全扫描工具 | JS敏感信息收集、API端点提取、API文档解析、页面爬取、子域名发现、漏洞测试、WAF检测与绕过、JS代码分析2026-03-06](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496398&idx=1&sn=976a1a305be37800cb063e8249bb8841&scene=21#wechat_redirect)  
[跨平台自动化安全应急响应数据采集与分析工具 |  应急响应、入侵排查、挖矿病毒溯源2026-03-05](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496388&idx=1&sn=6c8481d1353a47b05e4cdc9a2ff00644&scene=21#wechat_redirect)  
[银河麒麟OS安全检测工具 | 资产清点、合规检查、漏洞扫描和报告生成一体化2026-03-04](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496374&idx=1&sn=ce539b27c456cd9de061db0ed14415f5&scene=21#wechat_redirect)  
[漏洞报告处理平台 - 支持Nuclei/Xray/自定义txt报告导入，AI驱动的安全漏洞管理与分析系统2026-03-03](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496368&idx=1&sn=c40c9187ca8b190e3b088cae3cb1f8b8&scene=21#wechat_redirect)  
[漏洞管理平台 | 支持Excel格式的漏洞扫描报告导入、智能关联资产、漏洞可视化管理2026-03-02](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496361&idx=1&sn=e640bdb2795d33f2a32945b4aed1d3d6&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
