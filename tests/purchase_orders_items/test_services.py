import pytest
from purchase_orders_items.services import PurchaseOrdersItemsService


def test_check_maximum_po_quantity(seed_db):
    with pytest.raises(QuantityException) as ex:
        PurchaseOrdersItemsService()._check_maximum_purchase_order_quantity(
            seed_db['purchase_orders'].id, 30)
    assert ex.value.code == 400
    assert ex.value.description == 'Você somente pode adicionar mais 20 itens'
