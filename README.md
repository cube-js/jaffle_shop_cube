# Using dbt with Cube

* For structuring dbt projects follow this guide - https://docs.getdbt.com/guides/best-practices/how-we-structure/2-staging
* Do not create denormalized marts, following this guide for marts design - https://docs.getdbt.com/guides/best-practices/how-we-structure/5-semantic-layer-marts
* Your `marts` folder should contain normalized datasets-entities with dimensions
* bring dbt `marts` from dbt to Cube as cubes. Use `cube_dbt` integration for this.
* define measures and joins on cube level 
* define views as virutal denormalized marts and expose them to your BI tools