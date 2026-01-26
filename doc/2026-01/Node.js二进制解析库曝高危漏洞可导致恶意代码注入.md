#  Node.js二进制解析库曝高危漏洞可导致恶意代码注入  
 FreeBuf   2026-01-26 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39HonLcKiaspBzoEOs6Ltos7zKTcuPFicoMnGUbSuFkNYXaTILAEB29WF3rM9tPHN6SHvxDTBMVOTsg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part01**  
## 漏洞概述  
  
  
Node.js二进制解析库（binary-parser）被发现存在一个高危代码注入漏洞（CVE-2026-1245），影响2.3.0之前的所有版本。该漏洞允许攻击者在应用程序使用不可信输入构建解析器定义时执行任意JavaScript代码，可能危及应用程序完整性和系统安全。  
  
  
**Part02**  
## 技术细节  
  
  
该库原本设计用于以声明式语法简化二进制解析器的编写，但存在危险的代码生成缺陷。其运行时通过Function构造函数动态生成JavaScript代码，关键问题在于用户提供的解析器字段名称和编码参数未经任何验证或净化处理就被直接拼接到生成的代码中。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39HonLcKiaspBzoEOs6Ltos7TZohKDgJQrdJ5l1Gf6vBVBDokB2jficicmaOqF6r8PnNaaXwwyy8DrXQ/640?wx_fmt=png&from=appmsg "")  
  
  
**Part03**  
## 攻击场景  
  
  
当应用程序将不可信或外部提供的数据传入解析器字段名称或编码参数时，未经净化的值会篡改运行时生成的JavaScript代码。这种操纵使攻击者能够以Node.js进程的完整权限执行任意代码。需注意的是，仅使用静态硬编码解析器定义的应用程序不受此漏洞影响。  
  
  
成功利用该漏洞可能导致：  
  
- 在Node.js进程上下文中执行任意JavaScript代码  
  
- 根据部署环境和应用权限，可能实现本地数据未授权访问和应用程序逻辑篡改  
  
- 执行系统命令或在网络基础设施中进行横向移动  
  
- 处理第三方数据的企业级应用面临更高风险  
  
**Part04**  
## 修复建议  
  
  
厂商已发布2.3.0版本，实施了输入验证机制并修复了不安全的代码生成方式。CERT/CC建议立即采取以下措施：  
  
- 将binary-parser升级至2.3.0或更高版本  
  
- 审计应用程序中所有使用外部数据源构建解析器定义的情况  
  
- 对解析器配置参数实施严格的输入验证  
  
- 避免将用户可控值传入解析器字段名称或编码参数  
  
**参考来源：**  
  
Critical Vulnerability in Binary-Parser Library for Node.js Allows Malicious Code injection  
  
https://cybersecuritynews.com/node-js-binary-parser-library-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334254&idx=1&sn=60c1a1f106cdbab728bc207a35262d08&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
