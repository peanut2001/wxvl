#  第70天-Web攻防实战：文件下载、读取与删除漏洞 & 目录遍历与穿越  
原创 萧瑶
                    萧瑶  AlphaNet   2026-03-06 11:02  
  
在 Web 应用开发中，**文件操作功能几乎不可避免**  
。  
  
例如：  
  
- 文件下载  
- 文件读取  
- 文件删除  
- 文件管理器  
- 日志查看  
- 模板加载  
如果开发者在实现这些功能时**未正确限制路径或文件权限**，攻击者就可能借此读取服务器敏感文件、遍历系统目录，甚至破坏系统环境。  
  
  
这一类漏洞通常属于：  
  
  
**文件操作安全漏洞（File Operation Vulnerability）**  
  
  
本文将系统分析：  
  
  
1️⃣ 文件下载 / 读取 / 删除漏洞2️⃣ 目录索引与目录遍历漏洞3️⃣ 黑盒与白盒挖掘方法4️⃣ 实战攻击思路与防御方案  
  
  
# 一、文件安全问题：读取、下载与删除  
  
  
文件操作漏洞通常出现在**文件下载接口或后台管理系统**。  
  
  
核心本质其实是：  
  
>   
> 用户可以控制服务器访问的文件路径。  
>   
  
  
  
因此攻击者可以尝试访问**服务器上不应该公开的文件**。  
  
  
# 二、文件下载漏洞（File Download）  
  
## 1、正常下载方式  
  
  
最常见的文件下载方式是：  
  
```
http://www.xiaodi8.com/upload/123.pdf

```  
  
  
服务器直接提供静态文件下载。  
  
  
这种方式风险较小，因为访问路径固定。  
  
  
## 2、动态下载接口（高风险）  
  
  
很多系统会使用**动态下载接口**：  
  
```
http://www.xiaodi8.com/download.php?file=123.pdf

```  
  
  
或  
  
```
http://www.xiaodi8.com/api/down?file=123.pdf

```  
  
  
如果服务器代码类似：  
  
```
$file = $_GET['file'];
readfile("/upload/" . $file);

```  
  
  
攻击者就可以尝试修改参数：  
  
```
http://www.xiaodi8.com/download.php?file=../../config.php

```  
  
  
这就是经典的：  
  
  
**路径遍历读取漏洞**  
  
  
## 3、攻击目标文件  
  
  
攻击者通常会尝试读取以下敏感文件：  
  
### 数据库配置文件  
  
  
例如：  
  
```
config.php
database.php
.env
settings.py

```  
  
  
示例内容：  
  
```
DB_HOST=127.0.0.1
DB_USER=root
DB_PASS=123456

```  
  
  
一旦泄露，数据库可能被直接控制。  
  
  
### 系统密钥  
  
  
例如：  
  
```
secret.key
jwt.key
rsa_private.key

```  
  
  
攻击者可用于：  
  
- 伪造 JWT  
- 破解加密通信  
- 冒充服务器身份  
### 中间件配置  
  
  
例如：  
  
```
nginx.conf
web.xml
application.yml

```  
  
  
这些文件可以暴露：  
  
- 内网结构  
- 服务端口  
- 后端接口  
# 三、文件删除漏洞（File Delete）  
  
  
文件删除漏洞通常出现在：  
  
  
**后台管理系统**  
  
  
例如：  
  
```
http://example.com/admin/delete.php?file=test.jpg

```  
  
  
后台代码：  
  
```
unlink($_GET['file']);

```  
  
  
如果没有限制路径，攻击者可以：  
  
```
delete.php?file=../../config.php

```  
  
  
从而删除服务器关键文件。  
  
  
## 攻击场景  
  
### 1、删除配置文件  
  
  
例如删除：  
  
```
config.php
.env

```  
  
  
导致系统崩溃。  
  
  
### 2、删除安装锁  
  
  
很多程序安装后会生成：  
  
```
install.lock

```  
  
  
攻击者删除后可以重新进入安装程序：  
  
```
http://example.com/install/

```  
  
  
重新初始化数据库，直接接管系统。  
  
  
这种攻击在 CMS 系统中**非常常见**。  
  
  
# 四、目录安全问题  
  
  
目录相关漏洞主要有两种：  
  
  
1️⃣ 目录索引2️⃣ 目录遍历  
  
  
# 五、目录索引漏洞（Directory Index）  
  
  
当 Web 服务器未关闭目录浏览功能时，访问目录会直接列出文件。  
  
  
例如：  
  
```
http://example.com/upload/

```  
  
  
如果出现：  
  
```
Index of /upload
-----------------------
file1.jpg
file2.zip
backup.sql
config.bak

```  
  
  
攻击者可以直接下载敏感文件。  
  
  
## 常见敏感文件  
  
```
backup.sql
www.zip
db_backup.tar
config.bak

```  
  
  
很多真实渗透测试中，**数据库备份文件就是这样拿到的**。  
  
  
# 六、目录遍历漏洞（Directory Traversal）  
  
  
目录遍历也叫：  
  
  
**路径穿越漏洞（Path Traversal）**  
  
  
核心利用符号：  
  
