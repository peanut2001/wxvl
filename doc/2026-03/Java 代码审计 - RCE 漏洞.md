#  Java 代码审计 - RCE 漏洞  
原创 GOWLSJ125
                    GOWLSJ125  走在网安路上的哥布林   2026-03-11 08:52  
  
# 什么是 RCE 漏洞  
## 概述  
  
  RCE 是远程代码执行或远程命令执行，指当应用程序需要调用系统命令执行函数时，若开发人员未对用户可控的输入参数进行严格的校验、过滤或转义，攻击者可通过篡改这些参数，将恶意系统命令拼接至正常执行逻辑中，最终让服务器执行非预期的危险指令，从而实现命令注入攻击。  
  
  这类漏洞的触发场景与修复逻辑可具体拆解：攻击者通常通过 WEB 界面、客户端接口等渠道提交构造好的恶意命令参数，而服务器端若存在两类问题 —— 一是未对执行系统命令的函数入参做任何安全过滤，二是业务逻辑设计存在缺陷（如参数拼接逻辑未做边界限制），就会导致恶意参数被直接带入命令执行流程。  
  
  从本质来看，该漏洞的根源是开发人员在代码层面，未对可执行系统命令的敏感函数、自定义执行方法的入口参数做合规校验：既未过滤命令拼接的特殊字符（如 ;  
、&&  
、|  
 等命令分隔符），也未限制参数的合法范围，最终使得客户端提交的恶意指令能够绕过校验，被服务器端直接解析并执行。  
## 总结三点  
1. RCE 漏洞的核心是用户可控参数未过滤，导致恶意命令被拼接至系统执行函数中；  
  
1. Java 场景下常见风险点为 Runtime.getRuntime().exec()  
 等系统命令执行函数或方法的参数处理不当；  
  
1. 漏洞本质是开发端未对敏感执行函数或方法的入参做校验、过滤或逻辑限制。  
  
# 可能出现的场景  
1. 服务端直接存在可执行函数，如 Runtime.getRuntime().exec()  
、ProcessBuilder  
 等，且对传入的参数过滤不严格导致 RCE 漏洞。  
  
1. 有表达式注入导致的 RCE 漏洞，常见的有 OGNL  
、SpEL  
、MVEL  
、EL  
、Fel  
、JST+EL  
 等。  
  
1. 由 Java 后端模板引擎注入导致的 RCE 漏洞，如 Freemarker  
、Velocity  
、Thymeleaf  
 等。  
  
1. 由 Java 一些脚本语言引起从 RCE 漏洞，如 Groovy  
、JavascriptEngine  
 等。  
  
# 可执行函数导致的 RCE 漏洞  
## Runtime.getRuntime().exec() 导致的 RCE  
### Runtime.getRuntime().exec() 概述  
  
java.lang.Runtime  
 公共类中的 exec()  
 用于在运行时执行外部操作系统命令。它接受用户提供的命令字符串，并将其传递给操作系统的命令解析器，从而允许用户执行系统级操作。  
### 基本用法  
  
