#  工具推荐 | 自动检测Vue框架 绕过Vue.js 站点路由守卫 一键发现隐藏资产与未授权漏洞  
Ad1euDa1e
                    Ad1euDa1e  星落安全团队   2026-02-02 16:00  
  
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
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllkHeOo24ias7Bmd5d3mpRHiaLsyxZsb2F234p6J7WF8a0WA7UOBQticfMelicXf0BCz3DGegSkKH3uABw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**工具介绍**  
  
VueCrack  
这是一个专为红队人员开发的浏览器插件，用于分析Vue框架网站的路由结构，并绕过路由守卫，从而发现站点的**隐藏资产**  
与**未授权访问漏洞**  
。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllm468SwvLRVA7g1YjVPzrqzN2STJYqaQsY3zmd3kAY8ChqdF8RnOxm4FA50WAArBv2W2BCibSUGwiaQ/640?wx_fmt=jpeg "")  
## 💻 开发背景  
- 本工具源于实际攻防中的需求，在对使用VUE框架的站点进行测试时，我们发现大量VUE站点绕过前端路由后，可以未授权访问站点页面，本插件简化了手动测试步骤，提高红队行动效率。  
  
- **本工具已多次在攻防、SRC挖掘场景中出货。**  
## 📝核心功能  
- **自动检测Vue框架**  
：快速识别目标站点是否使用Vue.js  
  
- **绕过路由守卫**  
：自动清除路由守卫，允许访问受保护路由  
  
- **修改鉴权字段**  
：自动修改路由元信息中的auth字段，绕过前端权限检查  
  
- **路由结构分析**  
：提取所有路由路径，包括可能隐藏的管理页面  
  
- **批量操作**  
：支持一键复制和访问所有发现的路由  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllm468SwvLRVA7g1YjVPzrqzT9RlGqPyVlzo4oMSknPFqnZRyO59f6DxGrFVsicOk6d25xXKQsjPEZg/640?wx_fmt=png&from=appmsg "")  
## 🔧使用方法  
1. 在 Chrome 或基于 Chromium 的浏览器中安装此扩展  
  
1. 访问基于 Vue.js 的网站  
  
1. 点击扩展图标，工具将显示所有可能的 URL 路径  
  
1. 使用生成的 URL 列表，尝试访问目标站点的受限页面  
  
1. 利用“打开”按钮直接导航到可能的未授权页面  
  
## 📄技术实现  
- **多重检测引擎**  
：使用多种策略检测Vue及Router实例  
  
- **守卫清除机制**  
：通过修改Router原型方法清除beforeEach等路由守卫  
  
- **权限标志修改**  
：递归遍历路由树，修改所有auth相关字段  
  
- **内存路由提取**  
：直接从内存中获取完整路由表，包括隐藏路由  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllm468SwvLRVA7g1YjVPzrqzgduV2ghLdMfu4u7cRicsHHro6icMNmnocfdUw6MWJ7NdHibicib1lHcqhcg/640?wx_fmt=png&from=appmsg "")  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260203  
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
  
  
