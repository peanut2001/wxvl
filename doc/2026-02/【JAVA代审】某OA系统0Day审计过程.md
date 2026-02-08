#  【JAVA代审】某OA系统0Day审计过程  
原创 C@ig0
                    C@ig0  菜狗安全   2026-02-08 01:01  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPlzg5sZKIlTPHGFlkF53seUMNUsR3TKcn9VGDeJTwzichS2dI31pVDLibP6XhejxiakNbBahbqtchM5A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/QtaE6uFmibPlzg5sZKIlTPHGFlkF53seUgwlRhqQibojuE58lklgLm1hpT7yT88speo9QwTL6dlaFNdP9TvsdL9Q/640?wx_fmt=gif&from=appmsg "")  
  
点击上方蓝字·关注我们  
  
  
免责声明  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/QtaE6uFmibPlzg5sZKIlTPHGFlkF53seUZHdTe6rSPrTwIbY4nGDic3ick7JK8o2LnQqAYibZia3uZmzNvdMZiciaZMPw/640?wx_fmt=gif&from=appmsg "")  
  
  
由于传播、利用本公众号  
菜狗安全  
所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号  
菜狗安全  
及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，会立即删除并致歉。  
  
前言  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/QtaE6uFmibPlzg5sZKIlTPHGFlkF53seUZHdTe6rSPrTwIbY4nGDic3ick7JK8o2LnQqAYibZia3uZmzNvdMZiciaZMPw/640?wx_fmt=gif&from=appmsg "")  
  
  
文章首发先知社区，原文链接：  
https://xz.aliyun.com/news/  
91536  
，作者：  
caigo(本人)  
  
文章目录  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/QtaE6uFmibPlzg5sZKIlTPHGFlkF53seUZHdTe6rSPrTwIbY4nGDic3ick7JK8o2LnQqAYibZia3uZmzNvdMZiciaZMPw/640?wx_fmt=gif&from=appmsg "")  
  
  
```
介绍
项目分析
代码审计
    鉴权分析
        downloadfilter
        ProtecFilter
    多处SQL注入
        第一处
        第二处
    多处文件上传
        第一处
        第二处
        第三处
    多处任意文件读取
        第一处
        第二处
    多处BSH代码执行
        第一处
        第二处
最后
```  
  
  
# 介绍  
  
  
一套比较老的OA系统，在野资产不多，产品版本迭代后换了个马甲，在野只剩下寥寥无几，内网可能还有点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqKoMnQ0tdwBz95nBBD8mQoQCHczCmSvOR2alY4jzW4icGe9zvp0mqic2vEXtZHCTmJBZbLK3gYlVcibWmWcHa1NYibxDF6AgJLoIw/640?wx_fmt=png&from=appmsg "")  
# 项目分析  
  
  
又是个大杂烩项目，项目的属于是传统的SSM架构，后端的业务处理是Struts2和spring MVC，前端渲染采用jsp，但是项目的一些可以直接访问的jsp文件中有业务代码  
  
那么我们审计的接口和方法就有，Struts2方法，Spring MVC方法，jsp文件了  
# 代码审计  
  
  
## 鉴权分析  
  
查看项目注册了哪些Filter  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqRnEj0NibybWVHOwjwH9eJicIHhTvIJAQicdTiaruJCb6FjhWkJp7OwH8FI2gHicFHKbqYCqYxocSXKx7NjNyonER5aL1UWLwYDju0/640?wx_fmt=png&from=appmsg "")  
  
  
这里正常就一个个看了，优先看全局拦截的  
  
### downloadfilter  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrUQYuJ7DlX8icmyyf3UPvMSh6qhBzMfHnccJqRb3SOKhYXYE4kxLCQWEZd5pU1iaCYMOzibHYIkwmASDlxq7cRJ5mjbIl4RrMNy4/640?wx_fmt=png&from=appmsg "")  
  
  
还是一样，看Filter的时候先定位doFilter的放行点，然后看逻辑，关键判断是什么  
  
  
那么这里可以看到只有57行一处放行点，并且是在这大if块外面的，所以我们就要看if块中的逻辑，是否有什么条件语句导致方法提前return导致无法走下去  
  
  
可以看到有两个if代码块中有return的点，分别是44-49和50-54  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqDLPXC6X8VayRXqR5CQToMz6ciaeTLQG44FFJzTgFNAiaEr0TmqJVRN1icWiaAts0ksFRpBjBicQ6WDekr70hCuSKlNtQfLA1aQ5jM/640?wx_fmt=png&from=appmsg "")  
  
  
38-43都是初始化逻辑，定义了参数，然后对ServletRequest进行HttpServletRequest转换，接着使用getRequestURL获取当前的请求url，经验丰富的看到这个方法那么存在鉴权绕过的可能性就很大了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqZcQ1Picibf7y7JJP3AcuwTRmPUibdDZibU53o9jHicVINqwiarDsCch9sBKJibLbP3OJX0TWDcr18VmhPiaomoaZicfPib8bVTiaADic7Cco/640?wx_fmt=png&from=appmsg "")  
  
  
第一个if判断，如果请求url中出现了bak或者CacheTemp则会进入代码块，接着调用privilege.isUserPrivValid方法判断，这里一个参数是request请求还有个是admin，用脚趾头想想也知道是鉴权的方法了，这里后面再分析下privilege.isUserPrivValid方法的逻辑有没有问题，这个如果不满足就会进入if构造一个url，然后302跳转，这个判断一看就是校验是否访问备份文件和临时缓存文件的，我们看下一个  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTovIPmIJ20kHBStTv6t4Z2ocp3PAACsORX7hsoQq4icPPQPQGTwEqoib1NsIHcKcib7AEp80U9Impnuicaic2F6Pb38lzMVDs798ZSE/640?wx_fmt=png&from=appmsg "")  
  
  
这个判断逻辑长点，但是也很简单，这里把几个条件拿出来  
1. !(privilege.isUserLogin(req1)  
  
1. (path = (requestUri = req1.getRequestURI()).substring((ctxPath = req1.getContextPath()).length())).equals("/")  
  
1. path.indexOf("common.js") != -1 || path.indexOf("module_field_ajax.jsp") != -1 || path.indexOf("/setup") != -1 || path.equals("/index.jsp") || path.indexOf("/login_oa") != -1 || path.indexOf("/activex") != -1 || path.indexOf("/public") != -1 || path.indexOf("/js/") != -1 || path.indexOf("/inc/") != -1 || path.indexOf("/skin") != -1 || path.indexOf("/other") != -1 || path.indexOf("chatservice") != -1 || path.indexOf("images/") != -1 || path.indexOf("nest_") != -1 || path.indexOf("/flow/") != -1 || path.indexOf("module_sel.jsp") != -1 || path.indexOf("basic_select_sel.jsp") != -1 || path.indexOf("flow_sequence_sel.jsp") != -1 || path.indexOf("module_field_sel.jsp") != -1 || path.indexOf("/wap") != -1 || path.indexOf("/test") != -1 || path.indexOf("desktop") != -1 || requrl.indexOf("/error.jsp") != -1)  
  
