#  JAVA漏洞集合工具  
dmd5安全
                    dmd5安全  dmd5安全   2026-03-06 07:48  
  
简介  
  
hyacinth是一款java漏洞集合工具，之前攻防的时候，总是需要打开多个jar包，觉得很麻烦，就做了一款集合工具。  
其中包含Struts2、Fastjson、Weblogic（xml）、Shiro、Log4j、Jboss、SpringCloud、等漏洞检测利用模块，及免杀webshell生成模块 Bypass、以及一些小工具模块等，由于图形化比较简明易懂，所以也不需要使用说明吧 。  
  
本项目的部分payload进行了一些混淆，具备一定过waf能力  
  
  
注：开发环境8u181，此版本可稳定运行，太高 如8u281会出现部分功能失效，如shiro的链爆破，如果发现有问题，可通过cmd运行jar包观察报错，大部分是因为jdk版本导致的  
  
  
工具截图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTePqDJswUCL33K9SDEzVcCqEx2rXAK3yqScibZo52oiaLdT2hYomxtjPIiaPicxMPj7dcYBxzvib6lxIy3Y2AQaicG0G2mUYuJFuwbMY/640?wx_fmt=png&from=appmsg "")  
  
  
项目地址  
  
https://github.com/pureqh/Hyacinth?tab=readme-ov-file  
  
