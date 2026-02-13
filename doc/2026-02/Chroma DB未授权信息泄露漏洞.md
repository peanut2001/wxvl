#  Chroma DB未授权信息泄露漏洞  
 TtTeam   2026-02-13 16:41  
  
<table><thead><tr style="height:39px;"><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">项目</span></p></th><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">详情</span></p></th></tr></thead><tbody><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">漏洞名称</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">Chroma DB未授权信息泄露漏洞（Unauthorized Information Disclosure）</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">发现者</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">Shay Ben Tikva</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">风险等级</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><strong><span leaf=""><span textstyle="" style="font-weight: normal;">高危（High）</span></span></strong></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">关联组件</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">Chroma DB（向量数据库）</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">官方参考</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">https://www.trychroma.com/security</span></p></td></tr></tbody></table>  
  
二、漏洞核心原理与危害  
  
Chroma DB作为一款开源向量数据库，广泛应用于AI应用、语义搜索等场景，其核心功能依赖集合（Collections）管理向量数据。本次发现的未授权信息泄露漏洞，根源在于Chroma DB的集合相关端点存在访问控制配置缺陷，未对请求者身份进行严格校验，同时Swagger/OpenAPI文档端点暴露敏感接口细节，进一步扩大了攻击面。  
  
具体而言，漏洞主要体现在两个维度：其一，Chroma DB的集合端点可直接泄露集合元数据，攻击者无需认证即可通过接口获取完整的Chroma数据，包括数据ID、名称、配置信息、维度参数及其他向量相关核心数据，这些数据往往涉及业务核心逻辑或用户敏感信息；其二，应用的/docs端点默认开放，泄露了完整的Swagger/OpenAPI规范，攻击者可通过该文档枚举所有可用接口、参数格式及业务逻辑，为后续精准攻击（如进一步数据窃取、接口滥用）提供便利。  
  
该漏洞的高危属性源于其“零认证门槛”的利用条件——攻击者仅需发起HTTP请求即可获取敏感数据，无需复杂的技术手段。一旦攻击者成功枚举集合并窃取向量数据，可能导致业务数据泄露、AI模型训练数据被盗、用户隐私信息曝光等严重后果，对依赖Chroma DB的企业及应用造成不可逆的损失。  
  
三、漏洞检测方法  
  
针对该漏洞，可通过发送特定HTTP请求至目标Chroma DB服务端点，验证是否存在信息泄露情况，检测过程简单高效，最大请求次数不超过2次，且支持“命中即停止”的检测逻辑。  
  
漏洞匹配条件  
  
需同时满足以下两个条件，方可确认漏洞存在：  
  
1. 响应体特征匹配：响应Body中包含以下关键字段（均为Chroma DB集合核心配置数据，具有唯一性）："sync_threshold":、"hnsw_configuration":、"tenant":"default_tenant"、"database":"default_database"。  
  
2. 响应头特征匹配：响应Header中包含"application/json"，表明接口正常返回JSON格式数据，而非错误页或拦截提示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB0S28fQebuyVHiatq18c0iasHcCovDjcZGFIU1anIPQYllgl6iaDyuENWz9Cn3M7AmKUytETVuFjHgQw/640?wx_fmt=png&from=appmsg "")  
  
  
防丢失  
  
  
  
