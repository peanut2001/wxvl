#  CRLF 注入漏洞 ┏(｀-´)┛  
原创 ExplorerFD1
                        ExplorerFD1  D1TASec   2026-02-04 13:52  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1TEuKEW8cLkN9VkmFa4KOKe6wSiamozZZ0fFuoDWISOiavV8f4b1iaBpUmxnFxr1x2GHHIcP4S92MPoveGV8MBnHw/640?wx_fmt=gif&from=appmsg "")  
  
  
  
  
  
免责声明  
  
  
  
  
来自 D1TASec（本公众号）的技术文章仅供参考，此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他用途！！！  
  
  
## 漏洞原理  
  
CRLF 是CR  
（回车）和LF  
（换行）两个字符的拼接，对应转义符\r\n  
，全称为 Carriage Return/Line Feed。  
  
它的编码对应关系如下：  
- 十六进制编码：0x0d  
（CR）、0x0a  
（LF）  
  
- URL 编码：%0D  
（CR）、%0A  
（LF）  
  
CRLF 组合在一起，相当于键盘上的「Enter」键，常被用作各类程序和协议的分隔符。不同操作系统的换行符也存在差异：  
```
Windows：使用 CRLF（\r\n）表示行结束
Linux/Unix：仅使用 LF（\n）表示行结束

```  
  
而在**HTTP 协议**  
中，有两个关键的分隔规则：  
1. 多个 HTTP 响应头之间，用一个CRLF  
分隔  
  
1. HTTP 响应头与响应体（页面内容）之间，用两个CRLF  
分隔  
  
浏览器和服务器正是依靠这个规则解析 HTTP 报文。如果**用户可控的输入被直接回显在 HTTP 返回包的 Header 中**  
，攻击者就可以通过注入CRLF  
提前结束响应头，篡改报文结构，甚至注入恶意内容。因此，CRLF 注入也被称为**HTTP 响应拆分 / 截断（HTTP Response Splitting，简称 HRS）**  
，可能引发 XSS、Cookie 伪造、日志篡改等高危安全问题。  
## 漏洞利用  
  
假设某接口的参数会直接在 HTTP 响应头的Server  
字段中回显，我们以此为例看完整的利用过程。  
### 第一步：正常请求与响应  
  
请求包（参数为普通字符串）：  
```
GET /xxx/xyz/zzz?param=123456 HTTP/1.1
Host: xxx.com

```  
  
响应包（Server  
字段回显了参数值）：  
```
HTTP/1.1 200 OK
Server: 123456
Content-Type: text/html; charset=utf-8

```  
### 第二步：注入 CRLF 创建新响应头  
  
利用核心是在参数中插入 URL 编码的 CRLF（%0D%0A  
），截断原有响应头，创建新的自定义头。  
  
请求包（注入%0D%0AHello:789  
）：  
```
GET /xxx/xyz/zzz?param=123456%0D%0AHello:789 HTTP/1.1
Host: xxx.com

```  
  
响应包（Server  
字段后出现了新的Hello  
字段，说明注入成功）：  
```
HTTP/1.1 200 OK
Server: 123456
Hello: 789
Content-Type: text/html; charset=utf-8

```  
### 第三步：进阶利用（关闭 XSS 防护 + 注入恶意脚本）  
  
通过注入两个连续的%0D%0A  
（对应\r\n\r\n  
），可以分隔响应头和响应体，进而注入 XSS 脚本，同时关闭浏览器的 XSS 防护。  
  
请求包：  
```
GET /xxx/xyz/zzz?param=123456%0D%0AX-XSS-Protection:0%0D%0A%0D%0A<script>alert('xss')</script> HTTP/1.1
Host: xxx.com

```  
  
响应包（成功关闭 XSS 防护，且响应体中出现恶意脚本）：  
```
HTTP/1.1 200 OK
Server: 123456
X-XSS-Protection: 0

<script>alert('xss')</script>
Content-Type: text/html; charset=utf-8

```  
  
此时浏览器会执行恶意脚本，完成 XSS 攻击，这只是 CRLF 注入的其中一种高危利用场景。  
## 漏洞修复方法  
1. 过滤 / 移除所有 CRLF 相关字符  
  
对所有用户可控输入（URL 参数、POST 数据、Cookie 等），移除或替换\r  
、\n  
、%0D  
、%0A  
等核心字符，避免被解析为分隔符。  
  
1. 采用白名单验证输入  
  
对有固定格式的输入（如重定向 URL、手机号），仅允许合法内容通过（如仅允许指定域名、仅允许数字），从根源杜绝非法字符。  
  
1. 禁止用户输入直接拼接 HTTP 响应头  
  
不允许将未经处理的用户输入直接作为响应头的键或值，如需使用，需先进行安全编码（如 URL 编码、Base64 编码）。  
  
1. 开启框架 / 中间件 / WAF 内置防护  
  
升级 Web 框架至最新版本，开启 Tomcat/Nginx 的 CRLF 拦截功能，或通过 WAF 拦截包含 CRLF 的恶意请求，形成多层防护。  
  
1. 针对性加固高发场景  
  
对重定向（Location  
头）、设置 Cookie（Set-Cookie  
头）、页面刷新（Refresh  
头）等高发场景，做额外的专项校验。  
  
## 各语言原生开发注意点  
### Python（Django/Flask）  
1. 高发场景：使用response.headers  
直接设置响应头、redirect  
函数接收用户输入作为跳转地址。  
  
1. 注意事项：避免直接使用request.args.get()  
获取的参数拼接响应头，推荐使用框架自带的安全响应方法，手动过滤可借助正则移除 CRLF 字符。  
  
1. 小技巧：Flask 可使用crlf-sanitizer  
中间件全局过滤，Django 可在表单验证层添加 CRLF 校验。  
  
### PHP（原生 / ThinkPHP）  
1. 高发场景：使用header()  
函数设置响应头、setcookie()  
函数接收用户输入作为 Cookie 值。  
  
1. 注意事项：原生 PHP 无内置 CRLF 防护，需手动封装过滤函数，禁止直接将$_GET  
/$_POST  
/$_COOKIE  
参数传入header()  
。  
  
1. 小技巧：设置 Cookie 时可使用urlencode()  
编码值，避免特殊字符被解析，应急场景可临时开启magic_quotes_gpc  
（不推荐长期使用）。  
  
### Java（Servlet/Spring Boot）  
1. 高发场景：使用response.setHeader()  
、response.sendRedirect()  
拼接用户输入。  
  
1. 注意事项：Spring Boot 2.6.x 及以上版本内置 CRLF 防护，低版本需手动过滤；避免使用反射获取用户输入拼接响应头。  
  
1. 小技巧：可封装通用工具类，统一处理所有用户输入，优先使用org.apache.commons.codec  
进行安全编码。  
  
  
  
  
  
  
  
**📞 联系我们**  
  
  
如果你在使用过程中遇到任何问题，或者有任何建议和反馈，欢迎通过以下方式联系我们：  
  
邮箱：D1TASec@126.com  
  
**欢迎关注**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1TEuKEW8cLkN9VkmFa4KOKe6wSiamozZZbCxGb0dJ7Ol8Nmu1gPu37Gb8WmdfS51sB45Orm5YGJAvTk6Byr1iadA/640?wx_fmt=jpeg&from=appmsg "")  
  
我们终会上岸，无论去到哪里  
  
都是阳光万里，鲜花灿烂  
  
  
  
