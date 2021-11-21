from json import dumps

from django.core.paginator import Paginator
from django.shortcuts import redirect, render, reverse
from django.core.exceptions import ObjectDoesNotExist

from devpro.encurtador.models import UrlLog, UrlRedirect
from devpro.encurtador.facade import separa_e_conta_os_redirecionamentos_por_data, soma_de_cliques,\
                                     obtem_todas_as_urls


def home(request):
    urls = obtem_todas_as_urls()
    paginator = Paginator(urls, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'encurtador/home.html', context={'page_obj': page_obj})


def relatorio(request, slug: str):
    reduce = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/{reduce.slug}')

    redirecionamentos_por_data = separa_e_conta_os_redirecionamentos_por_data(slug)

    datas, cliques = [], []
    for r in redirecionamentos_por_data:
        datas.append(str(r.data))
        cliques.append(r.cliques)

    contexto = {'reduce':  reduce,
                'url_reduzida': url_reduzida,
                'redirecionamentos_por_data': redirecionamentos_por_data,
                'total_cliques': soma_de_cliques(redirecionamentos_por_data),
                'dias_grafico': dumps(datas),
                'cliques_grafico': dumps(cliques)
                }

    return render(request, 'encurtador/relatorio.html', context=contexto)


def redirecionar(request, slug: str):

    try:
        url = UrlRedirect.objects.get(slug=slug)
    # se nao achar o slug redireciona para a home
    except ObjectDoesNotExist:
        return redirect(reverse('home'))
    else:
        path = url.destino

        UrlLog.objects.create(
            origem=request.META.get('HTTP_REFERER'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            host=request.META.get('HTTP_HOST'),
            ip=request.META.get('REMOTE_ADDR'),
            url_redirect=url,
        )
        return redirect(path)
