#  GHSA-qrq5-wjgg-rvqw: OpenClaw 龙虾插件安装路径遍历漏洞分析报告  
原创 塑造者壹号
                    塑造者壹号  幻泉之洲   2026-03-13 01:34  
  
>   
  
## 基本漏洞信息  
  
说实话，这个漏洞影响不小，但触发不算特别容易，因为需要用户主动去安装恶意插件。  
- **漏洞编号：**GHSA-qrq5-wjgg-rvqw  
- **影响版本：**2026.1.29-beta.1 到 2026.2.1 之前的所有版本  
- **修复版本：**2026.2.1 及以后  
- **漏洞类型：**路径遍历  
- **危险等级：**严重  
- **发现者：**@logicx24  
## 这个漏洞到底怎么回事？  
  
OpenClaw 装插件的时候，会从插件的 package.json 文件里读取 name 字段。  
  
对于像 @xx公司/插件名 这种带作用域（scoped）的包，它会提取 @xx公司/ 后面的部分作为插件目录名。  
  
问题就出在这里。修复之前的 OpenClaw，没有好好检查这个提取出来的目录名。  
  
攻击者如果把包名写成 @邪恶公司/..，那么提取出来的目录名就是 ..。程序会傻乎乎地把插件文件拷贝到“扩展目录/..”，也就是扩展目录的上一层去。  
  
这样一来，攻击者完全可以控制文件被安装到任何位置，甚至可以一路指向上级目录的目标系统文件。  
## 漏洞代码长什么样？  
  
关键的代码在 src/plugins/install.ts 里面。修复前，safeDirName 这个函数只做了件“皮毛”工作。  
  
function safeDirName(input: string): string {  const trimmed = input.trim();  if (!trimmed) {    return trimmed;  }  // 只是简单地替换正斜杠  return trimmed.replaceAll("/", "__");}  
  
它只把 / 换成了 __，但 ..、. 这些能向上级导航的路径根本没管。遇到 @邪恶公司/.. 这样的名字，它会得到 ..，然后直接就用了。  
  
后面的 path.join 函数一拼接，路径直接就跑出去了。  
## 攻击者是怎么利用的？  
  
攻击者准备一个恶意插件，核心就是它的 package.json。  
  
{  "name": "@evil/..",  "version": "1.0.0",  "openclaw": {    "extensions": ["./dist/index.js"]  }}  
  
然后把这个插件包通过各种方式发给用户，比如伪装成一个有用的工具发布在公共仓库，或者在论坛里推荐下载。  
  
用户一旦执行 openclaw plugins install 恶意包.tgz，OpenClaw 就会读取这个 package.json，把名字解析成 ..。  
  
默认情况下，扩展目录可能是 C:\Users\用户名.openclaw\extensions 或者 /home/用户名/.openclaw/extensions。  
  
path.join 把“用户配置目录/extensions”和“..”拼在一起，就变成了“用户配置目录”。  
  
插件里的所有文件就会被直接复制到“用户配置目录”，如果里面有叫 config.json 的文件，就会覆盖掉原有的主配置文件。  
  
更坏的情况下，要是你能构造出 ../../../../etc/passwd 这样的上级导航，理论上就能覆盖系统里的任何文件，但实际要看程序运行的用户权限。  
## 漏洞的完整数据流  
  
我们把这个过程再完整地画一遍，看看攻击者控制的输入到底是怎么一路畅通无阻到达“危险区域”的，代码里一般叫“Sink点”。  
  
1. **源头**：package.json 里的 name字段。  
  
2. **提取**：交给 unscopedPackageName 函数处理，@evil/.. 变成 ..。  
  
3. **“安全”清理**：交给 safeDirName 函数，它不处理 ..，所以返回的还是 ..。  
  
4. **拼路径**：path.join(extensionsBase, "..")，目标路径就变成了上级目录。  
  
5. **执行文件操作**：fs.cp 或 fs.mkdir 按照错误的路径写入文件。  
  
6. **完成破坏**：可能覆盖了用户配置，也可能植入了后门脚本。  
## 官方是怎么修复的？  
  
开发者在 2026年2月2号提交了修复。这个修复不是简单地打补丁，而是在好几个地方上了“锁”。  
  
**第一层锁**：增强了 safeDirName。现在它不光把 / 换成 __，也把 Windows 的反斜杠 \ 换掉。  
  
**第二层锁（最关键）**：新增 resolveSafeInstallDir 函数。它用上了真正的“杀手锏”。  
  
修复代码先用 path.resolve 把基础目录（比如 /home/user/.openclaw/extensions）的绝对路径，以及最终目标目录的绝对路径都算出来。  
  
然后，用 path.relative 计算出“从基础目录到目标目录的相对路径”。  
  
接着检查这个相对路径：  
- 如果相对路径是 ..， 直接拒绝。  
- 如果相对路径以 ..\ (Windows) 或 ../ (Unix) 开头，也拒绝。  
- 如果相对路径是绝对路径，还是拒绝。  
这一下子就从结果上堵死了所有想往上爬的路。  
  
**第三层锁**：增加 validatePluginId 函数，明确拒绝名字是 . 或者 .. 的插件。  
## 这个修复够安全吗？  
  
可以。它考虑了我们能想到的大多数绕过方式。  
- **Unicode编码绕过？**path.resolve 会把这些特殊编码的路径点规范成真实的 . 和 ..，然后 path.relative 的检查照样能抓住它。  
- **用反斜杠？**safeDirName 已经把 \ 换掉了。  
- **用大小写变体？** 检查用的是 === 直接匹配字符串，.. 和 .. 不一样，不会被认为是路径点。  
- **用超长名字？** Node.js 的 path 模块有能力处理，检查是在路径解析之后做的，所以没问题。  
所以，从目前看，这个漏洞在 2026.2.1 版本里算是被堵上了。  
## 用户现在该做什么？  
  
如果你在用 OpenClaw，第一件事就是检查版本。  
  
打开终端，运行：  
  
openclaw --version  
  
如果版本号低于 2026.2.1，赶紧升级。  
  
然后，可以去看看你的 OpenClaw 扩展目录里有没有奇怪的东西。  
  
目录通常在这：  
- Windows: %USERPROFILE%\.openclaw\extensions\  
- macOS/Linux: ~/.openclaw/extensions/  
另外，安装插件时也留个心眼，别装来路不明的东西。最好去官方或有信誉的社区找插件。  
## 结语  
  
这个漏洞（GHSA-qrq5-wjgg-rvqw）挺典型的，就是个不信任用户输入的老问题。攻击者控制了一个看似“无害”的字段（包名），程序没有做足够的检验，结果就出事了。  
  
万幸 OpenClaw 团队反应挺快，两天就搞定了修复。他们的方法也值得学习，不是只在输入口上堵，还在最终操作前用 path.relative 这种“结果验证”的方式再兜底检查一次，这才是比较稳妥的安全做法。  
  
现在安全版本已经发了，大家尽快更新，就没事了。  
>   
  
  
**参考链接**  
- 官方安全公告：GHSA-qrq5-wjgg-rvqw（https://github.com/openclaw/openclaw/security/advisories/GHSA-qrq5-wjgg-rvqw）  
- 漏洞修复提交记录：d03eca8（https://github.com/openclaw/openclaw/commit/d03eca8450dc493b198a88b105fd180895238e57）  
  
  
