#  0day代码审计：某知名OA SQL注入  
原创 团队内部成员供稿
                    团队内部成员供稿  凌曦安全   2026-02-06 02:01  
  
本推文提供的信息、技术和方法仅用于教育目的。文中讨论的所有案例和技术均旨在帮助读者更好地理解相关安全问题，并采取适当的防护措施来保护自身系统免受攻击。  
  
严禁将本文中的任何信息用于非法目的或对任何未经许可的系统进行测试。未经授权尝试访问计算机系统或数据是违法行为，可能会导致法律后果。  
  
作者不对因阅读本文后采取的任何行动所造成的任何形式的损害负责，包括但不限于直接、间接、特殊、附带或后果性的损害。用户应自行承担使用这些信息的风险。我们鼓励所有读者遵守法律法规，负责任地使用技术知识，共同维护网络空间的安全与和谐。  
  
本文  
来自凌曦安全团队成员-juzi供稿  
## 一期课程&&新版课程介绍（链接直达）：Zer0 sec 正式更名为 凌曦安全！新的一年，新的课程，元旦特惠来啦~  
## 声明：  
  
厂商已公布补丁：  
https://security.yonyou.com/#/noticeInfo?id=756  
## 1.漏洞方法确认  
### 思路  
  
U8C是典型MVC所以我们先去找controller层，从controller层定位source点然后source一路跟到sink点即可。  
### source点  
#### PaperQueryAction.save  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQNYvezB2xtdw8qRIoIqXx9KnAJOko5lr11ScG2mK2KC7qGfPpAIc2fnOdNqKGxbuMjcQFIF0YL7VB4GX9bxtaSBp32wTk8wV4/640?wx_fmt=png&from=appmsg "null")  
  
这里sava方法接受一个PaperExecuteVO类型数组的参数传入到PaperBP().queryResult里面，根据这个方法的名字其实已经能猜到就很可能是有问题的。  
#### PaperBP.queryResult  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBTPEnAPCxIxIc46DoVicRfNdppnFolKtn3dbROjaJqfu2dCQ40ETQBibibQbnowvf1yfD25ibrNAibDXeup44UzZozpF90ZlZoDtntY/640?wx_fmt=png&from=appmsg "null")  
  
这边会传入到PaperResultDMO().query  
#### PaperResultDMO().query  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQdLRIT04yosDNVLVddSGRMgtuicu5fCSaOV2iagicHgfChjajcNAfPdndUdOaoH2evyPN8EAFLOMHMZsR6nZhKjO0CBHg4ft9C0U/640?wx_fmt=png&from=appmsg "null")  
  
此处接受两个传参pk_paper  
和pk_questiongroup  
然后直接拼接传到queryVOByWhere  
根据分析发现没有什么过滤，很明确的存在sql注入。  
## 2.路由分析  
  
漏洞方法确定了那么就要知道怎么调用，完整的路由怎么访问。  
  
因为漏洞方法是PaperQueryAction  
，那么就要去找doAction  
。  
  
它本身没有声明的话就去看父类  
  
