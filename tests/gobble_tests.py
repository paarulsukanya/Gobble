import os
import unittest
#from ..common.schema import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import gobble
from common.configdb import get_db, get_client, init_db, delete_db


class TestRestaurantsGetAll(unittest.TestCase):
	def setUp(self):

		self.client = gobble.app.test_client()
		#self..config.from_object(__name__)
		self.client.config['TEST'] = True

		with gobble.app.app_context():
			db = get_db()
			client = get_client()
			init_db(db, client)

			client.put_item(TableName='restaurant',Item='{"restaurant_id":111, \
															"restaurant_name":"IHOP", \
															"menu":[{"category":"Breakfast", \
															"items":[{"item_id":2, "item_name":"Pan Cakes", "item_price":25}]}]}')
			client.put_item(TableName='restaurant',Item='{"restaurant_id":300, \
															"restaurant_name":"Cheese Cake Factory", \
															"menu":[{"category":"Dinner", \
															"items":[{"item_id":2, "item_name":"Cheese Cakes", "item_price":50}]}]}')
			client.put_item(TableName='restaurant',Item='{"restaurant_id":99, \
															"restaurant_name":"Kabob and Curry", \
															"menu":[{"category":"Lunch", \
															"items":[{"item_id":2, "item_name":"Biryani", "item_price":20}]}]}')


	def testGetAllRests(self):
		pass

	def tearDown(self):
		with gobble.app.app_context():
			delete_db()

'''
class TestGobbleUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'hello': 'world'})


class TestGobble(unittest.TestCase):
    def setUp(self):
        self.app = flaskapi.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {'hello': 'world'})

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/')
        assert <make your assertion here>
'''

if __name__ == "__main__":
    unittest.main()