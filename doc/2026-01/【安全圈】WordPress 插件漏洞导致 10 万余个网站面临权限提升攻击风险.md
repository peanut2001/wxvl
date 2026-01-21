#  【安全圈】WordPress 插件漏洞导致 10 万余个网站面临权限提升攻击风险  
 安全圈   2026-01-21 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
一项严重的安全漏洞出现在广受欢迎的 **Advanced Custom Fields: Extended**  
 WordPress 插件中，已使 **10 万多个网站**  
 面临被完全接管的风险。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgNvQhMlVoJLediaAJpSuzSk3ztPZanePhic2qVptT7yicibiasQWIh6OCXwnkOsImXbm3cACyMpcDpExw/640?wx_fmt=png&from=appmsg "")  
  
该漏洞编号为 **CVE-2025-14533**  
，影响插件 **0.9.2.1 及之前版本**  
，CVSS 评分高达 **9.8（严重）**  
。  
  
如果未及时修补，未认证的攻击者可以利用用户注册表单中角色处理机制的缺陷，直接获得管理员级别权限。  
### 漏洞成因  
  
该问题源于插件通过自定义表单创建用户的实现方式。网站管理员可使用字段组构建注册或用户资料表单，收集用户名、邮箱、密码以及用户角色等信息。  
  
在正常情况下，新注册用户的角色应受到严格限制，通常只允许诸如“订阅者（subscriber）”等低权限角色。然而，在受影响的版本中，这一控制机制失效，为滥用打开了大门。  
  
Wordfence 分析人员发现，当表单中映射了角色字段时，插件的 insert_user 表单动作并未正确限制注册过程中可分配的角色。  
  
这意味着，攻击者可以提交一个精心构造的请求，即使前端界面限制了可选角色，也能在请求中将自己的角色设置为管理员。  
  
一旦请求被处理，系统就会创建一个拥有完整管理员权限的账户。获得管理权限后，攻击者即可**彻底控制**  
受影响的 WordPress 网站。  
### 潜在影响  
  
攻击者在取得管理员权限后，可以：  
- 上传带有后门的恶意插件或主题  
  
- 篡改网站内容，将访客重定向至钓鱼或恶意网站  
  
- 植入垃圾内容或 SEO 投毒代码  
  
- 创建额外的管理员账户以维持长期访问权限  
  
鉴于该插件安装量巨大，且在存在漏洞配置时利用门槛极低，只要网站将相关用户操作表单暴露在公网，就可能遭受严重影响。  
### 修复与风险现状  
  
在漏洞披露时，插件开发方已在 **0.9.2.2 版本**  
中发布修复补丁，安全厂商也在防火墙层面提供了针对利用行为的拦截措施。  
  
然而，那些**尚未更新插件、且仅依赖应用层防护**  
的网站，仍然是攻击者进行自动化扫描和入侵的理想目标。  
### 漏洞详情一览表  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">字段</span></span></section></th><th style="box-sizing: border-box;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">说明</span></span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">漏洞编号</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">CVE-2025-14533</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">插件名称</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">Advanced Custom Fields: Extended</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">插件标识</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">acf-extended</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">受影响版本</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">≤ 0.9.2.1</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">修复版本</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">0.9.2.2</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">漏洞类型</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">未认证权限提升</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">攻击向量</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">恶意用户注册表单提交</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">触发条件</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">存在映射了角色字段的公开表单</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">CVSS 评分</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">9.8（严重）</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">受影响安装量</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">10 万+ 活跃安装</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">发现者</span></span></section></td><td style="box-sizing: border-box;"><section><span leaf=""><span textstyle="" style="font-size: 17px;">andrea bocchetti（Wordfence 漏洞悬赏）</span></span></section></td></tr></tbody></table>### 权限提升是如何实现的？  
  
该漏洞的核心在于插件高度灵活的表单系统，其初衷是让站点管理员无需编写代码即可构建自定义的用户管理流程。  
  
在典型配置中，管理员会定义一个字段组，包含用户信息字段，并将其关联到“创建用户”或“更新用户”的表单动作。其中一个字段可以是角色选择器，表面上受到“允许用户角色（Allow User Role）”设置的限制。  
  
但在后台，当表单提交时，插件会在 acfe_module_form_action_user  
 类中调用 insert_user()  
 函数。该函数会收集所有提交的数据（包括角色字段），并直接传递给 WordPress 原生的 wp_insert_user()  
 函数。  
  
问题在于，在受影响版本中，插件并未在后端强制执行字段组中配置的角色限制。前端设置营造了安全假象，但后端逻辑并未遵守这些规则。  
  
因此，只要存在一个包含角色字段的公开表单，未认证攻击者就可以绕过可见的角色选项，在 HTTP 请求中自行指定角色（如 administrator）。由于插件未对该值进行校验或过滤，WordPress 会接受请求并创建一个拥有完整管理员权限的账户。  
  
整个过程**无需已有账号、社会工程学手段或密码猜测**  
，直接构成一条通向网站完全失陷的通道。  
  
一旦攻击者以管理员身份进入系统，便拥有与合法站点所有者相同的控制能力，可持续操纵和破坏网站。这使得 **CVE-2025-14533**  
 成为在特定配置存在时，导致 WordPress 网站被全面攻陷的高危漏洞。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】网络工程师李某以技术手段窃取赌博网站184万余名中国公民个人信息，警方已扣押其180余个比特币](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073800&idx=1&sn=2243bc4e8751be2209553741800e555d&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Linux 用户注意：Snap Store 爆发新型攻击，过期域名成黑客后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073800&idx=2&sn=4a017624a7c6c15eef19008560c122cd&scene=21#wechat_redirect)  
  
  
  
[【安全圈】密码管理器 Keepass 不兼容 1 月 Win11 更新，导致自动填充失效](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073800&idx=3&sn=75b7460e72bb4f2ede8a6b357fe3a0ec&scene=21#wechat_redirect)  
  
  
  
[【安全圈】苹果督促用户更新 iPhone 高危漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073786&idx=1&sn=651dca9c8e72b03014a22b79574bf873&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
  
  
