from flask_restful import Resource,reqparse,fields, marshal_with
from boto3.dynamodb.conditions import Key, Attr
from common.configdb import dynamodb,ddbclient
import decimal
import json

table = dynamodb.Table('restaurant')


parser = reqparse.RequestParser()
parser.add_argument('restaurant_id', type=int, required=True)
parser.add_argument('restaurant_name',required=True)




menu_item_fields = {
	'menu_item_id': fields.Integer,
	'menu_item_name': fields.String,
	'menu_item_price': fields.Float,
}
menu_fields = {
	'category': fields.String,
	'items': fields.Nested(menu_item_fields),
}

restaurant_fields = {
	'restaurant_id': fields.Integer,
	'restaurant_name': fields.String,
	'address': fields.String,
	'menu': fields.Nested(menu_fields),
}


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

class Restaurant(Resource):
    def get(self):
    	#return details of all retaurants
    	response = table.scan()
    	items = json.dumps(response['Items'], cls=DecimalEncoder) #[json.dumps(i, cls=DecimalEncoder) for i in response['Items']]
    	print("GET LOG:", items)
    	return items

    @marshal_with(restaurant_fields)
    def post(self):
       
    	args = parser.parse_args()

        # if not 'restaurant_id' in args or not 'restaurant_name' in args:
        #     # we return bad request since we require name and id
        #     return {'message': 'Missing required parameters.'}, 400
        print("POST LOG", args)
        resp = ddbclient.put_item(TableName='restaurant',Item=args)
        return resp, 201
