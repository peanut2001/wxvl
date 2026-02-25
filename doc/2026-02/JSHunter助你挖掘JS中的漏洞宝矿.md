#  JSHunter助你挖掘JS中的漏洞"宝矿"  
原创 锐鉴安全
                    锐鉴安全  锐鉴安全   2026-02-24 23:02  
  
WEN3o75  
  
书站的未授权漏洞，忆校园青春  
[阅edu证书站的未授权漏洞，忆校园青春](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486254&idx=1&sn=993cd82bceba042301a009c28ca2d251&scene=21#wechat_redirect)  
  
  
  
点击蓝字 关注我  共筑信息安全  
  
  
  
  
  
  
￼  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！  
  
  
  
  
1  
  
  
  
  
背景  
  
  
本次实战的案例，源于某高校的人脸采集系统，听着都感觉危害很大，因为全是敏感信息，如身份证、人脸等，拿到就是高危漏洞。从无账号到登录系统，靠的就是fuzz，详细的过程见实战过程。  
  
  
  
  
  
  
2  
  
  
  
  
实战过程  
  
  
通过一系列的信息收集，高校的人脸采集系统引起了作者注意，为什么？因为有敏感信息。  
  
  
  
  
连Hunter、Fofa都没索引到这个系统，作者靠灯塔拿到了，灯塔确实好使，关键还免费，需要的师傅可以文末获取下载链接！  
  
  
  
  
系统的首页如下图，可以看到，只用一个登录按钮。  
  
  
￼  
  
  
  
  
看下findsomething，也没有找到“注册”功能相关的关键字，同时也跑了下接口，并无接口未授权问题。  
  
  
￼  
  
  
  
  
  
本次案例的关键操作来了，首先抓包观察下登录系统的数据包情况，随意输入账号密码，点击登录。  
  
  
￼  
  
  
  
可以看到登录的数据包中有个login关键字，秉着试试的心态！  
  
  
作者将login改为register，惊喜时刻，注册账号成功。  
  
  
￼  
  
  
  
使用注册成功的账号登录系统。  
  
  
￼  
  
  
  
可以看到获取到了身份凭证。  
  
  
￼  
  
  
  
登录到了个人信息首页。  
  
  
￼  
  
  
  
任意用户注册账号漏洞拿下，这个fuzz操作确实有点妙。都登录系统，肯定得把全量的功能测一遍，一般可以测试sql注入、越权、文件上传等漏洞。  
  
  
  
  
co  
  
  
点击蓝字 关注我  共筑信息安全  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlNDd8O4wJKfGhV48dQHTMk8icXxCBI5BKxPqWQOfwFWxPtG2e8iazqUssJg/640?wx_fmt=png "")  
  
**免责声明：**  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具等造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！  
  
  
**1**  
  
  
  
**工具概述**  
  
JSHunter 是一款用于自动化下载 Webpack 打包的 JavaScript 异步 chunk 文件，并扫描其中敏感信息（如手机号、身份证号、JWT、API 接口、账号密码等）的工具。  
  
  
它通过分析入口文件（如 app.js）中的 chunk 映射表，智能识别所有chunk的URL，下载到本地后进行全面敏感信息检测，最终生成 Excel 报告。助力各位师傅高效出洞。  
  
  
工作原理  
- 自动提取 chunk 映射  
  
支持多种 Webpack 打包格式，包括带引号的键、数字键、数组映射、r 函数内部对象等。  
  
- 智能 URL 构造  
  
根据入口文件路径自动推断基础目录，并尝试多种常见路径格式（如直接拼接、js/子目录、chunks/子目录等）。  
  
- 敏感信息扫描  
  
内置正则规则，可识别手机号、身份证号、JWT、URL 路径、API 接口、账号密码、Token 等。  
  
- 并发下载与重试  
  
使用 requests 会话管理，支持 SSL 忽略和自动重试机制，提高下载稳定性。  
  
- 结果输出 Excel  
  
扫描结果以结构化表格形式保存，方便查看和后续分析。  
  
- 自定义配置  
  
通过 JSON 配置文件灵活设置目标网站、下载目录、输出文件等参数。  
  
  
  
使用方法  
  
1、安装依赖包  
  
解压缩工具包后，运行以下指令。  
```
pip install -r requirement.txt
```  
  
  
2、为了提升识别精准度，在在conf.json中配置以下两个选项。  
  
```
"BASE_URL": "https://example.com",#目标网站的根地址，用于构造 Referer 等请求头
"ENTRY_URL": "https://example.com/js/app.8d9f6a06.js",#此为js的主文件，一般以app开头，可以在加载网页后，在控制台中获取完整链接
```  
  
  
3、运行主文件JSHunter  
```
python JSHunter.py
```  
  
  
4、运行完成后会在同目录下生成报告，直接打开查阅即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVIzz2MB22ApoHvr4eEgczo98ox3ibscxO0evn8ndMyjR3EbWXOmC4G4Q4WAZHGRgPA6gibNjWCaElEMepZ21hEmQBB20KczxRMFc/640?wx_fmt=png&from=appmsg "")  
  
  
功能界面  
  
