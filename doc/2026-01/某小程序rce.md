#  某小程序rce  
 迪哥讲事   2026-01-27 01:01  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
  
漏洞挖掘  
```
web挖不动了,可以瞅瞅小程序，很多中学的小程序
还是很脆的，因为多数都支持一键登录。。。
信息收集之后，看到了这个小程序，进去看看功能。
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpH7QM6sHpibgu9TA9MPGQM1FX53vbkgl2nLWcFtmDGcQrHibx8HVhkiagBQ/640?wx_fmt=png&from=appmsg "")  
  
点击小程序进行登录，登录之后把对应的功能都看看  
  
测试之后发现这个校友企业存在问题  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpH7xzTkiapApb98fkG3Lty2ZjsbCzchWzPlVibyzvsc7vNTqC8aZTkbAVg/640?wx_fmt=png&from=appmsg "")  
  
点击校友企业  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHSpxdjQvRmfBuKBMlaJMLicibfx37dRs1q5FyQf4mlTOd0m6wGreMVh8Q/640?wx_fmt=png&from=appmsg "")  
  
会出现校友创建的公司，注意这里直接返回了，校友的名字  
  
记得之前看文章的时候，看到过，前端只是渲染了后端返回数据的一部分  
  
所以退出到上一个页面，点击校友企业进行抓包  
  
成功返回了，校友的敏感信息，手机号，sfz啥的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHx1xUG7MoIIxJ13Y91KIgwwjz6GukhXJ81k2ubia7SB26Vlq6Chr7nuA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHoLOuJB1w4ozZo9Yu01EsJzwFbOqBE7fArAcrhibe6yhHY0UYdp3x6DA/640?wx_fmt=png&from=appmsg "")  
  
非常合理，继续测试  
  
来到小程序最容易出现问题的地方，上传头像处的xss  
  
点击个人信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHmEJtWpfgfwMDphDXwaia43A7U5yxZcD2v2Pf9MqnbEFzIuibuichpCicmQ/640?wx_fmt=png&from=appmsg "")  
  
点击头像进行上传，随便选择一张图片，进行上传抓包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpH0DSHBA4mx25rf9ksaBzvlAR2YymcMAjSkLSMgzHKYYnicibvVdTcrvTA/640?wx_fmt=png&from=appmsg "")  
  
将数据包后缀修改为.html进行上传测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHDql9EXiavLnyWC3gichNoqJAw6bDAz6UkRfP030IeiczicmvSZbruW0cJg/640?wx_fmt=png&from=appmsg "")  
  
没有做限制，访问上传成功之后返回的路径，又水一个  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpH0cXKa95XlwbX9ib5ZtVhibib0fVHFic82qgKjMvPY17mXEyyexiaOk7nLEg/640?wx_fmt=png&from=appmsg "")  
  
本来都打算跑路了，后面想了一下既然连个waf都没有  
  
大胆点尝试一下getshell  
  
观察上传数据包，发现是php写的，修改后缀为php然后  
  
内容写一个phpinfo();不需要写一句话，证明解析即可。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHqqztibafaUwbPg34uFr6PPtF6lsMf3krX8X3yDibzTn8ttQRsgPDQxZQ/640?wx_fmt=png&from=appmsg "")  
  
发送数据包成功返回上传路径  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpH1Mhb5QRopgnicLMG9lwahZnXZnxwtPYqiblz6v1XicPblOE2XAzg6sJ7A/640?wx_fmt=png&from=appmsg "")  
  
进行访问尝试，成功解析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5p5SCWiaibrMEKa4m9DOswpHn18fecPv3p645l3NfR4tMpp93PnWSXzsC6WQHxic9WTVgDzKbib7apvw/640?wx_fmt=png&from=appmsg "")  
  
后面发现图库啥的，只要能上传东西的地方，都没有做限制，直接写报告，提交跑路。。  
  
如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg "")  
  
往期回顾  
#   
# 如何利用ai辅助挖漏洞  
#   
# 如何在移动端抓包-下  
#   
# 如何绕过签名校验  
#   
  
[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)  
  
  
[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)  
  
  
[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)  
  
  
[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)  
  
  
[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)  
  
  
[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)  
  
  
[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
  
  
  
  
  
  
  
  
  
