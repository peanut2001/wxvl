#  Apache配置以及漏洞  
原创 信安路漫漫
                    信安路漫漫  信安路漫漫   2026-01-22 01:00  
  
# 前言  
  
apache使用比较广泛的web服务器，以前也看过一些关于apche的漏洞，但是比较 零散，本文就来重新总结一下apache可能存在的漏洞以及配置。  
# Apache简介  
  
Apache 是世界使用排名第一的 Web 服务器软件。  
  
它可以运行在几乎所有广泛使用的计算机平台上，由于其跨平台和安全性被广泛使用，是最流行的 Web 服务器端软件之一。  
  
它快速、可靠并且可通过简单的 API 扩充，将 Perl/Python 等解释器编译到服务器中。  
# 安装  
  
通过yum方式安装：yum install httpd httpd-tools  
  
查看服务是否开启：service httpd status  
# 默认配置  
  
/etc/httpd/conf/httpd.conf    Apache默认配置文件  
  
/var/www/html/        Apache的默认根目录  
  
查找apache配置文件的方式：rpm -qc httpd  
# 配置文件详解  
```
# 服务器类型：独立模式（默认）
#作用‌：定义Apache运行模式。现代系统通常使用standalone，由httpd进程直接处理请求
ServerType standalone
# 服务器根目录（配置文件和日志存放位置）
ServerRoot "/etc/httpd"
# 存储主进程ID的文件
PidFile "run/httpd.pid"
# 服务器超时时间（秒）
Timeout 60
# 启用Keep-Alive（复用TCP连接）
KeepAlive On
# 每连接最大请求数
MaxKeepAliveRequests 100
# Keep-Alive超时时间（秒）
KeepAliveTimeout 15
# 监听端口（默认80）
Listen 80
# 加载核心模块（如重写、SSL）
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule ssl_module modules/mod_ssl.so
# 运行Apache的用户和组
User apache
Group apache
# 错误日志路径和级别
ErrorLog "logs/error_log"
LogLevel warn
# 访问日志路径和格式
CustomLog "logs/access_log" combined
# 默认文档根目录
<Directory />
    Options FollowSymLinks
    AllowOverride None
    Require all denied    #拒绝所有访问
    #require all granted    #允许所有访问 
</Directory>
#用于处理http的mime类型
<IfModule mime_module>                          
    TypesConfig /etc/mime.types
    AddType application/x-compress .Z
    AddType application/x-gzip .gz .tgz
    AddType text/html .shtml
    AddOutputFilter INCLUDES .shtml
</IfModule>
# 主站点文档根目录
#<Directory>：针对特定目录设置权限。
#Options：控制目录行为（如Indexes显示目录列表，FollowSymLinks允许符号链接）。
#AllowOverride：允许.htaccess覆盖配置（All表示允许所有指令）。
#Require：基于IP或主机名限制访问（如all granted允许所有请求）。
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>
# 默认虚拟主机（处理所有请求）
#定义多个网站，每个网站可独立配置域名、文档根目录和日志。
#*:80表示监听所有IP的80端口。
<VirtualHost *:80>
    ServerAdmin webmaster@example.com
    DocumentRoot "/var/www/html"
    ServerName example.com
    ErrorLog "logs/example_error.log"
    CustomLog "logs/example_access.log" combined
</VirtualHost>
# 防止文件解析漏洞
<FilesMatch "\.(php|php3|php4|php5)\.">
    SetHandler application/octet-stream
</FilesMatch>
```  
#   
# Apache多后缀解析漏洞  
## 后缀解析的原理  
  
运维人员配置了某个后缀的优先级为最高，只要出现了指定的后缀，不管文件是什么类型的都会被当作那个指定的文件来解析；  
  
如果运维人员给.php后缀的文件添加了处理程序 AddHandler application/x-httpd-php .php 那么在有多个后缀的情况下，只要文件含有.php后缀那么该文件就会被识别为PHP文件进行解析。  
  
如：index.php.jpeg   这个文件在前端会被当做图片的格式上传成功，但上传到服务器里会当做php文件来解析  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1objo7qy0vDncxSftWToohXWl1pzycH56dwveQx1mRtpclbmPdIVb0Vw/640?wx_fmt=png&from=appmsg "")  
  
