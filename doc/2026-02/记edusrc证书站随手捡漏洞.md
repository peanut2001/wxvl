#  记edusrc证书站随手捡漏洞  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-02-26 09:46  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
  
前言  
```
运气也是运气的一部分，和实力不沾边。
```  
  
漏洞测试  
  
小程序起手,输入学校的名字,看到相关程序开始测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ0XremKK3sKs1uI1tD6NbZhdKq5hSXdicj7Qd6fGkIJ3MSNFoKXnHyvKkVmR9Dic50aKRxAZVfwf3d6ER619wg3b9ogESgjg20Q/640?wx_fmt=png&from=appmsg "")  
  
点击显眼的预约功能进行查看，可以看到这个页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQXgPzSjkXicKVtb73NPzKOJLeV8AxhWNOMzgpQeXFqGXbj9qqLL9D21uFcVMNkPp7vbMwXynaXQfA7lbJn10QYMEFibIOPjfrYs/640?wx_fmt=png&from=appmsg "")  
  
输入手机号正常获取登录不进去，针对edu的测试，当前功能点可以尝试  
测试这三种。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQmljm7tDyvZklGVnIF1PFWOD6yb0aMleuHYQbR9jtqibnWhZeCVGt2Ag0jZSTqPuzTw1Kiaibic7h2p1ibZFx7X9Phch1bxjBPb7CY/640?wx_fmt=png&from=appmsg "")  
  
先收集一个手机号，当前学校学生的手机号  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTyCbyA2Cf4XBQnKkLR5DnQLE0ZDrTtukUEjGWbPqT93XC95612yRnUnticjcry3kGga0iaqyvYDSYZHCP7KC5SCGA2TrcPa9rL8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRIsXMsGK6IMqTnOdq6u8ia100J9icErZibUqsIcx0BAVtPkzichd3YZkTMicXkgxS8AL215SiaVk8pTlhcTrMcOtqXksPoKR8EA4bA/640?wx_fmt=png&from=appmsg "")  
  
google语法简单找到，拿到手机号测试  
  
短信验证码回显不存在，短信分发不行，验证码都发不出来爆破也没戏。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQmPs4orMlGrBWTcZ21hDB8qa5e2MXiaf15tQkgN65IbILFT8auam9gz2xcicAszrAlziaIMqUiaLTy9QYn1GxO7jqchFvVbnVWOZc/640?wx_fmt=png&from=appmsg "")  
  
这就是证书站的强度吗？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4vURzxOrTDy2besf0KV1BCtstTAjwvFAQia337YIV9nPSUmA66vgiarK5qBaT8oIV4wVtFAsSu3ic4w/640?wx_fmt=png&from=appmsg "")  
  
柳暗花明，复制小程序的地址，在浏览器打开，往往有想不到的效果，尝试访问之后又看到一个登录框。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSReBwo0uCsxZCEaTia6Bvyk3nZoCh4H5Ea5IOU6XshLd6y7qehibbm4ZiaWQvK1Xk5xlic56XCGc4QOOQm77EVJfvpDem6xr9Cibhg/640?wx_fmt=png&from=appmsg "")  
  
尝试一下常见的思路，弱口令没成功  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVggRicNjXicZUia3MzdTr5rpjrEe9PXtias5qibmZakicfufUC6Ugt9ib8MgWHCjKmqSW55SnsgMpxJuqVtDtIToT8mdLUMapsvaZVY/640?wx_fmt=png&from=appmsg "")  
  
看看接口，有好多，get/post啥的跑一下，edu没必要根据结果构造参数啥的跑，找找二级路径配合接口简单测测就行，资产多，没有就换，主打效率。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT9OlaRw0GIOHqib0LichKlpicIweQYjJPibY7hicLEa9tqaGSua140NQrZ3ZqMK6un9YnIReS3tD3wt2pibRAetedokZdmvWVKticw9Y/640?wx_fmt=png&from=appmsg "")  
  
进行尝试，最终也没啥东西。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRGXoOASLjDnJ5Sqjr6Ogb3wB4yJLOdibUKiaNWKFYf6WcBlHz2fBOXWowBEF0547BCHBviagKFyyDeVcNSZdrdddSf0FGx66uwPY/640?wx_fmt=png&from=appmsg "")  
  
