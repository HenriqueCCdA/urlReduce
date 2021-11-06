from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


from devpro.encurtador.models import UrlRedirect

# Create your views here.

# links = {'google': 'https://www.google.com'}


def home(resquest):
    return HttpResponse('Olá, eu sou o encurador')


def redirecionar(resquet, slug: str):

    try:
        obj = UrlRedirect.objects.get(slug=slug)
    # se nao achar o slug redireciona para a home
    except ObjectDoesNotExist:
        return redirect('/')
    else:
        path = obj.destino
        return redirect(path)
