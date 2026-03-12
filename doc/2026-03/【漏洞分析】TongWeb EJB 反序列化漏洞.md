#  【漏洞分析】TongWeb EJB 反序列化漏洞  
原创 yinsel
                    yinsel  红细胞安全实验室   2026-03-12 03:37  
  
2025 年 11 月 13 日爆出的漏洞，手上有环境和源码，并且朋友第一时间透露了利用链的信息，于是便尝试复现并分析，记录下来。  
## 漏洞原理  
  
TongWeb   
ejb  
 服务没有校验请求的数据，直接对来源的数据进行反序列化，而默认情况下，  
http  
 服务（8088 端口）   
/ejbserver/ejb  
 接口会转发至   
ejb  
 服务（5100 端口）的相同接口，攻击者可发送特定的数据包，造成反序列化漏洞，其中可利用的反序列化链主要有：  
```
```  
## 影响版本  
```
```  
## 前提条件  
1. TongWeb   
http-8088  
 服务可访问  
  
1. 未做安全加固，  
/ejbserver/ejb  
 接口可访问  
  
## 漏洞复现  
### 7.0.4.2  
  
判断反序列化点是否存在：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlZJqB4eoact4HJvk5TkOqSuGvB3MV5hh3NhwreibcaHicunXrs11rVDDKjFWQHlI205V71UV6Hz6esfIfgcA8IcYsbbbx8nBibkM/640?wx_fmt=png&from=appmsg "")  
  
睡眠成功，确认反序列化点存在：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnpDrDkLNa0515icU9UP5BNSmZN0QZ3CxIfrBL5HibkUBwfsMmm87w3Hh2bbpQU0qIoMrva8gvccmJWESsMDwYS98ZKFZuWa6AfU/640?wx_fmt=png&from=appmsg "")  
  
利用第一条链注入内存马，配合   
MemshellParty  
:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkkleUl4coJYypbjoxwQCE0J66oulic2giatkr9MtOtrFPZQxK2PvzUnxrFdPeF9XBqrhJHsBWmNr9tz7uZfpXpXfrKmI8T0Nd0U/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XktAToROeubprI84Pa3TkQiatXFTnuLoYrNxJWEpmYWkd98wLrw4DicOB5QWUtJDvxpjibmfNWv7znQx0NoxrjbibyHLiaxfpssuFeY/640?wx_fmt=png&from=appmsg "")  
### 7.0.4.9  
  
判断反序列化点是否存在：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnWMBGC80jnB79PDic0ic3QZyHLj8ib6YIhJKVpxdMJYFcQquXdBlpJbgjOQDvGHtcqFqyE55hH9FX0ibfXGHPrkjia5sLKduUP8N4s/640?wx_fmt=png&from=appmsg "")  
  
睡眠成功，确认反序列化点存在：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmPNwBzrqjiccKH4jED8Csz2CR6pDlItyc6mhm6TZNe7iaMYnriaYGfLnoCZPzUs8hfXSzRb1cxlBbicjMcANic60IUSKFbeTDAw3qc/640?wx_fmt=png&from=appmsg "")  
  
利用第二条链注入内存马，配合   
MemshellParty  
:  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XldLZ4NkzHDZT5kViaexMGbc9dwicgkqmq5Jo7byic8uVvG0KdLXDE9Na2EdBlSeTjVVqY51GaRh1TP8THNXhbzzJsadYp5mLnRlE/640?wx_fmt=png&from=appmsg "")  
## 漏洞分析  
### 7.0.4.2  
#### 定位接口类  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnDDKbzL0BzH6MxUcyicS0Z4c8ZPYvCQGTgiczsPHD6Qibp3OSmctQbzAOVqyRT8kEZJ9f5RPEL6icicytdYP6Wv4OvJGFKor7kJ1J8/640?wx_fmt=png&from=appmsg "")  
#### 对应的入口类应该在：com.tongweb.tongejb.server.httpd.ServerServlet  
#### 寻找入口点  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XleL24qb2S6u1qnnUZuYKpQyEtsfWNwwvic1t84GChv9pTlTpprxpYNYJe7L8SYRYqwwictPBG0l32CxRs6VPfPmw1nMEffaPPag/640?wx_fmt=png&from=appmsg "")  
  
进入  
   
