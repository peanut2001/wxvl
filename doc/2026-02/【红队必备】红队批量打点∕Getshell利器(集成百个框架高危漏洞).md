#  【红队必备】红队批量打点/Getshell利器(集成百个框架高危漏洞)  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-24 00:59  
  
# 【红队必备】红队批量Getshell利器(集成百个框架高危漏洞)  
  
  
⚠️  
  
    请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。  
**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**  
  
⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"  
**0xSecDebug**  
"设为星标⭐️"否则可能就看不到了啦  
,  
点击下方卡片关注我哦！  
  
**💡项目地址在文章底部哦！**  
  
  
  
## 📖 项目/工具简介  
  
WebFrameworkTools是面向红队的批量Web框架漏洞利用工具，**集成百个高危EXP，支持一键getshell与自定义DLL插件扩展。**  
## 🚀 一句话优势  
  
集成ThinkPHP、Struts2等百个框架高危漏洞，支持批量一键getshell与自定义插件扩展。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">批量漏洞利用</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">一键getshell，非仅检测存在</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">框架覆盖全面</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持ThinkPHP、WebLogic、OA系统等</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自定义DLL扩展</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持C<a class="wx_topic_link" topic-id="mlzw9rkb-hn2yt9" style="color: #576B95 !important;" data-topic="1">#编写插件扩展漏洞库</a></span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">智能模块筛选</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持勾选或排除指定检测模块</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">DNSLog验证</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">解决无回显漏洞检测难题</span></section></td></tr></tbody></table>  
## 📸 运行截图  
  
### 工具主界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODy2kiaBPvRt1EdQ3EkiaDGsu6uwQboH11ryibibicKvbyKpibmFt0gdfGNKb7u4icOk4RDXDjS5RWDeTdmwtYJj7klroh2fa2IlI8IWvY/640?wx_fmt=png&from=appmsg "")  
### 内置exp模块  
- ◆  
thinkphp  
- ◆  
weblogic  
- ◆  
struts2  
- ◆  
hadoop  
- ◆  
atlassiancrowd  
- ◆  
ueditor  
- ◆  
tongdaoa  
- ◆  
apacheflink  
- ◆  
ruijie  
- ◆  
apachedruid  
- ◆  
......集成ThinkPHP、Struts2等百个框架高危漏洞  
### 实测部分效果  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img alt="CVE-2025-55182注入内存马" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002896" data-ratio="0.5259259259259259" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwJMBf0hl94XDHKfeDX2hrs04aXE9iaTzYL9zuYfYhbmIicDhoe0icOYm2A0bBWpur8x0ptnSmutg6ogxVgxDvzlr4Nseq32NTibtM/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="CVE-2025-53770批量getshell" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002897" data-ratio="0.4537037037037037" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwOE5YdVH7zibF6g2gmBS7lJKbHic2ic1vBicdAy7TSiavvY7ibdyXicdvGxCVxAE3oiaicQKG3fRSaNxYKP2j7EOKaHLuwW5ia2I76VDFgs/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="CVE-CVE-2021-22205" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002899" data-ratio="0.5361111111111111" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODx4M48nKSzxjxVmicjNGXEfpl0LONUDlELViaRv98jAohHJalRRjXDYl7uNe5nic6g5ZbxylpG8xsliciay6wRTsVaBEicyWzU07IzMU/640?wx_fmt=png&amp;from=appmsg" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td></tr></tbody></table>## ✨ 核心亮点  
  
### 1. 实战化一键getshell设计  
  
不同于仅返回漏洞是否存在的扫描器，WebFrameworkTools每个集成漏洞都经过实战验证，优先采用RCE、反序列化、上传等方式直接获取权限。**工具拒绝"只检测不利用"的鸡肋逻辑**  
，批量导入URL后自动将成功的shell路径写入文件。这种设计大幅压缩了从发现漏洞到获取权限的时间窗口，适合红队快速打点场景。  
### 2. 灵活的插件扩展机制  
  
工具支持通过Visual Studio编写C# DLL插件，**内置一键生成器降低开发门槛**  
。遇到新披露的0day时，你可以快速将Python EXP转化为C# DLL模块，无需等待官方更新。这种架构让工具具备持续进化能力，目前已支持用户自定义反序列化链、内存马注入  
等高级利用方式。  
### 3. 精准的模块控制策略  
  
