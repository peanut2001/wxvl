#  WordPress插件前台RCE漏洞分析审计  
原创 学员投稿
                    学员投稿  进击安全   2026-02-11 01:30  
  
# 免责申明本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。  
## 一、前言  
  
这次学员审计出来了一个WP的插件前台RCE漏洞，这里将审计思路分享给大家，可以一起学习一下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dfrm5V3o6kQicJ1UfGItaH2YYqn1Eq4Hdpj37Zh5OUWaBib6s3GJ4GCmFnYNaq8wnctEjhvqhrNGS4lu19SkWMee0wW5hj3IvNoLHveo3zlcc/640?wx_fmt=jpeg "")  
  
这里插件已经安装好了。（这里编号为CVE-2025-6440）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTY4uVXgFag5sDDNCrMic82dFJg5DXWBIU9BFHOU6oSquLe2poXZ5DicWB0kVZTt2Ob9mSibzaogyMglvbv4cV9gnMKibmyibpyibmUU/640?wx_fmt=png&from=appmsg "")  
## 二、路由分析  
  
先来进行分析目录结构。  
  
```
wc-designer-pro/
├── wc-designer-pro.php       # 主入口文件
├── settings.php              # 设置定义
├── index.php                 # 空文件（安全）
├── unistall.php              # 卸载处理
├── changelog.txt             # 更新日志
├── assets/                   # 静态资源
│   ├── images/               # 图片资源
│   ├── fonts/                # 字体文件
│   └── js/                   # JavaScript 文件
├── includes/                 # 核心功能文件
│   ├── wcdp-admin-menus.php          # 后台菜单
│   ├── wcdp-editor-shortcode.php     # 编辑器短代码
│   ├── wcdp-my-designs.php           # 我的设计功能
│   ├── wcdp-save-design.php          # 保存设计
│   ├── wcdp-upload-images.php        # 图片上传
│   ├── wcdp-upload-fonts.php         # 字体上传
│   ├── wcdp-manage-shapes.php        # 形状管理
│   ├── wcdp-manage-filters.php       # 滤镜管理
│   ├── wcdp-metabox-*.php            # 各种元数据框
│   ├── wcdp-functions.php            # 核心函数
│   ├── wcdp-order-design.php         # 订单设计
│   ├── wcdp-duplicate-design.php     # 复制设计
│   ├── wcdp-content-editor.php       # 内容编辑器
│   ├── wcdp-skin-style.php           # 皮肤样式
│   ├── wcdp-convert-colors.php       # 颜色转换
│   ├── wcdp-translations.php         # 翻译
│   └── wcdp-docs.php                 # 文档
├── product-demos/            # 产品演示
├── profiles/                 # 配置文件
├── languages/                # 语言文件
├── user-manual/              # 用户手册
└── Licensing/                # 许可证相关
```  
  
  
跟常规的 MVC 框架不同，WordPress 的插件入口通常不是直接访问某个 PHP 文件，而是通过统一的 AJAX 接口进行分发。  
  
我们先看插件的主逻辑文件，全局搜索 add_action  
，可以看到如下代码：  
```
// includes/wcdp-functions.phpadd_action( 'wp_ajax_wcdp_save_canvas_design_ajax', 'wcdp_save_canvas_design_ajax' );add_action( 'wp_ajax_nopriv_wcdp_save_canvas_design_ajax', 'wcdp_save_canvas_design_ajax' );
```  
  
在这里可以看到注册了两个动作钩子。  
- wp_ajax_  
 是给登录用户用的。  
  
- wp_ajax_nopriv_  
 是给未登录用户用的。  
  
当然在这里我使用AI进行筛选出来了权限划分。  
```
端点 URL 格式: /wp-admin/admin-ajax.php
| Action | 处理函数 | 文件:行 | 功能描述 | 访问控制 |
|--------|----------|---------|----------|----------|
| wcdp_upload_img_file_ajax | wcdp_upload_img_file_ajax() | wcdp-upload-images.php:31 | 上传图片 | 无 |
| wcdp_convert_resource_cmyk | wcdp_convert_resource_cmyk() | wcdp-upload-images.php:65 | CMYK 颜色转换 | 无 |
| wcdp_save_canvas_design_ajax | wcdp_save_canvas_design_ajax() | wcdp-save-design.php:124 | 保存设计画布 | 无 |
| wcdp_get_json_design_ajax | wcdp_get_json_design_ajax() | wcdp-metabox-designs.php:523 | 获取设计 JSON | 无 |
| wcdp_remove_canvas_design_ajax | wcdp_remove_canvas_design_ajax() | wcdp-metabox-designs.php:554 | 删除设计 | 需登录 (代码检查) |
| wcdp_rename_my_design_ajax | wcdp_rename_my_design_ajax() | wcdp-metabox-designs.php:579 | 重命名设计 | 需登录 (代码检查) |
```  
  
