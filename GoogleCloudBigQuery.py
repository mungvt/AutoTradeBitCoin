from google.cloud import bigquery


class GoogleCloudBigQuery(object):
    """
    Wrapper Class of Google Cloud BigQuery client.
    """
    def __init__(self, project_id):
        self.project = project_id
        self.client = bigquery.Client(project=project_id)

    def create_partition_table(
            self,
            dataset_id,
            table_id,
            schema,
            partition_type,
            partition_field,
            exists_ok=False
    ):
        """
        Create time-partitioning table
        :param dataset_id:
        :param table_id:
        :param schema:
        :param partition_type:
        :param partition_field:
        :param exists_ok:
        :return:
        """
        table_ref = self.get_table_ref(dataset_id, table_id)
        table = bigquery.Table(table_ref, schema=schema)
        table.time_partitioning = bigquery.TimePartitioning(
            type_=partition_type,
            field=partition_field,
        )
        self.client.create_table(table, exists_ok=exists_ok)

    def get_table_ref(self, dataset_id, table_id):
        """
        Get table ref to project and dataset
        :param dataset_id:
        :param table_id:
        :return:
        """
        dataset_ref = bigquery.DatasetReference(self.project, dataset_id)
        table_ref = bigquery.TableReference(dataset_ref, table_id)
        return table_ref
