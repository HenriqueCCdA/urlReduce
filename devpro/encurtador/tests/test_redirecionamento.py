from http import HTTPStatus

from django.test import Client


def testa_redirecionamento_com_slug_existente(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se aplicao foi redireciona para o site desejado
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/' + url_encurtada.slug)
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == url_encurtada.destino


def testa_redirecionamento_com_slug_nao_existente(client: Client, db):
    '''
    ---------------------------------------------------------------------------------------
    Testa se a aplicação foi rederecionada para '/' quando
    são existe o slug
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/banana')
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == '/'
