#  这类漏洞危害有点低，SRC 好像不收录！  
原创 xazlsec
                    xazlsec  信安之路   2026-03-18 02:31  
  
今天分享一个被大家忽略的漏洞，地图 API 的 key 泄露问题，目前还有大量网站存在该风险，不过由于危害不足没有得到重视，在此之前，看看今天有哪些 SRC 有活动：  
  
![image-20260318102327549](https://mmbiz.qpic.cn/mmbiz_png/VnwOz8XYCTYaSZpokics60UxM3HAzSWicyyQZxUQJSOaIoPiaoTzlyvMicR731lLVcq62JSCZPDPCYRGSV2f6Z5sibIwE3XaPpaNNLqZP6KibyWW4/640?wx_fmt=png&from=appmsg "")  
  
系统调用地图 key 是付费的，但是价格好像也不高，如果 key 泄露，可以被他人调用刷取额度，导致资金损失，但是成本好像不太高，危害不太够，国内三大地图企业 API 格式及价位。  
## 高德地图  
  
![null](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTYG6qQzkrxDAG5AM2NRrv5QSjA2y9rZ7gzW8WI7ClVNCsOIWS2UOiawgicy8Y48yBPJBQN82asmN0gC5lykcBqlRbIsWD2g6XboY/640?wx_fmt=png&from=appmsg "")  
  
一万次调用 30 块，被盗刷的危害也就是经济损失。案例：  
  
![null](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTY0Bib10j0ujdqVALia34r6nzia7VCHSRNBTwVOL8MBk1x7BKsOwbBsaoibsBO1PVOLW6ciajrXYibsQKhEZibJp8KaVR4ibLqQRZKwf8o/640?wx_fmt=png&from=appmsg "")  
### 高德 webapi  
  
```
https://restapi.amap.com/v3/direction/walking?origin=116.434307,39.90909&destination=116.434446,39.90816&key=这里写key
```  
  
### 高德 jsapi  
```
https://restapi.amap.com/v3/geocode/regeo?key=这里写key&s=rsv3&location=116.434446,39.90816&callback=jsonp_258885_&platform=JS
```  
### 高德小程序定位  
```
https://restapi.amap.com/v3/geocode/regeo?key=这里写key&location=117.19674%2C39.14784&extensions=all&s=rsx&platform=WXJS&appname=c589cf63f592ac13bcab35f8cd18f495&sdkversion=1.2.0&logversion=2.0
```  
## 百度地图  
  
![null](https://mmbiz.qpic.cn/mmbiz_png/VnwOz8XYCTYEM8PKeDmKUz7UFd7wOh4LnMgRCFurz71LEzMBKicfaXArFySqx0bNsdAaHmJqGzULsqS52ic1EDlwja8Q0n18QfEaPovEXr8Iw/640?wx_fmt=png&from=appmsg "")  
  
按年付费，如果被盗刷的危害，每日额度别消耗完后，服务提供不可用。案例;  
  
![null](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTZmwzZj8nEF3FknO7XCYfLPPZub0FE4MX3J1xS1OfeH9KFbuuf55Wiaib7sFa3EQnIsXGywDsmZqMGibQvTLicVmibAm2pnP8mPic8AU/640?wx_fmt=png&from=appmsg "")  
### 百度 webapi  
```
https://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=这里写key
```  
### 百度 webapi IOS 版  
```
https://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=这里写key=iPhone7%2C2&mcode=com.didapinche.taxi&os=12.5.6
```  
## 腾讯地图  
  
![null](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTZWQu1TmibwGEozBOjEj96icrfcfblERsvkVVA4dg8Fccdj0jb1UOyia3kUiaAVbOcCc8AtLg6uvHdlz3x0wRgbWgD1sIxJ3ITRjIc/640?wx_fmt=png&from=appmsg "")  
  
固定配额，被盗刷的危害，每日额度别消耗完后，服务提供不可用。案例：  
  
![null](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTacK2FrzQwTiaF9ic6LX2ba4FgN69ibj2m5vNIu5OUFSSibpqUOHEMBVFrLjYxTJRPEwy4WCCIfjzW74iagMw4iawBficbsVr3GDOfFAU/640?wx_fmt=png&from=appmsg "")  
### 腾讯 webapi  
```
https://apis.map.qq.com/ws/place/v1/search?keyword=酒店&boundary=nearby(39.908491,116.374328,1000)&key=这里写key
```  
  
SRC 监控平台，发现大量网站存在地图 API key 泄露的情况：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VnwOz8XYCTZLL699ibj1iaSQicdKSNdOS2WWyn73gT0uzibslGoky3gBibJDwuzuHeKFfOOcbwVPZCPzDkPac3kezCfJCiboSAvYZvzaicXq1Qzwf0/640?wx_fmt=png&from=appmsg "")  
  
由于危害不足，没有引起大家的注意，各大 SRC 可能不收录相关风险，你是否交过类似漏洞，是否被收录，欢迎留言！  
  
最后欢迎注册体验：  
> 平台地址：  
http://src.xazlsec.com  
（注册码：XAZLSEC）  
  
  
如果你想体验一下非 10 积分的 SRC 项目，可以选择小积分充值，10 积分等于 10 元，联系我即可，新加入知识星球、新续费知识星球以及当前知识星球有效期内的同学，可以联系我获得 100 积分赠与。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VnwOz8XYCTYCLG3nbQGj1PzcHTtGjMtGo3dibibDzKxxWTicH9x3F1oz7TJO7GDmIp9Zr0uoZZLf1MmLXmlWRiaGFhF3Yom896b6aO5eueXjVm4/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
  
  
  
  
  
  
  
