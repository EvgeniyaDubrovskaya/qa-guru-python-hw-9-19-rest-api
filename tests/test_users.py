import json
import requests
from jsonschema import validate
from utils.schemas import path

base_url = 'https://reqres.in/api/users'


def test_create_user_success():
    response = requests.post(base_url, data={'name': 'jane', 'job': 'qa'})
    body = response.json()

    assert response.status_code == 201
    with open(path('users_post.json')) as file:
        validate(body, schema=json.loads(file.read()))


def test_update_user_success():
    user_name = 'joe'
    user_job = 'dm'
    response = requests.put(f'{base_url}/2', data={'name': user_name, 'job': user_job})
    body = response.json()

    assert response.status_code == 200
    with open(path('users_put.json')) as file:
        validate(body, schema=json.loads(file.read()))

    assert str(body['name']) == user_name
    assert str(body['job']) == user_job


def test_get_user_success():
    response = requests.get(f'{base_url}/2')
    body = response.json()

    assert response.status_code == 200
    with open(path('users_get_one.json')) as file:
        validate(body, schema=json.loads(file.read()))

    assert str(body['data']['first_name']) == 'Janet'


def test_get_user_fail_user_not_present():
    response = requests.get(f'{base_url}/99999')
    body = response.json()

    assert response.status_code == 404
    assert len(body) == 0


def test_delete_user_success():
    response = requests.delete(f'{base_url}/2')
    body = response.text

    assert response.status_code == 204
    assert response.text == ''
