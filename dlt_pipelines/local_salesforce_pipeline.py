import dlt

from salesforce import salesforce_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="salesforce",
        destination="filesystem",
        dataset_name="salesforce_data",
    )

    # limit resources to just `sf_users`
    load_info = pipeline.run(salesforce_source().with_resources("sf_user"))

    print(load_info)
