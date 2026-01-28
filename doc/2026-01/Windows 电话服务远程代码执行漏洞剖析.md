#  Windows 电话服务远程代码执行漏洞剖析  
骨哥说事
                    骨哥说事  骨哥说事   2026-01-28 16:00  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf=""><span textstyle="" style="font-size: 14px;">声明：</span></span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf=""><span textstyle="" style="font-size: 14px;">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/5235  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
![Windows Telephony](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnsdp4MNwplsibSjibav3jYNw37Dguux9NR5kBuzzk2ULHIgmkTusggxlL9PVmgjHRIjZSOePCymUTw/640?wx_fmt=png&from=appmsg "")  
  
Windows Telephony  
  
数十年来，Windows 一直支持计算机电话集成，为应用程序提供了管理电话设备、电话线路和通话的能力。尽管现代部署日益依赖基于云的电话解决方案，但经典的电话服务仍是 Windows 开箱即用的功能，并继续在特定环境中使用。因此，这些遗留的电话组件仍是 Windows 默认攻击面的一部分。  
  
本研究深入探讨了我在电话服务的服务器模式下发现的一个漏洞。该漏洞**允许低权限客户端向服务可访问的文件写入任意数据**  
，并在特定条件下实现远程代码执行。  
## Windows 电话技术概览  
  
Windows 通过 **电话应用程序编程接口 (Telephony Application Programming Interface, TAPI)**  
 向外界提供电话功能，允许用户模式应用程序通过一个统一的抽象层与电话设备和服务交互。  
  
TAPI 主要有两种形式：提供过程式 C 风格 API 的 TAPI 2.x 和使用 COM 实现的 TAPI 3.x。尽管 API 不同，但两者都依赖相同的底层架构：应用程序与 TAPI 运行时通信，该运行时将请求转发给**电话服务提供商 (Telephony Service Providers, TSPs)**  
。  
  
TSPs 是供应商提供的组件，它封装了特定于设备或服务的逻辑，并与底层电话后端（如物理电话硬件、PBX 系统或 VoIP 终端）交互。从客户端应用程序的视角来看，这些差异都被 TAPI 抽象层所隐藏。  
## 什么是电话服务 (Telephony Service)  
  
应用程序与 Windows 电话栈的交互有两种方式：调用由 tapi32.dll  
 导出的   
TAPI 2.x 函数  
，或使用由 tapi3.dll  
 提供的   
TAPI 3.x  
 COM 接口。在这两种情况下，这些库主要充当客户端包装器：它们对请求进行编组，并将其转发给实际实现电话逻辑的系统服务。  
  
这个服务就是 **_电话_服务 (TapiSrv)**  
。它实现了实际的 TAPI 功能，并通过 tapsrv  
 RPC 接口将其暴露给客户端应用程序。当应用程序调用一个 TAPI 调用时，请求最终由 TapiSrv  
 处理，它会选择合适的 TSP 并协调相应的底层交互。  
  
该服务在 NETWORK SERVICE  
 账户下运行，且配置为手动启动类型，但当进程首次通过 tapi32.dll  
 或 tapi3.dll  
 调用 TAPI 请求时，系统会按需自动启动它。整个实现驻留在 tapisrv.dll  
 库内。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnsdp4MNwplsibSjibav3jYNw9btny0F4QVPM605UAFnicxRTV76BD00OlWszT1BRpvFzQiaF0fSUaphA/640?wx_fmt=png&from=appmsg "")  
  
(此 MSDN 示意图虽已过时，但提供了大体的架构理解)  
## TAPSRV RPC 接口  
### 概述  
  
TAPI 客户端与电话服务之间的通信通过名为 tapsrv  
 的经典 MSRPC 接口进行。相应的协议 MS-TRP 是  
公开文档化的  
。**默认情况下，此接口仅限于本地调用者**  
。  
  
然而，在 Windows Server 系统上，TAPI 可以  
 配置为接受远程客户端连接。此行为由注册表值HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Telephony\Server\DisableSharing  
