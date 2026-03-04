#  漏洞预警 | RustFS授权绕过漏洞  
浅安
                    浅安  浅安安全   2026-03-04 00:01  
  
**0x00 漏洞编号**  
- # CVE-2026-27607  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
RustFS是一款基于Rust语言开发的分布式对象存储系统，采用高性能、内存安全的设计理念，支持S3兼容接口与集群化部署，适用于云存储、数据湖及大规模非结构化数据场景。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXyUpeaFS0y6MiaqDjlNGve3zBhNRv2hg8PXMWqS8kN1ZrXxuYs4XSDpS5bvgw9gR0o4Sp8DsKpaeA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-27607**  
  
**漏洞类型：**  
授权绕过  
  
**影响：**  
越权操作  
  
**简述：**  
RustFS的PostObject策略验证缺失导致授权绕过漏洞，由于其服务端未对签名策略中的关键限制条件进行有效解析与验证，包括content-length-range、starts-with以及Content-Type等约束，导致攻击者可绕过既定上传策略。利用该缺陷，攻击者可上传超出限制大小的文件、将对象写入任意Key路径，或伪造文件类型，从而引发存储资源耗尽、越权数据覆盖及潜在的跨站脚本风险。  
  
**0x04 影响版本**  
- 1.0.0-alpha.56 <= RustFS <= 1.0.0-alpha.82  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://rustfs.com/  
  
  
  
