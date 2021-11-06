import pytest
from http import HTTPStatus

from django.test import Client

# from devpro.django_assertions import assert_contains

from devpro.encurtador.models import UrlRedirect


@pytest.fixture
def new_url(db):

    url_dct = {'destino': 'https://www.google.com',
               'slug': 'google'
               }

    url_model = UrlRedirect()
    url_model.destino = url_dct['destino']
    url_model.slug = url_dct['slug']
    url_model.save()
    return url_model


def test_status_code(client: Client):
    '''
    Testa se o caminho para o home foi encontrado
    '''
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_redirect_with_slug_found(client: Client, new_url):
    '''
    Testa se aplicao foi redirecionado
    '''
    url_model = new_url
    response = client.get('/' + url_model.slug)
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == url_model.destino


def test_slug_not_found(client: Client, new_url):
    '''
    Testa se a aplicação foir rederecionada para '/' quando
    são existe o slug
    '''
    response = client.get('/banana')
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == '/'


# def test_if_slug_is_corret_in_view(client: Client):
#     '''
#     Testa se slug esta no corpo da pagina
#     '''
#     response = client.get('/google')
#     assert_contains(response, 'google')
