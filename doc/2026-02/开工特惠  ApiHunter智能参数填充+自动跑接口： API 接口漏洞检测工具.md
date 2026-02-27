#  开工特惠 | ApiHunter智能参数填充+自动跑接口： API 接口漏洞检测工具  
11firefly11
                    11firefly11  星落安全团队   2026-02-26 16:01  
  
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
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGpaBtjM9mjMWETAicwJ4d6qOSiavBOXatDvS0F19LtUicicxqTIxicYEuicO37ib4eVqaBibmPlPsw58xPxcM86mrUSFDibZxCSssCDg34/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**背景介绍**  
  
ApiHunter 是一款功能强大的 API 接口安全检测工具，专为渗透测试人员和安全研究人员打造。无需复杂的配置，支持 Swagger/OpenAPI 和 ASP.NET Help Page 文档一键导入，自动解析接口、智能填充参数、批量测试，并提供强大的敏感信息检测和漏洞扫描功能。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaF6GdUsGgmDz4ibNNfbIay0SRzkClxyp1r87miaB1jrk4k34wGTp5YoqGWB9h4nTAibvYtq9MvU7P99u0aux14Whj4RWdyt3N596M/640?wx_fmt=png&from=appmsg "")  
## 项目特点  
POST 智能填充与多格式测试：针对 POST/PUT 请求，工具不仅能自动智能填充参数值（如自动识别 id, email, phone 等），还会自动生成三种数据包格式进行测试：确保测试覆盖所有可能的参数传递方式，不遗漏任何漏洞。URL 参数模式 (Query String)JSON Body 模式 (application/json)Form Body 模式 (x-www-form-urlencoded)多文档格式一键导入：支持 Swagger 2.0/3.0 JSON 文档和 ASP.NET Web API Help Page 网页导入。自动解析所有接口端点、请求方法和参数定义，省去手动抓包的繁琐。自动文件上传检测：智能识别上传接口（upload/file等关键词），自动构造 multipart/form-data 请求，并上传 XSS 测试文件（.html）和普通文本文件，快速验证上传漏洞。强大的结果去重：内置智能去重引擎，根据“状态码 + 响应长度”进行指纹去重，有效过滤大量重复的无效响应（如统一的 404 或 500 页面），让您专注于有价值的差异化结果。敏感信息深度检测：内置 100+ 条高精度检测规则，覆盖云服务密钥 (AWS/Aliyun/Tencent)、各类 Token (JWT/Github)、数据库连接串、个人隐私信息 (手机/身份证/邮箱) 等，并支持用户完全自定义规则。安全模式与生产环境保护：提供“安全模式”，自动拦截 DELETE/PUT 等高危方法，并过滤包含 delete/remove/drop 等关键词的接口，防止在测试过程中误删数据。同时支持自定义黑名单。交互式数据包重发：双击任意结果即可查看标准 HTTP 格式的数据包，支持直接编辑请求头/体并立即重发。响应内容自动格式化（JSON/XML）并高亮敏感信息，方便二次验证。全面的代理与网络支持：支持 HTTP/HTTPS/SOCKS5 代理配置，方便配合 Burp Suite 进行流量转发。支持自定义请求头（Cookie/Authorization），轻松绕过鉴权。自定义参数值：支持自定义参数值,如userid:100,username:test等,如果不自定义参数也会采用默认配置自动补充参数## 🚀 快速开始  
  
**使用前请确保已获得目标系统的合法授权，本工具仅用于授权的安全测试。**  
1. **启动程序**  
  
1. 双击 ApiHunter.exe  
 即可启动，开箱即用。  
  
1. **开始任务**  
  
1. **方式一（单目标）**  
：输入 URL 和接口路径，点击测试。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaER6uAOgWwO0picOMtciaB0wpHD42icpVnT1H6LmOFcZ9pDdZPtbPXAgbFqZRywxHpOiaicwgWYt6u8yrbkoDO60Z5E99zbfv5IxD7g/640?wx_fmt=png&from=appmsg "")  
  
1. **方式二**  
：切换到“接口文档”区域，输入 Swagger/ASP.NET 地址，点击 [导入]  
，然后点击 [swagger]  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaG3bFibmK3IAHst2BTib7kmpMdLVw7NP18VhhuiacMqlHpNdgwU6G7P3BvgYicvDTdMw6nxDUaRsPe1BQv7OxW7YhlXtVjK1SOCNIM/640?wx_fmt=png&from=appmsg "")  
  
  
1. **查看结果**  
  
1. 扫描结果实时显示，敏感信息红色高亮。  
  
1. 双击行查看详情，右键可导出或复制。  
  
## 📖 使用指南  
### 1. 主界面操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFhgbYibp6eF1xFfj3t5OAYnWicoSeJZV2R5M3mgknG14hocVrnVJgeuG40l5nTG1jHycBfX4SRJ2Gia6oyTjoYNHAg2wnfdcIuwM/640?wx_fmt=png&from=appmsg "")  
- **接口文档导入**  
：选择文档类型，输入 URL，一键解析所有 API,点击swagger按钮跑接口。  
  
