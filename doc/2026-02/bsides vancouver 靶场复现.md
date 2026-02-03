#  bsides vancouver 靶场复现  
原创 小木说安全
                    小木说安全  智检安全研习社   2026-02-03 03:18  
  
## 1.主机发现  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dscz0L9F63BGWxJFzkXk2mQCAYlaWrbddTZMcW7AIU1IdQibmaiaGNErTSog/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczcmbukInUdzxgnZJ6pCVRJ9iagwojcdKokkaFNqt4WDEIh9du8YUG9TA/640?wx_fmt=png "")  
  
使用nmap测得靶机ip为192.168.40.141  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczvOvTkSHNfTneOB9Xs9Gc2g73ib4hSLEH5JaC51AYfTJta7tzBtJCFFg/640?wx_fmt=png "")  
  
探测服务，开启了21、22、80端口。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczAjsASS0AOo5ffdzHlnYy3RtRcxic3uOHEDApfIHrp3vopic6R1J8Lc5g/640?wx_fmt=png "")  
## 2.web渗透  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczxoOI2z7x6uicMRcUEo1Aro0u45KLibrhRpSXmrhHCyuiakOx2LVZU80ibg/640?wx_fmt=png "")  
  
目录扫描，发现robots.txt。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczfQ4J5PYjzZuN7U6JOmVNAlQHerLZibCerLpyc1ibREibibBuH766e0XyIg/640?wx_fmt=png "")  
  
尝试访问，发现wordpress系统。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DscztRCEKZU7tFC2cBwIE1beDrFSkA3GRBfCXIagQjAVEW7pwLd9FkKHcw/640?wx_fmt=png "")  
  
使用wpscan扫描wordpress用户：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dsczc8yibnSM8a9OxxkOuTmsHqvnQ40zpd6vMdDiaic3HPicG6OKbZR1hDamsw/640?wx_fmt=png "")  
  
发现用户john和admin。  
  
   
## 3.ftp端口渗透  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dscz44OWU359Eg5vqWp5diaA97PuHhxQOMqsmqxYRHjaQia73UlL4fIUWU8A/640?wx_fmt=png "")  
  
  
发现一个文件，发现下面有很多用户名：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczuribY25y4HbSKib7ZxvqNxaHkFOGHTsichqsGBPSpp0x7A6jkbatQvQ3w/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dscz8VPFCwk0fWRd1qmjEfaDLx6nla8NMicJMa8mZwvAiaJc3AsnJWmM3IiaQ/640?wx_fmt=png "")  
  
用超级弱口令工具爆破一下，发现了anne的密码princess。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczNMzWSPq9fTvxsVY4v8iatUDtuE40DWyOCj0yicwQW07eQpRvG77tXrqA/640?wx_fmt=png "")  
  
用xshell成功登录：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczicgpUyJRaxdoUu4h9tZhn2ytSlibzibxyMzc1pCDiblKI3PaPxow8pqV3Q/640?wx_fmt=png "")  
  
查找工作目录，发现了anne用户的flag。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczSZcGgN4onWSCM98yJfhIL2TwxJChmZbV1SY04vb0g96ibwt9MWqlN7Q/640?wx_fmt=png "")  
## 4.提升root权限  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczicaMx9bYmXTN80eHc0G5Uqtr03gny1GL580cBJcqYaS66Iicj4TkDNOA/640?wx_fmt=png "")  
  
Wordpress登录界面。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczhMZTHVOIEJllTMdUnefs7RJibw5iaGGuEEwcEan6ShpQfvQcaAy5HM8A/640?wx_fmt=png "")  
  
Wpscan爆出了密码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dsczu3FCib5ydWnChKiciadHWI9opHul5LB68cWicw9TprCtSbMqBjqw7HHAEw/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczTaib3WtemuicFs3ficjmnJlic8SibBWSHp76KBHAh7ueWiaxFfYOiahMbwv8w/640?wx_fmt=png "")  
  
登录成功。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczV4vJyB1VkaouzmtvUqLRwXicQB6JX0szzP8d0gPB8do8kIEsNdJU4Lw/640?wx_fmt=png "")  
  
一般在这个404界面会存在命令执行。  
  
写入shell：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dscz1m6I1o5vjAU9CLhkN8SUefq0ZVtvSYSP4rA5lsRBQIp8o3za1PdkWg/640?wx_fmt=png "")  
  
Kali设置监听拿到shell：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczbL6bHNASoUZnaX7zENoIW4YdNaanGFSzN7MhYzBzarh2gtm1fy3nHA/640?wx_fmt=png "")  
  
利用python获得新的shell：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczSqMCPd5JOJeHx5okgSmxqtZDqzCU9q4tEwfz02FZ2woTNznWFKyjZg/640?wx_fmt=png "")  
  
查找每个用户文件，和浏览各目录文件，发现位于 /usr/local/bin/cleanup 文件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczjucnnEX2EHtib3PwlfOqaY3gxWa41Px2E6t7AQUOTmFrbeHFXmELuvg/640?wx_fmt=png "")  
  
这是一段清理Apache日志的脚本，需要root权限运行。            
  
查看cleanup文件的权限为777，可以随意修改和执行，可以将文件内容改成一个反弹shell  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczSgtsUjPh5bHUSbRb533QYVUD2WRQvbNt7oXic90cxZgJkeELuEmGUog/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczEQW919kskXhlxHHZN99L35WusBvxzk52cfFY79noNaCW7IOibbclHdg/640?wx_fmt=png "")  
  
再次查看 cleanup已经变成这样了：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dsczc8niaYt7RjNWIiaPF5gqmFwt6ahncKtmmMD2ZDia62B1BiaEYtj8QXdicuA/640?wx_fmt=png "")  
  
然后kali开启监听：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0Dsczb70ukWpicPdRKa4ib1TmgibQ5DDcmVz41Hm7Ub216jv3CzvVaN5AWu5sw/640?wx_fmt=png "")  
  
再次查看一下cleanup文件就能反弹成功了：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ihw4oic2pnCuQagsRQvgjEjKpqRe0DsczeBtZ6AVfib5jhUoKKglY8sLbOYEKup6mjib9QZNtzdyib2uz9f8bQ2Xlg/640?wx_fmt=png "")  
  
  
