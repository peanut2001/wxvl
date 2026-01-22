#  某edusrc小程序rce漏洞挖掘  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-01-22 10:52  
  
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
  
后台回复  
加群  
加入交流群  
  
有思路需要的师傅可以加入  
小圈子  
  
主要内容是（2025-2026/edusrc实战报告）  
  
  
其他内容懂得都懂，持续更新中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