控制，也可以通过 电话  
 MMC 管理单元 (TapiMgmt.msc  
) 进行管理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnsdp4MNwplsibSjibav3jYNwrN5cUdkjX7M21xYhibDTE6XErvVk50MYVFUNutWEQibuUnEO49PBWdVQ/640?wx_fmt=png&from=appmsg "")  
  
虽然远程访问本地调制解调器或电话设备通常没有实际用处，但此功能是为了满足 PBX 系统或电话交换机等服务器端电话部署而存在的。在此类场景中，电话硬件和相关的 TSPs 集中安装在服务器上，多个 TAPI 感知(aware)的客户端远程连接，而无需在每个客户端上安装独立的 TSP。可以通过 tcmsetup /c <SERVER NAME>  
 命令将客户端配置为使用远程 TAPI 服务器。  
  
当启用远程访问时，接口通过 tapsrv  
 命名管道暴露，这意味着客户端必须先通过 SMB 进行身份验证以建立连接。在此配置下，TAPI 服务器还会将服务相关信息发布到 Active Directory，使得在域环境中相对容易发现它。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnsdp4MNwplsibSjibav3jYNwZWgibaxkXwtCLrGVZf7iaNSQuIoasEg8Bqhia3cWCNcFjYSwpoHpltHBA/640?wx_fmt=png&from=appmsg "")  
### 请求调度模型  
  
tapsrv  
 RPC 接口是极简主义的，仅包含  
三个可调用的方法  
：ClientAttach  
、ClientDetach  
 和 ClientRequest  
。会话的初始化和拆除由前两个调用处理，而 ClientRequest  
 用于调用所有与电话相关的操作。  
  
ClientRequest  
 接受一个单一的二进制数据块 (blob)，该数据块代表一个序列化的请求数据包。该数据包的前四个字节包含一个 Req_Func  
 字段，该字段充当内部调度表的索引。缓冲区的其余部分包含特定于选定操作的已编组参数。  
  
支持的 Req_Func  
 值集合及相应的数据包布局大多在 MS-TRP 规范中有文档记录，并紧密映射到 Win32 TAPI 2.x 的 API 表面。从概念上讲，这导致在 MSRPC 之上增加了一个额外的调度层——实质上是“RPC 内的 RPC”设计。类似的模式也出现在其他 Windows 服务中，例如由 RasMan  
 服务暴露的 RASRPC 接口（此前我也在该接口中发现过一个  
本地权限提升漏洞  
）。  
### 客户端会话建立  
  
在 TAPI 术语中，客户端  
 是连接到 TAPI 服务器接口的机器，而 线路应用程序  
 是该客户端系统上一个发出电话请求的程序。客户端会话是通过调用 ClientAttach  
 建立的，其签名如下：  
```
long ClientAttach(     [out]   PCONTEXT_HANDLE_TYPE *pphContext,     [in]    long    lProcessID,     [out]   long   *phAsyncEventsEvent,     [in, string]    wchar_t *pszDomainUser,     [in, string]    wchar_t *pszMachine    );
```  
  
在会话初始化期间，服务会评估调用者的安全上下文，并为客户端分配内部权限标志。这些标志随后被各种电话操作引用，以控制对敏感功能的访问。  
```
CheckTokenMembership(hClientToken, pBuiltinAdministratorsSid, &bIsLocalAdmin);if (bIsLocalAdmin || IsSidLocalSystem(hClientToken)) {    ptClient->dwFlags |= 8;}if (bIsLocalAdmin || IsSidNetworkService(hClientToken)                  || IsSidLocalService(hClientToken)                  || IsSidLocalSystem(hClientCommand)) {     ptClient->dwFlags |= 1;}if (TapiGlobals.dwFlags & TAPIGLOBALS_SERVER) {    if ((ptClient->dwFlags & 8) == 0 ) {        wcscpy ((WCHAR *) InfoBuffer, szDomainName);        wcscat ((WCHAR *) InfoBuffer, L"\\");        wcscat ((WCHAR *) InfoBuffer, szAccountName);        if (GetPrivateProfileIntW(                          "TapiAdministrators",                          (LPCWSTR) InfoBuffer,                          0, "..\\TAPI\\tsec.ini"                        ) == 1) {            ptClient->dwFlags |= 9;        }    }}
```  
  
