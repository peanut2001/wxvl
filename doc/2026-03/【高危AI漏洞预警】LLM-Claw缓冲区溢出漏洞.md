#  【高危AI漏洞预警】LLM-Claw缓冲区溢出漏洞  
cexlife
                    cexlife  飓风网络安全   2026-03-04 10:09  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Yd9HAo0qc3on4LhkrPCskh8DG9uQQXCw4zoibhLcpibmhH1xmeIUKzbSkUibfrJWeBQKGpeEuNYibS9r47E1ibrHTzV52aNT1gIsxwLjDMCLJuCI/640?wx_fmt=png&from=appmsg "")  
  
漏洞描述:  
  
在 LLM-Clаԝ 0.1.0/0.1.1/0.1.1а/0.1.1а－р1中检测到一个安全漏洞,受影响的元素是组件Aɡеnt Dерlоуmеnt的文件/аɡеntѕ/dерlоу/initiаtе.с中的函数 аɡеnt_dерlоу_init,此类操作会导致缓冲区溢出可远程发起攻击,应应用补丁以修复此问题  
  
影响产品及版本:  
  
受影响产品为LLM-Claw系统,具体版本包括:  
  
0.1.0  
  
0.1.1  
  
0.1.1а（含变体字符混淆版本）  
  
0.1.1а-р1（存在特殊编码变种）  
  
修复建议:  
  
目前官方已有可更新版本,建议受影响用户升级至最新版本  
  
建议措施:  
  
立即升级：将 LLM-Claw 系统升级至官方发布的修复版本（若已发布）  
  
输入验证强化：对所有进入 agent_deploy_init 函数的输入参数进行长度校验与边界检查，避免缓冲区溢出  
  
启用安全编译选项：启用栈保护（Stack Canary）、ASLR、DEP/NX 等内存安全机制。  
  
检测规则更新：在防火墙、WAF、IDS/IPS 中增加对包含“混淆字符”（如 а, с, о 与 a, c, o 混淆）的请求模式的检测规则  
  
日志监控：对 agent_deployment 模块的异常调用行为进行日志审计，重点关注高频、异常长度或非法字符的请求  
  
  
