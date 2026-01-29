#  漏洞预警 | vLLM远程代码执行漏洞  
浅安
                    浅安  浅安安全   2026-01-28 23:50  
  
**0x00 漏洞编号**  
- # CVE-2026-22807  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
vLLM是一个高性能的大模型推理框架，专为大规模语言模型的高吞吐量、低延迟部署而设计。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SW9BialdxKvN1AlcuDRdaLCe2sca1VJ7fwzmrhyCfwW38V19sDxZvb6koPyUBGV4ykqrKucZrRwSMg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-22807**  
  
**漏洞类型：**  
代码执行  
  
**影响：**  
执行任意代码  
  
  
  
**简述：**  
v  
LLM存在远程代码执行漏洞，由于其在解析模型配置时，无条件加载Hugging Face模型中的auto_map动态模块，且未对trust_remote_code选项进行有效校验。攻击者一旦能够控制模型仓库路径，即可在模型加载过程中注入并执行任意Python代码。  
  
**0x04 影响版本**  
- 0.10.1 <= vLLM < 0.14.0  
  
**0x05****POC状态**  
- 未公开  
  
****  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://github.com/vllm-project/vllm  
  
  
  
