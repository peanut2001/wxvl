#  CVSS 9.8高危沙箱逃逸漏洞，vm2缺陷危及数百万应用  
 FreeBuf   2026-01-27 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38p1qHebKib5H8RBpPYAibsIcjqprCYubXRcA0P9zsfs8gOKzFzEWTMFnNbzrFF1NZxXhhnVVibDG9Qg/640?wx_fmt=png&from=appmsg "")  
  
  
Node.js 生态中广受欢迎的沙箱库 vm2 曝出重大安全漏洞（CVE-2026-22709），该漏洞 CVSS 评分高达 9.8 分，可使攻击者完全绕过沙箱环境，在宿主机上执行任意代码。数百万开发者使用该库运行不可信代码，受影响版本为 3.10.0 及以下。  
  
  
**Part01**  
## 漏洞原理分析  
  
  
漏洞根源在于沙箱对 JavaScript Promise 的处理机制存在缺陷——特别是回调函数的净化机制。虽然 vm2 设计上会对本地 Promise.prototype.then 和 Promise.prototype.catch 的回调进行净化，但研究人员发现全局 Promise（globalPromise）存在盲区。  
  
  
安全公告指出："在 lib/setup-sandbox.js 中，本地 Promise.prototype.then 的回调函数会被净化，但 globalPromise.prototype.then 却未受净化。"由于"异步函数的返回值是 globalPromise 对象"，攻击者只需定义异步函数即可获取未净化的 Promise 对象引用，进而突破沙箱限制。  
  
  
**Part02**  
## 攻击链构造  
  
  
攻击者可利用全局 Promise 上未净化的 catch 方法访问错误对象的构造函数，继而通过原型链溯源获取 Function 构造函数，最终在沙箱限制外生成新代码。公开的漏洞利用代码显示，攻击者可通过此链加载 child_process 模块执行系统命令（如 execSync('echo HELLO WORLD!')）。  
  
  
**Part03**  
## 影响范围与修复建议  
  
  
vm2 每月下载量超过 370 万次，该漏洞潜在影响面极大。维护者已发布 3.10.2 版本修复该缺陷，强烈建议用户立即升级以确保沙箱安全。  
  
  
**参考来源：**  
  
CVSS 9.8 Sandbox Escape: Critical vm2 Flaw Exposes Millions of Apps  
  
https://securityonline.info/cvss-9-8-sandbox-escape-critical-vm2-flaw-exposes-millions-of-apps/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334254&idx=1&sn=60c1a1f106cdbab728bc207a35262d08&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
