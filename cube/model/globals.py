from cube import TemplateContext
from cube_dbt import Dbt

template = TemplateContext()

manifest_url = 'https://cube-dbt-integration.s3.amazonaws.com/manifest-jaffle-shop-cube.json'

dbt = Dbt.from_url(manifest_url).filter(paths=['marts/'])

@template.function('dbt_model')
def dbt_model(name):
  return dbt.model(name)