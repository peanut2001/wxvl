#  承影 ChYing：支持 Nuclei POC+JWT 爆破 + 403 Bypass，开源渗透利器  
yhy0
                    yhy0  渗透安全HackTwo   2026-02-04 16:01  
  
0x01 工具介绍  
  
  
2023 年 4 月，我在 GitHub 创建了开源项目「承影 ChYing」。名字取自《列子・汤问》中的上古名剑：“将旦昧爽之交，日夕昏明之际，淡淡焉若有物存，莫识其状。其所触也，窃窃然有声，经物而物不疾也。” 我希望这款工具，能像承影剑一般，在渗透测试的明暗之间，成为安全从业者手中隐蔽而锋利的实战利器。  
  
在渗透测试中，一站式、轻量化工具能显著提升实战效率。**承影 ChYing**  
，这款类 BurpSuite 的现代化平台集成流量代理、重放、编解码等核心能力，支持 Nuclei POC 批量检测、JWT 密钥爆破、403 绕过等高频场景，搭配液态玻璃 UI 与流畅交互，兼顾易用性与攻击性，助力安全人员高效完成漏洞挖掘。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6B4iaI4kmJouRypyRU6X84IyrF5YkXrr5eyoegXYG6swyRwGSo9MzJicNkLEv3dMkv0iawIudoxuQKQ/640?wx_fmt=png&from=appmsg "")  
  
注意：  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾 #渗透安全HackTwo**  
  
0x02   
功能简介  
  
  
✨ 主要特性  
  
HTTP 代理 & 流量分析  
- 实时捕获 HTTP/HTTPS 流量  
  
- 智能过滤（按方法、主机、状态码、路径）  
  
- 右键菜单一键发送到 Repeater/Intruder/扫描器  
  
Repeater（重放器）  
- 手动修改请求，反复测试  
  
- 支持多标签页，对比测试更方便  
  
Intruder（入侵者）  
- 自动化攻击测试  
  
- 支持多种 Payload 类型  
  
- 结果实时展示  
  
Decoder（编解码）  
- URL/Base64/Hex/Unicode 一键转换  
  
- MD5/SHA 哈希计算  
  
- 支持链式编解码  
  
插件模块  
- JWT 解析与密钥爆破  
  
- Swagger API 测试（未授权访问、注入检测）  
  
- 403 Bypass  
  
- Shiro 解密  
  
集成 Jie 扫描器  
- 被动流量扫描  
  
- 主动漏洞检测（XSS、SQL 注入、SSRF、命令执行等）  
  
- Nuclei POC 支持  
  
技术栈  
- UI：液态玻璃设计  
  
这次重构最大的变化是 UI。借助 AI 的帮助，我终于实现了心中的设计：  
  
我不是专业设计师，但我希望每天打开这个工具时，心情是愉悦的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6B4iaI4kmJouRypyRU6X84IbtKbwkHHcPgd7vPdic2GWq2qwoQyGGYwHdibcWVvFhytu3TeILEGAhiaA/640?wx_fmt=png&from=appmsg "")  
  
  
- 液态玻璃风格（Glassmorphism）：半透明、模糊背景、柔和阴影  
  
- 深色/浅色主题：护眼，也好看  
  
- 响应式布局：各种分辨率都能用  
  
- 流畅动画：每个交互都有反馈  
  
- 后端：Go（高性能、跨平台）  
  
- 前端：Vue 3 + TypeScript  
  
- 框架：Wails v3（Go + Web 的完美结合）  
  
- 数据库：SQLite（轻量本地存储）  
  
- 扫描引擎：Jie  
  
0x03更新说明  
```
分离构建和发布步骤，避免并行 job 冲突
升级 softprops/action-gh-release 到 v2
使用 artifact 在 job 间传递构建产物
统一在 release job 中创建 release 并上传所有文件
```  
  
  
0x04 使用介绍  
  
📦  
使用指南  
  
Windows 直接双击运行；Linux/macOS 赋予执行权限后启动，首次运行自动配置运行环境  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6B4iaI4kmJouRypyRU6X84IB5Ioo0VHic17By6vOsf5OHQKyQDGm9YlteDibuk29iaN1mfc6xuYeNIOg/640?wx_fmt=png&from=appmsg "")  
###   
  
  
**0x05 内部VIP星球介绍-V1.4（福利）**  
  
        如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，  
**每天更新1day/0day漏洞刷分上分****(2026POC更新至5212+)**  
**，**  
包含全网一些**付费扫描****工具及内部原创的Burpsuite自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**  
。shadon/Zoomeye/Quake/  
Fofa高级会员，CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"   
**星球**  
 "有优惠券名额有限先到先得  
**❗️**  
啥都有  
**❗️**  
全网资源  
最新  
最丰富  
**❗️****（🤙截止目前已有2400+多位师傅选择加入❗️早加入早享受）**  
  
****  
最新漏洞情报分享：  
https://t.zsxq.com/lFN5j  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.4版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20260205获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.4（AI自动化工具）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.全新升级BurpSuite2025.12专业(稳定版)**  
  
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
  
  
