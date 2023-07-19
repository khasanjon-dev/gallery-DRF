import pytest
from django.core.cache import cache
from rest_framework.reverse import reverse_lazy

base_url = 'users'


class TestUser:
    @pytest.mark.django_db
    def test_user_list(self, load_user, api_client):
        url = reverse_lazy(f'{base_url}-list')
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_send_code(self, api_client, phone_fixture):
        url = reverse_lazy(f'{base_url}-send-code')

        payload = {
            "phone": phone_fixture
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_check_code(self, api_client, phone_fixture, ):
        url = reverse_lazy(f'{base_url}-check-code')
        payload = {
            "phone": phone_fixture,
            "code": cache.get(phone)
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200
