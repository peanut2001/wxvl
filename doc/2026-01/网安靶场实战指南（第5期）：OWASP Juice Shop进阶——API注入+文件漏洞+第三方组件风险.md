#  网安靶场实战指南（第5期）：OWASP Juice Shop进阶——API注入+文件漏洞+第三方组件风险  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-30 02:55  
  
上一期我们搞定了OWASP Juice Shop的基础业务漏洞，熟悉了前后端分离架构下的漏洞挖掘思路。但这个靶场的核心价值，远不止基础业务逻辑漏洞——它还隐藏了API接口型SQL注入、文件读取/上传漏洞，以及真实场景中高频爆发的第三方组件漏洞（npm依赖风险）。  
  
这一期我们聚焦Juice Shop的进阶漏洞，拆解“API注入绕过、文件类漏洞利用、第三方组件风险挖掘”的核心技巧，同时强化“多漏洞组合利用”思维，帮你适配更复杂的实战渗透场景。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralYLyC1oCXATWa90WEyEpNnTFnJ4blYUdnSK5OIpGz8dBux22uXPttehLU8qbnqj7Bn6c0cznUUXrQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
## 一、API接口型SQL注入：前后端分离下的注入新姿势  
  
和DVWA的传统URL参数注入不同，Juice Shop的SQL注入隐藏在API接口的JSON参数中，后端接收JSON格式数据并拼接SQL语句，属于“参数型注入”，绕过逻辑更贴近真实接口场景。  
### 漏洞场景与防护逻辑  
- 漏洞位置：用户登录接口（POST /api/Login  
）、商品搜索接口（GET /api/Products?search=  
）；  
  
- 防护特点：前端无过滤，后端对部分特殊字符做了转义，但未覆盖所有注入场景；  
  
- 核心难点：JSON参数中注入需注意语法格式，避免破坏JSON结构导致请求失败。  
  
### 实战1：登录接口SQL注入（布尔盲注）  
#### 利用步骤：  
1. 前端操作：进入登录页面，输入任意账号密码（如test@123.com  
/123456  
），用Burp Suite抓包；  
  
1. 分析请求：登录接口为POST /api/Login  
，请求体为{"email":"test@123.com","password":"123456"}  
；  
  
1. 构造注入Payload：利用布尔盲注逻辑，在email参数后拼接注入语句，同时保持JSON格式正确：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKpibFgiazGbXP6v9P81yEN9JFa3FYcIUJGmNgVe1ZjNoPtS86ZnOibrLYNw/640?wx_fmt=png&from=appmsg "")  
  
注：--   
（双横杠+空格）注释后续语句，避免破坏SQL语法，同时JSON中需用双引号包裹内容，单引号作为注入分隔符。  
  
1. 验证结果：发送请求后，页面返回“登录成功”（即使账号密码错误），说明注入生效，成功绕过登录验证；  
  
1. 深化利用：猜解管理员账号，构造Payload：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKpEkQSqIsRRVsKDdWZvg1TFPmWStjMGD659uIdlNXPvbdd0dibFgmtvpQ/640?wx_fmt=png&from=appmsg "")  
  
### 实战2：商品搜索接口注入（报错注入）  
#### 利用步骤：  
1. 前端操作：在首页搜索框输入关键词（如apple  
），抓包获取搜索接口GET /api/Products?search=apple  
；  
  
1. 构造报错注入Payload：在search参数后拼接报错语句，利用数据库报错返回敏感信息：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKpbVbWx3ZF8ib82bPZBqWEBCM1tI8BK2jo7icVOycMW8kTOqxyfcn7s2Wg/640?wx_fmt=png&from=appmsg "")  
  
1. 验证结果：发送请求后，后端返回数据库报错信息，包含当前数据库名（juiceshop  
），确认注入点存在；  
  
1. 延伸利用：通过报错注入可进一步猜解表名、字段名，最终获取管理员账号密码。  
  
### 绕过技巧：特殊字符编码  
  
若后端过滤了单引号，可将单引号URL编码为%27  
，注入Payload变为：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKp98nm72UsHAiaRLwUshAicR9QicUXHpbIXuldicsSESt4XykpibDAVAPbCPQ/640?wx_fmt=png&from=appmsg "")  
  
后端接收后会自动解码，注入语句正常执行。  
## 二、文件类漏洞：读取敏感文件+上传突破  
  
Juice Shop的文件漏洞虽不明显，但贴合真实业务场景——包含文件读取（敏感配置泄露）和文件上传（头像上传功能隐藏漏洞），需结合API接口特性挖掘。  
### 1. 文件读取漏洞：利用API接口读取配置文件  
#### 漏洞本质：商品图片加载接口未校验文件路径，允许目录遍历+文件读取。  
#### 实战步骤：  
1. 前端操作：进入商品详情页，任意点击一张商品图片，抓包获取图片加载接口：GET /api/Images/products/1.jpg  
；  
  
1. 构造目录遍历Payload：修改图片路径，读取后端敏感配置文件：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKp81uaianF6M732qia2twycrZ4M6pYetWKEgIxVMgggYmVOqJpB2aEHKSQ/640?wx_fmt=png&from=appmsg "")  
  
注：../  
表示向上跳转一级目录，多次跳转可突破当前目录限制，读取服务器根目录下的文件。  
  
