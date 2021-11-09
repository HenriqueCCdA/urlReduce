import pytest
from http import HTTPStatus
from model_bakery import baker

from django.test import Client
from devpro.django_assertions import assert_contains
from devpro.encurtador.models import UrlRedirect, UrlLog

from devpro.encurtador.facade import separa_e_conta_os_redirecionamentos_por_data


@pytest.fixture
def url_encurtada(db):
    return baker.make(UrlRedirect)


@pytest.fixture
def lista_urls(db):
    return baker.make(UrlRedirect, 2)


@pytest.fixture
def logs(lista_urls):
    log_url1 = baker.make(UrlLog, 3, url_redirect=lista_urls[0])
    log_url2 = baker.make(UrlLog, 8, url_redirect=lista_urls[1])
    return log_url1, log_url2


def testa_a_relacao_entre_o_modelo_url_redirect_e_url_log(logs, lista_urls):
    '''
    ---------------------------------------------------------------------------------------
    Testa os modelos UrlRedirect e UrlLog com o ORM.
    ---------------------------------------------------------------------------------------
    '''

    # numero total de url cadastradas
    assert len(UrlRedirect.objects.all()) == 2

    # numero total de logs
    assert len(UrlLog.objects.all()) == len(logs[0]) + len(logs[1])

    # numero toral de logs da url1 acessado utilizando a chave estrangeira
    assert len(lista_urls[0].logs.all()) == len(logs[0])

    # numero toral de logs da url2 acessado utilizando a chave estrangeira
    assert len(lista_urls[1].logs.all()) == len(logs[1])


def testa_a_facada_separa_e_conta_os_redirecionamentos_por_data(logs, lista_urls):
    '''
    ---------------------------------------------------------------------------------------
    Testa a fachada que calcula o numero de cliques em uma url por dia
    ---------------------------------------------------------------------------------------
    '''
    for url, log in zip(lista_urls, logs):
        redirecionamentos_por_data = separa_e_conta_os_redirecionamentos_por_data(url.slug)
        for r in redirecionamentos_por_data:
            assert r.cliques == len(log)


def testa_codigo_de_estato(client: Client):
    '''
    ---------------------------------------------------------------------------------------
    Testa se o caminho para o home foi encontrado
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def testa_redirecionamento_com_slug_existente(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se aplicao foi redireciona para o site desejado
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/reduzido/' + url_encurtada.slug)
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == url_encurtada.destino


def testa_redirecionamento_com_slug_nao_existente(client: Client, db):
    '''
    ---------------------------------------------------------------------------------------
    Testa se a aplicação foi rederecionada para '/' quando
    são existe o slug
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/reduzido/banana')
    assert response.status_code == HTTPStatus.FOUND  # 302
    assert response.headers['Location'] == '/'


def testa_codigo_de_estato_da_pagina_de_relatorio(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa o estado da pagina de relatorio
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorios/{url_encurtada.slug}')
    assert response.status_code == HTTPStatus.OK  # 200


def testa_se_foi_carregado_o_template_correto(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se o template correto foi carregado atraves da busta de Original no html
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorios/{url_encurtada.slug}')

    assert_contains(response, 'Original')


def testa_se_url_do_destino(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se url do destino apareceu corretament
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorios/{url_encurtada.slug}')

    assert_contains(response, f'<a href="{url_encurtada.destino}"')
