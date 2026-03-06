#  官方新漏洞-泛微云桥 e-Bridge系统 sendWxMsg 存在SQL注入漏洞  
原创 小菜鸟
                    小菜鸟  智动心域   2026-03-06 08:39  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJQ4JwYjlqNJxYQrKjdBSTVctcZAJPf7mtOpk5I8IHO0Qt1UicXRGHicEHy1kZCEWVIvo7tbFKLTmbBibcwhRYnvdhb1EuUuS7rh9I/640?wx_fmt=jpeg "")  
  
泛微云桥 e-Bridge 系统的 /wxthirdapi/sendWxMsg 接口在处理用户传入的 tpids 参数时，未对其进行有效的安全过滤，直接将  
  
用户可控的参数内容拼接进 SQL 查询语句中，导致攻击者可构造恶意 SQL 语句执行数据库操作。  
  
                             指纹  
  
FOFA：(body="泛微云桥e-Bridge" && (body="wx.weaver.com.cn"||body="www.weaver.com.cn"))||header="EBRIDGE_JSESSIONID" || title="泛微云桥e-Bridge"  
  
                              复现  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJS0icBGUkjXDVlT3geIia1ib20cibYicibDMeVsXos6DibETHa2vEtrtBnqt6rAysz95ArNsrPsXOGAAVU9NAZR5UEGlaVhk1s2hmiboL8/640?wx_fmt=jpeg "")  
  
                              圈子  
  
漏洞poc已发内部圈子，纷传圈子刚成立，适合需要新出漏洞poc和网络安全小白入门学习，不定期分享新出漏洞poc以及漏洞报告等学习资料，大佬误触  
  
            ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJSb2Bia2c3LX18as7eib5eTvj6jzaTlJtk5OTMYib9CpzM8jj1qU41ElgwnHskc80Q0jePgH6ZulV2yagUrwABPyJGSf0mODEXJia8/640?wx_fmt=jpeg "")  
  
  
  
