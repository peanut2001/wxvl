#  代审0day-开源图库任意用户登录+getshell  
原创 Yi1StaR
                    Yi1StaR  奕星安全   2026-03-02 03:02  
  
> 本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责。  
  
  
# 一、前言  
  
  
    本次是对开源项目  
LightPicture  
的代码审计过程记录，  
分析了两个比较严重的漏洞。  
本  
次审计在两个月前就完成了，但是一直没写文章记录。在今年年前发现ncc社区已经有其他师傅审计并发出了，自己就也在公众号记录一下。  
  
# 二、项目架构分析  
  
  
项目地址：https://github.com/osuuu/LightPicture  
  
进去可以看见是thinkphp+vue开发的项目。  
  
thinkphp的项目就属于是MVC架构。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8YLaQPX5CaZFeic5giaia82KCj32q6V57JvASlrGpBP0JoGctxzT44jXg5QPbDD5TPGnHCRz1BFdMP48IBh6alwLwbpGdjrMeYIW8/640?wx_fmt=png&from=appmsg "")  
  
包含 model、controller、services等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8awibmBYm97LbPY2o3JGqrMBl0eJyC28jFbKImXib4icSEx3W0OMqFR5ibrZ3ATot56qoiaUP1aN14U6uMVSuosYTvU6p12vkEiaxnnQ/640?wx_fmt=png&from=appmsg "")  
  
# 三、任意用户登录  
  
  
这是由于tokenkey硬编码导致token可以伪造，从而引发了任意用户登录的漏洞。  
  
打开controller/  
Account.php  
查看login方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8ZOWGF4F0wHicUW5RZIFgpTEQicI9FJGgheD2slRMDXOJ8ib2pVcVgiaUhicP2ibcWW9wAV8ROPUQI1GFjgS90lctrFASoz2tsaD03cI/640?wx_fmt=png&from=appmsg "")  
  
存在一个createToken的token生成函数。  
```
$token = $tokenClass->createToken($user['id']);
```  
  
跟进一下这个函数，看看是如何生成token的。  
  
跟进到了  
app\services\AuthToken.php，可以找到这个方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8aicClS3Kv6r4sPIyff3iaO3Gx4yFn9QNCYK4dmvrAebXjGKchChhfROK7CtEF6HBY2aMqEVYcNVstMyEoicGAZIrTBf0cgnU2E0c/640?wx_fmt=png&from=appmsg "")  
```
class AuthToken
{
    /**
     * 获取token
     * @param string $username 自定义参数
     */
    public function createToken($username)
    {
        try {
            $key = TokenKey;
            $time = time(); //当前时间
            //$token['iss']=''; //签发者 可选
            //$token['aud']=''; //接收该JWT的一方，可选
            $token['iat'] = $time; //签发时间
            $token['nbf'] = $time; //(Not Before)：某个时间点后才能访问，比如设置time+30，表示当前时间30秒后才能使用
            $token['exp'] = $time + 85400*14; //token过期时间
            $token['username'] = $username; //自定义参数
            $json = JWT::encode($token, $key);
            return $json;
        } catch (\Firebase\JWT\ExpiredException $e) { //签名不正确
            // return $this->create([], $e->getMessage(), 104);
            return "";
        } catch (\Exception $e) { //其他错误
            return "";
        }
    }
    
}
```  
  
分析一下这个方法的逻辑：  
  
该方法需要传入一个参数（  
$username）。  
  
1、通过  
全局常量 TokenKey获取密钥。  
  
2、  
调用 time() 获取当前服务器时间戳。  
  
3、设置签发时间、生效时间、过期时间；过期时间默认设置为14天。  
  
4、接收传入的username的参数。  
  
5、  
通过$json  
  
=  
  
JWT  
::  
encode  
(  
$token  
,   
$key  
);方法生成token。  
  
6、出现异常则均返回空字符串。  
  
我们可以知道，仅需  
$username  
和  
key  
就可以得到token。  
  
