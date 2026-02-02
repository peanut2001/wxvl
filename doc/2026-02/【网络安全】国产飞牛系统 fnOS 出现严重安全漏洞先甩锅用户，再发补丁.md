#  【网络安全】国产飞牛系统 fnOS 出现严重安全漏洞先甩锅用户，再发补丁  
 嗨嗨安全   2026-02-02 00:20  
  
国产飞牛系统 fnOS 出现严重安全漏洞先甩锅用户，再发补丁  
  
近日，飞牛NAS用户群与论坛中大量用户反映设备突发异常，包括频繁断网、严重丢包、无法登录，同时系统出现异常高负载及未知进程。经查，飞牛OS（fnOS）被曝出多个高危  
0day漏洞，已遭黑客大规模利用。据估计，目前已有数以万计的设备被植入后门与挖矿木马，甚至可能被纳入僵尸网络，用于发起DDoS攻击。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPuCib72gwDsbaZGPVxEPRhQOWmqPMwP0saicib55MAgic8nr7nTgVGnbGVg/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPkibn8W53ciblXianqJ7ZribDhKJ0Q5zxbrKKnbEJicnu1j1Q8qK9Hn04icog/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1 "")  
  
以下是基于现有信息的梳理与整合：  
  
事件时间线与漏洞详情  
  
飞牛私有云fnOS是一款基于Debian Linux内核深度开发的国产、正版免费NAS操作系统。它专为家庭和个人用户设计，提供影视库（飞牛影视）、相册、文件管理、网盘挂载等功能，支持将闲置电脑、旧笔记本或Mini主机转化为安全、高效率的私有云存储。飞牛私有云fnOS出现严重0day漏洞，可以访问nas上任意文件（包括系统配置文件，用户存储文件）。  
  
目前已知1.1.18版本已经修复该漏洞，漏洞影响范围未知（1.1.18版本以下均可能受到影响），互联网部署数量较多，请及时排查！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHP6tib9ib2Z7d0mmTh9hwDtdBnmuebN9P5gdxmPpibU9av3oBltb8vQfc8A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2 "")  
  
1月21日起：已有零星用户报告设备异常，但未引起官方充分预警。  
  
1月30-31日：漏洞细节被公开，主要包括路径遍历0day（可越权访问系统文件）与WebSocket命令注入等高危漏洞。攻击者无需登录或仅需简单绕过验证，即可读取、篡改NAS上的所有数据，包括用户私人照片、视频、文档，乃至系统配置文件与私钥。  
  
影响范围  
  
几乎所有 1.1.15 之前版本 均受影响。  
  
官方虽在 1.1.15 和 1.1.18 版本声称修复，但社区反馈表明，相关攻击手段在新版中仍可能部分生效。  
  
攻击手法  
  
攻击主要针对公网暴露的Web界面（无论HTTP/HTTPS）。黑客利用路径穿越漏洞（例如通过构造特殊URL如 /app-center-static/...?size=../../../../）直接访问系统文件，进而植入恶意程序，如 gots、trim_https_cgi、snd_pcap.ko内核模块等。  
  
1.路径穿越 / 未授权访问  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPo0neo4icJ89DdechLMqWiaFz2Ho57zzVw2LhrnfjPmlx83jqfHefGtPA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3 "")  
  
在特定条件下，**无需正常登录即可访问系统路径或接口**  
，即使你没有主动对外开放管理页面，也可能存在风险。  
  
2.后门程序与异常进程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPEGYnJfasQPe41cG9dhTtNS0NEhYribRjzfZ5UmlWALMFJXPicMaibcdLA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPsf56W1xa7OqnUVnJrhyHicUnYQUubEvFY4icQrtZvexlzWS4T94pkQHQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5 "")  
  
部分用户发现系统中存在异常文件或进程，例如：  
- • 不明可执行文件  
  
- • 自动启动的未知服务  
  
- • 被修改的启动脚本  
  
- • 系统无法更新  
  
3.官方修复不够“彻底”  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPkLoibjRcSRy6UNrW1E9NpzLcWw5YSkULTOCYlsX9qhciaY9Q7xEFyVXg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6 "")  
  
虽然官方版本更新中提到已修复相关问题，但**社区中仍有用户反馈漏洞并未完全解决**  
，存在残留风险。  
  
4.终端插件远程命令执行漏洞  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPO8pcMeRpCiaofkGiafvbr3BLGyfaFqSkVNGMBxjpmwEaoUibiad5mx31ow/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPynGzFrVyNWPF4J3j4k0VWNOxVt3nyrFVLh6TZZ9rz98QwV0ia3xcwqw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPD9FgtNlibbvx4aGKjWffZywYcH0sZP3JajektL9mZEyicPCIlKpCLODg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9 "")  
  
特征表现  
- • 网络流量异常增大  
  
- • NAS 无故卡顿、掉线  
  
- • 后台出现陌生连接 IP  
  
- • 系统日志中存在不明进程或命令  
  
- • 明明没操作，却出现配置变更  
  
造成的后果  
  
