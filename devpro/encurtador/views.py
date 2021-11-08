from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist


from devpro.encurtador.models import UrlRedirect

# Create your views here.

# links = {'google': 'https://www.google.com'}


def home(request):
    return HttpResponse('Olá, eu sou o encurador')


def relatorios(request, slug: str):
    reduce = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/reduzido/{reduce.slug}')
    contexto = {'reduce':  reduce,
                'url_reduzida': url_reduzida}

    return render(request, 'encutador/relatorio.html', context=contexto)


def redirecionar(request, slug: str):

    try:
        obj = UrlRedirect.objects.get(slug=slug)
    # se nao achar o slug redireciona para a home
    except ObjectDoesNotExist:
        return redirect('/')
    else:
        path = obj.destino
        return redirect(path)
