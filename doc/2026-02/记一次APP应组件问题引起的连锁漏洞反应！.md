#  记一次APP应组件问题引起的连锁漏洞反应！  
原创 tangkaixing
                    tangkaixing  开心网安   2026-02-05 07:09  
  
**免责声明**  
  
由于传播、利用本公众号开心网安所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号开心网安  
及作者不为**此**  
承担任何责任，一旦造成后果请自行承担！如需要转载等，请标注文章来源。如有侵权烦请告知，我们会立即删除并致歉，谢谢！  
# 概述  
  
         
在移动应用安全测试中，Android应用的四大组件安全性往往是突破口。本文将通过一个真实的渗透测试案例，展示如何从信息收集开始，逐步发现并利用多个安全漏洞，最终实现对目标应用的深度测试。整个过程涵盖了组件安全、隐私合规、验证码机制等多个维度，展现了移动应用安全测试的完整流程和方法论，涉及相关图片均厚码处理，感谢看官理解。  
# 正文  
## 1. 信息收集与目标确定  
  
在一次src对某服务平台系统的漏洞挖掘过程中，我首先通过资产收集工具（如ARL）发现了旁站目标子系统。访问目标网站后，看到一个标准的登录界面。按照常规的Web渗透测试方法，我对登录框进行了看似全面的安全测试(文章末尾附有登录框测试点表)然而，这些常规测试并未发现明显漏洞。正当我准备放弃时，注意到登录页面下方有一个"APP下载"的二维码。这引起了我的兴趣，因为移动应用往往比Web应用存在更多的客户端安全问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDTa6Kwc6zMWNYHBKBy3iape5W0ib0EsIhQCwJtC5GOwhjIhoCaRO9Om5F7rdicJ6nGXzhH955eJvwyHZOIAoSIgKg3MibcooibT9PJo/640?wx_fmt=png&from=appmsg "")  
##   
## 2. 移动应用初步分析  
  
下载APK文件后，我首先进行了基础的静态分析：  
  
使用工具检测发现应用已被加壳保护  
  
考虑到脱壳分析的时间成本，我决定直接采用动态分析的方法，从Android应用的四大组件入手进行测试。这个决策基于一个经验：许多开发者在组件安全配置上存在疏漏。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/uLpuFLYKHdW0pQwO6FiaUlmdorl9QElK0ydkN8sBZ5l4U30jnOtHyyDhoWvqIhBfFUpfoV1HDO8Un1ibvM0YjKnA/640?wx_fmt=png&from=appmsg "")  
  
## 3. 攻击面分析：发现导出的组件  
  
使用Drozer工具对应用进行攻击面分析：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDTusyzvaZQn47VRFNfCKwqtMgLVSICcRqPXQSbXccQcicCOMLc07Sl6d9ibAMzbhpw9lmsibvKxQMibBPITCdaMT8RcXLd7ZLEMKeM/640?wx_fmt=png&from=appmsg "")  
  
应用导出了17个Activity、1个广播接收器和1个服务，且大多数都没有任何权限保护。这为后续的渗透测试打开了思路。  
  
打开app登录发现不输入有效用户无法到达登录界面，会一直弹窗提示，看着就以为完了，但是分析了  
AndroidManifest.xml文件就有了新发现也为后面发现其他漏洞埋下点。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDQzReWkJxWlndBHjSNwWxF8ib78Ky1QOwricMlInjUtD4IDZcRgQovEhM1msjXKmuXgwdNnzYt6pFibPxIr8OHbKaNc6jJgIx5LKA/640?wx_fmt=png&from=appmsg "")  
  
## 4. 隐私协议绕过漏洞发现  
  