username是自己传入的，所以我们只需要知道key的值就可以得到token  
  
我们全局搜索这个key常量，可以得到：  
```
define("TokenKey", "e06b7b61978b30fd1e87723ef61746fb"); 
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8bDnX4LLzS7Bgp4ekhmRmjibhv5HpXIS4R5oTXuhaZIOHnPDohH8qU7ojtUibXJyVuZr7l3S2jm9arf8lydj7ZOT9KI5EgKP5CKg/640?wx_fmt=png&from=appmsg "")  
  
现在token生成的条件都满足了.  
  
写一个php，来调用createtoken函数来生成一个管理员token。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/THialw6iaZk8Y5OXkqcop3vicTeCebcplVF8kfaQaxupeMNWmU9aCs1HeBk4TqGaOOemYM1wpDb8GESKGyiaf7mjOiaL7BEeQALvm1ibSZDqNvEoc/640?wx_fmt=png&from=appmsg "")  
  
当然可能会有人有疑惑，为什么这里username是1。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8ZmwibYAztolZn1nooyeyRLgnXQY2aXpjSwdMRdwuBgFwEmPDAicUibhoJHEPWQOOLVgdtcOwQpaJUkSOlMn030KG3cib9RTenPZia4/640?wx_fmt=png&from=appmsg "")  
  
是因为 虽然  
AuthToken.php  
传入的是$username。  
  
但是在  
Account.php  
生成的时候是传入的是$user  
[  
'id'  
]生成的token。  
  
而admin的id为1。所以需要设置为1。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/THialw6iaZk8ZVstVicNdpCCZo9eN71sM8nURlUhsLfialHPlZEu2YibibN1zgNFeV0F9AwY1HWjicQpSUwGIia29OIW3b3miabOr3tWF5sZpmAnroUo/640?wx_fmt=png&from=appmsg "")  
  
拿前面得到的token去自己的网站验证一下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/THialw6iaZk8ZnLCRCgVMvicxyAkIlX9PXzLYd9dKmpDRp51WWamvpMPx1UmXI9X0Autqqt5iaEAnq14eakLEctGyzaoia9v5r45xMxpzzEiatY3I/640?wx_fmt=png&from=appmsg "")  
  
f12 在本地存储添加刚刚生成的lp_token,即可进入管理员后台。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8a3dic9g8gtm02w7AMUAtibHpw4TfPiakpTmOlgx0tiaKoeUfZ80oyGbF8x0ZiaFzOGsiazPOZuLBbjBQGqnQtJHhbTHudE3hmPiamOu8/640?wx_fmt=png&from=appmsg "")  
  
也可也成功调用/user/info接口，返回管理员信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8bgUwzsq33MvcB7KKLxdFqwvQIJzhDjMyOVdicMnQKbF0CFCRvicKC5WL8a4kucLjsS2jibFhyhTRzCmPa8N6xrnPGg7JNxlqxcbM/640?wx_fmt=png&from=appmsg "")  
  
# 四、任意文件上传getshell  
  
  
查看controller/Api.php，可以看见  
upload  
(  
Request  
  
$request  
)上传方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8ZcW1GNnfl2QyljRIlfRibjvubkFCOMaKP0fX1A5vIV43NibWhBXA3ee8fI1Uice2UIyfuZuFDUylXl2F78OibiccTaljLVicxbgMJN4/640?wx_fmt=png&from=appmsg "")  
  
查看路由  
route\app.php文件，可以发现Api.php不存在token鉴权。而其他路由则存在TokenVerify鉴权。  
在该方法中，仅存在key作为鉴权。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8bvldBs5ajZ2N3pvhwYLcEeKp4cTJHZ2wUURiaqWYaKITWib5UPBwY0AlWEaweZbz5vEsfh6sXsrKXcgUPGic6aoXVmvLibMA8r4ZI/640?wx_fmt=png&from=appmsg "")  
  
而我们用拿到的管理员的token去调用  
/user/info，可以得到管理员的Secret_key。  
拿到这个key就可以进行文件上传，而无需token。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8b1r1D1sOiciaEP8WxalKnxiaQ9nyrwJVMRslxY37mK16F4a2hlL2ZdibCsS5A9uIEsEAzKuMJ4jseXnAlhEU6nq0iakibNYhIliaNsH0/640?wx_fmt=png&from=appmsg "")  
  
在  
Api.php中的  
upload方法，上传文件就会调用create方法。  
  
如果是本地上传，又会调用到location_upload(  
$file  
)方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8a0nC93cJG4PHV0Mkw34YJE2HcRvhWEia4e1TemiaeLA2YausFv0aDfEDIHQDVjbIdgg4kdVTACq64fC8vgDYZZOs7MlOVeCoRhk/640?wx_fmt=png&from=appmsg "")  
  
跟进到  
app\services\UploadCLass.php。  
  
查看它的本地文件上传方法  
location_upload  
(  
$file  
)，  
  
可以看见使用了getname方法，我们进而跟进一下getname方法，查看文件名的处理逻辑。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8Z0QS5nKQhkqM8tiaeQae0Rl7l1OVIGQQDFzicibWia3pRjl7tMvnJt1IibSlWl5LlvfF8Aa7DwNJ2IWsSsx5LLr1lFqgIFUic9JnpQ0/640?wx_fmt=png&from=appmsg "")  
```
function location_upload($file)
    {
        // 获取网站协议
        $protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
        $path = './' . $this->getPath;
        if (!file_exists($path)) {
            mkdir($path, 0777, true);
        }
        $newName = $this->getName($file['name']);
        // 本地上传
        if (move_uploaded_file($file["tmp_name"], $path . $newName)) {
            $url = $protocol . $_SERVER['HTTP_HOST'] . '/' . $this->getPath . $newName;
            return array(
                'path' => $this->getPath . $newName,
                'name' => $newName,
                'url' => $url,
                'state' => 1,
            );
        } else {
            return array(
                'msg' => '上传失败',
                'state' => 0,
            );
        }
    }
