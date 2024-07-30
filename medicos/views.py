from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from medicos.models import Medico
from django.contrib import messages
from .forms import MedicoForm

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

@login_required(login_url='home:login')
def cadastrar_medico(request):

    """ Essa view exibe o formulario de cadastro do medico """

    form = MedicoForm()

    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('medicos:display_medicos')
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('medicos:display_medicos')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'cadastrar',
    }
    return render(request, 'medicos/cadastro.html', context_)


@login_required(login_url='home:login')
def editar_medico(request, id):

    """ Essa view exibe o formulario de edicao do medico """

    medico = get_object_or_404(Medico, id=id)

    form = MedicoForm(instance=medico)

    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medicos:display_medicos')  # redirecionar para página de sucesso após edicao
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('medicos:display_medicos')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Editar - ',
        'funcionalidade': 'editar',
    }
    return render(request, 'medicos/cadastro.html', context_)


@login_required(login_url='home:login')
def deletar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('medicos:display_medicos')