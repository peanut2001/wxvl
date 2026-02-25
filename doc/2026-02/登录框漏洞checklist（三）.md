#  登录框漏洞checklist（三）  
原创 游山玩水
                    游山玩水  山水SRC   2026-02-25 05:17  
  
## 概述  
  
本文讲解了在渗透测试中遇到登录框时进行测试的部分checklist（检查表单）  
## Vue梭哈（前端路由未授权访问）  
  
存在原因：在前后端分离架构中，前端路由由Vue Router等客户端框架管理，页面跳转和渲染在浏览器中完成。如果后端API接口**缺乏对每个请求进行有效的身份验证和授权检查**  
，那么攻击者即使未登录，也可能通过直接访问前端路由对应的URL，或直接调用后端API来获取未授权数据  
  
测试方法：  
  
①发现vue框架  
  
使用Chrome浏览器插件  
wappalzer（如何安装自己搜教程）/url带有#（比如https://wwww.xxx.com/admin/#/user）  
  
使用界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8tDOXFoCoQibfCYZw7uIvovBKvaG3CTOXiaYHd77918eYw1iafsicQb3T1fh4NGyu1V58IZVmVbNj9dOal55m87f4JzVgibe9icHrNsz48qPziaiaFw/640?wx_fmt=png&from=appmsg "")  
  
②使用插件AntiDebug_Breaker获取url路由  
  
地址：  
https://github.com/0xsdeo/AntiDebug_Breaker  
  
使用界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8tDOXFoCoQic8iajEkwmwloGVugX5H1RZgwQK3EbLv9sicAJnyND4vhWWzgedaxtz7Q5WTU1V5zbsECv4kL9Tp5zRUMP7ibKRiaqyAwVZ321cHOo/640?wx_fmt=png&from=appmsg "")  
  
vue的功能部分全部打开，刷新需要检测的页面，如果下面会给出url就说明可能存在该漏洞，直接点击url后面的打开就会跳转到目标页面，看是否存在敏感信息（  
插件列出路由URL，只是展示了网站存在的所有前端路由路径，这**本身不能证明存在漏洞**  
。是否存在漏洞，取决于**直接访问这些路由URL时，后端是否返回了未授权的敏感数据**  
。）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8tDOXFoCoQicp6dwIrgPOeZXGG8bmzVZ18f4UoMrIn7BnFyzZFITwop7tVuVVFy0Kruupibw02iaFWEFAD3jw0CrmA5ibkmgcsOPrPUxKq0P6NQ/640?wx_fmt=png&from=appmsg "")  
  
有的点击打开后他页面会进行跳转，这时候要结合bp使用看看数据包是否存在敏感信息（有的页面没显示敏感信息，但数据包里有）  
## 恶意账号锁定  
  
案例：有些网站登录次数多后会显示账户封禁一天，那么就可以写一个脚本每天都登录错误这个账号从而导致该账号封禁（只有这个一点的漏洞不收）  
  
因此我觉得如果再存在用户枚举漏洞的话该漏洞就会收了（有大佬知道这样收不收吗），因为可以通过账号枚举举出很多账号再写脚本对爆破出的账号进行每日封禁  
  
## 注册覆盖/session覆盖  
  
注册覆盖（注册已存在用户）  
  
session覆盖：  
  
前提：步骤分步（1.输入用户名/手机号  2.输入验证码   3.输入新密码），如果是输入用户名（手机号）和验证码在一个步骤该漏洞是不是就不存在了  
  
1.A找回密码输入正确验证码到输入新密码的步骤（保持页面打开）  
  
2.B找回密码到输入验证码的步骤（同一浏览器打开新标签页）  
  
3.刷新A页面输入新密码（此时用户名从A变成了B，很可能存在该漏洞），保存  
  
4.新密码登录B账号（验证）  
  
  
