#  将超出漏洞范围的 HTML 注入升级为高危 9.3 分 XSS 漏洞（绕过 WAF）  
原创 骨哥说事
                    骨哥说事  骨哥说事   2026-03-16 05:46  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
## 引言  
  
在漏洞众测中，耐心是最有用的武器，有时发现的漏洞本身并无利用价值，必须进一步深挖才能产生实际危害。本文讲述国外白帽小哥如何从一个简单且超出范围的漏洞入手，被严格WAF拦截后，等待2个半月学习新技能，最终将其升级为高危9.3分反射型XSS（跨站脚本）的全过程。  
  
### 第一章：超出范围的漏洞与WAF拦截  
  
事情始于12月中旬，白帽小哥在某政府部门的漏洞披露项目（ target.com ）中进行漏洞挖掘。测试某接口时发现， q.LIKE 参数会将输入内容直接回显到页面。  
  
简单测试后确认可实现**HTML注入，**  
但存在一个关键问题：项目规则明确写明，HTML注入属于**超出漏洞接收范围**  
。想要提交有效漏洞报告，必须将其升级为XSS（跨站脚本）。  
  
白帽小哥尝试直接输入简单的 <script>alert(1)</script>  
，结果被**拦截**  
。目标站点部署了防护力度极强的AWS WAF，更麻烦的是，该WAF带有严格的封禁机制。每次检测到恶意载荷，都会将IP封禁5分钟。当时白帽小哥还不会使用IP轮换，手动测试搭配5分钟封禁，根本无法正常开展测试。  
  
研究陷入僵局，但小哥没有关闭该标签页，而是将其保留在浏览器中，转而学习新的技术。  
### 第二章：2个半月的沉淀与能力提升  
  
在接下来的两个半月里，这个标签页一直保持打开。这段时间小哥专注学习，研究高阶XSS利用技巧，更重要的是学会了在Burp Suite中配置**IP轮换**  
功能。  
  
启用IP轮换后，WAF的5分钟封禁不再构成阻碍，小哥准备重新对目标进行测试。  
### 第三章：PortSwigger学习笔记中的测试方法  
  
白帽小哥按照从PortSwigger Web安全学院学到的方法，分步对WAF进行测试。  
  
**步骤1：HTML标签模糊测试**  
首先需要确定WAF允许哪些标签。小哥将请求发送到Burp Intruder，使用HTML标签列表（<svg>、<body>、<a>、<video>等）进行模糊测试。WAF规则非常严格，但唯独允许（  
<video>  
）标签。  
  
**步骤2：事件处理器模糊测试**  
只拿到可用标签还不够，小哥再次使用Burp Intruder，对标签内的JavaScript事件处理器（如 onload、onerror 等）进行模糊测试。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZj1xH46NuQ9M7TxosSmZ2MrJCGe8XzHpS4CqCJWdEb6d3bljY2uT7Z5Hp2ffHrsGrmbovic77iaibBCj4VqfsVVJQIJAhLFJoGnQU/640?wx_fmt=png&from=appmsg "")  
  
几乎所有事件处理器都被拦截，但有一个事件处理器返回了**200 OK**  
：   
onwebkitpresentationmodechanged  
。WAF开发人员拦截了常规事件处理器，却漏掉了这个WebKit内核（Safari浏览器）专属的事件。  
### 第四章：最终绕过方案（字符串拼接）  
  
白帽小哥已经拿到可用的标签<video>  
与 onwebkitpresentationmodechanged 事件，接下来需要实现JavaScript代码执行。  
  
但WAF仍在对代码内容进行检测，直接编写 window.location 或 javascript:alert(1) 都会被拦截。为绕过检测，小哥使用**字符串拼接**  
，把被拦截的关键词拆分成小段，使WAF无法正常识别。  
  
不直接写 window.location，而是写成： window['loca'+'tion']。  
  
为让Payload完全避开WAF检测，小哥还使用了 window.name 技巧。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhw1vyzuGAAVzNsAnSVxibuqwCpiaciamDVib3mhS0QIIM5fKXX7nVHAKbSeW4fgddIoOKxuibnj3SPvbMxYNVB3VygArJjOW0Sqml0/640?wx_fmt=png&from=appmsg "")  
  
最终攻击链：  
1. 构造恶意HTML页面，设置： window.name = "javascript:alert(document.domain)"  
  
1. 该页面将受害者跳转到存在漏洞的URL  
  
1. 注入后的载荷大致如下： ...<video/controls/src="..."/onwebkitpresentationmodechanged="window['loca'+'tion']=window['na'+'me']"></video>...  
  
1. 当Safari用户播放视频或开启画中画模式时，该WebKit专属事件被触发  
  
1. 浏览器执行隐藏在 window.name 中的恶意Payload  
  
## 结论  
  
小哥将完整报告提交到漏洞平台，研判团队确认该WAF绕过有效，将漏洞评定为高危级别（CVSS 9.3）并收录。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgiaXyDA0jIWUriblTn3ibH0zWbJIPt520Q5vibvw2guGXnJp4ic8HicjmcEibn0iaetDmRmeblheeMwad2nwWGEMKqoRfKfiaFoicVTgHSs/640?wx_fmt=png&from=appmsg "")  
  
**经验总结：**  
如果发现某个漏洞不在接收范围内，不要直接放弃。遇到WAF拦截时，先暂停测试，学习新技能，再以更强的状态回来。永远不要关掉那个关键标签页！  
  
原文：https://medium.com/@housien.a.khalek19/escalating-an-out-of-scope-html-injection-to-a-critical-9-3-xss-waf-bypass-12b194d6a1df  
  
- END -  
  
**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**  
  
