#  记某edusrc的任意用户密码重置漏洞挖掘  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-01-21 10:11  
  
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
在面对登录框的时候，特别是有图形验证码，登录功能
弱口令啥的不好测试的时候,去看看登录页面其他功能
，比如忘记密码等，往往会有更好的突破。
```  
```
一位好兄弟的案例，一起学习一下。。
登录框，没有突破，直接尝试测试，忘记密码功能。
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILGXce3rtFAREoZliauWV2PhXaicOXjNfACGYJbNWXJX2rHum9RsTibvxyg/640?wx_fmt=png&from=appmsg "")  
  
忘记密码功能常见测试思路  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILOyzwDbSnJ5OgACsUMDKHkE9hqOxlRCuevMdH6v4jq1xqc6x5uTEaVA/640?wx_fmt=png&from=appmsg "")  
  
通过忘记页面，发现需要邮箱地址，进行重置  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILSPD9TgcXrKDP63DxaLoJh5iaQrPrzx9CsE4gyTTTlkj5uMm4EGxNtvg/640?wx_fmt=png&from=appmsg "")  
  
这里可以使用google语法去收集一下（登录需要学号）  
```
site:xxx.edu.cn 邮箱
site:xxx.edu.cn 学号
```  
  
把同时出现邮箱和学号的邮箱先记录下来  
  
在忘记密码页面输入邮箱，点击发送验证码之后，随便输入一个验证码进行抓包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILiaDF1OY3icmwXcxJ4aAjibGksYkSCqx0OMJ3NWkt8RtMFjVpHTUnNy4ng/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILvdzGJCh0TbmATJUj2Pem0QHsj7micUkAkrKGtyjd1BF7xUP1zhKQyQQ/640?wx_fmt=png&from=appmsg "")  
  
放掉第一个数据包（没有验证码，应该是检验邮箱是否存在的），  
  
看到第二个数据包（同时出现邮箱和验证码）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOIL5rzegGmibwkDTf6qTeD8SBlnDY4HsSPPE63O3dD2WtYfLTI0Ao5W4mA/640?wx_fmt=png&from=appmsg "")  
  
右键点击拦截响应包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILOVyZbtLwswoARRPGlrkAHxF2McvEjdccKYsjsLDUicmvj9TRQB7ak4Q/640?wx_fmt=png&from=appmsg "")  
  
经典返回，error,修改为success进行放包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILQ1gW7Fq5Q5Riaiat2Zeoqye8vdQxvicPAKMgK6vxqlxQdicxTrCjaw3aPw/640?wx_fmt=png&from=appmsg "")  
  
返回包修改小tip  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILjBgsvh3yG4E1B8vhZDhibMAqNQVhxWuGUSAOcic8KBJib0Xib73Vicibz8Rw/640?wx_fmt=png&from=appmsg "")  
  
然后来到输入新密码阶段  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILdvsZPeyvRjticEicGbicJxJjqnpN5ww1sP7QfQGbtoiau3uUadZyPPS3lA/640?wx_fmt=png&from=appmsg "")  
  
正常输入符合规则的密码，进行重置，点击下一步，最后重置成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOIL7NqBrBfBnxEy9BZouHKYiaNvlL1R2vFwxvAmYObKVicYEgXeOzrzcm1w/640?wx_fmt=png&from=appmsg "")  
  
返回登录页面  
  
输入我们收集到的学号和重置后的密码以及正确的验证码进行登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILbtvukxzGRoee5jjaWLuW0QibMDcc8cUruBMRQ0eOPrHAs1Dq1tXB7oQ/640?wx_fmt=png&from=appmsg "")  
  
成功登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6fer3ibXfH2vjo7IHINxOILV2SJuWeH2Bqr1uXJTNrc5YxQ3WsxGwX3wMtwKKpkAjmRP0GRN7eIaA/640?wx_fmt=png&from=appmsg "")  
  
over,over  
  
后台回复  
加群  
加入交流群  
  
有思路需要的师傅可以加入  
小圈子   
  
主要内容是（2025-2026/edusrc实战报告）其他内容无需多言  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg "")  
  
密码重置常见思路文字版  
```
任意用户密码重置

Access-Reset-Ticket
直接重置admin密码，可以看到请求头里面有这个Access-Reset-Ticket，复制他的值，直接重置管理员不成功，我们可以自己注册一个然后，重置的时候替换管理员的Access-Reset-Ticket，进行重置然后可以，任意用户密码重置

抓取数据修改手机号获取验证码之后输入之后再次修改手机号绕过验证进行重置

任意邮箱/手机号验证（验证码与绑定用户未统一验证）

通过他人手机号找回密码，抓包，将他人手机号替换为自己的手机号，获取验证码，提交后修改密码

通过自己手机号找回密码，获取验证码后抓包，将数据包中的用户ID改为他人账号ID，提交后成功修改他人密码

邮箱找回
构造链接修改别人的密码
通过邮箱找回密码，URL链接中修改用户ID为他人，邮箱不变，之后通过链接可以将他人账户绑定为自己的邮箱，之后通过邮箱找回密码

错误验证码
进行爆破

正确验证码
修改手机号为其他的看能否成功

任意/批量用户密码重置

用户绑定手机号枚举/账户名枚举

短信相关（短信分发之类的）

修改返回包绕过逻辑验证

越权修改别人的密码

auth值可以枚举导致密码重置问题
用户修改密码时，邮箱中会收到一个含有auth的链接，在有效期内用户点击链接，即可进入重置密码环节。而大部分网站对于auth的生成都是采用rand()函数，那么这里就存在一个问题了，Windows环境下rand()最大值为32768，所以这个auth的值是可以被枚举的。如下面这个代码可以对auth的值做一个字典。$a=0;
for ($a=0;$a<=32768;$a++){
    $b=md5($a);
    echo "\r\n";
    echo $b;
}
然后重置某个账号，并且对重置链接内的auth进行枚举。

密码重置时候注意观察有没有step类似的字眼进行流程跳步操作，升级版就是如果没有这种操作可以先正常进行重置，到输入新密码的这一步看能不能直接未授权访问到
修改返回包

一个任意用户密码重置的点可以先用自己的信息进行重置抓取完整的返回包，然后再输入别人的信息把返回包替换为自己的完整返回包，然后放包可以重置他人的信息
另类密码重置
密
码重置使用刷脸进行重置
进行信息收集对应的账号和图片然后使用图片刷脸进行简单绕过

使用手机号加姓名进行重置
知道手机号加姓名去重置，知道手机号去找姓名知道姓名去找手机号，然后后续可以测试，两个到底是对哪个参数进行了重置，是手机号还是姓名，还是两个都做了鉴权，从而扩大危害

不可遍历id配合信息泄露实现任意用户密码重置

在进行忘记密码测试的时候发现是通过类似id之类的东西进行鉴权的于是找到可能泄露他人id的点进行查找从而替换实现越权
```  
  
  
