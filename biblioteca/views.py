from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from biblioteca.models import Ies

# Create your views here.

def index(request):
    busca = Ies.objects.filter(id_ies='1')
    print busca
    return render_to_response('index.html', RequestContext(request))

def acessoacervo(request):
    return render_to_response('acessoacervo.html', RequestContext(request))

def teste(request):
    return render_to_response('teste.html', RequestContext(request))