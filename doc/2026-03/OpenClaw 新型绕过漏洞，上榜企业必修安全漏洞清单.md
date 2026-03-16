#  OpenClaw 新型绕过漏洞，上榜企业必修安全漏洞清单  
原创 腾讯云安全
                    腾讯云安全  云鼎实验室   2026-03-16 06:26  
  
必修漏洞是指影响范围广、危害程度高、技术细节已公开或存在在野利用的安全漏洞。此类漏洞被攻击者利用后，可能导致业务系统中断、核心数据泄露、服务器被远程控制、内部网络被横向渗透等严重后果，造成经济损失和声誉损害。  
  
腾讯云安全研究团队综合评估“漏洞危害程度、影响范围、技术细节披露情况、安全社区关注度、在野利用情况”等因素，筛选出需优先修复的安全漏洞，定期发布企业必修安全漏洞清单。  
  
本清单旨在为企业安全运维人员提供漏洞修复优先级参考，助力企业提升安全防护能力、降低安全风险。  
  
注：本清单为腾讯云安全基于专业评估提供的技术参考，企业应根据自身业务特点、系统架构、安全等级等实际情况，制定相应的漏洞修复计划。  
  
   
**以下是2026年2月份必修安全漏洞清单**  
：  
  
**一、**  
OpenClaw   
安全绕过漏洞（  
CVE-2026-28363  
）  
  
**二、**  
大蚂蚁  
 (BigAnt)   
即时通讯系统任意文件上传漏洞  
   
(  
TVD-2026-5210  
)  
  
**三、**  
OpenCode   
远程代码执行漏  
洞  
（  
CVE-2026-22812  
)   
  
**四、Langflow CSV Agent**远程代码执行漏洞 (CVE-2026-27966)  
  
**五、**  
Gradio SSRF 服务器端请求伪造漏洞(CVE-2026-28416)  
  
