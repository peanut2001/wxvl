#  Zombie ZIP 漏洞披露：让 WinRAR/7-Zip 解压报错，已伪装绕过 50 款主流杀软  
安世加
                    安世加  安世加   2026-03-12 11:01  
  
新闻  
  
News Today  
  
3月11日消息，网络安全公司 Bombadil Systems 研究员 Chris Aziz 最新披露 Zombie ZIP 漏洞技术，成功绕过 50 款主流杀毒引擎检测，利用 WinRAR、7-Zip 等常规解压文件遇到的报错，执行恶意代码。  
  
  
援引博文介绍，该漏洞技术追踪编号为 CVE-2026-0866，专为规避杀毒软件和终端检测与响应（EDR）系统而设计，成功绕过了 VirusTotal 平台上 50 款主流杀毒引擎，几乎实现了完全的“隐身”。  
  
  
在技术原理方面，研究人员解释称，杀毒引擎通常会盲目信任 ZIP 文件的“Method”（压缩方式）字段。攻击者将该字段设置为“0”（即 STORED，代表未压缩），但实际上内部数据却采用了 DEFLATE 算法进行压缩。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/757fvrbk7oYRLLia6TlV6vpWQKYgFibbygunHXUAdnn97bImqibC9xgJ9u5B1m6qwFPqwj201r4e6hN9ulHicz0worHCIU2867DAzt8X7s3X0Gg/640?wx_fmt=png&from=appmsg "")  
  
  
在安全工具扫描该文件后，读取到的只是一堆混乱的“压缩噪音”，从而无法匹配到任何恶意软件的特征码，最终将其误判为安全文件。  
  
  
该技术为进一步隐藏踪迹，还会故意制造解压障碍。研究人员指出，通过将确保数据完整性的 CRC 校验值设置为未压缩状态下的校验和，常规解压工具（如 WinRAR、7-Zip 等）在尝试提取文件后，会直接报错或显示数据损坏。  
  
  
然而，黑客会使用专门定制的加载器，直接无视伪造的文件头，解压并释放出隐藏的恶意代码。研究人员目前已在 GitHub 上发布了概念验证（PoC）及样本。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/757fvrbk7oanNdVyGvia8yzzCLpFuvBV9DhAAQMetd4h9yhZZvpTxBUzH26Ftdbxgnn9FO7nQ0XmW06jQsP8ScDOmvXXSl1s2O2GXYUcmXAY/640?wx_fmt=png&from=appmsg "")  
  
  
针对这一严重威胁，计算机应急响应小组协调中心（CERT / CC）昨日正式发布安全公告，并为该漏洞分配了编号 CVE-2026-0866。该机构指出，这与二十多年前影响早期 ESET 杀毒软件的一个漏洞（CVE-2004-0935）高度相似。  
  
  
CERT / CC 建议安全工具供应商必须将压缩字段与实际数据进行交叉验证，并增加检测机制以识别结构异常的压缩包。  
  
本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！  
  
文章转自：IT之家  
  
  
安世加为出海企业提供SOC 2、ISO27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）  
  
[](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)  
  
  
