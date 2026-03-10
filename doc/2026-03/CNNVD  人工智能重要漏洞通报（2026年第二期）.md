#  CNNVD | 人工智能重要漏洞通报（2026年第二期）  
 中国信息安全   2026-03-10 08:25  
  
[](https://cisat.cn/all/14915419?navIndex=3)  
  
**漏洞情况**  
  
根据国家信息安全漏洞库（CNNVD）统计，近期（2026年1月12日至2026年3月3日）共采集重要人工智能漏洞255个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了谷歌、IBM、微软等多个厂商。CNNVD对其危害等级进行了评价，其中超危漏洞27个，高危漏洞48个，中危漏洞180个。   
  
## 一人工智能漏洞增长数量情况  
  
  
近期CNNVD采集人工智能漏洞255个。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uOZw5Efn8evehEmpN9wMEH6UcVuBDI0oQCA3CcehV15HzLCGImIEHRkxcPxB7SRJRmCaFozBwc0HH1WTFnQiampoBfRnYuhBFLPQHiaL02nls/640?wx_fmt=other&from=appmsg&watermark=1#imgIndex=3 "")  
  
图1 近五周漏洞新增数量统计图  
  
****  
## 二人工智能漏洞具体情况  
  
  
近期共采集人工智能漏洞255个，包括谷歌、IBM、微软等多个厂商的漏洞。其中超危漏洞27个，高危漏洞48个，中危漏洞180个。具体如表1所示：  
  
表1 人工智能漏洞列表  
  
![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8etI0XibfQHGsxHBYkiclnFINVcjicmXmw8Enicl83HyibzFmdU0zCJH3SkMyQ4brwia2suN1hDwrXhCagIefRJhxMLyUibtMqNm2ApQLI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4 "")  
  
## 三重要人工智能漏洞实例  
  
  
近期重要漏洞实例如表2所示。  
  
表2 本期重要漏洞实例  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/uOZw5Efn8etq6H0QAkppzeHmqx1L67rJIBfgvydz2r90LsKwB5riclIpz6ly2HsGuZtEAFC5pKHiaOzLwAiaewep64f6dElnGvnrsMNFCnNAhQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5 "")  
  
1. Langflow 安全漏洞（CNNVD-202602-4530）****  
  
Langflow是一个开源的用于构建多代理和RAG应用程序的可视化框架。  
  
Langflow 1.8.0之前版本存在安全漏洞，该漏洞源于在创建CSVAgent时将allow_dangerous_code参数硬编码为True，导致系统自动启用LangChain的python_repl_ast工具，攻击者利用该漏洞可以远程执行代码。  
  
目前厂商已发布升级补丁以修复漏洞，参考链接：  
  
https://github.com/langflow-ai/langflow/releases  
  
2. Cursor 安全漏洞（CNNVD-202602-2275）****  
  
Cursor是一款开源的深度集成AI的智能代码编辑器。  
  
Cursor 2.5之前版本存在安全漏洞，该漏洞源于允许通过写入.git配置实现沙箱逃逸，攻击者利用该漏洞可以远程执行代码。  
  
目前厂商已发布升级补丁以修复漏洞，参考链接：  
  
https://cursor.com/  
  
3. AutoGPT 授权问题漏洞（CNNVD-202602-2072）****  
  
AutoGPT是一个开源的自主智能代理框架，具有目标驱动的任务拆解、自动规划执行以及工具调用等功能。  
  
AutoGPT 0.6.48之前版本存在授权问题漏洞，该漏洞源于图形验证未强制执行禁用标志，允许经过身份验证的用户绕过限制，攻击者利用该漏洞可以远程执行代码。  
  
目前厂商已发布升级补丁以修复漏洞，参考链接：  
  
https://github.com/Significant-Gravitas/AutoGPT/releases  
  
  
（来源：CNNVD）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20CiacnC1Zhy9UATRh0fdpnmmzHticIvIRHWNSia77EFpubWticicjKFhFIuy2ibbsTMw1XyLe7ia2Qj1v4tMzZQIgLfhvsf8EeuWWOrPW8/640?wx_fmt=png&from=appmsg "")  
  
[](https://cisat.cn/page/3105255?navIndex=0)  
  
