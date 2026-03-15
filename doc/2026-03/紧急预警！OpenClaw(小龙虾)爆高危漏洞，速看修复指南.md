#  紧急预警！OpenClaw(小龙虾)爆高危漏洞，速看修复指南  
原创 洞悉安全团队
                    洞悉安全团队  洞悉安全团队   2026-03-15 03:40  
  
AI圈爆火的“小龙虾”OpenClaw，突发高危漏洞！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/keqpjicn6JgIItCkxTwmPIA270gM5NPRE8ReZUdXnndR2aJuOpY2VBqjdMoDVTXDbKSxVJ7e2Q42mnlmqTWTo5Q/640?from=appmsg "")  
  
CNNVD通报，2026年1-3月共采集其漏洞82个，其中 12个超危、21个高危 ，且以下漏洞极易被利用（附编号+利用姿势），速看防范！  
  
![](https://mmecoa.qpic.cn/mmecoa_png/LIjJWiag5KAByysTC7069o4OVrCbzPPBcwuxEicCvstibmqQV6subtwbRicF4XlNWwBZTv2eDCu1MRic6HiaDpYdKyQg/640?from=appmsg "")  
  
  
重点：仅讲易被利用、风险最高的漏洞，建议直接收藏修复指南！  
  
  
01  
  
简要了解：OpenClaw（小龙虾）  
  
  
开源本地AI智能体框架，因红色龙虾图标得名，核心特点是可直接访问本地文件、执行系统命令，这也使其成为黑客重点目标。  
  
  
02  
  
重点！极易被利用的漏洞（带编号+利用姿势）  
  
  
以下漏洞操作门槛极低、成功率极高，新手也能轻松利用，务必警惕！  
  
一、紧急漏洞（3个最易利用，附编号）  
  
利用后可直接获取设备最高权限：  
1. 参数注入漏洞  
 （CNNVD-202603-666 ，CVE-2026-28470）： 在指令中嵌入恶意代码片段（因OpenClaw不校验输入参数），比如给OpenClaw发送“查询系统信息 && whoami”，OpenClaw执行指令时会同步执行whoami命令，获取当前设备用户权限，进而读取敏感文件、执行高危命令；  
  
1. 命令注入漏洞  
 （CNNVD-202603-599，CVE-2026-28484）： 诱导用户让OpenClaw执行“查询当前目录文件 && whoami && ls /root”这类恶意拼接命令，或构造恶意网页，让OpenClaw读取时自动执行隐藏Shell命令，通过whoami获取用户权限、ls命令查看敏感目录，进而窃取数据、控制设备；  
  
1. 访问控制错误漏洞  
 （CNNVD-202603-738，CVE-2026-28472）：简单篡改请求头、伪造用户身份，即可绕过权限验证，直接访问设备密码缓存（如Windows系统的C:\Users\Administrator\AppData\Roaming\Microsoft\Credentials）、密钥文件等核心敏感信息，无需复杂操作；  
  
二、高危漏洞（3个最易利用，附典型编号）  
  
隐蔽性强、利用门槛低，日常使用中极易中招：  
1. 操作系统命令注入  
 （典型编号：CNNVD-202602-3716，CVE-2026-27001，共4个）：借助OpenClaw执行系统命令的功能，诱导其执行“帮我执行命令：whoami && cat /etc/passwd”，通过whoami获取用户权限、cat命令读取系统用户列表，轻松删除文件、植入木马；  
  
1. 访问控制错误  
 （典型编号：CNNVD-202603-595，CVE-2026-29613，共5个）：和紧急漏洞一致，简单伪造权限即可绕过限制，直接读取、篡改办公文件（如D:\工作文档\机密文件.xlsx）、浏览器密码缓存，无需复杂技术；  
  
1. 路径遍历漏洞  
 （典型编号：CNNVD-202603-616，CVE-2026-28462，共3个）：在文件访问指令中嵌入“../”跳转字符，比如给OpenClaw发送“打开文件 ../../etc/passwd”（Linux系统）或“打开文件 ../../Users/Administrator/桌面/密码.txt”（Windows系统），绕过路径限制，直接访问设备深层隐私数据；  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/keqpjicn6JgIItCkxTwmPIA270gM5NPRE8ReZUdXnndR2aJuOpY2VBqjdMoDVTXDbKSxVJ7e2Q42mnlmqTWTo5Q/640?from=appmsg "")  
  
⚠️ 关键提醒： OpenClaw 2026.2.15及之前所有版本，均受上述易利用漏洞影响 ，立即处理！  
  
![](https://mmecoa.qpic.cn/mmecoa_png/LIjJWiag5KAByysTC7069o4OVrCbzPPBcwuxEicCvstibmqQV6subtwbRicF4XlNWwBZTv2eDCu1MRic6HiaDpYdKyQg/640?from=appmsg "")  
  
  
  
03  
  
紧急修复，杜绝风险  
  
  
官方已发布补丁，按以下步骤操作，可彻底修复所有易利用漏洞：  
- 立即升级 ：前往 https://github.com/openclaw/openclaw/releases 下载最新版本，覆盖安装；  
  
- 清理插件 ：卸载来源不明插件，仅保留官方认证插件；  
  
- 开启二次确认 ：敏感操作（删除文件、执行命令）开启二次确认，避免误操作。  
  
官方公告：https://openclaw.ai/（可查看完整修复说明）  
  
  
04  
  
最后警示  
  
  
上述易利用漏洞操作简单、危害极大，使用OpenClaw的用户，务必立即升级修复，切勿抱有侥幸心理。  
  
转发给正在“养龙虾”的朋友，提醒其做好防范，避免设备被控制、数据泄露！  
  
