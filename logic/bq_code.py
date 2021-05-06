from google.cloud import bigquery
import os
import configparser
import model
import logic

config = configparser.ConfigParser()
config.read('config/config.ini')

FILE_PATH = config['DEFAULT']['FILE_PATH']

BQ_KEY_PATH = config['BIGQUERY']['BQ_KEY_PATH']
URI_DATA = config['BIGQUERY']['URI_DATA']
PROJECT_ID = config['BIGQUERY']['PROJECT_ID']
DATABASE = config['BIGQUERY']['DB']
TABLE = config['BIGQUERY']['TABLE']

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(BQ_KEY_PATH)
project_id = PROJECT_ID
bq_client = bigquery.Client(project=project_id)


def bq_create_partition_table(
        dataset_id,
        tbl_id,
        schema_,
        part_type,
        part_field
):
    tbl_ref = table_ref(dataset_id, tbl_id)
    delete_table(dataset_id, tbl_id)

    table = bigquery.Table(tbl_ref, schema=schema_)
    table.time_partitioning = bigquery.TimePartitioning(
        type_=part_type,
        field=part_field,
    )
    bq_client.create_table(table)
    result = f"Create table {tbl_ref} successfully!"
    print(result)
    return result


def load_data_from_gs_into_table(
        dataset_id,
        tbl_id,
        schema_,
        skip_rows,
        uri_file
):
    job_config = bigquery.LoadJobConfig(
        schema=schema_,
        skip_leading_rows=skip_rows,
        source_format=bigquery.SourceFormat.CSV,
    )
    tbl_ref = table_ref(dataset_id, tbl_id)
    load_job = bq_client.load_table_from_uri(
        uri_file, tbl_ref, job_config=job_config
    )
    load_job.result()
    print(f"Load table {tbl_ref} successfully!")


def load_data_from_local_into_table(
        dataset_id,
        tbl_id,
        schema_,
        skip_rows,
        file_path
):
    job_config = bigquery.LoadJobConfig(
        schema=schema_,
        skip_leading_rows=skip_rows,
        source_format=bigquery.SourceFormat.CSV,
    )
    tbl_ref = table_ref(dataset_id, tbl_id)
    with open(file_path, "rb") as source_file:
        load_job = bq_client.load_table_from_file(source_file, tbl_ref, job_config=job_config)
    load_job.result()
    print(f"Load table {tbl_ref} successfully!")


def delete_table(dataset_id, table_id, not_found_ok=False):
    tbl_ref = table_ref(dataset_id, table_id)
    bq_client.delete_table(tbl_ref, not_found_ok=not_found_ok)
    print(f"Delete table {tbl_ref} successfully!")


def table_ref(dataset_id, tbl_id):
    dataset_ref = bigquery.DatasetReference(dataset_id=dataset_id, project=project_id)
    tbl_ref = dataset_ref.table(tbl_id)
    return tbl_ref


def create_all_tables():
    if logic.is_dryrun():
        print("create all table")
    else:
        bq_create_partition_table(DATABASE, TABLE, model.btc_schema, 'DAY', 'unix')


def load_btc_data_into_bq():
    if logic.is_dryrun():
        print("import data")
    else:
        file_path = os.path.abspath(FILE_PATH)
        load_data_from_local_into_table(DATABASE, TABLE, model.btc_schema, 1, file_path)


if __name__ == '__main__':
    # create_all_tables()
    # load_btc_data_into_bq()
    create_all_tables()
