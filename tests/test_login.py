import json
import requests
from jsonschema import validate
from utils.schemas import path

base_url = 'https://reqres.in/api/login'


def test_login_success():
    response = requests.post(base_url, data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
    body = response.json()

    assert response.status_code == 200
    with open(path('login.json')) as file:
        validate(body, schema=json.loads(file.read()))

    assert len(body['token']) >= 0


def test_login_fail_no_password():
    response = requests.post(base_url, data={'email': 'eve.holt@reqres.in'})
    body = response.json()

    assert response.status_code == 400
    with open(path('login_error.json')) as file:
        validate(body, schema=json.loads(file.read()))
    assert body['error'] == 'Missing password'


def test_login_fail_no_email():
    response = requests.post(base_url, data={'password': 'cityslicka'})
    body = response.json()

    assert response.status_code == 400
    assert body['error'] == 'Missing email or username'