系统层面：出现恶意进程监听异常端口（如57132）、启动脚本被篡改、日志被清空、审计记录遭删除。  
  
功能破坏：导致DNS解析失效、系统命令（如cat）被替换、网络严重异常。  
  
安全威胁：设备被用于下载远端木马（关联IP：45.95.212.102、151.240.13.91），部分设备被纳入僵尸网络，已监测到国内相关攻击流量达TB级别。  
  
影响规模  
  
据统计，全网暴露飞牛OS Web界面的设备超过 30万台，其中已确认被入侵的数量可能高达数万台。  
  
重要提醒  
  
如果您的飞牛NAS设备开启了公网访问（包括直接暴露、内网穿透、Cloudflare Tunnel、FRP等方式），则面临极高的入侵风险，建议立即采取隔离、排查与升级措施。  
  
官方态度  
  
飞牛官方对此次漏洞事件的应对引发了广泛批评。  
  
官方最初回应时，将入侵原因归咎于“用户使用HTTP明文访问”，建议关闭公网端口。然而，社区技术专家迅速证实，漏洞本质与通信协议无关，即使设备开启HTTPS、双因素认证及强密码，依然能够被攻破。  
  
2月1日凌晨，官方紧急发布fnOS 1.1.18版本，声称已修复漏洞并增加了自动查杀功能。但大量用户升级后发现，恶意文件仍可能残留，部分设备甚至出现升级后无法启动的“变砖”情况。  
  
从漏洞出现到大规模爆发历时十余天，官方的应对流程——未能及时预警、初期归咎于用户操作、事后紧急修补——严重影响了用户对其安全响应能力的信任。  
  
应急响应  
  
第一步：立即隔离设备  
  
物理断网：拔掉NAS网线，或直接在路由器中禁用该设备的访问。  
  
关闭所有远程访问通道：立即停用内网穿透（如FRP、Tailscale）、反向代理（如Cloudflare Tunnel）等一切将NAS服务暴露至公网的设置。  
  
第二步：检查是否已被入侵  
  
通过SSH登录设备后，执行以下命令进行检查：  
```
# 检查常见恶意进程文件
ls -l /usr/sbin/gots 2>/dev/null  # 若存在输出，则可能已中招

# 检查启动脚本是否被篡改
cat /usr/trim/bin/system_startup.sh  # 查看末尾是否有异常wget或curl下载命令

# 检查恶意内核模块
ls /lib/modules/*/snd_pcap.ko 2>/dev/null  # 若存在，则系统已被植入
```  
  
第三步：紧急清理与加固  
  
操作顺序建议：先清理，再升级。  
  
1.优先使用官方清理脚本（相对最安全）：  
```
curl -fsSL http://static2.fnnas.com/aptfix/listautostart.sh | bash
```  
  
请注意：在安全事件期间运行任何远程脚本均有风险，请务必通过官方渠道核实脚本地址。  
  
2.或使用社区已验证的清理脚本：  
```
wget https://file.tongrens.top/sd/L2PjYOsr/clear.sh && chmod +x clear.sh && ./clear.sh
```  
  
3.手动深度清理（如果熟悉命令行）：  
  
在执行前，请确保已备份重要数据。主要操作包括：  
  
移除关键恶意文件（如 /usr/sbin/gots、/snd_pcap.ko 等）。  
  
清理被篡改的启动项（/etc/rc.local、/etc/modules）。  
  
完成后重启设备。  
  
4.升级系统与加固配置：  
  
重启后，立即升级到官方发布的最新版本（如1.1.18或更高）。  
  
严禁将NAS管理界面直接暴露于公网。务必启用系统防火墙，严格限制入站连接。  
  
关闭SSH密码登录，仅使用密钥认证；可考虑部署 fail2ban 等防暴力破解工具。  
  
长效安全防护原则  
  
1.摒弃“公网直连”：NAS不应直接在公网暴露。所有远程访问必须通过VPN（如WireGuard、OpenVPN） 或具备强认证机制的安全隧道进行。  
  
2.严格执行备份策略：对重要数据遵循 3-2-1备份原则（至少3份副本，2种不同介质，1份异地/离线保存）。  
  
3.建立主动监控：定期检查系统进程 (top)、网络连接 (netstat、ss) 及资源使用情况，设置异常告警。  
  
4.审慎进行系统更新：在安装大版本更新前，建议优先备份系统配置与数据。  
  
官方控评  
  
评论区精选各种丧事喜办+阴谋论+带节奏的评论  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPWHA8nKH10dkI9XE1jOUQnIdNyB5zhFr4NeB80nTUWED2oUzLkNB9hw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=10 "")  
  
好了，赶紧升级吧各位，小心你的小姐姐成别人的了！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR12Qtr0l3X9hO0yDU6ia3BibHPSQTmjNINHxcKx03fEvYROYSdxU0FvMUDplNoZfq5nCpVIJ7eabAapg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=11 "")  
  
本文来源:利刃信安  
  
https://mp.weixin.qq.com/s/CI4YQn-WMwXUwidgpOX1yQ  
  
  
