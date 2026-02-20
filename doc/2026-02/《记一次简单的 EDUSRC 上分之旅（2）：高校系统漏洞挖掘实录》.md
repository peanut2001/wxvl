#  《记一次简单的 EDUSRC 上分之旅（2）：高校系统漏洞挖掘实录》  
原创 陌上ms
                    陌上ms  陌上ms   2026-02-19 06:45  
  
郑重说明  
  
本公众号文章内容均为作者日常学习与经验积累所得，仅供学习交流使用。若需转载，请联系作者取得授权。文中涉及的网络安全相关内容，**仅限在合法授权范围内进行测试与研究**  
，严禁用于任何商业或非法用途。  
  
任何未经授权的测试行为所导致的后果，均由行为人自行承担，与作者本人及本公众号无关。  
  
正文Action  
  
# 漏洞1：任意用户登录  
#   
# 日常在挖EDUSRC的时候，遇到一个系统需要手机号登录，  
# 经过测试发现，没有注册按钮，只有内部手机号才能登录。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV7JQFlUc6FXRXRM3IibZQvC6Gxdo58pmyLpm6zdxYXMbILL7hBS9kf5yUt8NicPOIYt5ESUvCm7KRQ1ZpyEMff2egpjfdAP6atmE/640?wx_fmt=png&from=appmsg "")  
#   
  
经过多种方法的信息搜集，终于找到了老师手机号（抖音，小红书，谷歌都找不到，最后在百度高级搜索中找到）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV533icK9Afqq9pmyIVo9DhCu6OiblnYVm5O2FzsjKlQSNqyANpHVAw8jniaO3YHuawIfJythzApPibIQT5gP2n3zF8GurSmpFRu0MI/640?wx_fmt=png&from=appmsg "")  
  
经过信息收集，找到了其中一位老师的手机号，13xxxxxxxx  
  
验证码随意输入即可（例如：1234），  
  
点击登录抓包，  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV71wKkZQYWdiajjNE9V83QRtk2NxblgWhGtjoN7feaCOsGRnk0XGg6NQgmX5QedYxiasaXov8Po3fg8tryuopHOvSPuQTLc7EdpI/640?wx_fmt=png&from=appmsg "")  
  
此时截取返回包会显示，  
  
{"code":81,"msg":"验证码失效","data":false}  
  
将返回包修改为{"code":200,"msg":"验证码失效","data":true}，  
  
进行放包，  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV55p2NcLicAicXTHFCSEynviacq9UVyCBbzjM5TQd9lBiaBAoChat1q8icJ3BhlrXqXhmravfJrnlAms6icRznCcfynyHX1FZSOQnXJI/640?wx_fmt=png&from=appmsg "")  
  
即可登录成功。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV7Th7rnAhg7JID2JBX4bn8nzKAe6N071ujaIDaHv2Gw4U1Ru04MDEKW0mNia1BJqLxuXnarpsgcbSiaJ51xgcVXhWcVHc4P47YdY/640?wx_fmt=png&from=appmsg "")  
#   
# 非常简单的手法，但确实很有用！  
#   
  
可以看到此处有post传参，5427，  
  
此时我修改5427为1，  
  
可看到管理员手机号（还有密码），  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV5JTAfMkhbfd4NzOngViaibEFgiaObOVkD0atKIrVz6Oc0Px6PQiaNA7xUq2UoAlKGXlibmwQJIzuEqdNO4DibEElFXMUqP8mEibAGgAU/640?wx_fmt=png&from=appmsg "")  
  
那就可以重复上述步骤，登录成功，接管管理员账号。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV7lcboUQZSO965rloqambsK9WGWl5mzs1zwqWyrY1Ty96yibXSYgJKfssicMe8maF6z3wLf54BYk5exmGg21DXkJHqpdEZDEX1Jg/640?wx_fmt=png&from=appmsg "")  
  
通过遍历可看，总共可遍历出9872-4870=5002个有效的数据包，并泄露了其他老师的工号，密码，姓名，手机号等敏感信息，此时我可登录全校老师的账号。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV4cDxyol04r2Rxuw53vkgmpBoc7eJdvGymH4owUBHCeCDliaUxYA5kwsomXMxNqUaPSIct3ZyTyDCZCWPTtADGtW3G7YzM3l3dY/640?wx_fmt=png&from=appmsg "")  
# 漏洞2：SQL注入  
  
点击待办-已审核，进行抓包，  
  
在参数endTimeYear和dateTmp处存在注入，  
  
sql注入payload：and sleep(5)  
  
非常简单的延时  
payload，  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV7kc6icCxHe91micen2sml7QOwIfxKHHVqSxoAAHbM34HstK4zj1KLDiay8AEEehdGx8c7TDF5HyEZVdiaJ4ZUs8ysYHdydwAJTxqU/640?wx_fmt=png&from=appmsg "")  
  
总结：这是一次手法与上篇文章【  
> 《记一次简单的 EDUSRC 上分之旅（1）：高校系统漏洞挖掘实录》  
  
> 陌上ms，公众号：陌上ms[《记一次简单的 EDUSRC 上分之旅（1）：高校系统漏洞挖掘实录》](https://mp.weixin.qq.com/s?__biz=MzE5MTIwNzkyMA==&mid=2247483990&idx=1&sn=1c56cdabc4a275eddc44e61169ae0096&chksm=960b42c9a17ccbdf29c4059db9e69b9875daebd4910749f2610e39ae2196432307d5e97f76c6&token=137385646&lang=zh_CN#rd)  
  
  
  
】一致的挖洞经历，主要是在第一步需要寻找内部记录在册的老师手机号，后面就是很简单了，也是拿到了高危。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV4MjDn8ic8tXr0flaubgLzniaf94icMKUudFtDUYTSA1BUNrYPibiaib6EfvzVqPibvKDRic0icx2dMtuYgfeib0RiakMkYczeKGVzl1ic6iaibQ/640?wx_fmt=png&from=appmsg "")  
  
  
