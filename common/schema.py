from marshmallow import Schema, fields


class ItemSchema(Schema):
	item_id = fields.Integer()
	item_name = fields.String()
	item_price = fields.Decimal()

class MenusSchema(Schema):
	category = fields.String()
	item = fields.Nested(ItemSchema,many = True)

class RestaurantSchema(Schema):
	restaurant_id = fields.Integer()
	restaurant_name = fields.String()
	address = fields.String()
	menus = fields.Nested(MenusSchema, many=True)