针对当前功能在edu的场景下，不存在用户名枚举，可以尝试使用常见的用户名配合密码进行爆破，但是密码是加密的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBU5Fax242h3pdhGLtdkdCic3X8UZpjcHrRkYqBzaIqUsnJfWZLttPaJJj5ia0qBJ6KxkiazT1R0NrvEicRnXiaK0dO8nIcwd3TN88/640?wx_fmt=png&from=appmsg "")  
  
而且不是base64  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQS7J0ZBZNgemKM1st1TlZmDiat5sJAET4nqtq0NIb8IINtRdtnxq7YatLPAtJRPZ4QKMkOMBOs85nUnoACcnhicmgEKF3FXH6ibM/640?wx_fmt=png&from=appmsg "")  
  
这个时候可以固定密码爆破用户或者js逆向进行解密，选择前者，但是最后也是没有找到弱口令，账号锁定，url重定向啥的edu也不收  
  
试试了试sql也不太行,会过滤符号，然后返回这种结果  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboROzCjle8HDOElKCtvnx8YZd3aqzUMPu5FQHzZuRa7BrVVbHkib6h1fVxg3Ebr0mVjgVUEw2ElP6lQ6E38yI48MLjTF10pgslSs/640?wx_fmt=png&from=appmsg "")  
  
没招了，打开思维导图在看看漏了哪些点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSjYEUwrTokOicvoeuPk2ZYrlqysFEoOiajv2ia6CcqpbwtE9ULXgTKLs1pVfElmpdDcBo6SlAPCUScycnl42kJHxK93YsTtE4Arg/640?wx_fmt=png&from=appmsg "")  
  
这次捡漏洞靠的就是他，其实还是太粗心了，每次看插件，只是看接口错过了很多好东西，还好又梳理了一下。  
  
登录页面有身份证号你敢想？  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSqeVhV90q8R8V3hY3Phfa8fzVLE6AptGZaCYz7ceT6BqpaXwLb9zuW5MsibicRB9kuib3Xic5XialIRibKicOgdp3Qrz26F9LPwEBz5g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRQc9Enp6FvnXN0OmA5tSeBZ7PxIGiaKRVo1ibELBQLuYibHKCic2iaap9ia1dO3thQNquOaCJF0OHcJzTASdbCia7xhbQcpNgJibJWicqI/640?wx_fmt=png&from=appmsg "")  
  
进行解码尝试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTwY53RRqYBiaIsXZw2QAAktOjicibBciaydEwCkJoaqB2x5qmibcu5zUtjfg9vQX64BguembU4GDPsicNv2S4qSmSL5u7ByHDmOibWrc/640?wx_fmt=png&from=appmsg "")  
  
又瞅了瞅，还有弱口令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRcmNg4rFozAA4H19mbRf5XTLx2fDT82L8C0dn4jE1ZFR65OgicfzUVMM1neBV6GQSpCUPLYiadictWGQudIR9xr4pJcMiciciacAV84/640?wx_fmt=png&from=appmsg "")  
  
进行登录尝试失败，检索看一下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRS1uRDUTqgxictPvMTPRKbWibW4eQicRz7vrHHDCsRQ0QEzicHndfjibicgmTKpjP8S3b7Dwu6iaxZaFcsVVvkZy8O1UBsnb9DkOB3pI/640?wx_fmt=png&from=appmsg "")  
  
原来是其他ip的，这里就没东西了，后续扫了一下ip的全端口  
  
没找到web，打包提交，水个低危漏洞。  
  
万万没想到，感谢师傅，又水本证书，没滋滋。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQMO3VTAqqcPLnodXRIXeB92zMrUfHm8qiasWbpSOLvTexMzURicOFySourboNzMlPvlMSWN6FdAGOpib0HibKfiaUx6CHZPZaUkE6w/640?wx_fmt=png&from=appmsg "")  
  
  
后台回复  
加群  
加入交流群        
  
有思路工具需要的师傅可以加入  
小圈子                               
  
主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/src学习资料等）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg "")  
  
部分思维导图展示  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，目前300多条内容，持续更新中。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboR62DgT5O1EN2BAoeuib0MK0Pl43pvCLVia2lKAnotaUfutyQ9licdV0TFBr4A6jnzbPX9rHsTtWdThK6kpSiaGEGWCEGesecVo3PE/640?wx_fmt=jpeg&from=appmsg "")  
  
