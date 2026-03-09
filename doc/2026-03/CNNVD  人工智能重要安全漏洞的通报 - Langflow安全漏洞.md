#  CNNVD | 人工智能重要安全漏洞的通报 - Langflow安全漏洞  
 中国信息安全   2026-03-09 10:31  
  
[](https://cisat.cn/all/14915419?navIndex=3)  
  
**漏洞情况**  
  
近日，国家信息安全漏洞库（CNNVD）收到关于Langflow 安全漏洞（CNNVD-202602-4530、CVE-2026-27966）情况的报送。攻击者利用该漏洞可以远程执行代码。Langflow 1.8.0之前版本均受此漏洞影响。目前，Langflow官方已发布补丁修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。  
  
## 一漏洞介绍  
  
  
Langflow是一个开源的用于构建和部署AI驱动智能体与工作流的可视化平台。Langflow存在一个安全漏洞，该漏洞源于在创建CSVAgent时将allow_dangerous_code参数硬编码为True，导致系统自动启用LangChain的python_repl_ast工具，攻击者利用该漏洞可以远程执行代码。  
  
****  
## 二危害影响  
  
  
Langflow 1.8.0之前版本均受此漏洞影响。  
  
****  
## 三修复建议  
  
  
目前，Langflow官方已发布补丁修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方参考链接：  
  
https://github.com/langflow-ai/langflow/security/advisories/GHSA-3645-fxcv-hqr4  
  
本通报由CNNVD技术支撑单位——中国银联股份有限公司、三六零数字安全科技集团有限公司、清远职业技术学院、温州市数据集团有限公司、金盾检测技术股份有限公司、奇安信网神信息技术（北京）股份有限公司、上海戟安科技有限公司、北京网御星云信息技术有限公司、北京赛博昆仑科技有限公司、任子行网络技术股份有限公司、中国联合网络通信有限公司深圳市分公司、内蒙古数字安全科技有限公司、天翼安全科技有限公司等技术支撑单位提供支持。  
  
CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。联系方式: cnnvd@itsec.gov.cn  
  
  
（来源：CNNVD）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20CjJodMR7Dko2OyfsNiaNO0eic0R4CT1QJAcrKzD9vaN4bAaS9RnusVjNQEDadedbgrvpBBpDicNvXvVIQsxKuibBf8GpStSm71DAdo/640?wx_fmt=png&from=appmsg "")  
  
[](https://cisat.cn/page/3105255?navIndex=0)  
  