**六****、**飞牛私有云  
fnOS   
路径遍历漏洞  
(TVD-2026-4961）  
  
**七、Apache Camel**反序列化远程代码执行漏洞（CVE-2026-25747）  
  
**八、**Gogs 远程代码执行漏洞（CVE-2025-64111）  
  
九、  
n8n 沙箱逃逸漏洞（CVE-2026-27577）  
  
  
**漏洞介绍及修复建议详见后文**  
  
  
  
  
**一、****OpenClaw**安全绕过漏洞  
  
****  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
OpenClaw  
的风险公告，  
漏洞编号：  
TVD-2026-8067  
（  
CVE  
编号：  
CVE-2026-28363  
，  
CNNVD  
编号：  
CNNVD-202602-4748  
）  
。成功利用此漏洞的攻击者，可绕过命令执行安全验证机制，在无需审批的情况下执行任意系统命令。  
  
OpenClaw  
是一款开源的  
AI  
编码代理工具，旨在为开发者提供智能化的代码编写和项目管理能力。它采用先进的大语言模型技术，能够理解用户的自然语言指令并执行相应的编码任务，包括代码生成、代码审查、  
Bug  
修复等。  
OpenClaw  
通过沙箱机制和命令白名单来保护系统安全，其中  
`tools.exec.safeBins`  
功能用于定义允许执行的安全命令列表，在白名单模式下只有明确允许的命令才能被执行，从而防止恶意命令的执行，保障开发环境的安全。  
  
据描述，该漏洞源于  
OpenClaw  
的  
tools.exec.safeBins  
验证机制在处理  
sort  
命令时存在缺陷。攻击者可以利用  
GNU  
长选项缩写特性（如使用  
--compress-prog  
代替  
--compress-program  
）绕过白名单验证，因为系统只拒绝完整的  
--compress-program  
字符串，而允许其缩写形式通过，从而实现无需审批的命令执行。  
  
注：攻击者要成功利用该漏洞，系统必须配置为  
tools.exec.security=allowlist  
、  
tools.exec.ask=on-miss   
且  
 tools.exec.safeBins   
包含  
 sort  
。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">8.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
OpenClaw < 2026.2.23  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.  
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】：建议您在升级前做好数据备份工作，避免出现意外。  
  
https://github.com/openclaw/openclaw/releases  
  
2.  
临时缓解措施：  
  
-   
如无必要，避免开放至公网  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
  
  
  
  
**二、****大蚂蚁 (BigAnt) 即时通讯系统任意文件上传漏洞**  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于大蚂蚁即时通讯系统的风险公告，  
漏洞编号：  
TVD-2026-5210  
。成功利用此漏洞的攻击者，最终可上传恶意文件，远程执行任意代码。  
  
大蚂蚁（  
BigAnt  
）即时通讯系统是由杭州九麒科技开发的一款专注于政企市场的私有化部署企业级即时通讯平台。该系统始于  
2003  
年，提供即时通讯、文件共享、组织架构管理、协同办公、视频会议及文档管理等一体化功能，并以其独特的消息确认机制、离线消息支持和远程控制等特色著称。大蚂蚁即时通讯系统强调  
“  
自主可控、安全可靠  
”  
，全面适配国产化软硬件环境，支持单机、跨域级联及高可用集群等多种部署方式。  
  
据官方描述，该漏洞源于系统  
 API   
接口未对上传文件的类型及存储路径进行严格校验。远程攻击者无需登录即可利用该漏洞上传恶意脚本文件，从而获取服务器控制权限，导致数据泄露或系统被完全控制。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.6pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.6pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.6pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.5pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">9.9</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
BigAnt 5.5.x   
系列及以上版本  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.  
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://www.bigant.cn/article/news/435.html  
  
2.  
临时缓解方案：  
  
-   
如无必要，避免将服务开放至公网  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
  
**三、****OpenCode 远程代码执行漏洞**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
OpenCode  
的风险公告，  
漏洞编号：  
TVD-2026-3349  
（  
CVE  
编号：  
CVE-2026-22812  
，  
CNNVD  
编号：  
CNNVD-202601-1875  
）  
。成功利用此漏洞的攻击者，最终可远程执行任意代码。  
  
OpenCode  
是一款开源的  
AI  
代码编程助手，旨在为开发者提供智能化的编码体验。它基于先进的人工智能技术，可以帮助开发者自动生成代码、提供代码补全建议、检测代码错误并给出修复方案。  
OpenCode  
支持多种主流编程语言，能够无缝集成到现有的开发环境中，提高开发效率。该工具通过本地  
HTTP  
服务器与用户进行交互，提供  
API  
接口以便于各种  
IDE  
和编辑器进行集成调用，帮助开发者在编写代码过程中获得实时的智能辅助。  
  
据描述，该漏洞源于  
OpenCode  
在启动时会自动开启一个未经身份验证的  
HTTP  
服务器，且该服务器配置了宽松的跨域资源共享  
(CORS)  
策略。攻击者可以通过  
本地恶意程序或恶意网页  
向该服务器发送请求，以当前用户权限执行任意  
Shell  
命令，最终实现远程代码执行。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">8.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
OpenCode < 1.0.216  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://github.com/anomalyco/opencode/releases  
  
2.   
临时缓解方案：  
  
-   
如无必要，避免将服务开放至公网  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
  
  
**四、****Langflow CSV Agent**远程代码执行漏洞  
  
****  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
Langflow  
的风险公告，  
漏洞编号：  
TVD-2026-7892(CVE  
编号：  
CVE-2026-27966  
，  
CNNVD  
编号：  
CNNVD-202602-4530)  
。成功利用此漏洞的攻击者，最终可远程执行任意代码。  
  
Langflow  
是一款开源的可视化  
AI  
工作流构建工具，专为构建和部署  
AI  
驱动的智能代理和工作流程而设计。它提供了直观的拖拽式界面，让用户无需编写大量代码即可创建复杂的  
AI  
应用程序。  
Langflow  
支持与  
LangChain  
深度集成，用户可以轻松组合各种  
AI  
组件，包括大语言模型、向量数据库、文档处理器等。其中  
CSV Agent  
功能允许用户通过自然语言与  
CSV  
数据文件进行交互，实现数据查询、分析和可视化等操作，极大地简化了数据分析工作流程。  
  
据描述，该漏洞源于  
Langflow  
的  
CSV Agent  
节点在代码中硬编码了  
allow_dangerous_code=True  
参数，这会自动暴露  
LangChain  
的  
Python REPL  
工具（  
python_repl_ast  
）。攻击者可以通过构造恶意提示词注入攻击，在服务器上执行任意  
Python  
代码和操作系统命令，最终实现完整的远程代码执行。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">9.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
Langflow < 1.8.0.dev55  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://github.com/langflow-ai/langflow/  
  
2.   
临时缓解方案：  
  
-   
如无必要，避免开放至公网  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
  
  
**五、Gradio SSRF 服务器端请求伪造漏洞**  
  
****  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
Gradio  
的风险公告，  
漏洞编号：  
TVD-2026-8173  
（  
CVE  
编号：  
CVE-2026-28416  
，  
CNNVD  
编号：  
CNNVD-202602-4619  
）  
。成功利用此漏洞的攻击者  
，最终可实现服务器端请求伪造，访问内部资源并窃取敏感信息。  
  
Gradio  
是一款开源的  
Python  
库，专为快速构建机器学习模型演示和原型应用而设计。它允许开发者通过几行代码就能为  
AI  
模型创建交互式  
Web  
界面，支持各种输入输出组件，如文本、图像、音频、视频等。  
Gradio  
因其简单易用的特性，被广泛应用于机器学习研究、模型展示和  
AI  
应用开发领域。其中  
`gr.load()`  
功能允许用户加载托管在  
Hugging Face Spaces  
或其他平台上的  
Gradio  
应用，方便用户复用和集成现有的  
AI  
模型和应用，促进了  
AI  
社区的协作与共享。  
  
ope  
  
据描述，该漏洞源于  
Gradio  
在处理  
`gr.load()`  
加载外部  
Space  
时存在安全缺陷。当受害者应用使用  
`gr.load()`  
加载攻击者控制的恶意  
Space  
时，配置中的恶意  
`proxy_url`  
会被信任并添加到允许列表中，使攻击者能够通过受害者的基础设施访问内部服务、云元数据端点和私有网络资源。  
  
注：任何使用  
 gr.load()   
加载外部或不可信  
 Spaces   
的  
 Gradio   
应用程序均受该漏洞影响。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">8.2</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
Gradio <= 6.5.1  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.  
   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，建议升级至最新版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://github.com/gradio-app/gradio/releases  
  
2.  
   
临时缓解措施：  
  
-   
避免使用  
`gr.load()`  
加载不受信任的外部  
Space  
  
-   
配置防火墙或网络规则，限制服务器对内部网络和云元数据端点的访问  
  
-   
如无必要，避免开放至公网  
  
  
**六、****飞牛私有云 fnOS 路径遍历漏洞**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于飞牛私有云  
fnOS  
的风险公告，  
漏洞编号：  
TVD-2026-4961  
。成功利用此漏洞的攻击者，最终可读取服务器上的任意敏感文件。  
  
飞牛私有云  
FnOS  
是一款基于  
Linux  
内核（  
Debian  
发行版）深度开发的国产免费  
NAS  
系统，它兼容主流  
x86  
硬件，可将闲置旧电脑轻松改造为私有云存储服务器。该系统集成了智能影视刮削、相册备份、多用户文件管理、  
Docker  
容器支持以及应用中心等丰富功能，并通过免费的  
FN Connect  
内网穿透服务实现安全便捷的远程访问，为个人用户和小型团队提供了低门槛、高效率的私有云存储与管理解决方案。  
  
该漏洞源于飞牛私有云  
 fnOS NAS  
操作系统中的  
/app-center-static/serviceicon/myapp/  
接口中存在路径遍历漏洞，未经身份验证的远程攻击者可通过构造恶意请求读取  
 NAS   
上的所有数据，包括用户私人照片、视频、文档，乃至系统配置文件与私钥等，从而造成敏感信息泄露。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:17.55pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 17.55pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span style="mso-spacerun:yes;"></span></span><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 17.55pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">8.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
飞牛私有云  
 fnOS < 1.1.18  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://fnnas.com/download  
  
2.   
临时缓解方案：  
  
-   
如无必要，避免将服务开放至公网  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
  
  
  
  
  
  
**七、****Apache Camel 反序列化远程代码执行漏洞**  
  
****  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
Apache Camel   
组件的风险公告，  
漏洞编号：  
TVD-2026-7326  
（  
CVE  
编号：  
CVE-2026-25747  
，  
CNNVD  
编号：  
CNNVD-202602-3925  
）  
。成功利用此漏洞的攻击者，最终可远程执行任意代码。  
  
Apache Camel  
是  
Apache  
软件基金会开发的一款开源企业级集成框架，基于企业集成模式  
(EIP)  
设计，为开发者提供了丰富的组件和连接器，用于实现不同系统之间的数据交换和集成。  
Camel  
支持超过  
300  
种协议和数据格式，广泛应用于企业服务总线  
(ESB)  
、微服务架构和消息驱动应用中。  
LevelDB  
组件是  
Camel  
的聚合存储库实现之一，使用  
Google  
的  
LevelDB  
键值存储引擎来持久化聚合过程中的中间消息，确保消息在系统重启后不会丢失，为高可用性和容错性提供支持。  
  
据描述，该漏洞源于  
Apache Camel  
的  
LevelDB  
组件中  
DefaultLevelDBSerializer  
类在反序列化数据时存在安全缺陷。该类使用  
java.io.ObjectInputStream  
反序列化从  
LevelDB  
聚合存储库读取的数据，但未应用任何  
ObjectInputFilter  
或类加载限制。攻击者若能够写入  
Camel  
应用程序使用的  
LevelDB  
数据库文件，可注入恶意构造的序列化  
Java  
对象，在正常聚合存储库操作期间触发反序列化，最终实现任意代码执行。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;height:21.1pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 21.1pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 21.1pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">8.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
3.0.0 <= Apache Camel < 4.10.9  
  
4.11.0 <= Apache Camel < 4.14.5  
  
4.15.0 <= Apache Camel < 4.18.0  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，及时更新漏洞补丁  
  
https://camel.apache.org/download/  
  
2.   
临时缓解措施：  
  
-   
配置防火墙或网络规则，仅允许特定  
IP  
地址或  
IP  
段访问  
  
-   
如无必要，避免开放至公网  
  
  
  
  
  
**八、****Gogs**远程代码执行漏洞  
  
****  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
Gogs  
的风险公告，  
漏洞编号：  
TVD-2025-47166  
（  
CVE  
编号：  
CVE-2025-64111  
，  
CNNVD  
编号：  
CNNVD-202602-995  
）  
。成功利用此漏洞的攻击者，最终可远程执行任意代码。  
  
Gogs  
是一款开源的轻量级自托管  
Git  
服务，采用  
Go  
语言编写，以其极低的资源占用和简单的部署方式而著称。  
Gogs  
提供了类似于  
GitHub  
的  
Web  
界面，支持仓库管理、问题追踪、  
Wiki  
、代码审查等功能，适合个人开发者和小型团队使用。它支持多种数据库后端，包括  
SQLite  
、  
MySQL  
、  
PostgreSQL  
等，可以在各种操作系统上运行，包括  
Windows  
、  
Linux  
、  
macOS  
和  
ARM  
架构设备。  
Gogs  
的设计目标是成为一个易于安装、运行和维护的  
Git  
托管解决方案，让用户能够快速搭建私有的代码托管平台。  
  
据描述，由于针对  
 Gogs   
远程代码执行漏洞（  
CVE-2024-56731  
）的补丁修复不完整，在  
 internal/route/api/v1/repo/contents.go   
文件的  
UpdateRepoFile   
函数调用路径中，安全校验逻辑仍存在遗漏，攻击者仍可通过  
 API   
接口，利用仓库中的符号链接文件（如指向  
 .git/config   
的链接），以  
 Base64   
编码的方式提交恶意配置内容，从而篡改  
 Git   
配置的  
 sshCommand   
等关键参数，最终在服务器端执行任意系统命令。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.65pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">9.8</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
  
Gogs <= 0.13.3  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
https://github.com/gogs/gogs/releases  
  
2.   
临时缓解方案：  
  
-   
建议在  
 app.ini   
中关闭  
 Gogs   
用户注册功能，防止攻击者注册账号进行登录利用（修改后需重启  
 Gogs   
服务）：  
  
[auth]  
  
DISABLE_REGISTRATION = true  
  
  
  
**九、**n8n 沙箱逃逸漏洞  
  
****  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**漏洞概述**  
  
腾讯云安全近期监测到关于  
n8n  
的风险公告，  
漏洞编号：  
TVD-2026-7841  
（  
CVE  
编号：  
CVE-2026-27577  
，  
CNNVD  
编号：  
CNNVD-202602-4190  
）  
。成功利用此漏洞的攻击者，可通过表达式注入绕过沙箱限制，在宿主机上执行任意系统命令。  
  
n8n  
是一款开源的工作流自动化平台，专为技术人员和企业设计，用于连接各种应用程序和服务以实现业务流程自动化。它提供了直观的可视化界面，支持超过  
400  
个应用程序集成，包括常见的  
SaaS  
服务、数据库、  
API  
等。  
n8n  
的核心优势在于其灵活性和可扩展性，用户可以通过拖拽方式创建复杂的自动化工作流，也可以使用  
JavaScript  
编写自定义逻辑。  
n8n  
支持自托管部署，让企业能够完全控制自己的数据和工作流，广泛应用于数据同步、通知推送、报表生成等自动化场景。  
  
据描述，该漏洞是  
CVE-2025-68613  
的后续漏洞，源于  
n8n  
在表达式求值机制中存在额外的安全缺陷。经过身份验证且具有工作流创建或修改权限的用户，可以在工作流参数中构造恶意表达式，绕过沙箱限制，在运行  
n8n  
的宿主机上触发非预期的系统命令执行，最终实现沙箱逃逸和远程代码执行。  
  
漏洞状态：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">类别</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">状态</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">安全补丁</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞细节</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">PoC</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">已公开</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">在野利用</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">未发现</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
风险等级：  
<table><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border: 1pt solid windowtext;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">评定方式</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(68, 114, 196);padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><b><span style="font-size:11.5pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:white;letter-spacing:.4pt;"><span leaf="">等级</span></span></b><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">威胁等级</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高危</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:2;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">影响面</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:3;height:18.65pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">攻击者价值</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.65pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">高</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:4;height:18.3pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">利用难度</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 18.3pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">低</span></span><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:5;mso-yfti-lastrow:yes;height:16.4pt;"><td data-colwidth="274" width="274" valign="top" style="border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span style="font-size:10.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">漏洞评分</span></span><span lang="EN-US" style="font-size:13.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:
  宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><o:p></o:p></span></p></td><td data-colwidth="274" width="274" valign="top" style="border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;height: 16.4pt;"><p style="text-align:center;word-break:break-all;"><span lang="EN-US" style="font-size:10.0pt;font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-font-family:宋体;mso-hansi-theme-font:minor-fareast;color:#222222;letter-spacing:.4pt;"><span leaf="">9.9</span><o:p></o:p></span></p></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**影响版本**  
  
n8n < 1.123.22  
  
2.0.0 <= n8n < 2.9.3  
  
2.10.0 <= n8n < 2.10.1  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**修复建议**  
  
  
1.   
官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。  
  
【备注】建议您在升级前做好数据备份工作，避免出现意外。  
  
https://github.com/n8n-io/n8n/releases  
  
2.   
临时缓解方案：  
  
-   
将工作流的创建和编辑权限限制在完全可信的用户范围内，避免不可信用户利用该漏洞  
  
-   
将  
 n8n   
部署在强化后的环境中，限制其操作系统权限和网络访问范围，以降低漏洞被成功利用后可能造成的危害  
  
  
  
  
  
*  
以上  
漏洞评分为腾讯云安全研究人员根据漏洞情况作出，仅供参考，具体漏洞细节请以原厂商或是相关漏洞平台公示为准。  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/FIBZec7ucChYUNicUaqntiamEgZ1ZJYzLRasq5S6zvgt10NKsVZhejol3iakHl3ItlFWYc8ZAkDa2lzDc5SHxmqjw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**END**  
  
  
更多精彩内容点击下方扫码关注哦~  
  
  
关注云鼎实验室，获取更多安全情报  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0mfEkibaEU8uriaORBdj9W37EhEIZlIFuzudKVafyia4vTv1q1usxN57bsdeAY4icwcKw9qJ1W4COeR4Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
  