```
../

```  
  
  
表示：  
  
```
返回上一级目录

```  
  
  
## 示例  
  
  
假设服务器代码：  
  
```
/download?file=report.pdf

```  
  
  
攻击者修改为：  
  
```
/download?file=../../../../etc/passwd

```  
  
  
服务器可能返回：  
  
```
root:x:0:0:root:/root:/bin/bash

```  
  
  
说明攻击成功。  
  
  
## 常见攻击路径  
  
  
Linux：  
  
```
/etc/passwd
/etc/shadow
/root/.ssh/id_rsa

```  
  
  
Windows：  
  
```
C:\Windows\win.ini
C:\boot.ini

```  
  
  
# 七、黑盒漏洞挖掘方法  
  
  
黑盒测试主要从：  
  
  
**功能点与 URL 特征**  
  
  
进行分析。  
  
  
## 1、重点功能点  
  
  
重点关注：  
  
- 文件上传  
- 文件下载  
- 文件删除  
- 文件管理器  
- 日志查看  
- 图片查看  
- 模板加载  
这些功能**几乎必然涉及文件操作**。  
  
  
## 2、URL关键字特征  
  
  
常见路径：  
  
```
download
down
readfile
read
del
delete
dir
path
src
lang

```  
  
  
示例：  
  
```
/download?file=test.pdf
/read?file=1.txt
/delete?file=test.jpg

```  
  
  
## 3、参数特征  
  
  
常见参数名：  
  
```
file
path
filepath
readfile
data
url
realpath
dir

```  
  
  
例如：  
  
```
/api/download?file=123.pdf
/api/read?path=log.txt

```  
  
  
这些参数通常**高度可疑**。  
  
  
# 八、白盒代码审计方法  
  
  
白盒分析重点是寻找：  
  
  
**文件操作函数**  
  
  
## PHP危险函数  
  
### 文件读取  
  
```
readfile()
file_get_contents()
fopen()

```  
  
  
### 文件下载  
  
```
readfile()
fpassthru()

```  
  
  
### 文件删除  
  
```
unlink()

```  
  
  
### 目录操作  
  
```
opendir()
readdir()
scandir()

```  
  
  
如果这些函数直接使用用户输入参数，例如：  
  
```
$_GET['file']

```  
  
  
就极有可能存在漏洞。  
  
  
# 九、真实攻击链示例  
  
  
一个典型攻击流程：  
  
### 第一步：发现下载接口  
  
```
/download.php?file=1.pdf

```  
  
  
### 第二步：尝试路径遍历  
  
```
/download.php?file=../../config.php

```  
  
  
### 第三步：获取数据库配置  
  
```
DB_USER=root
DB_PASS=123456

```  
  
  
### 第四步：连接数据库  
  
  
直接登录数据库获取：  
  
- 用户信息  
- 管理员账号  
- token  
### 第五步：获取后台权限  
  
  
最终实现：  
  
  
**完全控制系统**  
  
  
# 十、安全防御方案  
  
  
开发者应采取以下措施：  
  
  
## 1、禁止用户直接控制路径  
  
  
不要直接拼接路径：  
  
  
错误代码：  
  
```
readfile($_GET['file']);

```  
  
  
正确方式：  
  
  
使用白名单：  
  
```
$allow_files = ['a.pdf','b.pdf'];

```  
  
  
## 2、路径规范化  
  
  
使用：  
  
```
realpath()

```  
  
  
限制访问目录。  
  
  
## 3、限制访问目录  
  
  
例如：  
  
```
/var/www/download/

```  
  
  
禁止访问系统目录。  
  
  
## 4、关闭目录索引  
  
  
Nginx：  
  
```
autoindex off;

```  
  
  
Apache：  
  
```
Options -Indexes

```  
  
  
## 5、严格权限控制  
  
  
避免 Web 进程拥有：  
  
- 删除系统文件  
- 访问系统配置  
# 十一、总结  
  
  
文件操作类漏洞在 Web 渗透测试中非常常见。  
  
  
核心问题通常来自：  
  
  
**用户输入 → 直接控制文件路径**  
  
  
常见攻击方式包括：  
  
- 文件下载漏洞  
- 文件读取漏洞  
- 文件删除漏洞  
- 目录索引漏洞  
- 目录遍历漏洞  
攻击者通过这些漏洞可以：  
  
- 获取数据库配置  
- 下载服务器备份  
- 删除关键文件  
- 遍历系统目录  
在实际渗透测试中，这类漏洞往往是**突破系统的第一步**。  
  
  
# 参考案例复盘  
  
```
https://mp.weixin.qq.com/s/Kiec7FhvpAmPf7zTWvJa3g
https://mp.weixin.qq.com/s/QqXxpTwXSjCNN622fSsZAQ
https://mp.weixin.qq.com/s/A2FvZMuPpHiewGrL5UDlHw
https://mp.weixin.qq.com/s/w2PH7EI6Z2R9diV_tBA1Zw

```  
  
  
这些案例展示了：  
  
- 下载漏洞利用  
- 目录遍历攻击  
- 文件删除漏洞  
- 敏感信息泄露  
值得深入复盘分析。  
  
