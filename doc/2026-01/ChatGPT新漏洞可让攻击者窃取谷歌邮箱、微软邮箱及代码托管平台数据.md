#  ChatGPT新漏洞可让攻击者窃取谷歌邮箱、微软邮箱及代码托管平台数据  
 天黑说嘿话   2026-01-29 01:42  
  
作者：古鲁・巴兰. 发布时间：2026 年1 月8 日  
  
写在前面：这是三篇文章的合集，先看到第一篇报道，然后又把相应的漏洞攻击细节找到放在了一起。这样就能对这两个漏洞的有更全面的了解。  
  
  
ChatGPT新漏洞可让攻击者窃取谷歌邮箱、微软邮箱及代码托管平台数据  
  
ChatGPT  
存在的高危漏洞，可使攻击者在无需用户交互操作的情况下，从谷歌邮箱（  
Gmail  
）、微软邮箱（  
Outlook  
）、代码托管平台（  
GitHub  
）等互联服务中窃取敏感数据。  
  
命名为  
“  
影子泄露  
”  
（  
ShadowLeak  
）和  
“  
僵尸代理  
”  
（  
ZombieAgent  
）的漏洞，会利用该人工智能的连接器  
（  
Connectors  
）和记忆  
（  
Memory  
）功能，发起零点击攻击、实现持续入侵，甚至进行攻击扩散。  
  
OpenAI  
推出的连接器功能，能让  
ChatGPT  
仅需几次点击，就能与谷歌邮箱、  
Jira  
、代码托管平台（  
GitHub  
）、微软团队协作软件（  
Teams  
）以及谷歌网盘（  
Google Drive  
）等外部系统实现集成。  
  
而默认开启的记忆功能，会存储用户的对话内容与相关数据，以此生成个性化回复，同时支持人工智能对存储条目进行读取、编辑或删除操作。  
  
尽管这两项功能提升了工具的实用性，但也使其获得了访问个人及企业数据的大量权限，因防护措施不到位而加剧了数据泄露风险。  
  
攻击者会发送恶意电子邮件，或分享植入隐藏指令的文件。这些指令会通过白色文本、极小字号或页脚等形式隐藏，使用户无法察觉。  
  
在零点击服务端攻击  
模式下，  
ChatGPT  
会在执行邮件总结等常规任务时扫描收件箱，自动运行恶意程序，在用户尚未察觉之际，通过  
OpenAI  
的服务器窃取数据。  
  
一次点击攻击  
模式则会在受害者上传恶意文件时触发，进而能够对互联的代码仓库或云端网盘发起连环攻击。  
<table><tbody><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击类型</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">触发条件</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">数据窃取方式</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">影响范围</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">零点击服务端攻击</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">分享恶意文件</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">通过开放式人工智能服务器上的</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">browser.open()</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">工具</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">谷歌邮箱收件箱、个人身份信息</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">一次点击服务端攻击</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">通过文件篡改记忆数据</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">利用文档中的隐藏指令</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">谷歌云端硬盘、代码托管平台</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">持续入侵（僵尸代理）</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">通过文件篡改记忆数据</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">每次用户发起查询时持续泄露数据</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">所有对话记录、医疗数据</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击扩散</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">窃取电子邮箱地址</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">自动转发内容至联系人邮箱</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">向企业内部扩散</span></span><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="130" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击类型</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="138" width="100"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">触发条件</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="153" width="149"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">数据窃取方式</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td><td data-colwidth="118" width="102"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">影响范围</span></span></b><span lang="EN-US" style="font-family: Arial, sans-serif;color: rgb(31, 35, 41);"><o:p></o:p></span></p></td></tr></tbody></table>  
OpenAI  
曾阻止了动态修改  
URL  
的操作，但研究人员通过为每个字符（字母  
a-z  
、数字  
0-9  
、  
$  
代表空格）预设对应  
URL  
，成功绕过了这一限制。  
  
