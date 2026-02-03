#  赏金src报告分享&&edu证书站漏洞分享  
原创 湘南第一深情
                        湘南第一深情  湘安无事   2026-02-02 16:03  
  
  声明：  
由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
## 前言  
  
某次项目和学员一起挖掘，开局就直接起飞了，运气真的好，让我们来怎么起飞的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPe9zqzKiaovOoeo52gCeHicFMfRS8hN6q7jYQRTH9OFYUx2jTCvCntWBVg/640?wx_fmt=png&from=appmsg "")  
  
## 第一个漏洞任意登陆拿下几千大洋  
  
通过子域名收集到的，发现有注册，直接登陆进去试试。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPe4gR1qibLcATu7NER7y2MTWynvMKYhzMictwW1M8FnavdIgQOT69Hpv8g/640?wx_fmt=png&from=appmsg "")  
  
直接在js发现一个接口，通过ai来分析就是查询token值，刚开始以为是查自己的。  
```
auth/qryTokenlnfo
```  
  
当我把参数全部删除，发现竟然返回了所有人的嘿嘿  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPej0qIQ4k89AKibfhAaj7icph5MlJspmxIe9mzG2DfjJSvXfABzfNBDmug/640?wx_fmt=png&from=appmsg "")  
  
然后我尝试使用token-editor的扩展来进行账号接管  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPeSmrNaCQh2BE2VP8yAfLpyKesAX2jvLwCgvCib96P9XRGpAsCicnCvcUw/640?wx_fmt=png&from=appmsg "")  
  
卧槽直接成功了，我干了，nnd，又赚几千大洋，还得是学员呀。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPeTSibticaTsh95lXttm5NPUiayCoYbjqicUOHoguRGyD4DLFbOz3jxsMp8w/640?wx_fmt=png&from=appmsg "")  
  
直接接管成功，几千大洋到手啦~  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPeFaxdKuvgGGSFboaiaXVTozibxq2f4GZzW3Nw5HVyR0N6GB74053exIbQ/640?wx_fmt=png&from=appmsg "")  
  
为了展示危害，找到一个查询个人信息的接口，直接可以批量获取整个网站的个人信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPelKnY53NAwIToEiakA2iaZFu4o6YM0g6vFme9gfBiarvoNfHoaLbfpF4mQ/640?wx_fmt=png&from=appmsg "")  
  
并且还可以修改任意用户的账号密码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsQIPJeFic3BDpqtvh7cbuPellry7HnYoyn65qE6AcsGJBj4YCuZE1DnJVPniav3UcFCELQFKVuBYrg/640?wx_fmt=png&from=appmsg "")  
  
马上打电话让学员马上交报告。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFIRB9Ptb1301lxibuwqf643HtgCpNOfBRDmJ8V3JXw9ZH7vaRFAdktwQ/640?wx_fmt=png&from=appmsg "")  
  
后续直接拿下了，也有视频版放到下面啦  
> 【两分钟讲漏洞01-任意用户接管漏洞】 https://www.bilibili.com/video/BV1xkFPzgECB/?share_source=copy_web&vd_source=40d3d8c4cbf8bd3dc4fe6391b8b8f8dd  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFPib7hicDyc2FfkT83mIOgSfDP2ZoYaN7pqo7YoEG3ahE2LtcDWV7ZyLg/640?wx_fmt=png&from=appmsg "")  
  
## edu漏洞证书站分享  
  
直接发现一个网站，点击忘记密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFtzIV80l8wDMgkwO3M8qG5MILB6jKWWtrIU8GDdVj6Qx70hTpRCVhSQ/640?wx_fmt=png&from=appmsg "")  
  
发送完验证码抓包发现是加密的数据  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFCCTZXZ1qKs7gpicc0RsGOj4W61xpPIbJqsUiasmiae2HZynQMOiccrOebA/640?wx_fmt=png&from=appmsg "")  
  
很明显一看就是aes加密的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFIv7TYhCODAgujcx6VacdyCiaY1Sj7fRTenFQiaibOTtRIic9Qdjl84A4EA/640?wx_fmt=png&from=appmsg "")  
  