第一个也是基本一眼丁真是判断用户权限的，第二个则是判断请求的url是否为根目录，第三个就是喜闻乐见的白名单校验，只要请求的url包含第三条件中的其中一个，那么这里就不会进入if，就直接结束方法走到chain.doFilter  
  
这里只要构造url如下，即可绕过  
```
http://192.168.21.133:8088/test/高危接口;common.js
```  
  
就绕过了  
  
我们可以实测一下，找个代码中无鉴权的jsp敏感文件  
  
  
比如：admin/user_edit.jsp  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTr8clsec8dqicBNxsgx6EfzTuC0eqjlpgC9eL84f5TiaOGsRUdpJDFBVNSH5UUcharzNoFIOaJ7g5wXicfYfYlUMHNrcYVSTNd4rw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpunJMk7bEqFOTmLEwOI8sspSeuaLLeSy6wPFEIlpSkjUHrSJfomXFRoFblJ9gtBn9QlVJL6tBtAOL35nu4mZrhB6S9res6ib9s/640?wx_fmt=png&from=appmsg "")  
  
  
这个是因为这个jsp文件中有校验当前用户权限，但是我没登录，所以会提示权限非法，但是鉴权filter是绕过去了  
### ProtectFilter  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrOVLYiaspJm6JjGmf9grlZ2rFxxsoia46N5H3WBxO7RbgibBuLjKSIcicR0h7EwIrvS69C7Hr4bkcibribVr5WfcCKuAEIU9SHLlD2Q/640?wx_fmt=png&from=appmsg "")  
  
  
这个貌似是用于预防sql注入和xss的filter，如果请求的url不包含error.jsp则进入判断逻辑，初始化bl = true  
  
接着调用SecurityUtil.filter进行检查逻辑，跟进  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrBOicYLmC6LLqAcITvgT5yrn9HDpnqWPiaiaxqibVL2Ql74sc8S4DTD6P8nUXOa7z4RsXFN5C5kcpH5ic971XduzTrFicfU43hk3TuM/640?wx_fmt=png&from=appmsg "")  
  
  
这里逐块分析代码，第一部分  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqxVfjX5VoYOTiaicWB2n7ia9yYOwX22ry3AlVn9pOKUlbKXuSpjZ5nmet6wAiabDrTDwZ5eTVib8hBNHMrUW8meoiczPIdcfdpXl7NY/640?wx_fmt=png&from=appmsg "")  
  
  
new ProtectConfig接着get获取AllUnProtectUnit配置，for循环遍历其中的元素，判断我们请求的url是否包含UnProtectUnit的规则，如果满足就是return  
  
  
这里跟进下对应配置  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqpI6tTS1Qs3r5wFHA3w4XXXTuwjz2LdOodsIQqpS6a9cPzVDxgKsV1eXpOQ0ZKaMiaJdQ6TnFNjaYnLwz379pLKoiaL8ONwfzick/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrvTCW51a4P5Mj0LTAPaosP6KAuI0zduYq4q65PqCibib1jjgRHfMJQROcZwExzrtDemEtXp01ZMuPOugMxjyxkPDSs9ZAic0QlMg/640?wx_fmt=png&from=appmsg "")  
  
  
也就是说如果请求的url中包含了exclude="true"的接口，这里就是放行  
  
