#  告别手动构造 Payload：Burp 文件上传漏洞测试插件，1000 + 绕过 Payload 全解析|工具分享  
T3nk0
                    T3nk0  渗透安全HackTwo   2026-01-22 16:02  
  
0x01 工具介绍  
  
  
一款强大的Burp Suite插件——**Upload_Auto_Fuzz**  
。该工具集成了超过**1000种**  
精心设计的Payload，涵盖后缀变体、双写绕过、空字节截断及系统解析特性等14种核心策略。其最新的v1.2.0版本更支持可视化配置与特定语言定向Fuzz，配合Intruder模块，助你一键自动化突破上传限制，彻底告别繁琐的手工测试！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R08GXAooBUQnDic9HjN7AZFsyWfSl7NWHbw8T6Nr7ib6bkQhhu30VavPpibHEVGdJCpgU5w9CpKh5g/640?wx_fmt=png&from=appmsg "")  
  
注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾 #渗透安全HackTwo**  
  
0x02   
功能简介  
  
  
✨ 主要特性  
### 后缀绕过  
- 可执行扩展名变体：php3/php5/phtml/phar/asa/cer/ashx/jspx 等  
  
- 大小写混淆：pHp、PhP、aSp、JsP  
  
- 双写绕过：pphphp、aspasp、jspjsp  
  
- 特殊字符：空格、点号、分号（shell.php.  
、shell.php;.jpg  
）  
  
- 空字节截断：shell.php%00.jpg  
  
### 请求头操控  
- Content-Disposition 大小写：ConTENT-DisPoSition  
  
- form-data 污染：删除、替换为脏数据、多分号  
  
- filename 参数：双 filename、空 filename、未闭合引号、多等号  
  
- 换行注入：filename\n="shell.php"  
  
### Content-Type 绕过  
- MIME 类型伪造：image/gif、image/png、application/octet-stream  
  
- URL 编码：image%2Fgif  
、image%2Fphp  
  
- 双重 Content-Type 头  
  
- 大小写变换  
  
### 系统特性利用  
  
**Windows**  
- NTFS 数据流：shell.php::$DATA  
  
- IIS 分号解析：shell.asp;.jpg  
  
- 保留设备名：con.php、aux.asp  
  
- 尾部空格/点号  
  
**Linux**  
- Apache 多扩展名：shell.php.jpg  
  
- 路径穿越：../shell.php  
  
- 隐藏文件：.shell.php  
  
### 编码绕过  
- URL 编码扩展名：%70%68%70  
  
- 双重 URL 编码  
  
- MIME 编码（RFC 2047）  
  
- Unicode 字符替换  
  
### 配置文件上传  
- .htaccess  
SetHandler 解析任意文件为 PHP  
  
- .user.ini  
auto_prepend_file 文件包含  
  
- web.config  
IIS handlers 配置  
  
### 文件内容  
- 魔术字节注入：GIF89a、PNG 头、PDF 头  
  
- WebShell 内容（可选）  
  
- 图片头 + WebShell 组合  
  
0x03更新说明  
```
v1.2.0 - 架构重构，新增配置面板，策略模式，1000+ payload
v1.1.0 - 新增云环境绕过、AI 防御对抗模块
v1.0.0 - 初始版本，基础 Fuzz 功能
```  
  
  
0x04 使用介绍  
  
📦  
使用指南  
  
1. 下载 Upload_Auto_Fuzz.py  
  
1. Burp Suite → Extender → Add  
  
1. Extension type 选择 Python  
  
1. 选择下载的文件，点击 Next  
  
  
  
需要配置 Jython，可以网上搜索下载### 配置（可选）  
### 安装后在 Burp 顶部菜单栏会出现 Upload Fuzz 标签页：  
  
  
Target Backend Languages：选择目标后端语言  
  
Fuzzing Strategies：启用/禁用特定测试策略  
  
Include WebShell Content：是否在 payload 中包含实际 WebShell 代码  
### 测试步骤  
1. 抓取文件上传请求，发送到 Intruder  
  
1. 选中需要 Fuzz 的区域（建议选中整个文件部分）：  
  
```
Content-Disposition: form-data; name="file"; filename="test.jpg"
Content-Type: image/jpeg
[文件内容]
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R08GXAooBUQnDic9HjN7AZRPCrdsrGIAJfETMngibbDS7et7HicMdsOW3rhMNIMzLiby42Oiblrk073g/640?wx_fmt=png&from=appmsg "")  
### Payloads 标签页配置：  
  
  
- Payload type: Extension-generated  
  
- Select generator: Upload_Auto_Fuzz 1.2.0  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R08GXAooBUQnDic9HjN7AZibqYgBhaO7Vbrvqme86AgxEwuhwiasKm5ib1ALiadR6X0f90XzLibP7Uia7A/640?wx_fmt=png&from=appmsg "")  
### 重要：取消勾选 Payload Encoding  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R08GXAooBUQnDic9HjN7AZQj6p3hMibq9NXoyHZ9hf8cxSvN1AmD8SkLBmlhnjichLDwib3cv4awNSw/640?wx_fmt=png&from=appmsg "")  
  
  
开始攻击，根据响应长度/状态码筛选结果  
###   
  
  
**0x05 内部VIP星球介绍-V1.4（福利）**  
  
        如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，  
**每天更新1day/0day漏洞刷分上分****(2026POC更新至5094+)**  
**，**  
包含全网一些**付费扫描****工具及内部原创的Burpsuite自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**  
。shadon/Zoomeye/Quake/  
Fofa高级会员，CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"   
**星球**  
 "有优惠券名额有限先到先得  
**❗️**  
啥都有  
**❗️**  
全网资源  
最新  
最丰富  
**❗️****（🤙截止目前已有2400+多位师傅选择加入❗️早加入早享受）**  
  
****  
最新漏洞情报分享：  
https://t.zsxq.com/lFN5j  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.4版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20260123获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.4（AI自动化工具）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.全新升级BurpSuite2025.12专业(稳定版)**  
  
**4. 最新xray1.9.11高级版下载Windows/Linux**  
  
**5. 最新HCL AppScan Standard**  
  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
  
上一篇文章：  
[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)  
  
  
