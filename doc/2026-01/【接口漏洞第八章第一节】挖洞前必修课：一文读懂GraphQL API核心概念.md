#  【接口漏洞第八章第一节】挖洞前必修课：一文读懂GraphQL API核心概念  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-20 11:16  
  
**【文章说明】**  
- **目的**  
：本文内容仅为网络安全**技术研究与教育**  
目的而创作。  
  
- **红线**  
：严禁将本文知识用于任何**未授权**  
的非法活动。使用者必须遵守《网络安全法》等相关法律。  
  
- **责任**  
：任何对本文技术的滥用所引发的**后果自负**  
，与本公众号及作者无关。  
  
- **免责**  
：内容仅供参考，作者不对其准确性、完整性作任何担保。  
  
**阅读即代表您同意以上条款。**  
  
****  
今天我们来聊聊   
GraphQL API 漏洞  
  
GraphQL漏洞通常由实现与设计缺陷引发。例如，  
内省功能可能处于开启状态，使攻击者能够通过查询API获取其架构信息。  
  
GraphQL攻击通常表现为恶意请求，攻击者借此获取数据或执行未授权操作。此类攻击可能造成严重后果，尤其是当用户能够通过操纵查询或执行CSRF攻击获取管理员权限时。存在漏洞的  
GraphQL API也可能导致信息泄露问题。在进入这块功能的漏洞挖掘前，我们要先对   
GraphQL API   
有全面的基本了解，下面这边会结合以下问题，来让大家对它先有个全面的理解。  
- 什么是 GraphQL？  
  
- GraphQL 的工作原理是？  
  
  
- 什么是 GraphQL 模式？  
  
- 什么是 GraphQL 查询？  
  
- 什么是 GraphQL 变更？  
  
- 什么是 GraphQL 字段？  
  
- 什么是 GraphQL 参数？  
  
- 什么是 GraphQL 变量？  
  
- 什么是GraphQL   
别名？  
  
- 什么是   
GraphQL 片段？  
  
- 什么是   
GraphQL 订阅？  
  
- 什么是   
GraphQL 内省  
？  
  
  
什么是 GraphQL？  
  
GraphQL 是一种 API 查询语言，旨在提升客户端与服务器之间的通信效率。它允许用户精确指定响应中所需的数据，从而避免 REST API 中常见的大体积响应对象与多次调用问题。  
  
GraphQL 服务通过定义约定来实现客户端与服务器的通信，客户端无需知晓数据的具体存储位置。客户端只需向   
GraphQL 服务器发送查询，服务器便会从相关位置获取数据。由于   
GraphQL 与平台无关，所以它可以通过多种编程语言实现，且能与几乎所有类型的数据存储进行通信。  
  
  
GraphQL 的工作原理是？  
  
  
GraphQL 模式（  
Schema）定义了服务数据的结构，包括可用的  
对象（或叫类型）、  
字段及其  
关系。  
  
通过   
GraphQL 模式描述的数据可通过三类操作进行处理：  
- 查询（Queries）：获取数据。  
  
- 变更（Mutations）：添加、修改或删除数据。  
  
- 订阅（Subscriptions）：与查询类似，但订阅会建立持久连接，使服务器能够主动以指定格式向客户端推送数据。  
  
  
所有   
GraphQL 操作使用同一请求地址，通常以  
 POST 请求形式发送。这与   
REST API 形成显著区别，后者通过多种 HTTP 方法使用特定操作的端点。在   
GraphQL 中，操作的类型和名称决定了查询的处理方式，而非请求地址或所使用的 HTTP 方法。  
  
GraphQL 服务通常以符合请求结构的   
JSON 对象响应操作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0JxVlmtYtaYRMWBkicpGqKVKmk6mRjDf0bNuujV8yRSyfiaULTrS48tFmUNfz7IhtYZgrzjh3k23mw/640?wx_fmt=png&from=appmsg "")  
  
什么是 GraphQL 模式？  
  
在   
GraphQL 中，模式代表了服务前后端之间的合约。它通过人类可读的模式定义语言，以一系列类型定义可用的数据。这些类型随后由服务实现。  
  
大部分定义的类型为对象类型，它们指定了可用对象及其字段与参数。每个字段都有自己的类型，可以是另一个对象类型，也可以是标量、枚举、联合、接口或自定义类型。  
  
