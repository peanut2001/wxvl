#  红队必备POC模板管理漏扫工具(1243POC模板，支持多平台使用)  
0xSecDebug
                    0xSecDebug  0xSecDebug   2026-01-25 04:17  
  
# SerenNP Manager  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
  
  
  
**牛逼的 POC 漏洞检测模板管理工具**  
  
基于 Go + Wails 构建，支持 Windows、macOS、Linux 多平台  
## ✨ 工具使用  
### 仪表盘  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEM3HfiaxhVXEH07N8QcBUYxWC7FcR3sWmElq2LtFzcdWcs6L0z0ibPwDwuicF9NXsvwqmOOmluyvObA/640?wx_fmt=png&from=appmsg "")  
### POC模板  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEM3HfiaxhVXEH07N8QcBUYxRYicIibKLABMac3oJ3huuQDicUZbnODYtrQdZDpw0tdvYEcyQKwRQZ3nQ/640?wx_fmt=png&from=appmsg "")  
### 扫描器  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEM3HfiaxhVXEH07N8QcBUYxvSic999yY4xFicpohjiaEUgMKPllSqEcicgriaY9yDJd20mK3Py9JIYiacSg/640?wx_fmt=png&from=appmsg "")  
### 编码工具  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEM3HfiaxhVXEH07N8QcBUYx1O2ia14vhL5yQ87MQJFdeAXW4Fv5OXeCZictfEVWDdP2cJPDP6b1ic6ibw/640?wx_fmt=png&from=appmsg "")  
## ✨ 功能特性  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">功能</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">描述</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">📁 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">POC 模板管理</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">创建、编辑、删除、导入/导出 Nuclei YAML 模板</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✏️ </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">可视化编辑器</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Monaco 代码编辑器 + 可视化表单双模式</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">🎯 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">漏洞扫描</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">批量目标扫描，实时进度显示</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">📊 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">结果分析</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">按严重程度分类，查看请求/响应详情</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">🔧 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">编码工具</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Base64、URL、Unicode、Hex、AES、MD5、SHA 等</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">🎨 </span><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">现代 UI</span></strong></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">深色主题，流畅动画，响应式布局</span></section></td></tr></tbody></table>  
## 🛠️ 技术栈  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">类型</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">技术</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">版本</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">后端</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Go</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">1.22+</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">桌面框架</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Wails</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">v2.11</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">前端框架</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">React</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">18</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">类型系统</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">TypeScript</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">5.2</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">样式</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">TailwindCSS</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">3.3</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">构建工具</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Vite</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">5.0</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">编辑器</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Monaco Editor</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">4.6</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">加密库</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">crypto-js</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">4.2</span></section></td></tr></tbody></table>  
## 📥 多平台使用  
### 直接下载  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">平台</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">文件</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Windows</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><code><span leaf="">SerenNP-Manager-windows.exe</span></code></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Windows 10/11 64位</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">macOS</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><code><span leaf="">SerenNP-Manager-macos</span></code></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">M1/M2/M3 芯片 Mac</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Linux</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><code><span leaf="">SerenNP-Manager-linux</span></code></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">64位 Linux</span></section></td></tr></tbody></table>  
### 运行说明  
  
**Windows：**  
- 双击 SerenNP Manager.exe  
 运行  
  
- 首次运行可能需要允许 Windows 防火墙  
  
## 🚀 使用指南  
### 1. POC 模板管理  
- **新建模板**  
：POC 模板 → 新建  
  
- **编辑模板**  
：点击模板卡片  
  
- **导入模板**  
：支持导入标准 Nuclei YAML 模板  
  
- **搜索过滤**  
：按名称、分类、严重程度筛选  
  
### 2. 执行扫描  
1. 进入 **扫描器**  
 页面  
  
1. 输入目标 URL（每行一个）  
  
1. 选择 POC 模板  
  
1. 点击 **启动扫描**  
  
1. 实时查看进度和结果  
  
### 3. 查看结果  
- 按严重程度过滤  
  
- 点击 **查看 POC**  
 跳转模板  
  
- 点击 **查看数据包**  
 显示请求/响应  
  
### 4. 编码工具  
  
支持 Base64、URL、Unicode、Hex、HTML、AES、MD5、SHA 等编解码  
## 🔨 从源码编译  
### 环境要求  
- Go 1.22+  
  
- Node.js 18+  
  
- Wails CLI v2  
  
## 📝 模板格式  
  
兼容标准 Nuclei 模板格式：  
```
id: sql-injection-test

info:
  name: SQL Injection Detection
  author: your-name
  severity: high
  description: 检测 SQL 注入漏洞
  tags: sqli,web

http:
  - method: GET
    path:
      - "{{BaseURL}}/search?q=1' AND '1'='1"

    matchers:
      - type: word
        words:
          - "SQL syntax"
          - "mysql_fetch"
        condition: or

```  
## 📁 项目结构  
```
nuclei-poc-manager/
├── main.go              # 应用入口
├── app.go               # 主应用逻辑
├── wails.json           # Wails 配置
├── build/
│   ├── appicon.png      # 应用图标
│   ├── bin/             # 编译输出
│   └── windows/         # Windows 资源
├── internal/
│   ├── models/          # 数据模型
│   ├── poc/             # POC 管理器
│   └── scanner/         # 扫描引擎
├── frontend/
│   ├── src/
│   │   ├── components/  # React 组件
│   │   ├── App.tsx      # 主组件
│   │   └── types.ts     # 类型定义
│   └── package.json
├── templates/           # POC 模板目录
└── .github/workflows/   # CI/CD 配置

```  
  
  
📖 项目地址  
##   
```
https://github.com/InKu0721/SerenNP-manger  #项目地址https://pan.baidu.com/s/14gcq9bhTYAiW98l_Sr2Yew?pwd=akpa  #1243个POC模板
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
  
