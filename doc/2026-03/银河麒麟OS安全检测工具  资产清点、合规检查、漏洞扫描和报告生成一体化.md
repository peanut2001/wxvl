#  银河麒麟OS安全检测工具 | 资产清点、合规检查、漏洞扫描和报告生成一体化  
caibing3259
                    caibing3259  夜组安全   2026-03-04 00:01  
  
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
  
SecKeeper 是一款专为银河麒麟操作系统设计的安全检测工具，提供资产清点、合规检查、漏洞扫描和报告生成等一体化安全服务。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMI87WxJGibOx8qEbKUL0h25bxwVMN6oIw1657PLtMSUSE3ZkaicsjyEm8KNMMG6Ij7AlND0IEpOnHONbRK2gzuAgkrKBeIonlgTM/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
260304  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[漏洞报告处理平台 - 支持Nuclei/Xray/自定义txt报告导入，AI驱动的安全漏洞管理与分析系统2026-03-03](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496368&idx=1&sn=c40c9187ca8b190e3b088cae3cb1f8b8&scene=21#wechat_redirect)  
[漏洞管理平台 | 支持Excel格式的漏洞扫描报告导入、智能关联资产、漏洞可视化管理2026-03-02](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496361&idx=1&sn=e640bdb2795d33f2a32945b4aed1d3d6&scene=21#wechat_redirect)  
[渗透测试Payload速查平台 | XSS/SQLi/SSRF/RCE | React+TypeScript2026-02-28](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496352&idx=1&sn=7b8ed88d924b2cfb098dba470262be32&scene=21#wechat_redirect)  
[一款专业的文件上传漏洞检测工具，支持263+绕过技术、代理抓包、动态扫描2026-02-27](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496341&idx=1&sn=775579f21a148fe435d9be115008c1b5&scene=21#wechat_redirect)  
[Nim编写Windows平台shellcode免杀加载器 | 免杀，Bypassav，免杀框架2026-02-26](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496327&idx=1&sn=e1e47d0056a0158d1b9edb63313eca87&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