ChatGPT  
会将  
“  
Zvika Doe  
”  
这类敏感字符串标准化处理为  
“zvikadoe”  
，随后依次访问  
compliance.hr-service.net/get-public-joke/{param}  
这类固定链接，无需拼接网址即可实现数据窃取。这种服务端攻击方式能够绕过客户端防护、浏览器以及用户界面的审查。  
  
为实现持续入侵，攻击者会通过文件植入篡改记忆的规则：模型会在处理每一条消息前，优先读取指定的攻击者邮件，并执行数据泄露操作。  
  
尽管  
OpenAI  
明令禁止同时启用连接器与记忆功能，但攻击者可通过反向访问的方式规避限制，即使用户开启新的对话，也能实现持续的数据窃取。而攻击扩散的原理是，模型扫描用户收件箱获取联系人邮箱地址并泄露，攻击者的服务器再自动向这些邮箱发送恶意程序，从而实现对企业的定向渗透。  
  
Radware  
公司于  
2025  
年  
9  
月  
26  
日通过漏洞众测平台（  
BugCrowd  
）向  
OpenAI  
报告了上述问题，并提供了漏洞详情与修复方案建议。  
OpenAI  
复现全部漏洞后，已于  
2025  
年  
9  
月  
3  
日修复了  
“  
影子泄露  
”   
漏洞，于同年  
12  
月  
16  
日完成了所有漏洞的修复工作。  
  
专家提醒，由于智能体人工智能仍存在诸多安全盲区，用户需持续监控智能体的运行行为，并对输入内容进行安全过滤。  
  
影子泄露  
”  
（  
ShadowLeak）  
  
Radware  
公司声明，  
ChatGPT  
的深度研究智能体（  
Deep Research agent  
）存在一项安全漏洞，攻击者只需发送一封精心构造的电子邮件，就能操控该智能体泄露用户  
Gmail  
收件箱中的敏感数据。  
  
深度研究模式是  
OpenAI  
于  
2025  
年  
2  
月推出的自主研究功能，该公承诺：  
“  
你只需输入指令，  
ChatGPT  
就能检索、分析并整合数百个网络信息源，生成一份达到专业研究员水准的详尽报告。  
”  
  
现在，假设你希望借助**深度研究功能**  
，基于  
Gmail  
中的邮件内容和网络信息源生成一份报告。在这种情况下，用户需要授权该智能体访问自己的  
Gmail  
邮箱与网络搜索功能。  
  
向深度研究功能发送的常规指令可能如下：  
  
“  
深度分析我今天收到的邮件  
……   
汇总所有与  
……   
相关的内容  
”  
  
接下来我们将说明：在这种使用场景下，攻击者能够诱导该智能体，在用户完全不知情且未获授权的情况下，将其邮箱中的敏感信息窃取至攻击者控制的服务器。  
  
2025  
年  
9  
月  
18  
日，  
Radware  
公司的三名研究人员公布了一项新发现：当深度研究功能与  
Gmail  
相连，且用户要求从网络获取信息源时，该功能存在零点击漏洞  
。  
  
研究人员将此漏洞命名为  
“  
影子泄露  
”  
（  
ShadowLeak  
），它支持服务端数据窃取  
，即成功的攻击链路可直接从  
OpenAI  
的云基础设施中泄露数据，完全规避本地或企业级防护系统的检测。  
  
该攻击采用间接提示注入技术  
，通过白底白字、极小字号等方式，在电子邮件的  
HTML  
代码中嵌入隐藏指令。用户对此毫无察觉，但深度研究智能体却会执行这些指令。  
  
与此前的客户端数据窃取攻击（如  
AgentFlayer  
和  
EchoLeak  
）不同，那些攻击依赖智能体在用户界面中渲染攻击者控制的内容，而  
“  
影子泄露  
”  
的服务端泄露完全在  
OpenAI  
的云端完成。  
  
智能体的自主浏览工具无需客户端参与即可执行数据窃取操作，其利用后端执行逻辑而非前端渲染机制，大幅扩大了攻击面。  
  
1. 影子泄露攻击链路解析  
  
以下是攻击者试图窃取受害者个人身份信息（  
PII  
）时，一次成功的  
“  
影子泄露  
”  
攻击完整链路拆解：  
  
