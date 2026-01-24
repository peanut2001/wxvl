#  漏洞扫描神器-xray从入门到放弃  
原创 大表哥吆
                        大表哥吆  kali笔记   2026-01-24 02:53  
  
> 今天给大家介绍一款牛叉的漏洞扫描工具xray  
的安装及简单使用。喜欢就点赞收藏吧！  
  
### 特性  
- 检测速度快。发包速度快; 漏洞检测算法效率高。  
  
- 支持范围广。大至 OWASP Top 10  
通用漏洞检测，小至各种 CMS 框架 POC，均可以支持。  
  
- 代码质量高。编写代码的人员素质高, 通过 Code Review  
、单元测试、集成测试等多层验证来提高代码可靠性。  
  
- 高级可定制。通过配置文件暴露了引擎的各种参数，通过修改配置文件可以客制化功能。  
  
- 安全无威胁。xray  
定位为一款安全辅助评估工具，而不是攻击工具，内置的所有 payload  
 和poc  
均为无害化检查。  
  
### 下载安装  
  
xray  
跨平台支持，根据我们所需，按系统下载即可。需要注意的是xray  
并不开源。这里我们以kali为例。访问项目地址：https://github.com/chaitin/xray/releases  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibya9UdbUMFr79aCkbRlibbliaiacQApZUXStldam1JVlMhBLjS76vGffWzsA/640?wx_fmt=png "")  
选择对应的版本 使用 unzip  
命令解压，就可以得到xray_linux_amd64  
 文件了。  
  
然后运行 ./xray_linux_amd64  
 即可查看 xray  
的版本号。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyacCmT3UDcXrZSqfjNUAnDpd4jlVEcUGwbrTydyMP0aEpC4hEKeQcMKg/640?wx_fmt=png "")  
### 使用代理模式漏洞扫描  
  
代理模式下的基本架构为，扫描器作为中间人，首先原样转发流量，并返回服务器响应给浏览器等客户端，通讯两端都认为自己直接与对方对话，同时记录该流量，然后修改参数并重新发送请求进行扫描。  
#### 生成https证书  
  
对于https网站，我们必须先要配置证书。不然无法代理（和burp类似） 运行./xray_linux_amd64 genca  
 即可生成 ca 证书，保存为 ca.crt  
和 ca.key  
两个文件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyafULGxdJnyMc5jy3t2OV0flI6n7IR8MvT9qQchibic27CHMpibCl4z0Ieg/640?wx_fmt=png "")  
kali中默认的是FireFox 浏览器，我们在FireFox 浏览器中导入证书。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaOg66CtD3CHzoicYibtsc8YFWROpAB9iaFqo6QqNOniatqJrdgUQCWVibpFg/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyac8uXulJ2UaQiaI0bia1nG8kX0QaUmTk7kwr3T94trVtC0wLpLdH6GBCQ/640?wx_fmt=png "")  
#### 启动代理  
  
在扫描之前，我们还需要做一些必要的设置  
  
第一次启动 xray 之后，当前目录会生成 config.yml  
文件，选择文件编辑器打开，并按照下方说明修改。  
  
mitm 中 restriction  
 中 hostname_allowed  
 增加 你的目标域名。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyapVNzPKW33S0qd2ibUesic6lRict72j98b2teu4l7KlEmzBTspCM2Wibngg/640?wx_fmt=png "")  
#### 配置浏览器的代理  
  
和burp一样，设置代理。端口随意。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaUXusuIlRKnz5gMtPNErF7UrZuP8boetw2FcvdjYdicVtSXy1kGiaZPaA/640?wx_fmt=png "")  
#### 开始扫描  
```
./xray_linux_amd64 webscan --listen 127.0.0.1:7777 --html-output xray-testphp.html
```  
  
执行上诉命令后，我们在浏览器中访问目标域名，这时在xray  
中便可以获取到数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaic5ick7mWD6gTut4vf7FJS3Fmoxa9Rp1wbDpiaCqf7kS9uuKVYQEezPgQ/640?wx_fmt=png "")  
  
完成后，我们可以查看扫描报告  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaPiaov2bthR5cHPHicaB6GLvJO25CFNrKXtfo8LoeD6mkJria6BQ2Wun5g/640?wx_fmt=png "")  
### 对目标爬虫  
```
./xray_linux_amd64 webscan --basic-crawler https://bbskali.cn/ --html-output xray-crawler-testphp.html
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyad13KlRxY4DS8V28vcfkYLXOgGWAt8exIWUwu2rqE50O4K9jgGeAgYg/640?wx_fmt=png "")  
### 使用 Burp 与 xray 进行联动  
  
首先 xray 建立起 webscan 的监听  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyazFOofBOfGUC5esQJRhPvZ2yDibk17treRicRuNKKyNH3HBaQVQdOWVxw/640?wx_fmt=png "")  
进入 Burp  
后，打开 User options  
 标签页，然后找到 Upstream Proxy Servers  
设置。  
  
点击Add  
添加上游代理以及作用域，Destination host  
处可以使用*  
匹配多个任意字符串，?  
匹配单一任意字符串，而上游代理的地址则填写xray  
 的监听地址。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaG1hSQ6PI10D6ib1icZeVmSm3sBiaESN70ibIjib15ABQ5nx3ibglib1U6c6RA/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaxBZ8EpkeIP86r9eicGFSk4vias4FSqs2OpDZfJse1AU3wIxqljjLrTQw/640?wx_fmt=png "")  
这样两者便可以保持联动了。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Xb3L3wnAiatiaCxx8MlQXg9ohYEozxAibyaZPJUQ3zVQh0DN4DTZpvMew3fdA7FgM2TFZvvI5wOBxib2eQOKdeF3Fg/640?wx_fmt=gif "")  
  
喜欢本文就 再看 分享吧😘  
  
**更多精彩文章 欢迎关注我们**  
  
  