1. 验证结果：发送请求后，后端返回secrets.json  
文件内容，包含数据库账号密码、API密钥等敏感信息：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKpIEjOSU7fDAPD2gPjomgqHriaCdM0LaYCiaAuPczYwrobdpI5pO2HFkRA/640?wx_fmt=png&from=appmsg "")  
  
1. 延伸利用：读取其他敏感文件，如/etc/passwd  
（Linux系统用户信息）、/api/Images/products/../../../../package.json  
（项目依赖信息）。  
  
### 2. 头像上传漏洞：隐藏接口突破限制  
#### 漏洞场景：用户个人中心的头像上传功能，前端限制只能上传图片，但后端校验存在缺陷。  
#### 实战步骤：  
1. 前端操作：登录账号，进入个人中心（Profile  
），点击头像上传按钮，选择一张.jpg图片抓包；  
  
1. 分析请求：上传接口为POST /api/Users/avatar  
，请求体为multipart/form-data格式，包含文件内容和文件名；  
  
1. 构造恶意文件：创建包含PHP一句话木马的文件，命名为shell.php.jpg  
，在文件头部添加图片标识（FFD8FF  
，JPG文件头部），伪装为图片；  
  
1. 篡改参数：用Burp Suite修改文件名和文件内容，将Content-Type  
改为image/jpeg  
，发送请求；  
  
1. 验证与利用：上传成功后，通过文件读取漏洞获取上传路径（如/api/Images/avatars/shell.php.jpg  
），由于后端未严格校验文件内容，部分服务器会解析该文件为PHP，用蚁剑连接即可控制服务器。  
  
## 三、第三方组件漏洞：npm依赖风险挖掘  
  
现代Web应用大量依赖第三方npm包，Juice Shop模拟了“依赖包存在漏洞导致的安全风险”，这是真实企业场景中高频爆发的安全问题（如Log4j、Struts2漏洞）。  
### 实战：利用lodash漏洞触发命令执行  
#### 步骤1：确认依赖包版本  
  
读取项目package.json  
文件（通过文件读取漏洞），发现lodash  
版本为4.17.20  
（存在漏洞的版本）；  
#### 步骤2：构造Payload  
  
通过商品评价接口（存储型XSS）注入触发lodash漏洞的脚本：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuorala8Vx4zibvsR4aZ3X8yI7WKpzq41walBbhqdLZGC5po1ATY5iaNaQ0rLaMMePibmu6q2xOke691icSDzQ/640?wx_fmt=png&from=appmsg "")  
#### 步骤3：触发漏洞  
  
提交评价后，刷新页面，脚本执行whoami  
命令，获取服务器当前用户身份；若服务器开启了相应权限，可进一步执行ls  
、cat  
等命令，读取敏感文件。  
### 防御建议：  
1. 定期更新依赖包：使用npm audit  
命令检测依赖包漏洞，及时更新到安全版本；  
  
1. 限制依赖包权限：禁止第三方包调用child_process  
等危险模块，减少漏洞危害；  
  
1. 引入依赖审计工具：在项目构建阶段自动检测依赖包漏洞，提前规避风险。  
  
## 四、多漏洞组合利用：从信息泄露到权限控制  
  
真实渗透中，单一漏洞难以获取高权限，需组合多个漏洞形成攻击链，这里以“文件读取+SQL注入+越权”为例，演示完整攻击流程：  
### 组合流程：  
1. 文件读取漏洞：读取secrets.json  
获取数据库账号密码（root  
/juiceShopPass  
）；  
  
1. SQL注入：通过登录接口注入，登录管理员账号，获取管理员Token；  
  
1. 权限越权：使用管理员Token访问/api/Admin  
接口，篡改其他用户角色（将普通用户改为管理员）；  
  
1. 控制平台：通过管理员权限修改网站配置，植入恶意脚本，实现对整个靶场平台的控制。  
  
### 核心思维：  
  
每个漏洞都是“信息节点”——文件读取获取基础配置，SQL注入突破身份验证，越权扩大攻击范围，组合起来才能实现从“单点漏洞”到“全面控制”的突破。  
## 五、漏洞修复建议（企业级标准）  
1. API注入防护：使用参数化查询（Prepared Statement），避免SQL语句拼接；对JSON参数中的特殊字符进行全面过滤（单引号、双引号、分号等）；  
  
1. 文件漏洞防护：限制文件读取路径（禁止目录遍历），采用白名单机制校验文件上传的后缀、内容、大小；将上传文件存储到非Web访问目录；  
  
1. 第三方组件防护：建立依赖包审计机制，定期扫描漏洞；优先选用官方维护、更新频繁的依赖包；对危险模块进行权限限制；  
  
1. 权限加固：所有接口添加“身份校验+权限校验”，管理员接口单独做访问控制；敏感操作（如角色修改）添加二次验证。  
  
## 六、互动与下期预告  
  
Juice Shop的进阶漏洞完美还原了现代Web应用的安全风险，尤其是第三方组件漏洞，在真实企业渗透中占比极高。你在挖掘时是否遇到了依赖包漏洞难以触发的问题？或者有更巧妙的组合利用思路？评论区分享你的实战经验~  
  
下一期我们将结束OWASP Juice Shop的实战，转向VulnHub靶场（Web类镜像），聚焦“外网突破→内网渗透”的完整流程，教你从Web漏洞getshell，再通过Linux权限提升、横向移动扩大战果，关注不迷路！  
  
点击文末  
阅读原文  
领取200节攻防教程  
  
  
