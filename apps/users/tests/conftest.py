import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


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
def send_code(api_client)