from django.shortcuts import render

# Create your views here.

def display_medicos(request):
    return render(request, 'medicos/display.html')