基于此逻辑，标志值 8  
 对应于管理访问权限（本地管理员或 SYSTEM 账户），而标志 1  
 被分配给服务账户。当启用 TAPI 服务器模式时，明确列在 C:\Windows\TAPI\tsec.ini  
 文件 [TapiAdministrators]  
 节下的用户也会被授予提升的权限。  
  
客户端若想调用与 线路  
 抽象相关的方法，必须先通过发送一个   
Initialize  
 请求来初始化一个 线路应用程序  
 实例。  
### 异步事件处理  
  
电话本质上是事件驱动的：来电、状态变化和媒体事件可能独立于客户端请求发生。由于 MSRPC 遵循同步请求-响应模型，MS-TRP 协议实现了自己的机制，用于将异步事件从电话服务传递到已连接的客户端。  
  
事件传递模型在初始的 ClientAttach  
 调用期间协商，并根据客户端是本地还是远程而有所不同。  
  
对于本地客户端，异步事件通过一个共享的同步对象传递。客户端在 ClientAttach  
 期间提供其进程标识符 (lProcessID  
)，并收到一个事件对象的句柄。当事件数据可用时，电话服务会发出此事件的信号，提示客户端通过发出 GetAsyncEvents  
 请求来获取待处理的数据。  
  
当启用 TAPI 服务器模式时，协议提供了两种替代机制来传递异步事件：推 (push)  
 和 拉 (pull)  
 模式。所选模型由提供给 ClientAttach  
 的参数决定。  
  
在 推  
 模型中，客户端将 pszDomainUser  
 参数留空，并在 pszMachine  
 参数中提供用引号分隔的 RPC 字符串绑定（例如 CLIENT-PC-NAME"ncacn_ip_tcp"31337"  
）。电话服务会与指定的端点建立一个反向 RPC 连接，绑定到   
remotesp  
 接口，并在异步事件发生时调用 RemoteSPEventProc  
 方法。  
  
在 拉  
 模型中，客户端在会话初始化期间在 pszDomainUser  
 参数中指定一个  
邮件槽 (mailslot)  
 名称。电话服务会定期向此邮件槽发送 DWORD  
 大小的数据报，指示有事件可供检索。客户端随后应使用 GetAsyncEvents  
 来获取相应的事件数据。  
  
在所有情况下，服务器都使用客户端在 Initialize  
 数据包中提供的 InitContext  
 字段值将事件与特定的线路应用程序关联起来。该值被视为一个不透明的 4 字节标识符，并由服务器作为事件通知的一部分回显给应用程序。  
## 邮件槽的滥用  
  
邮件槽是一种遗留的 Windows 进程间通信机制，专为传输小的、单向的消息而设计。邮件槽写入器 (writer) 将数据报发送到指定的命名端点，而接收器 (receiver) 则被动读取传入的消息。从客户端角度来看，邮件槽使用标准的 Win32 文件 API 访问，如 CreateFile  
、WriteFile  
 和 CloseHandle  
。  
  
邮件槽使用一种特殊的路径语法寻址：  
  
\\<计算机名>\MAILSLOT\<邮件槽名>  
  
从客户端的角度看，获得的句柄的行为类似于只写文件。通过网络，邮件槽消息使用 NetBIOS-over-UDP 数据报传输（或者说_曾经是_——自   
Windows 11 24H2  
 起，远程邮件槽已被禁用）。因为通信是严格单向的，发送方不会收到任何关于远程邮件槽是否存在或消息是否正在被处理的确认。  
  
