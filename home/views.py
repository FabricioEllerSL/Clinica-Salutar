from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first_page(request):
    return HttpResponse('Tela Inicial')


def login_page(request):
    return HttpResponse('Tela de Login')