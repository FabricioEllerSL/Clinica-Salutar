from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def first_page(request):
    
    context_ = {
        'data_atual': data_atual,
    }

    return render(request, 'home/inicio.html', context_)


def login_page(request):
    data_atual = datetime.now().strftime('%d/%m/%Y')

    context_ = {
        'data_atual': data_atual,
        'page_title': 'Login -'
    }

    return render(request, 'home/login.html', context_)


def navigation_page(request):
    data_atual = datetime.now().strftime('%d/%m/%Y')

    context_ = {
        'data_atual': data_atual,
        'page_title': 'Navegação -'
    }

    return render(request, 'home/navegacao.html', context_)