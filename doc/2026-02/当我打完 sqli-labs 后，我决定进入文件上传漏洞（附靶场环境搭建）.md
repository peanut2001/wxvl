#  当我打完 sqli-labs 后，我决定进入文件上传漏洞（附靶场环境搭建）  
原创 武文学网安
                        武文学网安  武文学网安   2026-02-09 19:27  
  
# 大家好，我是武文。  
  
从零基础学习网络安全，到现在基本完成 sqli-labs 的练习。  
  
很多人会问：  
  
👉 SQL 注入学完之后，该学什么？  
  
我自己也经历了一段迷茫。  
  
直到我重新整理了一次渗透流程，才发现：  
  
SQL 注入只是 Web 安全的一部分。  
  
真正的攻击路径往往是：  
```
信息收集 → SQL注入 → 文件上传 → 获取Webshell → 权限控制

```  
  
于是，我决定进入下一阶段：  
  
**文件上传漏洞学习。**  
  
但这次，我不会只看理论。  
  
我要从靶场实战开始。  
# 一、为什么选择文件上传作为下一步  
  
原因其实很简单：  
## 1️⃣ 更接近真实攻击路径  
  
SQL 注入更多停留在数据库层。  
  
而文件上传开始接触：  
- Web服务器  
  
- 文件执行权限  
  
- 系统配置  
  
这是从「数据层」迈向「系统层」。  
## 2️⃣ 学习曲线非常自然  
  
很多概念和 SQL 注入是互通的：  
- 绕过验证  
  
- 构造Payload  
  
- 权限判断  
  
只是攻击点不同。  
## 3️⃣ 几乎所有渗透路线都会遇到  
  
真实环境中：  
  
上传漏洞经常成为最终突破口。  
# 二、我将使用哪些靶场进行练习  
  
这里不是随便选。  
  
我筛选标准是：  
- 新手友好  
  
- 真实环境模拟  
  
- 社区资料丰富  
  
## ✅ 第一阶段：Upload-Labs（主力靶场）  
  
这是国内学习文件上传最经典靶场。**upload-labs是一个使用php语言编写的，专门收集渗透测试和CTF中遇到的各种上传漏洞的靶场。旨在帮助大家对上传漏洞有一个全面的了解。目前一共20关，每一关都包含着不同上传方式。**  
  
特点：  
- 专门针对上传漏洞  
  
- 难度逐步提升  
  
- 涵盖常见绕过方式  
  
GitHub：  
```
https://github.com/c0ny1/upload-labs


```  
  
为什么选它：  
  
👉 和 sqli-labs 非常类似，适合你的学习习惯。  
## ✅ 第二阶段：DVWA（辅助练习）  
  
DVWA 不只是 SQL 注入。  
  
它也包含文件上传模块。  
  
优势：  
- 不同安全等级  
  
- 可以观察源码  
  
适合：  
  
👉 对比不同防护方式。  
## ✅ 第三阶段：Vulnhub 靶机（真实环境感）  
  
等基础熟练后。  
  
开始进入：  
- 完整渗透流程  
  
- 多漏洞组合  
  
# 三、靶场环境搭建（最简单方案）  
  
这里是我采用的方式。  
  
目标：  
  
👉 不折腾环境，快速开始学习。  
## Docker（推荐长期使用）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAzcG9Ld4UF5jG2oia1BboDam4J4RTzAcuF19NhMQ2OuF5VAqJyZlbDiaKn1QL04IVYgUhiaVAZKXuD9daNpF1aum5GxTL1Z0S0qVM/640?wx_fmt=png&from=appmsg "")  
## 直接在搜索栏搜索upload-labs就会直接出来镜像文件，点击pull按钮静待按照完成即可。  
  
优点：  
- 环境干净  
  
- 一键启动  
  
pull镜像后，点击run即可进入环境  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAxWAc09Q5ibUr1zcY2Xm1cGvgBgBbbyNcqno5WstfxjJicaY3O5sIW0dWYjnA4bcrUDgxfUqDvSLp2o2Ony1GBOAIyicvqfpBa8oM/640?wx_fmt=png&from=appmsg "")  
  
我这里填了0，表示随机映射一个端口到容器80端口。使用命令docker ps可以看到当前容器映射的端口：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAyibLicQIl6wVvn0EYICvck1MSrCerNoD2D8445icZApQbpk2yEMQuHgRfpkUichIhB4mTU4hDIFMbkYiaky9KHSRUTpDtj5W05HqIg/640?wx_fmt=png&from=appmsg "")  
  
访问：  
http:  
//localhost:32768  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAzjc0eD6xN5UJyeUoAUNKlHTiaVghhZ7icwc1b8skYJ2BkiandwR9Mdq2FlTy8ztS3EJ63icHvuxHZxLFUMSMS59yFHiam3sSSAEl10/640?wx_fmt=png&from=appmsg "")  
  
可以看到环境已经安装完成。  
  
  
四、很多新手没意识到的一件事  
  
上传成功 ≠ 攻击成功。  
  
很多情况下：  
- 文件可以上传  
  
- 但不能执行  
  
原因可能是：  
- Web服务器限制  
  
- 文件权限  
  
- PHP解析规则  
  
这也是我下一阶段重点研究的内容。  
# 五、接下来我的学习计划  
  
计划如下：  
  
1️⃣ 了解服务器如何处理上传文件  
2️⃣ 文件验证机制有哪些  
3️⃣ 为什么有些 Webshell 无法执行  
4️⃣ 如何判断上传是否真正成功  
# 结语  
  
完成 sqli-labs 后，我才真正意识到：  
  
网络安全不是一个漏洞，而是一条路线。  
  
SQL 注入只是起点。  
  
下一站，是文件上传。  
  
新的坑，新的认知升级。  
  
继续记录。  
  
  
