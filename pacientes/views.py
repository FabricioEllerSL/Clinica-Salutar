from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pacientes.models import Paciente
from .forms import PacienteForm


# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def display(request):

    """ Essa view exibe os pacientes cadastrados """
    
    pacientes = Paciente.objects.all()

    context_ = {
        'data_atual': data_atual,
        'pacientes': pacientes,
    }


    return render(request, 'pacientes/display.html', context_)


def search(request):

    """ Essa view exibe o resultado da pesquisa pelo paciente """

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



def infos(request, cpf):

    """ Essa view exibe as informações do paciente como nome, idade e endereço """

    paciente = Paciente.objects.get(pk=cpf)

    # metodo para calcular idade do paciente

    def calcular_idade(data_nascimento):
        data_atual = datetime.now()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        dia_atual = data_atual.day

        ano_nascimento = data_nascimento.year
        mes_nascimento = data_nascimento.month
        dia_nascimento = data_nascimento.day

        idade = ano_atual - ano_nascimento

        # Verifica se ainda não fez aniversário no ano atual
        if (mes_atual, dia_atual) < (mes_nascimento, dia_nascimento):
            idade -= 1

        return idade


    idade_paciente = calcular_idade(paciente.data_nascimento)

    endereco_paciente = paciente.rua + ', No.' + paciente.numero + ' - ' + paciente.bairro

    context_ = {
        'data_atual': data_atual,
        'paciente': paciente,
        'idade_paciente': idade_paciente,
        'endereco_paciente':endereco_paciente,
    }

    return render(request, 'pacientes/infos.html', context_)

def cadastrar_paciente(request):

    """ Essa view exibe o formulario de cadastro do paciente """

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes/display.html')  # redirecionar para página de sucesso após cadastro
    else:
        form = PacienteForm()
    return render(request, 'pacientes/cadastro.html', {'form': form})
