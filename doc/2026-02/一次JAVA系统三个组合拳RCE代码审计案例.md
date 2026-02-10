#  一次JAVA系统三个组合拳RCE代码审计案例  
原创 学员投稿
                    学员投稿  进击安全   2026-02-10 02:01  
  
**免责申明**  
  
本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。  
## 一、前言  
  
跟着小朋友师傅学习了一段时间代码审计，来验证一下成果，也把自己成果审计到的一个组合拳RCE漏洞分享给师傅们，希望师傅们不要嫌弃。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQl7vzicfEhe5hiaBzRg7W1fMDGGKmwqT6b9YBmIV0GjyiaWhfk5KTveWmZ4JTiclPx4o8JHVw9v3DnxdKCwic33qtrGtibVkDLianGHg/640?wx_fmt=png&from=appmsg "")  
  
针对上述系统进行代码审计，当然源码是通过py得到的。  
## 二、框架识别  
  
小朋友老师说过，在做审计之前先清楚对方系统框架是一个什么框架，这里进行查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRDJcfM90q9oVfccthyFeBZcNoy141XrcmpYLHcNCVpeErbrJC3vO4HY0DdIE7OFI86R6HYnaiaQticCwycntkOUf4IqA58DXp5E/640?wx_fmt=png&from=appmsg "")  
  
使用到的是Spring-MVC框架方式进行开发的，并且配置信息位于spring-servlet.xml文件当中，这个框架的中间件一般配置为Tomcat，并且tomcat下如果权限认证错误是存在一定的权限绕过风险的（小朋友说的）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRJ5arkSHz3csicJuCbDEwsOJBWs2ryuzRGplqvl0KeTxVTCIzI9j4PVjCia1X2PX9g5lX2dRXdHibXIMycbnBHFl2SwBx2rhdPt8/640?wx_fmt=png&from=appmsg "")  
  
并且在这里进行查看对应的class文件，确定为SPring-mvc开发方式。  
## 三、鉴权绕过  
  
刚才我们分析到了对应的springmvc架构，查看配置文件，主要是进行查看权限是如何进行校验的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTWXSncxz65RHFYhGoX1sNtKehpvqSFhWrcWUicgtEUahtibj6pIvFNXWhcCT8fBHVjotd4sHVwhnnXF9oWqfxt2Uuu4D1hWTF9A/640?wx_fmt=png&from=appmsg "")  
  
在这里可以看到权限校验是通过一个类AuthInterceptor类来进行验证，跟入这个类进行查看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dfrm5V3o6kTXOogqqia20xX6eGoZRoGicwZ8SIKfDHYwo4og2Acj0MKFsv8PqemOwf7wtASEpfBWY6j5qowSbalnMs9H7pTRrhMvGWWzibR6es/640?wx_fmt=jpeg&from=appmsg "")  
  
相关代码如下，其中我们着重观看下面的代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTeBCqLJaOB8bcqpuaZqZPWdIWoB7uepN4vcMeHyFJcs8WrjhiaYuWD5hjwQqVHMWPbV9LPBefdThsVH02hkDDibPR69K8qvJYU4/640?wx_fmt=png&from=appmsg "")  
  
在这里获取URL的方式存在错误，配合Tocmat中间价存在绕过风险，同时继续往下看。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQAN1qUfenEEyZE8p7QUfryenwJ1QLU8SkJ1fe3ESoa5c4aEDOxor1Y4hOvZoxo6pR0fzHFkco5qzbobahknKbdSAicYSCVWwus/640?wx_fmt=png&from=appmsg "")  
  
这里进行判断我们的URL是否包含uploadFileApp并且请求是否走的是上传数据包，这里我们不是，继续往下走代码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTRutBB5RyD890oPhh2iayaMial7hL7Snz0VoAQiaXOmN2GESVfPlBjC53L9cGun6kwlpoZmtBW8Ee1dlmMsOAzmETTvX1HZ2lx18/640?wx_fmt=png&from=appmsg "")  
  
