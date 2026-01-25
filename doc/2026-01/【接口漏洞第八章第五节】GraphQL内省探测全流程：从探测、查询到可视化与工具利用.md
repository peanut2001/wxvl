#  【接口漏洞第八章第五节】GraphQL内省探测全流程：从探测、查询到可视化与工具利用  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-25 14:00  
  
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
在上一节中[【接口漏洞第八章第四节】GraphQL漏洞挖掘实战：找不到参数？用“内省”透视API底层](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797781&idx=1&sn=ecf90878e8610d50c424203a930b202f&scene=21#wechat_redirect)  
我们大概知道了GraphQL API接口的  
内省功能，今天我们来继续深入探测内省功能。  
  
在生产环境中，有安全意识的厂商通常会禁用  
内省功能，但这一安全做法并非总是被遵循，这也就成为我们挖洞的切入点之一了。  
  
一、探测  
  
我们可以使用以下简单查询来探测  
内省功能。如果内省功能已启用，响应将返回所有可  
用查询的名称。  
```
graphql
# 内省探测请求
{
    "query": "{__schema{queryType{name}}}"
}
```  
  
注意：BurpSuite Scanner 工具可在扫描过程中自动探测内省功能。如果发现内省功能已启用，它会报告“  
GraphQL 内省功能已启用”问题。  
  
二、运行完整内省查询  
  
下一步是对端点运行  
完整的内省查询，以尽可能获取底层架构的详细信息。  
  
以下示例查询返回所有  
查询、  
变更、  
订阅、  
类型及  
片段的完整详情：  
```
graphql
# 完整内省查询
query IntrospectionQuery {
    __schema {
        queryType { name }
        mutationType { name }
        subscriptionType { name }
        types { ...FullType }
        directives {
            name
            description
            args { ...InputValue }
            onOperation   # 常需删除此项以运行查询
            onFragment    # 常需删除此项以运行查询
            onField       # 常需删除此项以运行查询
        }
    }
}
fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
        name
        description
        args { ...InputValue }
        type { ...TypeRef }
        isDeprecated
        deprecationReason
    }
    inputFields { ...InputValue }
    interfaces { ...TypeRef }
    enumValues(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
    }
    possibleTypes { ...TypeRef }
}
fragment InputValue on __InputValue {
    name
    description
    type { ...TypeRef }
    defaultValue
}
fragment TypeRef on __Type {
    kind
    name
    ofType {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
            }
        }
    }
}
```  
  
注意：如果内省功能已启用但上述查询无法运行，可尝试从查询结构中移除   
onOperation、  
onFragment 和   
onField 指令。许多端点不接受这些指令作为内省查询的一部分，移除后通常能更顺利地进行内省。  
  
三、可视化内省结果  
  
内省查询的响应可能包含大量信息，但通常内容冗长且难以处理。  
  
我们可以使用  
 GraphQL 可视化工具更直观地查看架构实体之间的关系。该在线工具可接收  
内省查询的结果，并生成返回数据的可视化图表，包括操作与类型之间的关联关系。  
  
四、例外情况--建议功能  
  
即使  
内省功能被完全  
禁用，您有时仍可利用  
建议功能来推断 API 的结构信息。  
  
建议功能是 Apollo GraphQL 平台的一项特性，服务器可在错误消息中提示查询修正建议。这通常用于查询存在轻微错误但仍可识别的情况（例如：“找不到 ‘  
productInfo’ 条目，您是否想查询 ‘  
productInformation’？”）。  
  
通过此功能，我们可能获取到有用信息，因为响应实际上透露了架构中的有效字段或类型。  
  
Clairvoyance【工具地址：  
https://github.com/nikitastupin/clairvoyance  
】 是一款利用建议功能自动恢复 GraphQL 架构（全部或部分）的工具，即使在内省功能被禁用时也能生效。这大大减少了从建议响应中拼凑信息所需的时间。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q2nYmgvicUOLibmvuSa8aQeFfe7CsjKcyM5XP8yp5cJTHUDbl2a1W7FR3iaMTBYwYicmnmAa2YxNHb7Qg/640?wx_fmt=png&from=appmsg "")  
  
今天的内容就先分享到这，明天这边会结合实际的应用场景，给大家分享  
结合前面理论内容，如何挖掘  
有关   
GraphQL API 漏洞的内容。感兴趣的话，可以点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
