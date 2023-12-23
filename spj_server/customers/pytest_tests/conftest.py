import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

ENDPOINTS_NAME_LIST = (
        'customer',
        'customuser',
        'vacancy',
        'task',
)

@pytest.fixture
def spj_client(django_user_model):
    user = django_user_model.objects.create(
        username='SPJ_client_test',
        is_staff=True,
    )
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client

@pytest.fixture
def endpoints_name_list():
    return ENDPOINTS_NAME_LIST

@pytest.fixture
def test_user(django_user_model):
    return django_user_model.objects.create(
        username='TestUser'
    )

@pytest.fixture
def test_user_token(test_user):
    return Token.objects.create(user=test_user)

@pytest.fixture
def user_client(test_user, test_user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {test_user_token.key}')
    return client