#  【0 day 在野】安科瑞企业微电网能效管理平台存在敏感信息泄露漏洞 附POC  
原创 阿伟
                    阿伟  船山信安   2026-02-10 02:50  
  
**免责声明**  
  
由于传播、利用本公众号船山信安所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号  
船山信安  
及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
**一、漏洞描述**  
  
**安科瑞企业微电网能效管理平台是一个集电力监控、能源管理、电能质量分析、电气安全预警、智能运维和分布式能源协调控制于一体的综合数字化平台。该平台存在严重的配置文件泄露安全漏洞：核心接口文件未做权限管控与敏感信息加密处理，直接泄露了系统账号及密码。攻击者可通过该泄露信息直接登录系统，突破权限边界获取系统操作权限，不仅能够篡改平台数据、中断微电网能效管理服务，还会导致企业核心能源数据泄露，对企业生产运营及用户权益造成实质性损害。**  
  
**二、影响版本**  
  
**企业微电网能效管理平台、智慧运维云平台**  
  
**三、360Quake 语法**  
  
**favicon: "7a14f5a016b0738807fafe202ef37520"**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquPUuD1cGahibweX0v0YmjTGMj5TC5DzP3bNoGAIlbe9nEiciaUCb5fLn5mYft7Sibpicvpy5EDnd5bicriapOBj5n7us35icSLbSkd2fzU/640?wx_fmt=png&from=appmsg "")  
  
**四、漏洞复现**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMw3SEFqdgkorQ8zluYl1Ut047WkzGzD9yOSuP65oarFp5OquTrzt24pNn6LUBIJsjuHmaNSj4xQ53NAAKx8nyAZHqHGvMSkNA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNrSTsEj3ItcnfydanLF86cMRibgLpSLWPd17wvPbfXqMmfS6P1jsBI2EfUBapClqkULBNkyUl8yRjeCmNoZicV1VS5Eucib1D2cw/640?wx_fmt=png&from=appmsg "")  
  
**五、修复建议**  
  
**升级平台版本并应用安全补丁、清理敏感信息泄露文件、严格管控接口访问权限、启用安全防护策略并开展全面安全审计、从源头消除安全隐患。**  
  
**六、敏感接口获取**  
  
**后台回复260210获取敏感信息泄露接口**  
  
