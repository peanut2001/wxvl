#  漏洞情报(已验证) | 深科特 LEAN MES系统 WarehouseCheck.ashx 存在SQL注入  
原创 wdgs
                    wdgs  WDCIA   2026-01-26 23:00  
  
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
  
      
  
      
深科特 LEAN MES系统 WarehouseCheck.ashx 存在SQL注入  
，  
未经身份验证的恶意攻击者利用 SQL 注入漏洞获取数据库中的信息(例如管理员后台密码、站点用户个人信息)之外，攻击者甚至可以在高权限下向服务器写入命令，进一步获取服务器系统权限。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**02**  
  
**影响版本**  
```
未知
```  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**03**  
  
**测绘语法**  
  
  
测绘语句:  
```
关注公众号，回复 深科特 获取
```  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**04**  
  
**POC**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/nvJGLMmlzsH3RSMqWXpj9vHNM2HkCFE3pSgHP0UTusovcZA8tSQTpMe7atibKw7HKGBMTejw3ztPFV4d5vEq6jw/640?wx_fmt=png&from=appmsg "")  
  
POC已放置圈子  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/nvJGLMmlzsEzkvjgiaMSVwYsrQu8shpFs8ia6lIt50QZMhX9rXbskKrcPpzAVPJwQSbRS4lq74ouNoZT3iac2icjicQ/640?wx_fmt=gif&from=appmsg "")  
  
**05**  
  
**历史漏洞**  
  
  
```
深科特 LEAN MES系统 SMTLoadingMaterial存在SQL注入漏洞-2025.05深科特 LEAN MES EquipmentTree.ashx 存在SQL注入漏洞-2025.10深科特 LEAN MES系统 MesATEApi.asmx 存在任意上传致RCE漏洞-2025.12深科特 LEAN MES系统FileSync.ashx-文件读取-2026.01深科特 LEAN MES系统WarehouseCheck.ashx SQL注入-2026.01
```  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HtBSeqUljlEX2U86CRIHg5OYkFjEichJCBOiao1DictoCzicWNibby5tkTS2mHic455icX62rECv7RrxTavz0Q4xHRZdw/640?from=appmsg "")  
  
圈子  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/3P3vXeGVfAjC9ib3Kr2ouds4E1crXD1wROicQHa8JpRHJEdxsIicN9t1fhUrsnyEEzgynlxZ3cGOdXkhGfpyAh0YQ/640?from=appmsg "")  
  
  
  
    圈子刚刚成立，专注于漏洞情报分享，不发烂大街的东西，不定时分享红队工具，欢迎加入，每日更新1-2个 0/1 Day（目前已更新100+）  
  
圈子新人优惠券已发放完，后期不定时发送，价格随人数增加而增加  
  
![](https://mmbiz.qpic.cn/mmbiz_png/nvJGLMmlzsFvvkgWGewJdZJCcnVTJDMQ136zQewU0FWFNeAqlquOvoogc5WziaJYVQXU6YJ6LtK6bO6NyanWViaw/640?wx_fmt=png&from=appmsg "")  
  
  
往期推荐  
  
[【全网首发】2025 0/1/N Day漏洞清单（超长版）](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484042&idx=1&sn=d0f6bdbd5bc1f30cd0667253c937f9b5&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 中成科信票务管理系统 SaleProduct.ashx SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484042&idx=2&sn=863b496938c2fb0ccfa366179c45c013&scene=21#wechat_redirect)  
  
  
[【40万POC？？？】小场面，看纽克如何拿捏海量POC场景](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484042&idx=3&sn=dbaa55fe300b1d232ddc712360f08ff0&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 深科特LEAN MES系统FileSync.ashx 存在文件读取漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484028&idx=1&sn=8c945921aa41873acc18a6515b554d21&scene=21#wechat_redirect)  
  
  
[漏洞情报(已验证) | 时空智友企业流程化管控系统formservice 存在 XXE漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484018&idx=1&sn=141c8cfdd99ea23c90b70ac1b4d761d2&scene=21#wechat_redirect)  
  
  
[【已复现】| 帆软export/excel sql注入](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484013&idx=1&sn=514d45521e2166d6f28f10eee4417bef&scene=21#wechat_redirect)  
  
  
[【已复现】| GeoServer 未授权XXE漏洞(CVE-2025-58360)](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247484006&idx=1&sn=4afee46de06596f891b173b27918ea41&scene=21#wechat_redirect)  
  
  
[漏洞预警（已复现）| 用友 U8 Cloud NCCloudGatewayServlet存在命令执行漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483940&idx=1&sn=c19e2a3e2ae9f433070ce965cbfd87d4&scene=21#wechat_redirect)  
  
  
[漏洞复现 | 用友 U8 Cloud 文件上传绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483895&idx=1&sn=d0bbaa35a7ea04d8a63b8c56285ca8b0&scene=21#wechat_redirect)  
  
  
[漏洞预警已复现| 0 Day 力软敏捷开发框架***********ad存在任意文件上传漏洞(非CrawlerHandler)](https://mp.weixin.qq.com/s?__biz=MzUyNzk1NjA5MQ==&mid=2247483887&idx=1&sn=a00974871b90a9d61f0867e8544f6d94&scene=21#wechat_redirect)  
  
  
  
  
