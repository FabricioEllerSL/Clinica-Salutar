from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def first_page(request):
    data_atual = datetime.now().strftime('%d/%m/%Y')
    return render(request, 'home/inicio.html', {'data_atual': data_atual})


def login_page(request):
    data_atual = datetime.now().strftime('%d/%m/%Y')
    return render(request, 'home/login.html', {'data_atual': data_atual})


def navigation_page(request):
    return render(request, 'home/navegacao.html')