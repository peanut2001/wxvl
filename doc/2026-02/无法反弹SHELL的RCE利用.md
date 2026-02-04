#  无法反弹SHELL的RCE利用  
安融技术
                    安融技术  安融技术   2026-02-04 03:38  
  
在无法直接反弹  
SHELL  
的情况下，  
RCE  
漏洞的利用需要根据目标系统的具体环境和限制，灵活运用多种技术和工具。在不直接获取交互式  
SHELL  
的情况下，实现对目标系统的控制和数据获取。以下是一些常见的利用方法和思路：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQhU3FnaPTWF3iad3pRNoSzrBbWFvJe3rWiavLCequatT4F5VgDlzXXfOg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
一、利用文件操作  
  
• 写入  
Webshell  
  
• 原理：通过  
RCE  
漏洞将  
Webshell  
代码写入服务器的  
Web  
目录中，然后通过浏览器访问该  
Webshell  
，从而获得对服务器的进一步控制。  
  
• 示例：假设目标服务器的  
Web  
目录为  
 /var/www/html   
，可以通过  
RCE  
漏洞写入一个  
PHP Webshell  
：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQRlVTqcTOMxFwpUfpt4sFQ6zRibslH0zISibwMDnibIKohme8ibutXEt7wg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
然后访问  
`http://target.com/shell.php?cmd=whoami`  
来执行命令。  
  
• 修改配置文件  
  
• 原理：修改服务器的配置文件，如  
.htaccess   
、  
php.ini  
等，以实现持久化控制或绕过某些限制。  
  
• 示例：通过  
RCE  
漏洞修改  
.htaccess  
文件，添加一个重写规则，将所有请求转发到一个恶意脚本：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQL5OFHAM5SibVK9aFNbW5zGnb8iasg9F03YMLkXjVNiaOauKRK3PdJUiaGg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
二、利用系统命令  
  
• 无交互命令执行  
  
• 原理：直接通过  
RCE  
漏洞执行系统命令，获取系统信息或进行其他操作。  
  
• 示例：在  
Linux  
系统中，可以通过  
RCE  
漏洞执行   
id   
命令来获取当前用户信息：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQR5XFG1VhHB6cDWLVMOUke3INpDGicIjPNTVwlBEZT5sFL1X66j6Ws1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
• 利用系统工具  
  
• 原理：利用系统自带的工具（如  
curl   
、  
wget   
等）下载或上传文件。  
  
• 示例：通过  
RCE  
漏洞使用  
 curl   
下载一个恶意脚本：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQibvuiaJE4aEwfPzKiaDibbla0aqVR4sks4qicwG2ia8KAPias0ZnvMacjg2ibw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
三、利用网络服务  
  
• 建立隧道  
  
• 原理：通过  
RCE  
漏洞在目标系统上启动一个隧道服务（如  
SSH  
、  
Socks5  
等），以便进行进一步的攻击。  
  
• 示例：在目标系统上启动一个  
SSH  
隧道：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQicwaOldiaSibva5icjibFhLm0prtjn9u2vibeIia5RIC9nTJNrDnkKvu6XoxA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
• 利用现有服务  
  
• 原理：利用目标系统上已有的服务（如  
FTP  
、  
SMTP  
等）进行数据传输或命令执行。  
  
• 示例：通过  
RCE  
漏洞利用  
FTP  
服务上传一个恶意文件：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQmxSLbJohdeiaBUnRibAO32PwJostWM6zWVF8ywibfubIMkg2QwicWNGsWw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
四、利用内存马  
  
• 内存马注入  
  
• 原理：通过  
RCE  
漏洞在目标系统的内存中注入一个恶意代码，从而实现持久化控制。  
  
• 示例：使用特制版哥斯拉工具注入内存马：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQonezvgxXVtr69OOsxgh5yZutZoXiaBiaOnFrr6dY3DOQ4h3IbkLHU4NQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
五、利用日志文件  
  
• 日志文件注  
  
• 原理：通过  
RCE  
漏洞将恶意代码注入到日志文件中，然后利用日志文件的解析漏洞执行代码。  
  
• 示例：在目标系统上将恶意代码注入到  
/var/log/apache2/error.log   
文件中：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQ3R3m3t4HRZvOVKvTtZeqxcJlpJBhLG36eVHibo5BZ2RiazECCXjf2G5Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
六、利用数据库  
  
• 数据库操作  
  
• 原理：通过  
RCE  
漏洞连接到目标系统的数据库，执行  
SQL  
语句以获取或修改数据。  
  
• 示例：通过  
RCE  
漏洞连接到  
MySQL  
数据库并执行  
SQL  
语句：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQUFibZxa8S5f0YfSib7BsPO4FianID0cfbCc2Msr3uXx1JTbm2BgGQZ26A/640?wx_fmt=jpeg&from=appmsg "")  
  
  
七、利用脚本语言特性  
  
• 无交互脚本执行  
  
• 原理：利用目标系统支持的脚本语言特性，执行恶意脚本。  
  
• 示例：在目标系统上执行一个  
Python  
脚本：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQrT1oZhKMpoon4FJv31BheStN4dyAQOgE6pjlq6Zhibj9R83UvD0MhxA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
八、利用系统漏洞  
  
• 利用已知漏洞  
  
• 原理：利用目标系统上已知的漏洞（如提权漏洞、本地漏洞等）进一步提升权限。  
  
• 示例：利用  
Linux  
系统上的提权漏洞  
 CVE-2021-33909   
：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQdpCzvQGuay0AFx34PAl7yWTfMGicmx3KzYcCWUbuhHrKXseA6fTLoxg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
九、利用社会工程学  
  
• 诱导用户交互  
  
• 原理：通过诱导目标用户进行某些操作（如点击链接、运行文件等）来实现攻击。  
  
• 示例：生成一个恶意的  
 .bat   
文件，诱导用户下载并运行：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQM2Jutzibqwpn7GZYg6qlVlINcOv09uF0ySyqnU4fibdDMsJN7vyQict9Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
十、利用内网资源  
  
• 内网渗透  
  
• 原理：通过  
RCE  
漏洞进入目标系统的内网，进一步渗透其他系统。  
  
• 示例：在目标系统上启动一个端口扫描工具，扫描内网其他主机：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCDUGpqpG2HLE2gJib9l8CiaoQibQj1tMNd9KLohajtpTKOUnz5x8FMXEa1TZYP9XXKYvRX86Tt5IltIg/640?wx_fmt=jpeg&from=appmsg "")  
  
