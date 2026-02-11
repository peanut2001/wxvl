#  upload_forge--专业文件上传漏洞扫描器  
原创 Hello888
                    Hello888  安全天书   2026-02-11 01:11  
  
0x01 工具介绍  
  
Upload Forge 是一款强大的生产级安全工具，旨在检测和利用网页应用中的文件上传漏洞。它专为渗透测试人员和安全研究人员设计，能够自动化测试文件上传表单的过程，针对各种绕过技术进行测试。  
  
主要特征  
- 🚀 异步扫描：高性能扫描引擎，由 和 驱动。httpxasyncio  
- 🕵️ 高级检测逻辑：  
- 分机旁通：双重扩展（）、大小写敏感性（）、稀有扩展（、）。.php.jpg.pHp.phtml.php5  
- **魔法字节伪造**  
：生成带有假头部（如PNG、GIF89a）的载荷以绕过内容检测。  
  
- 空字节注入：检测较旧的后端漏洞（）。shell.php%00.jpg  
- **多语种**  
：创建包含可执行代码的有效图像文件。  
  
- **🖥️ 现代图形界面**  
：采用PySide6构建的美丽暗色调图形界面，便于配置和实时监控。  
  
- **💻 Rich CLI**  
：功能丰富的命令行界面，包含进度条、表格和详细日志。  
  
- **📊 报告：**  
生成专业的HTML和JSON报告。  
  
- **🛡️ 验证**  
：通过尝试访问和执行上传文件，自动验证漏洞。  
  
![Screen Shot](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWKOeGRxt7g3cfOaGoChXcvcx9W67fZcDAR5MEYqERNtjy2FWL37dBicdicwbWqbicJBS6HPsbqCPnHzDdltGTYiaibbOM23tN7AtFo/640?wx_fmt=png&from=appmsg "")  
  
GitHub地址：  
```
https://github.com/errorfiathck/upload_forge
```  
  
注意：  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，  
安全性自测。  
  
0x02   
红蓝偶像练习生小圈子  
  
**圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化作，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结，学习笔记以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！圈子目前更新相关技术文章：HeavenlyBypassAV内部版-轻松免杀各大杀软Heavenly白加黑自动化生成免杀工具冰蝎webshell免杀工具哥斯拉webshell免杀工具红队场景下lnk钓鱼Bypass国内AV1日和0日POClnk钓鱼思路视频讲解lnk钓鱼Bypass天擎msi钓鱼chm钓鱼Kill360核晶AV对抗-致盲AV（核晶）捆绑免杀360杀火绒火绒6.0内存免杀kill-windows DefenderDefender分离免杀Defender知识点HeavenlyProtectionCS内部CS插件EDR对抗思路进程注入知识点自启动思路多种维权手法Fscan免杀核晶QVM解决思路红队思路-钓鱼环境下小窗口截屏窃取免杀Todesk/向日葵读取工具渗透测试文章思路内网对抗文章思路还有更多红队思路文章！期待您的加入！！！**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQXGy5hjatVdhgZaJJBcha5xCq57NrRWDEOlbhL5wPLcRqB3wKD5ib34yYh1VqhhGcbQEKd5xXMk2ghgecPl7zrDRyTCk77e0VbI/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
