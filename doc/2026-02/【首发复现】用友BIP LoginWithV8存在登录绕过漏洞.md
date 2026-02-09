#  【首发复现】用友BIP LoginWithV8存在登录绕过漏洞  
阿伟
                    阿伟  船山信安   2026-02-09 10:45  
  
**免责声明**  
  
由于传播、利用本公众号船山信安所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号  
船山信安  
及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
### 一、漏洞描述  
  
用友BIP 系统/bi/api/Portal/LoginWithV8/ 接口在处理ticket 认证参数时，未校验票据有效性、未验证用户身份合法性、未做权限隔离。攻击者通过传入ticket=admin 即可绕过正常登录流程，直接获取管理员有效 Token；利用该 Token 可未授权访问系统接口，枚举、获取用户账号、密码等敏感信息，实现完全登录绕过。  
严重威胁企业数据安全与系统完整性。  
### 二、影响版本  
  
用友  
BIP  
### 三、Fofa语法  
  
body="YonBIP | 数据应用服务"  
### 四、漏洞复现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPHY8ArhalbniabcVaianIh1K4aQGpw20GVQc0Snibeaa6RLMTyrz23WJ2dh4OS5KE4oUodQvfgde1gecKiadicgjouK9MNqUyibcSX0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMxwFib825s0eRsuZJ8WRKiak6awd8vBq4lOLq9M4nniaeZ1lYgh3cz138GJIPMN8nUlHah0pQUFkia7BhYiaXnOgxA1rELeafsCgTo/640?wx_fmt=png&from=appmsg "")  
### 五、漏洞修复  
  
·  
    
升级用友  
 BIP 至官方最新安全版本，应用厂商发布的安全补丁。  
  
·  
    
关闭非必要测试  
 / 调试接口，限制接口访问来源 IP。  
  
·  
    
启用接口防暴力破解、  
IP 限流、异常请求拦截策略。  
  
·  
    
对所有单点登录、票据登录、免登接口开展安全审计，避免同类弱校验漏洞。  
### 六、漏洞脚本下载  
  
后台回复260209  
 获取poc  
###   
  
  
