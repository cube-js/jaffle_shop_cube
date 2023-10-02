from cube import config

# config.schema_path = 'model'

# config.base_path = '/cube-api'

# Not tested
# config.web_sockets_base_path = '/cube-web-sockets'

# @config('logger')
# def logger(message: str, params: dict) -> None:
#   print(f"{message}: {params}")

# @config('driver_factory')
# def driver_factory(ctx: dict) -> None:
#   context = ctx['securityContext']
#   data_source = ctx['dataSource']
#   print(context)
#   print(data_source)
 
#   return {
#     'type': 'postgres',
#     'host': 'demo-db-examples.cube.dev',
#     'user': 'cube',
#     'password': '12345',
#     'database': 'ecom'
#   }
 
# @config('context_to_api_scopes')
# def context_to_api_scopes(context: dict, default_scopes: list[str]) -> list[str]:
#   return ['meta', 'data', 'graphql']

# contextToAppId
# contextToOrchestratorId
# repositoryFactory
# checkAuth
# checkSqlAuth
# canSwitchSqlUser

# @config('query_rewrite')
# def query_rewrite(query: dict, ctx: dict) -> dict:
#   query['measures'] = ['orders.count']
  
#   if 'min_count' in ctx['securityContext']:
#     query['filters'] = [{
#       'member': 'orders.count',
#       'operator': 'gt',
#       'values': [ctx['securityContext']['min_count']]
#     }]
  
#   return query

# preAggregationsSchema
# schemaVersion
# scheduledRefreshTimer
# scheduledRefreshTimeZones
# scheduledRefreshContexts
# extendContext
# compilerCacheSize
# maxCompilerCacheKeepAlive
# updateCompilerCacheKeepAlive
# allowUngroupedWithoutPrimaryKey
# telemetry
# http.cors
# jwt
# jwkUrl
# key
# algorithms
# issuer
# audience
# subject
# claimsNamespace
# cacheAndQueueDriver
# orchestratorOptions
# allowJsDuplicatePropsInSchema
# initApp
# processSubscriptionsInterval
# QueueOptions
# RequestContext
# securityContext
# SchemaFileRepository