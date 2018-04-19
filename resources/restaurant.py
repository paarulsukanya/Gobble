from flask import request, current_app
from flask_restful import Resource,reqparse
from marshmallow import Schema, fields
from boto3.dynamodb.conditions import Key, Attr
from common.configdb import get_db, get_client
from common.utils import DecimalEncoder
from common.schema import ItemSchema, MenusSchema, RestaurantSchema
import decimal
import json

app = current_app


class Restaurant(Resource):
    def get(self,restaurant_id=None):

		db = get_db()
		client = get_client()
		table = db.Table('restaurant')

		response=None
		if restaurant_id:
			response = table.query(KeyConditionExpression=Key('restaurant_id').eq(restaurant_id))
		else:
			#return details of all retaurants
			response = table.scan()

		res = json.dumps(response['Items'], cls=DecimalEncoder)
		app.logger.info("GET_LOG: " + res)
		return res, 200

   
    def post(self):
		db = get_db()
		client = get_client()
		table = db.Table('restaurant')
    	
		body = request.json
		items, error = RestaurantSchema().dump(body)

		app.logger.info("POST_LOG: "+ str(items))
		resp = client.put_item(TableName='restaurant',Item=items)
		return resp, 201


    def put(self,restaurant_id):
		db = get_db()
		client = get_client()
		table = db.Table('restaurant')

		body = request.json
		#data,error = RestaurantSchema().dump(body)

		response = table.update_item(
			Key={
		        'restaurant_id': restaurant_id
		    },
		    UpdateExpression="set restaurant_name = :r",
		    ExpressionAttributeValues={
		        ':r': body['restaurant_name']
		    },
		    ReturnValues="UPDATED_NEW"
		)

		items = json.dumps(response, cls=DecimalEncoder)
		app.logger.info("PUT_LOG: "+ str(items))
		return items, 200

    def delete(self, restaurant_id):
		#deleting only on id

		db = get_db()
		client = get_client()
		table = db.Table('restaurant')


		response = table.delete_item(Key={
			'restaurant_id': restaurant_id
			})
		items = json.dumps(response, cls=DecimalEncoder)
		app.logger.info("DEL_LOG: " + str(items))
		return "restaurant_id:" + str(restaurant_id) +" has been deleted", 204
