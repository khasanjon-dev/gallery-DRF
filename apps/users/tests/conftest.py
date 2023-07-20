import pytest
from django.core.cache import cache
from django.core.management import call_command
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

base_url = 'users'


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture(scope="function")
def load_user():
    call_command('loaddata', 'user.yaml')


@pytest.fixture(scope="function")
def phone_fixture():
    return '998902002020'


@pytest.fixture(scope="function")
def phone_fixture_new():
    return '998903003030'


@pytest.fixture(scope="function")
def send_code(api_client, phone_fixture):
    url = reverse_lazy(f'{base_url}-send-code')

    payload = {
        "phone": phone_fixture
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200


@pytest.fixture(scope="function")
def check_code(api_client, phone_fixture, send_code):
    url = reverse_lazy(f'{base_url}-check-code')
    payload = {
        "phone": phone_fixture,
        "code": cache.get(phone_fixture)
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200


@pytest.fixture(scope="function")
def register(api_client, phone_fixture, send_code, check_code):
    url = reverse_lazy(f'{base_url}-register')
    payload = {
        "first_name": "first_name",
        "phone": phone_fixture,
        "password": "password"
    }
    response = api_client.post(url, payload)
    assert response.status_code == 201
    return response.data


@pytest.fixture(scope="function")
def login(api_client, register, phone_fixture):
    url = reverse_lazy('login')
    password = register['password']
    payload = {
        "phone": phone_fixture,
        "password": password
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200
    assert response.data['access']
    assert response.data['refresh']
    return response.data


@pytest.fixture(scope="function")
def reset_password_send_code(api_client, register, phone_fixture):
    url = reverse_lazy(f'{base_url}-reset-password-send-code')
    payload = {
        'phone': phone_fixture
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200


@pytest.fixture(scope="function")
def change_phone(api_client, phone_fixture_new, register):
    url = reverse_lazy(f'{base_url}-change-phone')
    payload = {
        'phone': phone_fixture_new
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200