```  
  
跟进到app\services\UploadCLass.php中的getname()方法。  
  
可以发现该方法没有对 $format（文件后缀）做任何黑白名单校验。它盲目地信任用户上传时的原始文件名。导致了用户可以直接修改后缀为php进行上传。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8b5rexO3qmILMgZ1CmibVd99ADZ3OqRXPCzwiaXhKEaCth4mvmP4nRHXhPyTdZKwl4qGuz3AbKqDK6y9hicH2cWH7jwQSQ2Upj0eY/640?wx_fmt=png&from=appmsg "")  
  
构造文件上传包，上传webshell。修改文件后缀即可。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8YeKXDibnibumd80WBOPqXWyQ0ibexKuX0yKOrYZyZ4BW5I8LjialnvvjTpic4VAx3Xic4zQeQ97BtpYmlZvnUFzvam1Czdn50XPPdKc/640?wx_fmt=png&from=appmsg "")  
  
哥斯拉可连接：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/THialw6iaZk8bZGRwPn9nuhFWqZForyhTAWOgPbO0P8JD05IBhK4EicbX6xn9kIAibnlw0xENKh0OszdGHVajLmiczEQLRQa6XicVcWYtW6yaYa3k/640?wx_fmt=png&from=appmsg "")  
  
# 五、总结  
  
  
    本次审计分析了两个漏洞，一个为jwt密钥硬编码导致任意用户登录，一个为任意文件上传导致的getshell。而我们在代码审计的时候，可以  
从  
架构分析入手，重点关注认证授权、文件操作、数据验证等高风险模块，能够有效发现潜在安全隐患。  
若有纰漏，欢迎讨论。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8 "")  
  
**安全知识分享，欢迎师傅们关注！**  
  
  
  
  