我首先测试查找登录相关的Activity。以及看  
AndroidManifest.xml就发现  
LoginActivity字样，使用命令已验证没有想到直接就直接成功了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDSmkrfqg6wb6oxUx9vOqF4wjyDsyglsxjZuXWg0kZTJNFftUb6jiaHpnwk7LBktmBHGAhMsCg9vQUIWA5feDMKicZpYRDZDLty1w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/uLpuFLYKHdW0pQwO6FiaUlmdorl9QElK0oobibKGC7bYGwonyBLmmwyweSC5OGVB1jxWMx1DBGFmu5Bm5OnEDqNQ/640?wx_fmt=png&from=appmsg "")  
```
run app.activity.start --component package_name com.xxxxx.android.xxxx.activity.LoginActivity
```  
  
        
发现可以直接启动登录界面，但更关键的是：这个启动过程完全绕过了首次安装时必须同意的隐私政策弹窗和输入有效用户名到登录界面。由于LoginActivity被设置为`exported="true"`且无权限保护，可以通过Intent直接启动它，从而绕过隐私政策的同意流程和对有效账户判断流程直接来到内部用户登录界面。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xqXavzxLiaDShlfT5RLv49GFL9GoUMLwicJGsmlrFiaNSXB8OWL85VtaeHUBMTbO3DzZWsI9aUyUTwXaF4j2b2GC9skUYPiaDTqyL0jW23icNXYw/640?wx_fmt=jpeg "")  
  
这里已经就算第一个漏洞了，当然这里最直接影响就是  
违反《个人信息保护法》等法规要求。进一步测试发现，即使在未登录状态下，也可以直接访问多个业务功能界面：如下就举例一个直接发起调用手机相机，就不展示一一展示图片了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDQbfS2icooO9j9wyNSrUic9A0gwiaheUqkkiaPfjTHwibcpHkd6MnzWdPauEuwXrbia3B7DQiahC6zfttcb1MSkeogVVUYnpoA3Dq0BMA/640?wx_fmt=png&from=appmsg "")  
```
扫描功能
run app.activity.start --component package_name com.xxxx.android.xxx.activity.ScanNewActivity
票务相关功能
run app.activity.start --component package_name com.xx.lib.marketing.module.xxx.CollarTicketActivity
优惠券功能
run app.activity.start --component package_name com.xxx.lib.marketing.module.xxscount.MyDiscountActivity
```  
  
这个问题的根源在于应用没有实现统一的身份验证拦截机制。每个Activity都应该在`onCreate()`或`onResume()`中检查用户的认证状态，或者通过一个基类Activity来实现这一功能。  
## 5. 验证码回显漏洞发现  
  
