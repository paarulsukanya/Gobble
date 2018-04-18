import boto3

dynamodb = boto3.resource('dynamodb', 
        region_name='us-east-1', 
        endpoint_url="http://localhost:8000",
        aws_access_key_id='GobbleDB',
        aws_secret_access_key='YYYYYY')

ddbclient = dynamodb.meta.client


def initDB(conn,table_name):
    all_tables = [i.table_name for i in conn.tables.all()]
    if table_name not in all_tables:
        table = conn.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'restaurant_id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'restaurant_id',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 500,
            'WriteCapacityUnits': 500
        })
        return table
    else:
        return conn.Table(table_name)


def deleteDB(conn):
    table_iterator = iter(conn.tables.all())
    curr=next(table_iterator)
    while curr:
        curr.delete()
        curr=next(table_iterator)

# TODO: delete this function treat dynamodb as global instead of conn and dont pass table-name as param to initDB 
def createTable():
    print(initDB(dynamodb,'restaurant'))
    #print(ddbclient.list_tables())