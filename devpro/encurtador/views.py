from django.http.response import HttpResponse
from django.shortcuts import redirect

# Create your views here.

links = {'google': 'https://www.google.com'}


def home(resquest):
    return HttpResponse('Olá, eu sou o encurador')


def redirecionar(resquet, slug):
    path = links.get(slug, False)
    # se nao achar o slug redireciona para a home
    if not path:
        return redirect('/')
    # se achar vai para o link desejado
    else:
        return redirect(path)
