#  AI生成恶意软件利用React2Shell漏洞攻击Docker，低门槛威胁激增  
 FreeBuf   2026-02-11 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0zLepfzUY1vR01f8Y7KJfYXDqaOADfdmQUGwpMRGdLAiblmoqribw1Vof6Q3YtSzQvO17dX5lq44iamAAtIjI00oAmRvGKXofs5A/640?wx_fmt=png&from=appmsg "")  
  
  
**Part01**  
## React2Shell漏洞遭利用  
  
  
Darktrace公司"CloudyPots"全球蜜罐网络检测到一场完全由AI生成的恶意软件活动正在积极利用"React2Shell"漏洞。此次入侵事件突显了网络犯罪的关键转变：攻击者正在利用大语言模型（LLMs）降低实施有效网络攻击的技术门槛。  
  
  
Darktrace对事件的分析指出，"vibecoding"（AI辅助软件开发）趋势正在兴起，攻击者严重依赖LLMs快速生成功能性代码。虽然这种做法加速了合法开发，但同时也使低技能威胁行为者能够轻松制作复杂的漏洞利用工具。  
  
  
攻击者针对Darktrace的Docker蜜罐发起攻击，该环境专门设计为在无认证情况下暴露Docker守护进程。这种模拟云环境中常见错误配置的设置，使攻击者能够通过Docker API发现守护进程并启动攻击链。  
  
  
**Part02**  
## 从Docker API到XMRig的攻击链条  
  
  
入侵始于攻击者生成名为"python-metrics-collector"的恶意容器，该命名试图伪装成合法的遥测服务。容器配置了启动命令，在获取主要有效载荷前先安装curl、wget和python3等必要工具。  
  
  
攻击序列分为两个阶段：  
  
- 依赖项获取：容器从Pastebin URL（hxxps://pastebin[.]com/raw/Cce6tjHM）下载所需Python包列表  
  
- 有效载荷执行：攻击者从_hxxps://smplu[.]link/dockerzero_获取并执行Python脚本，该链接重定向至已被平台封禁用户"hackedyoulol"的GitHub Gist  
  
技术分析显示该Python有效载荷具有明显的LLM生成特征。与通常追求简洁并采用重度混淆的人类编写恶意软件不同，该脚本包含详细注释，其前言写道："具有漏洞利用框架的网络扫描器——仅用于教育/研究目的"。这些痕迹表明攻击者可能通过将请求伪装成教育练习来"越狱"安全对齐的LLM。GPTZero检测工具评估显示76%的代码为AI生成。  
  
  
脚本结构异常清晰，采用"精心设计的Next.js服务器组件有效载荷"强制触发异常并显示命令输出，这是React2Shell漏洞利用的核心技术。  
  
  
尽管投放手法复杂，但攻击活动的最终目标是劫持资源进行加密货币挖矿。脚本成功部署了XMRig挖矿程序（6.21.0版），配置为通过supportxmr矿池挖掘门罗币（XMR）。通过分析攻击者钱包地址，研究人员追踪到该活动已感染约91台主机，累计产生0.015 XMR（约合5英镑）。  
  
  
虽然经济收益微不足道，但操作影响严重：低技能攻击者使用主要由AI创建的工具集成功入侵了近100个系统。值得注意的是，该恶意软件缺少自我传播的"蠕虫"组件，这对于针对Docker的威胁而言并不常见。传播逻辑似乎由远程控制，初始连接来自印度住宅ISP注册的IP地址_49[.]36.33.11_。  
  
  
"React2Shell"攻击活动表明，AI能有效弥合意图与能力之间的差距，使攻击者能够按需生成定制化、功能性的恶意软件。对防御者而言，这需要转向行为检测和快速补丁，因为静态签名可能无法应对LLMs产生的无限代码变体。  
  
  
**Part03**  
## 入侵指标(IoCs)  
  
  
传播者IP – 49[.]36.33.11  
  
恶意软件主机域名 – smplu[.]link  
  
哈希值 – 594ba70692730a7086ca0ce21ef37ebfc0fd1b0920e72ae23eff00935c48f15b  
  
哈希值2 – d57dda6d9f9ab459ef5cc5105551f5c2061979f082e0c662f68e8c4c343d667d  
  
  
**参考来源：**  
  
Threat Actors Exploiting React2Shell Vulnerability Using AI-Generated Malware  
  
https://cybersecuritynews.com/react2shell-vulnerability-ai-generated-malware/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
