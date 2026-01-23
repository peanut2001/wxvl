#  谁在线上？利用 Windows Telephony Service 服务器模式漏洞：从任意文件写入到 RCE  
Sergey Bliznyuk
                    Sergey Bliznyuk  securitainment   2026-01-23 15:56  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://swarm.ptsecurity.com/whos-on-the-line-exploiting-rce-in-windows-telephony-service/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Sergey Bliznyuk</span></section></td></tr></tbody></table>  
几十年来，Windows 一直支持 computer telephony integration (计算机电话集成)，为应用程序提供了管理电话设备、线路与通话的能力。尽管现代部署越来越依赖基于云的 telephony 解决方案，但经典的 telephony 服务在 Windows 中仍然默认可用，并且依旧在一些专门场景中被使用。因此，这些遗留的 telephony 组件仍然构成了默认 Windows 攻击面的一个组成部分。  
  
本文研究探讨了我在 Telephony Service 的 server mode 中发现的一处漏洞：它允许低权限客户端向 Telephony Service 可访问的文件写入任意数据，并在特定条件下实现远程代码执行。  
## Windows Telephony 概览  
  
Windows 通过 Tele­pho­ny Ap­pli­ca­tion Pro­gram­ming In­ter­face (TAPI) 对外提供 telephony 功能，使用户态应用可以通过统一的抽象层与 telephony 设备和服务交互。  
  
TAPI 主要有两种形态：TAPI 2.x 提供过程式的 C 风格 API；TAPI 3.x 则基于 COM 实现。虽然两套 API 形式不同，但它们依赖相同的底层架构：应用与 TAPI runtime 通信，由后者把请求转发给 Telephony Service Providers (TSPs)。  
  
TSP 是由厂商提供的组件，用于封装特定设备或服务的逻辑，并与底层的 telephony backend 对接，例如物理 telephony 硬件、PBX 系统或 VoIP endpoint。对客户端应用而言，这些差异都被 TAPI 抽象层屏蔽了。  
## 什么是 Telephony Service  
  
应用与 Windows telephony stack 的交互方式主要有两种：调用 tapi32.dll  
导出的 TAPI 2.x functions，或使用 tapi3.dll  
提供的 TAPI 3.x COM interface。在这两种情况下，这些库大多扮演客户端 wrapper 的角色：负责封送 (marshal) 请求，并将其转发给真正实现 telephony 逻辑的系统服务。  
  
这个系统服务就是 Telephony  
服务 (TapiSrv  
)。它实现了实际的 TAPI 功能，并通过 tapsrv  
RPC 接口将能力暴露给客户端应用。当应用调用 TAPI 时，请求最终由 TapiSrv  
处理：它选择合适的 TSP，并协调相应的底层交互过程。  
  
该服务以 NETWORK SERVICE  
账号运行，启动类型为手动，但当某个进程首次通过 tapi32.dll  
或 tapi3.dll  
发起 TAPI 请求时，它会被按需自动启动。其完整实现位于 tapisrv.dll  
库中。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMxQQMfOm7AdTAj5Ks3iaYM9ibcOH3uO8PjJNMe3rpsZUc4E0grOeDwQXZHK9ib25ia6MxVPNHubvmeaw/640?wx_fmt=png&from=appmsg "")  
  
(该图来自 MSDN，虽然已经过时，但有助于理解整体结构)  
## TAPSRV RPC 接口  
### 概述  
  
TAPI client 与 Telephony service 之间通过一个名为 tapsrv  
的经典 MSRPC 接口通信。其对应协议 MS-TRP 已经 公开文档化。**默认情况下，这个接口仅允许本地调用者访问**  
。  
  
但在 Windows Server 系统上，TAPI 可以  
被配置为接受远程客户端连接。该行为由以下注册表值控制：  
  
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Telephony\Server\DisableSharing  
  
也可以通过 Telephony  
MMC 管理单元 (TapiMgmt.msc  
) 进行配置。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMxQQMfOm7AdTAj5Ks3iaYM9GbF4oQ2DIJyJgzc4byOsGkxR9ky1SIaFsXqUBokZ9VVWAQjIklLxdA/640?wx_fmt=png&from=appmsg "")  
  
虽然把本地 modem 或 telephony 设备远程共享出来通常用处不大，但该功能确实适用于 PBX 系统或电话交换机等 server-side telephony 部署场景。在这些场景中，telephony 硬件及其配套 TSP 会集中安装在服务器上，多台支持 TAPI 的客户端远程连接，而无需各自维护独立的 TSP 安装。客户端可通过 tcmsetup /c <SERVER NAME>  
命令配置使用远程 TAPI server。  
  
