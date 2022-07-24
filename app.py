from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.99
            }
        ]
    }
]


class PurchaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)


api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(port=5000)
