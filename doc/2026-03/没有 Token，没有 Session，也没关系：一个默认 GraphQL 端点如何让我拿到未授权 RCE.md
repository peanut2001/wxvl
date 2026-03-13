#  没有 Token，没有 Session，也没关系：一个默认 GraphQL 端点如何让我拿到未授权 RCE  
haidragon
                    haidragon  安全狗的自我修养   2026-03-13 04:09  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnu4h8jlLgyloHEYd4opwRmBbwdqY7C44rx830Oh9MSMj5rUbDFWOD8euJdrEj7xPPSLdL0w7ScO8dBCbe2OPalpDic913s6HgH8/640?wx_fmt=jpeg&from=appmsg "")  
  
那是一个寒冷的斋月夜晚。  
  
那种**所有人都睡了，房子安静得出奇**  
的夜晚。房间里唯一的光源，是终端屏幕发出的淡淡蓝光。  
  
我的咖啡还很热。  
  
而我有一种熟悉的感觉——  
一种**没有名字，但每个漏洞猎人都懂的感觉**  
：  
> “这里一定有什么东西，只是我还没找到。”  
  
  
我并没有追踪某个具体目标。  
没有 deadline，也没有特定任务。  
  
只有：  
- 我  
  
- Burp Suite  
  
- 一个当天刚拿到访问权限的 **Private Bug Bounty Program**  
  
我原本打算只花 **1 小时**  
看看。  
  
现在已经 **3 小时过去了**  
。  
# Recon 侦察阶段（看起来无聊，但其实最重要）  
  
我想诚实地谈谈 Recon 阶段。  
  
因为大多数 writeup：  
  
**要么跳过它，要么只用两句话带过。**  
  
但现实是：  
> **Recon 才是漏洞挖掘里最耗时间的部分。**  
  
  
大多数时候你会：  
- 枚举一堆没用的子域  
  
- 扫到被防火墙挡住的端口  
  
- 半夜 1 点在读你从没接触过的平台文档  
  
过程：  
- 很慢  
  
- 很枯燥  
  
- 但很关键  
  
在斋月的夜晚里，世界慢下来，夜晚更长，这个过程反而有点**冥想的感觉**  
。  
# 子域名枚举  
  
我从最基础的开始。  
  
常见的 Recon 工具链：  
```
```  
  
结果并没有什么特别激动人心的东西：  
- 一堆子域  
  
- 有些返回 **403**  
  
- 有些跳转到 **login 页面**  
  
- 有些完全死掉  
  
我就像平常一样：  
  
**一个一个慢慢看。**  
# 技术指纹识别  
  
在几个在线主机的 HTTP 响应头里，我注意到了一个东西：  
```
```  
# Liferay  
  
如果你做过企业级 Java 平台的漏洞挖掘，你会知道：  
  
看到 **Liferay**  
 就像看到一扇门，上面写着：  
> **“禁止进入”**  
  
  
但在漏洞猎人的世界里，这句话其实意味着：  
> **“这里可能藏着好东西。”**  
  
  
Liferay 是一个：  
- 巨大的 Portal 平台  
  
- 非常复杂  
  
- 功能非常多  
  
问题在于：  
- 很多功能 **默认开启**  
  
- 很少有人真正审核这些功能  
  
- 过去有很多 **CVE**  
  
更关键的一点：  
  
部署 Liferay 的团队通常只关注 **业务层**  
。  
  
他们往往：  
> **完全信任厂商默认配置。**  
  
  
而不会去研究：  
  
**这些默认配置到底暴露了什么。**  
  
我花了一些时间阅读：  
- Liferay 历史 CVE  
  
- 官方安全公告  
  
- HackerOne 上的 Liferay 报告  
  
我不是在找一个现成 exploit。  
  
我是在构建一个：  
  
**平台攻击面的心理地图**  
  
比如：  
- 有哪些功能  
  
- 常见 endpoint  
  
- 哪些地方容易 misconfig  
  
