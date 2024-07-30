from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from medicos.models import Medico
from django.contrib import messages

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display_medicos(request):

    """ Essa view exibe os medicos cadastrados """
    
    medicos = Medico.objects.all()

    context_ = {
        'data_atual': data_atual,
        'medicos': medicos,
    }


    return render(request, 'medicos/display.html', context_)

@login_required(login_url='home:login')
def search(request):

    """ Essa view exibe o resultado da pesquisa pelo medico """

    search_value = request.GET.get('q', '').strip()
    medicos = Medico.objects.filter(nome__icontains=search_value).order_by('nome')

    if not medicos:
        messages.error(request, 'Médico não encontrado!')
        return redirect('medicos:display_medicos')
    
    context = {
        'medicos': medicos,
        'page_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    return render(request, 'medicos/display.html', context)

@login_required(login_url='home:login')
def infos(request, id):

    """ Essa view exibe as informações do medico  """

    medico = Medico.objects.get(pk=id)

    context_ = {
        'data_atual': data_atual,
        'medico': medico,
    }

    return render(request, 'medicos/infos.html', context_)