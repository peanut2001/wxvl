#  记一次某EIS办公平台0day挖掘审计过程  
 黑白之道   2026-03-16 02:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
原文首发在：先知社区：  
  
https://xz.aliyun.com/news/90808  
  
环境搭建  
  
机缘巧合下从好兄弟那拿套源码，好久没审计有点生疏了，搭个环境练练手  
  
虚拟机选择win2012，在Internet信息服务（IIS）上新建网站，设置站点名称和安装路径  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZCogBKvpATqfm2b4GwN2AsicqL8G2jHtsD2153LO7UFgqjnWmx12jOFw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=0 "")  
  
  
在应用程序池中找到对应站点程序池，托管管道模式默认为集成，将其修改为经典模式.NET  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZnHUhgQDezkaiaia7Fpav7U2vXRPG9up4tPPqZqickBhTteqppLnWJQOCA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
  
新建数据库，与web.config  
连接保持一致即可  
  
<table><tbody><tr style="height: 33px;"><td data-colwidth="750" width="750" style="border: 1px solid #d9d9d9;"><pre data-language="plain" style="border: 1px solid #e8e8e8;border-radius: 2px;background: #f9f9f9;padding: 16px;font-size: 13px;color: #595959;"><code><span leaf="">set DBNAME=EIS</span><span leaf=""><br/></span><span leaf="">set SQLUSER=sa</span><span leaf=""><br/></span><span leaf="">set SQLPWD=password01!</span><span leaf=""><br/></span><span leaf="">set SQLSERVER=127.0.0.1,1433</span><span leaf=""><br/></span><span leaf=""><br/></span><span leaf=""> &lt;connectionStrings&gt;</span><span leaf=""><br/></span><span leaf="">        &lt;add name=&#34;&#34; connectionString=&#34;Data Source=.\SQLEXPRESS;User ID=sa;Password=password01!;Initial Catalog=EIS;Connection Timeout=30;Connect Retry Count=3;Connect Retry Interval=10;Pooling=true;Min Pool Size=0;Max Pool Size=100&#34; providerName=&#34;System.Data.SqlClient&#34; /&gt;</span><span leaf=""><br/></span><span leaf="">  &lt;/connectionStrings&gt;</span></code></pre></td></tr></tbody></table>  
  
按顺序依次导入sql文件  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZUgcLHAKusUqQnKibtp1MgGWibibsQ4hKhX7ERfnhhjMrCIJuQbhcovOug/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2 "")  
  
### Patch产品授权  
  
该产品是需要产品授权的，访问login.aspx  
会提示无效或过期  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZOeUAcKffCwtUmBXtx0MD43GbDEeKQ0wz01wKpNDbtmOZbJLyibNVVEg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3 "")  
#### 逆向破解算法，模拟生成授权licsense  
### 应用启动时验证（CheckLicense）  
  
位置  
:EkpBaseGlobal.Application_Start()  
→EkpGlobal.CheckLicense()  
  
流程  
:  
1. 读取文件授权  
(Checker.p_GetLicense()  
)  
  
- 读取Bin/Landray.lic  
文件  
  
- 获取CPU ID和MAC地址  
  
- 解密授权文件  
  
- 解析授权信息（10个字段）  
  
- 提取FullName  
  
1. 读取数据库授权  
  
- 从Mekp_EISProductInfo  
表读取LicenseKey  
  
- 使用相同的密钥和IV解密  
  
- 解析授权信息（2个字段：过期时间;FullName）  
  
1. 验证授权  
  
- 比较文件授权和数据库授权中的FullName是否一致  
  
- 如果是试用版，检查过期时间（逻辑：DateTime.Now < expiration  
→ 返回false）  
  
- 如果验证通过，将授权信息存储到Application  
对象中  
  
1. 更新数据库授权  
（如果是试用版）  
  
- 将数据库授权更新为当前时间 + FullName  
  
采用加密算法：3DES (TripleDES)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZC462r2hFOY1P5GcUnZeI9nibTDWQ8laJh4b9q0fTw940Odh5gGmXGEA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
- 文件授权lic  
：  
  
读取文件并解密（密钥：CPU + "xxxxxxx20800"  
，IV：MAC地址）  
  
解析10个字段，关键字段：array[3] = "DeptName|FullName  
存入lisenceInfo.FullName  
- 时间校验  
：if (DateTime.Now < result) return false  
，如果当前时间 < 过期时间，返回false（验证失败）  
  
- FullName匹配  
：lisenceInfo.FullName  
必须与数据库完全一致  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZfFUleQ2ebHWJC5X9xia8WibF0XwbW10k9MicY7MqKtVdXSrvyCKqeQm7w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
  
根据 CPU MAC 生成  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZIEM8tJIlo1ebzvtWcrBlYbOtwxpWZY8m7TvLjU3KBk36icY0fXUDv4w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6 "")  
#### 注释鉴权代码重编译  
  
如果觉得第一种方法比较复杂，也可以选择第二种简单粗暴的方法，直接注释掉核心鉴权代码  
  
