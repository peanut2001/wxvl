#  [漏洞复现]某资产管理运营系统存在SQL注入漏洞  
原创 Elon
                    Elon  好靶场   2026-03-09 02:00  
  
# 某资产管理运营系统存在SQL注入漏洞  
> 💡 好靶场   
> 团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。  
  
  
我们承诺每天至少更新1-2个新靶场。2026年冲刺1000个。  
## 1. 好靶场介绍  
  
**官网链接http://www.loveli.com.cn/**  
> 零基础入门不迷茫！   
> 专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！  
>  全场景实战全覆盖！ 聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！ 真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！  
  
### 好靶场类型  
> 新增AI靶场  
  
  
一、基础入门类 0基础训练营、通用Web漏洞（OWASP Top 10）、信息收集专项  
  
二、漏洞专项类 PHP/Java代码审计、SQL注入、XSS、文件上传、漏洞修复闭环训练  
  
三、实战场景类 SRC漏洞实战、应急响应、云安全  
  
四、竞赛与进阶类 CTF全题型、综合渗透链路、红队实战（模拟企业架构+防护对抗）  
> 🚀哈喽～ 各位宝子们👋！今日给大家分享的是某档案管理系统的SQL漏洞，攻击门槛极低，核心数据面临泄露风险，相关从业者建议立即自查修复！ 话不多说，我们直接上硬核干货，漏洞语法、POC内容、资产测绘全流程拆解，新手也能轻松上手👇  
  
## 2. 漏洞描述、版本  
> 百易云资产管理运营系统ticket.edit.php存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLGKhQr5IzVl7wecibPPHOkrGT7icpRXDv1T7rDafdE0TlMz31ibhwzEKvbW2JYsLhucpTNxk6Mhku9ibyEhko6JwETGicRHrE0NFf0/640?wx_fmt=png&from=appmsg "")  
## 3. 资产搜索语法  
> body="不要着急，点此"  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvL6nIMSpDb8sgVhib4FC1PdS8xbPnibVjjbNpOXtmA2dAVrHkuicTOAVbKjjYziaeSMk7DqaVIgZibHzqiaibKUhUS9SokfRgYcBpOEhY/640?wx_fmt=png&from=appmsg "")  
## 4. 漏洞POC  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvKMoGYVkLIaQNrclQKqC80Z9FbMrPyYeyfBcbcEAob8CZz0L73t50kjx0VMxziciaibm5oBGbbibDB8ibVicfJ0iabaqdTB2XO8qLxtxY/640?wx_fmt=png&from=appmsg "")  
## 5. 如何使用好靶场  
  
首先关注“好靶场微信公众号”然后发送bug，可以点击链接直接登录  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIgYuNO0GhbmETNNVfW8WIFew5e5hCZiaicP5rvrCjibn0AicsmSMA3bEFXNVOZ8Z2BTXNlMJoy24IlLWcXUeB4A4VSPpaDiaN4XDaY/640?wx_fmt=png&from=appmsg "")  
## 6. 福利  
  
福利1： 找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLCicFgYymsZVpugibO1C8AVsib8XicsA53jA7a050c434b35AhxXQHcdCOzjtRl9N3GpUzIsFdNXY0rh56Mll8dmpKNJIib98uZvibQ/640?wx_fmt=png&from=appmsg "")  
  
福利2： 关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvIicU6vDElyplQWIXkDdgNCmMkL9xCMOx9EsUKtNN4OhyBrAGbMo3QkpzFS5OP8ETAdLenHsJAjz3XCVrfnBSu186zyaqERbsLk/640?wx_fmt=png&from=appmsg "")  
## 7. 每日限免  
  
每日限免 为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJguqkEichc2zwjCTwfQsl8FW56dZAlNmdDAbLVarx22icu0Y6sJibk94vBBoibkNU3htXEknvAVQQCObYtlB51hatQab1ibRp13a98/640?wx_fmt=png&from=appmsg "")  
  
我们会在微信群、QQ群每天更新限免靶场，以及免费学习资料；任选一个群添加即可，所有的通知都会到位在交流群通知，请添加好友，我将邀请你加入“好靶场内部交流群”  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKvSCywPlC90S8mWg9fr8xxhWShHvJ3z1njibcmLCFHchA6Xl70fByLuek75ZgF8uUR5r8wqQJT730tcQvzD7ATHIdIibj1Yq3Io/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL62Jib8LO4pnzu27PofUnice4tk9fv57UjsK6dySBood4KOYYIyqcyzG8xdksv5hWMltXV27rSiaQBoXbQd4scwms3D2oXp5PX3A/640?wx_fmt=png&from=appmsg "")  
## 8. 好靶场AI客服机器人  
  
为方便学习还有提问，我们设计了好靶场Ai客服机器人，可以完成简单的客服能力，以及好靶场日常靶场提醒更新、根据你的询问推荐靶场  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLznbkWTbrE8J4oZUEYACsdaJCicxgiaZRhV7BJnnjmkIMQAZ84JNoiciasj1G5JNoIsbNkNQYee2K7zcQicKqnctibkGuf2Fmxp0icAE/640?wx_fmt=png&from=appmsg "")  
> “噜噜大王”正式上线  
  
  
大家点击左边的快捷工具，有一个AI助教功能，然后点开就可以和噜噜大王对话啦，由于是内测期间，仅限于年会员才可以进行使用。还需要进行微调，会随着大家的使用而进行优化。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLd65eFYnZlL8hbja3vUrogbO5yOdYoEzCXrYXdQfSzQpP3BXAib2KqVibtG8FwauFV7e77vxKnysDuygdzyPszc5wfwibBUicBEek/640?wx_fmt=png&from=appmsg "")  
  
你可以尝试问一下关于打靶场的问题  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJ8NUOXiap1gFgf1szKTva2G53B3H46fA95ecbSI8HXgyo30WwL77hWC2VlEkXCzJib3whj5FKN4QYWCyL7lRuNDqKszXSPWmg38/640?wx_fmt=png&from=appmsg "")  
## 🚀好靶场会员订阅  
  
好靶场会员订阅 首先点击会员订阅 ，然后选择对应的套餐 ，选择对应的会员去支付 ，支付完成后即可会员到账  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLicRSPx4NXENbaPVxeF2rLIuyHArtS8HOoIM8TfID3wFxo8icSQDQasMxnqU9QbjfXskbHibKgHbeVBw3nBZ21L65YekWYnt4xUA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcatqLTdbqI1MI6wP5uKCiagTMKqQOvHlrRI5nIGzOg4nzIKIwfOBruOVe7cSNK7T29SwAyUY7f0tMTuqicl4aKUBAGJKPKa3A0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJkQZQagkapGxPmA54TpyG9ic1NiaMQlhCdpKSVPMGuDZiaiaAZBHrD35MqBAb3DaOxiaDe4FZgUhFwOrDpUxrcKH6AzzS1KK3xnibVc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLqz0Ib7Km2ibLlJRMh5P4mxCyIticKBGMYVQdzCESabI8o64l24pyhHgOdoupK1EuykUMJdgNJAwJFYsnQjmNibuXVvQPp182M6o/640?wx_fmt=png&from=appmsg "")  
  
  
  
