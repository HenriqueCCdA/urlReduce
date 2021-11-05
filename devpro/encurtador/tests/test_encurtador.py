from http import HTTPStatus

from django.test import Client

# from devpro.django_assertions import assert_contains


def test_status_code(client: Client):
    '''
    Testa se o caminho para o home foi encontrado
    '''
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_status_code_with_slug(client: Client):
    '''
    Testa se aplicao foi redirecionado
    '''
    response = client.get('/google')
    assert response.status_code == HTTPStatus.FOUND  # 302


def test_slug_not_found(client: Client):
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
