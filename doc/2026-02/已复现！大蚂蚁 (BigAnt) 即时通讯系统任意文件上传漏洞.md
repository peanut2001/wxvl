#  已复现！大蚂蚁 (BigAnt) 即时通讯系统任意文件上传漏洞  
原创 微步情报局
                    微步情报局  微步在线研究响应中心   2026-02-04 01:59  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
漏洞概况  
  
  
大蚂蚁即时通讯系统是为企业提供实时消息传递、文件共享和团队协作的一体化通信平台。  
  
近日，大蚂蚁即时通讯官方发布通告，修复了大蚂蚁 (BigAnt) 即时通讯系统 任意文件上传漏洞。  
微步情报局已成功复现。  
经分析，该系统存在文件上传漏洞，漏洞源于系统 API 接口未对上传文件的类型及存储路径进行严格校验，攻击者可通过 file_info 参数允许通过 ../ 符号进行路径穿越，绕过预设的存储目录，将恶意文件直接写入 Web 根目录，从而获取服务器控制权限并窃取用户通信数据。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2025-33159）  
  
此漏洞  
无须用户权限  
，攻击者  
可通过该漏洞上传 Webshell，进而控制服务器并窃取用户通信数据，  
建议受影响用户  
尽快修复。  
  
漏洞处置优先级(VPT)  
  
  
**综合处置优先级：**  
高风险  
<table><tbody><tr><td rowspan="3" style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">基本信息</span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;"><section><span leaf="">微步编号</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">XVE-2025-33159</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">CNNVD编号</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">CNNVD-2025-42704091</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">漏洞类型</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">文件上传</span></section></td></tr><tr><td rowspan="5" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用条件评估</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的网络条件</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">网络可达</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要绕过安全机制</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">对被攻击系统的要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">无特殊要求</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">利用漏洞的权限要求</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">无须用户权限</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">是否需要受害者配合</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td rowspan="2" style="border: 1px solid #ddd;padding: 12px;vertical-align: top;font-weight: bold;background-color: #f8f9fa;"><section><span leaf="">利用情报</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">POC是否公开</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr><tr><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">已知利用行为</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">否</span></section></td></tr></tbody></table>  
漏洞影响范围  
  
<table><tbody><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">产品名称</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">杭州九麒科技有限公司 | 大蚂蚁即时通讯</span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">受影响版本</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">5.5.0&lt;=version&lt;=6.0.1（未安装1-260123143Z1413补丁）</span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;vertical-align: top;font-weight: bold;background-color: rgb(248, 249, 250);"><section><span leaf="">有无修复补丁</span></section></td><td style="border: 1px solid #ddd;padding: 12px;vertical-align: top;"><section><span leaf="">有</span></section></td></tr></tbody></table>  
漏洞复现  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLDfv0iaerjpNRg3SkV86M7biat3Dgk1wOSJB5p4RROlA5JMGRjzVia3LLic4t2HpXOY3AkBon4YmnpsA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLDfv0iaerjpNRg3SkV86M7bTicwC7E8UviaM4sehcyW8kIrnI84Dl5ZOxqamdfP6j5e2XDx6L9k9yxQ/640?wx_fmt=png&from=appmsg "")  
  
修复方案  
  
### 官方修复方案  
  
官方已发布修复方案，请访问链接下载：  
  
https://www.bigant.cn/article/news/435.html  
### 临时缓解措施  
  
1、如非必要，避免将资产暴露在互联网  
  
2、使用防护类设备进行防护，限制访问/index.php/***路径（完整路径通过漏洞情报查询），拦截file_info参数中包含"../"等路径穿越字符和恶意php语句的请求  
  
微步产品支撑  
  
  
微步漏洞情报于  
2025-09-09  
收录该漏洞。  
  
微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。  
  
微步威胁感知平台TDP于  
2025-09-17  
已支持检测，检测ID：  
S3100168160  
 ，模型/规则高于：  
20250917000000   
可检出  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLDfv0iaerjpNRg3SkV86M7bknqrl1LVj3QyxsDzwRqg1INnh7yZHmpIdUFaDcysWHhlndSsSxu8tA/640?wx_fmt=png&from=appmsg "")  
  
微步威胁防御系统OneSIG已支持防护规则ID为：  
3100121923  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLDfv0iaerjpNRg3SkV86M7bDlXMQGsicYSNO79Npb19B0z7U28MF1srcdroq0Dibs86BRlpFicnRibm7w/640?wx_fmt=png&from=appmsg "")  
  
##   
  
  
- END -  
  
  //    
  
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
  
  
  
