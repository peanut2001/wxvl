#  从侦察到利用：攻击者如何发现、利用和串联Web应用程序漏洞——以及防御者如何检测和阻止它们  
haidragon
                    haidragon  安全狗的自我修养   2026-03-03 04:10  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuzIkkTMTW8CUHV5MR68qFVAuOib3n0vY72jeyh4wYLP5KmTicwDXozFbqiaKPIayBMRfYtaN7VfK4e8OBRqXjnglo1adcbHVlZhU/640?wx_fmt=png&from=appmsg "")  
  
  
今天，我们用**攻击者的思维**  
，来做**防御**  
。  
  
攻击中最危险的部分，往往是你看不见的那一段 —— **侦察（Reconnaissance）**  
。  
  
大多数数据泄露并不是从漏洞利用开始的。  
  
它们始于攻击者绘制你的攻击面，在你察觉之前找到薄弱入口。  
  
根据 Verizon 的《数据泄露调查报告（DBIR）》，相当比例的安全事件涉及外部攻击者，并且通常始于侦察与扫描活动。  
  
在许多漏洞赏金（Bug Bounty）和 VAPT 评估中，初始入口往往是一个被遗忘的子域名、配置错误的 API 或暴露的服务 —— 这些都是在侦察阶段发现的资产。而互联网级扫描和威胁情报平台正是为了提前暴露这些风险。  
  
在本文中，我们将拆解攻击者如何从侦察走向漏洞利用 —— 以及防御者如何尽早检测并阻止他们。  
## 1. 引言  
  
现代攻击很少直接从漏洞利用开始。  
  
它们从**可见性（Visibility）**开始。  
  
攻击者不会随机入侵系统 —— 他们会先**绘制、观察、理解**  
目标。这种方法同样被漏洞赏金猎人、红队成员以及真实攻击者广泛使用。  
  
理解这种**端到端攻击流程**  
有助于：  
- 外部威胁情报平台（如 Whatoblock）在利用发生前就提供可见性  
  
- SOC 团队更早检测攻击  
  
- 安全工程师设计更有效的防御体系  
  
- 研究人员更快发现高影响漏洞  
  
本文将带你从攻击者视角出发，走完整个从侦察到利用与检测的流程。  
## 2. 侦察与外部可见性  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsZRfwJK5WLwy3uoK8mZiaEiat8JKEGUyLbdOYoJJchLg1RuS8G2bglh1a3yic6y6f460tgNks1nK8N7ztJEvtPku8c7tPKicspFic0/640?wx_fmt=png&from=appmsg "")  
  
一切从这里开始。  
  
攻击者要回答的核心问题是：  
> **“哪些资产暴露在公网，并且可以被访问？”**  
  
### 子域名枚举与端点发现  
  
常用工具：  
- **subfinder**  
：查找子域名  
  
- **amass**  
：深度子域名枚举  
  
- **crt.sh**  
：通过 SSL 证书日志发现子域  
  
- **dnsx**  
：解析并验证域名  
  
示例命令：  
```
```  
  
检测存活主机：  
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnued7ZT9M8kUDaVB6FQHCfzsH87azdd4xcdnFZBiag7d5iaWCeq9NO69ic1bjcl0FjiaRPjtLKHZTibzLyKJ9CBYs9wcOExiap8ULHVo/640?wx_fmt=png&from=appmsg "")  
  
用于识别活跃主机。  
### 端点与 URL 发现  
  
工具：  
- **gau**  
：获取历史 URL  
  
- **waybackurls**  
：获取归档 URL  
  
- **hakrawler**  
：爬取页面链接  
  
- **katana**  
：深度爬取隐藏端点  
  
```
```  
### 技术栈识别  
  
工具：  
- **Wappalyzer**  
：识别框架、CMS  
  
- **WhatWeb**  
：识别 Web 技术与服务器信息  
  
- **BuiltWith**  
：技术栈与集成分析  
  
- **httpx**  
：探测服务与 HTTP 响应  
  
```
```  
  
攻击者可以识别：  
- 前端框架（React、Angular、Laravel）  
  
- Web 服务器（nginx、Apache）  
  
- 后端技术（NodeJS、PHP）  
  
- 第三方集成服务  
  
### 互联网级扫描视角  
  
攻击者还会使用全球扫描引擎：  
- Whatoblock  
  
- Shodan  
  
- Censys  
  
- ZoomEye  
  
- FOFA  
  
示例查询：  
```
```  
  
SOC 视角提示：  
- 异常 DNS 查询激增  
  
- 大量 NXDOMAIN 响应  
  
- 重复 404 错误  
  
这些往往是自动化侦察的强烈信号。  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnu8X7w1g2k2caxon35171TJ4lBY36wrgmeNDiaIwJgc7NRjO1zrUJF8gav56ibLE5KY6s6dhdF6YSPD4ywHXtM0W0HFUicA15LepQ/640?wx_fmt=png&from=appmsg "")  
  
实时 TCP/UDP 扫描行为示例（来源：Whatoblock）  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuFOwRdtXqXCAPH1PvSOFrMkgwUbqTo6dbBVJJTD9gDwJg0ICh8fzG2RuMbt0GzbvDib9j7ftibZ3WPgBGP8nBRJoWibVDhKQpWm8/640?wx_fmt=png&from=appmsg "")  
  
