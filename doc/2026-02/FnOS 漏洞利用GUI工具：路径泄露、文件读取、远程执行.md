#  FnOS 漏洞利用GUI工具：路径泄露、文件读取、远程执行  
nyzx0322
                    nyzx0322  夜组安全   2026-02-06 00:05  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**NightCTI**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
## 工具介绍  
  
FnOS 综合漏洞利用工具 (FnOS Exploit Tool)，一个针对飞牛OS (FnOS) 的综合漏洞利用工具，集成了多种漏洞利用模块，旨在帮助安全研究人员验证系统安全性。工具采用 Python 编写，并提供了基于 Cyberpunk 风格的图形化界面 (GUI)，方便进行目标管理和漏洞验证。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UgySs9F0J5lmDAibOjPbqELOX7ba7DfwfTeYAibHibOk1kxSSC60R4EVzmYqyHRKSRyZC6uhO8AAvhw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UgySs9F0J5lmDAibOjPbqELxgJuuO5mbocyzYXINt4f2azoeam6iaetrXqlyTSFicYVxVLM0X1HLO3g/640?wx_fmt=png&from=appmsg "")  
## 主要功能  
  
本工具整合了针对 FnOS 的多个漏洞利用链，主要功能包括：  
- **🛡️ 认证绕过 (Authentication Bypass)**  
  
- 通过伪造 Secret 和 Token 绕过登录认证机制。  
  
- **📂 任意文件读取 (Arbitrary File Read)**  
  
- 利用路径穿越等漏洞读取系统敏感文件（如 /etc/shadow  
, rsa_private_key.pem  
 等）。  
  
- **⚡ 远程命令执行 (RCE)**  
  
- 利用漏洞链获取权限后执行任意系统命令。  
  
- 支持无需读取 RSA 私钥的命令执行方式（通过加密包实现）。  
  
- **🔑 Token 管理**  
  
- 支持 Fresh Token 生成、数据包签名与伪造。  
  
- **💻 图形化界面**  
  
- Cyberpunk 风格的 UI 设计。  
  
- 支持多目标配置管理（保存/加载目标 IP 和端口）。  
  
- 内置 WebSocket 和 HTTP 协议交互逻辑。  
  
## 使用方法  
1. **克隆或下载本项目到本地**  
  
1. **安装依赖**  
  
使用 requirements.txt  
 安装（推荐）：  
  
```
    pip install -r requirements.txt
```  
```
或者手动安装主要依赖：
```  
```
    pip install requests websocket-client pycryptodome pillow
```  
### 启动工具  
  
在项目根目录下运行主脚本：  
```
python run.py
```  
### 功能操作指南  
1. **配置目标**  
  
1. 在左侧配置栏输入目标 FnOS 系统的 **IP 地址**  
。  
  
1. 设置 **Web 端口**  
（默认为 888）和 **WebSocket 端口**  
（默认为 5666）。  
  
1. 点击 **“添加/更新目标”**  
 保存配置。  
  
1. **漏洞验证**  
  
1. 根据界面提示选择相应的漏洞利用模块（如文件读取、命令执行等）。  
  
1. 点击对应按钮开始验证。  
  
1. 查看右侧控制台输出获取执行结果。  
  
## 漏洞背景  
  
本工具涉及的漏洞主要包括：  
1. **任意文件读取**  
：允许攻击者读取服务器上的任意文件。  
  
1. **认证绕过**  
：利用 WebSocket 协议处理逻辑缺陷，伪造认证凭证。  
  
1. **授权命令执行**  
：结合上述漏洞，实现远程代码执行。  
  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260206  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[BurpSuite插件 | Xia Sql二开  SQL注入扫描神器！2026-02-05](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496263&idx=1&sn=c30c4a5930ced345924025d7232cc9d9&scene=21#wechat_redirect)  
[Burp Suite |  Web未授权访问漏洞检测插件2026-02-04](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496255&idx=1&sn=9da8e42382d92de4bb78f930bb29a98d&scene=21#wechat_redirect)  
[一个专为渗透测试和安全评估设计的资产管理平台，提供强大的数据聚合、关系分析和可视化能力2026-02-03](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496244&idx=1&sn=e542fc8c3097f9d5ea2e17b6c3c04028&scene=21#wechat_redirect)  
[基于腾讯云函数 (SCF) 的分布式 IP 代理池。用于绕过 WAF IP限制，支持安全扫描工具调用2026-02-02](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496237&idx=1&sn=a6ae0ce228701005bfb51116a83430bb&scene=21#wechat_redirect)  
[一个专为 AWD/AWDP 设计的竞赛自动化平台，提供 IP探测、WebShell 管理、SSH 终端、基线加固、Flag 读取等核心功能2026-01-30](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496226&idx=1&sn=ecafcf54d1f1045ba48d79fa9a93c017&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
