#  【漏洞复现】飞牛私有云 fnOS 0day 漏洞复现：可任意读取文件 + 绕过认证。  
原创 xuzhiyang
                    xuzhiyang  玄武盾网络技术实验室   2026-02-05 00:30  
  
***免责声明：本文仅供安全研究与学习之用，严禁使用本内容进行未经授权的违规渗透测试，遵守网络安全法，共同维护网络安全，违者后果自负。**  
  
****  
每日学习资源分享：  
图形化未授权访问漏洞批量检测工具  
  
更多资源请访问：  
www.xwdjs.ysepan.com  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0lxt0ibYqVFodyiaLaT0UNgQzWGoibKZIh453k7XHuhicvGbrD4sUAD4bqLKg9BRR6MXrJXTc0M03Wn1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
  
正文  
  
  
作为一款基于 Debian Linux 内核深度开发的国产 NAS 操作系统，飞牛私有云 fnOS 凭借免费开源、程序资源丰富的优势，成为众多个人和小型团队搭建私有存储的首选。然而近期，该系统被曝出严重 0day 漏洞，攻击者可利用此漏洞访问 NAS 设备上的任意文件（包括系统核心配置文件、用户隐私存储数据等），甚至能通过认证绕过获取管理员权限，给用户数据安全带来极大威胁。本文将基于安全测试环境，详细复现漏洞细节，并提供针对性防护建议（  
注：所有测试均在虚拟机中完成，内容仅用于安全研究与学习，坚决反对任何危害网络安全的非法行为）。  
  
## 一、漏洞环境说明  
  
  
本次测试选用飞牛私有云 fnOS v0.9.9 版本，部署在虚拟机中，系统网络配置如下：  
- 操作系统版本：fnOS v0.9.9  
  
- 主机名：trim-4312  
  
- IPv4 地址：192.168.50.88  
  
- Web 管理界面地址：http://192.168.50.88:5666测试工具采用 Kali Linux 系统搭配 Burp Suite Community Edition v2025.12.3，用于抓包分析与漏洞验证。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLm8ySVv7Oicgw654sAqpCXowlf8oI8LD5AFFyJHxfgQZ2R3WKqAgX7Vw/640?wx_fmt=jpeg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLODxA9yiaGpyVRAeBFld4icOKCTnMjaJ9czDBJKPiafrkKIVUyia3odnpJw/640?wx_fmt=jpeg "")  
  
![首页](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLNJiaiaSTiaCIfhEwV3ooLVyjic1hZYb5icqWqmtXhLIwZPeib4tndTLZfwaQ/640?wx_fmt=jpeg "")  
  
首页  
  
##   
  
## 二、漏洞复现：任意文件读取漏洞  
  
  
飞牛 fnOS 的该漏洞本质为路径穿越漏洞，攻击者可通过构造特殊请求包，突破系统文件访问限制，读取任意敏感文件。具体复现步骤如下：  
1. **访问目标地址并抓包**  
：在 Kali Linux 中打开浏览器，输入飞牛 fnOS 的 Web 管理地址http://192.168.50.88:5666，同时启动 Burp Suite 开启抓包功能，捕获浏览器与服务器之间的 HTTP 请求。  
  
1.   
1. ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLIIBfr7rXxtv9ibURGBwOXamhyDeZ9xINBUrHXOiaKcQ6IiaOkw4Xiat0Rw/640?wx_fmt=jpeg "")  
  
1. ****  
1. **构造 POC 触发路径穿越**  
：将捕获到的请求发送至 Burp Suite 的 Repeater 模块，构造如下 POC（路径穿越 payload）：  
  
```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../
```  
  
其中%7B0%7D  
是{0}  
的 URL 编码形式，../../../../  
用于向上穿越目录层级。点击发送请求后，服务器响应结果中出现了系统根目录的文件列表，包括 bin、boot、dev、etc、home 等核心目录，证明路径穿越漏洞存在。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLZE0sAhhPk3vLo22qjcCz5yQH5vLtFsOeUNJeFY9ruZ7UFZkTF3PeGQ/640?wx_fmt=jpeg "")  
  
1. **读取敏感系统文件**  
基于上述漏洞，进一步构造针对性请求，可直接读取系统关键配置文件：  
  
- 读取用户账号信息文件/etc/passwd  
，POC 如下：  
  
- ```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd
```  
  
  
-   
- ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqL2MGCFN76DN1zEj9cg7ooU40TcNlO3yRej4YJ2zSrU152DCUnbBZxBw/640?wx_fmt=jpeg "")  
  
-   
- 响应结果中返回了完整的用户列表，包括 root、daemon、bin 等系统账号及普通用户信息，包含用户名、UID、GID、家目录、登录 shell 等关键数据。  
  
