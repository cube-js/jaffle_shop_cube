from cube import context_func
from cube_dbt import load_dbt_manifest_from_url, dbt_models, model_name, model_as_cube, model_as_dimensions

manifest_url = 'https://cube-dbt-integration.s3.amazonaws.com/manifest-jaffle-shop-cube.json'
manifest = load_dbt_manifest_from_url(manifest_url)
models = dbt_models(manifest, path_prefix='marts/')

@context_func
def get_model(name):
  return next(model for model in models if model_name(model) == name)

@context_func
def as_cube(model):
  return model_as_cube(model)

@context_func
def as_dimensions(model):
  return model_as_dimensions(model)