启用远程访问后，该接口会通过 tapsrv  
named pipe 暴露出来，这意味着客户端必须先通过 SMB 完成认证才能建立连接。在这种配置下，TAPI server 还会向 Active Directory 发布与服务相关的信息，使其在域环境中相对容易被发现。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMxQQMfOm7AdTAj5Ks3iaYM999Nmibyrb7VmNbRG5ZAezeZiaicxbLbEwxQfIKiaLqJWN0ib9RqlDCzAtiaA/640?wx_fmt=png&from=appmsg "")  
### 请求分发模型  
  
tapsrv  
RPC 接口非常精简，只包含 三个可调用方法：ClientAttach  
、ClientDetach  
和 ClientRequest  
。前两个分别负责会话的建立与销毁；而所有与 telephony 相关的操作都通过 ClientRequest  
触发。  
  
ClientRequest  
接受一个二进制 blob，表示序列化后的请求包。该包的前 4 字节是 Req_Func  
字段，它作为索引进入内部的 dispatch table；其余部分则是针对所选操作封送后的参数。  
  
MS-TRP 规范基本记录了支持的 Req_Func  
值及其对应的 packet 布局，并且与 Win32 TAPI 2.x 的 API surface 高度相似。从概念上讲，这相当于在 MSRPC 之上又增加了一层分发逻辑，本质上是“RPC 套 RPC”的设计。类似的模式也出现在其他 Windows 服务中，例如 RasMan  
服务暴露的 RASRPC 接口 (我几个月前也在那发现过一个 LPE)。  
### 客户端会话建立  
  
在 TAPI 的术语中，_client_ 指连接到 TAPI server 接口的机器；而 line application  
则是运行在该 client 上、发起 telephony 请求的程序。客户端会话通过调用 ClientAttach  
建立，其函数签名如下：  
```
longClientAttach(     [out]   PCONTEXT_HANDLE_TYPE *pphContext,     [in]    long    lProcessID,     [out]   long   *phAsyncEventsEvent,     [in, string]    wchar_t *pszDomainUser,     [in, string]    wchar_t *pszMachine    );
```  
  
在会话初始化阶段，服务会评估调用者的安全上下文，并给 client 分配内部的权限标记 (privilege flags)。后续的多种 telephony 操作会基于这些标记来控制对敏感功能的访问。  
```
CheckTokenMembership(hClientToken, pBuiltinAdministratorsSid, &bIsLocalAdmin);if (bIsLocalAdmin || IsSidLocalSystem(hClientToken)) {    ptClient->dwFlags |= 8;}if (bIsLocalAdmin || IsSidNetworkService(hClientToken)                  || IsSidLocalService(hClientToken)                  || IsSidLocalSystem(hClientToken)) {     ptClient->dwFlags |= 1;}if (TapiGlobals.dwFlags & TAPIGLOBALS_SERVER) {if ((ptClient->dwFlags & 8) == 0 ) {wcscpy ((WCHAR *) InfoBuffer, szDomainName);wcscat ((WCHAR *) InfoBuffer, L"\\");wcscat ((WCHAR *) InfoBuffer, szAccountName);if (GetPrivateProfileIntW("TapiAdministrators",                          (LPCWSTR) InfoBuffer,0, "..\\TAPI\\tsec.ini"                        ) == 1) {            ptClient->dwFlags |= 9;        }    }}
```  
  
从这段逻辑可以看出：标记值 8  
对应管理权限 (本地管理员或 SYSTEM)；标记值 1  
则分配给服务账号。当启用 TAPI server mode 时，C:\Windows\TAPI\tsec.ini  
中 [TapiAdministrators]  
段落明确列出的用户也会被授予提升后的权限。  
  
随后，为了调用与 line  
抽象相关的方法，client 需要通过发送 Initialize 请求来初始化 line application  
实例。  
### 异步事件处理  
  
Telephony 天生是事件驱动的：来电、状态变化以及媒体事件可能独立于 client 请求而发生。由于 MSRPC 采用同步的 request-response 模型，MS-TRP 协议实现了自己的机制，用于将 Telephony service 的异步事件投递给已连接的 client。  
  
事件投递模型在初次 ClientAttach  
调用时协商确定，并会根据 client 是本地还是远程而有所不同。  
  