如前一节所述，电话服务使用 拉  
 式异步事件模型，通过定期向客户端提供的邮件槽名称发送数据报来通知远程客户端有待处理事件。ClientAttach  
 中负责初始化邮件槽句柄的相关代码路径如下所示：  
```
if (wcslen (pszDomainUser) > 0) {    if ((ptClient->hMailslot = CreateFileW(                pszDomainUser,                GENERIC_WRITE,                FILE_SHARE_READ,                (LPSECURITY_ATTRIBUTES) NULL,                OPEN_EXISTING,                FILE_ATTRIBUTE_NORMAL,                (HANDLE) NULL            )) != INVALID_HANDLE_VALUE) {        goto ClientAttach_AddClientToList;    }    ...}
```  
  
**关键在于，该服务直接将用户控制的 pszDomainUser 字符串传递给 CreateFileW，而没有验证该字符串是否引用了一个邮件槽路径**  
——没有执行任何检查来确保路径以 \\*\MAILSLOT\  
 命名空间开头，或以其他方式对应一个邮件槽对象。  
  
因此，客户端可以提供任意的文件路径，而不是一个邮件槽名称。**前提是该目标文件已存在且 NETWORK SERVICE 账户对其具有写入权限**  
，电话服务就会成功打开它，并在后续将异步事件数据写入其中。换句话说，基于邮件槽的事件传递机制可以被重新用于在服务的安全上下文中实现任意的文件写入原语。  
## 构建文件写入原语  
  
此时，攻击者控制了电话服务向 何处  
 写入数据。剩下的问题是写入 什么  
 数据。  
  
如前所述，在 拉  
 式异步事件模型中，电话服务通过向客户端指定的邮件槽写入一个 DWORD  
 值来发送通知。这个值实际上对应于生成事件的线路应用程序在初始化时提供的 InitContext  
 字段。  
  
因为 InitContext  
 完全由用户控制，并且因为邮件槽路径本身可以被重定向到任意文件，所以每个生成的事件都会导致一个可控的 4 字节数据写入到所选文件中。剩下的挑战是如何按需可靠地触发此类事件。  
  
跟踪将异步事件加入队列的代码路径发现，许多路径深嵌在电话呼叫处理逻辑中。与其尝试直接到达这些路径，更简单可靠的方法是通过 NotifyHighestPriorityRequestRecipient  
 来触发事件。  
  
这个辅助函数将事件传递给单个全局的“最高优先级”线路应用程序。**关键在于，它可以通过未记录的 TRequestMakeCall 数据包（Req_Func = 121）远程调用**  
，该数据包是已记录的   
tapiRequestMakeCall  
 API 的后端实现。  
  
最高优先级线路应用程序是在客户端通过未记录的 LRegisterRequestRecipient  
 处理器（Req_Func = 61  
）注册或取消注册为请求接收者时重新计算的。该处理器支持   
lineRegisterRequestRecipient  
 API。  
  
相关逻辑如下所示：  
```
if (dwRequestMode & LINEREQUESTMODE_MAKECALL) {    if (!ptLineApp->pRequestRecipient) {        // 添加到请求接收者列表        PTREQUESTRECIPIENT  pRequestRecipient;        pRequestRecipient->ptLineApp = ptLineApp;        pRequestRecipient->dwRegistrationInstance = pParams->dwRegistrationInstance;        EnterCriticalSection (&gPriorityListCritSec);        if ((pRequestRecipient->pNext = TapiGlobals.pRequestRecipients)) {            pRequestRecipient->pNext->pPrev = pRequestRecipient;        }        TapiGlobals.pRequestRecipients = pRequestRecipient;        LeaveCriticalSection (&gPriorityListCritSec);        ptLineApp->pRequestRecipient = pRequestRecipient;        // 重新计算全局最高优先级客户端        TapiGlobals.pHighestPriorityRequestRecipient = GetHighestPriorityRequestRecipient();        if (TapiGlobals.pRequestMakeCallList) {            NotifyHighestPriorityRequestRecipient();        }    }    ...}
```  
  
