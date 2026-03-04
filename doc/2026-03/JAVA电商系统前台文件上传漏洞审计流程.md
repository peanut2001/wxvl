#  JAVA电商系统前台文件上传漏洞审计流程  
原创 学员投稿
                    学员投稿  进击安全   2026-03-04 01:01  
  
# 免责申明本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。  
## 一、前言  
  
         
 前几天学员找我一起审计一个电商系统，记录一下最后成功为审计出来前台RCE漏洞的流程。  
  
二、鉴权分析  
      
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQsgCEIbCQsAjoic1icEFMuBS3QULyhrS8m01GBXrlGvuPrVKR7h2CgRJYa2VicVj7vGro5yxooIFr6sy5YShuuIMMRTakeaicEzzk/640?wx_fmt=png&from=appmsg "")  
  
首先进行分析对应的拦截器。  
  
```
@Configuration
public class CustomWebMvcConfigurerAdapter extends WebMvcConfigurerAdapter {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        // 拦截所有 /manage/** 路径的请求
        registry.addInterceptor(securityHandlerInterceptor())
                .addPathPatterns("/manage/**");
    }
}
```  
  
  
这里可以看到拦截器的拦截路径为/manage/下的路径。  
  
查看对应的拦截器代码。  
```
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
    // 1. 从 Cookie 获取 Token
    String token = getTokenFromCookie(request);
    // 2. Token 不存在则跳转登录页
    if (StringUtils.isBlank(token)) {
        request.getRequestDispatcher(Constant.LOGIN_URL).forward(request, response);
        return false;
    }
    // 3. 检查是否为豁免路径
    String path = request.getServletPath();
    for (String url : IGNORE_URI) {
        if (url.contains(path)) {
            return true;
        }
    }
    // 4. 从 Redis 获取 Session
    String key = "session:" + token;
    if (redisUtil.exists(key)) {
        Map
 session = (Map) redisUtil.get(key);
        List
 urlList = (List) session.get(Constant.URLS);
        // 5. 验证 URL 权限
        if (urlList.contains(path)) {
            return true;
        }
    }
    // 6. 无权限则跳转403页面
    request.getRequestDispatcher(Constant.UNAUTHORIZED_URL).forward(request, response);
    return false;
}
```  
  
这里其实没有进行细看是否存在相关的鉴权绕过，因为拦截器主要是针对路径  
/manage/**路径下的信息，所以这里直接先分析  
/manage/**路径之外的信息就好。  
  
三、前台文件上传  
  
这里进行搜索  
MultiparFile文件上传常用的类，来进行定位高风险漏洞触发点，寻找文件上传功能。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTMfjwLficP2DGjzrNN8ribkYYX3Ny4S97HXg1nziazQtfGKCoTeickYLhWe0OkXR6iaavklMdzkMMANCkvQaibu8PwiabxT62DIwqSOo/640?wx_fmt=png&from=appmsg "")  
  
上述文件当中是user开头，不会受到拦截器的影响，这里继续往下走。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQM1lria5Iu6RRPET2VxbjkuIwyYhBtxNibEibJDedr7WCU8GPfuvfL6scOIOBCyHzCOOZyDlGUUNRRoWia1b836QvngcCmrEBTHyA/640?wx_fmt=png&from=appmsg "")  
  
在这里进行获取到文件名称直接进行截断后缀，然后进行时间戳命名，上传到了/www/server/uploadFile文件夹当中，并未对相关的后缀进行黑白名单判断，而是直接上传。  
  
数据包如下：  
```
POST /user/pictureUpload HTTP/1.1
Host: x
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarym6T8Db2zfHB7BV2t
Content-Length: 165

------WebKitFormBoundarym6T8Db2zfHB7BV2t
Content-Disposition: form-data; name="businessLicense"; filename="1.jpg"

<data>
------WebKitFormBoundarym6T8Db2zfHB7BV2t--
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQEjHLibicZWWdL2eJMKYP5na85g5LLH2Z7AN7qRQCc5QbaKmLsJ4xKVmEQiajhwEpU5m97e2kF6j0HkLVT3ZopEFa1nPiaNjzRzOo/640?wx_fmt=png&from=appmsg "")  
  
这里没有直接上传shell，但是学员成功最后成功获取到了webshell权限。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQprGb0YfiayljeibR574R1Gp8dK7EF4pY3S32MmrO5AsQTEG2OibCbgaWNbo3PlWtBOVrPDNxicmehnfkEd16o00aibFYaCpbrPOdY/640?wx_fmt=png&from=appmsg "")  
  
**广告区域**  
  
  
    目前第四期进阶课程已经开始，课表如下：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQsqa0icLsG4CPdKsuicQ6GMJ4VUySmEJ2icANSx4qJktASDbEwyOvXdZNDiaEAdEbDP9s4g5rPmeAnfR8LhAym8UV6cztDX40Mrn4/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16 "")  
  
同时报名第四期基础课程同样可看，课表如下：  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTBGDfegoyISgcodQYrfiaQhs3WVY3HicYxj76VUbErvYs7YgUlDk6S3RhryRicB0v1rTlGALH4j7KGBEAVFRrSDsmLxTqC9MlWWM/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
  
同时具备内部资料以及靶场相关福利，想要了解的师傅可以冲了。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSCQaJynTsmjlSiaJaRWYkWrB8GvTO8wtzFl6TXUjUaujY2w5q9PMvJ1yVKprrMhFYOSxwmia5MibKZZoJOT3n7iaicFvU8spUHJyds/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSUMRWBDzF4da2Y1Gib79Uf9crOz1wrQibIB6kuIS72icMlekKUrG30oTWuUIcVHH974bz8TSDFJfnq0b12ia0H7ZfXZA5yM3SGwJ8/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSO9eN2pAA3hTSORcHlauF9rJ8QKHjBdGIR8UgCmGHWDKJJ7HDGXGejBMUk9FyMWp4KwGXQUbuQ1ILdvpRGoD5bDEXicMJ5kOh4/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23 "")  
  
  
  
  
  
  
  
