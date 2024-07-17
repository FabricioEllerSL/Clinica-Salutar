from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from pacientes.models import Paciente
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display(request):

    """ Essa view exibe os pacientes cadastrados """
    
    pacientes = Paciente.objects.all()

    context_ = {
        'data_atual': data_atual,
        'pacientes': pacientes,
    }


    return render(request, 'pacientes/display.html', context_)

@login_required(login_url='home:login')
def search(request):

    """ Essa view exibe o resultado da pesquisa pelo paciente """

    search_value = request.GET.get('q', '').strip()
    pacientes = Paciente.objects.filter(nome__icontains=search_value).order_by('nome')

    if not pacientes:
        messages.error(request, 'Paciente não encontrado!')
        return redirect('pacientes:display_pacientes')
    
    context = {
        'pacientes': pacientes,
        'page_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    return render(request, 'pacientes/display.html', context)


@login_required(login_url='home:login')
def infos(request, id):

    """ Essa view exibe as informações do paciente como nome, idade e endereço """

    paciente = Paciente.objects.get(pk=id)

    context_ = {
        'data_atual': data_atual,
        'paciente': paciente,
    }

    return render(request, 'pacientes/infos.html', context_)

@login_required(login_url='home:login')
def cadastrar_paciente(request):

    """ Essa view exibe o formulario de cadastro do paciente """

    form = PacienteForm()

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('pacientes:display_pacientes')
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('pacientes:display_pacientes')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'cadastrar',
    }
    return render(request, 'pacientes/cadastro.html', context_)

@login_required(login_url='home:login')
def editar_paciente(request, id):

    """ Essa view exibe o formulario de edicao do paciente """

    paciente = get_object_or_404(Paciente, id=id)

    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes:display_pacientes')  # redirecionar para página de sucesso após edicao
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('pacientes:display_pacientes')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'editar',
    }
    return render(request, 'pacientes/cadastro.html', context_)

@login_required(login_url='home:login')
def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('pacientes:display_pacientes')