根据报错的关键字定位相关的文件，发现有以下这些文件参与鉴权，这些方法都来源于yard.Framework.dll  
- EkpGlobal.CheckLicense() - 核心授权检查  
  
- EkpPage.OnInit() - 页面初始化检查  
  
- EkpPage.Page_Load() - 页面加载检查  
  
- EkpUserControl.Page_Load() - 用户控件检查  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZdx8os8wibr4FbY3D0qAK3MGoYlpleWu47HYoFm55u5GY7E2KMnRnic1A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7 "")  
  
因此我们可以使用dnspy导入dll，再导出工程到vs里面进行重编译  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZqicWSVysgeSd94YsWq6cQLjHBGhT8q7hXviaEbHNVJnh6DytaW1Pp8Jw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8 "")  
  
  
成功通过授权校验，访问系统首页  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZO4J5zoSGciaD4V81p5Via9WviaY2GRrr5fu8VdOKulicE4h3libIuEaoHeQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9 "")  
  
### web.config配置分析  
  
根据web.config  
分析，以下路径配置为允许所有用户访问（<allow users="*" />  
）  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZgTabgRFlPCU7GMQbwL5GCutSz2EO7RAK6h2I563GRNuSsF3Ql7iaEicA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10 "")  
  
  
（部分接口关键字替换了）整理如下：  
  
<table><tbody><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">配置路径</span></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">访问路径</span></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">说明</span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">&lt;location path=&#34;XX&#34;&gt;</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">/XX/*.asmx</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">WebService接口目录，所有ASMX文件可匿名访问</span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">&lt;location path=&#34;aaa&#34;&gt;</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">/aaa/*.aspx</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">该模块目录下所有aspx文件可匿名访问</span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">&lt;location path=&#34;third&#34;&gt;</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">/third/*.aspx</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">第三方集成目录</span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">&lt;location path=&#34;Global/Pages/CheckPage&#34;&gt;</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">/Global/Pages/CheckPage/*.aspx</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">检查页面目录</span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">&lt;location path=&#34;Services/MobileDown.aspx&#34;&gt;</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><span leaf="">/Services/MobileDown.aspx</span></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid rgb(217, 217, 217);"><p style="margin: 0;padding: 0;min-height: 24px;"><span leaf="">移动端下载接口</span></p></td></tr></tbody></table>  
### 漏洞分析  
#### 前台SSRF  
- 文  
件路径  
:  
  
- bin/yard.UI.Integration/yard.UI.Integration.third.template/Service.cs  
- 方法  
:PostResponse  
third目录配置允许匿名访问  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZfib4cNibc6k1NoOKqhNgxWTDX5b1kRXko1YLqLQ52x8USOmFFPwJYQVw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11 "")  
  
  
- link参数直接拼接  
:base.Request["link"]  
直接拼接到URL中，未进行任何验证  
  
- 无URL白名单  
: 未限制可访问的URL范围，虽然固定使用http://  
，但可以通过传入link  
参数控制造成SSRF  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZ7KtI7wXcwsPQiaStIVg23MAf678za6NLqV3Dr3FozNwRJ9fazXThGicw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12 "")  
  
  
#### 前台down.aspx SQL注入  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZ1RSpZxQxgCC3EbE09as1IKuVAFJtVCsFBQibNibTloWqeTQwE2kNMXbg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZFAVAqKzn5D4KLumv5VqsPSYM1ibKJHZI7EEHWc5Q1enmq7slEOvKgKg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14 "")  
#### 前台Notify.asmx SQL注入  
- 文件路径  
  
- :bin/yard.WebService/yard.WebService.WS.Notify/Notify.cs  
  
- LoginName参数直接拼接  
:person.LoginName  
直接拼接到SQL查询中  
  
