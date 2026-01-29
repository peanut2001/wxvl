#  【安全圈】PyTorch "安全"模式被严重RCE漏洞攻破，可执行任意代码  
 安全圈   2026-01-29 11:35  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
![banner](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljCia2ErX4op9oEhIOLywdc0K2lDYFXP3oXmsVWv7pVPib7pfCZqv3MmyuKdLU2TZhKGJibicRLRTTTZA/640?wx_fmt=jpeg&from=appmsg "")  
  
作为现代深度学习和AI研究核心框架的PyTorch，其开发团队近日修复了一个高危漏洞（CVE-2026-24747，CVSS评分8.8）。该漏洞会破坏PyTorch最受安全关注的功能信任机制——即使启用专门设计的防护设置，攻击者仍能执行任意代码。  
## 安全机制失效  
  
漏洞存在于weights_only=True反序列化器中，该机制本应确保仅安全加载模型数据而不执行代码。在Python AI领域，torch.load()函数是加载已保存模型检查点的标准工具。由于Python的pickle模块存在可执行任意指令的安全风险，PyTorch专门引入weights_only=True标志，承诺仅加载数据（权重）并阻断可执行代码。  
## 漏洞技术细节  
  
安全研究人员发现该防护机制存在缺陷。官方公告指出："weights_only=True反序列化器未能正确验证pickle操作码和存储元数据"。从技术角度看，该漏洞属于内存损坏问题，最终可升级为代码执行。攻击者通过构造恶意检查点文件（.pth）可触发两种特定故障：  
- 堆内存损坏：对非字典类型应用SETITEM或SETITEMS操作码  
  
- 存储不匹配：在存档中创建"声明的元素数量与实际数据之间的存储大小不匹配"  
  
当用户加载这个被污染的文件时（误以为受限模式能确保安全），反序列化器将损坏内存，可能导致攻击者劫持受害者进程。  
## 对AI供应链的影响  
  
该漏洞对AI供应链影响尤为严重，研究人员和工程师经常从Hugging Face或GitHub等公共存储库下载和测试模型检查点。公告警告称："能够诱使用户加载恶意检查点文件的攻击者，可在受害者进程上下文中实现任意代码执行。"  
## 影响范围与修复方案  
  
该漏洞影响PyTorch 2.9.1及之前所有版本。PyTorch团队已在2.10.0版本中发布修复补丁，强烈建议开发者和数据科学家立即更新环境，确保其"安全"加载实践真正安全可靠。  
  
  
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
  
  