这里直接使用了 nopriv  
，意味着这个接口没有进行权限校验，游客也可以访问。 根据 WordPress 的机制，所有的 AJAX 请求都会汇总到 /wp-admin/admin-ajax.php  
 这个文件。  
  
查看汇总的admin-ajax.php文件如何进行处理路由。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSvoAv24DTSq4LHnsWLatUnXgdsWXrSPxFl95ouiaibdlWIrXEiafYo5IzeWcS2dmsD0EZRzjy2JJbibOhvLiatN0BdjC0KmcZDSw4U/640?wx_fmt=png&from=appmsg "")  
  
这里可以看出来当我们访问插件的wp_ajax_nopriv是不进行鉴权的，并且我们也知道WP是通过admin-ajax.php  
来进行控制路由，那么我们根据刚才AI分析出来的。  
  
<table><thead><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">Action</span></section></th><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">处理函数</span></section></th><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">文件:行</span></section></th><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">访问控制</span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_upload_img_file_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_upload_img_file_ajax()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-upload-images.php:31</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">无</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_convert_resource_cmyk`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_convert_resource_cmyk()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-upload-images.php:65</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">无</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_save_canvas_design_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_save_canvas_design_ajax()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-save-design.php:124</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">无</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_get_json_design_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_get_json_design_ajax()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-metabox-designs.php:523</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">无</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_remove_canvas_design_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_remove_canvas_design_ajax()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-metabox-designs.php:554</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">需登录 (代码检查)</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_rename_my_design_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`wcdp_rename_my_design_ajax()`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">wcdp-metabox-designs.php:579</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">需登录 (代码检查)</span></section></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTS2Tlu4KkvGg5rXYkmSnQtSCaXu3eDkzjGiaRVjzZn5kibJmiasc0o281iaCZz2JA9QXVIstKCBCef7uENiafXSk5CXccRMEfW1rnE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQgtxCiaVbny4EahDtquwgaPIrqib7ZnpH1n0DeqCbEiaVxYAJBlWyP8R9JhN2bAibdDKPVicXCuK8HkrfJEic5p6ofT3Y8Is51Hkueo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRYibSVXtLq1TicJ05sElrw7pSgtvpeZlknoUTWdCkdH7r9WicIssmpGFQbg5LplanTTMZxlDxawHmNRWGl3ZnZUKwadkJUxI7J0g/640?wx_fmt=png&from=appmsg "")  
  
其中前面四个的action是不会进行鉴权处理的，那么我们访问URL格式为：  
```
http://ip/wp-admin/admin-ajax.php?action=前四个ajax都是不被鉴权的。
```  
  
尝试验证。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRutgJjdoZeelOP0bWs3icAblbAqJibRnm1AwsA89CRhQlpwcyh5SRh4YSic0yO6fH2klaSy6S2JdSumia59Wo6c5dMy6IOQZrAesg/640?wx_fmt=png&from=appmsg "")  
  
可以看到确实是可以访问的，下一步我们进行分析这个方法。  
## 三、漏洞分析  
  
分析方法wcdp_save_canvas_design_ajax。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQZ9WoycZRb3puKZYQXxsdV0ibicFuz3cIZVicXbmAfupicF9ic5HlibTNMZPtakiaHoVE5nTUrnnIjSEPoY8yOxBjeHuGWnv1fiaiczSUk/640?wx_fmt=png&from=appmsg "")  
  
在这里可以看到其中userid变量，在经过is_user_logged_in() ? get_current_user_id()三目运算符之后变为布尔值，只是对我们上传的目录有一定影响，其中接受参数params并且进行json解码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTcXoTu4gTRdhp2hdJrmEhfnakckMSxkInHlmJQlV0hzo9GMEImesjoy737GXDMtT8bsatUskCIKyWaLaQKbEt91zYkicl6Fxj8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTvvXico1ocAbdhQlzHbuhzd5lbiaChTjmbjxn6K8ZSfjahqZaJw0oMibLdSXAPicYGiaIDKqfpqJibpvBWCO1XTzkjicLmgFeQv7FS8Q/640?wx_fmt=png&from=appmsg "")  
  
