from google.cloud import bigquery
from google.api_core import exceptions


project_id = 'my-firebase-project-0001'
bq_client = bigquery.Client(project=project_id)


def bq_create_partition_table(
        dataset_id,
        tbl_id,
        schema,
        part_type,
        part_field
):
    tbl_ref = table_ref(dataset_id, tbl_id)

    try:
        bq_client.get_table(tbl_ref)
    except exceptions.NotFound:
        table = bigquery.Table(tbl_ref, schema=schema)
        table.time_partitioning = bigquery.TimePartitioning(
            type_=part_type,
            field=part_field,
            expiration_ms=600000
        )
        bq_client.create_table(table)


def table_ref(dataset_id, tbl_id):
    dataset_ref = bigquery.DatasetReference(dataset_id=dataset_id, project=project_id)
    tbl_ref = dataset_ref.table(tbl_id)
    return tbl_ref


if __name__ == '__main__':
    schema = [
        bigquery.SchemaField('unix', 'TIMESTAMP', mode='REQUIRED'),
        bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED'),
    ]

    bq_create_partition_table('btc_auto', 'test2', schema, 'HOUR', 'unix')
