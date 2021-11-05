from django.http.response import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(resquest):
    return HttpResponse('Olá, eu sou o encurador')


def redirecionar(resquet, slug):
    return HttpResponse(f'Olá, eu sou o encurador é minha slug é {slug}')
