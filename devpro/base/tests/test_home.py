from django.test import Client
from http import HTTPStatus


def test_status_code(client: Client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
