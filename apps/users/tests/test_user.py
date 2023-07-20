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
    def test_check_code(self, api_client, phone_fixture, send_code):
        url = reverse_lazy(f'{base_url}-check-code')
        payload = {
            "phone": phone_fixture,
            "code": cache.get(phone_fixture)
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_register(self, api_client, phone_fixture, send_code, check_code):
        url = reverse_lazy(f'{base_url}-register')
        payload = {
            "first_name": "first_name",
            "phone": phone_fixture,
            "password": "password"
        }
        response = api_client.post(url, payload)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_login(self, api_client, register, phone_fixture):
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

    @pytest.mark.django_db
    def test_refresh(self, api_client, register, phone_fixture, login):
        url = reverse_lazy('refresh')
        payload = {
            'refresh': login['refresh']
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200
        assert response.data['access']

    @pytest.mark.django_db
    def test_reset_password_send_code(self, api_client, register, phone_fixture):
        url = reverse_lazy(f'{base_url}-reset-password-send-code')
        payload = {
            'phone': phone_fixture
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_reset_password(self, api_client, register, reset_password_send_code, check_code, phone_fixture):
        url = reverse_lazy(f'{base_url}-reset-password')
        payload = {
            'phone': phone_fixture,
            'password': '12345'
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_change_phone(self, api_client, phone_fixture_new, register):
        url = reverse_lazy(f'{base_url}-change-phone')
        payload = {
            'phone': phone_fixture_new
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_change_phone_confirm(self, api_client, register, phone_fixture_new, change_phone):
        url = reverse_lazy(f'{base_url}-change-phone-confirm')
        payload = {
            'phone': phone_fixture_new,
            'code': cache.get(phone_fixture_new)
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200