如下图，上传的hhh.php.jpeg会被当成php文件进行解析  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1oPCvVIoMkMUUOEOicrm2HFYXYwLerfgrFtK0GiaZiaSD3TG2QqPvKLrOaw/640?wx_fmt=png&from=appmsg "")  
## 修复方式  
```
1、使用SetHandler,写好正则，只允许以.php后缀的文件解析
<FileMatch ".+\.php$">
SetHandler application/x-httpd-php
</FileMatch>
2、禁止.php这样的文件执行
<FileMatch ".+\.ph(p[3457]?|t|tml)\.">
Require all denied
</FileMatch>
```  
  
# Apache换行解析漏洞复现（CVE-2017- 15715）  
## 原理  
  
在Apache 2.4.0-2.4.29当中存在，在上述版本当中，Apache开启了正则表达式的多行属性，在匹配.php$文件时除了会匹配到的.php结尾的文件还会匹配到.php\0a结尾的文件，在业务环境中.php结尾的文件会交由PHP解释器执行，所以黑客可以上传.php\0a结尾对的文件来绕过上传限制，并且让文件中的内容按照PHP代码来执行  
  
通过在后缀结尾添加换行符来绕过黑名单的检测  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1ogmUNIHJYibl1iaR9icxfoSlTc6BBdhUJofyHqJgVrU5uGTliaCmppaAFqg/640?wx_fmt=png&from=appmsg "")  
# CVE-2021-41773 漏洞复现  
## 原理  
  
Apache httpd Server 2.4.49 版本引入了一个新的函数，在对路径参数进行规范化时处理不当，当检测到路径中存在%字符时，如果紧跟的2个字符是十六进制字符，就会进行url解码，将其转换成标准字符，如%2e->.，转换完成后会判断是否存在../。如果路径中 存在%2e./形式，就会检测到，但是出现.%2e/这种形式时，就不会检测到，原因是在遍历到第一个.字符 时，此时检测到后面的两个字符是%2而不是./，就不会把它当作路径穿越符处理，因此可以使用.%2e/或 者%2e%2e绕过对路径穿越符的检测。  
```
/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1obqiaicT0ibIZjtibdiakjELialrgmqeSBSyWIATANDsUicb1VR8ywKhLZX2Bg/640?wx_fmt=png&from=appmsg "")  
  
在修复该漏洞后，又出现了一个CVE-2021-42013，通过编码还可以可以绕过。源于对 CVE-2021-41773 的修复不充分。攻击者可通过特殊编码绕过路径规范化机制，读取任意文件或执行系统命令  
  
POC如下：  
```
/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd
```  
## 修复方案  
  
①更新版本，打补丁  
  
②根权限设置为require all denide  
# 目录遍历  
## 漏洞原理  
  
由于配置错误导致的目录遍历  
  
配置的时候开启了显示目录，如下所示：  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1oS7NtrthheNYficn9Fc7egBq8Sq1Unwxgt0mEamDxBnibicPa5S3sDE63w/640?wx_fmt=png&from=appmsg "")  
  
![0](https://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBxZXhQ7W82tqNmfrAuz9w1oH6fUBCwicWXbJtgxJnCTxolmSu5B5kSHI5X3hCAgISNl7apkPLhA38A/640?wx_fmt=png&from=appmsg "")  
## 上传.htaccess(htaccess可以作用于当前目录以及子目录）  
  
.htaccess是Apache的又一特色。一般来说，配置文件的作用范围都是全局的，但Apache提供了一种很方便的、可作用于当前目录及其子目录的配置文件——.htaccess（分布式配置文件）。  
## .htaccess生效条件  
  
要想使.htaccess文件生效，需要两个条件，一是在Apache的配置文件中写上：  
```
AllowOverride All
```  
  
若这样写则.htaccess不会生效：  
  
AllowOverride None  
  
二是Apache要加载mod_Rewrite模块。加载该模块，需要在Apache的配置文件中写上：  
```
LoadModule rewrite_module /usr/lib/apache2/modules/mod_rewrite.so
```  
  
## 上传.htaccess绕过限制  
  
.htaccess文件可以配置很多事情，如是否开启站点的图片缓存、自定义错误页面、自定义默认文档、设置WWW域名重定向、设置网页重定向、设置图片防盗链和访问权限控制。但我们这里只关心.htaccess文件的一个作用——MIME类型修改。如在.htaccess文件中写入：  
```
AddType application/x-httpd-php xxx
```  
  
就成功地使该.htaccess文件所在目录及其子目录中的后缀为.xxx的文件被Apache当做php文件。  
# 参考链接  
  
https://cloud.tencent.com/developer/article/2290320  
  
https://blog.csdn.net/qq_66934029/article/details/142634560  
#   
  
  
  