然后进行判断，是否包含actionCloudModifyFile以及actionCloudAddFile这两个路径，  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTOlLbhLfjKFhEfgTzvLbibQsRIdiaFbPezZfa672zm0V8WicPlyFE36x7mY7vL5OIrDOoZM0wrGPnUdZgWMwLejLNYaGibbLpE8hg/640?wx_fmt=png&from=appmsg "")  
  
这里同样是进行判断是否为上传请求，这两个路径的上传请求，继续往下看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSq4kXsDHsfWmmoh1XHhLyQ602eb1z2ec9qlGMk0NcibhzuzCxx1EyEIt22ojJbHOYVGfIODicNFUPmkAhIRr13iciaDvKib8ficV0to/640?wx_fmt=png&from=appmsg "")  
  
这里是重点，可以看到首先获取我们的session，我们模拟攻击视角肯定是没有session的，于是我们的u肯定为null，在下main进行判断我们的网址是否包含在属性opens当中，如果我们的URL是其中的某一类那么久进行返回true，这里我们查看opens属性的信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTBO57YW766O1VUt3Lym44ONVJubvR26dUbAYK4ibwJlZVPf1S4JcxBKuNVZ7ecMw5ZJ1OgKwt5pia8pKAqVl6KV444LTTibFaP1A/640?wx_fmt=png&from=appmsg "")  
  
那么这里我们就可以理解了，我们这里可以进行尝试绕过了，首先我们包含opens当中的信息的时候不进行鉴权，但是代码当中获取URL的方式有误，并且配合Tomcat导致出现解析问题，导致存在鉴权绕过。  
## 四、文件上传  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kR2osZh7WtPKSA93FD3YFxS2qH9UdaoJiblvTKm9r7K0hszBicfMnbagPyViaibDqajFpugtMm3Df8hXlibdyEktLvAj2ysuZDqnHeI/640?wx_fmt=png&from=appmsg "")  
  
这里可以看到目标是解析JSP文件的，于是直接进行尝试定位文件上传漏洞，搜索几个常见的文件上传关键词。  
  
