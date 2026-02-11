#  红队利器｜FnOS系统综合漏洞利用框架  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-11 05:03  
  
# FnOS GUI Exploit Tool  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
> **项目地址在文章底部哦**  
  
  
  
本项目是针对 FnOS 系统的综合漏洞利用工具，提供 **Web UI (网页版)**  
 和 **Desktop GUI (桌面版)**  
 两种交互模式，整合了资产管理、漏洞扫描、文件浏览、远程命令执行 (RCE) 及凭据窃取等核心功能。  
## 🌟 双版本特性  
  
本项目包含两个版本的操作界面，可根据实际场景灵活选择：  
### 1. Web UI (v2.1.1) - 当前推荐  
- **优势**  
: 现代化界面，支持多目标管理，可视化效果好，无需本地图形环境。  
  
- **优化**  
: 已针对 RCE 通道进行深度优化，支持长连接心跳、二进制数据兼容。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxjbpUjmhvXTBviap1O1enrZtXzzSyj7hX1v3OP8azmIVN5kdjmVAiaLTia2k9Qqfup109ZLlZlyPepdeibiaaJ0XNXVar9Ij5ARpFk/640?wx_fmt=png&from=appmsg "")  
## 🛠️ 环境搭建  
### 1. 基础依赖安装  
  
确保已安装 Python 3.8+。  
```
pip install -r requirements.txt
```  
> **注意**  
: 如果使用 GUI 版本的**图片预览**  
功能，请额外安装 Pillow  
 库：  
> pip install Pillow  
  
### 2. 启动方式  
#### 启动 Web 版 (推荐)  
```
python app.py
```  
  
启动后访问: http://127.0.0.1:7001  
#### 启动 GUI 版  
```
python run_legacy_gui.py
```  
## 📂 项目结构  
- app.py  
: **[Web 入口]**  
 Flask Web 应用主程序。  
  
- run_legacy_gui.py  
: **[GUI 入口]**  
 Tkinter 桌面版工具。  
  
- ```
core/
```  
  
 核心代码包。  
  
- rce_encrypted.py  
: 加密通道利用脚本（已优化，支持高可靠连接）。  
  
- rce_signed.py  
: 签名验证利用脚本。  
  
- scanner.py  
: 扫描核心逻辑，包含 LFI 探测引擎。  
  
- database.py  
: SQLite 数据库操作层，管理目标与配置。  
  
- file_ops.py  
: 封装远程文件操作（读取、上传、删除、递归下载）。  
  
- ```
exploits/
```  
  
RCE 核心利用模块。  
  
- templates/  
 & static/  
: Web UI 的前端资源。  
  
- data/  
: 数据存储目录。  
  
- assets/  
: 项目演示截图。  
  
## 🚀 核心功能详解  
### 1. 资产管理与自动化扫描  
- **批量导入**  
: 支持 CSV 批量导入目标，自动解析 IP、端口及协议。  
  
- **状态监控**  
: 实时跟踪目标扫描进度与漏洞存在情况。  
  
- **资产过滤**  
: 提供基于状态、关键字的快速筛选功能。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxp5yoEUzNxz2mVstvIsjp0V0M4ghzpYufXZerHFm6XqUalBGDBga8dRQa81Av6Kw8DyAS36ECV3rrUqibicQ2s3iayMrpkYA8c7M/640?wx_fmt=png&from=appmsg "")  
### 2. LFI 漏洞扫描引擎  
- **高并发能力**  
: 自定义线程池（1-100），实现毫秒级响应。  
  
- **智能指纹**  
: 通过识别 Linux 关键系统文件（如 /etc/os-release  
）和特定路径结构，确保高准确度。  
  
- **敏感文件扫描**  
: 自动化探测系统敏感文件，并提供在线预览。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyth3Rv8x1F9woXlKytOIGfMQ4GjoeJGosicAfqGg49dia039xpJtVRqO8FEhqZdqUKZnVicXSZZwjLBpibfLghPp0SOVI6fMNfuhk/640?wx_fmt=png&from=appmsg "")  
### 3. 深度文件浏览器 (File Explorer)  
- **全系统访问**  
: 利用 LFI 漏洞，实现对服务器文件系统的深度递归访问。  
  
- 文件操作流:  
  
- **在线预览**  
: 支持文本、JSON、配置文件的直接查看。  
  
- **快速上传/下载**  
: 支持单文件上传及目录递归打包下载。  
  
- **权限探测**  
: 自动识别目录与文件的可读性。  
  
- **WebDAV 入口识别**  
: 智能分析并提取 WebDAV 共享路径。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODw3vUfWCU6sRXPOfQtEp61ga254ymicOtJ8DLMiaxibiagsiaNibUd2X6YIgMun3s3lxRzuwIQtnKbT6LXkIKJqdcZG0n0xIiaZqBGM6o/640?wx_fmt=png&from=appmsg "")  
### 4. 远程命令执行 (RCE) 终端  
- 加密通道利用 (Encrypted Mode):  
  
- **无感利用**  
: 全自动完成 RSA 公钥获取、AES 密钥交换及 Payload 加密。  
  
- **绕过防御**  
: 利用 WebSocket 加密通道绕过大部分 WAF 与 IDS。  
  
- 签名执行模式 (Signed Mode):  
  
- **权限提升**  
: 在获取到系统私钥后，通过合法签名执行高权限指令。  
  
- **交互式体验**  
: 内置类终端界面，支持命令历史记录。  
  
- **稳定性增强**  
: 集成 WebSocket 心跳机制，支持长时间任务。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODz6cDN9sfVO7OfSjEQkZfGZwoTA8304yxpPGicnO8VTzPYqh45B5pbgym95tx48ibVIs2KyOiaQARky2uzc8OIQybXDw2A0c2ibVFM/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyofWpN0daqVKbiaXN9yvbjvVRaN3jia2hE5QnBo9P9M76NAPrxcYhpMdFmLNriczJA8o5SZxXVwCa0UibV0j8ibQ5aIpxUkYpU1YhQ/640?wx_fmt=png&from=appmsg "")  
## 📝 漏洞研究背景  
  
本工具旨在演示 FnOS 系统在以下维度的安全风险：  
1. **路径遍历 (Path Traversal)**  
：接口未对用户输入的路径进行安全清理。  
  
1. **不安全的通信协议**  
：WebSocket 接口在握手与消息处理阶段缺乏强认证。  
  
1. **敏感信息泄露**  
：系统关键配置与私钥文件存放路径可预测且权限设置不当。  
  
  
  
## 📖 项目地址  
```
https://github.com/nyzx0322/FnOS-GUI-Exploit-Tool
```  
## 💻 威胁情报推送群  
>   如果师傅们想要第一时间获取到**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
>  如果师傅们想要获取  
**网络安全相关知识内容**  
，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**  
。  
  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg "")  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
