#  带 AI 辅助的可视化漏洞扫描工具、支持 POC Nuclei 管理与生成、FOFA/Hunter/Shodan 资产搜索  
ChenChen
                    ChenChen  渗透安全HackTwo   2026-02-27 16:01  
  
0x01 工具介绍  
  
Nuclei_Gui 是一款基于 PyQt5 开发的可视化漏洞扫描工具，以 Nuclei 为核心扫描引擎，整合 AI 辅助能力，让漏洞扫描更高效、更便捷。工具支持 POC 全流程管理，涵盖导入、编辑、测试、同步及 AI 自动生成，大幅降低 POC 使用门槛。同时集成 FOFA、Hunter、Shodan 三大主流资产搜索引擎，可快速检索目标资产并直接导入扫描。Nuclei_Gui 实现全平台兼容，界面简洁直观，兼顾新手易用性与专业需求，助力安全从业者高效完成漏洞扫描、资产测绘与漏洞分析工作。  
  
注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾 #渗透安全HackTwo**  
  
0x02   
功能介绍  
  
✨ 主要特性  
### 仪表盘  
- 扫描统计概览 (总扫描次数、发现漏洞数、POC 数量)  
  
- 漏洞趋势图表  
  
- 最近扫描历史  
  
- 漏洞严重程度分布  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWBJFibaaygqQvibRUziceqdbYQJlNicOzlrVJoImz2IucP2Hpc8n4WWnqgG4GIKKVvFsOC6yxuHBKJ8A6vICKOny5BYSzgeclU0x4/640?wx_fmt=png&from=appmsg "")  
### 漏洞扫描  
- 支持单目标/批量目标扫描  
  
- 可选择多个 POC 模板  
  
- 实时显示扫描进度和结果  
  
- 支持暂停/恢复/取消扫描  
  
- 扫描结果可导出为 CSV/HTML  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVetm5wIoxzCibsntqlwoJXZibMXThicV975sWKysquNDvszxCHROZvOxEXkD6tvJvtBd7icSStydF5WvChkgS84Bf9Bo6qicB1eGNI/640?wx_fmt=png&from=appmsg "")  
### 任务队列管理  
- 多任务排队执行  
  
- 任务优先级设置 (紧急/高/普通/低/后台)  
  
- 断点续扫支持  
  
- 任务状态实时监控  
  
- 显示创建时间、开始时间、耗时  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU8QkL1C10ZILAvwMJ0RkZWB0lT2EfWvrlBVcp0OsMNk1ickdbmrwjF3vO2mpTObTjXm9pgeoMau4zUqIH6HrAkwuQWYg32QSuA/640?wx_fmt=png&from=appmsg "")  
### POC 管理  
- POC 列表浏览和搜索  
  
- 按严重程度/标签筛选  
  
- POC 导入 (文件/目录)  
  
- POC 在线同步 (从 nuclei-templates 官方仓库)  
  
- POC 编辑器 (语法高亮)  
  
- POC 快速测试  
  
- POC 收藏管理  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXNeMv3I5RB9Ir7vGfIeo7bja6DeBCMzKrJ8QJE2nVEj00LoOzNbXDoGWTicEMekepXXwelpeBPIOqKQNZjPQ8vyklYpXaBE1P4/640?wx_fmt=png&from=appmsg "")  
### 资产搜索  
  
支持多个资产搜索引擎：  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">引擎</span></span></span></th><th style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">说明</span></span></span></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">FOFA</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">国内主流资产搜索引擎</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">Hunter</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">奇安信鹰图平台</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">Quake</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">360 网络空间测绘</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">Shodan</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">国际知名搜索引擎</span></span></span></td></tr></tbody></table>- 搜索结果可直接导入为扫描目标  
  
- 搜索历史记录  
  
### AI 助手  
  
支持 OpenAI 兼容接口 (DeepSeek、通义千问、GPT 等)：  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">功能</span></span></span></th><th style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">说明</span></span></span></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">FOFA 语法生成</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">根据漏洞描述生成 FOFA 搜索语法</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">POC 生成</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">根据漏洞描述生成 Nuclei YAML POC</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">漏洞分析</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">深入分析漏洞原理和修复建议</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">智能推荐</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">根据目标特征推荐适用的 POC</span></span></span></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">漏洞报告生成</span></span></span></td><td style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 16px;">生成 SRC 提交格式的漏洞报告</span></span></span></td></tr></tbody></table>###   
  
0x03更新说明  
```
✅ 完全跨平台支持：Windows/macOS/Linux 全平台兼容
✅ 智能系统检测：自动识别操作系统和架构
✅ 内置下载功能：主界面和设置界面集成 Nuclei 下载
✅ 自动路径管理：智能查找和使用正确的 Nuclei 二进制文件
✅ 权限自动设置：Unix 系统自动设置执行权限
✅ 多下载方式：简化版和带进度条版本下载脚本
✅ 跨平台测试：新增测试脚本验证多系统兼容性
✅ 代码优化：清理冗余文件，精简代码库
✅ 文档完善：详细的跨平台支持文档
```  
  
  
0x04 使用介绍  
  
📦安装  
指南  
### 安装 Nuclei 扫描引擎(二选一)  
#### 方法一：手动安装  
1. 访问最新版Nuclei_3.7.0  
  
1. 下载适合您系统的版本并放入   
bin/  
 目录  
  
1. 根据系统重命名文件：  
  
1. **Windows**  
:   
nuclei.exe  
  
1. **macOS**  
:   
nuclei_darwin  
  
1. **Linux**  
:   
nuclei_linux  
  
1. 设置执行权限（Unix 系统）：  
  
```
chmod +x bin/nuclei_darwin  # macOS
chmod +x bin/nuclei_linux   # Linux
```  
#### 方法二：系统安装  
  
如果您已经在系统中安装了 Nuclei，程序会自动使用系统版本：  
```
# macOS (使用 Homebrew)
brew install nuclei
# Linux (使用包管理器)
sudo apt install nuclei  # Ubuntu/Debian
# 或者直接下载到系统路径
sudo wget -O /usr/local/bin/nuclei https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei_linux_amd
sudo chmod +x /usr/local/bin/nuclei
```  
  
### 安装依赖  
```
pip install -r requirements.txt
```  
  
  
### 启动程序  
  
  
**Windows**  
：  
```
python main.py
# 或双击 Run_Nuclei_GUI.bat
```  
  
**macOS/Linux**  
：  
```
python3 main.py
```  
##   
  
  
**0x05 内部VIP星球介绍-V1.4（福利）**  
  
          
如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，  
**每天更新1day/0day漏洞刷分上分****(2026POC更新至5312+)**  
**，**  
包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**  
。shadon/Zoomeye/Quake/  
Fofa高级会员/  
AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"   
**星球**  
 "有优惠券名额有限先到先得  
**❗️**  
啥都有  
**❗️**  
全网资源  
最新  
最丰富  
**❗️****（🤙截止目前已有2500+多位师傅选择加入❗️早加入早享受）**  
  
****  
最新漏洞情报分享：  
https://t.zsxq.com/VuWGw  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20260228获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.5（AI自动化）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.全新升级BurpSuite2026.2专业(稳定版)**  
  
**4. 最新xray1.9.11高级版下载Windows/Linux**  
  
**5. 最新HCL AppScan Standard**  
  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
  
上一篇文章：  
[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)  
  
  
