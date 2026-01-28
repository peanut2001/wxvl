#  【项目实战】复盘 Dify 系统的“组合拳”漏洞  
隐雾安全
                    隐雾安全  隐雾安全   2026-01-28 01:00  
  
📝 **编者语**  
  
甲方爸爸们都在疯狂上大模型（LLM）应用，Dify因为开源、好用，成了很多企业的首选私有化部署方案。  
  
但在我们最近的测试中发现：面对这类 AI 应用，传统的漏洞扫描器几乎失效。  
今天复盘的这个案例，通过一套“组合拳”，利用SSRF漏洞作为跳板，最终拿到管理员配置的OpenAI/Claude商业Key。  
  
(注：本文所有敏感信息已脱敏，仅供安全研究与教学交流，请勿用于非法用途。)  
  
1  
  
利用文件上传接口探测内网（SSRF）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX99tuFnibf23w0MHVhmaMDs1Eo9Zia9Rf3HV62uVxjf54I2x8iaHOibF57hQ/640?wx_fmt=png&from=appmsg "")  
  
我们首先对 Dify 的功能点进行测试，发现在 “上传文件” 的接口（/console/api/remote-files/upload）存在逻辑漏洞。  
服务器没有对用户传入的 URL 做严格过滤，导致我们可以利用它发起 SSRF（服务端请求伪造） 攻击。  
  
为了验证漏洞，我们构造了一个指向 DNSLog 平台的测试链接，试图让 Dify 服务器主动来访问我们：  
  
{"url": "http://4aa309cca1.ddns.1433.eu.org"}  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9SQ1OmYononNyjYbfC63usCWc4EbLJasYr4NyTuQCEflCJU9FibZdXnQ/640?wx_fmt=png&from=appmsg "")  
  
 可以看到，DNSLog 成功收到了来自 Dify 服务器的请求。这意味着服务器可以根据我们的指令访问任意网络地址，SSRF 漏洞实锤。  
  
2  
  
组合漏洞获取LLM KEY  
  
**第一步：发现高价值目标，但数据被加密**  
  
仅仅利用 SSRF 探测端口是不够的，我们的目标是获取高价值数据——LLM 的 API Key。  
  
在深入分析系统后，我们尝试获取数据库中的配置信息。虽然我们成功提取到了存储 API Key 的字段，但 Dify 出于安全考虑，对这些 Key 进行了加密处理。我们拿到的不是明文，而是一串被加密后的乱码字符串。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9HAVN4VhJ1ELNeY0MqoLrVYZybYjv76aGBOmCwIXKbqpy44US06E6YA/640?wx_fmt=png&from=appmsg "")  
  
如图所示，api_key 字段是一长串密文，直接拿去调用 OpenAI 接口是会失败的。  
  
**第三步：组合拳出击，SSRF 窃取私钥**  
  
面对密文，必须解密。这里我们参考了 e0mlja 师傅 关于 Dify 组合漏洞的研究文章，对 Dify 的加密机制进行了审计。  
  
通过查阅源码发现，Dify 的核心加密逻辑位于 api/core/helper/encrypter.py 文件中，使用的是 RSA 算法（注：不同版本可能略有差异）。这意味着，只要拿到服务器上的私钥文件（private.key），就能还原出明文。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9zfR1vK3RFmV7VP1Tia3VIbcKJM18HWnJuK6ARkXNrxXqU6YG4ZnFttg/640?wx_fmt=png&from=appmsg "")  
  
源码明确了私钥文件的存储路径。  
  
此时，第一步发现的 SSRF 漏洞成为了关键的“钥匙”。  
  
正常情况下，外网无法直接下载服务器本地的私钥文件。但我们可以利用 SSRF 漏洞（配合 file:/// 协议或利用内网未授权接口读取），强制服务器将本地的私钥文件内容“吐”出来。  
  
通过这种“隔山打牛”的方式，成功获取解密所需的私钥。  
  
**第三步：本地解密，图穷匕见**  
  
现在我们手里有了两样东西，攻击链闭环了：  
  
1. 密文（从数据库配置中提取的乱码）。  
  
1. 私钥（利用 SSRF 漏洞窃取的本地文件）。  
  
  
  
接下来就是编写脚本进行本地解密。我们编写了一个简单的 Python 脚本（思路源自 e0mlja 师傅），利用 RSA 私钥对密文进行解密操作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9Z6kkNKibu4micXI79iaatzCjbOkfsbDyStTbJB4oGmvXAcQM4ozbQTrMA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9cYNzGPElEnYl2rg8M8mB6I54VdUVVibkkUibVw2nx04kibuS1V9OWp3Yg/640?wx_fmt=png&from=appmsg "")  
  
运行脚本后，加密的乱码瞬间变成了明文的 sk- 开头的商业 Key！至此，我们完全接管了该大模型的调用权限。  
  
3  
  
总结与防御  
  
AI 应用的安全不仅仅是防注入，更要防“业务逻辑滥用”。  
  
防御建议：  
  
1. 限制出网：Dify 容器不应能随意访问内网敏感段（如 172.x.x.x）。  
  
1. 密钥管理：SECRET_KEY 极其重要，不要简单明文存放在容易被读取的环境变量中。  
  
1. 升级版本：关注官方的安全更新，增强沙箱隔离。  
  
  
  
🎁 文末福利  
  
联系客服获取更多实战报告  
  
**!**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ELQKhUzr34x9icHyTQkX29uCAYxGKxAX9bujYRZ7wQO4iaVjrRqdVTSQEysnT16cnMZVVbeibbicWfayKyNk5HpMiag/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**微信号丨**  
Hiddenfog001  
  
**往期内容**  
  
[通用0day挖掘思路](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247492296&idx=1&sn=0350ca481c64313904a1fc06da9c4f60&scene=21#wechat_redirect)  
  
  
[某大厂勒索病毒处置流程外泄](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247492246&idx=1&sn=469d15c6ac130d611b48f9098b832120&scene=21#wechat_redirect)  
  
  
[今年大一，不小心黑进学校的迎新系统怎么办](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247485696&idx=1&sn=b4e54d33ae5b6fae788c4c8089ead1df&scene=21#wechat_redirect)  
  
  
[英雄联盟租号平台getshell](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247496399&idx=1&sn=4d3b3d4a63539fcdab4ccfe24a5f115e&scene=21#wechat_redirect)  
  
  
[记一次色情APP的渗透过程](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247486334&idx=1&sn=c2be4746c5e59ebc6e21fe68fd00b85e&scene=21#wechat_redirect)  
  
  
****  
**课程推荐**  
  
[隐雾SRC第八期全面升级](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247498743&idx=1&sn=7ac290a5ec7d7c9b6ab01256bee48a2a&scene=21#wechat_redirect)  
  
  
[零基础就业班-三包模式](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247498939&idx=1&sn=8a1ea75429e8f1258b8887b14602b051&scene=21#wechat_redirect)  
  
  
[只要98，JS逆向带回家！](https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247499601&idx=1&sn=955e1bfc250b5847d1b324b04ee3ce40&scene=21#wechat_redirect)  
  
  
