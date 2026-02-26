#  【SRC赏金猎人必备】一款自动化SRC资产监控与漏洞扫描框架  
原创 0xSecDebug
                    0xSecDebug  0x八月   2026-02-26 00:01  
  
# 【SRC赏金猎人必备】自动化暴露面收集与监控框架  
  
  
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
  
laoyue是一款自动化SRC资产监控与漏洞扫描框架，集成多引擎能力，**适合赏金猎人快速发现攻击面。**  
## 🚀 一句话优势  
  
集成四种扫描引擎与资产监控，实现SRC自动化赏金挖掘全流程。  
## 📋 核心能力速览  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能名称</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">一句话说明</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多引擎漏洞扫描</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">集成Nuclei、Fscan、AWVS、Ffuf四款工具</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自动化资产收集</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">融合FoFa、Shodan等空间测绘API数据</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">暴露面资产梳理</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自动识别子域名、目录与敏感信息泄露</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">防卡死监控机制</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">定时检测任务状态，异常自动恢复保活</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">结构化报告输出</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">自动生成Excel格式汇总表方便提交</span></section></td></tr></tbody></table>  
## 📸 运行截图  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">功能模块</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">截图位置</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">暴露面资产发现</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxbrf2MxXUNLqFahWzKCxIicO9cf9ARoyibSNebZRhzV3UqKzJ7tPG27IicmldAqf7ziayVlThzWoT86GWVx0gx4oxtwhQZicRCX8fk/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.6674786845310596" data-type="png" data-w="821" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002924" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">敏感信息泄露检测</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwZSHk1r3icsfUq8NMFLiblNa8WX4o1icicKicVjaXJuVicCgtfdUpwd2y6cgL3EtnsetGmbdhEpN6IBNNyxNOcIRB8JRdoezrOCalbg/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5149769585253456" data-type="png" data-w="868" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002923" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">漏洞扫描结果（Nuclei/Fscan/AWVS）</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwQA1pjpYjasMSwS3NzMkI8aBybpIgjA8Uaukcm1v0u0OxXukSdV0O9lZgBYBbk4O7AsUmtv8S7NT48PLBAEyjGeTm2jaaagEQ/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="1.9793650793650794" data-type="png" data-w="630" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002926" data-aistatus="1"/></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Excel汇总报告示例</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwU9QsSFdAagicok7biaGGYJQS8BQkqcgStc0krKrzPToNiciapNPwYWxXnricPmkh6hNfjfjuqsmic9sSh2YXUtBpCh1Vukric4bRt7Q/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.6362694300518135" data-type="png" data-w="965" style="display: block;margin: 32px auto;max-width: 100%;border-radius: 4px;border: 4px solid #1a1a1a;box-shadow: 8px 8px 0px #1a1a1a;background: #fff;padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;" data-imgfileid="100002925" data-aistatus="1"/></section></td></tr></tbody></table>  
## ✨ 核心亮点  
1. 1  
多扫描引擎编排  
    通过命令行参数组合一键调度Nuclei、Fscan、AWVS、Ffuf，无需手动切换工具完成目录爆破与漏洞验证。实测中只需执行nohup python3 laoyue.py -d target.com -m -f -n -a  
即可串行启动全量扫描，避免重复配置环境变量。  
  
1. 2  
双模式资产发现  
    支持主动扫描（-d参数指定域名）和被动收集（-N模式导入历史URL），适配不同信息收集场景。虽然主域名收集接口已移除需自备初始资产，但子域发现与Host碰撞能力完整保留，适合已有资产清单的批量监控。  
  
1. 3  
自动化运维兜底  
    内置check_nohup_size.sh  
脚本监控nohup.out文件变化，检测到扫描卡死自动重启任务。配合nohup  
命令挂后台运行，可实现VPS长期无人值守的自动化SRC监控，适合  
7×24小时持续资产巡航。  
  
## 🛠️ 技术优势  
  
