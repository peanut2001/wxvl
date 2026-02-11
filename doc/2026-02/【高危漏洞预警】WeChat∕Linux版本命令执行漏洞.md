#  【高危漏洞预警】WeChat/Linux版本命令执行漏洞  
cexlife
                    cexlife  飓风网络安全   2026-02-11 11:55  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yd9HAo0qc3qc1crol9oquozKmyygblWlGK7Zw09jZviaf0WuFETrFjFt9RqsaVibaOlibzdAmq19fxtuBWPqIT17lTeialNpvBqlRBSib8WUC3lE/640?wx_fmt=png&from=appmsg "")  
  
漏洞描述:  
  
该漏洞源于微信Linuх版文件名校验不严格,攻击者可诱导用户打开恶意文件名的文件从而导致命令执行获取系统权限  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yd9HAo0qc3rDpFfKmibE1wCNeKhV66vyia9icBDdSH5qxgHEvZRw2LlAXbMdXFf2rTNjiarCVGibTmokLmP4nq5BazZvIup6DN0KEiaSprBJGIsCA/640?wx_fmt=png&from=appmsg "")  
  
在野利用情况:  
  
目前尚未观察到明确的在野利用证据（in_the_wild = false），但漏洞具备高利用可能性（vuln_exploit_possibility:  
  
高），且存在攻击向量明确、无需复杂前置条件的特征。  
  
攻击场景:  
  
攻击者通过构造含有恶意文件名的特制文件（如包含特殊字符或路径遍历符号的文件名）诱导用户在微信客户端中打开该文件因文件名校验机制存在缺陷导致恶意命令被执行进而获取系统权限。  
  
**影响产品及版本**  
：  
  
微信Linux版本 <= 4.1.0.13  
  
利用条件:  
  
用户交互   
  
修复建议:  
  
官方暂未发布安全补丁,请仔细防范恶意文件名的文件   
  
缓解方案:  
  
仔细防范恶意文件名的文件   
  
技术分析和建议:  
  
分析:该漏洞本质为“数据验证不恰当”导致的命令执行攻击者无需突破网络边界,仅需通过社交工程手段（如伪装成正常文档、压缩包、聊天附件等）诱使用户打开恶意文件,由于漏洞影响范围集中于Linux平台用户且微信在科研、开发、服务器运维等场景中广泛使用,一旦被利用可能导致敏感信息泄露、横向移动甚至系统控制权丢失  
  
建议:  
  
立即停止使用微信Linux版本 ≤ 4.1.0.13，建议升级至官方最新版本（当前最新为8.0.69，适用于Android平台，但Linux版需关注官方更新）  
  
严格审查来自外部的文件传输，特别是通过微信接收的压缩包、文档、脚本类文件，避免直接打开未知来源的文件  
  
启用文件类型白名单机制，在系统层面限制非标准文件类型的执行权限。  
  
部署EDR/XDR工具，监控微信进程中的异常命令调用行为（如sh, bash, system, exec等函数调用）  
  
加强用户安全意识培训，强调“不打开来历不明的文件”作为基本安全准则  
  
参考链接:  
  
https://linux.weixin.qq.com/  
  
  
  
