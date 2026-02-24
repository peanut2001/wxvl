#  红队实战利器：RapidDNS CLI + Nuclei/Httpx 打造自动化漏洞挖掘流水线  
原创 男人老白
                    男人老白  RapidDNS   2026-02-24 00:46  
  
大家好，我是男人老白。  
  
今天给大家分享基于RapiDNS API的实用工具——  
RapidDNS CLI。它的设计着重红队实战场景：  
支持管道流、自带数据清洗、支持自动化导出，能无缝对接  
httpx和  
nuclei等工具，直接把资产收集到漏洞扫描这一套流程打通。  
  
注意：这个工具本质上是调用 RapidDNS 的高级 API，所以你需要有一个 PRO 或 MAX 的账号来获取 API Key 才能跑起来。好处是只要你是会员，这就没有任何复杂的配额限制，直接调就完事了，简单粗暴。  
  
话不多说，直接上实战配置和玩法。  
# 0x00 第一步：环境准备与安装  
  
给大家推荐两种最快的安装方式：  
  
方式一：直接下载  
  
不用装 Go 环境，直接去 GitHub 的 release页面（https://github.com/rapiddns/rapiddns-cli/releases）， 下载对应你系统的压缩包（Windows/Mac/Linux 都有）。解压出来，把  
rapiddns-cli这个文件丢到命令行能访问的目录下就行。  
  
方式二：Go Install  
  
只要你有 Go 环境，一条命令搞定，永远保持最新版：  
```
go install github.com/rapiddns/rapiddns-cli@latest
```  
  
装好后，终端输入  
rapiddns-cli看看有没有反应。  
# 0x01 第二步：核心配置（必做）  
  
要让这辆跑车动起来，你得先给它加满油——也就是配置  
API Key。  
  
1. 获取 API Key  
  
登录 https://rapiddns.io ，在个人中心复制你的 API Key。  
  
2. 写入配置  
  
拿到 Key 之后，一行命令配置进工具：  
```
rapiddns-cli config set-key "你的API_KEY"
```  
  
验证一下配置成功没：  
```
rapiddns-cli config get-key
```  
  
配置完成，现在你拥有了全量数据查询的权限。  
# 0x02 实战技巧一：一行命令搞定 HTTP 存活探测  
  
以前我们要先跑子域名工具，把结果存文件，再用 httpx 读文件... 太麻烦了。RapidDNS CLI 设计了很多方便管道操作的参数。  
  
场景：我想搜集  
tesla.com的所有子域名，并且直接看哪些是活着的 Web 服务。  
  
组合拳命令：  
```
rapiddns-cli search target.com --column subdomain -o text | httpx -silent -sc -title -cl
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nwqpzvvFByPnI9yuNhNswofMTa4CBVjRWTicmCibDAgYnEOiaMsIkuUMFddcqJfyhMhtKTzanAIIelyKLMwG74LQWOC2LUdVakwUB7fEXibib3e0/640?wx_fmt=png&from=appmsg "")  
  
解析：  
  
--column subdomain: 只输出子域名这一列，不用你去 awk 切割了。  
  
-o text: 纯文本输出，每行一个。  
  
--silent: 静默模式，不打印那些 "Fetching..." 的进度条，只输出纯净数据给管道。  
  
| httpx ...: 直接喂给 httpx，接着就能看到满屏的 Web 指纹和状态码了。  
  
这一套下来，从收集到探测，几分钟的事。  
# 0x03 实战技巧二：自动化 Subdomain Takeover（子域名接管）  
  
接管漏洞是很多赏金猎人的最爱。我们可以把 RapidDNS 收集到的子域名直接喂给 Nuclei 扫描。  
  
组合拳命令：  
```
rapiddns-cli search google.com --column subdomain -o text| nuclei -t http/takeovers -o takeover_results.txt
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nwqpzvvFByOW99ib44tU1Lib5KRHJBpKmcZpDQwibJ9Hz7wNJdqkZV3LRCRJxAAlRoYhWPiamern0M5EFTEM9PqibsjxJcQAOduqQkncAY3LHXmE/640?wx_fmt=png&from=appmsg "")  
  
这比你手动去网站上查完再复制粘贴要快多少倍？配合定时任务，你甚至可以每天自动跑一遍新资产。  
# 0x04 实战技巧三：高级语法精准打击  
  
普通的子域名查询可能大家都会，但 RapidDNS CLI 最强大的地方在于支持  
Advanced Query（高级语法）。  
  
很多时候我们不想看所有的记录，只想找特定的“软柿子”。比如：  
我只想找解析记录是 CNAME 的子域名（因为 CNAME 记录最容易出接管漏洞）。  
  
使用  
--type advanced参数：查找 apple.com 下所有类型为 CNAME 的记录  
```
rapiddns-cli search "domain:apple AND tld:com AND type:CNAME" --type advanced
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nwqpzvvFByN1eqKBlhba7iagcJFJJFwficDZztgq1RiarBgV3ZjlfeWuDickF6pD7HvBYDFyNdFrZTZxl6icFRrhEM0nBvkBCtlJr2xn3xYyt1F4/640?wx_fmt=png&from=appmsg "")  
  
或者查找某个 IP 段内的所有 A 记录：  
  
精准定位某个 C 段的资产  
```
rapiddns-cli search "value:8.8.8.8/24 AND type:A" --type advanced
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nwqpzvvFByMHY1NCmzZyV8jyWHJfLYTacQ4qQOvTIn7bqs07mcC208V7b6OUopRXEFydib6fMibSxHVZQp3C7YTxW135nZYqVfsEgWicFGDSgM/640?wx_fmt=png&from=appmsg "")  
  
