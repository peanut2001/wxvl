#  上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-01-28 00:00  
  
# AIxVuln - AI 代码安全审计平台  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
  
  
  
    AI 驱动的代码安全审计平台前端。用户上传源代码压缩包，后端启动 Docker 容器进行漏洞分析，结果通过 WebSocket 实时回传。  
## ✨ 功能特性  
- 📦 **源码上传**  
 - 支持 / 格式，最大 500MB.zip``.tar.gz  
  
- 🔍 **漏洞扫描**  
 - AI 驱动的自动化代码安全分析  
  
- 📡 **实时反馈**  
 - WebSocket 实时推送扫描进度和结果  
  
- 🐳 **容器管理**  
 - 查看审计容器运行状态  
  
- 📊 **报告生成**  
 - 自动生成 Markdown 格式审计报告  
  
- 🌙 **赛博主题**  
 - 深色科技风界面设计  
  
## 📸 截图预览  
  
首页  
  
![图片-20260124195516171](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvU4iaWjDZJcf1tl9ibtIXibaOJFmc2X4szbujKTicAt1u6Or5VgP7XZ2JveQ/640?wx_fmt=png&from=appmsg "")  
  
  
项目详情  
  
![图片-20260124195502477](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUVjogGZPv9FgQaK3yhER1vR49oWhABSia8xB30tO8hEo7kPPZ6JupcqA/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞报告列表  
  
![image-20260124195528933](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUsOty7SD3CkYtURR5mWmhkyC8EVkdmxXqTlsRFdlPhSQAh4qqpSibOcg/640?wx_fmt=png&from=appmsg "")  
  
  
在线预览报告  
  
![图片-20260124195132766](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUpt03ibO1g4t54czGyia225ibcdAM9g2lbkgS7npQ2CibibK6b9GuuFXRZicA/640?wx_fmt=png&from=appmsg "")  
  
  
自动编写 POC 并验证漏洞真实性  
  
![图片-20260124195314511](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvU1PdR4NfPBJr5XlsnW68QGNbQD5lt1Cn2pxcV82oyVHc59DSJF0Plvg/640?wx_fmt=png&from=appmsg "")  
  
![图片-20260124195340464](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUnbNC17XdOaR7NzTNfbBcAHnHxIQ33dNFauxiaIfKLibkKGFoM7VibHhyA/640?wx_fmt=png&from=appmsg "")  
  
## 📊下个版本  
  
![11b17eb3e01e8985db710920b1254c45](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUfcKgDtHnaM8zd9ZEDlE6H7BPawaWfoib0gliaTpiaIqZGczo3ZGrFFVibA/640?wx_fmt=png&from=appmsg "")  
  
![图片-20260127090753141](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUz9pdwUGs8lMyauGkJv5Z5aebyn07Ex4qzWYib0j6IX3ZSiaGKibexHUtw/640?wx_fmt=png&from=appmsg "")  
  
![图片-20260127090531696](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvU7DrEkJTGwhZr6ShZz7Qe38QrtavyQgXibtaibuueVj3PvosL9ibgIfTeg/640?wx_fmt=png&from=appmsg "")  
  
![图片-20260127090552738](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEXnXvur4SbT838vrPhtfvUQ7hodIuEuseDEKNtWnHOycqBWukCIBOPnhdF4Ue00P4d6oFRCc08Kg/640?wx_fmt=png&from=appmsg "")  
## 🛠️ 技术栈  
- **框架**  
：Next.js 16（应用路由器）  
  
- **语言**  
： TypeScript 5  
  
- **样式**  
：Tailwind CSS 4  
  
- **组件**  
： shadcn/ui + Radix UI  
  
- **状态**  
： React Hooks + WebSocket  
  
- **动画**  
： tw-animate-css  
  
## 🚀 快速开始  
### 环境要求  
- Node.js 18+  
  
- NPM / 毛线 / PNPM  
  
### 安装  
```
# 克隆仓库git clone https://github.com/qqliushiyu/AIxVuln_Web.gitcd AIxVuln_Web# 安装依赖npm install# 配置环境变量cp .env.local.example .env.local# 编辑 .env.local 配置后端 API 地址# 启动开发服务器npm run dev
```  
  
打开 http://localhost:3000 查看应用。  
### 环境变量  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">变量名</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">说明</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">示例</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><code><span leaf="">BACKEND_URL</span></code></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">后端 API 地址</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><code><span leaf="">http://localhost:8080</span></code></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><code><span leaf="">NEXT_PUBLIC_WS_BASE</span></code></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">WebSocket 直连地址</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><code><span leaf="">ws://localhost:8080</span></code></td></tr></tbody></table>  
  
  
## 📖 项目地址  
```
https://github.com/kk12-30/KaliGPT
```  
## 💻 威胁情报推送群  
>   如果师傅们想要第一时间获取到**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
>  如果师傅们想要获取  
**网络安全相关知识内容**  
，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**  
。  
  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg "")  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