<table><tbody><tr style="height: 33px;"><td data-colwidth="750" width="750" style="border: 1px solid #d9d9d9;"><pre data-language="plain" style="border: 1px solid #e8e8e8;border-radius: 2px;background: #f9f9f9;padding: 16px;font-size: 13px;color: #595959;"><code><span leaf="">[WebMethod]</span><span leaf=""><br/></span><span leaf="">public NotifyResult getTodo(string targets, int type, string otherCond, int rowSize, int pageNo)</span><span leaf=""><br/></span><span leaf="">{</span><span leaf=""><br/></span><span leaf="">    Person person = JsonConvert.DeserializeObject&lt;Person&gt;(targets);</span><span leaf=""><br/></span><span leaf="">    if (!string.IsNullOrEmpty(person.LoginName))</span><span leaf=""><br/></span><span leaf="">    {</span><span leaf=""><br/></span><span leaf="">        // SQL注入点: LoginName参数直接拼接</span><span leaf=""><br/></span><span leaf="">        string oneStrValue = yard.DataAccess.DataAccess.GetOneStrValue(</span><span leaf=""><br/></span><span leaf="">            $&#34;SELECT id FROM FI_ORG_EMP where account=N&#39;{person.LoginName}&#39;&#34;);</span><span leaf=""><br/></span><span leaf="">        // ...</span><span leaf=""><br/></span><span leaf="">    }</span><span leaf=""><br/></span><span leaf="">}</span></code></pre></td></tr></tbody></table>  
  
构造请求，通过xp_cmdshell写入文件1.txt  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZzIdJSHJHNDaRHiakK9KmtcETF8ugKrGA1mofWaAlVIicr6ldzoxFZDzw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15 "")  
  
#### 前台任意用户添加  
- 文件路  
  
- 径  
:bin/yard.WebService/yard.WebService.WS/UserInfo.cs  
  
- User  
方法使用[WebMethod]  
标记，WS  
目录被配置为允许所有用户访问，该方法无权限校验可直接执行数据库插入操作  
  
- 继承于WebService可直接传入账号密码等信息新建用户，首先在数据库中查询是否存在该⽤户， 如果不存在就创建  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZBjM4ic29qCqcfBzljD1lRRTlicWDUcqdIzpLxvibeDjl1T3M9P0MNdLOA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZZLBzwWS0EuNsAC6KUfcDdKHNJibMxAia6Onn6n0vZqVLORINRXo4VR0Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17 "")  
  
  
FI_ORG_EMP  
为员工主表，可看到成功新建用户  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZPk2VMKCxpk8Qa2lCLGqPcQNFtahqTbEUJWRicsiaLhiagMtJwaHCo1y7w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18 "")  
  
#### 后台UploadLogImg.aspx任意文件上传  
  
文件bin\yard.Admin.UI\yard.Admin.UIUploadLogImg.cs  
提供了saveBg()  
和saveLogo()  
两个上传的方法  
  
string text = base.Server.MapPath  
这个地方路径不可控，默认会写到/App_Themes/Login  
下面，文件名为日期命名  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZoxibJWVztR5icqsevNrFmxf3aEZscFEwrJU7L2icYSrNTr3vCrfSFNbbg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=19 "")  
  
  
构造方法上传  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZ90gGbk9EdibV0roFKkFdqIjibodM1ZJYsDFdFtgDIwxriaazwiaf9iaibd0g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=20 "")  
  
  
/App_Themes/Login  
不允许，因此这个上传无法shell  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZDpwyA4XqIcqIstSvn9G28FELq0ColbiaDq31UWhjh8pJYpGzENFKUAw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=21 "")  
  
#### 后台 bulkinsert_data.aspx任意文件上传  
  
但是不要灰心，这个点找不到就找下一个，继续搜SaveAs(filename)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZrpgM5mhiaUQGJWWm0kuzIoIngKDvwicR93ft1cMxNNbjymdWTJuWUxfA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=22 "")  
  
- 这里还有两个值是必须的，__VIEWSTATE  
和__VIEWSTATEGENERATOR  
  
- 当用户首次访问/XX/bulkinsert_data.aspx?id=1  
时，页面加载 -Page_Load  
方法执行，所有服务器控件初始化，使用 Base64 编码，生成__VIEWSTATE  
和__VIEWSTATEGENERATOR  
值，ASP.NET 会验证，没有ViewState  
会导致Invalid ViewState  
错误，控件状态无法恢复  
  
<table><tbody><tr style="height: 33px;"><td data-colwidth="750" width="750" style="border: 1px solid #d9d9d9;"><pre data-language="plain" style="border: 1px solid #e8e8e8;border-radius: 2px;background: #f9f9f9;padding: 16px;font-size: 13px;color: #595959;"><code><span leaf="">string text = &#34;/files/&#34;;  // 固定基础路径</span><span leaf=""><br/></span><span leaf="">string fileName = tpfile.PostedFile.FileName;  // 用户输入</span><span leaf=""><br/></span><span leaf="">int num = fileName.LastIndexOf(&#34;\\&#34;);  // 查找最后一个反斜杠</span><span leaf=""><br/></span><span leaf="">string empty = string.Empty;</span><span leaf=""><br/></span><span leaf="">empty = ((num &lt;= 0) ? (&#34;\\&#34; + fileName) : fileName.Substring(num));  </span><span leaf=""><br/></span><span leaf="">tpfile.PostedFile.SaveAs(base.Server.MapPath(text + empty));</span></code></pre></td></tr></tbody></table>  
  
可进行目录穿越，代码会取  
最后一个\  
之后的部分  
，但是正斜杠可以正常绕过  
- ..\third\shell.aspx  
→empty = "shell.aspx"  
❌  
  
- ../third/shell.aspx  
→empty = "third/shell.aspx"  
✅  
️  
  
结合web.config  
，可写到third  
路径下  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTToedQqibxQ4TbFcDM1m9D8BZTxSHJficxTZ2ia6BWoHoTiamcpo3A5vG1UzHoTDgyArSL4SaWmzOMibJvA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=23 "")  
  
> **文章来源：亿人安全**  
  
  
  
黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！  
  
如侵权请私聊我们删文  
  
  
**END**  
  
  
