from cube import template
from cube_dbt import Dbt

context = template.JinjaContext()

manifest_url = 'https://cube-dbt-integration.s3.amazonaws.com/manifest-jaffle-shop-cube.json'

dbt = (
  Dbt
  .from_url(manifest_url)
  .filter(paths=['marts/'])
)

@context.function
def dbt_model(name):
  return dbt.model(name)