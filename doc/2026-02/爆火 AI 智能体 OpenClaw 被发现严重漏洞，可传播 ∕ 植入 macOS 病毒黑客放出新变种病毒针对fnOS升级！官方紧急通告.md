#  爆火 AI 智能体 OpenClaw 被发现严重漏洞，可传播 / 植入 macOS 病毒|黑客放出新变种病毒针对fnOS升级！官方紧急通告  
 黑白之道   2026-02-06 01:18  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
  
**关键词**  
  
  
  
AI、恶意软件  
  
  
密码管理工具 1Password 于 2 月 2 日发布博文，其安全团队发现有攻击者利用爆火 AI 智能体 OpenClaw（原名 Clawdbot 和 Moltbot），向 macOS 用户散播和植入恶意软件。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHpJgk3TAht66KCusicWt9kwJXdgMNou0qhvxw1gTYquHNqKTRgJpV4TtgXTRQ26IicBsJHzOJiaxEUKFwibGZwjE6aCuC6je0Xiazc/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=1 "")  
  
注：OpenClaw 是一个近期爆火的 AI 智能体，核心竞争力在于其 " 主动自动化 " 能力。该 AI 智能体无需用户发出指令，即可自主清理收件箱、预订服务、管理日历及处理其他事务。同时，它具备强大的记忆功能，能够保存所有对话历史，并从过往的对话片段中精准回调用户的偏好设置。  
  
攻击者利用了 OpenClaw 的 " 技能 "（Skills）文件，这些通常为 Markdown 格式的文件本用于指导 AI 学习新任务，**却被黑客伪装成合法的集成教程。**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljRMAYtDftYGPEJRsxwCSat6sOUga3IRib8xSK0ib37sibRLqazpZd19QvVIYlZfvibExicCOXzGx8TiaIw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=2 "")  
  
在看似常规的设置过程中，文档会诱导用户复制并运行一段 Shell 命令。该命令会在后台解码隐藏载荷、下载后续脚本，并修改系统设置以移除 " 文件隔离（Quarantine）" 标记，从而成功躲避 macOS 内置的安全检查。  
  
植入系统的有效载荷被确认为 " 信息窃取类（Infostealer）" 恶意软件。与传统破坏系统的病毒不同，该恶意软件专注于静默窃取高价值数据，包括浏览器 Cookie、活跃登录会话、自动填充密码、SSH 密钥以及开发者 API 令牌。对于开发人员而言，这意味着攻击者可能借此渗透至源代码库、云基础设施及企业 CI / CD 系统，造成连锁式的数据泄露。  
  
尽管部分开发者寄希望于 " 模型上下文协议（MCP）" 来限制 AI 权限，但事实证明该协议在面对此类攻击时形同虚设。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHzoncl5Yh6onursqaddbkSmtWvHT5uw8uvJ8la6sQARjfYPYHptqlick5WAAJUd1cHwYVAq0Gib84iay3XicYqbUT8zaAND0k58iaA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
由于攻击本质上是利用文档进行社会工程学欺诈，而非直接调用工具接口，因此可以轻易绕过协议边界。同时，此次攻击显示黑客对 macOS 的防御体系极为熟悉，单纯依赖苹果系统的环境隔离已无法有效阻断此类威胁。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGIibMDYic3nOE3HCLrmlFA1ueiaFssM3Toj0UxUYJIGp8YkMnliafoUEhB8zCuv7MDIlF8VDIlmRiatTNh2IRzmPa0jxibiaZFd8yF5c/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
**关键词**  
  
  
  
黑客  
  
  
日前，飞牛fnOS被曝出现重大安全漏洞引发业内和用户关注。  
  
今日，飞牛安全应急响应团队发布紧急安全通告，称昨日发布1.1.18安全更新后，大规模入侵行为已初步遏制。  
  
但攻击者针对OTA升级机制进行了对抗性升级，在官方发布查杀更新后，  
**黑客组织明显活跃，病毒已出现新变种，部分受感染设备的系统更新服务被恶意破坏，导致无法正常接收修复补丁。**  
  
与此同时，官网、社区、官方域名等也在持续承受不同程度的DDOS攻击。  
  
此次组合攻击呈现高度组织化、针对性的特征，攻击方正在根据防御动态持续调整策略。  
  
对于更新服务已损坏且未完成升级的受感染设备，存在被持续控制的重大风险。  
  
为降低设备风险，**飞牛提供以下修复建议，用户可按照自身情况，选择对应处理方式，尽快替换到最新系统。**  
  
**针对无法通过OTA升级的设备**  
  
建议可从官网下载1.1.18完整系统镜像进行重装，目前系统1.1.18镜像已上架官网：https://www.fnnas.com/download  
  
fnOS采用存算分离架构设计，重装仅替换系统分区，存储池数据可完全保留。  
  
重装后重新挂载即可恢复数据访问，存储空间不受该木马影响，此方案可以有效解决当前风险。  
  
**针对已经更新或者遇到异常情况的设备**  
  
目前提供了官方紧急验证查杀脚本，可以自行验证。  
  
curl -L https://static2.fnnas.com/aptfix/trim-sec -o trim-sec && chmod +x trim-sec && ./trim-sec  
  
该脚本连接云端病毒库，可识别并清除已知变种，官方也会随病毒特征变化实时更新规则。  
  
**针对暂时无条件进行更新或者重装的设备**  
  
建议立即断开设备公网连接或关机，防止设备成为僵尸网络节点或遭受进一步破坏。  
  
**针对已经完成更新，但是功能使用出现异常的设备**  
  
建议进入系统设置，使用系统修复功能，进行修复，该工具会强制校验并修复关键系统文件，恢复设备使用。  
  
此外，飞牛官方表示，注意到存在第三方人员恶意利用已公开漏洞，对未升级设备实施入侵的情况。  
  
此类行为已涉嫌破坏计算机信息系统罪，公安机关和国家通信部门已介入此类案件调查并固定相关证据，移交公安机关网络安全部门处理。  
  
![飞牛NAS用户注意！黑客放出新变种病毒针对fnOS升级 官方紧急通告](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0FbeQBMPx0ps7bJux9r2G6y8N3IybYXDI02Z57eickicHuG5C7tX7TibcnhRE7KrgOTiaaVKofAH9bw/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1 "")  
  
> **文章来源 ：安全圈**  
  
  
**精彩推荐**  
  
  
  
  
# 乘风破浪|华盟信安线下网络安全就业班招生中！  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575781&idx=2&sn=ea0334807d87faa0c2b30770b0fa710d&chksm=83bdf641b4ca7f5774129396e8e916645b7aa7e2e2744984d724ca0019e913b491107e1d6e29&scene=21#wechat_redirect)  
  
  
# 【Web精英班·开班】HW加油站，快来充电！  
  
  
‍[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650594891&idx=1&sn=b2c5659bb6bce6703f282e8acce3d7cb&chksm=83bdbbafb4ca32b9044716aec713576156968a5753fd3a3d6913951a8e2a7e968715adea1ddc&scene=21#wechat_redirect)  
  
  
‍  
# 始于猎艳，终于诈骗！带你了解“约炮”APP  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575222&idx=1&sn=ce9ab9d633804f2a0862f1771172c26a&chksm=83bdf492b4ca7d843d508982b4550e289055c3181708d9f02bf3c797821cc1d0d8652a0d5535&scene=21#wechat_redirect)  
  
**‍**  
  
  