优先级是基于应用程序模块名在一个列表中的顺序决定的：  
```
PTREQUESTRECIPIENT GetHighestPriorityRequestRecipient() {    BOOL               bFoundRecipientInPriorityList = FALSE;    WCHAR             *pszAppInPriorityList,                      *pszAppInPriorityListPrev = (WCHAR *) LongToPtr(0xffffffff);    PTREQUESTRECIPIENT pRequestRecipient,                       pHighestPriorityRequestRecipient = NULL;    WCHAR *pszPriorityList = NULL;    EnterCriticalSection (&gPriorityListCritSec);    pRequestRecipient = TapiGlobals.pRequestRecipients;    if (RpcImpersonateClient(0) == 0) {        // 获取当前用户的优先级列表        GetPriorityListTReqCall(&pszPriorityList);    }    while (pRequestRecipient) {        // 计算应用程序模块名在优先级列表中的索引        if (pszPriorityList && (pszAppInPriorityList = wcsstr(pszPriorityList, pRequestRecipient->ptLineApp->pszModuleName))) {            if (pszAppInPriorityList <= pszAppInPriorityListPrev) {                pHighestPriorityRequestRecipient = pRequestRecipient;                pszAppInPriorityListPrev = pszAppInPriorityList;                bFoundRecipientInPriorityList = TRUE;            }        }        elseif (!bFoundRecipientInPriorityList) {            pHighestPriorityRequestRecipient = pRequestRecipient;        }        pRequestRecipient = pRequestRecipient->pNext;    }    LeaveCriticalSection (&gPriorityListCritSec);    return pHighestPriorityRequestRecipient;}
```  
  
这个列表是在模拟客户端身份时从注册表中获取的：  
```
RPC_STATUS GetPriorityListTReqCall(WCHAR **ppszPriorityList) {    HKEY hKey = NULL;    HKEY phkResult = NULL;    EnterCriticalSection(&gPriorityListCritSec);    if ( !RegOpenCurrentUser(0xF003F, &phkResult) ) {          if ( !RegOpenKeyExW(                phkResult,                L"Software\\Microsoft\\Windows\\CurrentVersion\\Telephony\\HandoffPriorities",                0,                0x20019,                &hKey) ) {                // 从指定的注册表键加载值                GetPriorityList(hKey, L"RequestMakeCall", ppszPriorityList);                RegCloseKey(hKey);            }        RegCloseKey(phkResult);    }  LeaveCriticalSection(&gPriorityListCritSec);return RpcRevertToSelf();}
```  
  
具体来说，服务读取客户端 HKCU  
 配置单元下的如下键：  
  
HKCU\Software\Microsoft\Windows\CurrentVersion\Telephony\HandoffPriorities\RequestMakeCall  
  
默认情况下，此列表通常包含一个条目：DIALER.EXE  
。如果需要，可以使用未记录的 LSetAppPriority  
 请求（Req_Func = 69  
）插入更多条目。  
  
用于优先级比较的 pszModuleName  
 字段由客户端作为 Initialize  
 数据包的一部分提供，这使攻击者可以完全控制其线路应用程序的排名。  
  
掌握了这些信息后，就可以构建一个在 NETWORK SERVICE  
 安全上下文下可靠地、任意写入 DWORD  
 值的原语。  
  
首先，攻击者通过调用 ClientAttach  
 建立一个客户端会话，在 pszDomainUser  
 参数中指定目标文件路径。这将导致电话服务打开该文件一次，并为后续的事件通知保留得到的句柄。  
  
对于要写入的每个 4 字节值，攻击者随后执行以下步骤：  
1. 提交一个 Initialize  
 数据包（Req_Func = 47  
），设置：  
  
1. InitContext  
 为期望的 DWORD  
 值  
  
1. pszModuleName  
 为 DIALER.EXE  
（或其他高优先级条目）  
  
