import pytest
from purchase_orders.services import PurchaseOrdersService
from exceptions.exceptions import QuantityException


@pytest.mark.nocleardb
def test_check_quantity_less_then_miminum():
    with pytest.raises(QuantityException) as ex:
        PurchaseOrdersService()._check_quantity(30)
    assert ex.value.code == 400
    assert ex.value.description == 'A quantidade deve ser entre 50 e 150 itens'


@pytest.mark.nocleardb
def test_check_quantity_greater_then_maximum():
    with pytest.raises(QuantityException) as ex:
        PurchaseOrdersService()._check_quantity(151)
    assert ex.value.code == 400
    assert ex.value.description == 'A quantidade deve ser entre 50 e 150 itens'
