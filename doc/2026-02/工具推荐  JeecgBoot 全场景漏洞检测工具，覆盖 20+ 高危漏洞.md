#  工具推荐 | JeecgBoot 全场景漏洞检测工具，覆盖 20+ 高危漏洞  
Msup5
                    Msup5  星落安全团队   2026-02-09 16:00  
  
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
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaFiaAiauG0Bj7t0ibHiaicBbp6MJGDJdP8iaQfWaTSpZbS9ricNmRqYHhVb7XAKT6ewwGKwHgvicuBSugVDbhAmJ54dzCeibZHZAv3FicY2A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**背景介绍**  
  
针对 JeecgBoot 框架中频发的 SQL 注入、命令执行等漏洞，传统手动检测方式效率低、覆盖不全。JeecgGo 作为专为该框架打造的全场景漏洞检测工具，能有效提升测试效率与准确性。工具基于 Go 语言开发，集成 20 余种高危漏洞检测模块，涵盖 queryTableData 注入、testConnection 命令执行、未授权文件上传等核心风险点。支持携带 Token 进行身份验证、按需指定漏洞检测，检测结果自动导出为 JSON 格式，便于后续分析与报告生成。下文将系统介绍工具的使用方法与核心功能，助力安全团队高效完成 JeecgBoot 框架的安全评估。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHZCzv9TJBDP8y4jt4erXB1XxcZd1Vuhg9MlibAyCs43UavicdzGia4ibq0icriaxLQJ7xLxicyXcYKicibC3DQfLy67YsTHT1h6f5ZN4NY/640?wx_fmt=png&from=appmsg "")  
## 功能介绍  
  
全方位 JeecgBoot 漏洞检测覆盖 **20+ 类高危漏洞**  
，涵盖核心风险场景：  
  
**SQL 注入**  
：包含 queryTableData、qurestSql、getTotalData、show、getDictItemsByTable、check、column、parseSql 等 **9 类注入漏洞**  
，支持后台未授权注入检测。  
  
**命令执行 / 代码注入**  
：覆盖 testConnection 远程命令执行、loadTableData SSTI 模板注入、queryFieldBySql 模板注入、sendMsg Freemarker 注入、AviatorScript 表达式注入等 **5 类执行类漏洞**  
。  
  
**文件上传**  
：检测 jmreport/upload 未授权任意文件上传、commonController.do 任意文件上传等 **2 类上传漏洞**  
。  
  
**信息泄露 / 权限漏洞**  
：支持 querySysUser、checkOnlyUser、httptrace、dataSource_list 数据库账号密码泄露、fileTree 目录遍历、passwordChange 任意用户密码重置等 **6 类风险检测**  
。  
  
**灵活的测试模式**  
适配不同实战场景：  
- **基础 URL 一键扫描**  
：快速发现目标漏洞  
  
- **携带 Token 授权测试**  
：模拟已登录用户检测权限漏洞  
  
- **指定漏洞精准验证**  
：支持按漏洞名称（如 sendMsg、loadTableData） + 自定义命令（id、whoami）进行针对性检测  
  
**精准的检测逻辑**  
：  
- 针对 check、column 等注入漏洞采用**延时技术检测**  
，通过响应时间差异判定风险  
  
- 提示手动验证，规避网络波动导致的误报  
  
**便捷的结果输出**  
：  
- 扫描完成自动生成 **results.json**  
 文件  
  
- 清晰记录漏洞 URL、攻击 payload、响应内容  
  
- 便于后续分析与手动验证  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaGPP3ickMMZgSDk9FCjErB4I1NmbZgn4YstapzqEeTXqsgnKwGVBohTjwOic5QoJjCib8YUia7ibmBUvsqch03CgE1nUfghNLUrIS4Y/640?wx_fmt=png&from=appmsg "")  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260210  
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
  
  
