#  攻击者可删除文件、植入后门：MS-Agent漏洞曝出完整利用链  
看雪学苑
                    看雪学苑  看雪学苑   2026-03-06 10:08  
  
研究人员最新发现，一个名为MS-Agent的轻量级AI框架存在严重漏洞，可能让攻击者通过简单的“提示词注入”接管整个系统。  
  
  
MS-Agent框架设计了一个实用功能——“Shell工具”，允许AI直接调用操作系统命令来完成用户请求。这本意是提升AI的自主能力，却意外打开了潘多拉魔盒。  
  
  
研究发现，当AI处理外部输入时，这个工具并未对内容进行有效过滤。攻击者可以将恶意指令伪装成普通文本，例如在一份待总结的文档中嵌入隐藏命令。当AI读取这些内容时，会不加区分地将恶意指令传递给Shell工具执行。  
  
  
更令人担忧的是，虽然框架内置了一个名为check_safe()的过滤器，但它仅依靠简单的“黑名单”机制——列出禁止使用的命令词。这种防护形同虚设，攻击者只需使用替代语法或命令混淆技术，就能轻松绕过检测。  
  
  
成功利用此漏洞的攻击者，将获得与MS-Agent进程相同的系统权限。这意味着他们可以：  
  
- 窃取AI可访问的所有敏感数据  
  
- 修改或删除关键系统文件  
  
- 植入后门程序，建立持久化控制  
  
- 以此为跳板，侵入企业内网其他资产  
  
  
该漏洞已被分配编号CVE-2026-2256。截至目前，相关厂商尚未发布安全补丁或官方回应。在等待修复期间，安全专家建议采取以下紧急防护措施：  
  
- 隔离运行环境：将MS-Agent部署在高度隔离的沙箱中，限制攻击影响范围  
  
- 最小权限原则：仅赋予AI完成任务的必要权限，避免使用高权限账户  
  
- 外部输入审查*：确保AI处理的所有外部内容都来自可信来源  
  
- 强化命令过滤：放弃脆弱的黑名单机制，改用白名单模式，只允许执行预先批准的特定命令  
  
  
资讯来源：本文基于CERT/CC发布的安全漏洞通告编译整理  
  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
