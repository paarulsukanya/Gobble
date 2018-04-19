import boto3
from flask import current_app

app = current_app

dynamodb = boto3.resource('dynamodb', 
        region_name='us-east-1', 
        endpoint_url="http://localhost:8000",
        aws_access_key_id='GobbleDB',
        aws_secret_access_key='YYYYYY')
ddbclient = dynamodb.meta.client

testdb = boto3.resource('dynamodb', 
        region_name='us-east-1', 
        endpoint_url="http://localhost:8000",
        aws_access_key_id='TestDB-1',
        aws_secret_access_key='YYYYYY')
tdbclient = testdb.meta.client



def get_db():
    return testdb if app.config['TEST'] else dynamodb

def get_client():
    return tdbclient if app.config['TEST'] else ddbclient

def init_db(db, client):
    app.logger.info("Initializing DB ...")
    table_name = 'restaurant'
    all_tables = [i.table_name for i in db.tables.all()]
    if table_name not in all_tables:
        table = db.create_table(
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
        return db.Table(table_name)


def delete_db(db, client):
    table_iterator = iter(db.tables.all())
    curr=next(table_iterator, None)
    while curr:
        curr.delete()
        curr=next(table_iterator, None)