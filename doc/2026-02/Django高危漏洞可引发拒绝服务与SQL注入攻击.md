#  Django高危漏洞可引发拒绝服务与SQL注入攻击  
 FreeBuf   2026-02-06 02:13  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0Y2AmHpfIAu4PveTDj2ckE0iaibcCrLRQCdHvst2WZ3vBalBAz5pXpvzfcrHAxyF05dOo0SNiaBPbSZVYPHe6nI39n85t7WrOuC8/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part01**  
## 漏洞概况  
  
  
Django 开发团队紧急发布安全更新，修复了影响多个版本 Python Web 框架的六个高危漏洞。这些漏洞涉及三个高危 SQL 注入漏洞和多个拒绝服务攻击向量，影响 Django 4.2、5.2、6.0 版本及主开发分支。  
  
  
**Part02**  
## SQL注入漏洞分析  
  
  
已披露的三个高危漏洞可能允许攻击者执行任意 SQL 命令：  
  
- CVE-2026-1207影响 PostGIS 用户，攻击者可通过 GIS 字段的栅格查询功能，将不受信任的数据作为波段索引参数触发 SQL 注入  
  
- CVE-2026-1287针对 FilteredRelation 功能，当精心构造的字典被传递给 annotate()、aggregate() 和 values() 等 QuerySet 方法时，可通过控制字符在列别名中实现 SQL 注入  
  
- CVE-2026-1312利用 QuerySet.order_by() 方法，当与 FilteredRelation 结合使用时，可通过包含句点的列别名实施 SQL 注入  
  
**Part03**  
## 拒绝服务漏洞详情  
  
  
同时修复的两个中危拒绝服务漏洞包括：  
  
- CVE-2025-14550影响 ASGI 实现，攻击者发送包含重复标头的请求会导致字符串重复拼接、超线性计算和服务降级  
  
- CVE-2026-1285针对 django.utils.text.Truncator 的 HTML 方法，当处理包含大量未匹配 HTML 结束标签的输入时，chars()、words() 函数及 truncatechars_html、truncatewords_html 模板过滤器会出现二次方时间复杂度问题  
  
此外，（CVE-2025-13473）低危时序攻击漏洞影响 mod_wsgi 认证处理器，攻击者可通过测量 check_password() 函数的响应时间差异枚举有效用户名，辅助暴力破解攻击。  
  
  
**Part04**  
## 漏洞影响版本与修复措施  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX35qcyNtkkEZSmnInA60320dmJZDapiblo0mUe2jtOLjgL6Oge1s9Jib7X9zU51KyYkgZB77jOFzRHXxnzagyQcEtE0BQYaI7WA8/640?wx_fmt=png&from=appmsg "")  
  
  
**Part05**  
## 漏洞影响版本与修复措施  
  
  
Django 团队已发布 6.0.2、5.2.11 和 4.2.28 版本补丁，所有用户应立即升级。各受影响分支的修复代码可通过 GitHub 变更集获取。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0NjQDqStyaMXU4z2hlS6Zia2ggT6ZSOY3YQdwkkm0ZDRiau8zD93ib0a1XIjiaRiboibluiaKBnWRBOMblma7hOQsWgyKeCFlbvFIibjQ/640?wx_fmt=png&from=appmsg "")  
  
  
安全公告特别强调，所有不受信任的用户输入在使用前都应进行验证。本次更新由 Jacob Walls 使用 PGP 密钥 ID 131403F4D16D8DC7 签署发布。  
  
  
**参考来源：**  
  
Critical Django Vulnerabilities Enables DoS and SQL Injection Attacks  
  
https://cybersecuritynews.com/django-vulnerabilities/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334777&idx=1&sn=e052da512a608ee2d0ee20b662e93404&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
