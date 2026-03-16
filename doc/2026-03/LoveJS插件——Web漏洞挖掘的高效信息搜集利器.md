#  LoveJS插件——Web漏洞挖掘的高效信息搜集利器  
原创 m3x1
                    m3x1  梦醒安全   2026-03-16 00:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Aj9tsa4DmOmra6EI659XoNIvNn9wnMpVqicmqFmpJAwWJA0fw90SqBVOCEicpkLlV63QbNibrCx4BYT4JKia33l1Yg/640?wx_fmt=png&from=appmsg "")  
  
免责声明：本公众号内容仅用于知识分享和学习，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号梦醒安全及作者不为此承担任何责任，一旦造成后果请自行承担！  
  
PART.01  
  
前言  
  
在Web安全测试与漏洞挖掘工作中，信息搜集是核心前置环节，能否精准找到隐藏接口、敏感信息，直接决定后续测试的效率和深度。今天给大家分享一款专为安全从业者打造的浏览器插件——LoveJS，它能自动化完成隐藏接口提取、敏感信息嗅探，还支持批量URL验证等实用操作，大幅降低手工搜集成本，提升测试效率。  
  
PART.02  
  
介绍  
  
## 一、LoveJS核心能力  
  
传统的信息搜集方式往往依赖手工分析页面源码、抓包筛选接口，耗时且易遗漏。LoveJS针对这些痛点，集成了四大核心能力，覆盖从信息提取到操作落地的全流程：  
### 1. 智能信息搜集：挖深、挖全关键信息  
- **隐藏接口提取**  
：自动分析页面网络请求和加载的JavaScript文件，精准定位未在页面显式暴露的API端点、URL路径（如/admin/、/user/profile等后台接口），无需逐行翻看源码或抓包日志。  
  
- **敏感信息嗅探**  
：基于正则匹配技术，扫描页面源码和JS文件中的敏感数据——包括邮箱、手机号、AWS/阿里云等云服务API密钥、Access Key等，不放过任何硬编码的敏感信息。  
  
### 2. 高效操作工具：让搜集结果快速落地  
- **一键拼接URL**  
：支持自定义基础目录（如/api/v1/），点击“复制完整URL”即可自动将域名、基础目录、接口路径拼接，直接用于Burp、浏览器测试，无需手动拼接。  
  
- **批量打开URL**  
：将爆破得到的路径、待验证URL整理后粘贴（每行一个），插件可批量在新标签页打开，快速筛选可访问路径或暴露信息的页面。  
  
- **本地记事本**  
：测试过程中的思路、关键路径、待验证点可实时记录，数据本地存储，浏览器重启后不丢失。  
  
### 3. 灵活自定义配置：减少无效干扰  
- **自定义基础目录**  
：针对不同目标的接口规范，预设基础路径，适配各类系统的URL格式。  
  
- **域名黑名单**  
：可屏蔽第三方CDN、统计代码等无关域名，避免插件在非目标页面无效扫描，提升效率。  
  
### 4. 多浏览器兼容：适配主流测试环境  
  
完整支持Chrome（及基于Chromium的Edge）、Firefox浏览器，其中Firefox版本可从官方插件商店安装。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUsj5oVAjpN4sRlxYbibePmNG1F79iaY7muff3lcoUm9sMGfbecr4IWo5icQibDeOSuwTibGrIRfUric4iaYmC6Ye1M9qTIr6z6tZelE3Q/640?wx_fmt=jpeg "")  
## 二、实战利用  
  
结合实际测试场景，看看LoveJS如何落地解决问题：  
### 场景1：挖掘并验证隐藏API接口  
  
对https://example.com进行测试时：  
1. 访问目标网站，打开LoveJS插件面板，插件自动扫描并列出隐藏接口（如/admin/list、/user/profile）；  
  
1. 若已配置基础目录为/api/，点击“复制完整URL”可得到https://example.com/api/admin/list；  
  
1. 直接将URL粘贴到浏览器或Burp中，测试接口是否存在未授权访问、信息泄露等漏洞。  
  
### 场景2：批量验证爆破后的潜在路径  
  
通过字典爆破得到一批疑似路径（如/backup/、/config.json、/.git/HEAD）：  
1. 将路径整理为完整URL（每行一个），粘贴到LoveJS“批量打开URL”输入框；  
  
1. 点击“打开选中URL”，插件批量在新标签页打开链接；  
  
1. 快速浏览标签页状态，筛选出实际可访问、或暴露敏感信息的路径（如/.git/HEAD可能泄露源码信息）。  
  
### 场景3：搜集JS文件中的敏感信息  
  
测试目标网站的管理后台/用户中心时：  
1. 浏览多个核心页面，LoveJS自动扫描JS文件；  
  
1. 切换到“敏感信息”视图，查看插件识别出的硬编码信息（如admin@example.com邮箱、OSS访问密钥片段）；  
  
1. 基于这些信息进一步开展漏洞利用（如密钥泄露导致的云资源越权）、社会工程学测试。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGOErZb4ryb1a7rcwibW59ITKwkVkdicT1jEXfA5knP9uW3YSMOrXra1paFlyepPsj8uxsaojDB5MItMn3M8FIjCyvaBia6yFMIEBY/640?wx_fmt=png&from=appmsg "")  
  
  
  
PART.03  
  
总结  
  
LoveJS的核心价值在于“自动化搜集+高效落地”，将安全从业者从繁琐的手工分析、URL拼接、批量验证等重复性工作中解放出来，聚焦于漏洞挖掘的核心环节。在合规测试的前提下，用好这款工具能显著提升信息搜集的效率和深度，为后续的漏洞验证、利用打下坚实基础。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=49 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=50 "")  
  
**往期好文**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=53 "")  
  
  
  
[Nacos系列漏洞：风险点与综合利用工具详解](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484974&idx=1&sn=b8f9f5375db98f79537e8e97d38d49ab&scene=21#wechat_redirect)  
  
  
[实战解析：绕WAF的SQL注入变形技巧思路](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484981&idx=1&sn=24c9dcac423c627942ae8923fcc748d3&scene=21#wechat_redirect)  
  
  
[揭秘PDF与JS混编攻击：Polyglot文件的构造与防御](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485028&idx=1&sn=dcbdd3cd69fe767cd6cdbc24600e0556&scene=21#wechat_redirect)  
  
  
[深入理解OAuth 2.0：原理、流程与安全风险](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485029&idx=1&sn=560293b3792153ce6dd3de65975c0f0e&scene=21#wechat_redirect)  
  
  
[GNU Inetutils Telnetd 远程认证绕过漏洞（CVE-2026-24061）深度剖析与防护指南](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485064&idx=1&sn=322b4b95414b428d59ebf795466e5dbb&scene=21#wechat_redirect)  
  
  
[CVE-2026-24061漏洞快速检测工具](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485070&idx=1&sn=7513ea32faa0fa4ef543b4481e37ab99&scene=21#wechat_redirect)  
  
  
[YoScan：一站式资产收集神器深度解析](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485072&idx=1&sn=4fde1a17a98f82dfaab54ab15d7ed636&scene=21#wechat_redirect)  
  
  
