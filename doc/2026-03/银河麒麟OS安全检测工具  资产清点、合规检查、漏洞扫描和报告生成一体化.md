#  银河麒麟OS安全检测工具 | 资产清点、合规检查、漏洞扫描和报告生成一体化  
 黑白之道   2026-03-10 01:49  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
## 工具介绍  
  
SecKeeper 是一款专为银河麒麟操作系统设计的安全检测工具，提供资产清点、合规检查、漏洞扫描和报告生成等一体化安全服务。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMI0uPYbFTNYZFMdKfhlaicHGkpuPwjVraRibrHF5ibhl2c7EwsK9A8ictCLlRFw7DLYq9I6AKKtKQXYKuNvlXhWukV2YygOqtbsPzU/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1 "")  
## 项目结构  
- **前端部分**  
：backend/seckeeper-web  
  
- **后端四个模块**  
：  
  
- 资产扫描：backend/core/real_asset_scanner.py  
  
- 合规检查：backend/core/real_compliance_checker.py  
  
- 漏洞扫描：backend/core/real_vulnerability_scanner.py  
  
- 报告生成：backend/core/report_generator_fixed_safe.py  
  
- **主程序**  
：backend/app.py  
  
>   
> **注意**  
：在网页和后端如果需要密码，sudo管理员密码为：yinheqilin1  
  
## 工具使用  
1. 双击桌面 ces  
 文件夹，找到 backend  
 文件夹并双击打开。  
  
1. 在空白处鼠标右键，选择“打开终端”。  
  
1. 在终端中输入以下命令运行（如果依赖已安装可跳过安装步骤）：  
  
```
sudo pip install -r requirements.txt   # 安装依赖（正常运行时可以跳过）python3 app.py
```  
  
回车执行。 4. **保持前一个终端运行**  
，返回 backend  
 文件夹，找到 seckeeper-web  
 文件夹（前端）并双击打开。 5. 双击 index.html  
 文件即可在浏览器中打开相关页面。  
## 检查内容  
### 一、密码复杂度测试  
  
项目通过系统配置检查来测试密码复杂度：  
1. **检查系统密码策略文件**  
  
1. 读取 /etc/login.defs  
 中的 PASS_MIN_LEN  
 设置，验证最小密码长度。  
  
1. 检查 /etc/pam.d/common-password  
 中的 pam_pwquality.so  
 配置，验证是否启用了密码复杂度要求（如要求混合字符类型）。  
  
1. **密码熵计算**  
  
1. 使用数学公式计算密码强度：**密码长度 × log₂(使用的字符集大小)**  
  
1. 字符集包括：小写字母、大写字母、数字、特殊字符。  
  
1. 根据熵值评估密码强度等级。  
  
1. **实际检查项目**  
  
1. 密码最小长度是否达到安全标准（通常8位以上）  
  
1. 是否强制要求使用多种字符类型  
  
1. 密码过期策略设置  
  
1. 密码历史记录防止重复使用  
  
### 二、CVE漏洞数据导入  
  
项目采用本地JSON数据库管理CVE：  
1. **数据存储方式**  
  
1. 使用 data/cve_database.json  
 文件存储所有CVE信息。  
  
1. 每个CVE记录包含完整的元数据：ID、严重程度、描述、影响范围、修复方案等。  
  
1. **导入新CVE的方法**  
  
1. **首次运行自动初始化**  
：创建包含基础CVE记录的数据库。  
  
1. **手动JSON导入**  
：通过格式化的JSON文件批量导入新CVE。  
  
1. **单个CVE添加**  
：直接编辑JSON文件添加个别漏洞。  
  
1. **数据更新机制**  
  
1. 代码预留了从NVD官方API获取数据的接口。  
  
1. 支持从Ubuntu/Debian安全公告获取漏洞信息。  
  
1. 提供数据合并和去重功能。  
  
  
  
## 工具获取  
  
  
  
https://github.com/caibing3259/seckeeper  
  
  
> **文章来源：夜组安全**  
  
  
  
黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！  
  
如侵权请私聊我们删文  
  
  
**END**  
  
  
