#  【工具】Hikvision海康威视综合漏洞利用工具  
原创 track
                    track  泷羽Sec-track   2026-01-22 01:37  
  
>   
> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！  
  
  
**往期推荐：**  
  
**【工具】Shiro反序列化利用工具**  
  
**hw中用到的某云waf绕过技巧**  
  
**若依(RuoYi)框架漏洞战争手册**  
  
**【工具】Sqlmap中文汉化版**  
  
**【工具】多平台GUI图形化资产测绘工具，支持一键导出**  
  
**公众号：**  
  
  
工具获取在后台回复  
260122  
即可  
# Hikvision综合漏洞利用工具  
  
官方  
```
https://github.com/MInggongK/Hikvision-

```  
  
海康威视综合漏洞利用工具 收录漏洞如下：  
- Hikvision 摄像头未授权访问漏洞  
  
- Hikvision 远程代码执行漏洞  
  
- Hikvision iVMS综合安防系统任意文件上传漏洞  
  
- Hikvision综合安防管理平台isecure center文件上传漏洞  
  
- Hikvision综合安防管理平台config信息泄露漏洞  
  
- Hikvision综合安防管理平台env信息泄漏漏洞  
  
- Hikvision综合安防管理平台report任意文件上传漏洞  
  
- Hikvision综合安防管理平台api session命令执行漏洞  
  
- Hikvision applyCT命令执行漏洞  
  
- Hikvision applyAutoLoginTicket命令执行漏洞  
  
- Hikvision keepAlive远程代码执行漏洞  
  
- Hikvision综合安防管理平台orgManage任意文件读取漏洞  
  
- Hikvision综合安防管理平台files任意文件读取漏洞  
  
- Hikvision综合安防管理平台detection远程命令执行漏洞  
  
- Hikvision综合安防管理平台productFile远程命令执行漏洞  
  
- Hikvision综合安防管理平台licenseExpire远程命令执行漏洞  
  
- Hikvision综合安防管理平台installation远程命令执行漏洞  
  
## 功能介绍  
  
批量检测模块，模块如下：  
- Hikvision 远程代码执行漏洞  
  
- Hikvision iVMS综合安防系统任意文件上传漏洞  
  
- Hikvision综合安防管理平台isecure center文件上传漏洞  
  
- Hikvision综合安防管理平台config信息泄露漏洞  
  
- Hikvision综合安防管理平台api session命令执行漏洞  
  
- Hikvision综合安防管理平台env信息泄漏漏洞  
  
- Hikvision applyAutoLoginTicket命令执行漏洞  
  
- Hikvision综合安防管理平台orgManage任意文件读取漏洞  
  
- Hikvision综合安防管理平台files任意文件读取漏洞  
  
- webshell利用模块 Hikvision iVMS综合安防系统任意文件上传漏洞  
  
- Hikvision综合安防管理平台isecure center文件上传漏洞  
  
- Hikvision综合安防管理平台report任意文件上传漏洞  
  
- cmshell命令执行模块  
  
- Hikvision 远程代码执行漏洞  
  
- Hikvision综合安防管理平台api session命令执行漏洞  
  
- Hikvision applyAutoLoginTicket命令执行漏洞  
  
## 使用方法  
  
启动程序  
  
![image-20260122092651102](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43uVoibSYUic82nyG0oO9BmNwOUE59qIESdbCU4o8R3d0vQwqhhFJJXubg/640?wx_fmt=png&from=appmsg "")  
  
image-20260122092651102  
  
默认模块可一键扫描所有漏洞  
  
![image-20260122092614010](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43rghYLgOwnrM5MIibDib0lIEBswElc7PC7AbIMv3HrTu9IYO08GWJS8RQ/640?wx_fmt=png&from=appmsg "")  
  
image-20260122092614010  
  
选择模块可单独选择你要检测的模块，输入目标，点击选择模块即可检测漏洞，批量检测内置路径：/hikvision.txt  
  
![image-20260122092749064](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43iaVIcv5Wic6fk6oTSZcFEG92UkcmHPWWFhuTTXhrJPnH0LkNj0AnByWA/640?wx_fmt=png&from=appmsg "")  
  
image-20260122092749064  
  
Cmdshell模块：选择模块进行漏洞验证，如果存在，在cmdshell输入你要执行的命令即可  
  
![image-20260122092822267](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43m8krYCau8MMgnfEbfqLHGMV1zapyjpJsvEQ8bkJiajbwlScEJrqr85Q/640?wx_fmt=png&from=appmsg "")  
  
image-20260122092822267  
  
webshell利用模块：内置Godzilla，Behinder，AntSword，cmd，四种类型的shell![image-20260122092853820](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43plicibnz2v7l5yiaJq0sbSlicyYdmREk9uu7geM4iaCZOz5fgtEH2UF7CWw/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞说明  
  
![image-20260122092917172](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43UEJLuSgtb2E1GnTsiaNKkTRoyMicibT1iaL2pUztYFBEWBPEGU6nyibj0vA/640?wx_fmt=png&from=appmsg "")  
  
image-20260122092917172  
  
## 知识星球  
  
**可以加入我们的知识星球，包含cs二开，甲壳虫，渗透工具，SRC案例分享，POC工具等，还有很多src挖掘资料包**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K43kub4CWqa6ibMLIfoXm2zUcCVpe5T2uNVwlDzOK1v8xuxz5APibjkvvIQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K436a0iaP64MhtrAApib7bVN1H3ps5S27rafl8G9vPOvxaaqQbOv0a51gew/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw3xQiaAZ3oF6IOGDTn7P4K437GDiah4tXAic9I3CVVBUdhtFHVW0Xic6qPRknkKEQjib8RM7TtoEtpQia8Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
