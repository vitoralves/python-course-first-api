from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from .services import PurchaseOrdersItemsService


class PurchaseOrdersItems(Resource):
    __service__ = PurchaseOrdersItemsService()
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida'
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço válido'
    )

    def get(self, id):
        return self.__service__.find_by_purchase_order_id(id)

    def post(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            data = PurchaseOrdersItems.parser.parse_args()
            data['purchase_order_id'] = id

            purchase_orders_item = PurchaseOrdersItemsModel(**data)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()

        return jsonify({'message': 'Purchase order de id {} não encontrado'.format(id)})
