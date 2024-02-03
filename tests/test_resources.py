import json
import requests
from jsonschema import validate
from utils.schemas import path

base_url = 'https://reqres.in/api/unknown'


def test_get_resources_by_page():
    response = requests.get(base_url, params={'page': 2, 'per_page': 5})
    body = response.json()

    assert response.status_code == 200
    with open(path('resources.json')) as file:
        validate(body, schema=json.loads(file.read()))

    assert body['total'] == 12
    assert body['total_pages'] == 3


def test_get_resources_by_page_empty_page():
    response = requests.get(base_url, params={'page': 100, 'per_page': 5})
    body = response.json()

    assert response.status_code == 200
    assert len(body['data']) == 0
