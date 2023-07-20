import pytest
from django.core.cache import cache
from rest_framework.reverse import reverse_lazy

from users.models import User

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
    def test_login(self, register, api_client):
        url = reverse_lazy('login')
        payload = {
            'phone': register['phone'],
            'password': register['password']
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200
        access = response.data['access']
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        data = response.data
        return data

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
    def test_reset_password_send_code(self, api_client, login, phone_fixture):
        url = reverse_lazy(f'{base_url}-reset-password-send-code')
        payload = {
            'phone': phone_fixture
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_reset_password(self, api_client, login, reset_password_send_code, check_code, phone_fixture):
        url = reverse_lazy(f'{base_url}-reset-password')
        payload = {
            'phone': phone_fixture,
            'password': '12345'
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_change_phone(self, api_client, phone_fixture_new, login):
        url = reverse_lazy(f'{base_url}-change-phone')
        payload = {
            'phone': phone_fixture_new
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_change_phone_confirm(self, api_client, login, phone_fixture_new, change_phone):
        url = reverse_lazy(f'{base_url}-change-phone-confirm')
        payload = {
            'phone': phone_fixture_new,
            'code': cache.get(phone_fixture_new)
        }
        response = api_client.post(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_read_user(self, api_client, register):
        user = User.objects.filter(phone=register['phone']).first()
        url = reverse_lazy(f'{base_url}-detail', kwargs={'pk': user.id})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['id'] == user.id

    @pytest.mark.django_db
    def test_patch_user(self, api_client, register, login):
        user = User.objects.filter(phone=register['phone']).first()
        url = reverse_lazy(f'{base_url}-detail', kwargs={'pk': user.id})
        payload = {
            "first_name": "khasan",
            "last_name": "string",
            "phone": register['phone'],
        }
        response = api_client.patch(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_user(self, api_client, login, register):
        user = User.objects.filter(phone=register['phone']).first()
        url = reverse_lazy(f'{base_url}-detail', kwargs={'pk': user.id})
        response = api_client.delete(url)
        assert response.status_code == 204
