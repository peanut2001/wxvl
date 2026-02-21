#  Web-Check：一款全面的web网站信息和漏洞扫描工具  
原创 网安武器库
                    网安武器库  网安武器库   2026-02-21 12:03  
  
**更多干货  点击蓝字 关注我们**  
  
  
  
**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**  
  
**往期回顾**  
  
  
  
  
  
  
·[upload_forge：CTF利器-文件上传漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486388&idx=1&sn=f7c43e484275521abb27f417a26ddb60&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[Super Xray：一款基于 Xray 的漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486414&idx=1&sn=e344d3236ff2d3e83bffef09c1f7e1f7&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486351&idx=1&sn=5ad805f6aa58a79e2f21b777849db642&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[Havoc：现代化后渗透命令与控制(C2)工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486375&idx=1&sn=98207489b2de236c7eb471e09875c659&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[URLFinder：一款高效网页内部隐藏链接挖掘工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486361&idx=1&sn=763c9b7b0a992c4094efbb6263beeb10&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
介绍  
  
  
  
    Web-Check 是一个功能强大的开源网站分析工具，为任何网站提供全面、 按需的开源情报收集和安全评估。  
  
    Web-Check 允许用户深入了解给定网站的内部运作，包括服务器架构、安全配置、技术栈分析等多个维度的详细信息。该工具旨在帮助网站所有者、安全研究人员和开发人员轻松理解、优化和保护他们的网站。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJ1BSSPTrzHn9bMvEic4HsNLFKHyTQzGYdlePu0khzUg9zO3LoLm1uPnrDQ9OpVU7KgMBGpnTQZvuiaGpicZDKCn6kJrWrRibT0tw8/640?wx_fmt=png&from=appmsg "")  
  
  
  
项目地址：  
```
https://github.com/cdxiaodong/web-check-zh
```  
  
  
核心功能  
  
Web-Check 提供了丰富的分析功能，包括但不限于：  
```
服务器信息 ：IP地址、服务器位置、开放端口、路由跟踪
安全分析 ：SSL/TLS证书链、DNSSEC、防火墙检测、HTTP安全头部
DNS分析 ：DNS记录、邮件配置(DMARC/DKIM/SPF)、TXT记录
网站技术 ：技术栈识别、Cookies分析、HTTP头部、重定向链
SEO与合规 ：robots.txt、站点地图、社交标签、全球排名
性能与质量 ：Lighthouse质量指标、碳足迹分析
安全情报 ：恶意软件检测、黑名单检查、安全.txt分析
```  
  
  
技术架构  
  
##前端技术  
```
框架 ：React、Svelte、Astro
语言 ：TypeScript
UI组件 ：Framer Motion、Recharts、React Simple Maps
样式 ：Sass
```  
  
##后端技术  
```
服务器 ：Express.js、Node.js
核心依赖 ：
Puppeteer（网站截图）
Wappalyzer（技术栈检测）
Axios（HTTP请求）
Cheerio（HTML解析）
Traceroute（网络路由分析）
```  
  
  
应用场景  
```
网站所有者 ：评估网站安全状况，优化性能，改进SEO
安全研究人员 ：发现潜在漏洞，进行安全审计
开发人员 ：了解竞争对手技术栈，学习最佳实践
数字营销人员 ：分析网站SEO状况，评估竞争对手
```  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
部署  
  
  
  
方法一：从源代码部署  
  
前提条件  
```
Node.js ：版本 22.x（项目指定）
包管理器 ：npm 或 Yarn
Git ：用于克隆仓库
```  
  
部署步骤  
  
  
1. 克隆项目仓库  
```
   git clone https://github.com/
   Lissy93/web-check.git
   cd web-check
```  
  
2. 安装依赖  
```
   # 使用 npm
   npm install
   # 或使用 Yarn
   yarn install
```  
  
3. 构建项目  
```
# 使用 npm
   npm run build
   # 或使用 Yarn
   yarn build
```  
  
4. 启动服务  
```
   # 使用 npm
   npm start
   # 或使用 Yarn
   yarn start
```  
  
5. 访问应用 打开浏览器，访问 http://localhost:3000  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicI6byTuXzOqwRwyokmYP0h4gZ4gjxQ0pTX3Dxuco2RJ4efhm9HRA7IvFjorOdTcPS7sNNEIqnaZDK0KdAT0S3matGp7gExSM9s/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicK8YoxBFlvlPyp4qTqjHhVEraezR84gGroNdhbF3MZNBLlvBXIPQy3MYkXtnLQHPTU5At04drHpK3AaJicEWC36T2WAzuQpl7pI/640?wx_fmt=png&from=appmsg "")  
  
  
方法二：  
使用 Docker 部署  
  
前提条件  
  
Docker已安装并运行  
  
  
部署步骤  
  
1. 拉取 Docker 镜像  
```
   docker pull lissy93/web-check
```  
  
2. 运行容器  
```
   docker run -p 3000:3000 lissy93/
   web-check
```  
  
3. 访问应用 打开浏览器，访问 http://localhost:3000  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicItHibCCAob1AMsvJiaETicVbtib6vMGJRkWzdb8bNHy0skIgA5NAiajkm6WTXQS9sjprtXbGenTDCyBwxMCaGFvibGibz1b1Jwiau5p1E/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