这种精细化的查询，能帮你过滤掉大量无效信息，直接定位到最可能有问题的资产上。配合导出功能使用，效果更佳。  
# 0x05 实战技巧四：自动化资产清洗与 IP 统计  
  
当我们拿到几万个子域名时，最头疼的是什么？  
  
去重（重复的太多）。  
  
分析 IP 段（看看资产主要分布在哪个 C 段，方便做内网渗透或后续扫描）。  
  
RapidDNS CLI 自带了数据清洗功能，不用你自己写脚本了。  
  
命令：  
```
rapiddns-cli search target.com --extract-subdomains --extract-ips
```  
  
跑完这个命令，你的result/目录下会自动生成三个文件：  
  
target.com_subdomains.txt: 纯净去重后的子域名列表。  
  
target.com_ips.txt: 纯净去重后的 IP 列表。  
  
target.com_ip_stats.txt: IP 段统计报告  
# 0x06 终极玩法：海量数据自动化导出  
  
如果你面对的是像  
google.com这种级别的超大目标，或者你需要一次性拉取几十万条数据，普通的  
search命令可能会因为翻页太慢或者本地网络波动断掉。  
  
这时候就要用  
Export 模式。这是专门为 API 用户设计的高级功能，任务完全在云端跑，跑完自动下载。  
  
而且，Export 模式也支持高级语法！  
  
启动导出任务：导出 apple下所有 CNAME 记录，并自动提取子域名  
```
rapiddns-cli export start "domain:apple AND tld:com AND type:CNAME" --type advanced --extract-subdomains
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nwqpzvvFByNF6mvlT9FVB6aaqzCsB1PWAIm2vSPXG5QsUfCrosVkVYfhRViampjGQWvia2M0Zz1lWI3ofbnM7iaEpOrBDd3a8jVqD94SezkEO8/640?wx_fmt=png&from=appmsg "")  
  
它会自动执行以下流程：  
1. 提交任务到云端。  
  
1. 自动轮询状态（你可以去喝杯咖啡，不用守着）。  
  
1. 任务完成后，  
自动下载 ZIP 包。  
  
1. 自动解压。  
  
1. 自动解析 CSV，给你生成好去重后的 txt 文件。  
  
# 0x07 总结  
  
RapidDNS CLI 不仅仅是一个查询工具，它更像是一个  
资产数据的“连接器”。  
  
对于初学者：去 GitHub 下个文件，配个 Key 就能用，简单无脑。  
  
对于老手：利用 Advanced Search 精准筛选数据，再配合 Pipeline 喂给 Nuclei等工具，实现快速的漏洞发现等。  
  
RapidDNS会不断扩充数据，以帮助各位白帽子发现更多有价值的数据。致力打造成为各位白帽子的渗透测试利器。  
# 0x08 付费指南 (支持微信)  
  
虽然 RapidDNS 网站目前是全英文界面，但支付过程非常简单，且完美支持国内支付方式。  
  
第 1 步：进入价格页  
  
点击下方链接，或在网站顶部导航栏点击 "Pricing"。  
  
👉 升级地址：https://rapiddns.io/pricing （也可以点击阅读原文进入）  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/SYxbvhekRGcDROPuGtC3DTzRMKhibxusuN1s9A8P3EcPKpfT8VvPRicHauLugxYooVXrGVP1IYibmROR3O2qqXtSg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
第 2 步：选择套餐  
  
如果你想订阅月付，点击下方的 "Subscribe to PRO"或者"Subscribe to MAX"。当前年付订阅更优惠，年付则可以切换到yearly进行订阅。订阅方式仅支持外币的信用卡进行支付。  
  
如果你想抢终身版，找到 "Lifetime" 卡片，点击 "pay with wechat"。  
  
点击后会跳转到支付页面，选择微信，输入姓名，点击"继续使用微信"即可打开微信支付二维码页面。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/SYxbvhekRGcDROPuGtC3DTzRMKhibxusuQsvI2ayGGMO1FPu9cU39Cpmkia0ObzAQM9lkaz1pT7g26ltouYdG5rA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
注意：如果没有外币信用卡的朋友，只能通过“Pay with wechat” 进行支付。微信支付只能一次性，需要自己到期后主动续费  
  
第 3 步：支付 (关键)  
  
接下来使用微信扫码支付即可。  
  
(支付成功后，账号权限将自动开通。如遇问题，请直接在公众号留言)。  
# 0x09 全量售卖  
  
另外除上述功能外，全量数据售卖长期持续进行中。有意者可联系我了解详细内容。全量即当前网站全部内容，售价3万。全量数据随着数据量的不断增加，后续价格可能会涨。有意向尽快联系我，  
  
注：本文涉及的渗透测试内容仅供安全研究与教学使用，请勿用于非法用途。  
  
  
