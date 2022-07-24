from flask import Flask
from flask_restful import Api

from purchase_orders.resources import PurchaseOrders

app = Flask(__name__)
api = Api(app)

api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(port=5000)
