#  工具推荐 | TsojanScan v2.0：BurpSuite 2026版专属漏洞扫描插件  
Tsojan
                    Tsojan  星落安全团队   2026-01-27 16:01  
  
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
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllmXglrUJpqQ7icHNRqauN53Dgm75M4YMI3sQGHbKPRs3eaibIzKH02ZUC2xb5QD7zKibLnL6TJVLbA0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2 "")  
  
**工具介绍**  
  
TsojanScan是  
一款集成的BurpSuite漏洞探测插件。  
本着市面上各大漏洞探测插件的功能比较单一，因此与  
TsojanSecTeam  
成员决定在已有框架的基础上修改并增加常用的漏洞探测POC，它会以最少的数据包请求来准确检测各漏洞存在与否，你只需要这一个足矣。  
  
功能介绍  
  
1、加载插件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCtBpDic9gG0chOX6Bb47JsXawHaSyQjOzUxKOLZXXgKxOMm8Cy8Z9ZUQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1 "")  
#### 2、功能介绍  
#### 1. 面板  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCADTcfN7qzRDK9mspMkD68DYnK0G8ke55DnJ247Y494ZSVXD58NuiaPg/640?wx_fmt=jpeg&watermark=1#imgIndex=2 "")  
  
自定义黑名单，插件不扫描黑名单的url列表，进行Reg匹配优先级第一。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCWwT7ia1fSQ7DEsqmTQPsQjTXaDHYwTbNaY4bbJ1h9SCfjRcOZL32NwQ/640?wx_fmt=jpeg&watermark=1#imgIndex=3 "")  
#### 2. 主动探测  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCxiaLyuib82f5tP39KgQIGvLADLEEkssRe8TgDxBhADgQBgpTKl5S0wiag/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4 "")  
  
比如探测非根目录/，目录下面需要加/  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCtRynPKzoh2400FaSxX1TIqBtQT3ZukEwI2IGkxVBTLjHiciaI7WanmGA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5 "")  
#### 3、fastjson >=1.2.80探测  
#### 1. 本地环境  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCRMhBOEIMp40ofxzMzcSxjHajHvP7UrzDLR4a6mkZZdfUUCibWY0uccw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6 "")  
#### 2. 预查询DNSlog接口  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCmicF2K4FGBddRpnNsjhuDdcvm8TTh8PzJl007WbwloE3QVfudSDdWPQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCHY55Ev7CDSUqXd9hB2BH2CXQgWhad1x8M10dCvqyiaPoWqZj1z55ibtQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8 "")  
#### 3. 扫描  
####   
#### 4. 判断准确版本  
  
1.2.80版本探测如果收到了两个dns请求，则证明使用了1.2.83版本，如果收到了一个 dns 请求，则证明使用了1.2.80版本。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCWdysxtUVOZZrBlRW9Gg1mAE8EZlKK1tWiar6pTXiaJws1CBTYPFlZIDQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCuibZEEFXt9bP7rY9zNsEJzlNt60yE7YRelAwBcN4b06lzNfbQ3ibj9Qg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11 "")  
#### 4、DNSLog查询漏报  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCFRy6Q9maB1ej7leuLEAURlBcR04ib5jic6WezD5qfuR0G36IZnRxUKlw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCVHhb4eqvRcXThKomPfeRuO7Y7NFObL7ytm4nLQudJgCBDDpJ63uDUg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaC8Oxic2ZqshViakTsWmOsfzHNbgfb4CzTIIZAHKwGz62lvpSpDoogYOicw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaC5E1KEHCY38btOTHfdhS2NFTFnRp4O1RiayR7DZ4Jm2J76WcTXSiczm0g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15 "")  
  
注意⚠️  
：扫描结束后才会在BurpSuite的Target、Dashboard模块显示高危漏洞，进程扫描中无法进行同步，但可以在插件中查看（涉及到DoPassive方法问题）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaC00CClOKOELD68cFrVibaiaZ5N6UGibhBCRVIkIibRIly1NquHKZHAWiaUqw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16 "")  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20260128  
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
  
  