（1）攻击者向目标发送一封看似无害的电子邮件，邮件中暗藏指令，要求智能体在收件箱中查找受害者的全名与住址，并打开一个  
“  
公共员工查询  
URL”  
，同时将上述信息作为参数附加到链接中，而该  
URL  
实际指向攻击者控制的服务器；  
  
（2）受害者向深度研究智能体下达指令，要求其处理邮件信息并完成相关任务，却未察觉其中一封邮件包含隐藏指令，且智能体可能会执行这些指令；  
  
（3）深度研究智能体处理这封恶意邮件，主动访问攻击者的域名，并按照指令将受害者的个人身份信息注入到  
URL  
中，整个过程无需用户确认，也不会在用户界面中留下任何渲染痕迹。  
  
Radware  
的研究人员表示，为了构造出能触发深度研究智能体、并让其将个人身份信息注入恶意  
URL  
的邮件，他们经历了漫长的反复试验与多次迭代。  
  
例如，他们必须将恶意请求伪装成合法的用户指令，强制深度研究智能体使用特定工具（如支持直接发起  
HTTP   
请求的  
browser.open()  
函数），指令智能体  
“  
多次重试  
”  
，并要求智能体先将提取到的个人身份信息进行  
Base64  
编码，再附加到  
URL  
中。  
  
当所有这些技巧部署到位后，研究人员利用  
“  
影子泄露  
”   
技术窃取  
Gmail  
数据的成功率达到了  
100%  
。  
  
![The full end-to-end flow of the attack](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qco8URNVIcG6E5xbriaBo8KJu86oBzeWuAKuQ44bea7kmrfLEiakicJicGibetqk20SoowqvIiarGYsdL1ngyV17rtNA/640?wx_fmt=jpeg&from=appmsg "")  
  
资料来源  
：Radware公司《影子泄露攻击端到端完整流程》  
  
2.   
  
服务端  
AI Agent  
威胁的缓解措施  
  
Radware  
公司指出，企业可通过一项措施部分降低风险：在智能体处理邮件之前，对邮件进行安全过滤，移除隐藏的  
CSS  
、混淆文本以及恶意  
HTML  
。但该公司同时强调，这种措施对于操纵智能体本身的攻击，防护效果十分有限。  
  
更有效的防御手段是实时行为监控  
：持续对比智能体的操作行为、推理意图与用户的原始指令是否一致。一旦检测到未经授权的数据窃取等异常偏离行为，可在操作执行前及时发现并拦截。  
  
Radware  
的研究人员已于  
2025  
年  
6  
月通过漏洞众测平台  
Bugcrowd   
向  
OpenAI  
报告了相关发现。  
2025  
年  
8  
月，  
Radware  
公司发现  
OpenAI  
已悄然修复该漏洞；同年  
9  
月初，  
OpenAI  
正式确认了这一漏洞，并将其标记为  
“  
已解决  
”  
  
  
僵尸代理  
”  
（  
ZombieAgent  
）介绍  
  
这种名为  
“  
僵尸代理  
”  
（  
ZombieAgent  
）  
”  
的全新攻击方法，由  
Radware  
公司的安全研究员兹维卡  
・  
巴博（  
Zvika Babo  
）发现。  
  
近期，  
OpenAI  
为  
ChatGPT  
新增了一系列面向用户的功能，推动其向智能体化方向转型，其中就包括  
“  
连接器  
”  
（  
Connectors  
）功能。该功能可让这款聊天机器人便捷、快速地对接各类主流外部系统，例如  
Gmail  
、  
Outlook  
、  
Google Drive  
、  
GitHub  
等，同时还赋予了  
ChatGPT  
联网浏览、打开链接、数据分析以及图像生成等能力。  
  
巴博在这份瑞得万报告中坦言，  
ChatGPT  
的此次智能体化转型，让工具本身  
“  
变得更实用、便捷且功能更强大  
”  
，但与此同时，也使其获得了访问用户敏感个人数据的权限。  
  
