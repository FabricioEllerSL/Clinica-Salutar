from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first_page(request):
    return render(request, 'home/inicio.html')


def login_page(request):
    return render(request, 'home/login.html')