
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from resources.restaurant import Restaurant
from resources.menus import Menus
from resources.menu_item import MenuItem
from common.configdb import init_db, get_db, get_client

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
api = Api(app)

app.config.from_object(__name__)
app.config['TEST'] = False

with app.app_context():
    init_db(get_db(), get_client())

api.add_resource(Restaurant, '/Restaurant', '/Restaurant/<int:restaurant_id>')
api.add_resource(Menus, '/Menus', '/Menus/<int:restaurant_id>','/Menus/<int:restaurant_id>/<category>')

if __name__ == '__main__':
    handler = RotatingFileHandler('logs/gobbledegooks.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    with app.app_context():
        app.run(debug=True)