以下示例了一个简单的   
Product 类型模式定义。  
！操作符表示该字段在调用时不可为空（即必填字段）。  
```
graphql
# 示例模式定义
type Product {
    id: ID!
    name: String!
    description: String!
    price: Int
}
```  
  
模式必须至少包含一个可用查询，通常还会包含可用变更的详细信息。  
  
什么是 GraphQL 查询？  
  
GraphQL 查询用于从数据存储中检索数据，大致相当于   
REST API 中的 GET 请求。  
  
查询通常包含以下关键部分：  
- 查询操作类型：虽为非必填项但推荐使用，用于明确告知服务器传入请求是查询。  
  
- 查询名称：可自定义名称，可选但有助于调试。  
  
- 数据结构：指定查询应返回的数据。  
  
- 参数（可选）：用于创建返回特定对象详情的查询（例如“获取 ID 为 123 的产品的名称和描述”）。  
  
以下示例展示了一个名为   
myGetProductQuery 的查询，请求   
ID 为   
123 的产品的   
name 和   
description 字段：  
```
graphql
# 示例查询
query myGetProductQuery {
    getProduct(id: 123) {
        name
        description
    }
}
```  
  
注意，产品类型在模式中可能包含比此处请求更多的字段。仅请求所需数据的能力是   
GraphQL 灵活性的重要体现。  
  
什么是 GraphQL 变更？  
  
变更用于以某种方式  
修改数据，包括添加、删除或编辑数据，大致相当于   
REST API 中的   
POST、  
PUT 和   
DELETE 方法。  
  
与查询类似，变更具有操作类型、名称和返回数据的结构。但变更始终需要某种类型的输入，可以是内联值，但实践中通常通过变量提供。  
  
以下示例展示了一个创建新产品的变更及其关联响应。此处，服务配置为自动为新产品分配 ID，并按要求返回：  
```
graphql
# 示例变更请求
mutation {
    createProduct(name: "Flamin' Cocktail Glasses", listed: "yes") {
        id
        name
        listed
    }
}
# 示例变更响应
{
    "data": {
        "createProduct": {
            "id": 123,
            "name": "Flamin' Cocktail Glasses",
            "listed": "yes"
        }
    }
}
```  
  
什么是   
GraphQL   
字段？  
  
所有 GraphQL 类型都包含  
可查询数据项，  
这些就  
称为   
GraphQL   
字段的  
。发送查询或变更时，需指定希望 API 返回哪些字段。响应内容与请求中指定的结构一致。  
  
以下示例展示了获取所有  
员工 ID 和  
姓名详情的查询及其关联响应。此处，  
id、  
name.firstname 和   
name.lastname 为请求的  
字段：  
```
graphql
# 请求
query myGetEmployeeQuery {
    getEmployees {
        id
        name {
            firstname
            lastname
        }
    }
}

# 响应
{
    "data": {
        "getEmployees": [
            {
                "id": 1,
                "name": {
                    "firstname": "Carlos",
                    "lastname": "Montoya"
                }
            },
            {
                "id": 2,
                "name": {
                    "firstname": "Peter",
                    "lastname": "Wiener"
                }
            }
        ]
    }
}
```  
  
  
什么是   
GraphQL 参数？  
  
参数是为特定字段提供的  
值。类型可接受的参数在模式中定义。  
  
发送包含参数的  
数据查询或  
数据变更时，GraphQL 服务器根据其配置决定如何响应。例如，它可能返回特定对象的详情，而非所有对象的详情。  
  
以下示例展示了  
员工 ID 作为参数的   
getEmployee 查询请求。服务器仅返回  
匹配该 ID 的员工详情：  
```
graphql
# 带参数的示例查询
query myGetEmployeeQuery {
    getEmployees(id: 1) {
        name {
            firstname
            lastname
        }
    }
}

# 查询响应
{
    "data": {
        "getEmployees": [
            {
                "name": {
                    "firstname": "Carlos",
                    "lastname": "Montoya"
                }
            }
        ]
    }
}
```  
  
注意：如果用户提供的参数被用于直接访问对象，则   
GraphQL API 可能容易受到  
访问控制漏洞（如不安全的直接对象引用，IDOR）的攻击，这个我们后面会详细分享。  
  
什么是   
GraphQL 变量？  
  
变量允许传递动态参数，而非将参数直接嵌入查询字符串中。  
  
