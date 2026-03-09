#  搜索框漏洞测试checklist  
原创 游山玩水
                    游山玩水  山水SRC   2026-03-09 01:00  
  
## 概述  
  
本文讲解了在渗透测试中遇到搜索框如何进行渗透测试  
  
## 特殊符号测试  
  
%  
  
_  
  
输入这两个个符号可能会导致返回全部文章信息/  
数据库语法错误或逻辑错误  
  
具体原因大概是字符的闭合  
  
比如%  
  
原搜索内容A：select * from xxxx where xxxx  like  %A%  
  
搜索内容% ：select * from xxxx where xxxx like %%%（就成了搜索全部信息了）   
  
  
  
超长字符（5000个A）  
  
这就是测试  
DoS漏洞（很刑）  
  
逐步增加测试内容看响应包呢相应时间，如果随着内容增加时间增加就存在dos漏洞  
  
bp响应时间查看的位置  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQicUHoUoqgYIlq6LowmbYNynhMicZicibQQKwicgHUI3M6Lsn0qWebwicNYkY0uLFoHGibPTibgYJWN6C2ibdkMrkicKMibSPibAEMq04rWsX4/640?wx_fmt=png&from=appmsg "")  
  
## SSRF  
  
**SSRF（服务器端请求伪造）漏洞的核心前提是：应用程序的服务器端能够根据用户的输入，向一个任意或受控的地址发起网络请求。**  
  
如何从外表直接判断搜索框是可能否存在SSRF？  
  
功能设计上就需要去外部拉取内容  
- **链接预览**  
：输入网址，后台抓取该网页的标题和描述。  
  
- **图片/视频搜索**  
：输入关键词，后台调用第三方API获取素材  
  
- **文档内容搜索**  
：输入一个文档链接（如http://example.com/doc.pdf  
），声称能搜索文档内文字  
  
- **跨平台比价/信息聚合**  
：搜索商品，后台去其他电商网站抓取价格。  
  
什么情况下不存在ssrf  
  
**纯文本/数据库搜索**  
  
仅对本站内的文章、商品、用户信息进行数据库查询，功能描述和流量分析均无任何对外网络请求的迹象。  
  
如何测试SSRF见下面文章链接  
  
[用Auto-SSRF+SSRFmap构建SSRF自动化利用链](https://mp.weixin.qq.com/s?__biz=MzY4MTEwNDczMA==&mid=2247483811&idx=1&sn=3597b0a69b1503a6e730e305f4de5fe6&scene=21#wechat_redirect)  
  
  
总结：搜索内容为本站东西不用测  
## xss  
  
因为很多平台对不收反射型xss漏洞，那么我们的视角就要在存储型xss漏洞上  
  
测试前提：  
用户的搜索历史被保存（例如，在用户个人中心显示“最近搜索”），先确定存在该功能再测试  
  
测试xss见下面文章链接  
  
[存储型XSS漏洞checklist](https://mp.weixin.qq.com/s?__biz=MzY4MTEwNDczMA==&mid=2247483771&idx=1&sn=e00461d4287fff8759741b6c1354be68&scene=21#wechat_redirect)  
  
## SQL注入  
  
测试sql注入看下面文章就行  
  
[SQL注入漏洞测试优化流程（1.1）](https://mp.weixin.qq.com/s?__biz=MzY4MTEwNDczMA==&mid=2247483833&idx=1&sn=72f39953006c1f301e8549446bf037d3&scene=21#wechat_redirect)  
  
  
  
