#  记一次SRC漏洞挖掘：万能验证码与任意用户密码重置之旅  
原创 tangkaixing
                    tangkaixing  开心网安   2026-03-03 02:55  
  
**免责声明**  
  
由于传播、利用本公众号开心网安所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号开心网安  
及作者不为**此**  
承担任何责任，一旦造成后果请自行承担！如需要转载等，请标注文章来源。如有侵权烦请告知，我们会立即删除并致歉，谢谢！  
# 概述  
  
很久没有在渗透测试中遇到验证码类的经典漏洞了，这次在某SRC的测试中，意外发现两个接口分别存在“万能验证码”和“验证码可爆破”问题，组合利用可导致任意账户登录及密码重置。本文记录这次小随笔，重温那些年我们一起挖过的逻辑漏洞，  
于是我就记录下来，也水出一篇文章，感谢各位看官的理解与支持  
。  
# 正文/引言  
  
说实话，在现在的SRC漏洞挖掘中，验证码绕过漏洞已经越来越少见  
[个人观点勿喷]  
大部分系统都接入了成熟的短信服务商以及现在AI的加持等，验证码随机生成、有效期一分钟、错误几次就锁定等。然而，就在我测试某SRC在线学习平台时，一个古老的漏洞类型突然撞进眼帘，让我不禁感叹：经典永不过时啊。  
# 发现登录接口的“万能钥匙”  
  
目标是一个SRC教育类系统，登录页面支持手机号+短信验证码。抱着试试看的心态，随便输入一个测试手机号和1111验证码，然后抓取了登录请求包：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDTXqRq5oQJtlWK61pCtU4iciaRHXlJZTiaS7MSibo11IibhuzD2EuSZ5kDQ6Kj1HMZ7D0dB9UVbsaRaevxAgRejSSS0bJuuydTFwDSk/640?wx_fmt=png&from=appmsg "")  
```
POST /xxxx/api/wap/v1/account/login HTTP/2
Host: group.xxxx.cn
...
{"type":"code","code":"1111","phone":"13200000000"}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDTjernaEKvGvvTiaKGyHJgsu8xIriaKaMcKdJVm0Aia3nRIic86icJHWEcVDCaJtz1XcryVCdO7Rsxp7DPbSMmZCgXiaibhCbweiba2SGA/640?wx_fmt=png&from=appmsg "")  
  
响应成功返回了用户信息和token。  
code  
字段的值是  
1111  
，这引起了我的警觉。难道这是一个万能验证码？我立刻在Burp Suite中修改手机号为自己另一个测试号码，同样返回成功token。接着，我直接使用收集到正常用户的手机号，依然返回成功。至此，可以确认：  
后端未正确实现验证码验证机制，而是使用了固定值“1111”作为万能验证码  
。  
# 遍历手机号，接管海量账户  
  
万能验证码意味着什么？意味着可以枚举手机号，批量登录任意用户。我迅速将请求包发送到Intruder，把  
phone  
参数设置为payload位置，加载常见手机号段字典和收集到该src的相关手机号。几分钟后，上千个有效用户的toekn纷纷返回，虽然大部分是普通学生，但也不乏教师和管理员账户和测试用户。这漏洞一旦被恶意利用，后果不堪设想。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDS68qibd4gD81EaBgu2agLX6kM3LHEUFDqiaAl5mNbZ8OjuFNzD0icS08nQnIYd105HTicoh2StJUOIe0CquQ0O9Lt59oStYsUz8ns/640?wx_fmt=png&from=appmsg "")  
# 举一反三：密码重置接口的相同缺陷  
  
登录接口沦陷后，我下意识地想到：密码重置接口会不会也存在同样的问题？毕竟很多开发会复用验证码校验逻辑。很快找到了重置密码接口：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDQ8jq4icbt9t5YCLBAIqvVUHzyaEOuyQxXUXlE9toBwO38mib0sHrhtRFicqM3TCPgyvnUZiaItibTuic3RicKmAfnj9uG0NmqoSkck14/640?wx_fmt=png&from=appmsg "")  
```
POST /xxxxx/api/wap/v1/account/resetpwd HTTP/2
Host: group.xxxxxx.cn
...
{"phone":"13200000000","code":"1111","password":"Aa123456"}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDSyzkdHQTtZjsG8Ek6Ecrce8oZ079WzsuI0DE6lypB6zVibaKDGbicyBWiadJJM187YTkiaPvFKskicV4SclJgzReb08Qu4sundx058/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDShb1icsUjMk7CdpLGiaUlE8slIftxM89qDYMxuDvbicG6dNZFP05dUMyd2ibJkRLgWYJhPa8sUY4lAvawiak52xk4d2KYQQF5BoxV4/640?wx_fmt=png&from=appmsg "")  
  
尝试修改手机号和密码，果然，  
code=1111  
依然有效。更wo  
艹的是  
，这个接口没有任何错误次数限制，也是可以暴力枚举常见的验证码组合（如  
0000  
-  
9999  
），只要后端验证码不是动态生成的，就能轻易爆破成功。  
只需知道目标用户的手机号，即可通过该接口直接重置其密码，从而完全接管账户的风险。  
# 总结与反思  
  
这两个漏洞的本质都是  
验证码校验机制缺失  
，但表现形式略有不同：  
  
登录接口  
：采用了硬编码的万能验证码，属于最原始的“后门”行为，可能是开发调试遗留。  
  
重置接口  
：虽然验证码可能是动态生成的，但未限制尝试次数，且未绑定会话或手机号，导致可暴力枚举。  
  
从攻击链来看，两个漏洞都是可以独立利用的，但组合起来威力更大：先通过登录接口获取任意手机号对应的token，再通过重置接口修改密码实现长期控制。这种“验证码类漏洞”在OWASP TOP 10中属于“失效的身份验证”范畴，虽然技术门槛低，但危害极大。  
# 为什么现在还能挖到这类漏洞？  
  
按理说，验证码安全已是常识，为何高校和企业系统还会存在？我个人分析可能有以下几点：  
  
快速迭代遗留  
：很多系统由外包开发，上线前未做安全测试，调试代码被带到生产环境。  
  
验证码服务降级  
：部分开发为了节省短信成本，在测试阶段使用固定码，上线时忘记替换。  
  
缺乏纵深防御  
：即使验证码正确，也应检查手机号是否与当前会话匹配，但很多系统完全信任前端传入的数据。  
# 反思  
  
这次挖掘经历让我重温了最初的渗透乐趣—不需要复杂的0day，仅仅靠逻辑缺陷就能拿下系统。验证码作为身份认证的第一道防线，必须做到以下几点：  
  
动态生成  
：验证码必须是随机数，且与手机号、会话绑定。  
  
一次有效  
：验证通过后立即失效，防止重放。  
  
限制尝试  
：错误次数过多应临时锁定，并增加图形验证码。  
  
日志监控  
：记录异常请求，及时发现暴力破解行为。  
  
  
挖洞如此，人生亦然——有些经典漏洞，即使时代变迁，依然会以熟悉的面孔出现。而我们能做的，就是保持敏锐，让每一次“偶遇”都成为提升安全水位的机会。  
  
