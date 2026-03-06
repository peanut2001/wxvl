#  东胜物流软件GetData接口存在SQL注⼊漏洞 附POC  
2026-3-6更新
                    2026-3-6更新  南风漏洞复现文库   2026-03-06 15:40  
  
   
  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 东胜物流软件GetData接口简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。  
## 2.漏洞描述  
  
东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。 东胜物流软件GetData接口存在SQL注⼊漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
东胜物流软件  
![东胜物流软件GetData接口存在SQL注⼊漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6wD8qF9LU8IGQhBYy0pe1HXUYMiaN3UUEibuicgfFVkB3icAXE9iaJDpicdxyBiaq08XnHep3P465yn2MDRgOPjtUic5XbsFWVu1llDFX4/640?wx_fmt=png&from=appmsg "null")  
  
东胜物流软件GetData接口存在SQL注⼊漏洞  
## 4.fofa查询语句  
  
body="FeeCodes/CompanysAdapter.aspx"||body="dhtmlxcombo_whp.js"||body="dongshengsoft"||body="theme/dhtmlxcombo.css"  
## 5.漏洞复现  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zibaNHjzqF0dB9j1ZJFkfLLcfexiaic85aFxth90CMJobfQkicyTdWMynk4ZhqfSP89ibXuHzAAhibv7xSibJ1wSxvGUia2MPY8iaYcnVg/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zCtZN7LMXhBy7PiaU0ZXU8pNichuD5YwJ0pLlkas9EFDtgLVJswGiaRgrTO18tGI5s6OxTmX0eTgHUJDEKG7GH4pibAdGEFyibKLias/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yjrNMxoDLySE9jCqCialIXbeICmB2u5oGzPEDg64ic9GwncXq7zqBd1mFAQaNXibWrDlKD5PaEa7Q1su3UicicMibepw0rGMcsmElJY/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yZHnoibqm1Z4H7nzg2ibP4HxH74eoicjrkic3bfFqOy6lK9miaKAEJianOgpiafYnO5Dicia292ibUicYic2mxt0GQ6TTJGMrH3w4vx50VEGc/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zNHxRicr0JhMOJSTrk2Qic1uqwrv758QH2tkJM9dKoePQib1vSmeiaRcZ6f5KHzg6KHdGOtHgE8R9jYZ1Iz6dZXNjrMAicP8rHhwJw/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wibhS64twiaEMoicc3HY3AnLbOx5CaM2bZXXib4fOlLqZk0DgEeRvtoia8TgxqONLJFJfWJ6RkYggnnocoCO3KTeDzZsPm62TG0Lys/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zRckibB0go9iaXfic3HMxePryDONxZI8Un2fkYXjMfBwM2pSa6p9g1PWfLVoKXlEPfEMXhdicIpnTMvk2bzVNibCY3N55kgRPVZvNU/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