com.tongweb.tongejb.server.ejbd.EJBServer.service()  
 方法：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xl0LWx5vHamIicF4hMhblzjzezxh48kS9URqicla2Hd6pM5yTFqWibdG1yuW4UicibficpxWBOlLWqicYm7LnTDL4FxWAw052rn2geyEw/640?wx_fmt=png&from=appmsg "")  
  
进入  
   
com.tongweb.tongejb.server.ejbd.EjbDaemon.service()  
 方法：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkaQdviaJU9P10m1WGJByZTJBLnnrsCVyuRWS76LNDA0mr81zACl5zd7uTxXyaXL9H1mxIvwqPqzV6j6Q6pfr8Qva2feibfo9JeE/640?wx_fmt=png&from=appmsg "")  
  
先分析一下两种协议头解析的逻辑：  
  
客户端协议类：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xm7vvSuzAEaM8jWpl4KBXPCKoarricDQ7fwBaYic6oaLicdDWSfJzsiccnYAIYecibHJTVr4jSicRiaz1X6jR1qU87XOg1wqV2f21ysZk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnNb9hdPSmZFsHTfkNNibhczbr2VG8wHKHJplgYh2kMdNa8vqfJharKg8oJDdAltZrB6jzLGbvl1uD0tKswcRwkwOuD4TGtiaWrk/640?wx_fmt=png&from=appmsg "")  
  
服务端协议类：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xm44y8IErEwvB64ibGJQdKeYQmDuIxjpwy4G1P0slic7D4ToJeR4q5lGnouoL9624LvI93YCCNVicVOteib7BGyzdX9jL4exgmObbQ/640?wx_fmt=png&from=appmsg "")  
#### 入口点一  
  
其中   
readExternal、writeExternal  
 为自定义实现的反序列化方法和序列化方法，用于业务需求的灵活序列化传输，存在一个入口点：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XncrtjsgeP3PL1JfbbeBVmibicRqTetItBlgWicwTkEQBNnYcDfC7dUngnU4NgzF52bfjBpB933euIlnwaahTxBv6mlbGoHk2AVJE/640?wx_fmt=png&from=appmsg "")  
#### 构造序列化数据  
  
经过分析，存在一个反序列化入口点，并且根据代码中解析协议的顺序，构造合适的客户端协议头：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmrqaiaR7ST8kh47lhLR3J6pSYUuboHVziauEQtYX9EsxjAAI6zx6uclf6A6oUlnVLn08ur1Q7x4jQjaJJickE3zM4FjmvoPicx4l4/640?wx_fmt=png&from=appmsg "")  
  
代码实现：  
```
```  
  
可参考   
javachains  
 的   
sleep  
 探测反序列化点：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmKbObtHW7ic3eyQiboDnva4p2yeOIlHmtjgEddziabMZJD10BYBkVf5MjkjXrFVjbicibVvPOF1uWfWZwibd0enVkpTbToIvRyf5Q4o/640?wx_fmt=png&from=appmsg "")  
  