对于本地 client，异步事件通过共享的同步对象投递。client 在 ClientAttach  
中提供进程标识 (lProcessID  
)，并获得一个事件对象的 handle。当事件数据可用时，Telephony service 会 signal 该事件，提示 client 通过发送 GetAsyncEvents  
请求来取回待处理数据。  
  
启用 TAPI server mode 后，协议提供两种替代机制来投递异步事件：_push_ 与 _pull_。具体采用哪种模型取决于 ClientAttach  
的入参。  
  
在 push  
模式下，client 将 pszDomainUser  
置空，并在 pszMachine  
参数中提供用引号分隔的 RPC string binding (例如 CLIENT-PC-NAME"ncacn_ip_tcp"31337"  
)。Telephony service 会向该 endpoint 建立反向 RPC 连接，绑定 remotesp 接口，并在异步事件发生时调用 RemoteSPEventProc  
方法。  
  
在 pull  
模式下，client 在会话初始化时通过 pszDomainUser  
参数指定一个 mailslot 名称。Telephony service 会周期性地向该 mailslot 发送 DWORD  
大小的数据报，以提示有事件可供取回；client 随后通过 GetAsyncEvents  
拉取对应的事件数据。  
  
无论采用哪种模型，server 都通过 client 在 Initialize  
packet 中提供的 InitContext  
字段值，把事件与某个特定的 line application 关联起来。该值被视为一个不透明的 4 字节标识符，并会作为该应用事件通知的一部分由 server 回显给 client。  
## Mailslot 小把戏  
  
Mailslot 是一种遗留的 Windows IPC 机制，用于传输小型的单向消息。mailslot 写入端向一个命名 endpoint 发送数据报，而接收端被动读取收到的消息。从 client 侧来看，mailslot 可通过标准 Win32 文件 API (例如 CreateFile  
、WriteFile  
、CloseHandle  
) 进行访问。  
  
mailslot 使用如下特殊路径语法来寻址：  
  
\\<COMPUTERNAME>\MAILSLOT\<MailslotName>  
  
对 client 而言，得到的 handle 行为类似一个只能写入的文件。跨网络时，mailslot 消息通过 NetBIOS-over-UDP 数据报传输 (或者说曾经如此：自 Windows 11 24H2 起远程 mailslot 已被禁用)。由于通信严格单向，发送方不会收到远程 mailslot 是否存在、消息是否被处理的任何确认。  
  
如前一节所述，Telephony service 在 pull  
异步事件模型中会周期性地向 client 提供的 mailslot 名称发送数据报，从而通知远程 client 存在待处理事件。ClientAttach  
中负责初始化 mailslot handle 的关键代码路径如下：  
```
if (wcslen (pszDomainUser) > 0)        {if ((ptClient->hMailslot = CreateFileW(                        pszDomainUser,                        GENERIC_WRITE,                        FILE_SHARE_READ,                        (LPSECURITY_ATTRIBUTES) NULL,                        OPEN_EXISTING,                        FILE_ATTRIBUTE_NORMAL,                        (HANDLE) NULL                    )) != INVALID_HANDLE_VALUE)            {goto ClientAttach_AddClientToList;            }            ...        }
```  
  
关键点在于：服务直接将用户可控的 pszDomainUser  
字符串传给 CreateFileW  
，却没有校验它是否指向 mailslot 路径——既没有检查路径是否以 \\*\MAILSLOT\  
命名空间开头，也没有验证它是否对应一个 mailslot 对象。  
  
因此，client 可以把 pszDomainUser  
伪装成任意文件路径，而不是 mailslot 名称。只要目标文件已存在且对 NETWORK SERVICE  
账号可写，Telephony service 就能成功打开它，并在后续将异步事件数据写入该文件。换言之，基于 mailslot 的事件投递机制可以被“改造”为一个在服务安全上下文下执行的任意文件写入原语。  
## 构造文件写入原语  
  
到这里为止，攻击者已经控制了 Telephony service 把数据写到 哪里_；剩下的问题是写入的   
内容_ 是什么。  
  
如前所述，在 pull  
异步事件模型中，Telephony service 通过向 client 指定的 mailslot 写入单个 DWORD  
值来发送通知。这个值实际上对应于产生该事件的 line application 在初始化时提供的 InitContext  
字段。  
  
由于 InitContext  
完全由用户控制，并且 mailslot 路径本身又可以被重定向到任意文件，所以每次生成事件都会导致一次对指定文件的受控 4 字节写入。剩下的挑战是如何可靠地按需触发此类事件。  
  
