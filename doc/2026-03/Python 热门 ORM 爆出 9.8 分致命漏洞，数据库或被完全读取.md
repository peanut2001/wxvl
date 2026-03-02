#  Python 热门 ORM 爆出 9.8 分致命漏洞，数据库或被完全读取  
 信安在线资讯   2026-03-02 01:50  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyHZicpicHphIKSvAczBhFfnMjY2Fo5VGN2xib8wStQ6ytmNqSMXVxMLocqcdQiaJ68pY2xficynQFC0vuzGdfPVibey1CUsKoya4Q37E/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=1 "")  
  
近日，Python 异步 ORM 库 **ormar**  
 被披露存在一项严重安全漏洞，编号为 **CVE-2026-26198**  
，CVSS 评分高达 9.8 分。该漏洞影响版本 0.9.9 至 0.22.0，波及范围广泛。  
  
漏洞核心问题出现在聚合函数 min() 与 max() 的实现逻辑中。开发者在构造 SQL 语句时，将用户可控的列名参数直接传入 sqlalchemy.text()，且未进行任何校验或过滤，从而形成典型的 SQL 注入风险。攻击者可通过构造恶意字段名，注入子查询语句，读取与当前模型无关的数据库表内容，实现未授权数据访问。  
  
由于 ormar 在 FastAPI 及异步 Python 应用中使用广泛，且官方示例代码常允许用户选择聚合字段，若接口直接将前端参数传入 Model.objects.min() 或 max()，即可成为完整的 SQL 注入入口。该攻击在 SQLite、PostgreSQL、MySQL 等主流数据库后端均已验证可行。  
  
研究指出，该问题自 2021 年 3 月 12 日引入（v0.9.9）后从未被修改，持续存在近四年。  
  
目前维护者已在 0.23.0 版本中完成修复。建议开发者立即检查依赖版本，尽快升级，同时审计所有涉及动态字段传参的聚合接口，避免将用户输入直接用于 SQL 构造。  
  
原文来源：安全圈  
  
  
**end**  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/P4iaXc3dZWwUh6aAJKHdg03U8MjI2BEHkyyjjNjRoqoG8lLIcwFpiczlibBXqXloia8NEd73sa6nyawS8ic3gtO2exQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=gt07df4r&tp=webp#imgIndex=1 "")  
  
  
