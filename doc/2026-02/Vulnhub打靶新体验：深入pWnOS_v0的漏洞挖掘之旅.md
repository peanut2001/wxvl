#  Vulnhub打靶新体验：深入pWnOS_v0的漏洞挖掘之旅  
原创 沐青序
                        沐青序  数字序言   2026-02-07 23:30  
  
![](https://mmbiz.qpic.cn/mmbiz_png/a3wHm5p9J3DurW4V709IEEBkws0KBQZ7SMibSKdmYUJcI1IG3BvUawbzCDB5a7jaxknGoic6DthnnPDMpRYgCO7g/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ic8N8zjibwlznnK9I42GyictibNNicnr1zDDtyCJkWibFzf73ea0hl250NrDu5TdkIAiaDuBCujZ5JxmBmuXwqewk9J8Q/640?from=appmsg "")  
  
  
免责声明：本公众号内容仅供网络安全技术学习与合法研究，严禁用于非法用途。使用者须遵守法律法规，因非法使用造成的全部后果自行承担。本公众号及作者不对内容准确性作保证，不承担因此产生的任何损失。如涉及侵权，烦请告知，核实后将立即处理。感谢理解。  
  
## 一、nmap  
  
使用 nmap 对目标靶机进行全维度扫描，依次执行存活主机探测、全端口扫描、服务版本识别及漏洞脚本扫描，命令如下：  
```
nmap -sP 192.168.126.0/24  # 存活主机扫描
nmap -p- -sV -T5 目标IP     # 全端口+服务版本扫描
nmap --script=vuln 目标IP   # 漏洞探测扫描

```  
  
扫描结果发现靶机开放多个关键端口，包含 Webmin 相关服务，同时探测到潜在的服务漏洞，为后续渗透提供基础信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUwwicibEMtdviak16LUSzOogGBX2PpgiaNuFLRo6B0UINFJuC10LINkAvic6cIA53NXBPJJrJFdZpXiaWXictVtd5HHf12Nkja2jEmGlc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUzHZ37wuic22kiblob1hyFFDuLwttN3b4qHnUroTIFia799T1wyGqyQJaAgbPzEzDbQkpQP7ejIlaZbk7bnLLsM2ib3Lq01k0KR4Wg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUw5pX20dokosP0lKtHW6GlA7a9W2asibRiaDNic3JG5WDB2icGFF5ic9UWgXaZQxYYyhGcvs0FjgZYjpiaVib8By1cCWIYTb0tD6sXGFA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUyMoPFGx2vno253iave4bSjKLWVYLFTVDBQ43lHuEQMqgNI9TmdOqmicicleeKa1icIJejYZa09mveSWmZgdVPY0HFWdiajiaEia3d7mQ/640?wx_fmt=png&from=appmsg "")  
## 二、web渗透  
### 随便看看  
  
直接访问靶机 IP 的 Web 服务，查看首页及相关页面的展示内容，点击页面各类链接、查看页面源代码，未发现明显的隐藏入口、账号密码等敏感信息，仅看到常规的页面展示内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUxApwdiaLPYlWQ0nhGbX3GwCuU0mUEhZicNa0gU7piaTHtGhoavoq39raUn14krASAtsTnBq8AFG5Nia7Ld8TzwU20sOsNku2YMTBw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUxMvgjacokefmcr05TMVla40BILTVk0OsIAdHCcMt9fUias7rOd6iayBYW7yryhFuMxkyjLdwLiaaVWia7ibdtoygMyVQtS6SWDMJfE/640?wx_fmt=png&from=appmsg "")  
### 目录爆破  
  
使用 dirb 工具对目标 Web 服务进行目录爆破，执行命令dirb http://目标IP  
，采用工具默认字典，扫描后仅发现少量常规目录，未探测到后台管理入口、敏感脚本文件等有价值的路径。  
  
好像也没啥  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUwJjsicicMUibgJjY8tLbs7gmPsv9oPq6sBxLcnu4HbUDz5EdKNJEVSKD3Ss3W3zLl8okMANdbg4ibEia4znAWOZibMo1Uk0yc8SPXa8/640?wx_fmt=png&from=appmsg "")  
### /index1.php?help=true&connect=false  
  
在页面探测过程中发现该带参 URL，尝试修改参数值，将 connect=true 改为 connect=false 后，页面出现明显报错，暴露了部分服务端的运行信息，为后续漏洞挖掘提供了方向。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUxa5sPdsZhXEBPZRicI9lcu7HMU7Es62vQdFIFzqeDb7QyEibMbpfFpmDgcJEvebZpI6uIHsaoBpgNvaUB4xRPNhIkvmibSFfibFVQ/640?wx_fmt=png&from=appmsg "")  
### 文件包含漏洞  
  
基于前述参数修改的报错信息，推测页面存在文件包含漏洞，构造本地文件包含 payload 进行测试，执行后成功读取到系统相关文件，验证了文件包含漏洞的存在。  
  
随手一测，发现有东西  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUwn7OzibU6icITuXSRra3YyqLSJYsryFhyosKdGM42WvpFVuX28rPwlVLVlvBCtXGMTbLAftzdXbL1fKugfV1jYrjalaQvBs0BWY/640?wx_fmt=png&from=appmsg "")  
### Webmin的漏洞查找  
  
根据 nmap 扫描得到的 Webmin 版本信息，在 exploit-db 等漏洞库中检索对应版本的漏洞，重点查找文件泄露、远程代码执行、未授权访问等类型的漏洞，筛选可利用的漏洞利用方案。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUzHt57frzT65SFakkszicqtaLoAiaxSZNzJmpE4via3OLsBqYnbURXlibVCqS7EJ4SnibcjddGzcnsicP4ZFUsib0pczII9Bor7orE3Yg/640?wx_fmt=png&from=appmsg "")  
### 尝试包含出密码文件我们直接进行破解即可  
  
