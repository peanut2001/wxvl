#  已修复 | 微信Linux版本远程命令执行漏洞  
原创 微步情报局
                    微步情报局  微步在线研究响应中心   2026-02-11 10:20  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
漏洞概况  
  
  
Linux 版微信是腾讯基于 QT 或 Web 技术开发的官方客户端，让 Linux 用户无需通过 Wine 模拟即可在国产操作系统或主流发行版上直接收发消息和文件。  
  
近日，微步情报局监控到微信Linux客户端1click 远程命令执行漏洞已被修复。  
微步情报局已成功复现。  
经分析，Linux版本  
(包括银河麒麟等信创系统)  
微信中存在一个1click远程命令执行漏洞，攻击者可构造恶意文件名的文件（包括但不限于pdf，doc，xls等文件类型），诱使受害者点击查看，从而造成远程命令执行。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-3046）  
  
此漏洞  
无须用户权限  
，攻击者成功利用此漏洞可  
远程命令执行。  
  
漏洞处置优先级(VPT)  
  
  
**综合处置优先级：**  
高风险  
<table><tbody><tr><td rowspan="2" style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">基本信息</span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;"><section><span leaf="">微步编号</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">XVE-2026-3046</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">漏洞类型</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">命令注入</span></section></td></tr><tr><td rowspan="5" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用条件评估</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的网络条件</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">远程</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要绕过安全机制</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">对被攻击系统的要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">Linux操作系统</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的权限要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">无须用户权限</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要受害者配合</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是</span></section></td></tr><tr><td rowspan="2" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用情报</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">POC是否公开</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><span style="color: #d93025;font-weight: bold;"><span leaf="">是</span></span></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">已知利用行为</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">暂无</span></section></td></tr></tbody></table>  
漏洞影响范围  
  
<table><tbody><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">产品名称</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">深圳市腾讯计算机系统有限公司 | 微信客户端（Linux版本）</span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">受影响版本</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><span style="color: #d93025;font-weight: bold;"><span leaf="">由于腾讯在服务端做了修复，2026.2.11起所有版本都不受影响</span></span></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">有无修复补丁</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">有</span></section></td></tr></tbody></table>  
漏洞复现  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMiad16bVVxwVg5t2ib8Fu9dudibjva31PXicibTqM2dvApCOGWDVnRbNmTiaRjGiaiaBWPzFfuVVLnqcGXWN6FNJCDJ54YnGrhviczPGTg/640?wx_fmt=png&from=appmsg "")  
  
修复方案  
  
### 官方修复方案  
  
无需更新客户端，微信官方已在服务端修复此漏洞，发送恶意文件会显示发送中断，如下图所示：  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPXDvzBs06iaBAtfy2ib8CcmfVO1jib7XIb7X7ozpasViad90IhG9RFlKLcR2MYicc3V6oxzBnzPib0U84QQyT6AiavmBWNsoXqeLGBSo/640?wx_fmt=png&from=appmsg "")  
### 临时缓解措施  
  
1. 提升个人安全意识，不点击未知来源文件  
  
2. 禁用微信的文件自动下载功能，防止因误点造成的漏洞利用，配置方式如下所示：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEM6GY6S3p5IqiczwY5rviavuXF5ZFsLOiafGkBib46wdcjzx9YIWfFKQju0jcUIPPEXIJmEvvF7cINNBdib8w0U4Z22nHRN1LWibTbvk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOkY1bDneY3bXONLWZicBJK0Q1KIP1qrb5ZJ2ITYJhjd24duOibZibCuhzh4EJ8w19PaiaQlrnRFgkXGGcUMPmsfa2nZDpfNYMlvxs/640?wx_fmt=png&from=appmsg "")  
  
微步产品支撑  
  
  
微步漏洞情报于  
2026-02-10  
收录该漏洞。  
  
微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。  
  
微步终端安全管理平台OneSEC已于  
2026-02-10  
支持检测，检测ID：  
9107利用微信执行代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEO0qrxLPmgzoGYMfu6JDkbTERia9kx37LsWqNnm5O7w7retkJeRHbl3t2cWejKaibR3hwXgvNdkgvyk9IbyBbrlmicDRP6yLQeQlQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
- END -  
**微步漏洞情报订阅服务**  
  
  
微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：  
- 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；  
  
- 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；  
  
- 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；  
  
- 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新  
。  
  
  
扫码在线沟通  
  
↓  
↓↓  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
[点此电话咨询]()  
  
  
  
  
**X漏洞奖励计划**  
  
  
“X漏洞奖励计划”是微步X情报社区推出的一款  
针对未公开  
漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。  
  
活动详情：  
https://x.threatbook.com/v5/vulReward  
  
  
  
