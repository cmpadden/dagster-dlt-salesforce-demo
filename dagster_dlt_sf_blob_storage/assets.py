import dlt
from dagster import (
    AssetExecutionContext,
)
from dagster_embedded_elt.dlt import (
    DagsterDltResource,
    dlt_assets,
)
from dlt_pipelines.salesforce import salesforce_source


dlt_resource = DagsterDltResource()


# limit resources to just `sf_users`
@dlt_assets(
    dlt_source=salesforce_source().with_resources("sf_user"),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="salesforce",
        destination="filesystem",
        dataset_name="salesforce_data",
    ),
    name="salesforce",
    group_name="salesforce",
)
def salesforce_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)