共有以下 6 种使用方式：  
```
// 在单独的进程中执行指定的字符串命令@Deprecated(since="18")public Process exec(String command) throws IOException {    return exec(command, null, null);}// 在具有指定环境的单独进程中执行指定的字符串命令@Deprecated(since="18")public Process exec(String command, String[] envp) throws IOException {    return exec(command, envp, null);}// 在具有指定环境和工作目录的单独进程中执行指定的字符串命令@Deprecated(since="18")public Process exec(String command, String[] envp, File dir)    throws IOException {    if (command.isEmpty())        throw new IllegalArgumentException("Empty command");    StringTokenizer st = new StringTokenizer(command);    String[] cmdarray = new String[st.countTokens()];    for (int i = 0; st.hasMoreTokens(); i++)        cmdarray[i] = st.nextToken();    return exec(cmdarray, envp, dir);}// 在单独的进程中执行指定的命令和参数public Process exec(String[] cmdarray) throws IOException {    return exec(cmdarray, null, null);}// 在具有指定环境的单独进程中执行指定的命令和参数public Process exec(String[] cmdarray, String[] envp) throws IOException {        return exec(cmdarray, envp, null);    }// 在具有指定环境和工作目录的单独进程中执行指定的命令和参数public Process exec(String[] cmdarray, String[] envp, File dir)    throws IOException {    return new ProcessBuilder(cmdarray)        .environment(envp)        .directory(dir)        .start();}
```  
```
// 1. exec(String command) - 已弃用// 执行单个字符串命令，无法处理带空格的参数Process p1 = Runtime.getRuntime().exec("notepad.exe");// 2. exec(String command, String[] envp) - 已弃用// 带环境变量的形式tring[] env2 = {"PATH=/usr/bin", "JAVA_HOME=/opt/java"};Process p2 = Runtime.getRuntime().exec("echo Hello", env2);// 3. exec(String command, String[] envp, File dir) - 已弃用// 带环境变量和工作目录String[] env3 = {"MY_VAR=test"};Process p3 = Runtime.getRuntime().exec("cmd /c dir", env3, new File("C:\\"));// 4. exec(String[] cmdarray)// 数组形式Process p4 = Runtime.getRuntime().exec(new String[]{"notepad.exe", "test.txt"});// 5. exec(String[] cmdarray, String[] envp)// 带环境变量的数组形式String[] cmd5 = {"java", "-version"};String[] env5 = {"JAVA_HOME=D:\\Program Files\\Java\\jdk-21"};Process p5 = Runtime.getRuntime().exec(cmd5, env5);// 6. exec(String[] cmdarray, String[] envp, File dir)// 命令数组 + 环境变量 + 工作目录String[] cmd6 = {"cmd", "/c", "dir"};String[] env6 = {"MY_PROJECT=hello"};Process p6 = Runtime.getRuntime().exec(cmd6, env6, new File("D:\\workspace"));
```  
### 示例  
  
pom.xml  
```
<?xml version="1.0" encoding="UTF-8"?><project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">    <modelVersion>4.0.0</modelVersion>    <parent>        <groupId>org.springframework.boot</groupId>        <artifactId>spring-boot-starter-parent</artifactId>        <version>4.0.3</version>        <relativePath/> <!-- lookup parent from repository -->    </parent>    <groupId>demo.rce</groupId>    <artifactId>RceDemo</artifactId>    <version>0.0.1-SNAPSHOT</version>    <name>RceDemo</name>    <description>RceDemo</description>    <url/>    <licenses>        <license/>    </licenses>    <developers>        <developer/>    </developers>    <scm>        <connection/>        <developerConnection/>        <tag/>        <url/>    </scm>    <properties>        <java.version>21</java.version>    </properties>    <dependencies>        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-webmvc</artifactId>        </dependency>    </dependencies>    <build>        <plugins>            <plugin>                <groupId>org.springframework.boot</groupId>                <artifactId>spring-boot-maven-plugin</artifactId>            </plugin>        </plugins>    </build></project>
```  
  
Controller  
```
@RestControllerpublic class RceController {    @GetMapping("/exec")    public String executeCommand(@RequestParam("ip") String ip) {        StringBuilder output = new StringBuilder();        // 直接拼接用户输入 - 危险        String[] command = {"cmd", "/c", "ping " + ip};        try {            // 执行系统命令            Process process = Runtime.getRuntime().exec(command);            // 读取命令输出            BufferedReader reader = new BufferedReader(                new InputStreamReader(process.getInputStream(),"GBK")            );            String line;            while ((line = reader.readLine()) != null) {                output.append(line).append("\n");            }            // 等待命令执行完成            int exitCode = process.waitFor();            if (output.isEmpty()) {                output.append("命令执行完成,退出码: ").append(exitCode);            }            reader.close();        } catch (Exception e) {            output.append("执行出错: ").append(e.getMessage());        }        return output.toString();    }}
```  
  
Payload：127.0.0.1%20%26%20calc  
（%20  
=空格，%26  
=&  
）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUHbVCvLlpW3N3icI7FtPibsvEUgyZuvsAiaWLH3eYTrojVOCHPn3XZQkVLKaOkAvZIJoAQWsCCPibcGjUrOmqIpDOqg7EfNZRRPPibldianibcB4M/640?wx_fmt=png&from=appmsg "")  
>   
> Windows 命令连接符:  
  
& : 执行多个命令（无论前面是否成功）  
  
&& : 前面的命令成功才执行后面的  
  
| : 管道，将前面的输出作为后面的输入  
  
|| : 前面的命令失败才执行后面的  
  
