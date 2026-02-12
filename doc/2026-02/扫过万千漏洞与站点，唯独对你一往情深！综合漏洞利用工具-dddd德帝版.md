#  扫过万千漏洞与站点，唯独对你一往情深！综合漏洞利用工具-dddd德帝版  
原创 lemonlove7
                    lemonlove7  鹏组安全   2026-02-12 01:13  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0YvAy5BgkyNJe4vC6qtyDX3vcGgiameZcOwiaYlDgwuutJUicHD1ZWicn2T6WTuuiaLvsAcnHBq2a4f6LkwqGtGOuxw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
扫过万千漏洞与站点，唯独对你，一往情深！  
  
原版：  
https://github.com/SleepingBag945/dddd  
  
你是我心动最原本的模样，未经修饰，却一眼难忘。  
  
一款使用简单的批量信息收集,供应链漏洞探测工具，旨在优化红队工作流，减少伤肝的机械性操作。支持从Hunter、Fofa批量拉取目标  
```
自动识别输入类型，无需手动分类
便于拓展的主动/被动指纹识别
指纹支持复杂 与/或/非/括号 逻辑运算。人类友好。
Nuclei v3支持
便于拓展的指纹漏洞映射数据库，尽量避免无效发包
高效的子域名枚举/爆破，精准的泛解析过滤
Hunter、Fofa、Quake支持
Hunter 低感知模式
低依赖，多系统开箱即用
高效的HTML报表，包含漏洞请求响应
审计日志，敏感环境必备
```  
  
