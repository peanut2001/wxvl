#  如何用AI挖掘帆软表达式注入0day  
 哈拉少安全小队   2026-01-22 00:58  
  
# 前言  
  
前段时间帆软发布了安全公告修复了一个前台RCE漏洞。  
  
其实我在10月25号对比新旧版本的时候就发现帆软在10月20号修复了一个SQL注入绕过漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJCFpGe2m783lqAZPbjgcKsX2PJaXahGOTkHQw6Lb3hw0Z5pdoXfAxjw/640?wx_fmt=png&from=appmsg "")  
  
这里新增了一个关键词VACUUM  
，官方修复的这个漏洞利用链是先通过接口获取sessionid  
再利用export/excel  
接口构造SQL语句写入Webshell。  
  
实际还存在其他更为简单更为通用的接口可以利用SQLITE  
写文件。  
  
所以下面我只会**简单分析**  
官方修复的这个利用链  
  
**重点放在怎么通过AI来找到这个SQL注入写文件的绕过上面。**  
  
分析调试帆软漏洞推荐使用  
  
https://github.com/cwkiller/ClassLinefix  
  
建议大家把公众号“漫漫安全路”设为星标！因为公众号现在只对常读和星标的才会推送。操作方法：进入公众点击右上角的【...】，然后点击【设为星标】即可。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHVACNjeL9O7lrJ1rZUO62KZXl2vKe80FNrfxfjcpo8eLHB3vgW3UJCcBLTHhsmeKg7yIrDsIx79IQ/640?wx_fmt=png&from=appmsg "")  
# 获取sessionid  
  
帆软在很久以前也有一个前台RCE和这次的利用链一致，先获取sessionID然后通过模板注入构造SQL语句写入shell。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJpfn9SUoakPib143iaDPs8IoJ2DKk6tnw21QjG5oYojE4wzib9QqlbVsDg/640?wx_fmt=png&from=appmsg "")  
  
但是这个获取sessionID的漏洞似乎在年中被修复了，我使用2025.8.7版本测试显示如下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJicdVDibQ2d8LcIC7ibP9bCwWe9BtM5OfOKrBq8IekZB7OgTqnIf5DqaIw/640?wx_fmt=png&from=appmsg "")  
  
通过调试发现进入拦截器后会经过com.fr.decision.webservice.interceptor.handler.ReportTemplateRequestChecker#acceptRequest  
的检查![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJIyROwKNHgeQ3IicJ9QWfPWgNMdwZyA3otpgwV0iaPBCFGuiavNqBeTgdQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJiaZWC2BK8ylyxT2fuicicSCPaSauhyz61XIQs7yKIH6Xkz9LdX3vLxw5g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJUEcQdziaxTYlVTiamw7WpyUxmaG1xYqzShEpKNsJ54UFH57SGK71CVAQ/640?wx_fmt=png&from=appmsg "")  
当这四个参数不为空时需要检查用户token  
，而我们上面获取sessionID  
用了reportlet  
参数所以会被重定向到登录。  
  
实际上只需要换成不在检查范围里的其他参数然后构造一下即可绕过这个检查获取sessionID  
这里留给读者自行研究分析。  
# export/excel 接口表达式注入  
  
入口点com.fr.nx.app.web.controller.NXController#largedsExcelExportV9  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJuz5WzCwX9Had2WYZloUqRKPKWFZnK2xC2epbCuyx1eQaeNk3mWDoicA/640?wx_fmt=png&from=appmsg "")  
后面会进入![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJaibaA2yRDtZzgmtutt4jba2Uiawq6RFnhU85rYAJ1GrLw1wb3rJonNaA/640?wx_fmt=png&from=appmsg "")  
  
  
触发漏洞的逻辑在initCreator  
这里获取__parameters__  
参数我们设置为{}  
使其不报错即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJL6pZ1kPoaGrt3D5YGiawspibHErrz7ibElAeMg5cYA5KqEHRAn8YhHuqQ/640?wx_fmt=png&from=appmsg "")  
关键的值都是通过getEntity  
获取  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJC9ctW2an72sqPVh3MHA1vjuNKkJYBiaJ8MH8QEvibRtxRMaxJJb6Mkkg/640?wx_fmt=png&from=appmsg "")  
通过params  
参数获取，然后使用帆软自定义的一种xml反序列化来还原对象，我们主要设置Parameter  
及DsName  
即可。![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJu7liaaYXDeicpDudmn5BPBTXlLPyFOCUQkaibLu3ttUnVDXl0OftkliaYA/640?wx_fmt=png&from=appmsg "")  
sink点为com.fr.script.Calculator#evalValue  
这里可以执行帆软定义的一些函数，之前模板注入最后也是调用到这里。  
  
调用帆软的writeXMLableAsString  
方法生成参数值进行测试![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJD7sw7PjIkz31icLkVfwUaOXDUyE1zbBOckamFyZv1slkNyr6xvKu8IA/640?wx_fmt=png&from=appmsg "")  
  
  
成功执行表达式![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJjt0f15XqTCVlh1hInyWzOIscdzV2KjicBaZjWkH6vj1qzmfhD2dCicHA/640?wx_fmt=png&from=appmsg "")  
  
  
结合之前的模板注入和最开始的代码对比  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJCFpGe2m783lqAZPbjgcKsX2PJaXahGOTkHQw6Lb3hw0Z5pdoXfAxjw/640?wx_fmt=png&from=appmsg "")  
  
可知使用SQL函数调用SQLITE数据库的VACUUM  
关键字来写入webshell。  
  
