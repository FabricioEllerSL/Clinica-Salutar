from datetime import datetime
from django.shortcuts import render
from pacientes.models import Paciente

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def display(request):
    
    pacientes = Paciente.objects.all()

    print(pacientes, 'aqui')

    context_ = {
        'data_atual': data_atual,
        'pacientes': pacientes,
    }


    return render(request, 'pacientes/display.html', context_)