这部分 Recon 很花时间，但回报很高。  
  
因为你不只是跑工具：  
> **你是在理解目标。**  
  
# 目录扫描  
  
我阅读资料的同时，让 **feroxbuster**  
 在后台跑：  
```
```  
  
结果：  
- 大量 **302 → login**  
  
- 大量 **403**  
  
- Admin 路径被挡  
  
但我还是记下了一些有意思的路径。  
# Liferay 的 GraphQL API  
  
很多人不知道：  
  
**Liferay 7.4 默认带有 GraphQL API**  
  
端点：  
```
```  
  
这是 Liferay 的 **Headless Delivery API**  
。  
  
默认开启。  
  
官方文档也有。  
  
我是在一篇 **Liferay 开发者博客**  
里看到的。  
  
文章讲的是：  
> 如何用 GraphQL 查询 CMS 内容  
  
  
但我注意到一件事：  
  
**示例里没有任何认证。**  
  
我把这个细节记在脑子里。  
# WAF 与基础设施探测  
  
我又花了一些时间：  
- 看响应头  
  
- 查 CT logs  
  
- 比较响应时间  
  
确认了一件事：  
  
**前面有一个负载均衡器**  
  
后面至少有：  
  
**两个 backend 节点**  
  
这在后面会很重要。  
  
我也观察了 WAF 行为：  
- 有些路径触发 rate limit  
  
- 有些路径返回不同格式错误  
  
我大致画出了：  
  
**过滤规则最严格的地方**  
  
以及  
  
**最松的地方**  
# Recon 变成漏洞的那一刻  
  
然后我决定：  
  
**直接试一下 GraphQL endpoint。**  
  
没有特别期待。  
  
只是想看看。  
```
```  
  
我盯着终端。  
  
返回：  
```
```  
  
返回了完整 **schema**  
。  
  
没有认证。  
  
没有 login。  
  
没有 403。  
  
我把咖啡放下了。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsqCJ9fFzaEWRFp1HNf0Nfn9gsyQAcA0tTfRsDAxiaTnict7gyx5jWq83oYqpo1jxwfYAAicoo7lThib2U08TTficwySORvfcH9Ygmg/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntQPselVZ3cIr58kf8DHq1Bz5j6HUicmQWqeQQpgdmHstMgTUic2D2p03orlO0KcIlToVaEnqkGklTf4D6oFQDichAn6DWiblibc6Zs/640?wx_fmt=png&from=appmsg "")  
# 进入兔子洞  
  
GraphQL schema 返回：  
- **577 queries**  
  
- **990 mutations**  
  
全部：  
  
**无需认证即可访问。**  
  
这意味着：  
> 整个平台 API 完全暴露在互联网上。  
  
  
我开始浏览 schema。  
  
大多数是 CMS 内容相关：  
- articles  
  
- pages  
  
- documents  
  
这很正常。  
  
但后来我看到了一个东西：  
```
```  
  
对应的 mutations：  
```
```  
  
如果你了解 Liferay，你会知道：  
  
**Kaleo Workflow Engine**  
  
是它的工作流系统。  
  
工作流：  
- 用 **XML 定义**  
  
- 可以包含 **脚本**  
  
- 脚本语言支持 **Groovy**  
  
Groovy 在 JVM 上运行。  
  
Groovy 可以调用：  
```
```  
  
而 **ProcessBuilder**  
 可以：  
> 执行操作系统命令。  
  
  
此时我已经完全清醒了。  
# 读取服务器现有工作流  
  
我先查询服务器已有 workflow：  
```
```  
  
返回了：  
  
**所有 workflow XML 内容。**  
  
包括管理员之前创建的三个 workflow。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuK9ibVgMO8gFDY8N0Y5C72dxiaFoXI0mx0HrsJDB48MFp1Mzh2rRd1dOA770BicgXUDckDBlSQfZ7b6Cw189TnUib4Pn41HP1iahvg/640?wx_fmt=png&from=appmsg "")  
  
更离谱的是：  
  
