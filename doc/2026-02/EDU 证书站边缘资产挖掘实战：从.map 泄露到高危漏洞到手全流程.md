#  EDU 证书站边缘资产挖掘实战：从.map 泄露到高危漏洞到手全流程  
r0ngy40
                    r0ngy40  渗透安全HackTwo   2026-02-01 16:00  
  
**0x01 前言**  
  
**在  EDU 证书站这类高价值场景中，常规资产往往已被反复挖掘，边缘资产反而成为漏洞挖掘的 “蓝海”。本文聚焦某 EDU 证书站关联的高校目标，避开热门资产，通过 Hunter 语法精准测绘未备案边缘 IP 站点。**  
  
从意外发现的.map 文件泄露切入，逐步挖掘出未授权接口、任意文件下载与上传漏洞，借助 Base64 编码绕过限制成功读取敏感文件。更通过 bash_history 泄露获取管理员凭据与 Web 服务路径，最终利用路径穿越完成高危漏洞验证。  
  
全程还原从资产定位到漏洞利用的完整链路，所有操作均在授权范围内进行，漏洞已修复。旨在分享边缘资产挖掘思路与实战技巧，为安全研究者提供参考，严禁用于非法测试，坚守网络安全伦理底线。****  
  
现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo“设为星标”，否则可能就看不到了啦！**  
  
参考文章  
：  
  
```
https://xz.aliyun.com/news/91415
```  
  
  
**末尾可领取挖洞资料/加圈子 #渗透安全HackTwo**  
  
**0x02 漏洞详情**  
  
边缘资产测绘  
  
从证书站后几所学校锚定了一个目标，考虑到作为证书站的时间很长，常规的资产应该都被大手子们薅过了，于是尝试找找边缘资产。  
  
Hunter语法：  
```
web.title="xxxx大学"&&icp.number!="xxxxxxx"
```  
  
找到了一处没有域名备案的ip站点。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1Eh2jphHwiacm8GCUSFicDx265SM2RwUyaiauDUZEWRfIWFcntJSAccBseQ/640?wx_fmt=png&from=appmsg "")  
  
接口未授权  
  
站点存在.map文件泄露，把文件拖下来然后还原前端文件，可以发现存在文件下载和上传接口。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EO55LcgpSLonNY36q4UuDYYva2vic1D9DDR71CJY1W7k9LcosIWfrZCQ/640?wx_fmt=png&from=appmsg "")  
  
任意文件下载  
  
查看api对应的代码逻辑得知文件上传的参数是常规file。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EEGpDCGgs5AxsfPS6HUOlPLFQ5iaaoh9s0vibPAC6s4PnFumzeabibiakqg/640?wx_fmt=png&from=appmsg "")  
  
直接通过upload1接口上传文件，发现未对文件的内容和类型做限制。把响应包的base64解码可得到上传地址  
```
/datahome/attachment/2025-02-19/8f9689132e174fa5/test11111.jsp
```  
  
但是直接访问发现404，FUZZ了好一会也没FUZZ出来文件存储的路径。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EvA8JgpLfHCDFV9OmRHnX5v68dHFjoibIzAdOqeTMUpTnLGRvKRcGvgQ/640?wx_fmt=png&from=appmsg "")  
  
回头去看另一个下载的接口，直接尝试下载/etc/passwd发现报错，结合之前burp返回的路径是经过base64编码以及当前的Response反馈来看，fileName参数应该需要传递一个经过base64编码的路径值。  
  
将路径编码之后发送Request，成功下载文件，看到普通用户包括datahome和elasticsearch。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1E1zB0cJXibU9ZfbrQ7G31HpSa1zY0nxEN4sHaaicNFHU2qDY2AKOmKDdQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EHtlkoTCkfdIQajwlnvLGE5Pib4kXJSdBibDAphib7Shoa8Nia4ckeeWUicg/640?wx_fmt=png&from=appmsg "")  
  
Bash History泄露凭据和Web路径  
  
尝试读取/root/.ssh/id_rsa无果，尝试读取/root/.bash_history得到shell命令历史记录，在翻找历史记录中意外的得到了管理员账户凭据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1E3ohdjdZcic01ppTI0BN6wSuvNjtoKn5MD6Wx00bpT606esWnnGT7J1w/640?wx_fmt=png&from=appmsg "")  
  
