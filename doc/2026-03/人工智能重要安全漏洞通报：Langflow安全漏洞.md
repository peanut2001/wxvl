#  人工智能重要安全漏洞通报：Langflow安全漏洞  
Cismag
                    Cismag  信息安全与通信保密杂志社   2026-03-06 09:40  
  
近日，国家信息安全漏洞库（CNNVD）收到关于Langflow 安全漏洞（CNNVD-202602-4530、CVE-2026-27966）情况的报送。攻击者利用该漏洞可以远程执行代码。Langflow 1.8.0之前版本均受此漏洞影响。目前，Langflow官方已发布补丁修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。  
  
一、漏洞介绍  
  
Langflow是一个开源的用于构建和部署AI驱动智能体与工作流的可视化平台。Langflow存在一个安全漏洞，该漏洞源于在创建CSVAgent时将allow_dangerous_code参数硬编码为True，导致系统自动启用LangChain的python_repl_ast工具，攻击者利用该漏洞可以远程执行代码。  
  
二、危害影响  
  
Langflow 1.8.0之前版本均受此漏洞影响。  
  
三、修复建议  
  
目前，Langflow官方已发布补丁修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方参考链接：https://github.com/langflow-ai/langflow/security/advisories/GHSA-3645-fxcv-hqr4  
  
  
  
**来源：CNNVD安全动态**  
  
**★**  
  
  
**★ ★ ★**  
  
  
**★**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iclynibMMTgBwgCg9mGbuByfRqykUw7pNibhqs5FTfibiagTERwjA5aIr1nWU877gknbu4l0icwleVpLxzotXXbK3thA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5 "")  
  
  
