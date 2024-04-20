from datetime import datetime
from django.shortcuts import redirect, render
from pacientes.models import Paciente

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def display(request):
    
    pacientes = Paciente.objects.all()

    context_ = {
        'data_atual': data_atual,
        'pacientes': pacientes,
    }


    return render(request, 'pacientes/display.html', context_)


def search(request):

    search_value = request.GET.get('q', '').strip()
    print(search_value)

    if search_value == '':
        return redirect('pacientes:display_pacientes')
    

    pacientes = Paciente.objects.filter(nome__icontains=search_value).order_by('nome')


    context = {
        'pacientes': pacientes,
        'page_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    return render(request, 'pacientes/display.html', context)