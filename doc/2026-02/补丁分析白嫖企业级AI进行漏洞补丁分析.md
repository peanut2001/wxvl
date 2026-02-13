#  补丁分析|白嫖企业级AI进行漏洞补丁分析  
 进击的HACK   2026-02-13 16:04  
  
   
  
# 以Alist为例，展示AI分析补丁包的能力  
## 白嫖来源-长亭MonkeyCode  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnHwCezh6A0cNqxzJoXK8YyKzScAkDBk2oEyeEzN34gUZZMAKfm8PxV1gQKR5U6Iia0etKj68SM1LjKEibpaUuL88BLy93AyTTZyw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icAu5T9rQGnHgPAicOV4VzHH9PpYcybiaf7vxKt9KMkDPfKBjBOrkM2L2iapCVvWRzrjXTu4kicYNQbXbdiaAGJSujyw5uOqaibgAoBNtNVPArGuBc/640?wx_fmt=png&from=appmsg "")  
  
白嫖的最香。## Alist CVE  
### 1. CVE-2026-25161  
#### NVD链接  
```
https://nvd.nist.gov/vuln/detail/CVE-2026-25161
```  
#### 发布日期  
  
2026年2月4日  
#### 漏洞风险  
  
高危  
#### 漏洞类型  
  
路径遍历  
#### 漏洞描述  
  
Alist 是一个支持多个存储文件的文件列表程序,由 Gin 和 Solidjs 提供支持。在3.57.0版本之前,该应用程序在多个文件操作处理程序中包含路径遍历漏洞。经过身份验证的攻击者可以通过将遍历序列注入文件名组件,从而绕过目录级别授权,从而在同一存储挂载中实现未经授权的文件删除、移动和复制。此问题已在 3.57.0 版本中进行了补丁。  
#### 截图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnGX92B3vxSC4CTq39T2mloPH6CYOwRCv8rBI8Rdn9rlajs1HmHgZPiaq70ibka0BMbROatJTlCFyTjzibmIvsKm19XTT7NJZNquPI/640?wx_fmt=png&from=appmsg "")  
### 2. CVE-2026-25160  
#### NVD链接  
```
https://nvd.nist.gov/vuln/detail/CVE-2026-25160
```  
#### 发布日期  
  
2026年2月4日  
#### 漏洞风险  
  
中危  
#### 漏洞类型  
  
TLS证书校验绕过  
#### 漏洞描述  
  
Alist 是一个支持多个存储文件的文件列表程序,由 Gin 和 Solidjs 提供支持。在3.57.0版本之前,该应用程序默认禁用所有外向存储驱动程序通信的TLS证书验证,使系统容易受到中间人(MitM)攻击。这使得存储操作过程中传输的所有数据都能实现完全解密、窃取和操作,从而严重损害用户数据的机密性和完整性。此问题已在 3.57.0 版本中进行了补丁。  
#### 截图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icAu5T9rQGnGNMpSmTkZTnqmPT7hzllcl638eIvc3j8ibicbzPBgZib2B8uXwWea4mUEiaaNBa8J7w0ick6BYUe6LmL1HqZ4NZCF4N1GWZ7NJYCAo/640?wx_fmt=png&from=appmsg "")  
## 使用长亭MonkeyCode进行补丁包分析  
### 1.下载仓库  
```
https://github.com/AlistGo/alist.git
```  
### 2. 查看两个版本差异并保存  
```
git diff v3.56.0 v3.57.0 > diff-356-to-357.txt
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icAu5T9rQGnFjpVWM9raOfbXUMIbTryfwaXntZNelicUsxJdt3OgG9GFQdXl2LZdvia96qDoeda5GqBh2ufgpr0RgDLbOBfJ7OiagD7jOytdibNI/640?wx_fmt=png&from=appmsg "")  
### 3.上传V3.57.0版本zip并将差异文件内容复制给MonkeyCode  
#### 链接  
```
https://github.com/AlistGo/alist/archive/refs/tags/v3.57.0.zip
```  
#### AI分析  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnGNhjvlAhzNDbF7YoB5WxEbia9sUQ6vUyEt4tvZW87WYRHYdutoWia15wB4ywabniaric1UXK22gRZEsA73H0ZWGFIC7AnJgg7CC64/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnHXKaruAIdUIUghGMDUzib44ARKDDIiarUtXBRvrRMaUQCX91bEhPFaicGiaGvxlek8Sy56RuXcAf3wpttPDhhJictFxb9Zibqtia6HiaI/640?wx_fmt=png&from=appmsg "")  
  
  
分析完成并要求写入md文档，可以通过源文件复制md代码保存本地。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icAu5T9rQGnGg0otl1PiaFUcZeGWrj7jLBtiaC25p2rbcHUUXy1I9Q0qBdBpgrgQ40gkAteI9EchwyfARkLWjkxKrrnUyeBThFkEXQ43C58ic8M/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnFRjquRFY6bpsb2BNDXhE3yHqmt0GC9gSugt9plw2NJd8KZkeVpdoegp6yueAlPCWU6IdHFuicmguYqnOPaVXoMgI32NBxIfKmQ/640?wx_fmt=png&from=appmsg "")  
#### AI结果  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icAu5T9rQGnHgTxYWWfPeQeIxhFgFEf2XmcYpDtiavktweoxGNIeUpgOyyHTo1icicU6Z64WoiaiatUoUc2qLu69sicmrO3VmwIWib0lfzPRjsCxz3A/640?wx_fmt=png&from=appmsg "")  
## 对MonkeyCode感兴趣的可以入群交流  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icAu5T9rQGnEfZ2zcwG4utnwOaG4h7icY85Hpz4udbd9oaNpmTlYGHnWicz9J03OFo8gCBGnIHqw5GOGW12S4wc4q3JmliaDlMWn6dHPLXjDe0w/640?wx_fmt=png&from=appmsg "")  
  
  
   
  
  
