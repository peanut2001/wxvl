#  常见OAuth 漏洞：未验证token  
原创 Pwn1
                        Pwn1  漏洞集萃   2026-01-21 14:38  
  
   
  
> **免责声明**  
  
本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。  
  
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
1.    
  
1.    
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
  
   
  
   
  
   
  
<table><tbody><tr><td style="padding:20px;background:#fdfdfd;border:1px solid #e8e8e8;border-radius:14px;font-size:15px;background-image: repeating-linear-gradient(45deg, #fafafa, #fafafa 8px, #f5f5f5 8px, #f5f5f5 16px);"><p><span leaf="">原文链接</span></p><section><span leaf="">          </span><span leaf="">https://brbr0s.medium.com/broken-oauth-linking-94308b7d423e</span></section></td></tr></tbody></table>  
  
   
  
目标网站存在一个 **OAuth 链接功能**  
，目标网站主要功能包括采购和运输流程。  
  
在针对目标搜集信息的时候发现其具有连接到 **Facebook**  
 这一功能；该功能主要是将用户的帐户与提供的 **Facebook**  
 帐户关联，使用户无需输入 email:passwor  
。  
  
随后运行该功能并且使用 **Burp**  
 抓包，发现了请求如下：  
```
{"facebookId":"122109215XXXXXXXXX","shortTermAccessToken":"access_token"}
```  
  
这是 OAuth 机制的一种，通过将用户的 **Facebook**  
 个人资料与用户在另一个应用程序上的帐户关联起来的方式。该应用程序会向 **Facebook**  
 请求用户的唯一 facebookId  
 和一个特殊的临时短期 shortTermAccessToken  
。  
  
这些信息构成 key:token  
 对，用于验证用户的身份，从而允许应用程序连接到用户的 **Facebook**  
 个人资料。  
  
而这个 facebookId  
 是**公开**  
的，并且在各种 **Facebook**  
 集成平台上都很常见，因此相对容易获取。  
  
通过分析流量发现中间可能没有对 shortTermAccessToken  
 进行验证之后，尝试修改 shortTermAccessToken  
：  
```
{"facebookId":"122109215XXXXXXXXX","shortTermAccessToken":"dummy"}
```  
  
再次发送修改后的请求发现响应 **200**  
。  
  
即该应用程序**根本没有**  
将 shortTermAccessToken  
 令牌与提供的 facebookId  
 进行验证。  
  
这个漏洞就类似于 **只使用受害者的电子邮件地址就能登录网站，而无需密码**  
。  
  
这意味着可以利用受害者的 **Facebook**facebookId  
 帐户与攻击者自己的帐户关联起来，当受害者尝试使用“**使用 Facebook 登录**  
”登录时，其将被登录到**攻击者控制的帐户**  
。  
  
通过再次创建一个新的账号按照上述提到的再次操作：  
```
{"facebookId":"122107214XXXXXXXXX","shortTermAccessToken":"dummy"}
```  
  
响应如下：  
```
200 OK
```  
  
随机发现，即使 **Facebook**  
 帐户已经与其他用户帐户关联，执行此操作后，该网站也会将受害者的 **Facebook**  
 帐户与其帐户**解除关联**  
，并将其与攻击者的帐户**关联**  
（最新创建的的一个平台用户）。  
# 重现步骤：  
1. 攻击者使用邮箱/密码创建一个普通账户。  
  
1. 攻击者拦截了 **Facebook**  
 链接请求。  
  
1. 将 facebookId  
 替换为已知的受害者 ID（该 ID 已公开）。  
  
1. 发送带有 payload  
 的请求。  
  
1. **Facebook ID**  
 与受害者的原始帐户解除关联，并绑定到攻击者的帐户。  
  
1. 受害者通过 **Facebook**  
 正常登录 -> 却被**重定向到攻击者的账户**  
。  
  
# 影响  
  
当受害者像往常一样使用 **Facebook OAuth**  
 登录时，他们实际上登录的是攻击者的帐户，因为该 **Facebook ID**  
 现在已与攻击者的帐户关联。  
- 攻击者可以预先填写其账户信息，例如：**他们自己的收货地址**  
。  
  
- 受害者执行的任何操作（例如**下单**  
或**添加银行信息**  
）都会保存到攻击者的帐户中，而不是他们自己的帐户中。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOJJGrWlfxNDDD9Vo75r6XcV1W4iaRYlq75reMgTcrgQwdmx6QAw95aaibSfLJ2MzhN1icH1IrQvicNP6w/640?wx_fmt=png&from=appmsg "")  
  
  
  
   
  
   
  
  
觉得本文内容对您有启发或帮助？  
  
点个**关注➕**  
，获取更多深度分析与前沿资讯！  
  
  
👉 往期精选  
  
[信息收集最强OSINT姿势：Google一搜，全球程序员的密码、API Key、邮箱全裸奔](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484686&idx=1&sn=1f2d389d33dcfea473656e96ceb7a0ea&scene=21#wechat_redirect)  
  
  
[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)  
  
  
[【漏洞挖掘Tips】关于头像上传存储在s3的漏洞挖掘方法](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484415&idx=1&sn=147dee8beef8b2411b98e2fc7e6da691&scene=21#wechat_redirect)  
  
  
  
