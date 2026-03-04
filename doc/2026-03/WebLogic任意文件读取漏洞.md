#  WebLogic任意文件读取漏洞  
原创 晨星安全团队
                    晨星安全团队  晨星安全团队   2026-03-04 06:12  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0xLh3eaPqtmsCib3WKbhsQ4H58oXibyZsy5oUU4EygEtiaSGkKOHRibZF4k1wp3CJBXZREniae3GlicGTz8iaKe0XDic7g/640?wx_fmt=png "")  
  
  
**WebLogic**  
  
**任意文件读取**  
  
  
  
访问  
http://your-ip:7001/hello/file.jsp?path=/etc/passwd  
    
  
成功读取passwd文件，证明任意文件读取漏洞存在。  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/ZCjMVth9QjiaPhVzfxvJqyxWFgiaUs3tLbNeibfHb4bqRdSibtyPBmzrSwF6ZJzrT4TZ45BlIAPsjETupAQuOSnPuMmm8a7spVwGhDrFHkiaxZFg/640?from=appmsg "")  
  
这里忘记自己是连的热点了，所以直接改  
127.0.0.1  
了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9Qjh3lwAm5hHSeibib9xxvJhOvqYKJIfasq4wOuJlOwShRqHJUejg4qulYahffSIB4ZA5ATCpWCJNyib4iay2ENro1Fb5mJD9WOL5SPI/640?wx_fmt=jpeg "")  
  
WebLogic 的密码使用AES加密（老版本使用3DES）  
  
由于这是对称加密，如果我们能获得密文和加密密钥，就可以解密密码。  
  
这两个文件位于base_domain目录下：  
  
**·**  
SerializedSystemIni.dat  
：加密密钥文件  
  
**·**  
config.xml  
：包含加密密码的配置文件  
  
在本环境中，这些文件位于：  
  
**·**  
./security/SerializedSystemIni.dat  
  
**·**  
./config/config.xml  
  
(相对于     
/root/Oracle/Middleware/user_projects/domains/base_domain  
 目录）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjhvOibTedib1f9w7LIAvuia1ibPaHicJhttnLaoI59WoLWiacVVOKrgkfNyOEB0dIM07eVKvBbh5x7ZuJGItJibOhDKovZliaf4Ibd8X2g/640?wx_fmt=jpeg "")  
  
右键导出数据包（YaKit格式异常，需要切换为BurpSuite）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9Qjia6Qn0RZIw5PNXUmMVDGBTnHn5hMRAyoiaOuopqvGu6DQ5icHgfiatGjam38yNcMB7SWFf93VK0omqMUvPSHhPAfcr70yNKIbQTicM/640?wx_fmt=jpeg "")  
  
读取 AES 密文  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9Qjhkn4Vl2xVAZJohAuquVJVoevqT2ykJhfUohz1xtPHr6hrYXWiaHgkrw6bLy52WafmZiaSvVDeREXfYBaDljMxP2B0CQgtQTN3K8/640?wx_fmt=jpeg "")  
  
使用工具解密拿到密码  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9QjjdCgCXCOAQykA6mMiafibkFC1zdpezS67kJgrESY8G4bLT7SDo0zskODslX3AfDCic2p05d7KgGzzU50rTMwSf4I0we8EicnRAtRU/640?wx_fmt=jpeg "")  
  
  
   
成功登录后台  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9QjhI6eicIbxuYY331eBUrbxbPibpISsLuwzhejP2tiar2lOOtIGOOEibyaOiacfgGIIyKOhACHf1qIiaoYibxmmq2M6Z1NWbYJN4GgXfv8/640?wx_fmt=jpeg "")  
  
  
  
**-END-**  
  
****  
  
