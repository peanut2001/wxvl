#  警惕最新高危漏洞n8n 严重缺陷（CVSS 9.9）允许远程代码执行  
ZM
                    ZM  暗镜   2026-01-29 22:00  
  
JFrog研究员 Natan Nehorai发现n8n 中存在一个严重的远程代码执行 (RCE)编号为 CVE-2026-1470， CVSS 评分为 9.9，允许已认证用户突破平台的沙箱防御，并在主节点上执行任意代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCStic9niaD3HlFbQ2jS6Mtb4d9jbicg8fg9Xk5M4KFJ8dJrGYhK9tWNoRF4gUHozqT4nFcjicFRWLbMRfjg/640?wx_fmt=png&from=appmsg "")  
  
该针对的是n8n灵活性的核心：其表达式求值系统。该功能旨在允许用户编写自定义逻辑，但经发现其与底层运行时环境的隔离不足。  
  
问题在于 n8n 如何处理用户提供的表达式。根据，“已认证用户在工作流配置期间提供的表达式可能会在与底层运行时隔离不足的执行上下文中进行求值”。  
  
这一疏忽将一项强大的功能变成了致命的武器。拥有认证访问权限的攻击者（可能是低级别用户）可以注入恶意载荷，从而完全绕过沙箱机制。  
  
“经过身份验证的攻击者可以利用这种行为，以 n8n 进程的权限执行任意代码”。  
  
一旦代码运行，攻击基本上就结束了。攻击者将获得与 n8n 应用程序本身相同的访问权限，这通常包括访问敏感数据、修改业务关键型工作流程以及执行系统级操作的权限。  
  
该漏洞影响平台的特定版本范围。管理员应立即检查其实例。受影响的版本包括：  
  
1.123.17  
  
版本介于 2.0.0 和 2.4.5 之间（不包括 2.4.5）  
  
版本介于 2.5.0 和 2.5.1 之间（不包括 2.5.1）  
# 相关验证  
  
{{ (function(){ var constructor = 123; with(function(){}){ return constructor("return process.mainModule.require('child_process').execSync('env').toString().trim()")() } })() }}  
  
