#  山石安全能力中心｜青龙面板未授权RCE漏洞通告  
原创 山石网科
                    山石网科  山石网科新视界   2026-03-06 06:00  
  
#   
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8Jb8ZACqDjPdMzgicp2SzdZ19mFnVcBO53s1uA2cSfarQkwibVUeCeH9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=kzx4ched&tp=webp#imgIndex=1 "")  
  
  
漏洞通告  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NGIAw2Z6vnLKuKAwMiaYedpTAYugKibaTBsHzf5pDuztECgfIgOfpG5DRF31jzhosMEj23dlx186q0zgLaIZj9lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2c2qx2ig&tp=webp#imgIndex=2 "")  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&randomid=hhvjiwep&tp=wxpic#imgIndex=3 "")  
  
01 漏洞概况  
  
  
青龙面板是一款定时任务管理平台，支持Python3、JavaScript、Shell等多语言，凭借其灵活的自动化脚本运行能力，成为了不少NAS用户的必备工具，其Docker镜像下载量高达16M。  
  
  
山石安全能力中心监测到青龙面板存在未授权RCE漏洞，经进一步分析确认，问题根因在于其JWT校验机制及自定义鉴权逻辑采用大小写敏感的路径匹配方式。由于接口路径匹配未进行统一规范化（如未做大小写归一处理），攻击者可通过构造大小写变形的请求路径，绕过既有认证校验逻辑，从而访问本应受保护的接口。在被绕过的未授权接口中，存在多个具备命令执行能力的功能点，攻击者可在无需登录的情况下调用相关接口，最终实现远程命令执行。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&randomid=hhvjiwep&tp=wxpic#imgIndex=3 "")  
  
02 漏洞基本信息  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbFUa7hBE7s3YOY6kIrvZpZiawjyzGlzIzcFPbMticYoEzuoBgOnv526K69V5DL8FhWa2x5JUrQGohtvyvmtBgr1cKibic29griciafCM/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&randomid=hhvjiwep&tp=wxpic#imgIndex=3 "")  
  
03 原理分析  
  
  
该漏洞是由于在JWT验证和自定义认证中使用了大小写敏感的字符串匹配，漏洞位置在back/loaders/express.ts文件下的JWT验证正则表达式处：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbEWrAhw5LEc1Bxk3zN3ynRNuDjd2ibpFia9h7yWJ7TuVj3MzcMkQQPIQSUI68VqjANa0bFvByty9mDea5NOZjJP9EH9KiaQdWrjjg/640?wx_fmt=png&from=appmsg "")  
  
  
可以看到该处只检查路径是否以小写/api/开头，这里我们以/api下的/system子路由为例子，当接口为/api/system时不匹配正则需要JWT验证，否则匹配正则绕过JWT验证，接着进入到自定义认证路径检查部分：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Zjic54DsBHbGqS0bTl6Tz7X1gUEo8xnWY9acI6D1VLoBIwvRV3MNgaickmnhq4s3QAnyaX4QbSQdRYBNxp8gYNx5cl6gtroNaMBVDzTkadAsY/640?wx_fmt=png&from=appmsg "")  
  
  
这里我们可以看到通过startsWith() 检查路径是否以小写 /api/ 开头，但是当我们使用大写时就可以绕过认证，执行next()，而在Express的路由匹配中默认配置是大小写敏感的，导致/API/system会被成功路由到/api/system的处理逻辑里。当我们进入到/system路由里（也是就是/back/api/system.ts文件）可以看到存在一些远程命令执行的操作，例如：/command-run接口：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Zjic54DsBHbG12ib0Zk4zVAHgrYHvej6V2tSTZRe0Wkjs2iadVJl1DsRkfNgZr19BSibcyVpeLn2r5sQ0nBoWRibEjAZMibP88jkcsOresa1E1Q3o/640?wx_fmt=png&from=appmsg "")  
  
  
可以看到这里通过req.body获取command参数并进行拼接最后调用promiseExec执行命令，导致远程命令执行。  
  
  
完整攻击链：JWT验证中间件 -> 自定义认证中间件 -> Express路由匹配 -> 存在命令执行功能接口（这里只是介绍了其中一处，该项目还有很多地方可以造成远程命令执行）  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&randomid=hhvjiwep&tp=wxpic#imgIndex=3 "")  
  
04 漏洞复现  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Zjic54DsBHbGgsnW4Y2YYS52aw9jndopA1egefCr53V3eYkF1Ul8nMHtYiaCLbx3MZuTlAibQ2rsw4Sia7w2icBjvOu0tW2wOrqicqkP2TibQ324RY/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&randomid=hhvjiwep&tp=wxpic#imgIndex=3 "")  
  
05 修复方案  
  
  
1.临时缓解措施：  
- Nginx反向代理过滤；  
  
- 防火墙IP白名单；  
  
- 通过边界设备防护，限制访问API和OPEN大小写路径；  
  
- 如非必要，避免将资产暴露在互联网。  
  
  
2.官方修复：  
  
建议联系厂商打补丁或升级版本，官方网站：  
  
https://github.com/whyour/qinglong/  
  
  
3.山石产品解决方案：  
  
山石网科入侵防御系统可实时检测该漏洞，通过精准特征识别与行为分析机制，快速识别恶意利用流量，并在攻击链早期阶段进行监测，有效防止漏洞被利用，保证客户安全。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnIYnBoVjHn0mWO3pro1TfcNW1g9SygLH6FI0c8mzWjXzibo9E0zM28pwRHFqwdHGwa2KbdicjgWdTtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=852hkcz1&tp=webp#imgIndex=6 "")  
  
- [从波兰到印度：国外电厂网络攻击频发，电力工控安全该如何破局？](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305625&idx=1&sn=9eda2f7821efbe630b49c6014ff4d16a&scene=21#wechat_redirect)  
  
  
- [山石安全能力中心｜微软2026年2月份漏洞补丁日安全通告](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305379&idx=2&sn=de37da4649812108c7636b31bb633e04&scene=21#wechat_redirect)  
  
  
- [AI 简讯｜重要AI事件](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305348&idx=3&sn=1d0120129cdb2199572753f0bba9b321&scene=21#wechat_redirect)  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8KrXv9sZf93yt4huq2kARyZSgmdnic40GayohIYiaD2FAkkAqJehJSMtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=7oqdpqlb&tp=webp#imgIndex=7 "")  
  
山石网科是中国网络安全行业的技术创新领导厂商，由一批知名网络安全技术骨干于2007年创立，并以首批网络安全企业的身份，于2019年9月登陆科创板（股票简称：山石网科，股票代码：688030）。  
  
现阶段，山石网科掌握30项自主研发核心技术，申请560多项国内外专利。山石网科于2019年起，积极布局信创领域，致力于推动国内信息技术创新，并于2021年正式启动安全芯片战略。2023年进行自研ASIC安全芯片的技术研发，旨在通过自主创新，为用户提供更高效、更安全的网络安全保障。目前，山石网科已形成了具备“全息、量化、智能、协同”四大技术特点的涉及  
基础设施安全、云安全、数据安全、应用安全、安全运营、工业互联网安全、信息技术应用创新、AI安全、安全服务、安全教育等10大类  
产品及服务，50余个行业和场景的完整解决方案。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxPibycdiaNQCI4PNojUk3eYCQDZs6c5zNMUkq7yFNeYQIxicAV33eHNdFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2m7uy0lj&tp=webp#imgIndex=8 "")  
  
  
