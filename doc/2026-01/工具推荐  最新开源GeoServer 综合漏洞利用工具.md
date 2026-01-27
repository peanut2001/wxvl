#  工具推荐 | 最新开源GeoServer 综合漏洞利用工具  
netuser
                    netuser  星落安全团队   2026-01-26 16:01  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/spc4mP9cfo75FXwfFhKxbGU93Z4H0tgt4O9libYH9mKfZdHgvke0CeibvXDtNcdaqamRk3dEEcRQiaWbGiacZ2waVw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
点击上方  
蓝字  
关注我们  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/WN0ZdfFXY80dA2Z4y8cq7zy2dicHmWOIib5sIn8xAxRIzJibo2fwVZ3aicVBM8RnAqRPH5Libr4f02Zs5YnMLBcREnA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
  
现在只对常读和星标的公众号才展示大图推送，建议大家能把  
**星落安全团队**  
“  
**设为星标**  
”，  
否则可能就看不到了啦  
！  
  
【  
声明  
】本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统以及盈利等目的，一切后果由操作者自行承担！！！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllmoE4FJAmgtiaS12eB9iaa5mejA0UGGiasuhfGWzfSShfmFjgf0ylt4iaPCSkEHEGqtzlZxmHiaXvr6t6Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**工具介绍**  
  
一个简洁高效的 GeoServer 漏洞验证平台，提供图形化界面和多个常见漏洞的利用功能。  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllmXglrUJpqQ7icHNRqauN53D5Kk4VObz4Ft6jz3RWwjd317JbiaLXHPkdY74SGFwxWGhVyrFylyoO7A/640?wx_fmt=png&from=appmsg "")  
## 功能模块  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;"><span cid="n7" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">漏洞</span></span></span></th><th style="box-sizing: border-box;"><span cid="n8" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE</span></span></span></th><th style="box-sizing: border-box;"><span cid="n9" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">功能</span></span></span></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span cid="n11" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">RCE 命令执行</span></span></span></td><td style="box-sizing: border-box;"><span cid="n12" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE-2024-36401</span></span></span></td><td style="box-sizing: border-box;"><span cid="n13" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">执行系统命令</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span cid="n15" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">内存马注入</span></span></span></td><td style="box-sizing: border-box;"><span cid="n16" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE-2024-36401</span></span></span></td><td style="box-sizing: border-box;"><span cid="n17" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">注入内存马</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span cid="n19" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">XXE 注入</span></span></span></td><td style="box-sizing: border-box;"><span cid="n20" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE-2025-30220</span></span></span></td><td style="box-sizing: border-box;"><span cid="n21" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">文件读取和 SSRF</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span cid="n23" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">反弹 Shell</span></span></span></td><td style="box-sizing: border-box;"><span cid="n24" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE-2024-36401</span></span></span></td><td style="box-sizing: border-box;"><span cid="n25" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">交互式命令执行</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span cid="n27" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">文件读取</span></span></span></td><td style="box-sizing: border-box;"><span cid="n28" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">CVE-2025-58360</span></span></span></td><td style="box-sizing: border-box;"><span cid="n29" mdtype="table_cell" style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">读取服务器文件</span></span></span></td></tr></tbody></table>## 使用方法  
1. 选择漏洞模块：左侧单选按钮选择要测试的漏洞  
  
1. 输入参数：在右侧输入框填入目标 URL 和对应参数  
  
1. 执行验证：点击"执行漏洞验证"按钮  
  
1. 查看结果：下方显示执行结果  
  
## 功能特点  
- 📱   
简洁的图形化界面（基于 Fyne）  
  
- 🔄 自动适配参数字段（切换模块时清空输入）  
  
- 🌐 支持 HTTP 代理设置  
  
- ⚡ 异步执行，无需等待  
  
使用示例  
### 命令执行  
1. 选择 "RCE 命令执行"  
  
1. 输入目标 URL：  
http://192.168.1.100:8080  
  
1. 输入命令：  
cat /etc/passwd  
  
1. 点击 "执行漏洞验证"  
  
### 内存马注入  
1. 选择 "内存马注入"  
  
1. 输入目标 URL  
  
1. 点击 "执行漏洞验证"  
  
1. 使用提示的配置（JAVA_AES_BASE64, pass, key）访问   
/*  
 路径  
  
### XXE 注入  
1. 选择 "XXE 注入"  
  
1. 输入目标 URL  
  
1. 输入恶意 XSD URL：  
http://attacker.com/evil.xsd  
  
1. 点击 "执行漏洞验证"  
  
反弹 Shell  
1. 选择 "反弹 Shell"  
  
1. 输入目标 URL  
  
1. 输入攻击机 IP：  
192.168.1.50  
  
1. 输入监听端口：  
4444  
  
1. 在攻击机上开启监听：  
nc -lvnp 4444  
  
1. 点击 "执行漏洞验证"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllmXglrUJpqQ7icHNRqauN53DWTOibKm2QRAyXbAMXb0WLpm0DrM84YO8oic3SQibsvV1uB8eF44OjFWsQ/640?wx_fmt=png&from=appmsg "")  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260127  
**”，即可获取项目下载地址！**  
  
****  
  
****  
**圈子介绍**  
  
博主介绍  
：  
  
  
目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。  
  
  
目前已经更新的免杀内容：  
- 部分免杀项目源代码  
  
- 星落安全内部免杀工具箱1.0  
  
- CobaltStrike4.9.1星落专版1.9  
  
- 一键击溃windows defender  
  
- 一键击溃火绒进程  
  
-    
CobaltStrike免杀加载器  
  
- 数据库直连工具免杀版  
  
- aspx文件自动上线cobaltbrike  
  
- jsp文件  
自动上线cobaltbrike  
  
- 哥斯拉免杀工具   
XlByPassGodzilla  
  
- 冰蝎免杀工具 XlByPassBehinder  
  
- 冰蝎星落专版 xlbehinder  
  
- 正向代理工具 xleoreg  
  
- 反向代理工具xlfrc  
  
- 内网扫描工具 xlscan  
  
- Todesk/向日葵密码读取工具  
  
- 导出lsass内存工具 xlrls  
  
- 绕过WAF免杀工具 ByPassWAF  
  
- 等等...  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9 "")  
  
  
目前星球已满1000人，价格由208元  
调整为  
218元(  
交个朋友啦  
)，1100名以后涨价至268元。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllk2esLaDRsI4yjB0HkCibHziaIib60SuyBT4jibwGo2PTfuzEmmaS80AC6WsEn8D2CsxReEBsZPiadegrw/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11 "")  
  
     
往期推荐  
     
  
  
1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)  
  
  
  
2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)  
  
  
  
3.[【免杀】CobaltStrike4.9.1二开 | 自破解 免杀 修复BUG](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247488486&idx=1&sn=683083d38a58de4a95750673d9cb725d&scene=21#wechat_redirect)  
  
  
  
4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12 "")  
  
  