在  
Radware  
公司此前发布的一份报告中，巴博曾与两位同事发现，  
ChatGPT   
深度研究智能体（  
Deep Research agent  
）存在结构性漏洞。攻击者只需发送一封精心构造的电子邮件，就能操控该智能体，窃取用户  
Gmail  
收件箱中的敏感数据。  
  
研究人员将这一攻击手段命名为  
“  
影子泄露  
”  
（  
ShadowLeak  
）。该技术可实现服务端数据窃取，也就是说，一次成功的攻击链路能够直接从  
OpenAI  
的云基础设施中窃取数据，从而规避本地或企业级防护系统的监测。  
  
这种攻击利用**间接提示注入技术**  
，将隐藏指令植入电子邮件的  
HTML  
中，具体手段包括采用白字配白底的文字、极小字号等，这样一来，用户完全不会察觉，而深度研究智能体却会执行这些隐藏指令。这些指令通常会包含一个由攻击者控制的链接，并要求智能体将敏感数据以  
URL  
参数的形式附加到链接中，比如通过  
Markdown  
图像或browser.open()  
函数来实现。  
  
为防范此类攻击，  
OpenAI  
强化了护栏安全防护机制，禁止  
ChatGPT  
动态修改  
URL  
。巴博在最新报告中总结道：  
“  
如今，  
ChatGPT  
仅能打开与提供的链接完全一致的地址，即便收到明确指令，也不会为链接添加任何参数。  
”  
  
然而，该研究员很快又找到了一种能够彻底绕过这一防护措施的方法。  
## 1. 僵尸代理”（ZombieAgent）攻击原理  
  
这种攻击方式利用了  
OpenAI  
在URL修改  
防护机制上的缺陷，借助预先构建好的静态  
URL  
，逐个字符地窃取  
ChatGPT  
中的敏感数据。  
  
攻击者不会采用会触发  
OpenAI  
安全过滤系统的动态生成  
URL  
方式，而是提供一组固定的  
URL  
，每个  
URL  
对应一个特定字符，涵盖字母、数字以及空格  
token  
。随后，攻击者会向  
ChatGPT  
下达如下指令：  
  
（1）提取敏感数据（例如来自电子邮件、文档或内部系统的数据）；  
  
（2）对数据进行标准化处理（转换为小写格式，并用$  
等特殊符号替代空格）；  
  
（3）依次  
“  
打开  
”  
预先定义的  
URL  
，逐个字符地完成数据窃取；  
  
通过使用带索引的  
URL  
（例如用a0  
、a1  
……a9  
对应不同字符），攻击者能够确保窃取到的数据顺序准确无误。  
  
由于  
ChatGPT  
并未对  
URL  
进行任何构造操作，仅仅是严格按照指令打开提供的链接，因此这种攻击手段能够绕过  
OpenAI  
的  
URL  
重写和黑名单防护机制。  
  
2. 完整的攻击流程：  
  
（1）攻击者发送一封包含预构建  
URL  
和数据窃取指令的恶意电子邮件；  
  
（2）用户后续向  
ChatGPT  
下达与  
Gmail  
相关的操作指令；  
  
（3）ChatGPT在读取用户收件箱时，执行攻击者预先植入的指令，进而完成数据窃取；  
  
整个过程中，用户除了与  
ChatGPT  
进行常规对话外，无需进行任何其他操作  
  
