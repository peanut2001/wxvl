#  可视化漏洞扫描器Nuclei_Gui、支持POC管理与生成  
原创 小白爱学习Sec
                        小白爱学习Sec  小白爱学习Sec   2026-03-03 00:01  
  
**免责声明**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=wxpic&random=0.18042352401019524&random=0.49301784938611526&random=0.7409665131631742 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/7L4WY53VhUO2spBG8TGAPF8o98Ac6Y3EPLSEFGmKXeZyQCOGkqFWbeMibTfC1wZLjJTDmLb4Z0P9VCAV3RLDbbQ/640?random=0.11828586430527777&random=0.3266770581654057&random=0.7229092426155448 "")  
  
本文旨在提供有关特定漏洞工具或安全风险的详细信息，以帮助安全研究人员、系统管理员和开发人员更好地理解和修复潜在的安全威胁，协助提高网络安全意识并推动技术进步，而非出于任何恶意目的。利用本文提到的漏洞信息或进行相关测试可能会违反法律法规或服务协议。  
作者不对读者基于本文内容而产生的任何行为或后果承担责任。  
如有任何侵权问题，请联系作者删除。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**简单介绍**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
Nuclei_Gui工具基于 PyQt5 开发，以 Nuclei 为核心扫描引擎，融合 AI 辅助能力，工具支持 POC 全流程管理，涵盖导入、编辑、测试、同步及 AI 自动生成，大幅降低 POC 使用门槛。同时整合多款主流资产搜索引擎，实现漏洞扫描全流程可视化操作。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**功能介绍**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
<table><thead><tr><th data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">功能模块</span></section></th><th data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">核心能力</span></section></th></tr></thead><tbody><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">漏洞扫描</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">单 / 批量目标扫描、多 POC 模板选择、实时进度展示、暂停 / 恢复 / 取消扫描、结果导出</span></section></td></tr><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">任务管理</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">多任务排队执行、优先级设置、断点续扫、任务状态实时监控、耗时 / 时间记录</span></section></td></tr><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">POC 管理</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">导入 / 同步 / 编辑 / 测试 / 收藏 POC、按严重程度 / 标签筛选、语法高亮编辑器</span></section></td></tr><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">POC 生成器</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">多步骤配置、根据请求包自动生成、支持漏洞信息补充</span></section></td></tr><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">资产搜索</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">多引擎集成、结果直接导入扫描、搜索历史记录</span></section></td></tr><tr><td data-colwidth="195" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">AI 助手</span></section></td><td data-colwidth="365" style="border: 1px solid rgb(204, 204, 204);padding: 8px;text-align: left;"><section><span leaf="">多接口兼容、五大核心 AI 功能、智能分析与生成</span></section></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakHibJ94kicUSZLO0XqicU6zrzNxHDtg3xruWib0icOgPRQIyxqNPrpibf7MpD2kMfNMgicibuOC5KvkzoLduvibHObZvSXZ6nrVprwzoN0rM/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH9CmpvJu19952VXG3UnaNhEHfzUQqHBAI1o9OQCiakBWTPZKpo37Lia6XTLuK56uZzg0NWSsIDcZg9x9ssnOmbyVPSZcDVg9tvP4/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakHibKQic5JfWr44CYIXbaWX8SLFCGLZicGG4t7796wJeEzPDh6M4wJDe3lwhJDtTWlrYXQl8277SiaUAQASYmWjaeEicsavxKuxCyGLk/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**安装使用**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
Nuclei_Gui 实现**Windows/macOS/Linux**  
全平台无缝兼容，且完成多项人性化更新优化，解决跨平台使用的各类问题，上手零障碍。  
### 环境要求  
  
```
Python 3.8+
Windows 10/11 / macOS 10.14+ / Linux (Ubuntu 18.04+)
```  
  
安装依赖  
  
```
pip install -r requirements.txt
```  
  
### 安装 Nuclei 扫描引擎  
#### 方法一：程序内置下载（推荐）  
  
```
安装nuclei失败建议连接代理重试
程序启动后会自动检测 Nuclei 状态，如果未安装会显示下载按钮：
```  
1. **主界面下载**  
：点击"下载最新版本 Nuclei"按钮  
  
1. **设置界面下载**  
：在设置对话框中点击"下载 Nuclei"按钮  
  
程序会：  
- 自动检测您的操作系统和架构  
  
- 从 GitHub 下载最新版本的 Nuclei  
  
- 自动解压并重命名为正确的文件名  
  
- 设置执行权限（Unix 系统）  
  
#### 方法二：命令行自动下载  
  
```
# 简化版下载（推荐，网络问题已修复）
python download_nuclei_simple.py

# 带进度条下载
python download_nuclei_with_progress.py
```  
#### 方法三：手动安装  
1. 访问   
Nuclei Releases  
  
1. 下载适合您系统的版本并放入 bin/  
 目录  
  
1. 根据系统重命名文件：   
  
- **Windows**  
: nuclei.exe  
  
- **macOS**  
: nuclei_darwin  
  
- **Linux**  
: nuclei_linux  
  
1. 设置执行权限（Unix 系统）：   
  
```
chmod +x bin/nuclei_darwin  # macOS
chmod +x bin/nuclei_linux   # Linux
```  
#### 方法四：系统安装  
  
如果您已经在系统中安装了 Nuclei，程序会自动使用系统版本：  
  
```
# macOS (使用 Homebrew)
brew install nuclei

# Linux (使用包管理器)
sudo apt install nuclei  # Ubuntu/Debian

# 或者直接下载到系统路径
sudo wget -O /usr/local/bin/nuclei https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei_linux_amd64
sudo chmod +x /usr/local/bin/nuclei
```  
### 启动程序  
  
**Windows**  
：  
```
python main.py# 或双击 Run_Nuclei_GUI.bat
```  
  
**macOS/Linux**  
：  
```
python3 main.py
```  
  
**资源下载**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=wxpic&random=0.18042352401019524&random=0.49301784938611526&random=0.7409665131631742 "")  
  
  
点击下方名片后台回复【  
NucleiGui  
】获取资源信息  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/x095A8xUTuWMRpvvqmMwKABosFPL6ptacLNz6fxia55bJuCgfYNDtSfiaSIZ9nU9IxDicXfNricwyMTJZUgo9dIgTg/640?wx_fmt=gif&from=appmsg "")  
  
创作不易，点赞、分享、转发支持一下吧！！  
  