开始分析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFQGBdjtRBgn9lqdlochIMECrZe3QsUkI2a5D4H9yW5icXh4p6SNib8oAQ/640?wx_fmt=png&from=appmsg "")  
  
第一个匿名函数会有提示没有定义加密也就是说加解密需要调用此函数  
  
接着在下面发现加解密函数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFPicWo48aiczXTxHpFenJ4jQ3tVo4ZTlcCHicyibcJDPZK6nmOJd7HicT5lQ/640?wx_fmt=png&from=appmsg "")  
  
虽然是JS经过了混淆我们直接在控制台调用就好了，首先是数据的解密  
```
let opts = getOptions(); let cipherText = '这里写密文';  let decrypted = decrypt(cipherText, false); console.log(decrypted);
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFLs82GD8BKssQjepeZ3Gpqrv83YcDt3ic5ls4To7icLMxlFUiagPCL0ibXA/640?wx_fmt=png&from=appmsg "")  
  
  
尝试对刚才数据包中请求包的data和返回包的data进行解密，成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWF4LDqdDC3icd22qa68uvElbsEboKnB5ux5mQCAm8UWMYpz8oBanRXPYw/640?wx_fmt=png&from=appmsg "")  
  
直接写个循环生成加密函数得了，加密请求包data的字典去爆破验证码，控制台生成。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFf8YfkU1OWGdS44ibNOD81CxehIicvlruUAoNLxHeHiaR8EyHu1iawkN2mg/640?wx_fmt=png&from=appmsg "")  
  
得到加密的字典  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFL3JVKt4eocnYoico24jHJDp04zpwHTt2ICIRYXcQWZRGBQ81nLUaZHA/640?wx_fmt=png&from=appmsg "")  
  
重新抓取输入完验证码的包进行爆破  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFCrc4nVrrZFVVZiceUicTaLgYiclQ74Ovoum15fhLGxk35z2GFUFD53yfg/640?wx_fmt=png&from=appmsg "")  
  
成功爆破，解密数据为  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWF9HAjIX7l4JGlhOFMIWHkAKUCk7wRabOHk8CQtFVdVWRZCIq1gDgU2A/640?wx_fmt=png&from=appmsg "")  
  
输入正确的验证码后直接输入新密码即可成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFLDkCe9GInBg0K9Uk2uOW5ogefpicF2rIZbn9jEicMUQ5C4beXEgqLj2g/640?wx_fmt=png&from=appmsg "")  
  
往期文章  
  
[服务号存在注入之有意思的edu漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494659&idx=1&sn=e357db59d806c93f3a5a36b5c312b335&scene=21#wechat_redirect)  
  
  
[edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494702&idx=1&sn=5f0d05b6bea8550eda36ed2ce8ddbf7a&scene=21#wechat_redirect)  
  
  
[学员投稿之edu漏洞的JS逆向解密导致任意密码重置](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494634&idx=1&sn=7cc83a90badea88d7d7d25583bd0c419&scene=21#wechat_redirect)  
  
  
[最近学员小灶总结之双十二特惠](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494604&idx=1&sn=80f030c8114ee3287036586c670289c9&scene=21#wechat_redirect)  
  
  
[卡顿页面导致三本edu证书现世之学员案例分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494572&idx=1&sn=14c21f1cae87dbdbf2ca5c4b10533f5d&scene=21#wechat_redirect)  
  
  
[看完这场EDU通杀刷屏，连我自己都沉默了](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=1&sn=113dd5e17065def94a5dacad361176b3&scene=21#wechat_redirect)  
  
  
[edu证书站挖掘之学员分享案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494524&idx=1&sn=bff39f27ea27bccb884e832603acda92&scene=21#wechat_redirect)  
  
  
[如何快速挖掘低微漏洞-项目挖掘总结版](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494500&idx=1&sn=2da7aa0d40075b462eb27695f2da9e83&scene=21#wechat_redirect)  
  
  
[公众号接管漏洞之偷偷加](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)  
  
[小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)  
  
  
[辅助学员审计案例-php代码审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=1&sn=2feaf2786717c2c577fe0b5230cbc58f&scene=21#wechat_redirect)  
  
  
[学员-补天800赏金报告分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=2&sn=c54ea91e0b3dc79f48f54f931df413c0&scene=21#wechat_redirect)  
  
  
[从js逆向到sql注入waf绕过到net审计-edu证书漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494171&idx=1&sn=0d589d01dfbb068e53f9ad9c22676d7a&scene=21#wechat_redirect)  
  
  
[空白页面引起的高危src漏洞-再次绕过](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494082&idx=1&sn=6d1cc92a049d28b5395d417e0a5203a5&scene=21#wechat_redirect)  
  
  
[空白页面引起的高危src漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494061&idx=1&sn=bfb1406138041fcba8286811aa7ac6e1&scene=21#wechat_redirect)  
  
  
[难忘的优惠劵漏洞(深情哥破防版)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494035&idx=1&sn=422326cc617c33c78b3d518471e0862d&scene=21#wechat_redirect)  
  
  
[什么？又日母校？竟然还有表扬](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)  
  
[信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)  
  
  
[sql server注入靶场搭建](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493947&idx=1&sn=885ee489f74211ba26a4a097f7ba30d6&scene=21#wechat_redirect)  
  
  
[记一次学校ai沦为我的宠物之拿下e](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)  
  
[du证书](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)  
  
  
[疯狂星期四两本证书漏洞合集](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493926&idx=1&sn=06ac298909e27d0e37fef90f64b205da&scene=21#wechat_redirect)  
  
  
[湘安无事之深情哥版edu+src培训](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493855&idx=2&sn=bb025b6a32bc022319f8dc8057a6436d&scene=21#wechat_redirect)  
  
  
[记两次js逆向拿下985证书站(学员投稿)~](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493855&idx=1&sn=0d507bc1f90b04588393698ee1c2d4b8&scene=21#wechat_redirect)  
  
  
[重生之我在教育园暴打小朋友](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493410&idx=1&sn=17df8a525145bf062ed5d6ecc3e09539&scene=21#wechat_redirect)  
  
  
[某医院微信小程序签名机制绕过分析](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493408&idx=1&sn=672ff76188ab6c97bc1b8d688ac7228f&scene=21#wechat_redirect)  
  
  
[记二次帮学员拿下edu证书站](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493399&idx=1&sn=425e84fa877f789598a2e8afdf8320c6&scene=21#wechat_redirect)  
  
  
[记一次难忘的net直播审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493369&idx=1&sn=e10ae1cd25ece5fe3c3ca4c2b455cb51&scene=21#wechat_redirect)  
  
  
[记一次小米-root+简易app抓包(新手)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493374&idx=1&sn=7dea1086256be1d5a2b1a18fa4ab3be0&scene=21#wechat_redirect)  
  
  
[记一次带学员渗透母校](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=1&sn=7b1881174201094a5449fe1400ddc8a6&scene=21#wechat_redirect)  
  
  
[同学，你试过交edu漏洞交两天两夜嘛](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=2&sn=0d706a4064111b3e131f24460b2f2c56&scene=21#wechat_redirect)  
  
  
[手把手带学员拿下浙大edu证书](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=4&sn=cd157b6471a1ab1e63b8dbfe0f62b42e&scene=21#wechat_redirect)  
  
  
[记一次手把手带学员拿下600赏金](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493151&idx=1&sn=3e1a791a4d14b9ad21d2f0afe8a455a2&scene=21#wechat_redirect)  
  
  
[深情版edu+src培训讲解(3000)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=2&sn=9dfb9ceda7361c9523471a64d8f16f5b&scene=21#wechat_redirect)  
  
  
最后总结  
  
感兴趣的可以联系深情哥进群  
，有公开课会在群里面通知，包括审计和src。  
edu邀请码获取，咨询问题，hvv渠道推荐，nisp和cisp考证都可以联系深情哥  
。  
  
**内部edu+src培训，包括src挖掘，edu挖掘，小程序逆向，js逆向，app渗透，导师是挖洞过40w的奥特曼深情哥，edu上千分的带头大哥！！！联系深情哥即可。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuia9ElbKdSKcUez91EkPBWFokDtf71hO1acCjaYBZ5t3WoIBDYdPZ0PMwXK6z5VGyQ3CBQ0MtTvXg/640?wx_fmt=png&from=appmsg "")  
  
  
  