最终代码如下：  
```
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmEbmqa3vr3UQfjnt7l41U6S90jxELlwOMpHMYQ1J1jKwJuXEe5HEnJRo2wQRQpQJUcOX7BtGl8oz43WI6aCc3eibwrzZFfDv2Y/640?wx_fmt=png&from=appmsg "")  
#### 入口点二  
  
在代码中下方还有一个反序列化入口点，如图所示：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnLppv6oGfqUgicEbiae5jAsRmAHGvVb8Gq2yfibKojJWTe0ka5OvzkAJaZweDnRoc3Z3tEThZsHqDvcwRID41JOfCzgNB90eiaBlo/640?wx_fmt=png&from=appmsg "")  
  
进入   
com.tongweb.tongejb.server.ejbd.EjbDaemon.processEjbRequest()  
 方法：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkmtzEOs0s0BzwNVLReGm5ghK5G1aibAuG9fWgAoMTC0HdUMvQ6dWxiaZp2hvkubW1TZJ1gniazCpn8empCQY4JTk8J0xdSZlib0jQ/640?wx_fmt=png&from=appmsg "")  
  
进入   
com.tongweb.tongejb.server.ejbd.EjbRequestHandler.processRequest()  
 方法：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlD9UE56StouWsXAeHVRqN6Tp0icWnF685WsPhfs0lhjWvzbNMD6JjWXLfWukrcibsGnFecbVQpWiaUib7vLGdn4ppVxRhOIiasnMlY/640?wx_fmt=png&from=appmsg "")  
  
进入   
com.tongweb.tongejb.client.EJBRequest.readExternal()  
 方法，到了最终的第二个反序列化入口   
this.deploymentId = (String)in.readObject();  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkVFqatUaK8njC5ibWcWBicoFMNPzAkyTT6CodzUg8ktibfuUjlBjnP34yVyRoA2QOzicMEr5ibcx8Rdt6LUql5ib1zAW0juO4PIpzDg/640?wx_fmt=png&from=appmsg "")  
  
在来到这里之前，需要满足一定的条件：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkT87HtGZkI0Q8cXS0PSS6Dz6GlicPV1bLxk7gI8ATFVkSicdo608M04Dtxv2Ju3BuWvuBUHkcPrC822Wjiceia8uaTjBzdB1Mr1aI/640?wx_fmt=png&from=appmsg "")  
  
因此在   
payload  
 构造时，需要再加一个额外的字节，并且其值不为对应的枚举值：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmYXpiaNoSn08VDrGOvXJowoEQElr5K3c7dB0Grqqacs3MtmUngCeFJicxiavIPKDaA9WppDxb5SXczUoPfVtn0etEMmrgOkiaDeFw/640?wx_fmt=png&from=appmsg "")  
  
排除两个值即可：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnsdsoxrDunFxZCx4n5VibNIjhGmXiahImwZ34lictzpicmxU4AmCSrbs5pgX213ubDiclskWMdp7bpPSvFQgh0FRTsMwfhJ6tmDN9w/640?wx_fmt=png&from=appmsg "")  
  
接着往下看，又读取了一个字节作为   
requestType  
，根据上图的枚举值，其值必须为   
0  
 (byte)：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkbdGR8TnYgXYJFVDSjvjWw6nopic0yqXI8ZicOJL4fPMywtD4jFiaF4ggexMGduHCwQZ95rnlm8jLlTnvMV9QaPU8PU1o3X76CRw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlMfUuicnjtOwRiaPtOia4giaDIftNp2EuFrHF1OOicGFpN0YuWOibPoWZPic3TAnOGHJcGHuN2jibWiaEF33ciaPI7OtXw2SUoMfFambTibU/640?wx_fmt=png&from=appmsg "")  
  
根据上文的简单分析，最终来到   
com.tongweb.tongejb.client.EJBRequest.readExternal()  
，再次读取一个字节作为   
RequestMethodCode  
，并且仅需满足为合法的   
RequestMethodCode  
：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmJsw8ficggKCnBQMib5iclTia61dZZWOJsKCswMO6vQ40V0bvMvCvwQBURc9axpd7O0jAkur7GIe1gWuJNJD4Y3I7AmDsmFI7rVwE/640?wx_fmt=png&from=appmsg "")  
  
任选其一即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XllzNTr2EDZDSYfcQXjWEz8oJGO3BR99gibvMUoOiaZ70J5ibpKa55FkPlTSqW7F9wjz3rzticm9Epw3twxQBHuImBtXBF618Hj1Bs/640?wx_fmt=png&from=appmsg "")  
  
那么最终的   
payload  
 为下图所示，满足条件即可触发反序列化：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlwE5ibxMiaHiaMlAtIGIr7DfGXXn0ZlMoqibgGXc6AXtTdgXd2o9Bibj4fWNicRuicGew3ERzM5VGQySia00d6V39HRxv1IibicIQnP75v0/640?wx_fmt=png&from=appmsg "")  
  
构造序列化数据  
  
最终代码如下：  
```
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlX31AZ2e29xAxBiaGIiaicic1aZ5XGYibIGe464TsSlNgDyLRLfl9UAzUsH3BPdzuanTTxsG4rV4ia1cB7Rb2XnuR8sfapW5KYegaH0/640?wx_fmt=png&from=appmsg "")  
### 7.0.4.9  
  
与   
7.0.4.2  
 相比，不同的是   
payload  
 的构造以及入口点部分差异，有以下几个不同点：  
  
首先第一点，客户端协议解析方法被置空，因此不再需要开头的 8 字节：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmLqEVYCvjsyKD5c8u6RnPnGwU8hX5oibfs5xjjSB35iaujlAianITSKowTdsC0JgJA7uyAqLLAly9iazmkrGHv1rTUibQaoEqGicW6Q/640?wx_fmt=png&from=appmsg "")  
  
第二点，在   
com.tongweb.tongejb.client.ServerMetaData.readExternal()  
 方法中，入口点在   
