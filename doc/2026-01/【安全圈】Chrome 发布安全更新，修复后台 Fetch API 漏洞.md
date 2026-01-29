#  【安全圈】Chrome 发布安全更新，修复后台 Fetch API 漏洞  
 安全圈   2026-01-29 11:35  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
![可用- Chrome](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljCia2ErX4op9oEhIOLywdc0xeenkLMTFPVwTZbvYFI8SRguQBgRDkCnVkK2376o7iamXIjCJ1EqZHA/640?wx_fmt=jpeg&from=appmsg "")  
  
Chrome 稳定版通道已推送 144.0.7559.109 和 144.0.7559.110 版本，修复了 Background Fetch API 中存在的一项高危安全漏洞。  
  
该更新将在未来数天至数周内向 Windows、Mac 和 Linux 系统逐步推送，**用户务必尽快将浏览器更新至最新版本**  
。  
  
本次安全修复的核心是漏洞 CVE-2026-1504，这是一个影响 Background Fetch API 功能实现的**高危漏洞**  
。  
  
该漏洞被归类为功能“实现不当”问题，可能被威胁攻击者利用。  
  
此漏洞由安全研究员 Luan Herrera 于 2026 年 1 月 9 日发现并上报，且凭借该漏洞获得谷歌漏洞奖励计划（Vulnerability Reward Program）3000 美元赏金。  
  
Background Fetch API是一项网络标准，允许网络应用在后台下载大型文件，即使用户关闭了浏览器标签页或离开了该网站。  
  
此实现中的漏洞可能使攻击者能够操纵后台获取操作。不过，在大多数用户安装补丁之前，具体的漏洞利用细节将暂不公开。  
  
此次更新体现了 Chrome 对安全性的持续投入，并进一步巩固了浏览器的多层防御体系。  
  
谷歌部署了 AddressSanitizer、MemorySanitizer、UndefinedBehaviorSanitizer、Control Flow Integrity、libFuzzer 及 AFL 等多款先进检测工具，用于发现安全问题并阻止其流入稳定版通道。  
  
Chrome 144.0.7559 版本更新已立即启动推送。但为确保系统稳定性并便于监控，更新将分阶段进行，持续数周。  
  
**用户可通过访问 Chrome 设置菜单中的“检查更新”来手动安装更新**  
。  
  
Windows 和 Mac 用户应更新至版本 144.0.7559.109 或 144.0.7559.110，Linux 用户则应更新至 144.0.7559.109版本。  
  
安全专家建议，尤其是依赖搭载 Background Fetch API 的 Web 应用的企业用户与个人用户，应优先安装此更新。  
  
管理大量 Chrome 部署的企业组织应在更新期间**密切关注推送情况**  
，并验证相关应用的兼容性。  
  
本次构建所包含的全部更改的完整列表，可在官方的 Chrome 提交日志中查看。  
  
若在更新后遇到问题，用户可通过漏洞报告系统提交反馈，或前往 Chrome 社区帮助论坛寻求支持。  
  
谷歌将持续与全球安全研究人员合作，不断强化 Chrome 的安全防护能力，竭力防止漏洞对用户造成影响。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073891&idx=1&sn=5a28b35ef1f9877f68769c480ec7c614&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Office漏洞正被黑客大量利用！2016、2019、2021、365全中招](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073891&idx=2&sn=37b25475a55602fcc0f9d4adb0230448&scene=21#wechat_redirect)  
  
  
  
[【安全圈】消息称耐克遭暗网黑客入侵，1.4 TB 数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073891&idx=3&sn=1a35e5886b4e61f72d6a74b570283b18&scene=21#wechat_redirect)  
  
  
  
[【安全圈】东营网警侦破一起金融借贷领域非法获取公民个人信息案](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073876&idx=1&sn=146711e5f26f23ce33059afd4c20ff37&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
