from cube import config, file_repository

# config.schema_path = 'model'

# config.base_path = '/cube-api'

# TODO: Not tested
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

# @config('context_to_app_id')
# def context_to_app_id(ctx: dict) -> str:
#   return f"CUBE_APP_{ctx['securityContext']['tenant_id']}"

# @config('context_to_orchestrator_id')
# def context_to_orchestrator_id(ctx: dict) -> str:
#   return f"CUBE_APP_{ctx['securityContext']['tenant_id']}"

# @config('repository_factory')
# def repository_factory(ctx: dict) -> list[dict]:
#   return file_repository('model')
 
# @config('repository_factory')
# def repository_factory(ctx: dict) -> list[dict]:
#   context = ctx['securityContext']
 
#   return [
#     {
#       'fileName': 'file.js',
#       'content': 'cube("foo", {sql_table:"123",measures:{count:{type:"count"}}})'
#     }
#   ]
 
# @config('check_auth')
# def check_auth(ctx: dict, token: str) -> None:
#   context = ctx['securityContext']

#   if token == 'my_secret_token':
#     return

#   raise Exception('Access denied')

# @config('check_sql_auth')
# def check_sql_auth(req: dict, user_name: str) -> dict:
#   if user_name == 'my_user':
#     return {
#       'password': 'my_password',
#       'securityContext': {
#         'some': 'data'
#       }
#     }

#   raise Exception('Access denied')
  
# @config('can_switch_sql_user')
# def can_switch_sql_user(current_user: str, new_user: str) -> dict:
#   if current_user == 'admin':
#     return True

#   if current_user == 'service':
#     return new_user != 'admin'

#   return False

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

# @config('query_rewrite')
# def query_rewrite(query: dict, ctx: dict) -> dict:
#   context = ctx['securityContext']
 
#   if 'filter_by_region' in context:
#     query['filters'].append({
#       'member': 'regions.id',
#       'operator': 'equals',
#       'values': [context['region_id']],
#     })
 
#   return query

# @config('pre_aggregations_schema')
# def pre_aggregations_schema(ctx: dict) -> str:
#   return f"pre_aggregations_{ctx['securityContext']['tenant_id']}"

# import random

# @config('schema_version')
# def schema_version(ctx: dict) -> str:
#   # Don't do this!
#   # Data model would be recompiled on each request
#   context = ctx['securityContext']

#   return random.random()

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