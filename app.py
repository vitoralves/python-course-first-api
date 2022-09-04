from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from db import db

from purchase_orders.resources import PurchaseOrders, PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems


def create_app(env):
    app = Flask(__name__)
    api = Api(app)

    database = 'python_course'
    if env == 'testing':
        database = 'python_course_test'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost:5433/{}'.format(
        database)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    Migrate(app, db)

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrderById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