一直跟就能跟到AbstractBatchSaveAction  
### AbstractBatchSaveAction  
```
public abstract class AbstractBatchSaveAction<E>
implements IAction,
IActionExcel,
IChgToJson<E> {
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTgk07EdvicWUa8G6U4yJwU9cIEhnwokV1VibwQJGX0iaDbdnVerviab9frKJW28FH51fsOYZG2MVPJKUCLUKO8pKAibOAXqdb4bZzA/640?wx_fmt=png&from=appmsg "null")  
  
这里直接去看调用方法最方便  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRbxXIgYFprlwn4O5WxDnvBfuKKsovkp1k3KB3dQC9mwbUzEVjV2VpcDU5Fba1csztpPVdicyNB4I2d7lWQ7LibicMBQbvtaiagqds/640?wx_fmt=png&from=appmsg "null")  
  
看到这个ExtSystemInvokerServlet就会很熟悉(因为它在web.xml有出现过)  
  
是api openapi yls这三个baseurl的servlet  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBR3wibzYML4xuqzVibm4eDZ8ib8aR3iaOQrollfa7aicu0sib4YnCicrqYxVwaW0pIyJANiclWKG9e6RZ7JgXEYo3PIpDQPfY4va4Bohs4/640?wx_fmt=png&from=appmsg "null")  
  
到这里就对路由构造就有把握了。  
  
然后我们跟着调用一点点来看即可。  
### 2.JSONInvokeBP读取配置文件  
#### JSONInvokeBP.invoke  
  
**注意这边接受的数据是json格式的**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBT5LzHl9s5eE3QXibChxnEnG9iaicyeQUKcyiaAb6jia2qUG9EE7LQjPFoqup81pK6oaZMz5rwCice7P49VF4OKtTIK4wSkPo176EA4g/640?wx_fmt=png&from=appmsg "null")  
  
invoke方法的主要作用：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTwGwb94GHicaudm7gn2icbh7W3vHhZoRvRCXSib8xURicswKlL9fAJxNyJZuYSvYiaqWf1A1jq5K3oKym854XDrf3xJKqt5sNW8wEc/640?wx_fmt=png&from=appmsg "")  
  
主要是queryConfigVO这边  
#### BillConfigFileParse.queryConfigVO  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBSz8DxticjYJBSG3icCks2slrNLOnoIBCXr1I7QXiczUgOIR3bZW8KHCrklaaoaMTSKZpE626d1jgRXDkBYPNxt6J4bxndBXTozZM/640?wx_fmt=png&from=appmsg "null")  
  
这边会先把传入的**servername**  
分割成多段然后**path**  
这边先是获取你本地的**api**  
路径然后读取前面分成多段的第一个加上.config例如你传入ce.paper.query 那么就是变成ce.config然后用 ServerConfigHandler  
 解析其中定义的 <service>  
 项，再通过匹配完整的 serviceName 返回对应的 APIConfigVO  
 配置对象  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTTebvPcP7Kyccgy3z9YBCX9jTAcXs8dUiaRz77SRicggpwd0tNicwfHfaoibYDgPscTCrficDoAe7s6Egq9SRZHLkowmE2FSrtWk8I/640?wx_fmt=png&from=appmsg "null")  
  
此时就可以明确必须得根据config里面的传入  
```
    <billconfig name = "ce.paper.query">
        <action>u8c.bs.ce.action.PaperQueryAction</action>

    </billconfig>

```  
  
  
即这边要用ce.paper.query  
  
然后继续根据调用继续分析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQ6LGUbB9iahTIIt4HMlwgoiboH7Mibg52fZALqGALJ5ZPVj6xFTOpsgbDgqrcDjiaKia2zdGia6mRnTqs7sWGacia9kUKQmnF2jWGicXQ/640?wx_fmt=png&from=appmsg "null")  
### 3.分析鉴权并绕过  
#### APIOpenController.forWard  
  
这个方法有两个鉴权的地方。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSgBWBicibmU3Q6kFLZz9icyKzToWomnzUGVKZbEX6NbqZSMXMjrLQlfTCNvkMkltyOibI4U8eWeXEWy5ZAdACJoWtpLur5BadGpQY/640?wx_fmt=png&from=appmsg "")  
##### 1.appcode  
  
它会先解析基础请求信息而后进行一个合法校验是否传入U8 cloud颁发的appcode  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSo93DzaV1UAZK7A9mOMEUdoSHn4Cbenhe8ibRciaibIqNaUECPZwbToibDMX0Cr5noavTtJcdJPUl5VicA15Gw0S0uErM2iaf9zunZw/640?wx_fmt=png&from=appmsg "null")  
  
只要我们能满足传入的路由里面带有appcode并且是如下四种就可以通过  
```
huo esn lbsj ubz
```  
##### 2.isEncrypt  
  
还会根据isEncrypt这个参数判断是否加密  
```
String decryptData = this.decrypt(inPutData.getIndata(), inPutData.isEncrypt(), secretKey);
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBSG1MfJTtFbCicLfPVQ50qfPnm1icA9NcpwsMJDXhibr9840jeNfnCib7j97MubruicpwDtP5icjYS6xPZ2lQoUWCV2x3ibgriaicBkOsA4/640?wx_fmt=png&from=appmsg "null")  
  
此时保证isEncrypt=N即可。  
##### 3.upm读取  
  
这里还有一点  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBRFmD2Kne5CphYMbIz0udbNFWq149AQkANkWibYibNE736d1cdAlBk19snXTiaWUyC4X5pwhXvrDpiaFbdgEF3e7uLUU77nib1QRDYQ/640?wx_fmt=png&from=appmsg "null")  
  
NC开发中会先写个upm文件它类似映射表   
  
https://blog.csdn.net/mr_accompany/article/details/124608265  
  