这是一种新的SQLITE执行SQL语句写shell的方法，下面我们用AI来看看怎么找到这种方法。  
# 如何用AI找到SQLITE写文件的新方法  
  
我自己之前曾尝试过FUZZ、查看SQLITE文档、使用AI均没有找到如何绕过帆软的SQL检测写文件的方法。文档里还是有VACUUM  
的用法，只不过我没有注意到。  
  
当我看到这个补丁时我再一次使用AI，发现只需稍微变换提示词即可找到。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJDsibyDpkIFehibfSaLc10xn5FDmhFOKNYLmS89eFnClonW0ceIdyZqgQ/640?wx_fmt=png&from=appmsg "")  
  
这是我当时挖掘时和AI对话的提示词，后面我发现变换一种方式不在问AI SQLITE如何使用SQL语句写文件，换成**SQLITE里有哪些命令可能涉及文件操作**  
AI很快给出答案！！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJLGS8vW0DaFD5wIRNjuDAiaCHiaIdicuxic8ia1ru5KS8icCwR5mOULNF8Haw/640?wx_fmt=png&from=appmsg "")  
将数据库保存到新文件，意味着我们只需要在数据库里插入shell脚本，然后导出后即可获取shell。然后我们注意到insert也被禁用了，询问AI如何不使用insert插入数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJ4R3ogurwWRSnJKuGxH52RcOj5kIPnm8ortJI7BrpIL8U0CGCd5ydNQ/640?wx_fmt=png&from=appmsg "")  
我们组合SQL语句然后使用表达式注入写入shell进行测试。  
```
CREATE TABLE testxxx AS SELECT x'shellhex' AS id;VACUUM INTO "../webapps/webroot/shell.jsp";
```  
  
发现由于数据库里数据太多写入的shell无法解析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJjicUtJAykg9JMbwmU814vZH6Rdhtz8pYbicQDvYdtLYMNHxxNgICepCA/640?wx_fmt=png&from=appmsg "")  
因为这个FRDemo数据库全部是测试数据，所以我们可以清空数据库，然后再创建表插入数据导出shell。继续询问AI  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJib85GcksKp4dic8q54iaSSu8oxqgwibr6pgAicBa4dMo82QjD33UNqeMPIw/640?wx_fmt=png&from=appmsg "")  
  
所以得到最终的SQL语句  
```
PRAGMA writable_schema = 1;DELETE FROM sq1ite_master WHERE type IN ('table', 'index', 'trigger');PRAGMA writable_schema = 0;VACUUM;CREATE TABLE testxxx AS SELECT x'shellhex' AS id;VACUUM INTO "../webapps/webroot/shell.jsp";
```  
  
由于需要执行多条SQL语句需要多次使用SQL函数可使用||  
连接多个SQL函数这样只需一次发包即可写入shell  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJxwKUdTWyBz3PuZjZOgw08FMdqHxQl4ptiaeFIDWhuvNZ9FPZiaHrDSew/640?wx_fmt=png&from=appmsg "")  
  
最终效果  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AKz6F8hGbHXWTjLGdYT2rAJ60Q6geOcJtl9MZPhaiaQp5c1icdMTqbj8vwiaR5Zm0wqzaYJic6VibVoyytLQw0n6ybQ/640?wx_fmt=png&from=appmsg "")  
  
**上述操作会清空帆软的FRDemo数据库，虽然都是测试数据还请谨慎操作。**  
  
可使用下面两种方法先备份原有数据库。  
  
1.访问/webroot/help/FRDemo.db  
路径下载数据库文件  
  
2.先使用VACUUM INTO "xxx.bak"  
备份数据库，再进行后续操作  
  
但是这两种方法都需要shell以后替换数据库文件才能恢复数据库  
# 总结  
  
整个漏洞利用链可以分为以下几个关键步骤:  
## 1. 获取sessionID  
- 早期版本可通过特定接口直接获取sessionID  
  
- 新版本增加了ReportTemplateRequestChecker  
拦截器检查  
  
- 绕过方法：避免使用reportlet  
等被检查的参数，改用其他未被拦截的参数构造请求  
  
## 2. 表达式注入触发  
- 入口点：/webroot/decision/nx/report/v9/largedataset/export/excel  
接口  
  
- 通过params  
参数传入精心构造的XML序列化对象  
  
- 最终调用到com.fr.script.Calculator#evalValue  
执行帆软表达式  
  
## 3. SQL注入写Shell  
- 利用帆软内置的SQL  
函数执行SQLite语句  
  
- **核心绕过技巧**  
：使用VACUUM INTO  
命令代替被禁用的传统写文件方法  
  
## 4. AI辅助挖掘的启示  
- **关键思路转变**  
：不要问"如何写文件"，而是问"哪些命令涉及文件操作"  
  
- AI能够快速梳理SQLite的文件相关特性（ATTACH、VACUUM等）  
  
- 通过多轮对话逐步完善利用链（如解决INSERT被禁用、数据库数据过多等问题）  
  
这个案例充分展示了**AI在漏洞挖掘中的价值**  
——通过合理的提示词设计，可以快速发现被忽略的功能特性，从而找到新的攻击面。同时也提醒开发者，**基于黑名单的防御往往不够完善**  
，需要从架构层面限制危险功能的调用。  
  
  
公众号专注于网络安全知识分享，主要为代码审计、攻防实战、  
WAF  
绕过等内容每周一篇期待你的关注。  
  
  
本文仅供安全研究和学习使用，由于传播、利用此文档提供的信息而造成任何直接或间接的后果及损害，均由使用本人负责，公众号及文章作者不为此承担任何责任。  
  
