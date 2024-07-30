from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from medicos.models import Medico

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display_medicos(request):

    """ Essa view exibe os pacientes cadastrados """
    
    medicos = Medico.objects.all()

    context_ = {
        'data_atual': data_atual,
        'medicos': medicos,
    }


    return render(request, 'medicos/display.html', context_)