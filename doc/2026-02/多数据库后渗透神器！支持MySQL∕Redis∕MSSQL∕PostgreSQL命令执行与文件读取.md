#  多数据库后渗透神器！支持MySQL/Redis/MSSQL/PostgreSQL命令执行与文件读取  
0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-14 08:32  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzrWHOiatXaxWFA0AqutoKGE5NPtqh9f4VAINbwfQ2knz44Aa85ZnKXrVPFibXHJzsDoMAvOdxRwUia04hPMDKk0G7iamibn2MVoI9E/640?wx_fmt=png&from=appmsg "")  
# 🦜 Turacos  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
> **项目地址在文章底部哦**  
  
  
  
**多数据库安全评估工具 | 后渗透辅助 | 企业级安全测试**  
## 📖 项目简介  
  
**Turacos**  
 是一款专业的多数据库安全评估工具，支持 **PostgreSQL、MySQL、Redis、MSSQL**  
 等多种数据库的后渗透操作。 为安全研究人员提供系统化、模块化的数据库安全测试能力，助力企业安全评估与漏洞验证。  
## ⚠️ 法律声明  
### 🛡️ 免责声明  
  
**本工具仅供个人安全研究与学习用途。请勿用于非法活动！ 由于传播、使用本工具而造成的任何后果与损失，均由使用者本人承担。**  
## 🎯 功能特性  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">功能模块</span></strong></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">🐬 MySQL</span></strong></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">🟥 Redis</span></strong></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">🗄️ MSSQL</span></strong></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">🐘 PostgreSQL</span></strong></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">命令执行</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">任意文件读取</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">🚫</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">脚本加载</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">✅</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">数据浏览</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">✅</span></section></td></tr></tbody></table>  
## 🚀 快速开始  
### 📦 环境要求  
- Java **17+**  
  
- 数据库支持：  
  
- PostgreSQL **9.0+**  
  
- MySQL **5.7+**  
  
- Redis **4.0+**  
  
- MSSQL **2012+**  
  
### 🧩 使用方法  
```
# 克隆项目git clone https://github.com/alanni-tom/Turacos.git# 进入目录并编译cd turacosmvn clean package# 运行工具, 这里需要加载 javafx sdk模块java -jar Turacos-1.0-SNAPSHOT.jar
```  
### 🚀 项目预览  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyiaSbpAe7n3usoGI57h60ibAWU4M7T9nk5GsSicP3CmhAXcbQlSicwRUYErmLjCGI8VrEDsFDKe4ic1m4hk43Y1TgCsiaUeu1ZKFwWY/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzxL9OV5HJjanCtjKGapyU5MnRBNtmZicj4Zic2Xd8ZNo7SPIwzcYib7uVBtVO6LicO8icuqZMgDHUju80uPJ0UMhq541XHLAKibo5Hg/640?wx_fmt=png&from=appmsg "")  
  
  
## 📖 项目地址  
```
https://github.com/EdinLyle/Turacos?tab=readme-ov-file
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
  