追踪异步事件入队的代码路径可以发现，许多路径深埋在 telephony 的通话处理逻辑之中。与其直接尝试触达这些路径，一个更简单且更可靠的办法是通过 NotifyHighestPriorityRequestRecipient  
来触发事件。  
  
该辅助函数会把事件投递给全局唯一的“最高优先级”(highest-priority) line application。关键在于，它可以通过未公开的 TRequestMakeCall  
packet (Req_Func = 121  
) 被远程触发；而这个 packet 正是公开 API tapiRequestMakeCall 的后端实现。  
  
当 client 通过未公开的 LRegisterRequestRecipient  
handler (Req_Func = 61  
) 注册或取消注册为 request recipient 时，最高优先级 line application 会被重新计算；该 handler 对应公开 API lineRegisterRequestRecipient 的后端实现。  
  
相关逻辑如下：  
```
if (dwRequestMode & LINEREQUESTMODE_MAKECALL)            {if (!ptLineApp->pRequestRecipient)                {// Add to request recipient list                    PTREQUESTRECIPIENT  pRequestRecipient;                    pRequestRecipient->ptLineApp = ptLineApp;                    pRequestRecipient->dwRegistrationInstance =                        pParams->dwRegistrationInstance;EnterCriticalSection (&gPriorityListCritSec);if ((pRequestRecipient->pNext =                            TapiGlobals.pRequestRecipients))                    {                        pRequestRecipient->pNext->pPrev = pRequestRecipient;                    }                    TapiGlobals.pRequestRecipients = pRequestRecipient;LeaveCriticalSection (&gPriorityListCritSec);                    ptLineApp->pRequestRecipient = pRequestRecipient;// Recalculate global highest-priority client                    TapiGlobals.pHighestPriorityRequestRecipient = GetHighestPriorityRequestRecipient();if (TapiGlobals.pRequestMakeCallList)                    {NotifyHighestPriorityRequestRecipient();                    }                }                ...            }
```  
  
优先级依据“应用模块名”在某个列表中的出现顺序来确定：  
```
PTREQUESTRECIPIENT GetHighestPriorityRequestRecipient(){    BOOL               bFoundRecipientInPriorityList = FALSE;    WCHAR             *pszAppInPriorityList,                      *pszAppInPriorityListPrev = (WCHAR *) LongToPtr(0xffffffff);    PTREQUESTRECIPIENT pRequestRecipient,                       pHighestPriorityRequestRecipient = NULL;    WCHAR *pszPriorityList = NULL;EnterCriticalSection (&gPriorityListCritSec);    pRequestRecipient = TapiGlobals.pRequestRecipients;if (RpcImpersonateClient(0) == 0)    {// Fetch the priority list for current userGetPriorityListTReqCall(&pszPriorityList);    }while (pRequestRecipient)    {// Calculate the index of app's module name in priority listif (pszPriorityList &&            (pszAppInPriorityList = wcsstr(                pszPriorityList,                pRequestRecipient->ptLineApp->pszModuleName                )))        {if (pszAppInPriorityList <= pszAppInPriorityListPrev)            {                pHighestPriorityRequestRecipient = pRequestRecipient;                pszAppInPriorityListPrev = pszAppInPriorityList;                bFoundRecipientInPriorityList = TRUE;            }        }elseif (!bFoundRecipientInPriorityList)        {            pHighestPriorityRequestRecipient = pRequestRecipient;        }        pRequestRecipient = pRequestRecipient->pNext;    }LeaveCriticalSection (&gPriorityListCritSec);return pHighestPriorityRequestRecipient;}
```  
  
该列表在模拟 (impersonate) client 的情况下从注册表中读取：  
```
RPC_STATUS GetPriorityListTReqCall(WCHAR **ppszPriorityList){    HKEY hKey = NULL;    HKEY phkResult = NULL;EnterCriticalSection(&gPriorityListCritSec);if ( !RegOpenCurrentUser(0xF003F, &phkResult) )    {if ( !RegOpenKeyExW(                phkResult,L"Software\\Microsoft\\Windows\\CurrentVersion\\Telephony\\HandoffPriorities",0,0x20019,                &hKey) )            {// Load the value from the specified registry keyGetPriorityList(hKey, L"RequestMakeCall", ppszPriorityList);RegCloseKey(hKey);            }RegCloseKey(phkResult);    }LeaveCriticalSection(&gPriorityListCritSec);returnRpcRevertToSelf();}
```  
  