```
*.getOriginalFilename();
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRicUopP0KuF9y4I7dnADWUaUOra62sia98vYDicKF2AS7Tu37O6kibiclkqIWwz69QuiaJ3TYzt1oDOFC5DZZISqpj6jocHkUVYSxn0/640?wx_fmt=png&from=appmsg "")  
  
最终在这里成功定位到了漏洞。  
  
获取到文件名之后直接进行重命名保存，并未进行过滤，并且这里的路径为actionDetailTmpFile，并非拦截器当中判断的uploadFileApp、actionCloudModifyFile、actionCloudAddFile这三个路径，导致可以进行上传。  
  
但是还要注意原由参数pa_id\text\position这几个参数。  
## 五、漏洞验证  
  
构造数据包成功上传相关文件，但是发现并为进行返回信息，重新回去查看代码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSEDaickVs805rJSbDT4ta8AnYd5QwLJ3iahibzSia2xLeIUqcjW4OoQiabcMmEE5ko31SJ0UygfTDlrrlwsZJ6EnoK6afyBibBEmKAk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSCaziaJMdb7Q3GbN0QfKhyIZXrd9aiankoSqbJ31eVm44HMtjwMAYklgwgGbXO744rccCowdUCdYOzCkAXCJJ5CEias59INvHsvc/640?wx_fmt=png&from=appmsg "")  
  
确实在进行上传成功之后返回数字0。  
  
但是在下面还有一个接口。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSTP4VeffVMtrD2iaGTKBhKCwCmjXITFRFaiaLbfmhib9FQvu71o3Sv3QrRz1MDh9ngxgibsAEx0XI9bQdFxCbnjLJLIhFqFtfyiaOI/640?wx_fmt=png&from=appmsg "")  
  
这里进行传递参数pa_id参数，同时进行调用方法listPhotoAdsDetailTmp方法。  
  
查看刚才的上传代码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQ4vbd5ciaOKpAXRicl0nTsY1pBiaexFjIYKJy0cnP1GWFnuiaTPkBUZEQOLoB0bDITgMw2o7BtxqE0Qk5xKHiaMVqr9OYCEibX8zzsY/640?wx_fmt=png&from=appmsg "")  
  
发现上传成功之后会进行调用add方法，传递tmp信息，然而tmp信息当中是包含filename的，filename则为我们上传之后服务器重命名的参数，跟入add方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQpt8OvjrOnvaic2EQLLe3KLzs50WDTBickEzZsuibLwVDSZ7d0FRlDY6EVjXrickb8yPqD6CFkh7kLF6OO8MtAYQyxs5FlW4Y5ic54/640?wx_fmt=png&from=appmsg "")  
  
最终发现add方法保存在了表tb_photo_ads_detail_tmp当中。  
  
然而在看我们刚才的方法。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTfveBqNs6yOHDEBODfl1jdPbQnR97WecGyMbZ18boOXac1GdXDia41l7mkIxLRvgLkT4SHUeOj48L11sAgLOWCib1blKjM1c2UA/640?wx_fmt=png&from=appmsg "")  
  
通过传递进去pad_id可以知道。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTuW21XyfcT1wxWObRvO1EoBicPGSj5X9Wzs2DiaagsHD3QpBYpf5vo31vQTc355EOEaiaUTEJtZbxT0T0WVkylicE6mJ8y626ObfI/640?wx_fmt=png&from=appmsg "")  
  
查询了表tb_photo_ads_detail_tmp，并且该方法最后返回了查询信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTYsOaIvgXq3TcmkGZlg4fpVajFoLNyNow4EadROZjFtYmdWEo93sbEheCdBV6ag5yXIvgibV7yM9n4uDnsl93yhibqhLRlA8IUM/640?wx_fmt=png&from=appmsg "")  
  
那么我们就可以得到相关重命名之后的文件名称，尝试获取刚才上传的文件名称。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSykxmicbxyqK0ULB98zFVrCu3gtt9mPoWvhtDbOTXdMzePBCH4cOW9xJUu2QC3QMJzicVWHb1EicX4gEIbDCM2aWuiaOkssf1Igro/640?wx_fmt=png&from=appmsg "")  
  
成功获取文件名称。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQ8yibcAlr0sSfe2SqOYxhkHIOxwqS6Q0RpaQKiaGrv2I96yajUfRCfNMgQtulHXEtIjSWEy3w949JFN5whaCch8edCvibfmqGS4A/640?wx_fmt=png&from=appmsg "")  
  
上传到了这个目录，拼接这个目录后跟入获取到的文件名称。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQ0R3MgrOuhgFpslicWvT46HtPIpwlibOYvAo5m5QN8j0v7f206Hgg8kYGVfpicAxgYsG2cjXh0Be7oY98LVvTyC3dWZeKOBwbuok/640?wx_fmt=png&from=appmsg "")  
  
成功解析。  
  
**广告区域**  
  
  
    目前第四期进阶课程已经开始，课表如下：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kR4WSWlTrzCOicUqUVLmGxO3riagLkM3cEYQpAQOnJYNXy1IFo7V9Cv3ibdF2RoARPP4QO5qcUPoxzkZfZXFh4YPQkVQdN34EkxEk/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16 "")  
  
同时报名第四期基础课程同样可看，课表如下：  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSWZ3icTsw3jdaDAuQpMfb7WxkWa9fNp08KmXLek1FYWKg35UBibONVBeOpeELduwmicicRoSSib5S3TFqe118TOUzEdAogveerUXx0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
  
同时具备内部资料以及靶场相关福利，想要了解的师傅可以冲了。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRIsJq8Wgv6Sy1pB23yO3ubOSQmI5opvLM0vkuDdQuT0eRn8mpuSvzvSYC5a3kPhXINbH3puAsS34KO276R9BgyqJTicR9kP6c4/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRxMwlmtJ10f8vdrIeiaeJdwickqEGNiaVwBo61pQdzPmUGPkZtGrn02FagVhLgALkTXeYEGIrGKWeicqLjAfuVmaKLQ5icnMUSBGHE/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23 "")  
  
