
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from resources.restaurant import Restaurant
from resources.menu import Menu
from resources.menu_item import MenuItem
from common.configdb import createTable

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
api = Api(app)

initDB()

api.add_resource(Restaurant, '/Restaurant', '/Restaurant/<int:id>')
api.add_resource(Menu, '/Menu', '/Menu/<int:id>')
api.add_resource(MenuItem, '/MenuItem', '/MenuItem/<int:id>')

if __name__ == '__main__':
    handler = RotatingFileHandler('logs/gobbledegooks.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.run(debug=True)