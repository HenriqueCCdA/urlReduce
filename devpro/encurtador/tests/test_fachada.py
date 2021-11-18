from devpro.encurtador.models import UrlRedirect
from devpro.encurtador.facade import separa_e_conta_os_redirecionamentos_por_data,\
                                 soma_de_cliques_pela_slug, soma_de_cliques, obtem_todas_as_urls


def testa_a_fachada_que_calcula_o_numero_total_de_cliques_pela_slug(logs, lista_urls):
    '''
    Testa a fachada que calcula o numero de cliques em uma url usando apenas o slug com busca
    '''
    for url, log in zip(lista_urls, logs):
        assert soma_de_cliques_pela_slug(url.slug) == len(log)


def testa_a_fachada_que_calcula_o_numero_total_de_cliques(logs, lista_urls):
    '''
    Testa a fachada que calcula o numero de cliques em uma url usando usando o
    redirecionamentos_por_data
    '''
    for url, log in zip(lista_urls, logs):
        redirecionamentos_por_data = separa_e_conta_os_redirecionamentos_por_data(url.slug)
        assert soma_de_cliques(redirecionamentos_por_data) == len(log)


def testa_a_fachada_que_listagem_de_todas_as_url_cadastrada(lista_urls):
    '''
    Testa a fachada que gera a lista com todas as urls cadastradas
    '''
    listas = obtem_todas_as_urls()

    # numero total de logs da url1 acessado utilizando a chave estrangeira
    assert len(listas) == len(UrlRedirect.objects.all())


def testa_a_fachada_que_separa_e_conta_os_redirecionamentos_por_data(logs, lista_urls):
    '''
    Testa a fachada que calcula o numero de cliques em uma url por dia
    '''
    for url, log in zip(lista_urls, logs):
        redirecionamentos_por_data = separa_e_conta_os_redirecionamentos_por_data(url.slug)
        for r in redirecionamentos_por_data:
            assert r.cliques == len(log)
