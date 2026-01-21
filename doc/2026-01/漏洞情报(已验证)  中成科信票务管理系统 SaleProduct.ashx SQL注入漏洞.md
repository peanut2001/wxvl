#  漏洞情报(已验证) | 中成科信票务管理系统 SaleProduct.ashx SQL注入漏洞  
原创 wdgs
                    wdgs  WDCIA   2026-01-20 23:01  
  
动动小手  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/wR4G22TgErjfNpreeU6zMsUZOotoQgCSFfDdOpb1BgkAUaA1Ijhdd2MbcXKK6cwvfkY6G7m0BRoUt22zXu4nMQ/640?from=appmsg "")  
  
点个  
关注  
～  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HtBSeqUljlEX2U86CRIHg5OYkFjEichJCBOiao1DictoCzicWNibby5tkTS2mHic455icX62rECv7RrxTavz0Q4xHRZdw/640?from=appmsg "")  
  
内容仅用于学习交流自查使用，由于传播、利用本公众号所提供的POC信息及POC对应脚本而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号WDCIA及作者不为此承担任何责任，一旦造成后果请自行承担！  
  
如文章有侵权烦请及时告知，我们会立即删除文章并致歉。谢谢！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/3P3vXeGVfAjC9ib3Kr2ouds4E1crXD1wROicQHa8JpRHJEdxsIicN9t1fhUrsnyEEzgynlxZ3cGOdXkhGfpyAh0YQ/640?from=appmsg "")  
  
#   
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**01**  
  
**漏洞介绍**  
  
      
  
      
  
      
中成科信票务管理系统   
SaleProduct.ashx  
 接口处存在SQL注入漏洞复现，未经身份验证的恶意攻击者利用 SQL 注入漏洞获取数据库中的信息(例如管理员后台密码、站点用户个人信息)之外，攻击者甚至可以在高权限下向服务器写入命令，进一步获取服务器系统权限。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**02**  
  
**影响版本**  
```
中成科信票务管理系统
```  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**03**  
  
**测绘语法**  
  
  
测绘语句:  
```
关注公众号，回复 中成科 获取
```  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**04**  
  
**POC**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/nvJGLMmlzsHqOiaxRicopXfRqq4JYbFWpCxQu7DtZnNtyLgQrLeDeWUlruWl11bHv2cNRF5hibtMpjTor8HZ0ZX1A/640?wx_fmt=png&from=appmsg "")  
  
POC已放置圈子  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HtBSeqUljlEX2U86CRIHg5OYkFjEichJCBOiao1DictoCzicWNibby5tkTS2mHic455icX62rECv7RrxTavz0Q4xHRZdw/640?from=appmsg "")  
  
圈子  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/3P3vXeGVfAjC9ib3Kr2ouds4E1crXD1wROicQHa8JpRHJEdxsIicN9t1fhUrsnyEEzgynlxZ3cGOdXkhGfpyAh0YQ/640?from=appmsg "")  
  
  
  
    圈子刚刚成立，专注于漏洞情报分享，不发烂大街的东西，不定时分享红队工具，欢迎加入，每日更新1-2个 0/1 Day（目前已更新100+）  
  
圈子新人优惠券已发放完，后期不定时发送，价格随人数增加而增加  
  
![](https://mmbiz.qpic.cn/mmbiz_png/nvJGLMmlzsFvvkgWGewJdZJCcnVTJDMQ136zQewU0FWFNeAqlquOvoogc5WziaJYVQXU6YJ6LtK6bO6NyanWViaw/640?wx_fmt=png&from=appmsg "")  
  
往期推荐  
  
[漏洞情报(已验证) | 时空智友企业流程化管控系统formservice 存在 XXE漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484018&idx=1&sn=141c8cfdd99ea23c90b70ac1b4d761d2&scene=21#wechat_redirect)  
  
  
[【已复现】| 帆软export/excel sql注入](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484013&idx=1&sn=514d45521e2166d6f28f10eee4417bef&scene=21#wechat_redirect)  
  
  
[【已复现】| GeoServer 未授权XXE漏洞(CVE-2025-58360)](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484006&idx=1&sn=4afee46de06596f891b173b27918ea41&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 友加畅捷U+财会通 GetZTList 存在敏感信息泄露漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484002&idx=1&sn=a00ca88da2b64ef56d0169055cc35aa1&scene=21#wechat_redirect)  
  
  
[漏洞情报 | 0 Day 某信智能公交系统 SafeDevice_Mng.aspx 存在SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483945&idx=1&sn=a308958e88a92a2d63eb89ad82f0c2a8&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 0 Day 全程云OA Statistics.ashx 存在SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483924&idx=1&sn=8dbfcb4a9944a19bf8468803b0fb80f8&scene=21#wechat_redirect)  
  
  
[漏洞预警已复现| 0 Day 力软敏捷开发框架***********ad存在任意文件上传漏洞(非CrawlerHandler)](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483887&idx=1&sn=a00974871b90a9d61f0867e8544f6d94&scene=21#wechat_redirect)  
  
  
[漏洞复现 | 用友 U8 Cloud 文件上传绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483895&idx=1&sn=d0bbaa35a7ea04d8a63b8c56285ca8b0&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 0 Day 万户OA getNextAutoCode 存在SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483873&idx=1&sn=dc82d0c0ce79856e640eacf8d1647cd0&scene=21#wechat_redirect)  
  
  
  
  
  
