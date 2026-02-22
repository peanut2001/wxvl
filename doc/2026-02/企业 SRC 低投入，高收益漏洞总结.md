#  企业 SRC 低投入，高收益漏洞总结  
 sec0nd安全   2026-02-22 02:54  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具等资源而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任!  
  
01 背景  
  
总结下企业SRC常见的低投入高收入的漏洞，供各位师傅实战参考。  
  
号外号外，  
免费的睿鉴安全知识库上线了。点击下发链接，福利直达！！  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4dewc1NpibJQQ9JicEy2NOBBJ0jiaB5V1EFzPakRTCTJ3Ra4HicPLN0RjOwviaSTxIHibBwtO1RA263ibhwy8JmQicHSovMdEStFWmIhQZE/640?wx_fmt=png&from=appmsg "")  
  
安全知识模块，只要放一些实战的案例，目前已更新四期内容，后续会持续更新。主要内容如下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4ddFeIlQnPOcSRuZ258VFS3oMqOrXhvpJmvJpic3HLJIql93uZOpdltEQYYDFgHf7Hebsz67lMo4XjCQVDexRFljZ6mWUHrWCxws/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dfbP7t3KgSxn5ZkPkNWpbIFib6INAj29ajJV2MdkNwsdL3ZB3YHXRjjNbLjVo8uC1gDd5EPYwxz6jeIeQhbx68RHBbBMHOaKyuU/640?wx_fmt=png&from=appmsg "")  
  
资源中心，主要会放一些安全工具，给各位师傅提供一站式下载的渠道，目前已上线20+款工具，主要工具如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dcJibibRQFYDHJwSJKcHM2MxTN4XehibWoyKFQtJD3hFKpkFlj4czZFq25TVvJhHcdGGDUfQLqKAxle5UqNPB5uRwkO0RYz3IkM8w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dfCHURkY4rDWfnYZDdWHZ1rZ3LqLap8nqJuUS3K1L6M0Q4IVqG93lhB4VdNnq5utCgam6X5m8iatylS9rOBWJGP2FqjAqkp0np8/640?wx_fmt=png&from=appmsg "")  
  
  
02 常见漏洞  
  
1. 未授权访问 / 越权漏洞  
  
特点：不用复杂工具，不用代码审计，纯手工测接口  
  
常见功能点：  
- 接口不带 token /cookie 就能调用  
  
- 用户 ID、订单 ID、企业 ID 直接遍历  
  
- 后台接口、导出接口、列表接口未鉴权  
  
收益：中高危为主，SRC 赏金非常稳定  
  
成本：几乎为 0，抓包改包就能刷  
  
2. 敏感信息泄露  
  
特点：不用攻击，只要发现  
  
常见功能点：  
- 前端 JS 泄露密钥、API Key、Secret  
  
- 配置文件、日志、备份文件暴露  
  
- 接口返回手机号、身份证、内部地址  
  
收益：中危居多，极易成批提交  
  
成本：目录扫描 + 看 JS 就能出洞  
  
3. 逻辑漏洞  
  
常见功能点：  
- 任意密码重置（验证码可绕过 / 可爆破）  
  
- 越权修改他人资料 / 解绑手机  
  
- 支付 / 订单逻辑缺陷  
  
  
收益：高危多，赏金高  
  
成本：只需要正常走流程，抓包改参数  
  
4. 弱口令 / 默认口令  
  
常见功能点：  
- 后台、OA、运维系统、测试环境  
  
- admin/admin、Admin123、公司域名 + 年份  
  
收益：高危，一拿就是一个后台  
  
成本：字典跑一下，成本极低  
  
5. OSS/COS 对象存储 未授权访问  
  
常见功能点：  
- 阿里云 OSS、腾讯云 COS、七牛等可直接列出文件、下载源码、备份包  
  
收益：中高危，批量神器  
  
成本：抓包找 bucket 名字，浏览器访问即可  
  
6. XSS  
  
反射型 XSS、存储型 XSS  
  
常见功能点：  
- 搜索框、评论、用户昵称、URL 参数  
  
收益：低–中危，但容易大量过审，适合冲排名  
  
成本：简单 payload 就能测  
  
  
  
往期好文  
  
[网络安全人员的金牌证书：为你铺就高薪职业之路](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484847&idx=1&sn=62fefecfbed336486f417e60bdf5fdd2&scene=21#wechat_redirect)  
  
  
[【SRC实战】简单FUZZ拿下高危漏洞](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485405&idx=1&sn=669a4286abd1103b050059efdb3da268&scene=21#wechat_redirect)  
  
  
[AI大模型“越狱”实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485551&idx=1&sn=5e2accbd716bf890c37a9fb7be4c06b7&scene=21#wechat_redirect)  
  
  
[【SRC实战】任意用户密码重置实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485484&idx=1&sn=e3ccb64ef54194ae4216c1d43606b651&scene=21#wechat_redirect)  
  
  
[【SRC实战】记一次越权测试实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485379&idx=1&sn=37985dd7e56a66b2d023548eabd845ea&scene=21#wechat_redirect)  
  
  
[免密登录某后台管理系统实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485024&idx=1&sn=71c596dd36800993e18f1f05b9d37547&scene=21#wechat_redirect)  
  
  
[安服人应急“薅洞”指南](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485381&idx=1&sn=d0195d62adf45f6d614c785886d04e92&scene=21#wechat_redirect)  
  
  
[推荐一款资产筛选工具](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484744&idx=1&sn=7d205189f4a95c2a0cce1b6e99014c64&scene=21#wechat_redirect)  
  
  
[【SRC实战】短信验证码爆破，拿下某众测中危](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484618&idx=1&sn=9ef1826481eaace69ebef6849995bcfa&scene=21#wechat_redirect)  
  
  
[【SRC实战】一次“链式”渗透，从站点A打到站点B](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484164&idx=1&sn=9c2db3fc19000f60785499f2c4ad1f6f&scene=21#wechat_redirect)  
  
  
[用户账号接管实战，洞穿开发者逻辑](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247483991&idx=1&sn=c1f6e65233cf18ade53b6e566fa4b3af&scene=21#wechat_redirect)  
  
  
