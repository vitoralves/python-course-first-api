from flask import jsonify

from purchase_orders.model import PurchaseOrderModel
from .model import PurchaseOrdersItemsModel
from exceptions.exceptions import QuantityException


class PurchaseOrdersItemsService:

    def _check_maximum_purchase_order_quantity(self, purchase_order_id, purchase_order_quantity, quantity):
        purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(
            purchase_order_id)

        sum_items = 0
        for poi in purchase_orders_items:
            sum_items += poi.quantity

        if sum_items + quantity > purchase_order_quantity:
            raise QuantityException('Você somente pode adicionar mais {} itens'.format(
                purchase_order_quantity - sum_items))

    def find_by_purchase_order_id(self, purchase_order_id):
        purchase_order = PurchaseOrderModel.find_by_id(purchase_order_id)
        if purchase_order:
            purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(
                purchase_order_id)

            return [p.as_dict() for p in purchase_orders_items]
        return jsonify({'message': 'Pedido de id {} não encontrado'.format(purchase_order_id)})

    def create(self, **kwargs):
        purchase_order = PurchaseOrderModel.find_by_id(
            kwargs['purchase_order_id'])
        if purchase_order:
            self._check_maximum_purchase_order_quantity(
                purchase_order.id, purchase_order.quantity, kwargs['quantity'])
            purchase_orders_item = PurchaseOrdersItemsModel(**kwargs)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()

        return jsonify({'message': 'Purchase order de id {} não encontrado'.format(kwargs['purchase_order_id'])})