- 读取用户密码哈希文件/etc/shadow  
，POC 如下：  
  
- ```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/shadow
```  
  
  
-   
- 响应结果中包含了各用户的密码哈希值，攻击者可通过暴力破解等方式获取明文密码，进而登录系统。  
  
-   
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLHlaN25HVjL1nB1UY2aqdcH0UDNxJxY6kHkwsVO69VoLVDQfYkv7D4A/640?wx_fmt=jpeg "")  
  
当然，也可以在浏览器中输入目录，直接进入，**除了通过 Burp Suite 发送请求，攻击者还可直接在浏览器地址栏输入构造好的 URL，无需借助工具即可实现文件访问，操作门槛极低，风险范围进一步扩大。**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqL9SmvpEBJU1DRh7iclzcJYQnRkKkTvzFWick7nfrUzlunnMhoHKeZhWcQ/640?wx_fmt=jpeg "")  
  
  
三、漏洞延伸：Websocket 协议认证绕过  
  
除了任意文件读取漏洞，飞牛 fnOS 还存在认证绕过漏洞。攻击者可通过前端 Websocket 协议与服务器建立连接，生成合法的 secret 和 token，无需正确的用户名和密码即可绕过登录验证，获取管理员权限。  
  
具体测试过程中，通过 Websocket 协议与目标服务器完成握手后，发送登录相关数据包，服务器返回了包含以下关键信息的响应：  
```
uid: 1000（用户 ID）
admin: true（管理员权限标识）
token: "wGk/IP5Af21SNQvITz4Y9m1w9mcFw1YRRV08kWfY4="（合法访问令牌）
machineId: "87dc9eb3e0aa46c09520855c83dbef3e25dffb5c"（设备标识）
```  
  
获取该 token 后，攻击者可直接携带令牌访问系统的所有功能模块，包括文件管理、系统设置、应用中心等，完全掌控 NAS 设备，风险等级极高。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLjgia7SzhR6OJ1Wmow6EyH0IQibXkRwlf1tAEZd0NxpYqXaRZmY6ickribg/640?wx_fmt=jpeg "")  
  
## 四、漏洞危害总结  
1. ****  
1. **数据泄露风险**  
攻击者可读取用户存储的所有私人文件（如照片、文档、工作资料等），以及系统配置文件、账号密码哈希等敏感信息，造成严重的隐私泄露和数据安全事件。  
  
1. **设备完全受控**  
结合认证绕过漏洞，攻击者可获取管理员权限，对 NAS 设备进行任意操作，包括修改系统配置、植入恶意程序、删除关键数据等，甚至可能将设备作为跳板攻击内网其他设备。  
  
1. **影响范围广泛**  
由于飞牛 fnOS 的免费特性，大量个人用户和小型企业正在使用，且部分用户可能将设备直接暴露在公网中，导致漏洞影响范围进一步扩大，潜在受害者数量众多。  
  
1.   
## 五、紧急防护建议  
  
  
为避免遭受该漏洞攻击，保障数据和设备安全，建议所有飞牛 fnOS 用户立即采取以下防护措施：  
1. **1、优先更新系统版本**  
1. 这是最根本的防护手段。请立即登录飞牛私有云官方网站（https://www.fnnas.com），下载并安装最新版系统固件，官方已修复该 0day 漏洞，更新后可彻底杜绝攻击风险。  
  
1. **2、禁止设备暴露公网**  
在未完成系统更新前，尽量不要将 NAS 设备直接暴露在公网中，可通过内网穿透的白名单设置、路由器端口映射限制等方式，仅允许信任的 IP 地址访问设备。  
  
1. **3、加强账号密码防护**  
及时修改管理员账号密码，设置复杂度高的密码（包含大小写字母、数字、特殊符号），并定期更换，避免因密码泄露导致额外风险。  
  
1. **4、临时关闭不必要服务**  
可暂时关闭 Web 管理界面的对外访问权限，或通过防火墙限制端口 5666 的访问，仅保留内网必要的访问通道，降低被攻击概率。  
  
1.   
网络安全无小事，尤其是私有云存储设备，承载着大量敏感数据，一旦遭受攻击，损失难以估量。建议各位用户高度重视此次漏洞，尽快完成系统更新和防护配置，同时持续关注官方发布的安全公告，及时应对各类潜在风险。  
  
随手点个「推荐」吧！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0knIjq7rj7rsX0r4Rf2CDQylx0IjMfpPM93icE9AGx28bqwDRau5EkcWpK6WBAG5zGDS41wkfcvJiaA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5 "")  
  
声明：  
技术文章均收集于互联网，仅作为本人学习、记录使用。  
侵权删  
！  
！  
  