- **POST 自动填充**  
：无需手动输入参数，工具根据参数名自动生成测试数据（如 user_id=1  
, page=1  
）。  
  
- **代理设置**  
：在顶部输入框填入代理地址（如 http://127.0.0.1:8080  
），流量即可转发至 Burp。  
  
- **状态码过滤**  
：输入 404,500  
 可屏蔽无效结果。  
  
### 2. 设置面板与自定义  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaE2aChDP4SzDusu3jFnupUs7pS6AW88EKeGPm1LZLtSe2X6icw2E1RlJY12yttg6eufmyxdZnjXKcRsG0CJjapsYxgsTv0OowpE/640?wx_fmt=png&from=appmsg "")  
- **敏感规则**  
：支持正则自定义，可设置等级（High/Medium/Low）。  
  
- **请求头配置**  
：在此处添加 Cookie  
 或 Authorization  
 Token，实现登录态扫描。  
  
- **变异测试**  
：自定义 Fuzzing Payload（如 SQL 注入、XSS 字符），工具会自动对参数进行变异测试。  
  
- **安全设置**  
：切换安全模式/普通模式，配置接口黑名单。  
  
### 3. 数据包查看与重发  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHfdvykRj7QZGUudibyqzeDIkkPCBGArSx2toBYiaUbHNT8icg3Z3SrbW0rJMqhRKy85GLbl6eicGI6u5EibusL1dL2l5AVOrkRmxcY/640?wx_fmt=png&from=appmsg "")  
- **标准 HTTP 格式**  
：完整的请求/响应包，方便复制。  
  
- **可编辑重发**  
：修改参数后点击 [发送]，立即查看新响应。  
  
## 🌐 网站测试功能  
  
本工具针对 Web 网站渗透测试场景，提供了三大核心自动化功能，极大简化了手动操作流程。  
### 1. Swagger/OpenAPI 自动化测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHic8TSygpuAqibkkQzG2ibr7GFKVsaURVcxUMPUMLjz8nx0BH5gp78nBRdRgOGpeOLbzN40Ou4gSUwY733MDR9qZ5Fe6ukOSxric4/640?wx_fmt=png&from=appmsg "")  
  
针对现代前后端分离架构，直接解析 Swagger 接口文档，一键实现全站接口自动化测试。  
  
- **一键导入**  
：支持 JSON URL 或本地文件导入。  
  
- **自动解析**  
：完整解析 API 路径、请求方法、参数定义。  
  
- **智能填充**  
：根据参数类型和名称，自动填充测试数据。  
  
### 2. ASP.NET Web API Help Page 支持  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaHP8nSeKm2WlQlAEvxexLKvibnnU5n2O5y87CQYbwvEByhqX6fZZwPPx3xlIM3g9V5V19FUIqMibwnmMQp8mCI3hrg55R5IRk5ZE/640?wx_fmt=png&from=appmsg "")  
  
针对传统企业级 .NET 应用，支持 ASP.NET Web API 自动生成的 Help Page 文档解析。  
  
- **网页解析**  
：直接从 HTML 页面提取接口列表。  
  
- **示例参数提取**  
：自动提取文档中的 Sample Request 参数。  
  
### 3. 自动文件上传漏洞检测  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGoV3Iu5yvfjKU3tw1GPmKwgxKNWCQtMc9ibMibRV7iadDb03v9jWdKPpgWZia55lQGJjLhJ6SUr50JFwWm4FkdlyQPgZKk0ZLPfDo/640?wx_fmt=png&from=appmsg "")  
  
智能识别文件上传接口，自动构造 payload 验证上传漏洞。  
  
- **自动识别**  
：基于 URL 关键词 (upload/file) 和参数名自动锁定上传接口。  
  
- **双重 Payload：**  
- 222.html  
: 包含 XSS 测试代码 <script>alert('1')</script>  
  
- 12556.txt  
: 普通文本文件验证  
  
- **自动构造**  
：无需手动抓包，工具自动生成标准的 multipart/form-data  
 请求包。  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260227  
**”，即可获取项目下载地址！**  
  
****  
  
****  
**圈子介绍**  
  
博主介绍  
：  
  
  
目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。  
  
  
目前已经更新的免杀内容：  
- 部分免杀项目源代码  
  
- 星落安全内部免杀工具箱1.2.1  
  
- GoCobaltStrike星落专版2.0  
  
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
  
  
目前星球已满1100人，价格由208元  
调整为  
218元(  
交个朋友啦  
)，1200名以后涨价至268元。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHicicCAAxS6JIO8yP9LwImicVRvpTnFXMsF5DMAibon6Vibw1SuOyeVoCsgicqAqoUG2kmO7cEENKQfYdfPlBnwvbOD7k40BHU9XRhA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11 "")  
  
     
往期推荐  
     
  
  
1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)  
  
  
  
2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)  
  
  
  
3.[新增全新Web UI版本，操作与管理全面升级 | GoCobalt Strike 2.0正式发布！](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247497899&idx=1&sn=018f02ef4064930cbcb40d6b0495e136&scene=21#wechat_redirect)  
  
  
  
4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12 "")  
  
  
