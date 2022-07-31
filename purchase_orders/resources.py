from flask import jsonify
from flask_restful import Resource, reqparse

purchase_orders = [
    {
        'id': 1,
        'description': 'Purchase ORder id 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 19.99
            }
        ]
    }
]


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID válido'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida'
    )

    def get(self):
        return jsonify(purchase_orders)

    def post(self):
        data = PurchaseOrders.parser.parse_args()

        purchase_order = {
            'id': data['id'],
            'description': data['description'],
            'items': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)