例如  
```
http://192.168.21.133:8088/test/../mywork.jsp/../存在注入的文件?sql=恶意语句
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpiaFLzibhU6faOlz2sHk7ospm4iaibbA9r7dhJgwMx3oibhTiaZ595rYlompTe40czbN8ribJ8TLra2BKcKGVBufTHKV1XWwLfzDOSS4/640?wx_fmt=png&from=appmsg "")  
  
  
比如这个请求参数中有Update给拦截了，我们修改下url  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpbgI1puzicgG8u3qdbkffSGPPtxJPO0KiboL2y1PhbwZSnQAytFWz38MxQCSaVZv8xCe26ySiclfKB65L4BSTFLeJRQZQmX4XZcI/640?wx_fmt=png&from=appmsg "")  
  
  
成功绕过，这里也可以用error.jsp，就是前面的if判断  
## 多处SQL注入  
  
  
项目采用jdbc为主  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqD5tknPTmjqgZedafYKelicAkP1gibofzjoCstJvXyHwe4viclwic1ziaPXs1bnbQXDxpaqIRVl5UCbKgMsrFFyEOhz9UKOfR1euOo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTric7mbDyiaS9F5RCAVfs2f6MsD2oVKqxSrs7iaQ7E5XepjR01RgJmx11qibTnaFmyHShJQKhBNZicdM8bFXoAP5Pxg3JzqR506hUxw/640?wx_fmt=png&from=appmsg "")  
  
  
大部分不是预编译，就是参数不可控，部分可控的还有注入防护函数  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUToqav5VSWiaNFsYULsVb0pC5KJ1EY11UOqhMTuSNYsOd9ZibRBXicZ7XZQ3Z84YSqXN7EtYm0fjBvbFDWmTrN8lKibHUGQVWwP4YHk/640?wx_fmt=png&from=appmsg "")  
  
  
跟进方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTo6cqMN86lMvkW6BQvhSauJjCCOmgR1YcQoicELibgvHPoFjX23y5KFkczD7Vsr0yxYRsGHjWvTerdze0tIvgNHWIv1KNs7JwaHg/640?wx_fmt=png&from=appmsg "")  
  
  
如果传入的字符串中存在'则替换成''强行闭合，这个绕过得考虑宽字节，那么我们的审计思路就是找，非预编译，参数可控，没有调用sqlstr方法的拼接点  
  
  
这里从业务逻辑来说有两种  
  
1、查询参数需要传入整数  
  
2、in || order || where查询可能没有使用sqlstr  
  
  
原因这里就不说了，很基础的东西  
  
那么直接搜索对应的关键词，如果要前台还得文件中没有鉴权方法，所以这里我用FileLocator Pro来筛选  
```
"order by" AND NOT "!privilege.isUserPrivValid("
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTr2JbEIvW80SlwTyX5a6TibBNfvajWZicc6mTSoSn4Ig4Uogwd6aJfp8Tj4jeLxCsUUZHlVCgc0M1lx0LkknmoxVTmVfEQfxlicdI/640?wx_fmt=png&from=appmsg "")  
  
这里演示两处，主要还是找的思路  
### 第一处  
  
定位到linkman_list_sel.jsp  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpjrWWTicXyvicS9WWOsfIO40opQ1ibk4T8q9doPGHicXcpwUVZX4KiaibP3bE5qwC2rMKxyNHGuJGZh32gheosvJvXhRYYhFVObdiacQ/640?wx_fmt=png&from=appmsg "")  
  
  
这里前面的语句拼接都调用了StrUtil.sqlstr，最后的orderby和sort拼接没有调用，关注参数是否可控  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTp2GicjMUxJhPmGsZOdvyYYJcYRkIHan289U8pRS7RCYWna2Z7BNY6teB9qJiaEqeOIvflLtjCv3XluYSm7NrHypNfibWFBggqV6I/640?wx_fmt=png&from=appmsg "")  
  
  
调用ParamUtil.get方法获取，这里应该是个封装的从http请求获取参数值的方法，跟进看下有没有过滤处理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpt9R0ckwoc4sUSaa3HJNRic5ZbaibeI63RmUkyib8o6Vtv9ufZVjCCMgCakaM7Zib1DtgxSNiaLWsfIQeVaFNz2ZQlnVdAb2Grm6Sc/640?wx_fmt=png&from=appmsg "")  
  
  
方法很简单，从request中获取调用的参数值，参数值不为null，并且不为空这里调用UnicodeToUTF8进行UTF8解码，这里没有看到会对我们注入语句造成影响的点，那么存在注入  
  
  
构造poc  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpUbxUSnzoC0YyLOcHTyK6JicQUEnxjvwzR2Bvnu0m0iaw9dbO9btrYwkuicd4xlUiaId4XkawYgtu6erRnY1pOFIwFX9F5WZHY7eA/640?wx_fmt=png&from=appmsg "")  
  
### 第二处  
  
listmember.jsp  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTp6exzjTUHK0uTB2DYOUoUS4o2l2ySJM1pOKj85eb2ykYwM20YaXzhJm2EerP9QybCL6r25kYNiau7rlcib6l72ObZwFs62mOTPY/640?wx_fmt=png&from=appmsg "")  
  
  
这里sql语句组成直接拼接了orderBy和sort，跟进来源  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUToRwsyT6G9hwry0bLP97ia2FkUVb2ibic2QmYFspRsYEAnoFGoWf24olKS2JGbI9wvQXrYXCWhibvmW0cpfWibfia4k3paRnfqXIicf9U/640?wx_fmt=png&from=appmsg "")  
  
  
也是通过ParamUtil.get获取，存在注入  
  
  
构造poc  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpT9XW7RuOEvibEB77MY4LwHRzqmicW5kFaicazjkua33IZjE1eVgzgNNsgxY5VHxfia7Ia84icnFKaicgPnTq8QXOTXGQibKhHZq1FdI/640?wx_fmt=png&from=appmsg "")  
## 多处文件上传  
  
依旧掏出大宝贝开干  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUToiaETsU8TfIcho6PWNNC4zcZZ4icRAf7UbqYIm1H4XXtVh2JiapibkY8swsOvNLzvo8evnmAVfehD6QB4P0xu3MfAZ1StEyg5BNmc/640?wx_fmt=png&from=appmsg "")  
### 第一处  
  
FilecaseUploadAction.java中的execute方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTocngjBBFtWXic8UwYjEc4SxutpUibYiabuPUy0gL4yFC8uTSfUw4q45GMgicicVFGGbFdFUrndHYH6eMYqVKOb7gXNRP1WUh7gF4uM/640?wx_fmt=png&from=appmsg "")  
  
  
直接看关键点，调用this.getUpload()获取当前上传数据包的所有文件，213行遍历上传的文件，214行打开生成的文件，214行读取上传的文件数据流写入生成的文件中，这里生成的文件采用的原始文件名，也就是整个文件名和后缀我们完全可控，存在任意文件上传+目录穿越  
  
然后我们看下前面是否有什么条件需要满足  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTottianZ4OrDxjlFS4ibgWKZCH6u6RNSUP9Xsc0wfAXCfMPbZeSoP7l1VgWnRtibQxFkFMUdYIMKKJCRakcQSPSeyU9o3Iu2bBbUI/640?wx_fmt=png&from=appmsg "")  
  
  
  
