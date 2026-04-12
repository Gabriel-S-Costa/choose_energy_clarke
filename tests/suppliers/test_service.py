from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

client = TestClient(app)
client.headers.update({'X-Request-Token': settings.ACCESS_TOKEN})


def test_search_all_suppliers():
    response = client.get('/suppliers')

    assert response.is_success

    response_data = response.json()
    assert response_data
    assert set(response_data.keys()) == {'items', 'total', 'page', 'size', 'pages'}

    items = response_data.get('items')
    assert items is not None

    first_item = items[0]
    assert set(first_item.keys()) == {'code', 'name', 'type', 'total_clients', 'avg_rating', 'is_active', 'states'}
    assert first_item == {
        'code': '6599fc07-eac6-45fa-9981-99df98a747c6',
        'name': 'Amazonas Green Energy',
        'type': 'distributed_generation',
        'avg_rating': 0.0,
        'total_clients': 0,
        'is_active': True,
        'states': ['AM', 'PA'],
    }


def test_list_suppliers_by_limit_and_page():
    response = client.get('/suppliers?page=1&size=2')

    assert response.is_success

    response_data = response.json()
    assert response_data
    assert set(response_data.keys()) == {'items', 'total', 'page', 'size', 'pages'}

    items = response_data.get('items')
    assert items is not None
    assert len(items) == 2


def test_list_suppliers_with_invalid_token():
    client.headers.update({'X-Request-Token': 'token'})
    response = client.get('/suppliers')

    assert response.is_error
    response_data = response.json()

    assert response_data == {'detail': 'Header X-Request-Token is invalid or missing'}
