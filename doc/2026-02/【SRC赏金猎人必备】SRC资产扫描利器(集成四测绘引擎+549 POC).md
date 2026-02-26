#  【SRC赏金猎人必备】SRC资产扫描利器(集成四测绘引擎+549 POC)  
原创 0xSecDebug
                    0xSecDebug  0x八月   2026-02-26 00:10  
  
# 【SRC赏金猎人必备】SRC资产扫描利器(集成四测绘引擎+549 POC)  
  
  
⚠️  
  
    请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。  
**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**  
  
⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"  
**0x八月**  
"设为星标⭐️"否则可能就看不到了啦  
,  
点击下方卡片关注我哦！  
  
**💡项目地址在文章底部哦！**  
  
  
  
  
## 📖 项目/工具简介  
  
    FuYao是Go语言开发的自动化资产探测与漏洞扫描工具  
，适用于赏金猎人及安全团队进行SRC活动。（注：该工具目前维护中且不再开源）  
## 🚀 一句话优势  
  
    集成**四大网络空间测绘**  
引擎，实现子域发现到漏洞验证的全自动化闭环  
。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能名称</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">一句话说明</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多源资产收集</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">集成Hunter、FoFa、Quake、Shodan四测绘</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">子域名枚举</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">被动在线资源发现有效子域</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">存活验证联动</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">探测完成后自动验证资产存活状态</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多协议漏洞扫描</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持TCP/DNS/HTTP/FILE协议检测</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">零误报POC验证</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">基于Afrog引擎精准验证549个漏洞</span></section></td></tr></tbody></table>  
## 📸 运行截图  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能模块</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">截图位置</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">工具启动界面与版本检测</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzxaS9vicQWpPEuJANVMzRMiaVjkBeTlHH2CE2c2IGBJvndmiaWd6XKsZwcjSibtSN4JIYtSpIbMVAnBRRFvHpnQcg3hw4PGEA9U1o/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.4064814814814815" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002937" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">子域名与资产探测结果</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxwV9nBPJaSYtn4ECurWMkRNiaLOnqmIu5vzO6YlLRlrheiaiaGI00Wwq0DibHF7ngIGvticbxdfI01JJJfvOicYGSxTXcAWWDVmYibXY/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.4962962962962963" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002938" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">漏洞扫描POC执行过程与存活验证与端口探测输出</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODy8ehKVQcpX7jPt9TsDfIkNfDXcS5XXbQadrJsvaxNgCcr1fZV23hGqRIOnoPYOlDgwPkgMZsf8eUtOOTEVgSDrVR2dcUkYIPo/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5120370370370371" data-type="png" data-w="1080" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002939" data-aistatus="1"/></section></td></tr></tbody></table>  
## ✨ 核心亮点  
1. 1  
四测绘引擎融合资产发现  
    FuYao同时接入Hunter、FoFa、Quake、Shodan四大网络空间测绘API，通过多源数据交叉验证补充子域名资产  
。相比单一数据源，能覆盖更全面的暴露面，减少因信息源局限导致的资产遗漏，特别适合大型企业级资产梳理场景  
。  
  
1. 2  
扫描-验证-漏洞联动闭环  
    子域名枚举完成后自动进行存活验证  
，同步完成端口探测，存活资产直接进入漏洞扫描阶段。工具内置Afrog引擎加载549个POC  
，同时支持通过-p  
参数导入自定义xray格式模板，**实现从资产发现到漏洞报告的无人工干预自动化流程。**  
  
1. 3  
多协议低误报扫描架构  
    不仅支持HTTP/Web类漏洞检测，还覆盖TCP、DNS、FILE等各类协议  
。采用定制模板精准匹配漏洞特征，通过零误报设计减少无效告警，避免安全团队浪费时间在人工复核误报上，适合对大规模主机进行批量协议级安全检测。  
  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Go语言开发</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">编译型语言高并发处理</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">扫描速度快，资源占用低，适合大规模目标</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Afrog漏洞引擎</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">专业漏洞验证框架集成</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">549个内置POC，支持xray模板格式扩展</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">四测绘API融合</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Hunter/FoFa/Quake/Shodan</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">资产发现维度广，数据交叉验证减少遗漏</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多协议扫描架构</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">TCP/DNS/HTTP/FILE全支持</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">不仅限于Web，覆盖基础设施层协议检测</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">零误报模板设计</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">精准匹配逻辑</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">减少无效告警，提升安全团队处置效率</span></section></td></tr></tbody></table>  
## 📖 使用指南  
  
① **准备工作**  
：获取对应系统的二进制文件（不推荐Windows环境），在配置文件中填入FoFa、Shodan、Quake、Hunter的API密钥及Webhook通知地址。  
  
② **核心操作**  
：准备包含主域名的文本文件（一行一个），执行./FuYao -f list.txt  
启动自动化流程，可通过-p  
参数指定自定义xray格式漏洞文件夹路径。  
  
③ **结果查看**  
：扫描完成后查看控制台输出及Webhook通知，根据指纹探测识别结果和漏洞验证数据筛选有效发现，用于后续人工复核或SRC平台提交。  
  
## 📖 项目地址  
```
https://github.com/ExpLangcn/FuYao-Go/tree/main?tab=readme-ov-file
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
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="100.33333333333333" width="100.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyBdiau5GC7dWricMbXhF76xhhbcjia7Uj6987eBmBe6ov5ibhib2lJP6qmicTbz2zK2ObzgicE7kqY83MVGqJwTgJnIEbfXAkgGykAl8/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="1.306474820143885" data-w="695" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;" data-cropselx1="0" data-cropselx2="21" data-cropsely1="0" data-cropsely2="31" data-backw="0.7272800000000004" data-backh="0.7272800000000004" data-imgfileid="100002876" data-aistatus="1"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.625" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;" data-backw="32.72728" data-backh="19.72728" data-imgfileid="100002878" data-aistatus="1"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.9768518518518519" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;" data-backw="32.72728" data-backh="31.72728" data-imgfileid="100002877" data-aistatus="1"/></section></th></tr></thead></table>  
  
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
  