有好几处逻辑校验，主要是校验请求中的Skey  
  
privilege.Auth && privilege.getUserName 跟进校验逻辑  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpic26rGiaUkddgnGUias2hJua4oOIJZYmhic1weFLWJwN3CKU4NJsDjBnBzHNVJsgloUFibu5RIrmbH5cXoJhDibRPoUoxZuwv6uAcM/640?wx_fmt=png&from=appmsg "")  
  
  
调用ThreeDesUtil.decrypthexstr对应skey解密，lastIndexOf("|") 找到最后一个分隔符  ，提取|后的参数值，校验时间戳不超过当前时间20分钟，如果超过了返回true，返回json.put("res", (Object)"-2");，这里的关键是ThreeDesUtil.decrypthexstr的解密逻辑，先接着往下看  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpC3zTZv8icDmWe5yY6Tz1GGs1QOEeq6s3OOCTicnCXjoyHcy4zhia5gibcYTiajY62ak0MEKmLGN7COhkrf6WeIEsI13r6icxA6c76E/640?wx_fmt=png&from=appmsg "")  
  
  
这个方法实现差不多，提取的是第一个|出现前的内容，返回后调用user.getUserDb(userName)，这个应该是带入数据库查询用户信息的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqsm5UByCRBNj9o492bDl3HjLrAg3BooYTDxpBngRTmaROa39s8kgsRdYE3D6bSLiau0ibjdgXsAntUWxd3Cs4CjnK0jWl9nu5yc/640?wx_fmt=png&from=appmsg "")  
  
  
那么我们加密的内容就是admin|时间戳  
  
  
分析加密方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpNzibGCB9VSc8butwUbfnWP5xU6U55lvSKlZm3CNuK8sTXAib7g0Wib6ichLduYLC1NslpepheiagkbYibic3pth9EibCNYeTqfHYbgOc/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqx3rmBibuKmup9fibyC7sxrPNiaMribfziahIpUPI90b61qhmwTsVTRBjkCAUY83APq8sAa3wPichBkFtKcGUTcjbjN8VjgYldRibaIs/640?wx_fmt=png&from=appmsg "")  
  
  
  