当服务启动之后底层的 Component Container  
会：  
1. 遍历所有 jar 包和目录下的 META-INF/*.upm  
。  
  
1. 解析 XML 里的 interface  
 和 implementation  
。  
  
1. 把这些信息存入内存中的一个 **Registry（注册表）**  
。  
  
当代码运行到图内的IInvokeWithJSon invokeFrame = ()NCLocator.getInstance().lookup(IInvokeWithJSon.class);  
就会去内存里面查询。  
  
所以我们就需要去找IInvokeWithJSon对应的upm文件(该upm下面就会用到)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQXZjtvSczWc1OoJsA1DRpKM1P8iac7gRRWicqfs8cZ6ER2E5X7BwMfKR925vIeNuadxPT25M8AOhVbx1HRc1mojwgpeR2NwYDpA/640?wx_fmt=png&from=appmsg "null")  
  
可以指定文件后缀节省点时间。  
### 4.构造完整url  
#### ExtSystemInvokerServlet.doAction  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBSdiaJkQ4NEiaaLpBYKv1eqON7iaTZhuTNHvcia7BadtJQ93y1NicMgoZHnb3k1Kvu2eGMW21UyGnz7y4mu1NbDK5QtPlHQz86XuyiaE/640?wx_fmt=png&from=appmsg "null")  
##### doAction 的主要流程  
  
从请求 URI 解析对应服务名。根据服务名获取服务对象。启动线程监控并记录日志。  
  
判断对象类型：  
```
Servlet → 调用 service()

IHttpServletAdaptor → 调用 doAction()

普通对象 → 使用反射调用 doAction(request, response)

前置处理：preRemoteProcess()

后置处理：postRemoteProcess()

异常处理和日志记录：postErrorRemoteProcess()
```  
  
根据我们前面发现的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQFsxdFGUxMJicEf7Ja6fPq3ArMQ6qGel3pgWDySFyf2h3zA7GMvWAvuGXUUsbo51LkNsTQY0szZibUldJFXYyRnFdKd6gc4WM44/640?wx_fmt=png&from=appmsg "null")  
  
那么我们如何确认是哪个baseurl  
呢？以及是用doaction  
还是serivice  
呢？  
  
这个时候就要回头看我们唯一没有分析的调用了APIOpenServletForJSON  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBRib045Lqz1DwFw4PRKuPrpjwKt432H2RrjgnZLUAzib63LMlFMg3FPgt4QpXsTYmV0kTARX0DxcLs4Mz9O2CDDmG8oM94jB8njY/640?wx_fmt=png&from=appmsg "null")  
#### APIOpenServletForJSON  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBQouNU0u2bZob1Ug5lZZK1pJR7qliaBsnwQiaEzDDgdFuEydtc4gZgDOW2icMqJmarozukpteibaZu4c0YYh3Dg4R11z7Egl26bYS8/640?wx_fmt=png&from=appmsg "null")  
  
这里第二个问题就有回答了，implements IHttpServletAdaptor  
 所以是doaction  
  
再根据前面分析的upm文件  
```
        <component name="u8cloud_openapi" remote="false" singleton="false" tx="NONE">
            <implementation>u8c.server.APIOpenServletForJSON</implementation>

        </component>

```  
  
  
以及  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBQrNkq4UUdQiakLzLeia5FIzVqX84CfABtdW8jBVd6TzDdgvzS2niasuuVNlZhr3fF07xiadj7S0Azo23iasZ6lsULYYPqxYncnpTBs/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBTKHCpDgqbSgN8y3LQ3iaYFIS6RuPAglhJR9NxchPPUd9tGfB3iacdpyeicPgydhM1ia1lOibAbAS2njH6karY3AZWG9AmJEHSfRTgA/640?wx_fmt=png&from=appmsg "null")  
  
会去根据我们传入的找upm里面对应的name 而我们的调用链中有APIOpenServletForJSON  
  
所以对应的baseurl  
就是/u8cloud/openapi  
  
所以完整的路由就是  
```
/u8cloud/openapi/ce.paper.query?appcode=huo&isEncrypt=N
```  
## 3.Poc构造  
  
根据上面的以及  
  
PaperExecuteVO  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QLbB9SNicNBS3Kn4LnOE7hPDnwM1Lk51yfDgP2jxAlV9Ih1tiaNPpKqocHIathlsskGK78ZAZghtwjeM0yGZkqicIicfOQN1XJQv3b8gU0yGic8U/640?wx_fmt=png&from=appmsg "null")  
  
得到如下的Poc  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QLbB9SNicNBS0BohlIwvLhbWXV78655jIEt3PIDTgLUBsjDFSbMgLeekrKIscI1CibyEMsYk1ibl5utyz5ic51mwCDqLfHs9C99Yt3srATdh6BI/640?wx_fmt=png&from=appmsg "")  
  
由于群人数超过了200，只能邀请拉群，可以关注公众号，后台回复“加群”，获取助手绿泡泡，联系小助手进交流群  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOMfKLgicfzPibMbAiaD5sibH2dkaicjnVdvl67TCUKPBRdVcFf24HoU5mq0PojwIsN8YzOUXaL2TnKzlzw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=31 "")  
  
  
  
