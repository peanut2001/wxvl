#  《网络安全与数据治理》：基于大模型的深层 Web 越权漏洞检测方法​​  
 美创资讯   2026-03-04 04:03  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ib9aljs9x2mc2KErXn6CH8HJJP1WJD4vVjibrq7vEK1X8Hl99vHdLnEw0icqgMZFiaAabSee69uLoOMk7B3RfSsKaA/640?wx_fmt=gif&from=appmsg "")  
  
近日，《网络安全与数据治理》杂志（2026年第2期）正式刊发了  
美创科技第59号安全实验室的最新研究成果——《基于大模型的深层 Web 越权漏洞检测方法》。  
  
  
该研究创新性地将大模型技术应用于 Web 越权漏洞检测，提出了一种全新的被动式深层检测方法。该方法能够利用大模型自动识别参数名含义与参数值特征，动态生成测试参数并进行发包，随后通过综合研判返回流量包的长度大小、具体内容等多维度特征，实现对漏洞的精准定位。  
  
  
经实际测试表明，该方案不仅能够有效挖掘出隐藏更深的越权漏洞，更大幅降低了人工手动挖掘的成本，为 Web 安全漏洞检测提供了全新的解题思路。  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81kNjlmKzr7Srvy1jhHOgNjlPlj8lhuVicsVm7XhZOheas166jqzvib2yz6RxpdV6Nconfz0gXhicSHSjyUQlkd1gSPaK44iatJDnNw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
以下为论文全文，转自《网络安全与数据治理》  
  
  
  
**基于大模型的深层 Web 越权漏洞检测方法**  
  
文 | 覃锦端¹ 尉雯雯², 王月兵¹ , 柳遵梁¹ , 刘 聪¹  
  
(1. 杭州美创科技股份有限公司; 2. 陆军军医大学第一附属医院)  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81mXyfiaKu9j73GWTxqeobvPAXkN90n5Ll15BWgAJFPJHKksrpu9vHuUyNO5rG24myVhCHmHoEbhibiacFP1wI0YZIKKjR4q8UFxNI/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81mS559uaolFtDjiaflIRkj5riayUZJcGPItRVIZatBIV8deqgOcPMiaJfyu0eT03nj4wy5H8eFXfZNg912kX2LGbmUgMJ6Zm400kw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81lgW52eiaadpRwvsWwKiauRzN55sQ2JwOcrOCNCoa0pFJQWptcx8B6kGPPiaiaCiaSt9mnsNaQXfIGa4o7y7XBHQdYtcEpKYDCTb3fE/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81mrkKCPYFDJ2jjbXd02FQicoavlNZG8icgCFoU83pl09JA9OFVjib5VZjNY2mQ7RKHOtjEZw3s6xqsVA0qSS4spw2F3ertBIic2QAE/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81lPodh9axIGWFia1rJvGqSAavu5Y6WZORZA2wsT7ZCJjLlfsH1YiaJZicCGHZhZ1sRZpibMh9j7wV20wEcZVKJukkDZlvMdwxZ4qpk/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81mx94843lA2pqhQQhKQnct70PASw2pupHWwsldOaKAPDMWlEzgRSybahibxV9yFQq6YKXAtibGhhStGvM7pLiblmmddO1vLYictVXc/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81lVMo8BJlLUIsXHGRcdibhIWyQTEVya5PHXFZlT68Wu97oGsNDS6qgDBjxRYuVsEibRVHZkLJVnXddLLVFXTIDJZuSGWMEleVHSE/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81keGRm2B7I9gibSlx1op4j6RIbceLRbiaxBd6AeiblEmkkXHalibu3ZPibLgxianwR1F1zwFkSLu60EvsHNKoMdrtz8iaOAVbM3pcdicAQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/pJjOS4MSntVSQRXIHuHeHvW0Klr3u9EiaeB9lxKt3WOPVv7rnRqQbicn8gCnbRzMKrsrnLdaBtVe8ZxemVBSK8XQ/640?wx_fmt=other "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif "")  
  
[《金融电子化》：构建金融韧性运行安全体系：从灾备管理到主动防御新范式](https://mp.weixin.qq.com/s?__biz=MzA3NDE0NDUyNA==&mid=2650818292&idx=1&sn=5e50626662e77af27b8a73d38d1263fc&scene=21#wechat_redirect)  
  
  
[论文发表｜零信任模型下的医疗数据安全防护解决之道](https://mp.weixin.qq.com/s?__biz=MzA3NDE0NDUyNA==&mid=2650782883&idx=2&sn=68f451efd7a5d03f342cb563e982e36b&scene=21#wechat_redirect)  
  
  
[论文发表 | 美创&浙大二院合作论文在国家科技核心期刊发表](https://mp.weixin.qq.com/s?__biz=MzA3NDE0NDUyNA==&mid=2650789164&idx=2&sn=ce583ef93999e249c02dd778c094186a&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ib9aljs9x2mfD4buRKuU8ZMSge8IZuFiauVHTXZk3r1Xaj8CbqdedZCfLJl44Yy4VNXjscn0WPKu18bf9p4s8Gbw/640?wx_fmt=other "ÉãÍ¼Íø_401860691_wx_3d¿Æ¼¼¿Õ¼ä£¨ÆóÒµÉÌÓÃ£©.jpg")  
  
   [零信任数据安全深研与创新实践，美创论文入选中国科技核心期刊](https://mp.weixin.qq.com/s?__biz=MzA3NDE0NDUyNA==&mid=2650796412&idx=1&sn=bdd2dc643cb3f29ff4a2eb71de71a377&scene=21#wechat_redirect)  
  
  
  
[#Web漏洞]()  
  
 [#漏洞检测]()  
  
 [#越权漏洞]()  
  
 [#大模型]()  
  
  
