#  记一次edu证书站小程序漏洞挖掘  
原创 zkaq-笙南
                    zkaq-笙南  掌控安全EDU   2026-03-17 04:04  
  
扫码领资料  
  
获网安教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
  
# 本文由掌控安全学院 - 笙南 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  ）**  
# 信息收集  
  
初入 src，大部分新手都会选择教育 src 去作为入门，随着网络安全的兴起，各大高校对网络安全的认知逐渐增强，核心资产基本都存在 waf 保护，也进一步增加了渗透的难度。相对薄弱的站点就比较难找了，这里聚焦 wx 小程序->服务号等 进行收集。  
  
这里发现一个校友之家的小程序，经常测试小程序的应该可以发现，这类校友小程序基本都是通用的系统，渗透难度很大。这里也是非常的幸运，这 ui 一看就是自研，出洞概率也是非常大的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIs2RdQfMEgpZnNQdibsrkEw74oPITuN0YVickS8iafe10jy6MsxsTURAlibDrQ94dzyDYHdVpxP3nicBT7A6ZoBu3h8F2GQxg12Ejc/640?wx_fmt=png&from=appmsg "")  
# 渗透过程  
  
这里我们利用 yakit 去拦截小程序的数据包，也可以使用 burp+Proxifier  
  
打开小程序发现所有的功能都需要认真成功校友后才可使用  
  
查看认证界面需要什么信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK3AkL7s0ViclNnCwibkQlTEkDqBk49sxEh4J4ljpEmpmrMdI5wPa0HRzRRXVsbMZorHkQliaXzhiaajQVDdV1NIHChXBVBF5NEYQ8/640?wx_fmt=png&from=appmsg "")  
  
这里我们利用谷歌语法进行信息收集  
  
site:xxx.edu.cn 姓名  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLYicLZckwTbQgeibicKY5TTx5RVZ4BY0G1jcj9Aw3vBib3r8SffWic5yzzlmAMTicic2JiaCsd0TshvPdwIoNd9eWLfU03QDDJMOqhljs/640?wx_fmt=png&from=appmsg "")  
  
这里将姓名填写进去其他信息任意填写尝试，选择认证信息  
  
抓包发现把用户的所有信息全部泄露出来了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJUbojBicyAibibRsPa7H9H79bNIQ3ICgGGpia51rEc19x8cKFxK6kcaichRCoRvnooq6oAMZoKeR9F85sicjuVSPfzbcicibhUK38r67M/640?wx_fmt=png&from=appmsg "")  
  
这里尝试直接替换该流量包的 xm 字段看看能不能遍历  
  
这里提示需要人工审核，前端回显该用户已经被绑定过了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIj5vcSJf8CmZoUmzZ5gbTX16ia5F67sLibMZEaGTTZpOhvvodN1dlAYBOjEBrIBKThibdt1u4mZIBia0teicvxxQI8Bpj2xcvyKiaz0/640?wx_fmt=png&from=appmsg "")  
  
那就是可以遍历了。只需要学生没有绑定该小程序即可  
  
尝试其他姓名，提示我们验证码失效了，发现短信上写的有效期是 2 分钟  
  
所以我们需要重新获取验证码这里直接将验证码包重新发包即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKaJXOJs3HsKGEvvtQqdUibMJv1m9WicQu5MickMPIYycm0Liblgic9huJpSaIY8CQkiauXVxDv64YciaqOk84zLqa2je6Y39nmcyO2Tk/640?wx_fmt=png&from=appmsg "")  
  
验证成功，只需获取用户姓名即可泄露出所有敏感信息数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKWk2saw8qekt0dyrH9fqZxdUjm0QOjZxHYTFvDWtlcgesspDdjxC1LYK8aM5nuIePUaAy3c4n5JThW2VLMBj86fV4G6iadviaKE/640?wx_fmt=png&from=appmsg "")  
  
  
  
