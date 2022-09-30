from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
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
    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='Informe uma quantidade válida'
    )

    @jwt_required()
    def get(self, id):
        return self.__service__.find_by_purchase_order_id(id)

    @jwt_required()
    def post(self, id):
        data = PurchaseOrdersItems.parser.parse_args()
        data['purchase_order_id'] = id
        return self.__service__.create(**data)
