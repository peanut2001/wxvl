#  漏洞预警 | ComfyUI-Manager远程代码执行漏洞  
浅安
                    浅安  浅安安全   2026-01-21 00:01  
  
**0x00 漏洞编号**  
- # CVE-2025-67303  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
ComfyUI是一款基于节点式工作流的Stable Diffusion图形界面工具，广泛用于AI图像生成领域。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SUXMjseYbjJkzOZuEAZYkLX11hK4ic6BarLsIOibDXic98rTmic19Qiacv7KKic4DC2EOmDBnjmCfgCfILw/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2025-67303**  
  
**漏洞类型：**  
远程代码执行  
  
**影响：**  
执行任意命令  
  
  
  
**简述：**  
ComfyUI-Manager存在远程代码执行漏洞，由于其数据与配置目录在旧版本中未受ComfyUI的Web API访问控制充分保护，攻击者可通过发送特殊请求覆盖config.ini配置文件并利用其他危险接口执行恶意脚本代码，从而获取服务器权限。  
  
**0x04 影响版本**  
- ComfyUI-Manager < v3.38  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
h  
ttps://github.com/Comfy-Org/ComfyUI-Manager  
  
  
  