主页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVK373iaUknj72SXYuv9GTCKn6TJonXswgetXdWSTzLiauHRbvEjVPmseDILLVBGNRceuOEWn2YWFicEa2w70PiaKWZWUrTQVNib3Nvc/640?wx_fmt=png&from=appmsg "")  
  
  
文件拉取过程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJ9kQYwLcYrkh22TNeKmbrx8nanNNdkibXnACdkCIPDd6yuVDcBLicAT11C1s8xdQNpbxvG9G6Q0ic6k8GcNLZUNeibQgvTLdrSm9U/640?wx_fmt=png&from=appmsg "")  
  
  
文件分析过程  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVIRDXZ6sDCqibaCMaolRgCOswrrTXEWk3Nwcdrh2zvxIw0KWdtDl70TF9FRcovsVoicLKmR1FNCS5jWAXrc9OlXRX2gibiaCmY7UmM/640?wx_fmt=png&from=appmsg "")  
  
  
完成情况  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLBeBeKrPhaA8eKfFGj7LrS94qE2BBnjnFXrdEUjDNIBh6tbNzricrMUGogomVl1oY8JpW3Jy7rCDxUicpb3H8GAnwTicuYBqwM1w/640?wx_fmt=png&from=appmsg "")  
  
  
下载方式见文末。  
  
  
  
期待您的关注  
  
  
往期好文推荐  
  
[高效出洞必备浏览器插件](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488151&idx=1&sn=197953c5cb62d68fd91f90bac570593c&scene=21#wechat_redirect)  
  
  
[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)  
  
  
[记一次"高危"逻辑漏洞挖掘实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487704&idx=1&sn=f2f296b6870ed8ddbaa6d142c93ea114&scene=21#wechat_redirect)  
  
  
[记一次SRC支付漏洞实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487822&idx=1&sn=0cfb1fd7754a8bb5fee12d44e450cd53&scene=21#wechat_redirect)  
  
  
[安服仔薅洞必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487810&idx=1&sn=6fb51d171d6546386a5bdbda662046f7&scene=21#wechat_redirect)  
  
  
[更新|帆软、用友、泛微、蓝凌等常见OA系统综合漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487310&idx=1&sn=f27b0f1199b3f52b086d1c7dc18685d0&scene=21#wechat_redirect)  
  
  
[渗透测试集成工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487068&idx=1&sn=e343013c9f5a4f736865236e6dfd4bf0&scene=21#wechat_redirect)  
  
  
[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)  
  
  
[推荐一款资产“自动化”筛选工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486679&idx=1&sn=288fe9f4312c3267c33765cfa9e3ab06&scene=21#wechat_redirect)  
  
  
[Jeecg-boot最新漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486651&idx=1&sn=70d0e3d5ac4920684f52a4ee52531854&scene=21#wechat_redirect)  
  
  
[js.map文件还原组合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486582&idx=1&sn=a08daa5cc01f04b813d827e5d8bf444b&scene=21#wechat_redirect)  
  
  
[Fuzz参数收集工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486946&idx=1&sn=f5a726612058dfacd753e80caea4f7ad&scene=21#wechat_redirect)  
  
  
[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)  
  
  
[免密登录某后台管理系统实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487191&idx=1&sn=e28b38ca45337d96bab655455ac7cc37&scene=21#wechat_redirect)  
  
  
[小程序渗透测试之全站用户接管](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487037&idx=1&sn=e147355e8ea0ef4e647bbe67ac3c3a97&scene=21#wechat_redirect)  
  
  
[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)  
  
  
[这个站"穿"了,等同于Getshell？](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486154&idx=1&sn=68cfc0ceedbb1d6770c574a8f093195e&scene=21#wechat_redirect)  
  
  
[Edu src证书站IOT(物联网)漏洞挖掘](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247485955&idx=1&sn=27eb28e0b60be661bc0d49baf2a44b49&scene=21#wechat_redirect)  
  
  
  
入交流群请扫码：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP5YQMjXQSIUEUJtW3OUfjggT6EBE31VhDjHs3VkeoGZaB8oFJnMl0oe5EickUiccUd29zktHl5wib4nw/640?wx_fmt=png&from=appmsg "")  
  
  
下载方式：进入下方小程序，在资源中心获取下载链接。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKUHhr9sMJib2q1ndC3YmEqgxVGV4pZxT5bgfa6Da4tp1Jia5DKx2WdmKia8hSHfO4XRgfHFKxiao7cE61wC4llChyaJFchSuNsicAw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND18ovUTvvzp4MagwzrEIAu6ZHoicVWA2YvfmEgZicxv4tvVibeFB8T7w3A/640?wx_fmt=gif&from=appmsg "")  
  
  
