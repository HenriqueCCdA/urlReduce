import pytest
from http import HTTPStatus
# from model_bakery import baker

from django.test import Client

from devpro.django_assertions import assert_contains

from devpro.encurtador.models import UrlRedirect


@pytest.fixture
def url_encurtada(db):

    url_model = UrlRedirect()
    url_model.destino = 'https://www.google.com'
    url_model.slug = 'google'
    url_model.save()
    return url_model


def testa_codigo_de_estato(client: Client):
    '''
    Testa se o caminho para o home foi encontrado
    '''
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def testa_redirecionamento_com_slug_existente(client: Client, url_encurtada):
    '''
    Testa se aplicao foi redireciona para o site desejado
    '''
    response = client.get('/reduzido/' + url_encurtada.slug)
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == url_encurtada.destino


def testa_redirecionamento_com_slug_nao_existente(client: Client, db):
    '''
    Testa se a aplicação foi rederecionada para '/' quando
    são existe o slug
    '''
    response = client.get('/reduzido/banana')
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == '/'


def testa_codigo_de_estato_da_pagina_de_relatorio(client: Client, url_encurtada):
    '''
    Testa o estado da pagina de relatorio
    '''
    response = client.get('/relatorios/google')
    assert response.status_code == HTTPStatus.OK  # 200


def testa_se_foi_carregado_o_template_correto(client: Client, url_encurtada):
    '''
    Testa se o template correto foi carregado atraves da busta de Original no html
    '''
    response = client.get(f'/relatorios/{url_encurtada.slug}')

    assert_contains(response, 'Original')


def testa_se_url_do_destino(client: Client, url_encurtada):
    '''
    Testa se url do destino apareceu corretament
    '''
    response = client.get(f'/relatorios/{url_encurtada.slug}')

    assert_contains(response, f'<a href="{url_encurtada.destino}"')