(URI[])KryoUtil.readFromByteArrayBySize(datasize, in, classLoader, false);  
 中：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XksTBKL9fJZUrsWkEEn6w8LnB88YviaRZXhZSODNNA4wqJWjKvrH8uklpEXApVs2bPTE1RnVh01KzYz5LU5mk2cS5oibKHpoDONI/640?wx_fmt=png&from=appmsg "")  
  
本质上是一个序列化的工具类，也实现了类的序列化与反序列化，等同于   
readObject()  
：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XlwPmJRKsQM1f8ibiagRCzBaS3EZDbmHcc4zux76ecwIx9jtrhVOPfiakrLMUvI0VmzGAPnQzYpjsBq7ferD7BQQMpyFXKScUeYUg/640?wx_fmt=png&from=appmsg "")  
  
只不过需要按照该类的格式调用对应的方法进行序列化   
KryoUtil.writeToByteArray()  
：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkwbFEnjmcXCyEW7uqex9dRtUPtZCLJ82Fbk6E2d3Jopia14kiaRx8biaD0AVHgUkeLibPPe4QY7ODNMEdYiclwTJ80dvSibNmAYCdM8/640?wx_fmt=png&from=appmsg "")  
  
第三点，在   
com.tongweb.tongejb.client.EJBRequest.readExternal()  
 方法中，入口点也有细微差别，需要添加额外的字节：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmHpaKgE4xBUMDZM75GVjZCR3wd1KkaGyWlZ0RdZawXAVzOyhhNBmnlvPDEC4oRKz3qfjtsJ87ytZ20ByfJDOLa7iaHILLN0vbM/640?wx_fmt=png&from=appmsg "")  
  
那么整体就有两个序列化入口点，有了前一个版本的分析经验，那么对于   
7.0.4.9  
 就根据其逻辑的读取顺序写入相应的类型数据即可。  
#### 入口点一  
  
代码如下：  
```
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnCAG4O4Y0iaFY1YI9wHL4Fic1P4tmyk3JE65ggrAsqia4wt8mpG7nwUkcm69Clr5O7un3Sa4Ckkbo9jfEicHs1VLdjT2zjgpibU9pU/640?wx_fmt=png&from=appmsg "")  
#### 入口点二  
```
```  
### 利用链  
```
```  
  
参考   
javachains  
 中的代码即可，不同点是    
Xbean  
 依赖经过   
TongWeb  
 二次开发，需要更换部分包名，其他基本一致。  
## 武器化  
  
利用大佬们开发的   
javachains  
 编写对应的插件，将分析过程中代码集成至插件即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XntXfWiaDmJUsIib9gJ2PZeG94094MvD7tt5GhU6854LicNM6TO6B9W66a5drX4S2iaqcQveyKd4YKCZ1nqOoiaTKPo7eAu1l6yYFr8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkJCAqgG5vS1PslVqFWNHOC0ibwKpbky8DrAac644kLG6KlMEqswrwSySCibgIFCGyYlgrUuIFtibd8AulXVUBuYrdnfrLEpgNhEg/640?wx_fmt=png&from=appmsg "")  
## 常见问题  
### JDK 版本  
  
目标 JDK 版本为 11 及以上时，可能会出现：  
```
```  
  
需要使用   
Javassist  
 修改   
serialVersionUID  
。  
### 高版本利用链  
  
高版本下只能使用 JDK 原生链，其中   
EventListenerListToString  
 不可用，其序列化流程有所变更，  
EventListenerList  
 无法被其正常处理：  
```
```  
  
因此在   
7.0.4.9  
 高版本目前只能使用另一条原生链。  
## 总结  
  
整体的过程其实并不难，只不过需要一些的   
Java  
 基础以及熟悉   
Java  
 反序列化链的生成和利用，多实战多积累经验，持续学习。  
## 参考链接  
  
[https://mp.weixin.qq.com/s/9zxYCHVrnE3rlvNo9vnqkg](https://mp.weixin.qq.com/s?__biz=Mzk0ODM3NTU5MA==&mid=2247495244&idx=1&sn=61383c41881877e96af51951020e76c3&scene=21#wechat_redirect)  
  
  
[https://mp.weixin.qq.com/s/SThL617Eo5EVLrf5hu7dmw](https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247492984&idx=1&sn=427515004ded06320d11eb8ca7d04914&scene=21#wechat_redirect)  
  
  
https://github.com/vulhub/java-chains  
  
https://github.com/ReaJason/MemShellParty  
  
