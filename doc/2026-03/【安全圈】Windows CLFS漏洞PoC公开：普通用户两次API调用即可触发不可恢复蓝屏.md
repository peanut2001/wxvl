#  【安全圈】Windows CLFS漏洞PoC公开：普通用户两次API调用即可触发不可恢复蓝屏  
 安全圈   2026-03-01 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
安全漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFZqz3RAaNhQnjWpDqVCLmC5OyHfzLfalTMrw1AiaaeiaorX67VWMr89HZUWIjAL0qibFotplch4oIv4MyiaZqqYMyHXTCkAFoB1AU/640?wx_fmt=png&from=appmsg "")  
  
安全研究人员公开发布了针对 Windows Common Log File System（CLFS）驱动漏洞 **CVE-2026-2636**  
 的PoC代码。该漏洞存在于  
Microsoft Windows  
的CLFS.sys驱动中，允许任意低权限本地用户在无需提权的情况下，瞬间触发不可恢复的蓝屏死机（BSoD），属于拒绝服务（DoS）类型漏洞，CVSS评分为5.5。  
  
漏洞由  
Ricardo Narvaja  
（Fortra）在针对CLFS驱动的专项研究中发现。问题根源在于CLFS!CClfsRequest::ReadLogPagingIo函数对关键IRP标志位校验不当。当IRP_PAGING_IO和IRP_INPUT_OPERATION两个标志同时处于禁用状态时，驱动进入异常执行路径，最终直接调用内核函数nt!KeBugCheckEx，引发系统崩溃。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGfcKIdy3IoPJR9lRCCOYcWRMRfaf0JtLuichhMbCQWjyAbMyB62CjOVLabRcee1KCalHI1a8yKc9EDntHPE1Y0n6D1u1miaWXhU/640?wx_fmt=png&from=appmsg "")  
  
PoC利用过程极其简单，仅需两次API调用：首先使用CreateLogFile获取合法的.blp日志句柄，随后立即对该句柄调用ReadFile。由于ReadFile并非为此类日志句柄设计，CLFS驱动未能正确处理请求，直接导致内核级崩溃。整个攻击链从用户态KERNELBASE!ReadFile开始，经NtReadFile进入CLFS调度路径，最终触发系统BugCheck。无需构造恶意文件，也不涉及复杂堆喷或内存利用技术。  
  
微软已在2025年9月发布的Windows 11 2024 LTSC和Windows Server 2025累积更新中悄然修复该问题，Windows 25H2版本亦已包含补丁。但Windows 11 23H2及更早版本仍处于未修补状态。值得注意的是，CLFS驱动近年来屡次出现漏洞，包括CVE-2022-37969、CVE-2023-28252、CVE-2024-6768以及被勒索软件利用的CVE-2025-29824，均集中在同一驱动子系统。  
  
在多用户终端、企业工作站或自助设备环境中，该漏洞风险尤为突出。建议企业立即部署2025年9月或之后的累积更新，限制敏感系统的本地登录权限，并重点监测针对CLFS日志句柄的异常ReadFile调用行为。对于尚未升级的Windows 11 23H2及更早版本，应将其列为高优先级补丁修复对象。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】ClawJacked 漏洞曝光：网站可远程劫持 OpenClaw AI 代理，开发者需立即升级](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=1&sn=2f8e4442c9c605c764d28286413dffa2&scene=21#wechat_redirect)  
  
  
  
[【安全圈】“Vibe Coding”翻车：AI 社交网络 Moltbook 泄露 475 万条数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=2&sn=5180d19efcb21fb235721580938c11df&scene=21#wechat_redirect)  
  
  
  
[【安全圈】恶意npm包“ambar-src”投毒Windows、Linux与macOS](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=3&sn=6bf80090c0a276c836edd13d9b3b63e4&scene=21#wechat_redirect)  
  
  
  
[【安全圈】不用浏览器也能中招：Windows资源管理器成隐秘后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=4&sn=2a4acaa0943a8a81ed7eda038d8f1330&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
