# from google.cloud import bigquery

# Construct a BigQuery client object.
# client = bigquery.Client()
#
# # TODO(developer): Set table_id to the ID of the table to create.
# table_id = "my-firebase-project-0001.btc_auto.test"
#
# schema = [
#     bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
#     bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
# ]
#
# table = bigquery.Table(table_id, schema=schema)
# table = client.create_table(table)  # Make an API request.
# print(
#     "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
# )
#
#
# def get_table_ref(dataset_id, table_id):
#     """
#     Get table ref to project and dataset
#     :param dataset_id:
#     :param table_id:
#     :return:
#     """
#     dataset_ref = bigquery.DatasetReference(project, dataset_id)
#     table_ref = bigquery.TableReference(dataset_ref, table_id)
#     return table_ref

from GoogleCloudBigQuery import GoogleCloudBigQuery
gcbq = GoogleCloudBigQuery('my-firebase-project-0001')