尝试测试忘记密码功能时，很快就出第二漏洞。拦截忘记密码的请求：  
```
POST /mobile/kaptcha? HTTP/1.1
Accept-Language: zh-CN,zh;q=0.8
User-Agent: Mozilla/5.0 (Linux; U; Android 9; zh-cn; ASUS_I003DD Build/PI) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1
platform: m-andrid
x-project: atb-andrid-app
Content-Type: application/x-www-form-urlencoded
Content-Length: 18
Host: 
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
Cache-Control: no-cache

mobile=18888888888
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDSaB00aPu4JGnKMY7RuTSzqsniaycFibVpVLHmWonABT0lZv8pW6tyv1bs5OIxcaddlnJDrojRotkNAUZb8DmNH81AF1O1xjqAjg/640?wx_fmt=png&from=appmsg "")  
  
我直接一手枚举常见测试手机号，发现居然验证码在响应中，还有就是居然响应中还反馈会了身份证号，离谱，感谢开发赏饭吃，这里就可以改密码然后登录开发账户了和其他账户了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDRKTAuHfQibAozgtSdMRptL7rdmakHWLpavaEAweYJd7r7fhqaLPibcyWKuxbcjUDUmHUwXyRrvciatuPTFvto9avJicgdFnYfvw14/640?wx_fmt=png&from=appmsg "")  
  
## 6. 垂直越权漏洞发现  
  
在进一步测试中，发现从游客模式进入在点击个人中心，加载了一个info接口，也返回身份证信息，我就尝试把  
cardNo置空，遍历userld,结果可以看到整个平台的个人信息，返回大量敏感信息，到此第三个漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDQjJfKC22bmKDwO2298vkta4V9KdKj1OjT2OkiaItQgRicSvlMm8RSgYoSK8vkv0E5OyaKaIPETB6Q53iapGsV96Zd6veJsonOcQ0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDSia6SLW6epQgIicjN576OeGicYYutT1a7pDpiaqaT3EMc9WZY2N7nOlS66ZmkEwUetdBB0oS9uiaQgvpxxP77RuhqZyteHiaNSVOX1A/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDS41H57NSSYBRbKWgu2XtCW0UY62MAuZKT9icmSBLuWhibGyBZm3Kr5MFicZF7LMSDJ9UyryEE8kTKKq1hgrKOtj5YbbnO2jiapQTU/640?wx_fmt=png&from=appmsg "")  
  
到这里我很想说，网页的防护是拉满的，怎么APP防护就这么水，真是运气来忙了，挡都挡不住。进入后发现在游客模式可以看到的数据有限，但是都是依靠userid来判断数据是否存在。都是存在越权查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDQXMlLXSP7bKCI0jr2GUrtiat3m6mCswicJrc87n0kGtWm7eq4kk9PkLCmrfS4ABrXibPeNVF7HJINJ0DNtoXI9E57AibTsOfuAzzU/640?wx_fmt=png&from=appmsg "")  
  
到这里就结束了，很有多图片涉及数据较多比较敏感就不用展示了，后面还发现系统主要就算靠userid和返回sfz唯一值来出数据的。截图如下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDQ6Libfc7rUWaG9NPBvG34rA9hOtgBvDNFnHvCbL7tOSbbIHR1IDCj67IL9yM8IPnl8je5UmP7p9erBHsibRkqxYD0XQhYa1Twkc/640?wx_fmt=png&from=appmsg "")  
  
后面搞了一天把基本是功能点过了一遍，发现如下漏洞，  
打包一起提交  
。  
  
ps:[打个广告，可以接收任何短信的接码平台，欢迎各位看官注册使用，感谢]  
  
https://h5.haozhuma.com/reg.html?action=kaixing678  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xqXavzxLiaDS4QVtJc3VDIDx8icpq6b2fkkhZNZaTnnrsFbsW2cPDGnfORwiaUI5qTPlicXRV5IzUdiaggXMlvVavQqCic0e4icwzhURwEIia9VzBJ0/640?wx_fmt=png&from=appmsg "")  
  
# 总结与建议  
## 渗透测试的收获  
  
这次渗透测试展示了几个重要原则：  
1. 攻击面分析的重要性：从17个导出组件开始，逐步深入发现多个漏洞  
  
1. 组合测试的价值：单个漏洞可能危害有限，但组合利用可能造成严重影响  
  
1. 客户端安全不可忽视：即使Web端防护严密，客户端漏洞同样危险  
  
## 给安全测试者的建议  
1. 从攻击面开始：四大组件是Android应用测试的良好起点  
  
1. 关注业务逻辑：不仅仅是技术漏洞，业务逻辑漏洞同样重要  
  
1. 组合利用思维：考虑如何将多个漏洞串联形成攻击链  
  
1. 合规性检查：隐私保护等合规要求也是安全测试的重要内容  
  
这次渗透测试案例展示了，即使是加了壳的应用或是不会脱壳，通过系统的安全测试方法仍然可以发现多个安全问题。安全是一个持续的过程，需要开发者和安全测试者的共同努力。  
##   
## 付web登录框测试的点表  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xqXavzxLiaDTIvuLH6osVufhWI9kiclMfumYRzuich6wOadY0THUNib1Jy71ian8EjAG09oJLRpJ3wPlySB7osqeBsOIc6IYGYq0lLbicsn4nib8mo/640?wx_fmt=png&from=appmsg "")  
  
  
