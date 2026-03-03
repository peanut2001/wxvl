#  LLM驱动的多智能体协同漏洞挖掘与PoC验证框架  
原创 0x八月
                    0x八月  0x八月   2026-03-03 03:59  
  
# LLM驱动的多智能体协同漏洞挖掘与PoC验证框架  
  
  
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
  
    Strix是开源AI安全代理框架，**通过多代理协作实现自动化漏洞挖掘与验证**  
，适用于开发团队安全测试与CI/CD集成。  
## 🚀 一句话优势  
  
    基于LLM的多代理架构自动生成PoC验证漏洞  
，减少静态分析误报与人工渗透测试成本。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能名称</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">一句话说明</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">AI代理编排</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多代理协作执行分布式安全测试任务</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">动态代码分析</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Docker沙箱内运行目标代码验证漏洞</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">PoC生成验证</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自动构造概念验证排除误报</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">浏览器自动化</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多标签页测试XSS与认证流程</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">CI/CD集成</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">GitHub Actions流水线自动化安全检测</span></section></td></tr></tbody></table>  
## 📸 运行截图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzJmwYlMbKy3938jkJo4WWHj7lduiccbfLFia3uv3ianlbnplibeS0UIb5ZmmwMdGRrO500VEp3ts24h8KQ2MUHovR62I308jpX0wA/640?wx_fmt=png&from=appmsg "")  
## ✨ 核心亮点  
1. 1  
多代理协作验证机制：  
    Strix采用分布式代理架构，针对不同攻击面和漏洞类型分配专用代理。代理之间共享发现并动态协调，通过实际构造PoC验证漏洞而非仅依赖静态规则匹配  
，将验证环节从 hours 缩短至 minutes，降低传统SAST工具的高误报率。  
  
1. 2  
动态运行时沙箱检测：  
    在Docker沙箱中运行目标应用，结合HTTP代理、浏览器自动化和交互式终端，动态触发业务逻辑漏洞  
。支持IDOR、竞争条件等需要上下文交互才能发现的漏洞类型，弥补纯源码扫描在业务逻辑检测上的盲区。  
  
1. 3  
开发者友好集成：  
    提供CLI工具与GitHub Actions组件，支持在Pull Request阶段触发快速扫描。通过--instruction  
参数允许开发者指定测试范围与认证凭据，扫描结果包含可操作的修复建议与一键生成PR的自动修复功能，适配现有DevOps workflow。  
  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">LLM多提供商支持</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持OpenAI、Anthropic、Google等主流模型</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">可按需求选择性能与成本的平衡点</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Docker沙箱隔离</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">动态分析环境容器化</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">安全执行不受信代码，避免污染宿主机</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Playwright浏览器引擎</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">现代Web应用自动化测试</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">支持复杂SPA应用与多标签页交互</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">LiteLLM统一接口</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多模型提供商标准化接入</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">简化配置，便于切换不同AI后端</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">无头模式支持</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><code><span leaf="">-n</span></code><section><span leaf="">参数非交互式运行</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">适配CI/CD自动化流水线，失败时非零退出</span></section></td></tr></tbody></table>  
## 📖 使用指南  
  
① **准备工作**  
：安装Docker并配置LLM API密钥（export LLM_API_KEY  
与export STRIX_LLM  
），通过curl -sSL https://strix.ai/install | bash  
安装CLI。  
  
② **核心操作**  
：执行strix --target ./app-directory  
扫描本地代码，或strix --target https://your-app.com  
进行黑盒测试；CI/CD场景使用strix -n -t ./ --scan-mode quick  
启用无头模式。  
  
③ **结果查看**  
：扫描完成后查看终端输出的漏洞报告（包含PoC与复现步骤），或通过Strix平台查看可视化结果与自动修复建议，严重漏洞会以非零状态码退出供流水线捕获。  
  
## 📖 项目地址  
  
```
https://github.com/usestrix/strix?tab=readme-ov-file
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
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="214.33333333333334" width="214.33333333333334" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img alt="img" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100003010" data-ratio="1.3380281690140845" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyXfLtLHU3A88LXmZT8EtMqy6VegonUBiaGeLt2IUFCv7boItjxe0LE29TV7Noq8dYEL0GdJYEp3vIV2v53lhgdNBzcLKKT2pWQ/640?wx_fmt=png&amp;from=appmsg" data-w="639" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></th><th data-colwidth="205.33333333333334" width="205.33333333333334" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.625" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100003011" data-aistatus="1"/></section></th></tr></thead><tbody><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><td data-colwidth="234.33333333333334" width="234.33333333333334" style="font-size: 15px;border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section nodeleaf=""><img alt="img" class="rich_pages wxw-img" data-aistatus="1" data-imgfileid="100003012" data-ratio="0.9768518518518519" data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&amp;from=appmsg" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;"/></section></td><td data-colwidth="225.33333333333334" width="225.33333333333334" style="font-size: 15px;border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;color: rgb(45, 45, 45);font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyhsnwhsymx5SWwkgibVGHPndPNibVg0MLJZkZhT6txknbLib8DTkWNLIa7NQa3wvbmXm9ycgsHSsP05GPG5Gcib50KIxUEv65E4AY/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="1.4666666666666666" data-type="png" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100003013" data-aistatus="1"/></section></td></tr></tbody></table>  
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
  
