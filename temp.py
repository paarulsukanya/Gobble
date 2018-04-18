from flask import Flask
from flask_dynamo import Dynamo
from boto3.session import Session
from app import app, dynamo

#boto_sess = Session(
#    region_name='us-east-1',
#    aws_access_key_id='GobbleDB',
#    aws_secret_access_key='YYYYYYYYYYYYYYY')

#app = Flask(__name__)
#app.config['DYNAMO_SESSION'] = boto_sess
#app.config['DYNAMO_ENABLE_LOCAL'] = True
#app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
#app.config['DYNAMO_LOCAL_PORT'] = 8000

#dynamo = Dynamo()
#dynamo.init_app(app)

for table_name, table in dynamo.tables.items():
    print(table_name, table)



# # from flask import Flask
# # from flask_dynamo import Dynamo

# # app = Flask(__name__)
# # app.config['DYNAMO_TABLES'] = [
# #     {
# #          TableName='restaurant',
# #          KeySchema=[dict(AttributeName='restaurant_id', KeyType='HASH'),
# #          dict(AttributeName='item_id', KeyType='HASH'),
# #          dict(AttributeName='menu_type', KeyType='RANGE')],
# #          AttributeDefinitions=[dict(AttributeName='restaurant_id', AttributeType='N'),
# #          dict(AttributeName='restaurant_name', AttributeType='S'),
# #          dict(AttributeName='restaurant_address', AttributeType='S'),
# #          dict(AttributeName='restaurant_rating', AttributeType='N'),
# #          dict(AttributeName='menu_type', AttributeType='S'),
# #          dict(AttributeName='item_id', AttributeType='N'),
# #          dict(AttributeName='item_name', AttributeType='S'),
# #          dict(AttributeName='item_price', AttributeType='N')],
# #          ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
# #     }
# #  ]


# # app.py

# # app.py

# from flask import Flask
# from flask_dynamo import Dynamo
# from boto3.session import Session

# boto_sess = Session(
#     region_name='us-east-1',
#     aws_access_key_id='GobbleDB',
#     aws_secret_access_key='YYYYYYYYYYYYYYY')


# def create_app():
#     app = Flask(__name__)
#     app.config['DYNAMO_SESSION'] = boto_sess
#     app.config['DYNAMO_ENABLE_LOCAL'] = True
#     app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
#     app.config['DYNAMO_LOCAL_PORT'] = 8000
#     app.config['DYNAMO_TABLES'] = [
#         dict(
#              TableName='users',
#              KeySchema=[dict(AttributeName='username', KeyType='HASH')],
#              AttributeDefinitions=[dict(AttributeName='username', AttributeType='S')],
#              ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#         ), dict(
#              TableName='groups',
#              KeySchema=[dict(AttributeName='name', KeyType='HASH')],
#              AttributeDefinitions=[dict(AttributeName='name', AttributeType='S')],
#              ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#         )
#     ]

#     return app


# app = create_app()

# dynamo = Dynamo()
# dynamo.init_app(app)

# with app.app_context():
#     dynamo.create_all()

# @app.route('/create_user')
# def create_user():
#     dynamo.tables['users'].put_item(Item={
#         'username': 'rdegges',
#         'first_name': 'Randall',
#         'last_name': 'Degges',
#         'email': 'r@rdegges.com',
#     })

# create_user()