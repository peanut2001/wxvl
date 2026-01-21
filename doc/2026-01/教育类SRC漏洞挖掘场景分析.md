#  教育类SRC漏洞挖掘场景分析  
原创 youki
                    youki  C4安全   2026-01-21 02:53  
  
教育类SRC常见的资产包括高校官网、教务系统、选课系统、成绩查询、校园一卡通、学生管理系统、科研平台、在线考试系统等。  
### 一、信息收集  
### 这一步还是老生常谈的信息收集，熟悉的师傅们可以跳过  
#### 1. 域名与子域名枚举  
- **目标：****发现所有可能的Web入口**  
- **工具与方法：**  
- 使用 amass  
、subfinder  
、assetfinder  
 进行子域名爆破：  
  
```
amass enum -d edu.cn -o subdomains.txt
subfinder -d jiaoyu.edu.cn -o subs.txt
```  
- 利用搜索引擎语法（Google Dork）：  
  
```
site:jiaoyu.edu.cn inurl:login
site:*.edu.cn intitle:"教务系统"
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmSTKcEo2DYwBFlzmpWAxQ2gDhVapY1BjTUuwR93MKSnIzDibLmbGqEHOw/640?wx_fmt=png&from=appmsg "")  
- 查询证书透明度日志（如 crt.sh）获取历史子域名。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmS3Mvga38pleys3KeUiamHWj1zUlHA2xdMDqAlnIGjvzvKuCJuDFTZcrw/640?wx_fmt=png&from=appmsg "")  
  
#### 2. 资产识别与分类  
- 使用 httpx  
 批量探测存活服务：  
  
```
cat subdomains.txt | httpx -status-code -title -tech-detect -o alive.txt
```  
- 重点关注以下路径和系统：  
  
- /jwglxt  
 —— 教务管理系统（常见为正方、青果、东师等）  
  
- /xxglxt  
 —— 学生管理  
  
- /ksxt  
 —— 考试系统  
  
- /ykt  
 —— 一卡通系统  
  
- /lib  
 或 /opac  
 —— 图书馆系统  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmSTwJxbxfAnTfy1ib3YXusbAbgm0oibjbjPqMe7ibtuUHMNVjibwsKtr27wA/640?wx_fmt=png&from=appmsg "")  
#### 3. 技术栈识别  
- 常见技术组合：  
  
- 后台框架：Struts2、Spring MVC、ASP.NET（老系统居多）  
  
- 数据库：Oracle、SQL Server（部分MySQL）  
  
- 中间件：Tomcat、IIS、WebLogic（较少但存在）  
  
使用 Wappalyzer  
 浏览器插件或 whatweb  
 命令行工具识别  
  
### 二、常见漏洞点与利用思路  
#### 1. 弱口令与默认账户  
- **原因：管理员设置弱密码，或未修改出厂默认账号**  
- **测试方式：**  
- 用户名：admin  
, root  
, jwc  
, system  
  
- 密码：123456  
, admin123  
, jiaoyu@2023  
, Password1  
  
- 尝试登录页面使用常见组合：  
  
#### 2. SQL注入（SQLi）  
- **典型场景：**  
- 成绩查询接口：/score?stu_id=123  
  
- 课程查询：/course?id=1'  
  
- **检测方法：**  
- 输入 '  
 观察是否报错（如 Oracle 的 ORA-xxxxx  
 错误）  
  
- 使用时间盲注 payload 测试延迟响应  
  
```
http://xxx/score?stu_id=1'; IF(1=1) WAITFOR DELAY '0:0:5';--
```  
#### 3. 越权访问（水平/垂直越权）  
- **原理：系统未校验当前用户是否有权访问指定资源。**  
- **案例：**  
- A学生访问 /user/profile?uid=1001  
，修改参数为 uid=1002  
 查看他人信息。  
  
- 普通教师尝试访问 /admin/config  
 管理页面。  
  
- **验证方法：**  
- 登录两个不同权限账号（如学生和老师），抓包比较请求差异。  
  
- 修改关键参数（如 userid  
, role  
, deptid  
）观察返回内容变化。  
  
- 使用 Burp Suite 的 Compare  
 功能对比响应差异。  
  
#### 4. 文件上传漏洞  
- **常见位置：**  
- 头像上传  
  
- 论文提交系统  
  
- 教师资料上传  
  
- **绕过技巧：**  
- 后缀限制绕过：.php3  
, .phtml  
, .htaccess  
  
- MIME 类型伪造：将 Content-Type: image/jpeg  
 发送 PHP 内容  
  
- 配合解析漏洞（如 Apache 解析 .php.  
）  
  
#### 5. 反序列化漏洞（Java系系统常见）  
- **目标系统：基于 Struts2 或 Spring 的老版教务系统。**  
- **检测点：**  
- 检查是否存在 /struts-action  
 类路径  
  
- 查看 Cookie 或 Header 是否包含 Base64 编码的对象数据  
  
- 使用 ysoserial  
 构造 payload（仅限内网测试）  
  
#### 6. SSRF 与内网探测  
- **应用场景：**  
- 系统提供“导入外部图片”、“抓取网页快照”等功能  
  
- 利用该功能访问内部地址（如 http://127.0.0.1:8080/manager/html  
）  
  
- 示例请求：  
  
```
POST /import_image HTTP/1.1
Host: service.edu.cn
Content-Type: application/x-www-form-urlencoded