1. 使用 LRegisterRequestRecipient  
（Req_Func = 61  
, dwRequestMode = LINEREQUESTMODE_MAKECALL  
, bEnable = 1  
）将线路应用程序注册为请求接收者。  
  
1. 通过提交 TRequestMakeCall  
 数据包（Req_Func = 121  
）来触发一个事件。  
  
1. 使用 GetAsyncEvents  
（Req_Func = 0  
）将事件出列，完成写入。  
  
1. 取消注册请求接收者（LRegisterRequestRecipient  
, bEnable = 0  
）。  
  
1. 使用 Shutdown  
（Req_Func = 86  
）关闭线路应用程序。  
  
重复这个序列，攻击者可以将任意数据写入电话服务可写、且已预先存在的任意文件中。  
## 从文件写入到远程代码执行  
  
在此阶段，漏洞利用需要一个已存在的、且 NETWORK SERVICE  
 对其有写入权限的文件。一个特别明显的候选文件是前面提到过的 C:\Windows\TAPI\tsec.ini  
。在运行电话服务服务器模式的系统上，此文件始终存在且服务账户对其有写入权限。  
  
该文件除了其他配置设置外，还定义了电话服务将哪些用户视为管理员。通过在 [TapiAdministrators]  
 节下添加一个条目（例如 "[TapiAdministrators]\r\nDOMAIN\\attacker=1"  
），远程的、无特权的域用户可以授予自己在电话服务内的管理权限。在此修改后，通过 ClientAttach  
 建立新会话，将导致客户端上下文被设置管理权限标志位。  
  
拥有了对电话服务的管理访问权限后，额外的攻击面变得可用。一个特别强大的原语通过   
GetUIDllName  
 请求暴露出来，该请求是 MS-TRP 协议的一部分。  
  
根据规范：  
> GetUIDllName 数据包，与 TUISPIDLLCallback 数据包和 FreeDialogInstance 数据包一起，用于在服务器上安装、配置或移除一个 TSP。  
  
  
审查其实现发现，虽然非管理调用者仅限于从注册表中预定义的提供程序列表中选择，但管理客户端被允许从任意路径加载提供程序 DLL。  
```
switch (pParams->dwObjectType) {    case TUISPIDLL_OBJECT_LINEID:        ...    case TUISPIDLL_OBJECT_PHONEID:        ...    case TUISPIDLL_OBJECT_PROVIDERID:        // 如果客户端不是管理员，并且请求移除一个提供程序，        // 或者从请求中提供的路径（而不是注册表中的索引）安装提供程序，则返回错误        if ((ptClient->dwFlags & 8) == 0 && (pParams->bRemoveProvider || pParams->dwProviderFilenameOffset != TAPI_NO_DATA)) {            pParams->lResult = LINEERR_OPERATIONFAILED;            return;        }        if (pParams->dwProviderFilenameOffset != TAPI_NO_DATA) {            // 路径在请求中提供            TCHAR *pszProviderFilename = pDataBuf + pParams->dwProviderFilenameOffset;            if (ptDlgInst->hTsp = LoadLibrary(pszProviderFilename)) {                if (pfnTSPI_providerUIIdentify = (TSPIPROC) GetProcAddress(ptDlgInst->hTsp, "TSPI_providerUIIdentify")) {                    pParams->lResult = pfnTSPI_providerUIIdentify(pszProviderFilename);                } else {                    ...                }            } else {                ...            }        } else {            ....        }}
```  
  
通过提交一个 GetUIDllName  
 请求，将 dwObjectType  
 设置为 TUISPIDLL_OBJECT_PROVIDERID  
 并指定一个攻击者控制的 DLL 路径，我们就可以让电话服务加载该 DLL 并调用导出的 TSPI_providerUIIdentify  
 函数。这为在服务的上下文中执行代码提供了一个直接且可靠的路径。此外，如果导出的函数返回一个非零值，服务会在调用后卸载 DLL——这使得攻击者可以在执行后从磁盘上移除载荷。  
  
