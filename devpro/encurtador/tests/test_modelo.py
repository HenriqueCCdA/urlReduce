from typing import List, Tuple
from devpro.encurtador.models import UrlRedirect, UrlLog


def testa_a_relacao_entre_o_modelo_url_redirect_e_url_log(logs: Tuple[UrlLog], lista_urls: List[UrlRedirect]):
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


def testa_a_url_absoluta_para_url_reduzida(lista_urls: List[UrlRedirect]):
    '''
    ---------------------------------------------------------------------------------------
    Testa os url absoluta para o redirecionamento.
    ---------------------------------------------------------------------------------------
    '''

    for url in lista_urls:
        assert url.obtem_url_absoluta_para_url_reduzida() == '/' + url.slug


def testa_a_url_absoluta_para_o_relatorio(lista_urls: List[UrlRedirect]):
    '''
    ---------------------------------------------------------------------------------------
    Testa os url absoluta para o relatorios
    ---------------------------------------------------------------------------------------
    '''

    for url in lista_urls:
        assert url.obtem_url_absoluta_para_o_relatorio() == '/relatorio/' + url.slug


def testa_o_metodo_str_do_modelo_log(logs: Tuple[UrlLog], lista_urls: List[UrlRedirect]):
    '''
    ---------------------------------------------------------------------------------------
    Testa os url absoluta para o relatorios
    ---------------------------------------------------------------------------------------
    '''
    for i in range(len(lista_urls)):
        for log in logs[i]:
            assert str(log) == f'log for {lista_urls[i]}'


def testa_o_metodo_str_do_modelo_url(lista_urls: List[UrlRedirect]):
    '''
    ---------------------------------------------------------------------------------------
    Testa os url absoluta para o relatorios
    ---------------------------------------------------------------------------------------
    '''
    for url in lista_urls:
        assert str(url) == f'{url.slug} -> {url.destino}'