里面已经有 **Groovy ProcessBuilder payload**  
。  
  
也就是说：  
> **管理员自己已经测试过这个 RCE 向量。**  
  
  
而且把 payload **留在生产数据库里。**  
  
这让我意识到：  
  
这不是理论漏洞。  
  
**有人已经走过这条路。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnvEdAN1lQskpSCxotxia3EMJsicT4vPIia12mY92l10As9oHIXG20I3a2yiauA5MUKHtsUWS6gSuBCcSyPNibmaRCKoicph7kyayXmvU/640?wx_fmt=jpeg&from=appmsg "")  
# PoC 演示  
## Step 0 确认 endpoint  
```
```  
  
匿名访问。  
## Step 1 读取 workflow  
  
返回所有 XML workflow。  
  
包括 Groovy payload。  
## Step 2 未授权写数据库  
  
发送 mutation：  
  
创建 workflow。  
  
里面包含：  
```
```  
  
服务器返回：  
```
```  
  
说明：  
  
**匿名用户成功写入生产数据库。**  
## Step 3 激活 workflow  
```
```  
  
返回：  
```
```  
  
生产环境已激活。  
## Step 4 服务器确认  
  
我尝试删除 workflow：  
  
但 Liferay 不允许删除 active workflow。  
  
返回：  
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnt2pPOBzDN2GwEmPg8DkmcTdRN82QI5AwUwTFgxeSK0wcgviayNkodEheFKrvvK3yuHlD7x4IKhPVLdFI4iaE3b03h4q3eR7TQdc/640?wx_fmt=png&from=appmsg "")  
  
这个错误证明：  
> workflow 已经真实存在于数据库。  
  
## Step 5 清理  
  
我做了 cleanup：  
1. deactivate  
  
1. delete workflow  
  
服务器恢复原状态。  
  
我没有触发 Groovy 执行。  
  
因为 PoC 已经足够证明漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnszrlx7YiavbRtCEKmicQm4hNjITHJp75R2LRtt8SyuOicVG8OsLElgjuMNxzKfXSeAzO8hfvbiblCibice5LrH9jbSq1qFicwcKNsaiak/640?wx_fmt=png&from=appmsg "")  
# 攻击链  
```
```  
# 漏洞本质  
  
其实一点都不复杂。  
  
只是：  
  
**Java resolver 少了三个认证注解。**  
  
结果：  
- 990 个 mutation  
  
- 完全暴露  
  
- 其中几个控制 **Groovy 脚本执行**  
  
而且：  
  
**完全不检查登录状态。**  
# 更诡异的一点  
  
数据库里已有 payload。  
  
说明：  
  
**有人早就知道这个漏洞。**  
  
而且在生产环境测试过。  
# 结果  
  
这个漏洞被标记为：  
  
**Duplicate**  
  
我晚了几个小时。  
  
奖金没拿到。  
  
但我得到：  
- 经验  
  
- 积分  
  
- 一篇 writeup  
  
有时候这些比奖金更重要。  
  
祝你好运。  
  
保持道德。  
  
让咖啡保持热度。  
  
— **0xTyrion404**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntlic5qlicSAVmrHBIkZicCduIcLjvcN7hStIYQ9woM6FKeZSWyZ7yZkqaX1PjxZ1yXNcEcp3JewRjY8Y1jE2hOeViaGSHeibYgUDTM/640?wx_fmt=png&from=appmsg "")  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsxpWiaUdXAuUNjxE5YFHqF7QiadAicn7G9hlMa50NU0dHIRBibxic1jS5aHYnu7fFBnEEwPcqLJlUgJ6kqJSvT8LR2TJ2my1xqBxZ8/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1 "")  
  
##   
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntJsvLfG7ObQLAkW7tP4Om4CYC3hoLLyafHAX3h81KfRD80dSsJKOCxkZ87tt58DzEV4wQPx9bRgA2vx3rHCz5zcibiczQeicqWjY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
#   
  
  