### 动态调试过程  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUHbVCvLlpXlg7QJs1eXYibK7UFiaTtSGIXvLCgGLnAVPxxnYqOgBxzO2iaesSmylAKAZuCMOczGdFYqicriaroYFQdHOI37v765lT5U2uVgfFz8/640?wx_fmt=png&from=appmsg "")  
  
进入到 exec  
 方法中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/sUHbVCvLlpUfia6NXjs2OTia5Fv9Ly7Nr48AEEG7K1hyEkx9OLpj5DMHHeJib3SpLyKic37Lfn0HFjPy1nUMXchwicCF2Kl1wQZKubC9AzjUQtcY/640?wx_fmt=png&from=appmsg "")  
  
调用了 ProcessBuilder  
 执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUHbVCvLlpXMqVn7iaIy8UKl9icgXsDOiapnuu2vAIY0CcyvGXCeFQ3MSGnfB2bSGb57zLjKHdVWoo5icklvZjuKOZdibjSpeLoU3KWcwYiaKkoicM/640?wx_fmt=png&from=appmsg "")  
### 为什么要编码  
  
  这是一个关于 HTTP 协议和 URL 参数传输的技术问题。  
  
 ?ip=127.0.0.1 & whoami  
  
  ↓ 服务器解析  
  
 参数1: ip = "127.0.0.1 "  
  
 参数2: whoami = "" (空值)  
  
  所以实际接收到为：http://127.0.0.1:8080/exec?ip=127.0.0.1 & whoami=  
，ip 参数只是 127.0.0.1 ，后面的被截断了。  
  
  URL 编码后接收到的：http://localhost:8080/exec?ip=127.0.0.1%20%26%20whoami  
  
服务器收到: ip = "127.0.0.1 & whoami"  
  
执行命令: ping 127.0.0.1 & whoami  
## ProcessBuilder 导致的 RCE  
### ProcessBuilder 类概述  
  
ProcessBuilder  
 是 Java 提供的一个用于创建操作系统进程的类，它位于 java.lang  
 包中。它的主要作用是启动和管理外部进程。  
### 主要作用  
1. 创建和启动外部进程  
  
- ProcessBuilder  
 允许在 Java 程序中启动外部应用程序或系统命令，比如：  
  
- 执行系统命令（如 dir  
、ls  
、ping  
 等）  
  
- 启动其他 Java 程序  
  
- 运行脚本文件  
  
- 调用任何可执行文件  
  
1. 进程配置和控制  
  
- 设置工作目录  
  
- 配置环境变量  
  
- 重定向输入/输出流  
  
- 合并错误流和标准输出流  
  
### 示例  
```
p@GetMapping("/exec2")public String executeCommand2(@RequestParam("ip") String ip) {    StringBuilder output = new StringBuilder();    try {        // 使用 ProcessBuilder        ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "ping " + ip);        // 启动进程        Process process = pb.start();        // 读取命令输出        BufferedReader reader = new BufferedReader(            new InputStreamReader(process.getInputStream(), "GBK")        );        String line;        while ((line = reader.readLine()) != null) {            output.append(line).append("\n");        }        int exitCode = process.waitFor();        if (output.isEmpty()) {            output.append("命令执行完成,退出码: ").append(exitCode);        }        reader.close();    } catch (Exception e) {        output.append("执行出错: ").append(e.getMessage());    }    return output.toString();}
```  
  
Payload：127.0.0.1%20%26%20dir  
（%20  
=空格，%26  
=&  
）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUHbVCvLlpXz5GvPcdfTla2eHicNoSeYw9Rb7RVQVFzZ74mlicq3aXMW9wiar7g8kSlJIiaoIiatP1PficiaN5L7yicHSTe1VcpE8SLAYDN6onGiaObc/640?wx_fmt=png&from=appmsg "")  
# 审计关键词  
  
在代码审计中，搜索以下关键词：  
- Runtime.getRuntime().exec(  
  
- ProcessBuilder(  
  
- Process  
  
- .waitFor()  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/sUHbVCvLlpW84OwHfkMyFaMwibgu6G4AZSbZnh0h8ngOma9Ar421hdooL6k42NvHukmqtTpLP3su7kLjLtBVfreNr6quqZFdQSRhyrSYEseY/640?wx_fmt=jpeg&from=appmsg "")  
  
  
