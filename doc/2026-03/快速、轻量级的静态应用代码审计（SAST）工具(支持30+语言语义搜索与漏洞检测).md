#  快速、轻量级的静态应用代码审计（SAST）工具(支持*30+语言*语义搜索与漏洞检测)  
原创 0x八月
                    0x八月  0x八月   2026-03-10 08:39  
  
# 快速、轻量级的静态应用代码审计（SAST）工具(支持30+语言语义搜索与漏洞检测)  
  
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
  
  
**Semgrep**  
 是快速开源静态代码分析工具  
，支持30+语言  
语义搜索与漏洞检测，适用于代码审计与CI/CD防护。  
  
## 🚀 一句话优势  
  
  
**语义化代码匹配精准识别漏洞**  
，规则即代码无需学习复杂DSL。  
  
## 📋 核心能力速览  
  
  
<table><thead><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><th style="margin: 0px;padding: 12px 16px;box-sizing: border-box;border: 2px solid rgb(26, 26, 26);text-align: left;font-weight: 800;background-color: rgb(255, 217, 61);color: rgb(26, 26, 26);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能</span></section></th><th style="margin: 0px;padding: 12px 16px;box-sizing: border-box;border: 2px solid rgb(26, 26, 26);text-align: left;font-weight: 800;background-color: rgb(255, 217, 61);color: rgb(26, 26, 26);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">语义代码搜索</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">理解代码结构而非文本匹配</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: rgb(255, 249, 196);"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">多语言支持</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">覆盖Python、Go、Java等30+语言</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">供应链安全</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">检测第三方库中可达漏洞</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: rgb(255, 249, 196);"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">本地分析</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">默认代码不上传保障隐私</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">CI/CD集成</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">PR扫描与自动修复建议</span></section></td></tr></tbody></table>  
  
## ✨ 核心亮点  
  
  
### 1. 语义化搜索  
  
  
不同于grep文本匹配  
，Semgrep理解代码语义，搜索2时能匹配x = 1; y = x + 1  
，精准识别变量传播  
与控制流  
问题。  
  
### 2. 规则即代码  
  
  
Semgrep规则看起来就像你写的目标代码  
，无需抽象语法树知识或痛苦正则，降低规则编写门槛  
，安全团队可直接维护。  
  
### 3. 多维度检测  
  
  
社区版提供**SAST**  
基础能力，商业版增加*u>跨文件数据流分析*与**SCA**  
供应链检测，AI Assistant  
进一步降低误报率并提供修复指导。  
  
## 🛠️ 技术优势  
  
  
<table><thead><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><th style="margin: 0px;padding: 12px 16px;box-sizing: border-box;border: 2px solid rgb(26, 26, 26);text-align: left;font-weight: 800;background-color: rgb(255, 217, 61);color: rgb(26, 26, 26);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="margin: 0px;padding: 12px 16px;box-sizing: border-box;border: 2px solid rgb(26, 26, 26);text-align: left;font-weight: 800;background-color: rgb(255, 217, 61);color: rgb(26, 26, 26);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="margin: 0px;padding: 12px 16px;box-sizing: border-box;border: 2px solid rgb(26, 26, 26);text-align: left;font-weight: 800;background-color: rgb(255, 217, 61);color: rgb(26, 26, 26);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">程序分析引擎</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">基于语法树的语义理解</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">精准识别代码模式</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: rgb(255, 249, 196);"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">Pro引擎</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">跨文件跨函数数据流追踪</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">减少25%误报，增加250%真阳性</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">轻量架构</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">单二进制文件</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">快速启动低资源占用</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: rgb(255, 249, 196);"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">隐私保护</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">本地分析不上传</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">代码不出内网</span></section></td></tr><tr style="margin: 0px;padding: 0px;box-sizing: border-box;border: 0px;background-color: transparent;"><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">生态集成</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">VS Code、GitHub Actions等</span></section></td><td style="margin: 0px;padding: 12px 16px;box-sizing: border-box;font-size: 15px;border: 2px solid rgb(26, 26, 26);text-align: left;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section><span leaf="">无缝融入开发工作流</span></section></td></tr></tbody></table>  
  
## 📖 使用指南  
  
  
① **准备工作**  
：通过brew install semgrep  
或**pip install semgrep**  
安装，登录获取Pro规则访问权限。  
  
② **核心操作**  
：执行**semgrep ci**  
扫描整个项目，或使用trivy -e '$X == $X' --lang=py  
运行特定规则检测。  
  
③ **结果查看**  
：在IDE  
中查看实时高亮，或在PR评论  
中接收漏洞提醒，导出**JSON/SARIF**  
格式报告用于合规审计。  
  
## 📖 项目地址  
  
```
https://github.com/semgrep/semgrep?tab=readme-ov-file
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
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="214.33333333333334" width="214.33333333333334" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img alt="img" class="rich_pages wxw-img" data-aistatus="1" data-cropselx1="0" data-cropselx2="176" data-cropsely1="0" data-cropsely2="236" data-imgfileid="100003010" data-ratio="1.4665523156089193" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODxCPibZHwI0h87VgQCoac1RPa8LkqPfe94EibRdkObaIdFOLU6LE4dVo1h5ia9brohDj2hw7ia0TaPHZ2JGh07lw4ciaZgmIg2gMt8Q/640?wx_fmt=jpeg&amp;from=appmsg" data-w="1166" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 176px;height: 258px;"/></section></th><th data-colwidth="205.33333333333334" width="205.33333333333334" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.625" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100003011" data-aistatus="1"/></section></th></tr></thead><tbody><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="234.33333333333334" width="234.33333333333334" style="font-size: 15px;border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.9768518518518519" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100003012" data-aistatus="1"/></section></td><td data-colwidth="225.33333333333334" width="225.33333333333334" style="font-size: 15px;border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw9FiaDxkbDmibgOqmB8jafl5EsFpuMMngJvqHEI0tBTUol1fiaHV2Yc0PCvqYvPe15C7ibgSImsMFyc9Sk9fZl1Jabibrq1Zlq8JMA/640?wx_fmt=jpeg&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="1.4665523156089193" data-type="png" data-w="1166" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 143px;height: 210px;" data-cropselx1="0" data-cropselx2="143" data-cropsely1="0" data-cropsely2="210" data-imgfileid="100003013" data-aistatus="1"/></section></td></tr></tbody></table>  
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
  
