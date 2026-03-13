#  速修！泛微Ecology10多个远程代码执行漏洞  
原创 微步情报局
                    微步情报局  微步在线研究响应中心   2026-03-13 07:36  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
漏洞概况  
  
  
Ecology10 是泛微专为中大型组织打造的数字化运营平台，它基于微服务架构与低代码引擎，旨在帮助企业实现业务管理的智能化、平台化与全程数字化。  
  
近日，微步情报局监测到泛微官方发布通告修复了多个远程代码执行漏洞。  
微步情报局已成功复现。  
经分析，攻击者利用该系列漏洞可远程执行任何代码，从而获取服务器权限。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-2633 / https://x.threatbook.com/v5/vul/XVE-2026-2687/ https://x.threatbook.com/v5/vul/XVE-2026-2874）  
  
此漏洞  
无须用户权限  
，攻击者成功利用此漏洞可  
远程执行任意代码，获取服务器权限，  
建议受影响用户  
尽快修复。  
  
漏洞处置优先级(VPT)  
  
  
**综合处置优先级：**  
高风险  
<table><tbody><tr><td rowspan="2" style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">基本信息</span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;"><section><span leaf="">微步编号</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">XVE-2026-2633</span><span leaf=""><br/></span><span leaf="">XVE-2026-2874</span><span leaf=""><br/></span><span leaf="">XVE-2026-2687</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">漏洞类型</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">RCE</span></section></td></tr><tr><td rowspan="5" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用条件评估</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的网络条件</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">远程</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要绕过安全机制</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">对被攻击系统的要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">跨平台</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的权限要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">无须用户权限</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要受害者配合</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td rowspan="2" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用情报</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">POC是否公开</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">已知利用行为</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr></tbody></table>  
漏洞影响范围  
  
<table><tbody><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">产品名称</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">上海泛微网络科技股份有限公司 | E-cology</span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">受影响版本</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">&lt; E10安全补丁包 v20260312</span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">有无修复补丁</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">有</span></section></td></tr></tbody></table>  
漏洞复现  
  
  
XVE-2026-2633  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEPscUNpm8Ke9Oibab5JhsDpTmIkicfOS4c5cRU36bUsYKkfE6pz4ng4JiaYpgM5VgEibw8ZuqdYSkwVSqwoGl1B7touDV2QgpicgWPk/640?wx_fmt=png&from=appmsg "")  
  
XVE-2026-2874  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPmdNJujePWdf7g6icFgklibCXfBJJHOCSJylnvE9dt6rvORYflCwjGASyM3sUPtG8xQwgEUqw7KfUvlrNEIqcxlu9WIa8QNSnRk/640?wx_fmt=png&from=appmsg "")  
  
XVE-2026-2687  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEN5ibIGXa9PMJ3Ay6xhckIq5ibUYdFLuWlMCJmyhbvosTqksp3uxpxIYzPSRDgdHB3PhiaguECTzUA0926bhVKeXdVgJd02YV0YrY/640?wx_fmt=png&from=appmsg "")  
  
修复方案  
  
### 官方修复方案  
  
官方已发布安全补丁，请联系官方售后支持人员获取最新安全补丁。  
  
### 临时缓解措施  
  
1. 如非必要，避免将资产暴露在互联网  
  
2. 在不影响现有业务的情况下，在 nginx 中为 /papi/ 路径下的所有接口配置授权，最常用且最简单的方法是使用 Basic Auth  
  
微步产品支撑  
  
  
微步漏洞情报于  
2026-02-09  
收录该系列漏洞。  
  
微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。  
  
微步威胁感知平台TDP已于2026年2月12日支持检测，检测ID：  
  
XVE-2026-2874  
  
S3100174057、S3100174059、S3100174060  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEMn8tlme7AcL8VNTicia6zeqBc5nu5yqtdUsq1iaVRibxCR6l7LicHc0tXUCUbn4awoff7aP2TXu8w3gxtI8WKTWialftG7ryonAbIt4/640?wx_fmt=png&from=appmsg "")  
  
  
XVE-2026-2687  
  
S3100174056  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPQQkfmg565TrqzmbY7ibZ0zsw2QABNK0Kt9wHf6pWBJc1iaJXMuIjnxbMXcwKMx8UFbMbfbGCJHPBg0ibwlPceJ4nJuAq1JjRWfs/640?wx_fmt=png&from=appmsg "")  
  
XVE-2026-2633  
  
S3100174062、S3100174063  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEOOZX4HtIoEpoMROWEGINia7tk8r2PG7MRibQzfls6a6tRUc8ccjcl72cE20jSx546ZxwOiawqx1kYsm1jibOiakmYlSAuht7saJrzE/640?wx_fmt=png&from=appmsg "")  
模型/规则高于：  
20260212000000可检出 支持时间：  
20260212  
  
  
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
  
  
  
