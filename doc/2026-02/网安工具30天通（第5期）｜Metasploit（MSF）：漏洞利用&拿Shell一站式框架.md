#  网安工具30天通（第5期）｜Metasploit（MSF）：漏洞利用&拿Shell一站式框架  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-02-27 02:39  
  
## 一、工具核心定位  
  
Metasploit（简称MSF）是全球最主流、最完整的**渗透测试框架**  
，是从“找漏洞”到“拿权限”最直接的桥梁。  
  
不管是 CTF、护网、实战攻防，只要遇到可利用漏洞，MSF 基本都能**一键弹Shell、一键提权、一键内网漫游**  
。  
  
核心用途：  
- 加载公开漏洞模块（EXP）  
  
- 快速生成反弹Shell、木马  
  
- 内网信息收集、提权、横向移动  
  
- 对弱口令、未授权、远程执行漏洞批量利用  
  
## 二、最常用基础命令（实战必背）  
1. 启动MSF控制台  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyOnbFFct1KaS5rEYrUNmFLicSxCHlhrTibaF9rosRiaaicoUGlB9LkDPxWq8NObsRfkfw2nf63NRuyuSBkOOeRTXVzQiaI1uCnV6fBQ/640?wx_fmt=png&from=appmsg "")  
  
1. 搜索漏洞模块  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyNbvrCeNmbzhuVceEpQYoXDpOZBoqriaWuC9aYFUyayOMRwUvUiaxGfZIssD3BpS1IUXNNcBMgKYBvI4SWXibEibT8H4sh0kKxQRmU/640?wx_fmt=png&from=appmsg "")  
  
1. 选择模块  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyPzkv28uSO7ME3FuHfCHvAsiahRibHYwnCniaP6F2wO72p7XPPcGANIWKc2EGTTviaYSlF6vDQ8Unckic7IDBicLlgdalKiaCkkNGfKLw/640?wx_fmt=png&from=appmsg "")  
  
1. 查看需要配置的参数  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyMKHwHqqpPrCJW81cHFN1cSSS5iaxup1OOcePXwFJ7YhHHCSGhO2WzUvtVVnbWLUDStqL4icSElCx7mMHpDXM3fUBnCiaTlS0qjnQ/640?wx_fmt=png&from=appmsg "")  
  
1. 设置目标IP  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOMdcib8Vgr7KTibKpy8M9bV554AwQs5kbPV5qdgZic2gu9lZVPibgTQeM3eibg6iaoTsBmMqXMMVkyV2ciboziaiassKlYgMSd230Y1jpc/640?wx_fmt=png&from=appmsg "")  
  
1. 运行攻击  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyN4mRzn65ViaPYFxrn1oTYn8oI2ZG0iajCic2u6h2YdLibsWQdJuJ8qfq7FSboxQoaibLW5GaaFZwz4cc6zBbxquzqf0GIeznNVBZnY/640?wx_fmt=png&from=appmsg "")  
  
## 三、经典CTF真题实战  
### 真题名称：永远不过时的远程代码执行  
### 靶机信息  
- 系统：Linux  
  
- 端口：22、80、512、2049、**445**  
  
- 服务：Samba 3.5.0（存在经典漏洞）  
  
- 目标：利用MSF直接拿下root权限flag  
  
## 四、完整解题流程  
### 步骤1：扫描端口与服务  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyPLX6tHQiaAGBb2wvA7tOArSUPUJUabRiamZWEeVicfcw4lxxuzU7CqiaI1bXqyoMXV6vlQJTdSsYT4LchAUSbyBZjibpRDGUH5t17g/640?wx_fmt=png&from=appmsg "")  
  
关键结果：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyO3qs78S6Ow1KYBFszmaYXZxICRBrUickd504QTKrDGQ0pYNfjGia3iamtcOeJtiaDAOBmelYvdmU46yUUegrRINQzGQoujkmbCibZo/640?wx_fmt=png&from=appmsg "")  
### 步骤2：MSF查找对应漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyNxAyr06475nF9hL2iaRCBqz4VZwrhGtWroxJnwQOf8MlaXQO60flPR54Q0ibQb4m2iaOYDfX3KibUNdvo31CPAXFbEl20bddOM9sc/640?wx_fmt=png&from=appmsg "")  
  
找到经典漏洞：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOTjkW0V0UpcNcGF2NwUZPv8lVCMoJdLpP0yOyqHqklb97lk8p5ywGJ4OKZPWkGc4I4ca29G5iage881nUq0bdgC161nwjKmWg0/640?wx_fmt=png&from=appmsg "")  
### 步骤3：加载模块并配置  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyNiaqmGdkaVRGIuGOMyyzF2TklibNWbWicOicvuBG9JZUkxdDzU5NNKIIaVcntAgWrICReibVlS6VDChLe9Qv5IRmibNiaPIOvPgYAoFg/640?wx_fmt=png&from=appmsg "")  
### 步骤4：一键攻击拿Shell  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyOQHXPl9ibfaSfgPZ6ZJTWA0MESa1eUIVsfh5EtIqcRdGEYl03EQ4icVPkHtPZ0bfp3hMe6iaWFSCiaK5TOgQhcKtybHu2Xiceia3DoE/640?wx_fmt=png&from=appmsg "")  
  
成功直接拿到 **root 权限会话**  
。  
### 步骤5：读取flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyN09fDWohQPS9LontV8FNOc4iby7zrPMReHdGhI1IvLAl9b62DuaibXBeHZ0DIia23GbXMwLCpDUMtnef4bN7D5CKG1C1rr8Q7ib9s/640?wx_fmt=png&from=appmsg "")  
  
  
flag：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOqhwCPhPXY5AjhZpCK4wJfRnCtBKZ4EFma9jJQYMuj6udnnVnTIyDCkXuaGjblQuz535J2beLNBOS58VvVNlteeREsZMSQsao/640?wx_fmt=png&from=appmsg "")  
## 五、实战复盘  
1. 遇到老旧服务（如 Samba、Tomcat、Redis），**优先查MSF有无现成EXP**  
  
1. MSF不是“黑客工具”，是**渗透测试标准武器**  
  
1. 真正难点不是点run，而是**识别服务、匹配漏洞**  
  
1. 拿到Shell后，提权、内网漫游都能在MSF里完成  
  
## 六、福利领取：全系列资料合集  
  
为了感谢大家的一路跟随，整理了 **「200节攻防教程资源包」**  
这是我整理的精华内容，覆盖网安所有核心知识点，后台回复“  
学习  
”即可获取：  
  
全套学习资源，可以  
点击文末  
阅读原文  
领取200节攻防教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
## 下期预告（第6期）  
  
**Netcat（nc）：网络瑞士军刀**  
  
端口监听、反弹Shell、文件传输、简单聊天  
  
真题：《最基础也最致命的反弹Shell入门》  
  