url=http://127.0.0.1:8080/manager/html
```  
#### 7. JWT 安全问题  
- 新兴系统开始采用 Token 认证，常见于移动端API。  
  
- 检查方式：  
  
- 获取 JWT Token（通常在 Authorization 头）  
  
- 使用 jwt.io 解码，查看是否使用 none  
 算法或弱密钥  
  
- 若算法为 HS256  
 但密钥简单，可用 hashcat  
 破解：  
  
```
hashcat -m 16500 jwt_token.txt /usr/share/wordlists/rockyou.txt
```  
###   
### 三、专项突破策略  
#### 1. 教务系统专项（以正方为例）  
- 默认路径：/jwglxt/xtgl/login_sso.html  
  
- 常见漏洞：  
  
- 弱口令 + 无验证码 → 可批量爆破  
  
- 存在 getCaptcha  
 接口但未绑定session → 可绕过验证码  
  
- 参数 yh_id  
 控制用户ID → 存在越权风险  
  
- 版本指纹：  
  
- 查看登录页源码中的版本号或JS路径，判断是否为已知存在漏洞的旧版本（如 V5.0.1）  
  
#### 2. 在线考试系统  
- 关键风险：  
  
- 时间控制不当：前端控制倒计时 → 可通过修改本地时间跳过  
  
- 题目预加载：一次拉取所有题目 → 可提前查看答案  
  
- 提交结果可控：答题结果由客户端组装 → 可构造满分包重放  
  
- 抓包分析重点：  
  
- startExam  
 → submitExam  
  
- 检查是否有签名机制，若无则极易被篡改  
  
#### 3. 校园统一认证中心（CAS）  
- 地址通常为：/cas/login  
  
- 攻击面：  
  
- 四次握手流程中 ticket 泄露  
  
- Service 参数开放重定向  
  
- TGT Cookie 未设置 HttpOnly → XSS 可盗取  
  
- 可结合 XSS 实现会话劫持，进而冒充任意用户登录各子系统。  
  
感兴趣的师傅可以公众号私聊我  
进团队交流群，  
咨询问题，hvv简历投递，nisp和cisp考证都可以联系我  
  
**内部src培训视频，内部知识圈，可私聊领取优惠券，加入链接：https://wiki.freebuf.com/societyDetail?society_id=184**  
  
**安全渗透感知大家族**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmSjWVDEgnF58XicK2yPwMvN5cgJaBgibCwqHeyC0ZCJuLQibEMTalo4zGyw/640?wx_fmt=png&from=appmsg "")  
  
（新人优惠券折扣  
30.0  
￥，扫码即可领取更多优惠）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRrCWNeecQIlIAUPicvEicpmSkmjmCXibbX7zh3NLNgRBbuLbheIudvOPdxnpuyt81TSiaVgWogJHrsWg/640?wx_fmt=png&from=appmsg "")  
  
内部交流群  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EXTCGqBpVJSiao22HdM7F7OBu4zNJicKjkpxDWia5shmzQH4UialWGUCsoWYMHVpcEtUxF7RsfJaHKl9gsVWEjqAuw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=16 "")  
  
****  
**加入团队、加入公开群等都可联系微信：yukikhq，搜索添加即可**  
  
****  
END  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=7 "")  
  
**往期回顾**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=8 "")  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=9 "")  
  
[实战SRC-漏洞挖掘之XSS案例](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247488557&idx=1&sn=c0fde2a563e2e3df0f90eb7df494dea4&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=10 "")  
  
                    [海外SRC挖掘-业务逻辑漏洞案例分享](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247488515&idx=1&sn=6e33530abdd437c4fd7e0b4d7435105c&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=11 "")  
  
[FOFA API 驱动的团队资产发现工具 - Cloud Server](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247487707&idx=1&sn=66c094a3b3d359f9d6beded7a909347b&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=12 "")  
  
[闪紫 - AI赋能社工字典生成工具，自动联想关联变体](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247488623&idx=1&sn=1947cb0ef9ccd230c3e04c698afd290e&scene=21#wechat_redirect)  
  
  
  
  
  
