#  pac4j-jwt 身份验证绕过漏洞  
原创 🅼🅰🆈
                    🅼🅰🆈  独眼情报   2026-03-11 06:11  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAj8LyWib3pnneTEQ5ns1Zf0Ab7eSiaTq9wtNdibwOF8Lev21icc5E9u3kYczSzF4EJAmZQFEMxlh8k7S2jL7sYKk4rsIX2eQuIDFfk/640?wx_fmt=png&from=appmsg "")  
  
想象一下：你家门口有一个投递箱，任何人都可以往里塞东西，但只有你拿着私钥才能打开取出来。正常情况下，你取出信件后还需要核对里面是否盖有官方印章，才算确认这封信是可信的。但这次漏洞的问题在于——服务器成功打开了投递箱，却忘了核对印章，直接就相信了里面写的内容。攻击者只需要找到那个公开的投递箱入口，就能塞进一张写着「我是管理员」的纸条，服务器照单全收。  
  
2026年3月3日，安全研究团队 CodeAnt AI 披露了一个 CVSS 满分 10.0 的严重漏洞，编号为 CVE-2026-29000，影响 Java 生态中被广泛使用的认证库 pac4j-jwt。攻击者只需持有服务器的 RSA 公钥，便可伪造任意用户身份——包括管理员账户——完成完整的身份验证绕过，无需知道任何私钥或密码。  
## pac4j 和 JWT 是什么？  
  
要理解这个漏洞，先得搞清楚几个概念。  
  
**pac4j**  
 是 Java 生态中一个老牌的通用安全框架，被大量企业级应用、API 网关和 SSO 系统所集成，负责处理用户登录与权限校验。  
  
**JWT**  
 是一种常见的身份令牌格式。当你登录某个网站后，服务器会生成一个令牌发给你，之后你每次请求都带上它，服务器就能知道你是谁、有什么权限。  
  
JWT 有两个核心安全机制：  
- **加密**  
：把令牌内容加密，中间人无法偷看，对应格式叫 JWE。  
  
- **签名**  
：证明令牌是由持有私钥的服务器颁发的，对应格式叫 JWS。  
  
这两层机制各司其职——加密保护数据的机密性，签名保护数据的真实性。单纯能解密一个令牌，并不等于证明令牌是合法颁发的。而这次漏洞，恰恰就发生在这个关键区别上。  
## 漏洞的根源：一个「空值判断」悄悄架空了签名验证  
  
漏洞出在 JwtAuthenticator 组件处理加密令牌时的逻辑缺陷：当服务器解密 JWE 令牌后，会尝试将内层载荷解析为一个带签名的 JWT 对象。如果内层实际上是一个无签名的 PlainJWT，解析结果就是空值，而后续的签名校验判断正好依赖这个空值——一旦为空，签名验证就被完全跳过，服务器却继续用令牌中的声明字段构建用户身份。  
  
用更通俗的话来说：服务器成功解密了攻击者发来的内容，便错误地将「能解密」等同于「可信任」。但问题在于，任何人都可以用公钥加密数据——这正是公钥设计的初衷。服务器漏掉的那一步，是检验「这个令牌究竟是谁签发的」。  
  
这个 bug 的本质是**逻辑组合错误**  
：每一段代码单独来看都没有问题，但当「解密成功」和「签名验证」两个步骤被串联时，中间的条件判断出现了漏洞。  
## 影响范围：哪些系统受到威胁？  
  
凡是同时满足以下条件的部署，均处于危险中：使用了 RSA 加密配置、同时配置了加密和签名两层机制、通过 JwtAuthenticator 进行身份校验。  
  
受影响版本包括：  
- **4.x 系列**  
：4.5.9 以下所有版本  
  
- **5.x 系列**  
：5.7.9 以下所有版本  
  
- **6.x 系列**  
：6.3.3 以下所有版本  
  
如果 pac4j 被用于 API 网关或单点登录集成节点，影响范围会进一步扩大——伪造的身份可能会被下游系统完全信任，造成整个内网的信任链崩塌。这与当年 Log4Shell 的扩散模式非常相似：一个被广泛内嵌的组件一旦出问题，影响面会呈指数级放大。  
  
值得关注的是，这并非 pac4j 生态首次出现类似问题。更早的 CVE-2021-44878 同样涉及令牌算法校验漏洞，当时客户端可以通过「none」算法绕过 OpenID Connect 令牌校验。两次漏洞的根因惊人地相似：攻击者找到了一条让验证器跳过真实性证明的路径。  
## 如何应对？  
  
**立即升级**  
是唯一有效的修复手段：  
  
<table><thead><tr><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;font-weight: bold;background: none left top / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;text-align: center;"><section><span leaf="">版本系列</span></section></th><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;font-weight: bold;background: none left top / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;text-align: center;"><section><span leaf="">升级目标</span></section></th></tr></thead><tbody><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">4.x</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">4.5.9 或更高</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(248, 248, 248);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">5.x</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">5.7.9 或更高</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">6.x</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: center;"><section><span leaf="">6.3.3 或更高</span></section></td></tr></tbody></table>  
  
如果暂时无法升级，应临时限制接受加密令牌的接口访问，并对日志中出现的无签名令牌请求保持警惕。  
  
在更宏观的层面，这次漏洞提醒所有开发团队：「解密成功」不等于「身份可信」。加密只是令牌系统的一半——另一半是确认令牌是由谁创建、经过谁授权的。两者缺一不可。  
>   
> 详细技术分析：https://www.codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key  
  
  
  
