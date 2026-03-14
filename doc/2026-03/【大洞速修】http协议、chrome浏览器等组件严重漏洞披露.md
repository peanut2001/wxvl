#  【大洞速修】http协议、chrome浏览器等组件严重漏洞披露  
原创 小火炬
                    小火炬  小火炬sec   2026-03-14 11:35  
  
> 参考文献1  
  
> Feng Ning，公众号：AI-security-innora[位置被秒偷！10多亿人每天在用的国民支付应用，17个「正常功能」细思极恐！](https://mp.weixin.qq.com/s/xEBEYZlap3xuDMURuJd7_Q)  
  
  
  
> https://innora.ai/zfb/  
  
> 参考文献2  
  
  
  
一个链接，通向一切  
  
  
不负责任的披露时间线：  
  
我懒得遵循负责任的安全研究原则。在公开任何信息之前，没通过任何渠道向任何集团进行任何报告。  
  
2026.03.14 2:30  
  
发现安全问题  
  
  
2026.3.14 19:20  
  
懒得报送产商，详情面向公众公开  
  
  
已验证安全问题  
  
  
CRITICAL  
V-01  
  
谷歌浏览器rce漏洞：  
  
通过  
  
location.href='https://chromewebstore.google.com/detail/bookmarks-quick-search/[插件id]' 允许外部页面打开谷歌浏览器插件安装界面， 虽然最后安装仍然需要用户手动确认，但配合 UI 欺骗（V-08）和社会工程，用户误操作的风险极高。  
```
<script>location.href='https://chromewebstore.google.com/detail/bookmarks-quick-search/[插件id]'</script>
```  
  
  
UNKONWNV-02至V-06  
  
没发现对应的，先留白，对齐一下格式  
  
  
  
HIGH  
V-07  
  
网络ip精确定位窃取（无用户感知）  
  
  
发现http协议向服务器回传用户ip，连接建立后回传时间<1ms，可以导致用户被精准定位  
  
  
  
HIGH  
V-08  
  
  
UI 欺骗: 虚假提示通知 + 标题篡改  
  
chrome浏览器可以使用  
iframe标签  
嵌入其他网站，同时可以通过JavaScript的alert函数弹窗告知用户比如“安装插件否则浏览器无法使用”，使用title标签修改标题为“fbi插件安装”等。  
  
  
  
HIGH  
V-09  
  
  
OAuth 授权流程劫持  
  
任意  
OAuth  
应用都可以被授权劫持，通过修改redirect_uri参数发起OAuth授权服务调用。  
虽然未成功获取授权码，但弹出了"redirect_uri错误，请联系管理员确认"弹窗，证明请求到达了 OAuth 服务端。  
  
  
  
HIGH  
V-10  
  
零交互暴露浏览器地址和历史记录  
  
  
通过chrome://伪协议打开chrome://settings/addresses，可以直接打开谷歌浏览器保存的地址页面，显示 美利坚合众国华盛顿特区宾夕法尼亚大道1600号 。chrome://history/ 页面暴露20+ 条浏览器历史记录，无需任何额外确认。  
  
  
