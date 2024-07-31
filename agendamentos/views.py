from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from pacientes.models import Paciente
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from agendamentos.forms import AgendamentoForm
from agendamentos.models import Agendamento
from datetime import datetime

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def display(request):

    """ Essa view exibe os agendamentos cadastrados """
    
    agendamentos = Agendamento.objects.all() 

    context_ = {
        'data_atual': data_atual,
        'agendamentos': agendamentos,
    }


    return render(request, 'agendamentos/display.html', context_)

@login_required(login_url='home:login')
def search(request):

    """ Essa view exibe o resultado da pesquisa pelo agendamento """

    search_value = request.GET.get('q', '').strip()
    agendamentos = Agendamento.objects.filter(nome_paciente__nome__icontains=search_value).order_by('nome_paciente')

    if not agendamentos:
        messages.error(request, 'Agendamento não encontrado!')
        return redirect('agendamentos:display_agendamentos')
    
    context = {
        'agendamentos': agendamentos,
        'page_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    return render(request, 'agendamentos/display.html', context)


@login_required(login_url='home:login')
def cadastrar_agendamento(request):

    """ Essa view exibe o formulario de cadastro do agendamento """

    form = AgendamentoForm()

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('agendamentos:display_agendamentos')
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('agendamentos:display_agendamentos')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'cadastrar',
    }
    return render(request, 'agendamentos/cadastro.html', context_)

@login_required(login_url='home:login')
def editar_agendamento(request, id):

    """ Essa view exibe o formulario de edicao do agendamento """

    agendamento = get_object_or_404(Agendamento, id=id)

    form = AgendamentoForm(instance=agendamento, initial={'nome_paciente' : agendamento.nome_paciente, 'nome_medico': agendamento.nome_medico})

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamentos:display_agendamentos')  # redirecionar para página de sucesso após edicao
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('agendamentos:display_agendamentos')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'editar',
    }
    return render(request, 'agendamentos/cadastro.html', context_)

@login_required(login_url='home:login')
def infos(request, id):

    """ Essa view exibe as informações do agendamento """

    agendamento = Agendamento.objects.get(pk=id)

    context_ = {
        'data_atual': data_atual,
        'agendamento': agendamento,
    }

    return render(request, 'agendamentos/infos.html', context_)

@login_required(login_url='home:login')
def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect('agendamentos:display_agendamentos')