一个显而易见的载荷投递机制是指向攻击者控制的 SMB 共享的 UNC 路径。实际上，当共享位于同一域内的标准 Windows 机器上时，此方法可靠运行。然而，攻击者托管的 SMB 服务器，如 impacket-smbserver  
 或 Samba，可能会触发访客访问限制，导致 LoadLibrary  
 失败并返回 ERROR_SMB_GUEST_LOGON_BLOCKED  
 错误。  
  
既然已经拥有一个任意文件写入的原语，本地 DLL 投递提供了一个可靠的替代方案。  
  
可以使用 accesschk  
 工具来识别合适的可写文件。例如，以下文件几乎存在于任何系统上：  
- C:\Windows\System32\catroot2\dberr.txt  
  
- C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpCmdRun.log  
  
- C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\MpSigStub.log  
  
虽然使用 4 字节事件写入来写入整段载荷大小的 DLL 相对较慢，但它完全消除了对额外网络基础设施的需求。  
  
为了演示代码执行，可以构造一个最小的概念验证 TSP DLL。在以下示例中，TSPI_providerUIIdentify  
 导出函数——由电话服务在安装提供程序期间调用——将执行一个命令并将结果写入磁盘：  
```
#include <Windows.h>extern"C" __declspec(dllexport)LONG __stdcall TSPI_providerUIIdentify(LPWSTR lpszUIDLLName) {    wchar_t cmd[] = L"cmd.exe /c whoami /all > C:\\Windows\\Temp\\poc.txt";    STARTUPINFO si;    PROCESS_INFORMATION pi;    ZeroMemory(&si, sizeof(si));    si.cb = sizeof(si);    ZeroMemory(&pi, sizeof(pi));    if (CreateProcessW(NULL, cmd, NULL, NULL, FALSE, CREATE_NO_WINDOW | NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi)) {        CloseHandle(pi.hProcess);        CloseHandle(pi.hThread);    }    return0x1337;}
```  
  
TSPI_providerUIIdentify  
 的返回值会传播回 RPC 客户端，这提供了一个清晰的信号表明载荷已被执行：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnsdp4MNwplsibSjibav3jYNwZ8tmz1D7ibTuSOWHM2o9ibayicMB3OZgaJtz3hKLFxia79xpCR1ZQh91lw/640?wx_fmt=png&from=appmsg "")  
## 漏洞披露与修复时间线  
- **2025年11月6日**  
 – 漏洞报告给 Microsoft。  
  
- **2025年12月22日**  
 – Microsoft 确认该问题为安全漏洞。  
  
- **2025年12月23日**  
 – 根据 Microsoft Bug Bounty 计划获得 $5,000 奖励。  
  
- **2025年12月29日**  
 – CVE-2026-20931 编号被分配。  
  
- **2026年1月13日**  
 – 修复作为 2026 年 1 月补丁星期二更新的一部分发布。  
  
- **2026年1月19日**  
 – 本技术分析文章发表。  
  
此漏洞是按照协调漏洞披露 (CVD) 实践进行披露的。 Microsoft 的公告可在 2026 年 1 月安全更新指南中   
CVE-2026-20931  
 条目下查阅。  
## 结论  
  
本研究显示，即使是被很少使用的遗留 Windows 子系统，仍可能暴露出复杂且强大的攻击面。探究 TAPI 的结果比我预期的要有趣得多——这提醒我们，一些最有价值的研究往往隐藏在这个平台的、容易被忽视的部分中。  
  
最后值得重申的是，此处描述的漏洞**仅影响配置为服务器模式的 TAPI 系统**  
——这是一个相对不常见的配置，专为集中式电话基础设施设计——这大大限制了其实际影响范围。  
  
原文：https://swarm.ptsecurity.com/whos-on-the-line-exploiting-rce-in-windows-telephony-service/  
  
  
**感谢阅读，如果觉得还不错的话，动动手指一键三连～**  
  