最初形态：[网络安全之攻防：蓝队自查-红队一把梭哈DDDD二开【文末获取】](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491526&idx=1&sn=9b6c20183010082a13265bd773e94c98&scene=21#wechat_redirect)  
  
  
在所有相遇之前，你已是我心动最初的形态。  
  
增加的功能优化如下：  
```
1、修复主动指纹识别误报率
2、爬取js获取路径进行判断
   2.1、JS目录爆破识别（识别更多重点资产）
   2.2、JS敏感信息提取
3、蜜罐检测
4、poc检测
5、修复bug：修复mysql爆破失败的问题
6、指纹新增：遇到新的指纹就会进行增加
```  
  
雏形：[内网渗透利刃&外网打点神器：dddd-jb扫描器更新](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491551&idx=1&sn=70b6b25e12aa5bbde32e7e9fa40827dc&scene=21#wechat_redirect)  
  
  
我所有关于喜欢的雏形，都在遇见你那天慢慢成型。  
```
1、增加了xray的调用（缝合），将存在漏洞的结果也写入之前的报告中
2、增加web界面，方便配置更直观，每次启动随机密码
   2.2、新建扫描：可以建立新的工作流（比如单个poc验证、子域名联动+js爬取+xray联动），可自己新建删除，方便配置，快捷方便
   2.3、扫描任务：可以查看建立扫描的情况，有哪些已完成、哪些在扫描中，也可以停止在扫描的任务
   2.4、日志：在扫描任务处点击任意一个即可查看日志，方便部署在服务器上，通过web界面查看扫描日志  
   2.5、规则管理：可在此进行poc管理(新增、编辑)、指纹管理(编辑)、Workflow 管理(添加了poc需要将对应指纹和poc填写到此处)、目录管理(主动指纹识别需要添加的扫描路径)   
        新建poc(保存的时候会自动检测是否存在重复的poc)
   2.6、搜索引擎：配置好fofa、hunter、Quake等即可使用，搜索出来的结果可一键导入到新建扫描中
3、增加较新的poc，如：FineReport 帆软报表前台远程代码执行、友加畅捷管理系统文件上传、万维盈创污染源在线监控系统注入....
4、内网扫描杀器：直接运行dddd单文件即可,无需其他的文件，会调用内置的规则,除了xray无法调用其他正常使用  
```  
  
心动(目前)  
  
从遥遥无期到朝夕在意，从朦胧雏形到如今，满心都是你。  
```
1、加强js扫描规则，避免漏掉隐形资产
2、修复了在web界面中点击了规则管理下的目录管理后切换到其他界面也会显示的问题
3、poc列表按时间和名称排序
4、子域名枚举：开启子域名枚举后，无论输入是主域名还是 URL，都会对其注册域进行枚举。
```  
  
5、增加对存储桶的识别以及安全漏洞检测  
  
探测需要加上-js参数(可能会存在某些js中)，默认不进行写入和删除的操作，加--oss-safe-mode 会进行写入和删除漏洞检测  
  
阿里云、腾讯云、华为云、亚马逊云、七牛云、青云、又拍云、京东云、金山云、天翼云  
  
目录回溯探测：同一桶下的相同目录，只会被探测一次  
  
如：  
```
/admin/files/1.pdf
/admin/images/1.png
/admin/images/2.png
/admin/images/img/1.png
```  
  
只会探测一次  
```
/、/admin/、/admin/images/、/admin/images/img
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhI1SOicIlanwtbFpYL6gwibS21pPYXdPypqbRKQyuYsLhooA63culchzk91ciaZtPXptzpvER1AHKhM29gjQL3wDuVOE6hNEdiaOicY/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhJX8SBtx7Hkd7Kakkj3laFVlUUhHx9lAYAlAhmxALqR7ic353PGWqHB3UCOwzDRZW4EhokW308hGBXQd7olankeibgGBpbsXpibQI/640?wx_fmt=png&from=appmsg "")  
  
6、报告中增加按指纹进行分类，方便查找特定资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhITMicKD3giaAAnW1l6jaOC58GXsFmAUJicQvYHNgw4q3pzyulERPLMaKWFcBK4fZJHYvyHBRP3xibcS5Auj4QTdPq9piax5E7SuLYE/640?wx_fmt=png&from=appmsg "")  
  
经过实战（最近没有更新的原因：过年前的最后一场攻防演练），成功检出多款扫描器未发现的漏洞，取得阶段性成果，这一刻，真的让我怦然心动。特别是js爬取路径以及敏感信息，省事很多。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhJsre6LrAEnt0p9b1BOZ83iahXiaL4ZNMhxZibR2XTOCO7sGby6zUA24oG70ABdbMu7GzGl3rsko18DotSOhz9zXPNMBRuezfpXAw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhLV6avZibquP8cnx07B6A99v1EZN5lEG1kQjbsspAshLIRGzLKW8oEnJpOGEuj8EcaY9saxCHkaHHibMQq5zaWQMuY0rqNWcQPck/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhJTUxJT6cCdfPCT85JeU3CRiaVsM8RKADOF2dh0VpysiaaY65aHqI2995qQLSaoCuw9Hg3tnhibDfUK7Lo3tQqe0rA0UpUXy1Dibd4/640?wx_fmt=png&from=appmsg "")  
  
后续  
  
从初见雏形的试探，到实战突破的心动，原来真正的热爱，从来都藏在一次次深挖与坚守里。  
```
继续优化，使工具更实用。
包括但不限于：新功能、子域名的检测机制、持续增加poc、根据师傅们的反馈进行更多修改
```  
  
获取方式  
  
关注鹏组安全公众号，发送  
网络安全攻防一把梭哈DDDD获取  
  
[鹏组安全社区站：您身边的安全专家-情报 | 攻防 | 渗透 | 线索 | 资源社区](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491205&idx=1&sn=b212739965f6617c84c89726cc85d50c&scene=21#wechat_redirect)  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyNHF1CWPJ9XSApBFhIGwF5Jh0zD2ySOcHvBkYgicU4xZsqvR3XEjUEnfGKH7ya8TgqCibHpYZKcibDBQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=28 "")  
  
**扫码关注**  
  
**社区**  
  
鹏组安全社区：  
comm.pgpsec.cn  
  
  
专注网络技术与骇客的一个综合性技术性交流与资源分享社区  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyN92OtiagxgUpDAeq8RbcPacH8L82CwLzHtvucDrP1RrgfzeUYY8cS4WHk8niap3jKZzys9wK5oHB9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=29 "")  
  
免责声明  
  
由于传播、利用本公众号鹏组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号鹏组安全及作者不为  
此  
承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
好文分享收藏赞一下最美点在看哦  
  
