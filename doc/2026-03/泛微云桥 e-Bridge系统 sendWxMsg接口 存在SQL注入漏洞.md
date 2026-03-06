#  泛微云桥 e-Bridge系统 sendWxMsg接口 存在SQL注入漏洞  
原创 小菜鸟
                    小菜鸟  智动心域   2026-03-06 06:11  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJRIib4vhtl54Orc26g8nBFFtdqRPiaAs0fm0nwLiahFCSCyArJu585SK8qONAjEyyrwsM2lNHw0gfwbnnOicAwicicaGWWeXMCvFiapoc/640?wx_fmt=jpeg "")  
  
泛微云桥 e-Bridge系统的 /wxthirdapi/sendWxMsg 接口在处理用户传入的 tpids 参数时，未对其进行有效的安全过滤，直接将用户可控的参数内容拼接进 SQL 查询语句中，导致攻击者可构造恶意 SQL 语句执行数据库操作。  
  
                             指纹  
  
FOFA：(body="泛微云桥e-Bridge" && (body="wx.weaver.com.cn"||body="www.weaver.com.cn"))  
  
  
                             复现  
  
  
                         
圈子  
  
漏洞poc已在圈子更新，纷传圈子刚成立，适合需要新出漏洞poc以及入门网安小白基础学习，大佬误触  
  
             ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJT1bs0DV0h5I9NhguHU1vff16XABwrLT7GTVfjUFgGnlW3MjFicmlgzwScFicu6bpkk0daIUZSlDYkI6mgYSqib5IGtBYRxOfT4pA/640?wx_fmt=jpeg "")  
  
  
  
