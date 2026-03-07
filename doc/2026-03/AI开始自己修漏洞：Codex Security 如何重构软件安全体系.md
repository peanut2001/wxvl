#  AI开始自己修漏洞：Codex Security 如何重构软件安全体系  
王慧敏
                    王慧敏  AI与代码安全   2026-03-07 06:22  
  
随着软件系统复杂度的指数级增长，传统的应用安全工具逐渐难以满足现代软件研发的需求。2026 年，OpenAI 推出了 AI 驱动的安全代理 Codex Security  
，它能够在代码仓库中自动发现漏洞、验证漏洞并生成可执行修复方案，从而显著改变传统软件漏洞修复流程。  
  
本文从技术研发的角度  
深入解析  
 Codex Security 的核心技术原理，并探讨其如何颠覆传统安全工具。  
  
【  
AI代码助手、  
大模型智能体安全、AI代码静态分析工具、AI动态分析工具、AI渗透测试工具、AI模糊测试、AI恶意代码检测平台、AI软件漏洞挖掘平台、AI软件供应链安全平台。试用及合作请后台私信工程师13381155803（微信同步）】  
  
  
一、传统漏洞修复工具的技术瓶颈  
  
在理解  
 Codex Security 的创新之前，需要先看传统安全工具的架构。  
  
传统软件安全主要依赖三类技术：  
## 1. 静态分析（SAST）  
  
典型工具：  
  
1)  
Fortify  
  
2)  
Checkmarx  
  
3)  
SonarQube  
  
原理：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">代码</span></font><font face="宋体"><span leaf="">→ AST解析 → 规则匹配 → 漏洞报告</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
其  
特点：  
  
优点：  
  
1)无需运行程序  
  
2)可以扫描整个代码库  
  
缺点：  
  
1)误报率高  
  
2)无法理解业务逻辑  
  
3)无法自动修复  
## 2. 动态分析（DAST）  
  
原理：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">运行程序</span></font><font face="宋体"><span leaf="">→ 模拟攻击 → 观察响应</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
典型检测：  
  
1）SQL Injection  
  
2）XSS  
  
3）SSRF  
  
缺点：  
  
1）只能发现可触发漏洞  
  
2）需要运行环境  
  
3）很难定位代码  
## 3. SCA（软件供应链扫描）  
  
例如：  
  
1）Snyk  
  
2）Dependabot  
  
检测：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">依赖版本</span></font><font face="宋体"><span leaf="">→ CVE数据库匹配</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
问题：  
  
1）只能检测依赖漏洞  
  
2）无法理解业务代码  
## 传统漏洞修复流程  
  
典型流程：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">扫描</span></font><font face="宋体"><span leaf="">→ 人工分析 → 开发修复 → 安全复测</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
周期：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">1个漏洞 = 数小时 ~ 数天</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
核心痛点：  
  
1）  
误报多  
  
2）  
修复依赖人工  
  
3）  
缺乏上下文理解  
  
4）  
无法规模化处理  
# 二、Codex Security 的核心技术架构  
  
Codex Security 本质上不是“扫描工具”，而是一个 AI安全代理（Security Agent）  
。  
  
其核心能力包括：  
  
1）代码理解  
  
2）漏洞发现  
  
3）漏洞验证  
  
4）自动修复  
  
典型架构如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/316EM2ouicpy1wa40mdIpJRD8HQH1G0XRhRWVY346WT1eLribgH0bOhMbx0Arak6vBT4jcmP4lKXZBfvHuibRoYTzjATCxEibUbPJ7jChKo0Y7E/640?wx_fmt=png&from=appmsg "")  
  
# 三、关键技术机制  
## 1 代码语义理解（Semantic Code Understanding）  
  
传统扫描器只看：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">语法结构</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
而  
 Codex Security 会理解：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">数据流</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">调用关系</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">业务逻辑</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">权限边界</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
例如：  
  
传统工具看到：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">request.get(&#34;url&#34;)</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
Codex Security 会分析：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">外部输入</span></font><font face="宋体"><span leaf="">→ 网络请求 → SSRF风险</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
并结合系统上下文判断漏洞。  
## 2 上下文建模（Repository Context Modeling）  
  
Codex Security 会构建完整代码上下文：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Repository Graph</span></span><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></b></p></td></tr></tbody></table>  
包括：  
  
1）模块依赖  
  
2）API调用  
  
3）数据流路径  
  
4）commit history  
  
AI 可以理解：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">A函数 → B服务 → 数据库</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
而不是孤立代码。  
## 3 漏洞推理（Security Reasoning）  
  
传统工具：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">规则匹配</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
Codex Security：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI推理</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
例如识别：  
  
1）SSRF  
  
2）权限绕过  
  
3）业务逻辑漏洞  
  
甚至复杂漏洞：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">multi-step exploit</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
早期测试中，系统成功发现真实  
 SSRF 漏洞，并显著降低误报率。  
  
误报降低：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">50%</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
噪声减少：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">84%</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>## 4 自动漏洞验证（Exploit Validation）  
  
