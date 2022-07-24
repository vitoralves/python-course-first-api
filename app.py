from flask import Flask
from flask_restful import Api

from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById

app = Flask(__name__)
api = Api(app)

api.add_resource(PurchaseOrders, '/purchase_orders')
api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')

app.run(port=5000)
