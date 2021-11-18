from devpro.encurtador.models import UrlRedirect, UrlLog


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