具体来说，服务会读取 client 的 HKCU  
hive 下的以下键值：  
  
HKCU\Software\Microsoft\Windows\CurrentVersion\Telephony\HandoffPriorities\RequestMakeCall  
  
默认情况下，这个列表通常只包含一个条目：DIALER.EXE  
。如果需要，还可以通过未公开的 LSetAppPriority  
请求 (Req_Func = 69  
) 插入额外条目。  
  
用于优先级比较的 pszModuleName  
字段由 client 在 Initialize  
packet 中提供，这让攻击者能够完全控制自己的 line application 如何被排序。  
  
有了以上拼图，就可以在 NETWORK SERVICE  
安全上下文下构造一个可靠的任意 DWORD  
写入原语。  
  
首先，攻击者通过调用 ClientAttach  
建立 client 会话，并在 pszDomainUser  
参数中指定目标文件路径。这会使 Telephony service 打开该文件一次，并保留得到的 handle，以供后续事件通知写入使用。  
  
对于每一个需要写入的 4 字节值，攻击者按如下步骤操作：  
1. 提交 Initialize  
packet (Req_Func = 47  
)，并设置：  
  
1. InitContext  
为期望写入的 DWORD  
值  
  
1. pszModuleName  
为 DIALER.EXE  
(或其他高优先级条目)  
  
1. 使用 LRegisterRequestRecipient  
将该 line application 注册为 request recipient  
(Req_Func = 61  
、dwRequestMode = LINEREQUESTMODE_MAKECALL  
、bEnable = 1  
)。  
  
1. 提交 TRequestMakeCall  
packet (Req_Func = 121  
) 触发事件。  
  
1. 使用 GetAsyncEvents  
(Req_Func = 0  
) 出队事件，从而完成写入。  
  
1. 取消注册 request recipient (LRegisterRequestRecipient  
、bEnable = 0  
)。  
  
1. 使用 Shutdown  
(Req_Func = 86  
) 关闭 line application。  
  
重复执行上述序列，攻击者就能向任意一个“已存在且对 Telephony service 可写”的文件写入任意数据。  
## 从文件写入到 RCE  
  
在这个阶段，要实现利用需要一个 NETWORK SERVICE  
可写的既有文件。一个非常显眼的候选项就是前面提到的 C:\Windows\TAPI\tsec.ini  
。在以 server mode 运行 Telephony service 的系统上，该文件一定存在，并且对服务账号可写。  
  
该文件在其他配置项之外，还定义了哪些用户会被 Telephony service 视为管理员。通过在 [TapiAdministrators]  
下添加条目 (例如 "[TapiAdministrators]\r\nDOMAIN\\attacker=1"  
)，远程的低权限域用户就可以为自己在 Telephony service 内授予管理员权限。完成修改后再通过 ClientAttach  
建立新会话，就会得到一个带有管理权限标记的 client context。  
  
一旦拥有 Telephony service 的管理权限，就可以访问更多的攻击面。其中一个非常强力的原语来自 MS-TRP 协议文档中的 GetUIDllName请求。  
  
根据规范：  
> GetUIDllName packet 与 TUISPIDLLCallback packet、FreeDialogInstance packet 一起，用于在服务器上安装、配置或移除 TSP。  
  
  
查看实现可以发现：非管理调用者只能从注册表中预定义的列表里选择 provider；而管理 client 则被允许从任意路径加载 provider DLL。  
```
switch (pParams->dwObjectType)     {case TUISPIDLL_OBJECT_LINEID:             ...case TUISPIDLL_OBJECT_PHONEID:             ...case TUISPIDLL_OBJECT_PROVIDERID:// If the client is not admin and is requesting to// remove a provider or to install one from the path// supplied in request (rather than by index in registry),// return an errorif ((ptClient->dwFlags & 8) == 0 && (pParams->bRemoveProvider || pParams->dwProviderFilenameOffset != TAPI_NO_DATA)) {                 pParams->lResult = LINEERR_OPERATIONFAILED;return;             }if (pParams->dwProviderFilenameOffset != TAPI_NO_DATA) {// The path is supplied in request                 TCHAR   *pszProviderFilename = pDataBuf + pParams->dwProviderFilenameOffset;if (ptDlgInst->hTsp = LoadLibrary(pszProviderFilename)) {if (pfnTSPI_providerUIIdentify = (TSPIPROC) GetProcAddress(ptDlgInst->hTsp,"TSPI_providerUIIdentify")) {                         pParams->lResult = pfnTSPI_providerUIIdentify(pszProviderFilename);                     } else {                         ...                     }                 } else {                     ...                 }             } else {                 ....             }     }
```  
  
