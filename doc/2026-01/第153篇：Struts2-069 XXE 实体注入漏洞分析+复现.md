#  第153篇：Struts2-069 XXE 实体注入漏洞分析+复现  
原创 abc123info
                        abc123info  希潭实验室   2026-01-24 01:49  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcaA8wBFW4icTiaL7ELd8ia04Olh40TBx7CquHZyCicicl4eYJno2y0oZ0H4A/640?wx_fmt=png "")  
  
 Part1 前言   
  
大家好，我是ABC_123  
。最近Struts2框架爆出了一个S2-069漏洞，看了一下是XXE实体注入漏洞，简要地分析了一下，把过程写出来分享给大家。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
 Part2 技术研究过程   
  
该漏洞的成因在于Apache Struts2框架的 XWork-Core 组件对 XML 解析器的安全选项配置存在疏漏，攻击者可以构造恶意 XML 数据并向受影响的 Struts2 应用发起请求，从而触发XML外部实体注入攻击，最终实现数据窃取、SSRF或拒绝服务等恶意操作。影响版本：Struts 2.0.0-2.3.37 (EOL)，Struts 2.5.0-2.5.33 (EOL)，Struts 6.0.0-6.1.0。  
  
- 漏洞分析过程  
  
如下图所示，对比struts2-6.0.3版本与struts2-6.1.1版本代码的不同，可以看到在com.opensymphony.xwork2.util.DomHelper.parse类中，出现了右图中的修复方案  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEG6wjmOZT8oZeuRicIa1opcHNBJFIDiciadxMHK4TMMx3vicNwh9zkxdkAQw/640?wx_fmt=png&from=appmsg "")  
  
  
如下所示，修复后的Struts2框架通过上述代码关闭外部通用实体（External General Entities），禁止解析类似   
<!ENTITY xxe SYSTEM "file:///etc/passwd">  
 这种外部实体。  
```
factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
```  
  
如下所示，  
修复后的Struts2框架  
禁止解析 DTD 中的参数实体（更常用于复杂 XXE 变种），很多 XXE payload 依赖这个能力来加载远程 DTD 或绕过限制。  
```
factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```  
  
  
除此之外，我们继续对比不同版本的代码，XSLTResult.java类中也修复了一处XXE漏洞：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEGzkgq606P93w244DSPPczaqCEicqPtDlUXY68Z2jbWJHv3wicmCCF6vTA/640?wx_fmt=png&from=appmsg "")  
  
  
设置成 ""（空字符串）通常表示：完全不允许访问任何外部 DTD。  
```
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
```  
  
设置成 "" 表示：禁止访问任何外部 XSLT 样式表 stylesheet。  
```
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
```  
  
- 漏洞复现过程  
  
首先Intellij Idea编写一个测试环境，代码如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEGh2MkAAS1GacvLV9iahmHiarEmNmCtiaBcB5OibOZpcIZxYhMwLBFUgOZiaQ/640?wx_fmt=png&from=appmsg "")  
  
  
使用网上流传的EXP发包如下，确实可以利用成功。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEGouMvzia9eoUlwObMEoH9Ma5aKb1hlfobU8wLu04RAKic5ib9Hw8TQNz2Q/640?wx_fmt=png&from=appmsg "")  
  
- 漏洞验证方法  
  
接下来是如何检测发现这个漏洞，通过读取/etc/passwd及windows/win.ini文件内容来判断是否存在关键是一个方法。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEGhkpSU6R7kkxic6bcH72F8no6xpg0858lCezEqwUwzxrL3flPf10yc5w/640?wx_fmt=png&from=appmsg "")  
  
  
但有的XML读入过程未必会有回显，所以也需要加入DNSlog的方式来判断漏洞是否存在。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEG1aJLHhhRBsagSATdYAJPfF83Hu9KlCx6b9uXgAtohP0vAE3CqK4ogw/640?wx_fmt=png&from=appmsg "")  
  
  
 Part3 总结   
  
1.   
 等后续工具修正完bug后会提供下载地址。  
  
2.  
    
为了便于技术交流，现已建立微信群"  
希水涵-信安技术交流群  
"，欢迎您的加入。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CVq2PZ4OVApPUP5RfKbtEGodp9wG0b3xWia2S5phxYwwtOQTjxFEBsbsgcMDbhzTcQOibvosx24UyA/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18 "")  
  
  
**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**  
  
**Contact me: 0day123abc#gmail.com**  
  
**OR 2332887682#qq.com**  
  
**(replace # with @)**  
  
  
