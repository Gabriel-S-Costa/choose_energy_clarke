from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

client = TestClient(app)
client.headers.update({'X-Request-Token': settings.ACCESS_TOKEN})


def test_list_all_suppliers():
    response = client.get('/suppliers')

    assert response.is_success

    response_data = response.json()
    assert response_data
    assert set(response_data.keys()) == {'items', 'total', 'page', 'size', 'pages'}

    items = response_data.get('items')
    assert items is not None

    first_item = items[0]
    assert set(first_item.keys()) == {'code', 'name', 'type', 'total_clients', 'avg_rating', 'is_active', 'states'}
    assert first_item.get('name') == 'Amazonas Green Energy'
    assert first_item.get('type') == 'distributed_generation'
    assert first_item.get('avg_rating') == 0.0
    assert first_item.get('total_clients') == 0
    assert first_item.get('is_active') is True
    assert first_item.get('states') == ['AM', 'PA']


def test_list_suppliers_by_limit_and_page():
    response = client.get('/suppliers?page=1&size=1')

    assert response.is_success

    response_data = response.json()
    assert response_data
    assert set(response_data.keys()) == {'items', 'total', 'page', 'size', 'pages'}

    items = response_data.get('items')
    assert items is not None
    assert len(items) == 1


def test_list_suppliers_with_invalid_token():
    client.headers.update({'X-Request-Token': 'token'})
    response = client.get('/suppliers')

    assert response.is_error
    response_data = response.json()

    assert response_data == {'detail': 'Header X-Request-Token is invalid or missing'}


def test_search_suppliers():
    client.headers.update({'X-Request-Token': settings.ACCESS_TOKEN})
    response = client.get('/suppliers/search?uf=TO&consumption=1000')

    assert response.is_success

    response_data = response.json()
    assert response_data
    assert set(response_data.keys()) == {'state_base_cost', 'available_types', 'estimated_savings_per_type', 'suppliers'}

    state_base_cost = response_data.get('state_base_cost')
    assert state_base_cost is not None

    available_types = response_data.get('available_types')
    assert available_types is not None

    estimated_savings_per_type = response_data.get('estimated_savings_per_type')
    assert estimated_savings_per_type is not None

    suppliers = response_data.get('suppliers')
    assert suppliers is not None