实时 Botnet C2 基础设施监控（来源：Whatoblock）  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsrf7GlSzOVAFSibc7eSLh8ezJXWVSAaFPa0gAPGvTwCtic9LT3AKAMzYtVZFGZibs4fGN8oBbXnKdXm11NjLQ1BlTSLzKkgdrbx8/640?wx_fmt=png&from=appmsg "")  
  
（来源：Shodan）  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnunXvgKGFO60YaRUp7yNlDoLXWejyqzfbqkR4Ur3ibI8W0FJqrY0aulORGZa2ZXCVypAzDt82YFaq2enhkqvwaQibMskEnl9JAKI/640?wx_fmt=png&from=appmsg "")  
  
（来源：Censys）  
## 3. 攻击面映射  
  
侦察之后，下一步是理解应用如何运行 —— 这叫做**攻击面映射（Attack Surface Mapping）**  
。  
  
测试者会探索：  
- 所有参数  
  
- API 接口  
  
- 用户角色  
  
- 业务流程  
  
重点关注：  
- id  
、user_id  
、account_id  
  
- /api/v1/users  
  
- 登录 / 重置密码 / 2FA  
  
- 普通用户 vs 管理员差异  
  
示例：  
```
```  
  
尝试用普通用户访问管理员接口。  
  
工具：  
- Burp Suite  
  
- Postman  
  
- Chrome DevTools  
  
- FFUF  
  
```
```  
## 4. 漏洞发现  
  
真正的漏洞挖掘阶段。  
### 1. 越权访问 / IDOR  
  
修改请求中的 ID：  
```
```  
  
改为：  
```
```  
  
如果能访问他人数据，即为 Broken Access Control。  
### 2. 认证与会话问题  
  
检查：  
- 登出后 Token 是否仍有效  
  
- 每个请求是否验证 Session  
  
- 是否可绕过 2FA  
  
示例：  
```
```  
### 3. 业务逻辑漏洞  
- 优惠券重复使用  
  
- 跳过支付  
  
- 跳过 OTP  
  
### 4. 参数篡改与响应分析  
  
关注：  
- 状态码变化  
  
- 响应大小差异  
  
- 错误信息差异  
  
## 5. 利用与漏洞链  
  
真实攻击往往是**漏洞组合拳**  
。  
  
例如：  
- IDOR → 数据泄露 → 提权  
  
- 弱认证 → 会话复用 → 账户接管  
  
- 暴露 API → 管理接口 → 数据泄露  
  
## 6. 真实攻击链示例  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnslP4upoykDYicl0vMhTykDNBhRrlrL2Ql9FL3vfVjhnweTnyoXSS3NCYFuU9mzc4AjnytUibeRp6874OlK9oGoyMeQxlqYupuEE/640?wx_fmt=png&from=appmsg "")  
  
攻击流程：  
1. Recon → 发现 api.target.com  
  
1. 找到 /api/v1/user?id=123  
  
1. 修改 ID → IDOR  
  
1. 收集邮箱  
  
1. 利用弱密码重置流程  
  
1. 账户接管  
  
1. 提权至管理员  
  
影响：完整账户控制 + 敏感数据泄露  
## 7. 检测与防御  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvlqQREicy3tzYeH7ibZEU4GvI2jcKUemcFMiat1l6K7NsWbA33dvbffrxwrh1n5vxzQhG0FupCYfeicZlgGzJ2EP2YAosUP1vfmYw/640?wx_fmt=png&from=appmsg "")  
  
SOC 应监控：  
- 子域扫描激增  
  
- 大量 401 / 403  
  
- 参数快速递增  
  
- API 枚举  
  
- 连续 ID 访问  
  
按 Enter 或点击查看原图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnue2NsC9gaSa7SL5dQ2rCXYcB2lvSGCXxV6DhJsQmicrYL02oT52HwjK83q2H2Vib81wX3aQvmE2qF70vjJbMFewf1CmRsj0xMII/640?wx_fmt=png&from=appmsg "")  
  
IP 行为情报监控（来源：Whatoblock）  
### 应记录的日志  
- 用户访问模式  
  
- API 请求频率  
  
- 失败登录  
  
- 权限变更  
  
- 敏感数据访问  
  
### 安全设计实践  
- 对每个对象做授权校验  
  
- 验证资源归属  
  
- 实施限速  
  
- 持续异常检测  
  
- 最小权限原则  
  
## 8. 核心总结  
- 攻击者流程是可预测的  
  
- 许多漏洞源于暴露资产  
  
- Broken Access Control 仍最常见  
  
- 强日志与监控是早期检测关键  
  
## 9. 结论  
  
有效防御的前提是：  
> **像攻击者一样思考。**  
  
  
理解从侦察到利用的全过程，能够帮助团队：  
- 提前发现威胁  
  
- 更快响应  
  
- 构建更安全系统  
  
安全不再只是修复单个漏洞。  
  
而是缩小可见性盲区，构建能够**检测、抵抗和响应**  
威胁的系统。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/R98u9GTbBnt63H5HeVvH57DuhexHibDk6RPsjic3IV29yTdJckoNVdiaqYNWWhp8nZK5NKV1Rm3dD1WnpKR6HEnVVfTcemicYzaw9HWDooYoZLI/640?wx_fmt=gif&from=appmsg "")  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnurorYBauV1Nfudk6ShfOslGndYT1oJLNwGTDW1BlABdMPck06ZA2IfDTEFSWQYkfvcFGPQcWjpJvSdgGaSkIRTTbfticTLBZDA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