提供-include和-exclude参数实现精细化扫描，**避免全量检测触发WAF导致IP被封**  
。支持代理模式抓取真实EXP数据包，方便手工验证和绕过。针对无回显漏洞集成DNSLog验证，解决内网不出网场景下的漏洞确认难题，兼顾速度与隐蔽性  
。  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">.NET Framework</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">C<a class="wx_topic_link" topic-id="mlzw9rkc-6a35ap" style="color: #576B95 !important;" data-topic="1">#混合C</a>++开发</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">单文件部署，无需Python/Java环境依赖</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多线程引擎</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持自定义线程池</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">平衡扫描速度与准确性，避免高并发漏报</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">DLL插件架构</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">动态加载用户模块</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">EXP快速武器化，框架可持续扩展</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">代理与编码</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持HTTP/SOCKS代理</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">便于抓包调试与特殊字符绕过</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">DNSLog集成</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自动对接dnslog平台</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">解决无回显漏洞验证，提升内网适用性</span></section></td></tr></tbody></table>  
## 📖 使用指南  
1. 1  
环境准备:  
安装.NET Framework 4.5.1+及VC++运行库，下载release版本，创建包含http://或https://的url.txt目标文件。  
  
1. 2  
执行扫描:  
使用-type thinkphp  
指定框架，或创建include.txt勾选需检测的模块，通过-thread 20  
设置线程数（建议默认），启动后自动将getshell结果写入shell.txt。  
  
1. 3  
扩展开发:  
使用内置DLL生成器创建C[#插件]()  
，或编写自定义DLL放入目录，通过-dllname  
参数加载新EXP进行批量利用。  
  
  
  
## 📖 项目地址  
```
https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance
```  
## 💻 技术交流与学习  
  
      
如果师傅们想要第一时间获取到  
**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
  
    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，  
**内容还在持续整理中......**  
。  
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="100.33333333333333" width="100.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img alt="img" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100002876" data-ratio="1.230357142857143" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzPNweL1oOUEucY0N5qKrqzZCVqHq6jTWpY9iaKrRRdYYuxMQ72Phq4dfFLaf1R73eaoiaYSg74LKXtVsRr7pKrr30T0FjkkDfHM/640?wx_fmt=png&amp;from=appmsg" data-w="560" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.625" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002878" data-aistatus="1"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.9768518518518519" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002877" data-aistatus="1"/></section></th></tr></thead></table>  
  
### 推荐阅读  
  
  
✦ ✦ ✦  
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="439.3333333333333" width="439.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);background-color: rgb(255, 217, 61);text-align: left;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;word-break: break-all;"><section style="text-align: center;"><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485592&amp;idx=1&amp;sn=818004a6d625c4c4112ce73b83433854&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录</a></span></section></th></tr></thead><tbody><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="459.3333333333333" width="459.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485309&amp;idx=1&amp;sn=292afbe37fb95c64f33470f915b0c54e&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: rgb(255, 249, 196);"><td data-colwidth="459.3333333333333" width="459.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247486181&amp;idx=1&amp;sn=3ace47da643c72cec0d615aeccb955ac&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="439.3333333333333" width="439.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485488&amp;idx=1&amp;sn=a37acb031febe69db608de53ddee5732&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: rgb(255, 249, 196);"><td data-colwidth="439.3333333333333" width="439.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485208&amp;idx=1&amp;sn=b5181181c1e0800124e3e099706ef2ef&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">AI 原生安全测试平台(CyberStrikeAI)</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="459.3333333333333" width="459.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485805&amp;idx=1&amp;sn=8f374a239135f6a753d5cce887f8318b&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: rgb(255, 249, 196);"><td data-colwidth="459.3333333333333" width="459.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485314&amp;idx=1&amp;sn=56082cd314311ffc15cc0bcf03a395e2&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)</a></span></section></td></tr><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="459.3333333333333" width="459.3333333333333" style="padding: 12px 16px;border-width: 2px;border-color: rgb(26, 26, 26);font-size: 15px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf=""><a class="normal_text_link" target="_blank" style="color: rgb(255, 107, 107);border-bottom: 3px solid rgb(255, 217, 61);background: linear-gradient(transparent 70%, rgba(255, 217, 61, 0.3) 0px);transition: 0.2s;" href="https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&amp;mid=2247485127&amp;idx=1&amp;sn=b5eb3fdc1cc23976011e2bca396c1bc7&amp;scene=21#wechat_redirect" textvalue="" linktype="text" data-linktype="2">基于AI的自主渗透测试平台 </a></span></section></td></tr></tbody></table>  
  
✦ ✦ ✦  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