基于变量的查询与使用内联参数的查询结构相同，但查询的某些部分取自单独的基于 JSON 的变量字典。它们支持在多个查询中  
复用通用结构，仅更改变量值本身。  
  
构建使用变量的查询或变更时，需要：  
- 声明变量及类型。  
  
- 在查询的适当位置添加变量名。  
  
- 从变量字典传递变量的键和值。  
  
  
以下示例展示了与前一示例相同的查询，但 ID 通过变量传递，而非作为查询字符串的直接部分：  
```
graphql
# 使用变量的示例查询
query getEmployeeWithVariable($id: ID!) {
    getEmployees(id: $id) {
        name {
            firstname
            lastname
        }
    }
}

{
    "id": 1
}
```  
  
在此示例中，变量在第一行通过 ($id: ID!) 声明。! 表示此字段为此查询的必填项。随后在第二行通过 (id: $id) 作为参数使用。最后，变量值在变量 JSON 字典中设置。  
  
什么是   
GraphQL 别名？  
  
GraphQL 对象不能包含多个同名的属性。例如，以下查询会无效，因为它尝试返回   
product 类型两次：  
```
graphql
# 无效查询
query getProductDetails {
    getProduct(id: 1) {
        id
        name
    }
    getProduct(id: 2) {
        id
        name
    }
}
```  
  
别名通过显式命名希望 API 返回的属性来绕过此限制。您可以使用别名在单个请求中返回同一类型的多个实例，从而减少所需的 API 调用次数。  
  
在以下示例中，查询使用  
别名为两个产品指定唯一名称（product1和product2）。此查询现在通过验证，并返回详情：  
```
graphql
# 使用别名的有效查询
query getProductDetails {
    product1: getProduct(id: "1") {
        id
        name
    }
    product2: getProduct(id: "2") {
        id
        name
    }
}

# 查询响应
{
    "data": {
        "product1": {
            "id": 1,
            "name": "Juice Extractor"
        },
        "product2": {
            "id": 2,
            "name": "Fruit Overlays"
        }
    }
}
```  
  
注意：在变更中使用别名实际上允许在单个 HTTP 请求中发送多条 GraphQL 消息。  
  
什么是   
GraphQL 片段？  
  
片段是查询或变更的  
可复用部分，包含关联类型字段的子集。  
  
片段定义后，它们可被包含在查询或变更中。如果后续片段发生更改，则更改会体现在所有调用该片段的查询或变更中。  
  
以下示例展示了一个   
getProduct 查询，其中产品详情包含在   
productInfo 片段中：  
```
graphql
# 示例片段
fragment productInfo on Product {
    id
    name
    listed
}
# 调用片段的查询
query {
    getProduct(id: 1) {
        ...productInfo
        stock
    }
}

# 包含片段字段的响应
{
    "data": {
        "getProduct": {
            "id": 1,
            "name": "Juice Extractor",
            "listed": "no",
            "stock": 5
        }
    }
}
```  
  
什么是   
GraphQL 订阅？  
  
GraphQL   
订阅是一种特殊类型的查询。它们允许客户端与服务器建立长连接，使服务器能够  
主动向客户端  
推送实时更新，而无需客户端持续轮询数据。它们主要适用于大型对象的小幅更改以及需要小型实时更新的功能（如聊天系统或协同编辑）。  
  
与常规查询和变更类似，订阅请求定义了返回数据的形状。订阅通常通过   
WebSockets 实现。  
  
什么是   
GraphQL 内省？  
  
GraphQL   
内省是 GraphQL 的内置功能，允许向服务器查询模式化信息。它通常被   
GraphQL IDE 和文档生成工具等应用程序使用。  
  
与常规查询一样，您可以指定希望返回的响应字段和结构。例如，您可能  
希望响应仅包含可用变更的名称。  
  
内省可能构成严重的信息泄露风险，因为它可用于访问潜在敏感信息（如字段描述），并帮助攻击者了解如何与 API 交互。最佳实践是在生产环境中禁用内省功能。  
  
以上就是关于   
GraphQL API   
中较为基础的理论知识，我们可以先大概有个底，知道一些基础内容就可以。这也方便我们后续深入挖掘这类漏洞时，不至于太迷糊。  
  
关于API 漏洞挖掘的相关内容，这边会持续分享，感兴趣的话，记得点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正  
  
