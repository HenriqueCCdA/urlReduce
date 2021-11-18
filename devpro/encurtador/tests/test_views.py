from http import HTTPStatus

from django.test import Client
from devpro.django_assertions import assert_contains


def testa_codigo_de_estado_da_home(client: Client, db):
    '''
    ---------------------------------------------------------------------------------------
    Testa se o caminho para o home foi encontrado
    ---------------------------------------------------------------------------------------
    '''
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def testa_codigo_de_estado_da_pagina_de_relatorio(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa o estado da pagina de relatorio
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorio/{url_encurtada.slug}')
    assert response.status_code == HTTPStatus.OK  # 200


def testa_se_foi_carregado_o_template_correto_do_relatorio(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se o template correto foi carregado
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorio/{url_encurtada.slug}')
    assert_contains(response, '<h5>Original: <a href=')
    assert_contains(response, '<h3>Reduzido: <a href=')


def testa_se_url_do_destino_aparece_no_relatorio(client: Client, url_encurtada):
    '''
    ---------------------------------------------------------------------------------------
    Testa se url do destino apareceu corretamente
    ---------------------------------------------------------------------------------------
    '''
    response = client.get(f'/relatorio/{url_encurtada.slug}')
    assert_contains(response, f'<a href="{url_encurtada.destino}"')
