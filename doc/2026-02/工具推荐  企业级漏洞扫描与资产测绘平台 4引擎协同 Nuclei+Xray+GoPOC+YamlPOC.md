#  工具推荐 | 企业级漏洞扫描与资产测绘平台 4引擎协同 Nuclei+Xray+GoPOC+YamlPOC  
taielab
                    taielab  星落安全团队   2026-02-01 16:00  
  
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
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKsVkic6jOeaJlmoxeelYvrdSDUvvBSialdFbBVZ5lthqQbpQvlZeJ2UtQN3dZN8NVbtZTEo8S624g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**工具介绍**  
  
**YinVulKiller**  
 是一款功能强大的企业级漏洞扫描与资产测绘工具，集成了主机存活探测、端口扫描、服务识别、指纹识别、漏洞检测、弱口令爆破等多种功能。  
### 🎯 核心特性  
- 🚀 **三引擎 POC 检测**  
：集成 Xray + Nuclei + GoPOC 三大引擎，12,492+ POC 规则  
  
- 🔍 **深度服务识别**  
：基于 Gonmap/Nmap 探针库，6000+ 服务指纹  
  
- 🌐 **全面资产扫描**  
：支持 IP/CIDR/URL 多种目标格式，智能并发调度  
  
- 🛰️ **网络空间测绘**  
：集成 FOFA/Hunter 平台，自动资产发现与联动扫描  
  
- 📂 **目录扫描模块**  
：内置双字典（31,094 + 1,613 条路径），快速发现隐藏目录  
  
- 🎨 **多格式报告**  
：Excel/HTML 双格式报告，自动截图，可视化展示  
  
- 🔐 **30+ 弱口令模块**  
：覆盖 SSH、RDP、MySQL、PostgreSQL、SMB2/SMB3 等主流服务  
  
- 🧩 **640+ 指纹规则**  
：精准识别 Web 框架、中间件、CMS 系统  
  
- 🌍 **内网穿透**  
：Spy 网段探测 + 代理支持，适配复杂网络环境  
  
- 📦 **POC 外部化管理**  
：支持自定义 POC 规则，无需重新编译  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllkHeOo24ias7Bmd5d3mpRHiaL7kXGKiaS8XBXA1R1EzicSHjaOAQf5S1xfraCd08trEib3lJJGC7icdiawlg/640?wx_fmt=png&from=appmsg "")  
  
基础扫描  
```
# 1. 快速扫描单个主机（TOP100 端口）
./yinvulkiller scan -i 192.168.1.1 -p top100
# 2. 扫描整个 C 段（TOP500 端口）
./yinvulkiller scan -i 192.168.1.0/24 -p top500 --noping
# 3. 扫描指定 URL
./yinvulkiller scan -u https://example.com
# 4. 批量扫描 URL 文件
./yinvulkiller scan --urlfile urls.txt
# 5. 使用 Nuclei 引擎深度扫描
./yinvulkiller scan -u http://target.com --engine nuclei
# 6. 使用代理扫描
./yinvulkiller scan -i 8.8.8.8 -p top100 --proxy http://127.0.0.1:8080
```  
  
📚 功能详解  
  
🔍 扫描模式  
  
1. 资产扫描模式  
```
# 快速资产探测（不进行漏洞和弱口令扫描）
./yinvulkiller scan -i 192.168.1.0/24 -p top100 --nopoc --nocrack --noimg
```  
  
2. 全面漏洞扫描  
```
# 启用所有检测模块
./yinvulkiller scan -i 192.168.1.0/24 -p top500 --deep-scan
```  
  
3. 数据库专项扫描  
```
# 仅扫描数据库端口 + 弱口令爆破
./yinvulkiller scan -i 192.168.1.0/24 --dbs
```  
  
4. Web 应用扫描  
```
# 仅扫描 Web 端口 + POC 检测 + 截图
./yinvulkiller scan -i 192.168.1.0/24 --web
```  
  
5. 高危端口扫描  
```
# 仅扫描高危端口（SSH/RDP/MySQL/Redis等）
./yinvulkiller scan -i 192.168.1.0/24 --risk
```  
  
6. 目录扫描模式  
```
YinVulKiller 内置专业目录扫描功能，支持双字典选择：
# 使用默认字典（31,094 条路径）
./yinvulkiller dirsearch -u http://example.com
# 使用高危字典（1,613 条高风险路径）⭐ 推荐
./yinvulkiller dirsearch -u http://example.com --dict-type high
# 自定义字典
./yinvulkiller dirsearch -u http://example.com -f custom.txt
# 高级参数：并发、状态码过滤、代理
./yinvulkiller dirsearch -u http://example.com --dict-type high \
  -c 100 --code "200,403,500" \
  -p socks5://127.0.0.1:1080
# 指定输出格式（默认: txt,json）
./yinvulkiller dirsearch -u http://example.com -o html         # HTML 可视化报告
./yinvulkiller dirsearch -u http://example.com -o txt,csv,html # 多格式输出
./yinvulkiller dirsearch -u http://example.com -o all          # 所有格式
```  
  
输出格式：  
  
📄 TXT - 表格形式纯文本（推荐日常查看）  
  
📊 JSON - 机器可读（API/脚本集成）  
  
📑 CSV - Excel/WPS 打开（数据分析）  
  
🌐 HTML - 浏览器查看（带样式、搜索、高亮）  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260202  
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
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllk2esLaDRsI4yjB0HkCibHzialJBFBfcyeib4RRsQTOiamqSvAfZogia7pIcSY9lvfTicWXuTcCgtu3NP1w/640?wx_fmt=jpeg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11 "")  
  
     
往期推荐  
     
  
  
1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)  
  
  
  
2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)  
  
  
  
3.[新增全新Web UI版本，操作与管理全面升级 | GoCobalt Strike 2.0正式发布！](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247497899&idx=1&sn=018f02ef4064930cbcb40d6b0495e136&scene=21#wechat_redirect)  
  
  
  
4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12 "")  
  
  
