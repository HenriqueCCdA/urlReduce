from typing import List
from django.db.models.functions import TruncDate
from django.db.models import Count
from devpro.encurtador.models import UrlRedirect


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