通过获得的账户凭据以管理员身份登入后台，后台有站点备案，顺带帮我完成了资产的归属确定问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1ET3Oia5ctdic7ItE25OYtzORq0icXnZADpEKed1ZTvgRAXL8laaKvcrpQg/640?wx_fmt=png&from=appmsg "")  
  
任意文件上传+路径穿越  
  
在shell的历史记录中做进一步的检索，发现了运维人员修改过Web服务的配置文件，从而得知Web服务的绝对路径为  
```
/datahome/tomcat8_case/webapps/case
```  
  
已知默认情况下，我们上传的文件会被存储在/datahome/attachment/，如果我们能够文件名可控，我们可以想办法将文件上传到上述路径下，我们就可以直接访问了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EOcyEVAQucOHZKFpDickI2b1DqqaL0ic7yvkKTKDubC6oyJoVguJQd0eA/640?wx_fmt=png&from=appmsg "")  
  
因此自然而然的想到，测试服务对于文件名是否存在路径穿越的过滤，很幸运的是并没有，后续上传了一个计算1+1的jsp文件来保证文件可解析，作为对于站点接口的概念性验证。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6bQnUtKPdOk8OoTXkWNn1EAJPwLLOo5IY3nOJ1r2UwzOicJQgibl02DOOHvrzJVr94gDYPS0MZ7GSg/640?wx_fmt=png&from=appmsg "")  
  
点到为止，高危美美到手。  
  
  
**0x03总结**  
  
主要通过 Hunter 语法定位未备案 IP，也可以用fofa差不多，从.map 文件泄露切入，串联未授权接口、任意文件下载 / 上传、凭据泄露、路径穿越等漏洞，形成完整利用链。全程聚焦边缘资产挖掘思路，避开常规热门目标，高效拿下高危漏洞。所有操作均合规且漏洞已修复，分享实战经验供师傅们参考，祝师傅们天天出高危、挖洞不踩坑！🔥  
喜欢这类文章或挖掘SRC技巧文章师傅可以点赞转发支持一下谢谢！  
  
  
**内部星球VIP介绍V1.4（更多未公开挖洞技术欢迎加入星球）**  
  
  
**如果你想学习更多另类渗透SRC挖洞技术/攻防/免杀/应急溯源/赏金赚取/工作内推，欢迎加入我们内部星球可获得内部工具字典和享受内部资源/内部群🔥**  
  
🚀  
1.每周更新1day/0day漏洞刷分上分，目前已更新至5094+;  
  
🧰  
2.包含网上的各种付费工具/各种Burp  
漏洞检测插件  
/  
fuzz字典  
等等;  
  
🧩  
3.Fofa/Ctfshow/360Quake/Shadon/零零信安/Zoomeye各种账号高级VIP会员共享等等;  
  
🎥  
4.最新SRC挖掘/红队/代审/免杀/逆向视频资源等等;  
  
🧪  
5.内部自动化漏扫赚赏金捡洞工具，免杀CS/Webshell工具等等;  
  
🎯  
6.最新0Day1Day漏洞POC/EXP分享地址（同步更新）;  
  
https://t.zsxq.com/KcKlh  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7cpyLKdrg9g0QRpvkvBaQicGaNoLjesB2YZuPd6RMJOmxdwV8BBcEX8hjsT3OL6DuGpSedCkl2Mhw/640?wx_fmt=png&from=appmsg "")  
  
🔥  
7.详情直接点击下方链接进入了解，后台回复"   
星球  
 "获取优惠先到先得！后续资源会更丰富在加入还是低价！（即将涨价）以上仅介绍部分内容还没完！**点击下方地址全面了解👇🏻**  
  
  
**👉****点击了解加入-->>2025内部VIP星球福利介绍V1.4版本-1day/0day漏洞库及内部资源更新**  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
回复“**app**  
" 获取  app渗透和app抓包教程  
  
回复“**渗透字典**  
" 获取 一些字典已重新划分处理**（需要内部专属fuzz字典可加入星球获取，内部字典多年积累整理好用！持续整理中！）**  
  
回复“**书籍**  
" 获取 网络安全相关经典书籍电子版pdf  
  
# 最后必看  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.4版本0day推送**  
  
**2.最新Nessus2025.6.9版本下载**  
  
**3.最新BurpSuite2025.5.1专业版下载**  
  
**4.最新xray1.9.11高级版下载Windows/Linux**  
  
**5.最新HCL AppScan_Standard_10.8下载**  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
上一篇文章：  
[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)  
  
  
喜欢的师傅可以点赞转发支持一下  
  