通过提交一个 GetUIDllName  
请求，将 dwObjectType  
设为 TUISPIDLL_OBJECT_PROVIDERID  
，并指定攻击者可控的 DLL 路径，我们就能让 Telephony service 加载该 DLL 并调用其导出的 TSPI_providerUIIdentify  
函数。这在服务上下文中提供了一个直接且可靠的代码执行原语。更进一步，如果该导出函数返回非零值，服务会在调用后卸载该 DLL，从而允许后续将 payload 从磁盘移除。  
  
一个显而易见的投递方式是指定指向攻击者控制的 SMB 共享的 UNC 路径。实践中，当该共享托管在同一域内的标准 Windows 机器上时，这通常能稳定工作。然而，攻击者自建的 SMB server (例如 impacket-smbserver  
或 Samba) 可能触发 guest access 限制，导致 LoadLibrary  
以 ERROR_SMB_GUEST_LOGON_BLOCKED  
失败。  
  
由于已经拥有任意文件写入原语，一个可靠的替代方案是在本地落地 DLL。  
  
可以使用 accesschk  
来识别合适的可写文件。例如，下列文件在几乎所有系统上都倾向于存在：  
- C:\Windows\System32\catroot2\dberr.txt  
- C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpCmdRun.log  
- C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpSigStub.log  
尽管通过 4 字节的事件写入来拼接一个“payload 大小”的 DLL 相对较慢，但这能彻底消除对外部基础设施的依赖。  
  
为了演示代码执行，可以构造一个最小的 proof-of-concept TSP DLL。在下例中，Telephony service 在安装 provider 时会调用导出函数 TSPI_providerUIIdentify  
；该函数执行一条命令并将结果写入磁盘：  
```
#include<Windows.h>extern"C" __declspec(dllexport)LONG __stdcall TSPI_providerUIIdentify(LPWSTR lpszUIDLLName){wchar_t cmd[] = L"cmd.exe /c whoami /all > C:\\Windows\\Temp\\poc.txt";    STARTUPINFO si;    PROCESS_INFORMATION pi;ZeroMemory(&si, sizeof(si));    si.cb = sizeof(si);ZeroMemory(&pi, sizeof(pi));if (CreateProcessW(NULL, cmd, NULL, NULL, FALSE, CREATE_NO_WINDOW | NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi))    {CloseHandle(pi.hProcess);CloseHandle(pi.hThread);    }return0x1337;}
```  
  
TSPI_providerUIIdentify  
的返回值会被回传给 RPC client，从而提供一个清晰的信号来表明 payload 已被执行：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMxQQMfOm7AdTAj5Ks3iaYM9InubXXrmjgucAURF0359FLQJPOpt9QqX7gj8LWyKRWWdicmEiaesZOvw/640?wx_fmt=png&from=appmsg "")  
## 披露与补丁时间线  
- **Nov 6, 2025**  
– 向 Microsoft 报告漏洞。  
  
- **Dec 22, 2025**  
– Microsoft 确认该问题属于安全漏洞。  
  
- **Dec 23, 2025**  
– 在 Microsoft Bug Bounty Program 下获得 $5,000 奖励。  
  
- **Dec 29, 2025**  
– 分配 CVE-2026-20931。  
  
- **Jan 13, 2026**  
– 作为 2026 年 1 月 Patch Tuesday 更新的一部分发布修复。  
  
- **Jan 19, 2026**  
– 发布本文。  
  
该漏洞遵循 coordinated vulnerability disclosure 实践进行披露。Microsoft 的公告可在 2026 年 1 月 Security Update Guide 中的 CVE-2026-20931 条目下找到。  
## 结论  
  
本研究表明，即便是很少被使用的 Windows 遗留子系统，也仍可能暴露出复杂且强力的攻击面。对 TAPI 的探索比我预期的有趣得多——这也提醒我们，一些最有收获的研究往往藏在平台中那些容易被忽略的角落里。  
  
最后值得强调的是：本文描述的漏洞 **仅影响将 TAPI 配置为 server mode 的系统**  
。这是一种面向集中式 telephony 基础设施的相对少见配置，因此在现实环境中的暴露面会显著受限。  
  
---  
> Who’s on the Line? Exploiting RCE in Windows Telephony Service  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