<table><thead><tr style="border: 0;background-color: transparent;"><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">技术/特性</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;font-weight: 800;background-color: #FFD93D;color: #1a1a1a;text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section><span leaf="">优势</span></section></th></tr></thead><tbody><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Python3驱动</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">跨平台脚本架构</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">兼容CentOS7/Ubuntu20，部署成本低</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">多工具集成</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Nuclei+Fscan+AWVS+Ffuf组合</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">覆盖目录爆破、主机扫描、Web漏洞全场景</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">空间测绘API</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">FoFa/Shodan等数据融合</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">资产发现维度广，减少手工收集工作量</span></section></td></tr><tr style="border: 0;background-color: #FFF9C4;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">定时保活机制</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">检测nohup.out文件变化</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">防止扫描进程僵死，保障自动化连续性</span></section></td></tr><tr style="border: 0;background-color: transparent;"><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">Excel报告生成</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">统一格式数据汇总</span></section></td><td style="font-size: 15px;border: 2px solid #1a1a1a;padding: 12px 16px;text-align: left;color: #2d2d2d;font-weight: 600;min-width: 85px;"><section><span leaf="">方便直接提交SRC平台，简化报告流程</span></section></td></tr></tbody></table>  
## 📖 使用指南  
  
①   
准备工作：克隆仓库到VPS，根据系统选择执行build_centos7.sh  
或build_ubutu.sh  
安装依赖，在config.ini  
中配置FoFa、Shodan等API密钥及钉钉通知Key。  
  
②   
核心操作：单域名扫描使用-d example.com  
，多域名导入文本使用-d "src.txt"  
，按需组合-m  
（Ffuf）、-f  
（Fscan）、-n  
（Nuclei）、-a  
（AWVS）参数启动对应引擎；被动模式添加-N  
标志手动导入URL资产。  
  
③   
结果查看：扫描完成后查看./result/baolumian/  
目录下的Ex  
cel总表，按暴露面资产、敏感信息、漏洞分类筛选有效发现，直接用于SRC平台提交。  
  
📖 项目地址  
  
```
https://github.com/Soufaker/laoyue
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
  
<table><thead><tr style="border-width: 0px;border-style: initial;border-color: initial;background-color: transparent;"><th data-colwidth="100.33333333333333" width="100.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyBdiau5GC7dWricMbXhF76xhhbcjia7Uj6987eBmBe6ov5ibhib2lJP6qmicTbz2zK2ObzgicE7kqY83MVGqJwTgJnIEbfXAkgGykAl8/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="1.306474820143885" data-w="695" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;" data-cropselx1="0" data-cropselx2="21" data-cropsely1="0" data-cropsely2="31" data-backw="0.7272800000000004" data-backh="0.7272800000000004" data-imgfileid="100002876" data-aistatus="1"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img alt="img" class="rich_pages wxw-img" data-aistatus="1" data-backh="19.72728" data-backw="32.72728" data-imgfileid="100002878" data-ratio="0.625" data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&amp;from=appmsg" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;"/></section></th><th data-colwidth="89.33333333333333" width="89.33333333333333" style="border-width: 2px;border-color: rgb(26, 26, 26);padding: 12px 16px;text-align: left;background-color: rgb(255, 217, 61);text-transform: uppercase;letter-spacing: 0.02em;font-size: 14px;min-width: 85px;"><section nodeleaf=""><img data-src="https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&amp;from=appmsg" alt="img" class="rich_pages wxw-img" data-ratio="0.9768518518518519" data-w="1080" style="display: block;margin: 32px auto;border-radius: 4px;border-width: 4px;border-style: solid;border-color: rgb(26, 26, 26);box-shadow: rgb(26, 26, 26) 8px 8px 0px;background: none rgb(255, 255, 255);padding: 8px;transform: rotate(-1deg);transition: transform 0.3s;width: 100%;height: auto;" data-backw="32.72728" data-backh="31.72728" data-imgfileid="100002877" data-aistatus="1"/></section></th></tr></thead></table>  
  
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
  
