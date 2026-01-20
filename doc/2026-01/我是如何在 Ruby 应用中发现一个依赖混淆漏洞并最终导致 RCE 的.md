#  我是如何在 Ruby 应用中发现一个依赖混淆漏洞并最终导致 RCE 的  
haidragon
                    haidragon  安全狗的自我修养   2026-01-20 08:29  
  
# 官网：http://securitytech.cc  
  
  
大家好，我又带着新的安全发现回来了。  
  
今天我想分享一个我发现的非常有意思的 **依赖混淆（Dependency Confusion）漏洞**  
，并且最终成功实现了 **远程代码执行（RCE）**  
。  
  
泡杯咖啡，我们开始吧 ☕  
## 理解目标  
  
和大多数漏洞赏金一样，一切从信息收集开始。  
  
我通过以下方式审计目标：  
- 浏览他们的 GitHub 公共仓库  
  
- 分析技术栈  
  
- 理解依赖管理方式  
  
在查看公开代码时，我注意到他们大量使用 **Ruby**  
。这让我开始好奇 Ruby 的依赖是如何管理的，是否存在由于配置错误而暴露的内部包。  
## 什么是 Ruby Gem？  
  
**Ruby Gem**  
 是 Ruby 的包或库，用于共享和复用代码。  
  
开发者不需要重复造轮子，可以直接依赖 gem 来实现框架、工具和内部功能。  
  
**Gem 分两种：**  
- **公共 Gem**  
：托管在 RubyGems.org，任何人都能下载  
  
- **私有 / 内部 Gem**  
：托管在公司私有服务器，只允许员工访问  
  
公司通常创建内部 gem 来保护业务逻辑和内部工具。  
## 什么是依赖混淆？  
  
依赖混淆（也叫替换攻击）是指：  
  
公司内部使用了一个私有包名，而攻击者在公共仓库注册了一个**同名包**  
。  
  
如果包管理器配置错误，就可能优先安装攻击者的包。  
  
如果攻击者发布一个很高的版本号，比如：  
```
90002.0
```  
  
包管理器就会认为它是最新版本。  
> 这个问题不仅存在于 Ruby，也影响 npm、pip、Maven、NuGet 等生态。  
  
## 经典攻击方式  
  
Gemfile 示例：  
```
source 'https://rubygems.org'source 'https://internal-gems.company.com'gem 'rails'gem 'internal-gem'
```  
  
Bundler 会从：  
- rubygems.org  
  
- internal-gems.company.com  
  
同时拉取。  
  
由于 internal-gem  
 没指定来源，Bundler 允许从任意源解析。  
  
执行 bundle install  
：  
```
Found 'internal-gem' in multiple sources:- rubygems.org: version 90002.0 (攻击者)- internal-gems: version 1.0 (公司真实)Bundler 选择最高版本 → 安装恶意 gem
```  
  
安装时，恶意代码会**自动执行**  
。  
## 正确配置方式  
```
source 'https://rubygems.org'gem 'rails'gem 'sidekiq'source 'https://internal-gems.company.com'do  gem 'internal-gem'end
```  
  
这样 Bundler 永远不会从公共仓库解析 internal-gem。  
## 为什么危险  
  
bundle install  
 经常自动运行在：  
- 开发者机器  
  
- CI/CD  
  
- Docker 构建  
  
- 部署阶段  
  
特点：  
- 无需用户操作  
  
- 自动执行  
  
- 容易打入生产链路  
  
## 侦察阶段  
  
使用 ghorg 克隆仓库：  
```
ghorg clone <org> -t <token>
```  
  
提取 Gemfile：  
```
find . -type f -name Gemfile | \xargs -n1 -I{} awk '/^\s*gem / {gsub(/[",'\''()]/, "", $2); print $2}' {} | \sort -u
```  
  
检测哪些 gem 不存在于 RubyGems：  
```
xargs -n1 -I{} httpx -silent -status-code -mc 404 "https://rubygems.org/gems/{}"
```  
  
404 表示公共仓库没有该包。  
## 构建 PoC  
### 创建恶意 Gem  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2z96U2qh07mlxliardib91FxsNTqcLsZfjnJqicBj1nccRCPkoEtLJ39hA/640?wx_fmt=png&from=appmsg "")  
  
我创建同名 gem，并将版本设为极高值 90002.0  
。  
### 添加回调代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k26ocjicjcsOF9TWFBjpkXpXmoiciccyRFIkpF3j2EwSdssuibY290EaB3ZQ/640?wx_fmt=png&from=appmsg "")  
  
Ruby gem 在安装阶段即可执行代码。  
  
回调只采集：  
- 主机名  
  
- 用户名  
  
- 时间戳  
  
没有采集任何敏感数据。  
### 设置回调服务器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2FicbibO0ybPG3hoAG44dVicokMo8cJEgzHWIICJQ4l6Eic5OFNic6Q60fCA/640?wx_fmt=png&from=appmsg "")  
  
部署 HTTPS 服务器用于接收回连。  
### 发布到 RubyGems  
```
gem build internal-gem.gemspecgem push internal-gem-90002.0.gem
```  
## 等待命中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k20qxczktxbNHBHmPnZMpz2lfjvYiatL25IGEicRn1Mp7IdtKtmnbOpg4A/640?wx_fmt=png&from=appmsg "")  
  
几天后收到回连。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2uJ9NouVPSribA5hTYvEdRMVkAWud6M2mvSmTOjvCd9yBbZ5ZRNLtsiaQ/640?wx_fmt=png&from=appmsg "")  
  
说明恶意 gem 已在目标环境被安装。  
## 分析回调  
  
结果表明：  
- 主机名是开发者工作站  
  
- 用户名是真实工程师账号  
  
- 不是 CI 或生产服务器  
  
## 真正发生了什么  
  
Ruby 有两种安装方式：  
### Bundler  
- 读取 Gemfile  
  
- 遵守 source  
  
- 使用锁文件  
  
- 更安全  
  
### gem install  
- 忽略 Gemfile  
  
- 使用全局源  
  
- 选择最高版本  
  
- 可被混淆  
  
开发者执行了：  
```
gem install internal-gem
```  
  
从而绕过了 Bundler。  
## 影响  
  
开发者机器通常拥有：  
- 源码  
  
- Token  
  
- SSH Key  
  
- 云权限  
  
- 内网访问能力  
  
因此风险依然很高。  
## 厂商响应  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2l9FUqW6SytYfdkwGNYvmYBQPgkv7mdO3Zdm9NYWh5lTheRg7ycZD3A/640?wx_fmt=png&from=appmsg "")  
  
厂商确认生产与 CI/CD 安全。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2ZYzJFMobztp0kz02DamGib1ibw7LPpZhIibMKC01haFpegXmblkN2RYibA/640?wx_fmt=png&from=appmsg "")  
  
漏洞评级：**HIGH**  
。  
## ✅ 总结一句话  
> **依赖混淆不仅能打生产，也能控制开发者机器，是供应链攻击的重要入口。**  
  
  
  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vBZcZNVQERGfJmnA3VCqnfZQrg5wHmYscC27fKKiba3Kj0N2TSfoAlHicKKYM9zmUaRgNsebCpCMHuTIb9L5CSfQ/640?wxfrom=5&wx_fmt=jpg&watermark=1&tp=webp&wx_lazy=1#imgIndex=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
