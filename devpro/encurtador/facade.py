from typing import List
from django.db.models.functions import TruncDate
from django.db.models import Count
from devpro.encurtador.models.url import UrlRedirect


def obtem_todas_as_urls() -> List[UrlRedirect]:
    '''
    ---------------------------------------------------------------------------------
    Fachada que retorna uma lista com todas as urls cadastradas
    ---------------------------------------------------------------------------------
    return: Uma lista com as urls
    ---------------------------------------------------------------------------------
    '''
    return list(UrlRedirect.objects.all())


def separa_e_conta_os_redirecionamentos_por_data(slug: str) -> List[UrlRedirect]:
    '''
    ---------------------------------------------------------------------------------
    Fachada que calcula o numero de cliques em uma url por dia
    ---------------------------------------------------------------------------------
    param: slug o slug desejado
    ---------------------------------------------------------------------------------
    return: Uma lista com os redirecionamento com os campos novos de data e cliques
    ---------------------------------------------------------------------------------
    '''
    q = UrlRedirect.objects.filter(
                                   slug=slug
    ).annotate(
        data=TruncDate('logs__criado_em')
    ).annotate(
        cliques=Count('data')
    ).order_by('data')

    return list(q)


def soma_de_cliques(redirecionamentos_por_data: List[UrlRedirect]) -> float:
    '''
    ---------------------------------------------------------------------------------
    Fachada que calcula o numero total de cliques em uma url
    ---------------------------------------------------------------------------------
    param: redirecionamentos_por_data
    ---------------------------------------------------------------------------------
    return: Numero total de cliques
    ---------------------------------------------------------------------------------
    OBS: redirecionamentos_por_data tem que ter os campos data e cliques
    ---------------------------------------------------------------------------------
    '''
    return sum(c.cliques for c in redirecionamentos_por_data)


def soma_de_cliques_pela_slug(slug: str) -> float:
    '''
    ---------------------------------------------------------------------------------
    Fachada que calcula o numero total de cliques em uma url
    ---------------------------------------------------------------------------------
    param: redirecionamentos_por_data
    ---------------------------------------------------------------------------------
    return: Numero total de cliques
    ---------------------------------------------------------------------------------
    OBS: redirecionamentos_por_data tem que ter os campos data e cliques
    ---------------------------------------------------------------------------------
    '''

    return len(list(UrlRedirect.objects.get(slug=slug).logs.all()))
