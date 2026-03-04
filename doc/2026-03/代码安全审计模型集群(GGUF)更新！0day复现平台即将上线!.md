#  代码安全审计模型集群(GGUF)更新！0day复现平台即将上线!  
原创 秋风
                    秋风  北京秋风代码科技有限公司   2026-03-04 03:28  
  
今天 我们的代码审计模型迎来二次更新(地址在文件末尾)  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0KWwQcIjls9FgiaN6s9HcXaR1PTV4P68OoqnPVE8icmnWfd1IsGDwicHgaAibBygK6ibbib0sr5j16wRhFeaLpXCedogCgtFvrMV1VRg/640?wx_fmt=png&from=appmsg "")  
  
我们这次训练了一个模型的集群 针对性的解决了在代码审计场景中本地化的不足，通过一种语言一个小模型针对性训练来达到针对性提高，确保在微算力机器也可以实现一定效果，支持纯 CPU 推理  
  
文件一览：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KruTFGibo4M6Ps3D9iaicZfGnTML3l9ibI9UKicbT1JFRDQrIg5oyl5X9ZgINneMm8tAeLtvWOmwr53qF1E9Ufu5OscmIrLI7b3ENQ/640?wx_fmt=png&from=appmsg "")  
  
我们基于Qwen2.5-Coder 系列针对安全审计场景微调，按语言拆分为 6 个独立模型，分别覆盖 PHP、Java、Python、JavaScript、Go、C/C++。每个模型只关注对应语言的漏洞模式，输出包括漏洞定位、CWE 分类、攻击路径分析和修复方案。  
  
对话实例：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0KWfyk43z9SvicuqVvX1PumTOXXmBIwWvCJ3axU5qrgiaPQbAYUl9IibVlOAKicKJCER45s2boywd5FaL6q72zkzW1oKwuFJmSSrzg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KQ0TpWbYF205lzfjvGUI2mFY9KtxCBHByoqg4GmYlKfNAqcwZwaibac5BfOiamdOybBotYQlUgRZ0INkjL9CH8Zwwje7iaEAjZnA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0IBCHL6Xx0cVv6kAjHIv3f4iaksAOD8Pr3rSz8o0XBYlpC6ibVxoBb7Ns5lmKdibKLWexh56jRffFJe6DSW9Hx98xp1w5NKhrgDLo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0L2KSXeibmib3xdqTdQMAuichTrKwHbD82qhVAaue2pKpPvZiczuBk5oTQibpzcWPuHPkkIwI8zymdUmTVN0aErNf5qVnLpU2P2XyKw/640?wx_fmt=png&from=appmsg "")  
  
为了更好的服务客户，我司最强的训练模型我们放在了代码审计产品上，不对外开放  
  
  
此外，我们的0day复现平台将会近期上线，我们的想法是自动复现后的漏洞全部免费毫无保留的公布EXP dockerfile 输出等全部内容，并自动推送到邮箱，但目前由于政策合规问题我们还在逐步解决   
  
放几张图解解馋(并非最终形态)  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0IzaoEaqR14KVkkE24FaLkmexH2bNlM6Zkjd5YU2w8yuUrIPEC9ich6LJ4TLepHt6CK3LsVHWnliae4dNqKtMjib0gZbGZPcLh9Wg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0LGbebbwBNNJrQKFPEGJj3xVQW6Uf6XZWELVeeRw4WT4w1nDbeic3kiamBHhicMLallUGVwwuTXjvvNU1LlthXFgiaJveopthZqj1M/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0JfIRmBL7lr168qOZORkZK656Y4TibpT8yLT8etAoJib16oibZsltVTibhDsYaY1ZxOsbZvqODI1bZWSfTv9UkHicbb1W52ianSv9USE/640?wx_fmt=png&from=appmsg "")  
  
  
https://modelscope.cn/models/q1uf3ng/QiufengAudit-GGUF/summary  
  
点击原文链接也可跳转哦  
  
# 联系我们  
  
https://www.dmsec.cn  
  
地址：国家网络安全产业园区（通州园） 北京市通州区西集镇网安园创新中心1号-334  
  
联系电话:17896065108  
  
技术支持邮箱:glna9n@163.com  
  
  