利用已验证的文件包含漏洞，构造 payload 尝试读取/etc/passwd  
、/etc/shadow  
等系统密码文件，尝试多次后均未成功，推测存在路径过滤、权限限制等防护措施，该方式暂时无法利用。  
  
这个没戏  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUwqFkp06BVlMneahBCKGZN6B2WM8aibLbjIso6DiadxqInrhCI5IicLC7hgUa155qhvNzPYJdOSyTNJia0gnVXtxAsLkkurg9zJ1yI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUyuDxm0LFPUd6Swg4AGU5opQHNWic8vicDqNBUfh7wb0vwflBu9FFiaGBy8beGLibX2rH0qqK1IjFXYKicDAVzSXpwtyxZqxjwuef6c/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUyofCIx0fpIuV03ykyo8ytugzV40sWdJZibZOx9kRlns3RbutyCZK1NXRZF5RwuhpQEnpia55SxygkmPYrtBUuYE9yjLXLlXfulI/640?wx_fmt=png&from=appmsg "")  
### 2017.pl  
  
在漏洞库中下载多个 Webmin 相关漏洞利用脚本，依次修改脚本中的目标 IP、端口等配置信息并执行测试，经过多次尝试，2017.pl 脚本可成功运行，且能与靶机建立有效交互。  
  
经过不断尝试，终于有一个可以使用的了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUxAcnhynk6JQibHQiaL5vJeyRPUDjs0n8NcjEIAzhqz1RfhxmmMRhB9H92y8h2ALYuUvQN9UKSNYSibTDga9wyVlLoH897G1PMefE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUzMX7fA6y6Bkf4sFMj9wK9mQUH96KicgE0enP3DfeukY6iabh3HHn1xL7WFN0TYZQRMgv7z0pnKe339pkkjZsE1dGEjyhnltJOmY/640?wx_fmt=png&from=appmsg "")  
### 制作字典开始爆破  
  
结合靶机相关信息，使用工具制作自定义爆破字典，同时结合常用弱口令字典，针对靶机的 SSH、Webmin 等服务进行账号密码爆破，为后续内网登录做准备。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUxouWRWNSmjzGK4hTYFkYG1v7Yb184C4ZTSIiazxSwsuooxKTlibxsmfiaicJ0JUtdSvSajSeI7WRHql4FxaFv2qa2FFe09EVUckIk/640?wx_fmt=png&from=appmsg "")  
## 三、内网渗透  
### ssh进内网  
  
通过爆破获取到靶机的 SSH 账号密码，账号为 vmware，密码为 h4ckm3，执行以下命令成功登录靶机内网，获取普通用户权限。  
```
sudo ssh vmware@192.168.126.195
h4ckm3

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUwSPbkCykL4ibnxHvbupj7XNrAgYCgPTm7TVGZh6ua1uotg1cbvyp4B6CRgHibHMF2wfVmMztdmo03UV8ciafib4oiadROcaxolfL1E/640?wx_fmt=png&from=appmsg "")  
### 尝试提权  
  
登录后执行sudo -l  
、id  
等命令查看当前用户权限，同时查找系统中的 SUID 文件、可写配置文件等，尝试常规提权方式，未发现可直接利用的提权点。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUyIeP3JlRkiaX9dA4J66vww5qve1OfGgvatXqgKnHltA7ib05ibvxAeNcPZXXgZsUWibSqWqJCtol7NMnvGl52XsIDyHicj7XWuarZ8/640?wx_fmt=png&from=appmsg "")  
### 尝试内核提权  
  
执行uname -r  
查看靶机内核版本，在漏洞库中检索对应内核版本的提权 EXP，下载并编译运行，尝试内核提权，未成功触发提权漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUyqfbv8yjh49NWouVrwECbic6vyfgl2b8zhZ9cOxGgsRxfJvfj6RbJ8RHsrQicbOlTYLK3JOLCbsFKApfLOT7LrkibRqgRmMLH2PI/640?wx_fmt=png&from=appmsg "")  
### 提权  
  
通过 Webmin 文件泄漏漏洞成功读取到系统 shadow 文件内容，该文件权限较高，由此判断靶机存在提权漏洞。构造反弹 shell payload，在靶机上执行后，本地监听端口成功接收到反弹 shell，实现提权操作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XKicKxfY0KUwp2FicmybFdd62IqNVN7yrBhfpcHBr2cdfETkK6ukt2icOx83IxEQqfEL1tWyTU9HVGxZPqOxCreyzLc1XUmnUc5CBNz0BefTLI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XKicKxfY0KUyKCG6oAHM0AM9PUV8F0rzMiaJQHJRu4CmAQA2pyvxxru5licX28ol9565QISgkyW5rPLFNqHHggENxVD0D66NYicsO72MDGdxHKU/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O6A4XsPticNXIX6gxStPECqos3h70TEk5Q0ZRrOB8OXeD6gUdIFemic8a99eW2OKQRicSGk4M0UkbaN9zd1xC31SQ/640 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/U2XabLQoGIL1ibicuWXvE4WZib2ia6qpDPLUKic2McgsaetsxntL0btiazTxFPDKAI67icENdgk1LVD89DtMfZ7oNcP2Q/640?wx_fmt=jpeg&from=appmsg "")  
  
-扫码进交流群关注最新消息-  
  
微信号|  
wxid_g1bni0g9fdil22  
  
公众号|数字序言  
  
  