![ChatGPT Vulnerabilities Expose Sensitive Data](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qco8URNVIcG6E5xbriaBo8KJu86oBzeWuPibqaNpmHnB60R0pvRj7Sy1gZCSpX9vR5vHUF7iaKB48iav1o83YkKxDw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**资料来源**  
：  
Radware  
公司报告《僵尸代理（  
ZombieAgent  
）：  
ChatGPT  
新漏洞致数据持续泄露并扩散》  
## 3. 僵尸代理攻击实现零点击与点击攻击  
  
巴博借助这种攻击技术，成功实现了两种提示注入的服务端攻击：一种是无需用户点击的零点击攻击，另一种则是仅需用户点击一次的攻击。  
  
巴博在报告中写道：  
“  
我们还演示了一种可实现持续入侵的方法，攻击者不仅能一次性窃取数据，还能实现持续性的数据泄露。一旦攻击者侵入聊天机器人，就能持续窃取用户与  
ChatGPT  
之间的每一段对话内容。  
”  
  
“  
此外，我们还演示了一种全新的攻击扩散技术，该技术能让攻击进一步蔓延，精准锁定特定受害者，并提高攻击触及更多目标的可能性。  
”  
  
Radware公司将于  
2026   
年  
1   
月  
20   
日举办一场线上研讨会，详细解析僵尸代理攻击的完整链路  
  
# ShadowLeak（影子泄露）与ZombieAgent（僵尸代理）攻击对比表  
<table><tbody><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">对比维度</span></span></b><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ShadowLeak</span></span></span></b><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">（影子泄露）</span></span></b><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><b><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ZombieAgent</span></span></span></b><b><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">（僵尸代理）</span></span></b><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">发现主体</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">瑞得万（</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">Radware</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">）的兹维卡</span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">・</span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">巴博及两位同事</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">瑞得万（</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">Radware</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">）的兹维卡</span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">・</span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">巴博</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">核心利用漏洞</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">深度研究智能体的结构性缺陷</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">OpenAI URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">动态修改防护机制的规避漏洞；结合</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">连接器与记忆功能的权限</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击原理</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">采用间接提示注入，将隐藏指令植入邮件</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">HTML</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">（白字白底、极小字号），触发后通过动态添加</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">参数的方式窃取数据</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">不动态生成</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">，而是预设与字符一一对应的静态</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">，指令</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">标准化敏感数据后，逐个字符打开链接完成窃取</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">数据窃取路径</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">服务端窃取，直接从</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">OpenAI </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">云基础设施泄露数据，规避本地</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">/ </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">企业防护</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">服务端窃取，通过顺序访问静态</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">传输数据，绕过</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">重写和黑名单防护</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">触发条件</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">发送精心构造的恶意邮件，</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">执行邮件总结等常规任务时触发</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">发送含预构建</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">和窃取指令的恶意邮件，用户向</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">下达</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">Gmail </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">相关任务时触发</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击类型</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">主要为</span></span><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">零点击服务端攻击</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">支持</span></span><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">零点击、一键点击服务端攻击</span></span></strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">，还可实现持续入侵与攻击扩散</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击持续性</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">一次性数据泄露</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">可篡改</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">ChatGPT </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">记忆规则，实现持续窃取用户所有对话数据</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">攻击扩散性</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">无扩散能力</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">可扫描用户收件箱获取联系人邮箱，自动发送恶意</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">payload</span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">，实现企业级扩散</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">防护绕过方式</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">绕过用户视觉感知和本地防护</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">绕过</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">OpenAI </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">禁止动态修改</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">URL </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">的防护规则</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr><tr><td data-colwidth="108" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><strong><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">修复时间</span></span></strong><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="216" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">2025 </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">年</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">9 </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">月</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">3 </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">日</span></span><span lang="EN-US"><o:p></o:p></span></p></td><td data-colwidth="215" width="184"><p style="margin-top: 0px;margin-bottom: 0px;text-indent: 0px;"><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">2025 </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">年</span></span><span lang="EN-US"><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">12 </span></span></span><span leaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.6;letter-spacing: 0.034em;font-style: normal;font-weight: normal;"><span textstyle="" style="font-size: 15px;">月中旬</span></span><span lang="EN-US"><o:p></o:p></span></p></td></tr></tbody></table>  
参考资料：  
  
https://www.radware.com/blog/threat-intelligence/shadowleak/  
  
https://www.infosecurity-magazine.com/news/vulnerability-chatgpt-agent-gmail/  
  
https://www.infosecurity-magazine.com/news/new-zeroclick-attack-chatgpt  
  
https://cybersecuritynews.com/chatgpt-vulnerabilities-expose-sensitive-data/  
  
（完）  
  