传统工具：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">可能存在漏洞</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
Codex Security：  
  
验证漏洞是否真实  
  
方法：  
  
在沙盒环境运行漏洞利用  
：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">1 生成 exploit</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">2 模拟攻击</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">3 验证影响</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
类似：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI security researcher</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
系统甚至能生成漏洞利用示例证明漏洞影响。  
## 5 自动修复生成（Patch Generation）  
  
AI 根据系统上下文生成：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">安全补丁</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
修复不仅是代码修改：  
  
还包括：  
  
1）参数验证  
  
2）权限控制  
  
3）API限制  
  
输出形式：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Pull Request</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
开发者只需  
 review。  
# 四、Codex Security 的研发流程  
  
传统安全流程：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">开发</span></font><font face="宋体"><span leaf="">→ 安全扫描 → 修复</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
Codex Security：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">开发</span></font><font face="宋体"><span leaf="">→ AI安全代理实时分析 → 自动修复</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
在  
 DevOps 中形成：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI Security Loop</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
流程：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Code Commit</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">│</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Codex Scan</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">│</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI Vulnerability Analysis</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">│</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Exploit Verification</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">│</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Patch Generation</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">│</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Pull Request</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
整个流程：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">分钟级</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table># 五、技术创新点  
## 1 Agentic Security  
  
Codex Security 是 Agent-based AI  
。  
  
能力：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">自主分析</span></font></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">自主验证</span></font></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">自主修复</span></font></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></b></p></td></tr></tbody></table>  
而不是单纯：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI助手</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>## 2 大模型 + 程序分析融合  
  
技术栈融合：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">LLM</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">+</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Static Analysis</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">+</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Dynamic Testing</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">+</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Sandbox Execution</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
形成新的安全体系：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI-driven AppSec</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>## 3 自适应学习  
  
系统可以根据：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">开发者反馈</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞修复结果</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
持续学习。  
  
因此模型会越来越了解：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">企业代码风格</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">架构模式</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">安全策略</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table># 六、与传统工具的核心差异  
<table><tbody><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">技术能力</span></font></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></b></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">传统工具</span></font></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></b></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Codex Security</span></span></b><b><span style="font-family:宋体;font-weight:bold;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></b></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞发现</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">规则扫描</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI推理</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞验证</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">无</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">自动</span></font><span leaf=""> exploit</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞修复</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">人工</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI生成</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">代码理解</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">语法级</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">语义级</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">规模</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">限制</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">大规模扫描</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">误报率</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">高</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td><td data-colwidth="236" width="236" valign="top" style="padding: 0pt 5.4pt;border-left: 1pt solid windowtext;border-right: 1pt solid windowtext;border-top: none;border-bottom: 1pt solid windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">大幅降低</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table># 七、真实应用案例  
  
在测试阶段：  
  
Codex Security 已在开源项目中发现漏洞，例如：  
  
1）OpenSSH  
  
2）Chromium  
  
3）GnuTLS  
  
共发现：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">800+ critical issues</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">10000+ high-risk issues</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table># 八、对软件研发体系的影响  
  
Codex Security 代表一种新的研发模式：  
## Security Shift Left  
  
安全前移：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">开发阶段</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
而不是：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">上线前扫描</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>## DevSecOps 自动化  
  
未来安全流程：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI安全代理</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
成为：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">CI/CD基础设施</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>## AI安全工程师  
  
未来安全团队将从：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞修复</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
转向：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI安全策略设计</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table># 九、未来发展趋势  
  
未来  
 AI AppSec 将出现三大趋势：  
### 1 自动漏洞研究  
  
AI成为：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Security Researcher</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>### 2 自动补丁发布  
  
未来可能：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">漏洞发现</span></font><font face="宋体"><span leaf="">→ 自动修复 → 自动部署</span></font></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>### 3 自主安全系统  
  
最终形态：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Self-healing software</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
软件可以：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">自动修复漏洞</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table># 十、总结  
  
Codex Security 的真正创新不只是“AI修复漏洞”，而是将软件安全从 工具驱动  
 转变为AI代理驱动  
。  
  
技术范式变化：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">传统安全</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Rule-based</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><font face="宋体"><span leaf="">↓</span></font></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI Security</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Reasoning-based</span></span><span style=""><o:p></o:p></span></p></td></tr></tbody></table>  
未来的软件研发体系很可能演变为：  
<table><tbody><tr><td data-colwidth="710" width="710" valign="top" style="padding: 0pt 5.4pt;border-width: 1pt;border-style: solid;border-color: windowtext;"><p style="text-autospace:ideograph-numeric;mso-pagination:widow-orphan;line-height:150%;"><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">Human Developer</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">+</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI Coding Agent</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">+</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf=""><br/></span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><span leaf="">AI Security Agent</span></span><span style="font-family:宋体;font-size:12.0000pt;mso-font-kerning:0.0000pt;"><o:p></o:p></span></p></td></tr></tbody></table>  
共同完成软件开发与安全防护。  
  
  
  
  
  
