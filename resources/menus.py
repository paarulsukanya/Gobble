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

class Menus(Resource):
    def get(self,restaurant_id):
		db = get_db()
		client = get_client()
		table = db.Table('restaurant')

		response = table.query(
		    KeyConditionExpression=Key('restaurant_id').eq(restaurant_id)
		)
		res = json.dumps(response['Items'], cls=DecimalEncoder) 
		app.logger.info("GET_LOG: " + str(res))
		return res,200

    def post(self,restaurant_id):

		db = get_db()
		client = get_client()
		table = db.Table('restaurant')

		body = request.json
		data, error = RestaurantSchema().dump(body)

		response = table.update_item(
		Key={
			'restaurant_id': restaurant_id
		},
		UpdateExpression="set menus = :m",
		ExpressionAttributeValues={
			':m': body
		},
		ReturnValues="UPDATED_NEW"
		)
		res = json.dumps(response, cls=DecimalEncoder)
		app.logger.info("POST_LOG: "+ str(res))
		return res, 201

    def delete(self, restaurant_id): 

		db = get_db()
		client = get_client()
		table = db.Table('restaurant')

		response = table.update_item(
		Key={
			'restaurant_id': restaurant_id
		},
		UpdateExpression="set menu = :m",
		ExpressionAttributeValues={
			':m': []
		},
		ReturnValues="UPDATED_NEW"
		)
		res = json.dumps(response, cls=DecimalEncoder)
		app.logger.info("DEL_LOG: "+ str(res))
		return res, 204