采用的是3DES加密，主要密钥获取，从代码看是配置文件中拿的，看下是哪个配置文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTrqjgAjPicnqOvI4Ny3eGrPPBFVzZicIOROwusia78P8Nm6lictnE1icJJSNIZQs7xWXpvqglicWvLIBarZPgPCWNQXRh3ZyPwQePZrs/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqXIRdqFtnOibLdE2G5b80Y0lYK2j1nqMVjvq3HX88BsgLGN6LXpXxfjVRDXbN3nwUcEaw2Fa59kk6185QibrVgAlc6nibYsBMbTk/640?wx_fmt=png&from=appmsg "")  
  
  
拿到密钥，编写skey生成脚本  
```
from Crypto.Cipher import DES3
import binascii
import time
def generate_dynamic_skey(key_str, username):
    key = key_str.encode('utf-8')
    # 构造当前时间的毫秒数 (Java System.currentTimeMillis() 的等价物)
    timestamp = str(int(time.time() * 1000))
    # 尝试标准的 Redmoon 格式：用户名|毫秒数
    plain_text = f"{username}|{timestamp}"
    print(f"[*] 待加密明文: {plain_text}")
    # PKCS5Padding
    bs = 8
    padding_len = bs - (len(plain_text.encode('utf-8')) % bs)
    plain_text_padded = plain_text + (chr(padding_len) * padding_len)
    # 3DES ECB模式加密
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypt_bytes = cipher.encrypt(plain_text_padded.encode('utf-8'))
    return binascii.hexlify(encrypt_bytes).decode('utf-8').upper()
KEY = "000017697893609873688931"
USER = "admin"
new_skey = generate_dynamic_skey(KEY, USER)
print(f"[+] 生成的最新 skey: {new_skey}")
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpR7luSjZAgVNyTf3Rciag5ojbZIoAzEev5yM7U7eZKWmoy54qpa06G0DTva6lfZsCWvribQzMNnk8a3icToY2yDjQgHFTVfYaic1U/640?wx_fmt=png&from=appmsg "")  
  
  
寻找struts路由规则  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpdQcn8yY0vp0lia2Of6uFXJg1rbyZDokE2yeKMUF94fRFgRSusiaxKfR9GUMLQbcNW3HexP6MOuhmAIVSMaAkyeaGzf4PTwucxw/640?wx_fmt=png&from=appmsg "")  
  
  
构造上传数据包  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpDwz1e7I2BjArbPCYNsYRXHRhCkAXRiatXDZBqK9rWoNFydr9JOcNaltV6sfZLVgHibOVqfGzzoSfVhOiaYgnYLFkG9D2cvykl1Y/640?wx_fmt=png&from=appmsg "")  
  
  
应该上传成功了，回看下保存文件路径  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpAicg3uaCY35uK9dDUdcLWFvsVLiaxHLDQ4UkQQib75dR5vb4PIpbeaBmfu2VebicZccEUa6BvhATv3EXUP4liauvVISIg5zqx4qD8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUToovBpHccH2qDGuz9MNDCS0BV6xfDCXpLQsEo0UXMSpkjogJjVGvZsSKtbc4Ix5Fic3TMeE3icepscR3gAtFwyFxaKaMe7ukia7Ew/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpFAeU1Pp3ibVciaeHnVqIdibu0RCtLAvZYpa8dHX1yuliaSerkJWicqWd6kuepUdt7OuaDJUVZLkOCiaOkjYAA0mX1pTbHTqus41GBw/640?wx_fmt=png&from=appmsg "")  
  
  
year和month是当前的年月，那么对应的保存路径就是  
```
/upfile/file_folder/年/月/文件名
```  
  
  
访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpEKqJphzWQrVnBHtiadKCricKYrCtOaGx2ffgVHKkhXZbp0iaVibek3k310ibwotR3OWe4LoLDp6s6yyem3WCDQGl7p1hcoAZQ9YbE/640?wx_fmt=png&from=appmsg "")  
### 第二处  
  
NetdiskUploadAction.java中的execute  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTrpGWv6c6KRKzAz2Nds4EsGnzAEvTjNN3I7EjK3ibheqFsKGyvbYz0WR8BVIKY7WTBKRQlpMnfs7qnNAuoBCIF0B0aSiakiczuaQE/640?wx_fmt=png&from=appmsg "")  
  
  
  
几乎一样的逻辑，只是保存路径不同，cfg.get("file_netdisk")) + "/" + lf.getFilePath();  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUToACztyEZwzQLVPghR4GEIM5hmibUq8DVhrBFkGJUpJbTj3U01eN6IqWqh5FTrF82olDxLZed5TcFicP50Y7IBiawRibnYdibvB2AwU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTq7faSeibb4KjBDCxTuXu7x6bxh2RltKQ4laARQ8Y90oBW2xRdf9BFsCicDa6pwqEgDpYSSK8kGJuMrZu9jB1InwU1pfMk4rGWxM/640?wx_fmt=png&from=appmsg "")  
  
  
这个方法是要获取一个真实存在的路径，这里实际上是admin  
  
所以这里保存的路径是\upfile\file_netdisk\admin、  
  
寻找路由配置  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTp91vib3CncBMWJaibQAUtSxwqhDkp2SoF9KUlXqGXRF7cgDC9OyMCRxCXTerW7GgMZlWPAUmgVDR6TV0bYM3UUSqsGATTNMA7B0/640?wx_fmt=png&from=appmsg "")  
  
  
构造数据包  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrMukMoXKgVakqH6LEkEB87rttHASxrgeFBroQ1icYy7U2AiaiaK1tgJbFuaLxQymkaTvZVG0RiaU1ib3LuVVBfKiaAluKibs5ESfayNw/640?wx_fmt=png&from=appmsg "")  
  
访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTrwsEx6NRgjDph3590CAlSSPTToJ60HXgMaJx5lVl2hd5qwSXm8iczo93VNR2aKGyic5O9GNCOOQ174RicO9ZtqbbLiciaEd2LJ2lB4/640?wx_fmt=png&from=appmsg "")  
### 第三处  
  
NoticeAddAction.java中的execute  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpzG24wOuCWOic8WDC10YlfViaUaDmeGONOiaFx8fPRRQppY5KBG2MIeyJqqUKGxicGPMzDJu9NsxL2fgSILiauoWPYmS9peSvXmGQw/640?wx_fmt=png&from=appmsg "")  
  
  
这里保存文件的逻辑不太一样，文件名是FileUpload.getRandName()获取的随机数，拼接的后缀通过StrUtil.getFileExt处理上传的原始文件名，跟进方法处理  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrV1RUldnSmBrZNtXMWGsWCNvUwjTwpeIZl7wLowRg4G5Md1P5mbtiba8oHjC153oyjkKLRx9vxBYO9HBzWs0ia3w3hYeUfic7bFw/640?wx_fmt=png&from=appmsg "")  
  
  
就是单纯提取最后一个.后面的内容，那么这里文件后缀是可控的，存在任意文件上传  
  
  
查看路由规则  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUToicJ5qPGic8w75DvQQgT3XGicUQta2sr6whoUUJRia2TicG2MrfjNzqzVmic9ibabXAVsVOeQiaQmCSJFNv72kPnTHcomTb9tHVmo9sPI/640?wx_fmt=png&from=appmsg "")  
  
  
poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTptNsEAXXkoWJr4mia1tEKXep4WTrvUoYRkx9exmoxZJ4iczO9dZic8cwXOibpYhakibLTHqugXdZu0gzzcYJzY7bLSBecm8MEw6Ufw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTrUiczsUfia3jiaWZ3ao06sjeyN3ZGdJjpGulO31IDRXZ8hzaDUdGpV2cibsGaKdhsShtLc3PcicuOZdBiaic2RSSSx6ANclXs7jJBPDM/640?wx_fmt=png&from=appmsg "")  
  
  
保存路径是 upfile/notice/年/月/  
  
这里文件名的组合是时间戳加8位随机数爆破有点渺茫，但是这里上传成功后会把文件名等信息写入数据库中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqca4OkFn08ACVRt4yNu8blakMwFuyY7TibJkuaeRBbNSpXDE50NFkwQu83Mav9e6jAKXfb93UI0b1LMB3BS5kgx7wAueIrEhicU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUToemnZ0eSDLmE0icS5WSzY2h8pgfBGjRS9m0a9knu15VfNJZwwZB5jPp1v61Ec2TvwoLFXZjiaNCeDyicBSGxaiaqHDYwvmc8RLOFk/640?wx_fmt=png&from=appmsg "")  
  
  
可以尝试用前面的注入去读  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTox2tLbzicZWLokMywGAK8f8LNqdo0Z5ScQbLEWqzXcvAnF7y96xibCB31IseCPgJhLfEsRxI4L1SXcwvx79r1YtJiaicOvckEwQgA/640?wx_fmt=png&from=appmsg "")  
  
  
访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTovDibcibrm98f8sdTtvYb7ic8PQc96R0QibPpgoAiaiakeicic4yCXEbUkcbqAic8fiaI9J6FOYQ4ibNjl8YT5DHygcpoknG4CibDL7xiaNiasI/640?wx_fmt=png&from=appmsg "")  
## 多处任意文件读取  
### 第一处  
  
关键词：new FileInputStream(  
  
定位到getfile.jsp  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTouJJJcyYVzU2kplk5b4M4icoTpP3pgCNx7xNXuT4gJB4tHiaRQyAvd94RkP9kydA9g2xHVkl3kWt9RoNuUL64iboVdicsha37Huibo/640?wx_fmt=png&from=appmsg "")  
  
  
这里文件名和后缀都是request完全可控，56行调用new FileInputStream读取文件内容，63行输入到响应中，存在任意文件读取  
  
在上面代码还有个校验逻辑  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTrgDsdJqWIMboic7cDsaicia58J9oZ5iaPUViarR8dzBcYCHaUI7bKXAuqXKbqyVsGMV9GNr0lRjHKOlcI54dVZ8PzPpLXQ16Umn6wk/640?wx_fmt=png&from=appmsg "")  
  
  
但是这里一部分代码被注释了，所以只需要user不为null即可，user还是通过参数传递  
  
  
构造请求  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTrneZSPmQo1ctZZMt6spBlYXOZTrl2PHmZOeQqVmJP8xCfdxNULNRLGxYvedVHLMibBAJXeIZu1NOBrr8vRIyicLPsiba7of6I8yI/640?wx_fmt=png&from=appmsg "")  
### 第二处  
  
审计关键词 FileInputStream  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTqmXwcvrZd4QmO4cib0XT4xQY4dA9EpwHaCPyrBPic7ic06rjJYf1cRb8BdHBm7aYnKBzyicBV6NFtqnzw0vXU3ANghKKUsTZTPJoM/640?wx_fmt=png&from=appmsg "")  
  
  
request提取mappingAddress参数最后赋值给s，接着new File  
  
接着创建FileInputStream实例读取文件数据流  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqK244CqJKPAMcIzYNDheZhiaOoPoTHJHojFM0PkNEo82CbYgVgFQmibMHEJgPJNMjzLGjkTNu890mhZ8gde8w7Mtcl5tVkz3DuU/640?wx_fmt=png&from=appmsg "")  
  
  
最后输出到响应中，存在任意文件读取  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTq5PzqJSxCXLAHI0Ux2vRIulTUZuxRylHRF0SuQKbY85YY6yJsDBfLYvWyFicniaNWVa9OCdYOpk7TDYNmwcaiaJia9GSljq50cwibE/640?wx_fmt=png&from=appmsg "")  
## 多处BSH代码执行  
  
它是一个小型、免费、可嵌入的 Java 源码解释器，具有对象脚本语言特性，能够直接执行标准的 Java 语法，并对其进行了脚本化扩展    
  
简单来说就是可以执行java代码  
  
大致使用如下  
```
import bsh.Interpreter;
public class BshExample {
    public static void main(String[] args) throws Exception {
        Interpreter i = new Interpreter();
        // 设置变量
        i.set("foo", 5);
        i.set("date", new java.util.Date());
        // 执行脚本
        i.eval("bar = foo * 10");
        System.out.println(i.get("bar")); // 输出 50
        // 直接调用 Java 方法
        i.eval("System.out.println(\"Hello from BeanShell!\")");
    }
}
```  
### 第一处  
  
审计关键词 new Interpreter()  
  
定位到admin/script_run.jsp  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpzrHzTmLoMXSFlLCCBp8E0yLLO7cWySGLbicE6bTaCGBgOvqevK2svabCS6dHf2KMPmE3DRVyRZJUiagbGmngY4w56KqAibIFxo0/640?wx_fmt=png&from=appmsg "")  
  
  
这里57行的eval调用的参数myscript是通过request接收，完全可控，存在BSH代码执行  
  
poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpicH23jY6bdk0sy4sibp75AEynssibWoBSP7Tsz3np9Oiasom1EkD3P4zpuPu56ngrvibqfudxzibYm1u2VpoFLa8b7z78ic94mAqLfQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpN1duha5kibCXVR8jMjARIKeLLt9csYxZSOGqDdQ2RRrfGyc1zgc94WlmaSHSbH0qxMGa0gpIdAfvacxCuD52hldsr9EvcJoFQ/640?wx_fmt=png&from=appmsg "")  
### 第二处  
  
审计关键词 new Interpreter()  
  
BeanShellScriptJob.java的execute方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTozBbhyldyXRHwm4CUVoaAvwYlnVFj3icqy1Pc86KFwK8Dv9K0ZxRSx4heFmyicibqujkuSHZle4V2ZXn8EJo4o5BV9iaIibAK4jD4s/640?wx_fmt=png&from=appmsg "")  
  
  
这里eval执行的内容是通过jobExecutionContext这个调度任务中获取的  
  
从JobExecutionContext  
（任务执行上下文）中获取JobDataMap  
接着取出key等于script的字符串  
  
  
那么我们就得找下写入点，BeanShellScriptJob.execute继承了Job在启动调度任务的时候会自动触发  
  
  
定位到SchedulerManager.java的init方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTojIVSLAUhGljKu7DAibf0klLicxLhcHbFibJBA9h7vibJB9qyRMQxMa8w8EYu0Mt4XKiaGsUd3txjhDWiagiapOZHFIqib12aAmzF8JV0/640?wx_fmt=png&from=appmsg "")  
  
  
如果className等于com.redmoon.oa.job.BeanShellScriptJob，就从jud取出data_map，put进getJobDataMap中，这里可以看下是从哪个表拿出来的，寻找JobUnitDb的配置  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTq4NwuSGb38vzGOokq6wic562ibC8SbsicRemfsPbR6Vic8T4D7KbDReULCsmjazldGiaMoQ87VLkmxEzNI0qg3FibYuVBGfTDiaeQktI/640?wx_fmt=png&from=appmsg "")  
  
  
那么我们现在就找在哪里插入数据的就行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqwJibWatKsFSib9b3RtVvCRmUyxGzC6EY5ib4NibkyrAdnGk9s6ISTgzfvtIgWicnIJzW79z2rOylSm0zerjBhH548v04QYcL9GYPE/640?wx_fmt=png&from=appmsg "")  
  
  
定位到scheduler_add_script.jsp  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fQp8MibWmUTpzibceDYI1mR0O0eM77wED1W56gvibgLziaumSTVeDmHjkeZCpx58PRIDzDgvW0ic0eibeabcdVRzgSkTIa3LyFasKJ6eAYygWYozQ/640?wx_fmt=png&from=appmsg "")  
  
  
调用这里没看到直接的接收参数的点，那么应该是qom.create，跟进  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTqI7Ow6DhyNMvQriaAHiaWj9uOgic3ibNNDYF0AM46xtiaFsUPm9rmynToMQ2lM8WjCW5r8h2B1iaLYgbGiaviaBebUmhSNqaaOZe8u3Ps/640?wx_fmt=png&from=appmsg "")  
  
  
根据我们xml前面看到的结构提取参数，构造语句写入数据库，那么我们直接构造就行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUToXY7ibvdWCvtQPvzVmibpufIGSCPGKmZUom1ibVDiasica2COUic2hviaCTNc8lB02ruxTcz6wtx4Q82Un50qV7rUK0Z6ud75vb4bxeU/640?wx_fmt=png&from=appmsg "")  
  
  
这一处要理员权限校验，得登录  
  
主要就是data_map和job_class  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTpRn0gugWiaqUyuoibXd8aeQhjFnOcKDeribxlwOhOcfQ9iaT4LRWPtiaMK1rgAjquZCDuJicuKhxmibCbnSiaVpvBDqJHtOlVcP2y5EhU/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fQp8MibWmUTp97P5y7bDn7aHbPhV6lmchammBDqax8jNibqBiafdNDjza6FtmqOjkPSpTnVo8EtWbmfdXMpv9OYqox38vjHUwNwOnib56LcOsaw/640?wx_fmt=png&from=appmsg "")  
  
  
自动调用  
  
# 最后  
  
  
有其它问题或者对文章内容有疑问的，可以加作者微信，加交流群的话备注"交流群"  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPnw8V3reibBVvkUk8M8daLKaoQta5zql2B22KmutaD8Awz2JTpIDfsCicD1mamuWGibq70002YX2Duvw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
公众号培训广告，有需要可联系(混口饭吃)  
  
  
新一期课程介绍：[菜狗安全《代码审计培训》2026年新征程](https://mp.weixin.qq.com/s?__biz=Mzg4MzkwNzI1OQ==&mid=2247488001&idx=1&sn=17d3083967db3aa5a9314a0cac04ffbd&scene=21#wechat_redirect)  
  
  
  
JAVA审计闭源专题课表  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmBqWUJLPFFmVxeMQJKj8N6oKpmQDaJ5FAsiaaomKzraI6aKWpGcF1c1vMFsiaqUFDCDbz3RZkL87Rg/640?wx_fmt=other&from=appmsg "")  
  
内容对比上一期会更细点，并且主要围绕企业闭源项目，  
如果说上一期是CVE随便刷，那么这一轮就是奔着CNVD，CNNVD去了  
  
课程内容涵盖  
  
1、基础篇  
- 通用学习路线与指南  
  
- 这个会作为我们新一期课程的第一讲，主要是为师傅们梳理学习的思路，建立一套“以业务为核心，架构为先导”的底层审计逻辑，从而具备审任何语言都能快速上手的通杀能力  
  
- 漏洞的本质  
  
- 审计审计，我们审计的主要是漏洞，那么对于漏洞的理解就显得尤为重要，从漏洞产生的本质出发，理解漏洞，吃透漏洞，会大大提升对于不同类型漏洞的审计关注点，大大提升审计效率  
  
- 闭源项目常见架构审计差异与反编译  
  
- 讲解常见闭源项目的不同架构差异，以及源码到手后的准备工作  
  
- 不同架构项目路由传参以及鉴权装配模式  
  
- 讲解常见闭源项目的不同架构路由配置以及接口构造与参数传递，以及框架特性导致的鉴权装配模式差异  
  
- JAVAweb开发  
  
- 这一块内容是分割在每节漏洞审计的前置部分，不同于市面上的常规开发课程，通过实际业务分析漏洞产生原因，在实战案例前就学会如何挖漏洞！！！  
  
2、鉴权分析  
- 讲解java项目中常见的鉴权方法  
  
- 不同鉴权方式的路由白名单配置  
  
- 以及实战如何绕过鉴权  
  
- 实战情况中存在鉴权绕过的缺陷逻辑  
  
3、常见漏洞审计  
- SQL注入挖掘  
  
- 文件操作类挖掘  
  
- 组件安全审计  
  
- SSRF审计  
  
- XXE审计  
  
- RCE审计篇  
  
- 越权类挖掘  
  
- ......  
  
4、审计番外内容  
- ......  
  
这个第一期上过挺多次了，主要还是根据学员的需求来加的  
  
5、企业源码审计实战  
  
选取国内某OA，某ERP，某管理系统，等企业级源码，  
甚至是我实战中遇到的企业泄露源码(脱敏处理后的)，  
从反编译->项目架构分析->鉴权分析->漏洞审计的完整流程  
，并且每节都有  
0day挖掘案例  
，手把手教学，避免一看就会，一上手就废。  
  
这个模块第一期上了17次直播，也是给学员听爽了，也是修改为常驻，慢慢上  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPniagcIZAYHTC7iaCicMOYZzfXfqemDa4ribepf6koLxkhHA5KzVEqTXZNSbTaKHY0w8vANCdrzpLH4Ag/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
秉承节节有0Day，节节挖0Day，  
从源码解压到漏洞审计完整流程，现场手把手教学审0day  
  
学员内部福利  
  
1、国内几个源码站会员：9k9k，刀客，小蚂蚁，优选源码，源码庄，狗凯等，如果有需要其他源码站会员可联系我，我看情况开通  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPnE2Zdjia0QKELGfWiaoiciaiatAbZla7dXIj0iaVqzgwsN412Z9kUc9RkCMrxf8jUmUNyG10oYFRWHzdXg/640?wx_fmt=png&from=appmsg&watermark=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPnE2Zdjia0QKELGfWiaoiciaiatALQErjEWvBibj0nG76UoEa8UMQb1FngdhKHqN4wUW0sPMR4rRzX1zFXg/640?wx_fmt=png&from=appmsg&watermark=1 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GRY3mPHXFWqg1ibX6bcsIPZKVCJiaablo4nTvoQwMgnDuiaZISiaFn4dib3A/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
2、内部代码审计文档库加配套对应源码(持续更新中)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9Gd7fmibA0VDyw4df0gV0jDbv4Y89wOEuFLCMvQcwYM6zR59vYjp7F0IA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPniagcIZAYHTC7iaCicMOYZzfX3eSqtXQcEmVvlibPhm1koMOpK5pAAFbwaDINLvZVWcMnwQF9MSmSohQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPniagcIZAYHTC7iaCicMOYZzfXuT5qABPeShhbomoRribicjEriarHBFm4bJ7tMiaicibiaKC5ZBoxsWQiac4vJw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPniagcIZAYHTC7iaCicMOYZzfX2awdbNuDbiatwqbV68ZqFzAVFsyVbARlUbwicBEu6xeHTyGQ3gcdNhhA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8 "")  
  
每篇都是从  
项目架构分析->鉴权分析->漏洞审计，以思路为主，并非简单漏洞披露，源码类型广  
  
3、一些源码资源  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9G4e8KmLJRYwfmaBwlWJ7lDlEnFHvcetN3Wu721l9ott9m0aaVMvkbTg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GPzXibSlhqJwekkdIqGiaKXYChpibMfpRKXqfuArDLEjqjpZklPictmVtJg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10 "")  
  
4、不定期抽奖和布置考核任务给予奖品，  
形成玩中学，学中玩的学习氛围(太多了随便放两张)  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPkDmfleeBabXC5WBrdP5dWyfO6BIjNKeeOgzBmZYyVRNYUMeCFAC0HCW0YIl3GEdjBzGS8dwTRn9w/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPkDmfleeBabXC5WBrdP5dWyAI1WzsFk6gxkxeCUYMA1iaSUXo8K9eEznb7GAkUcBwoQwV6uDOjkuZg/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPkDmfleeBabXC5WBrdP5dWyO7w8ljfZqlicqHzsaOWrF7mjQbRYYcxsfjcaF9AgjqNPLAT8RB8mpvg/640?wx_fmt=jpeg&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPm2victuon7KLX2OjcPePUaibsmcAe0WNn6csA0K39WicqEq0icQEULev9FvNZKkZKfk8LIKkoMUbxH3Q/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=52 "")  
  
  
考核靶场  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPlst1qDPq3xpv50FmdZLYwwxicXKwOVeGiayNok2Bf2HHnudl9Ke76ibwn03O5HIDqeaaaubzOdzfyJw/640?wx_fmt=png&from=appmsg&randomid=nagy1kgx&watermark=1&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPlst1qDPq3xpv50FmdZLYwwYbsoVI4RVRaKia8WgGA1HSQZdKNTNCv0RteTx3JS6AvysO0PEdLbCPw/640?wx_fmt=png&from=appmsg&randomid=5cho2ban&watermark=1&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
4、部分项目(代码审计，渗透测试，讲师，HVV等等)优先推送  
  
5、更多内容筹备中。。。  
  
往期精彩课程(也可以看)：  
  
代码审计第一期(JAVA专题)[菜狗安全《代码审计培训》双十一优惠开启：手把手0day挖掘教学](https://mp.weixin.qq.com/s?__biz=Mzg4MzkwNzI1OQ==&mid=2247487578&idx=1&sn=a21fbe51597fd84452661e43c7461c7a&scene=21#wechat_redirect)  
  
  
价格  
  
哎呀，要不要涨价呢，我给出的回答是，短期内不考虑，目前课程原价依旧  
1299  
，  
一次报名后面可以一直听不会有二次收费  
，如果是学生确实没啥💴就看B站公开课吧，入门绝对够，付费课有能力再考虑  
  
暂时我也想不到其它问题了，如果有其他疑问可以在群里问，或者私信我  
  
心动不如行动  
  
有需要或者有问题可以加微信，备注“培训”  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPlst1qDPq3xpv50FmdZLYwwCVELHyicsRo53KPRMsv6Y8tO03tHbEhRYia4TO7zwib7Eia8vBgSvofQcQ/640?wx_fmt=jpeg&from=appmsg&watermark=1 "")  
  
学员反馈  
  
放几张意思下，  
还有  
一堆懒得找了  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GEU6ZU7rRwfSk7uv1tmHibMRG1YCnbI5JXq4RyGa9b4kGuSN6UFLk55A/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GAmJ72tKUZPlToepSMxTThWNxzLVGwUGdzD3OJuexAZnIkYpcm3NxKg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GRZU9Gk6pIev7veGSaonOEC9TSartI7UWNaIgYaShTAhqdqknIBjR5A/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GKlVTSukSrGyYnEeqQdLfM3JY7WNLRuI5rZcGiao0c4Zl45AiaXxJ8Uicw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GicL4ibIudLLfWXCgjCxZDBDfOokFL8iaxjHKnOwXJFns4D8sBEjicVib5bg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GOCuIy6JsYmGUQJ6nmIkRy7tnkDF7XZ75qSibA0Tz7TTfdiaJaBdXGwgA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GE2ONUALIYbNZuBFEx7bSvJGMrYD5pgZK5pWcXpyZa5KW6YicaqQFkNw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QtaE6uFmibPmHG1XrBuPOnQ0h6pfzqQ9GI651mFDDzpYfIzWQMeKI1BUPaGibS5MUcXOAjRKWWGDgVU8SEANtHSQ/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25 "")  
  
  
  
