import json


def test_get_items_by_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/1/items')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Item do pedido 1'
    assert response.json[0]['price'] == 19.99


def test_get_items_by_purchase_order_id_not_found(test_client):
    id = 9999
    response = test_client.get('/purchase_orders/{}/items'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Pedido de id {} não encontrado'.format(
        id)


def test_post_purchase_order_item(test_client):
    obj = {
        'id': 2,
        'description': 'Item teste',
        'price': 10.0
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert len(response.json['items']) == 2
    assert response.json['items'][1]['id'] == obj['id']
    assert response.json['items'][1]['description'] == obj['description']
    assert response.json['items'][1]['price'] == obj['price']


def test_post_invalid_id(test_client):
    obj = {
        'description': 'Item teste',
        'price': 10.0
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um id válido'


def test_post_invalid_description(test_client):
    obj = {
        'id': 2,
        'price': 10.0
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida'


def test_post_invalid_price(test_client):
    obj = {
        'id': 2,
        'description': 'Item teste'
    }

    response = test_client.post(
        '/purchase_order_items/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço válido'
