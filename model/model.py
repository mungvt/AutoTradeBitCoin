from google.cloud import bigquery


btc_schema = [
        bigquery.SchemaField('unix', 'DATE', mode='REQUIRED'),
        bigquery.SchemaField('open', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('high', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('low', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('close', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('volume', 'FLOAT', mode='REQUIRED'),
        bigquery.SchemaField('quote_av', 'FLOAT', mode='REQUIRED')
    ]
