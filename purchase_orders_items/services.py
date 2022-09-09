from flask import jsonify

from purchase_orders.model import PurchaseOrderModel
from .model import PurchaseOrdersItemsModel


class PurchaseOrdersItemsService:

    def find_by_purchase_order_id(self, purchase_order_id):
        purchase_order = PurchaseOrderModel.find_by_id(purchase_order_id)
        if purchase_order:
            purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(
                purchase_order_id)

            return [p.as_dict() for p in purchase_orders_items]
        return jsonify({'message': 'Pedido de id {} não encontrado'.format(purchase_order_id)})