并且进行遍历其中的files参数，其中分别有name、count、ext三个参数。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRWS7MmOojfEuwh6wicfBgBFZKbJhfEgRGc1sxmewC3hnt8JoHhhIWbJTlQyEcAuFV04PuHPic3qSC0qPFuqoShZzRmA9Pgic0SHs/640?wx_fmt=png&from=appmsg "")  
  
同时这里可以看到ext后缀为遍历数组files当中的name拼接上ext的后缀，这里只要ext后缀不是CMYK即可。  
  
这里传递参数FILE还是我们通过params当中的的fiels数组当中的变量$count定义的。  
  
同时这里回头也发现。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTV3Va2zzMiaKRa6gDQpHounEllS8o8Agr95tsiciaC0N5PwTR1z5pSFXe2Lav5g0Dn1M0THg4Nyu9Fb8uibedskuL9hT0egWTSRRs/640?wx_fmt=png&from=appmsg "")  
  
在这里mode要进行定义，定义save或者另外一个都可以，只不过这里是上传路径，这里我们就进行定义save，那么其中uniq则为我们上传的/tem/下的文件夹。  
  
那么这里我们总结一下：  
  
<table><thead><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">数据包参数</span></section></th><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">变量名</span></section></th><th style="box-sizing: border-box;text-align: left;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;font-weight: bold;background-color: rgb(240, 240, 240);min-width: 85px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`action=wcdp_save_canvas_design_ajax`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">\-</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">触发WordPress AJAX钩子</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$pr`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">JSON解码后的配置对象</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params.mode=&#34;save&#34;`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$pr[&#39;mode&#39;]`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">决定保存路径模式</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params.uniq=&#34;test_vuln&#34;`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$pr[&#39;uniq&#39;]`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">唯一标识符，用于目录名</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params.files[0].name=&#34;cwascaa1&#34;`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$name`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">保存的文件名（不含扩展名）</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params.files[0].ext=&#34;php&#34;`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$ext`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">**文件扩展名 - 漏洞点**</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`params.files[0].count=&#34;file_upload&#34;`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$count`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">指向 `$_FILES` 中的键名</span></section></td></tr><tr style="box-sizing: border-box;border-width: 1px 0px 0px;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`cc` (文件字段)</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">`$_FILES[&#39;cc&#39;]`</span></section></td><td style="box-sizing: border-box;font-size: 16px;border: 1px solid rgb(204, 204, 204);padding: 5px 10px;text-align: left;min-width: 85px;"><section><span leaf="">实际上传的文件内容</span></section></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQ2cYiboroNwwJHlia9SGTib6ftVUo0DUktlecMgByBibXkr0IjptQZiaicNxByKkj72SowsmGE2gYhUBdF1TNlaa9QdnU0f5ehVbXibw/640?wx_fmt=png&from=appmsg "")  
  
最终数据包如上，我们成功上传了saw11dc.php文件，进行查看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRrX6V6JXPOB13G9TnH47oD1W6xtYw4Lhz4YVMfGcVsZ72WgTdNqsgqFWNf14ezGZjzu9pnRjm86zF19eibYFTbiatDkeufccZGA/640?wx_fmt=png&from=appmsg "")  
  
成功RCE。  
  
**广告区域**  
  
  
    目前第四期进阶课程已经开始，课表如下：  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRuVzYibyvlCg9MPGhtbPMDibicxhX2VfgtSgWYibB3h6MD4Qevp0ey53OGFd5ibib9Rdj5JJMOKJlsFg2jzrVIcqMic9XfFXfBTzNz5M/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16 "")  
  
同时报名第四期基础课程同样可看，课表如下：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kRZdZbIjvX7mugkWddTMURicjssDYfRibMUzSYQ751TdZFMW1kY91EoicQvd80Agd7oNo66Xv8DG9tLgNYU0AicOmVlTYYwsOqdhyw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
  
同时具备内部资料以及靶场相关福利，想要了解的师傅可以冲了。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSk6QYMXsic87HtwWCetK8RBAEcqU22JFDTpaqicQm2hOj3kZtqJ9bic0xAErrR6Lqv18NTAWWBVJfLAMJnIurLtPibUsCdAQicwmhM/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQCNW7C6OIEoKkWhXFUlMZ62150sthiaPcqaclVPKfBvMoT8QpJXIcWj4XyIkIdoz9xHM22apibWCvaJ69VLicic4MqvS0yQ35uY2o/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23 "")  
  
  
  
  
  
  
  
  
