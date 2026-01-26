#  Android APP客户端漏洞挖掘思路（【补天白帽黑客城市沙龙-长沙站】）  
China_Sec
                    China_Sec  Hacking黑白红   2026-01-26 04:39  
  
分享一篇高手的  
Android APP客户端漏洞挖掘思路  
  
随着Android系统在移动设备中的主导地位，APP客户端安全漏洞已成为黑客攻击的主要入口。本议题将梳理Android APP常见客户端漏洞挖掘思路，包括:四大组件漏洞、Webview组件漏洞、防抓包对抗等，并结合实际案例演示漏洞挖掘过程。  
###   
### Speaker：China_Sec  
  
![幻灯片1.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25wqCeRuh90LKO13Z8qWB8DX9LLBJT0fQE5u6w9PpqNtwvHJQU25652Q/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片2.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25EbPhQMqmzUmVmKSORFu8O6lnE3llcJxGUf4ibqvtPUmaX8zKyGgNgpg/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片3.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25kt6o55UsdleicgEw9AZFld5cgqyS9lGVaG55bDgWPFJpKpKrDye9yZg/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片4.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25o5Ow6Hwqg0J4ZYXiavdGBQABf9kzXk8AGBXSjK3rNUZmibicUiaJWPEGkg/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片5.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo2530ic476nVVo1lwVQwBMxHbywc3l2hL9LBs9eDeDZP2I9LImcCshAibug/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片6.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo259wtxBXKv4QA52TD5bWtCvPIqKUm8EWia5x15oCd43PuqUUUmicCnNE6Q/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片7.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25eDjQ6jRibaN2Nkj6HX3T7kJgWmWtPJz5lwNtib6tRUicQaEarFB4eFUBw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片8.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25YetaKGst9G1qUzcrZWiaCQTicOGvfxibicIpKXxEpLbH0dMvficWvXAtWRQ/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片9.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25YruTB0RTx6DwaAmDId4yLW3yFMcezACY89bdEum9GpcMXGNtws5grw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片10.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo258jc5qFJXZg766zSvcQyV02gh9R6wKvpzIhBZDibt9zICcekYFQ90DCw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片11.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25Nic3YsQE5XNPaAm4UicicY3yWy54yuTa6jlS3URHj3eNgG2Dh0icoBz6kA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片12.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25LNpKHNXDKo7hx2Cq8hDaebrQ5REU5iavazFicTsdZibgQg4RatdxYRL6w/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片13.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25WsXuORHibgicjqKFxUlqgffiaTr7xwedlqPELq3zFpy3flRicIQsl9RetA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片14.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25YEKS3hkoCPtftHC3aDHLuw1Bkn07mQrkK11RomHH9eeiclsuF4wmIUw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片15.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo256HGDYfWgyE9TuKBrMEmaoygnq83z7yXLnGtfXH3P8GibnXibiaqup0iaQA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片16.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25OfVxsibWID8GJWiaOmwQ1Zs0IOTLhIiaedQ2clWhppibyia1QtxAFJavXDA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片17.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25pq4ds7ZUcLibRnT5P0RSLhZtINVNTZq5dKfJJMALM8WtTB83Ae4xPRA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片18.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25ia99ic069dQwS3ibDAg0lhGxauLlKleSwIqxEcWic7tox9RCcgdH72ttJw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片19.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25QsDp75wvmfib782DRIlSlqCR9Ay8OQd8s8YnRsAdVyB1WnaPCxhJAZA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片20.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo255skw7qgnofcSCZqZ8t0PbRgoTTXnP49DAGIece7BYRBH73z7dgnsMw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片21.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25WnLkrQofyq0c4yCZfic7TY5IadoyuNGpwBeK9ibiaIrocdBpIsljDtz3A/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片22.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25fickMIqE8bdOvIbdt6M7mkibHq4TnCUD1gtmewTrCrVUrjkMuBkIItHA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片23.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25QmlbC9JaMGEz50E71GRShN6MrIibwEYFX666cxGKUjwwxUBstrkpXAQ/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片24.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25Lce9OrgTjoV4WybdMTVviabpqic42BJpg5icfekEXMxiazMxg2iag1SlgXw/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片25.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25R1iak4ovzaEgk0EGlo5ibMiajH9uOcx48ew20eWbmsibv7Mxpx1PTgghCA/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片26.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo250WhcNZEbXFj2xzrUgwDNicTDUe1Q9OsOhUX8AksNYo5E84T68lfJicdg/640?wx_fmt=png&from=appmsg "")  
  
![幻灯片27.PNG](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSl95mjbibssDFp2C1Oibuo25kxsKFQLS33gXTqJpYia6W3KhCiar2pt9B0HicowAj3ITz1k87PjXTTKGg/640?wx_fmt=png&from=appmsg "")  
-   
