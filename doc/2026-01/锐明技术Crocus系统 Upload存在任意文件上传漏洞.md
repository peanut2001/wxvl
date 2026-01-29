#  锐明技术Crocus系统 Upload存在任意文件上传漏洞  
原创 aaa
                    aaa  Anonymous安全实验室   2026-01-29 00:28  
  
**>**  
**>**  
**>**  
**>**  
  
**影响组件**  
  
锐明技术Crocus系统  
  
**>**  
**>**  
**>**  
**>**  
  
**漏洞描述**  
  
锐明技术Crocus系统的Upload功能存在任意文件上传漏洞，由于未对上传文件的类型、内容及路径进行严格校验，攻击者可上传恶意文件至服务器，结合路径拼接缺陷实现目录穿越，最终可能导致远程代码执行（RCE）或服务器被控制。  
  
**>**  
**>**  
**>**  
**>**  
  
**修复建议**  
  
安装长亭雷池拦截，及时升级至最新版本。  
  
**>**  
**>**  
**>**  
**>**  
  
巡  
星  
平台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/9qJOKPPF51Q3AVa9qf0L1N5lMxYWbV4oYPClibhod9LlpH1jTy0E21iaxMd02VF78yJhFuU22yib0KU6BWKddfntg/640?wx_fmt=png&from=appmsg "")  
  
  
平台使用说明：  
https://ruisika.github.io/xunxing/intro/  
  
  
