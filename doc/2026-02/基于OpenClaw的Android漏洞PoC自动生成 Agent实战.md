#  基于OpenClaw的Android漏洞PoC自动生成 Agent实战  
原创 做安全的小明同学
                    做安全的小明同学  大山子雪人   2026-02-01 12:59  
  
   
  
  
花了一上午的时间在本机搭建了openclaw环境。晚上尝试配置自动分析patch并写出poc的多agent工具。  
  
经过一系列的摸爬滚打，终于有了雏形，并且验证成功。  
1. 1. 首先给了一段patch，并告诉agent通过分析该patch写出poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XmiaW85fpqqn6VFX73BicbIvSpPqIGnwBOzbr5gF69TzAndb0bkUpbnaw/640?wx_fmt=png&from=appmsg "")  
  
  2. agent开始补丁，并给出漏洞原理以及验证步骤  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XERnNCicWrDgGwqUIic9BiboyjZveTNgvFqvqicjwrcNSndK4ZAoTrkgs8g/640?wx_fmt=png&from=appmsg "")  
1. 3. 创建模拟器  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0X3Ft5Tskl86QGsNicQ3MsvPR4rVPWicw5KtWu7FIxia1NaCchTiacnaaFibQ/640?wx_fmt=png&from=appmsg "")  
  
1. 因为一开始并没有设置创建模拟器相关的skill，所以导致无法自动创建模拟器。然后让chatgpt帮忙写了一个创建模拟器的skill以及tool。本机有之前创建好的模拟器，所以  
agent复用了（主要原因在于我告诉agent该漏洞的受影响版本是android14，所以选取本机的android14）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XSIhYbmMxgMbo5Hsms0ibUmFhKOibAcLgyu8E6hTeVzvBibqkeBXb7vmlg/640?wx_fmt=png&from=appmsg "")  
  
1. 4. 开始自动验证漏洞  
  
1. ![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0Xl2rdMD8uINicanRoG4cgzSpUiciaOu5ZwhW1DYPTAenyu2GHOicXMexiaTQ/640?wx_fmt=png&from=appmsg "")  
  
由于本机环境android版本较新，实际漏洞不存在，所以agent报告漏洞已修复，并给  
  
出说明，根据日志也证明了poc是正确的。不过由于这个"失误"，反而有进一步机会，  
  
尝试agent的能力  
  
1. 5. 让模型选取受影响的版本  
  
1. ![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XG57MJibhAniaxo5PvOyLtoT2t4hO61kynxfEEwFz5DVAS8KzGhlJNzhg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XrkyicJIK7O5F40vIApP0TrsWq7X8KnTyk8uxqhRduofATuOCT2XAcIw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWaCz4pTbdsFPGcT2CnPHN0XH847QAAvgeq3KuO24TzywODV5Gt4U14rnzoicXz15FBqmIF5FlH7zqw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
   
  
