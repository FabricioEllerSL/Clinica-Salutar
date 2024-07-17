from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from funcionario.forms import FuncionarioForm
from funcionario.models import Funcionario
from django.contrib import messages

# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display_funcionarios(request):

    """ Essa view exibe os funcionários cadastrados """
    
    funcionarios = Funcionario.objects.all()

    context_ = {
        'data_atual': data_atual,
        'funcionarios': funcionarios,
    }


    return render(request, 'funcionario/display.html', context_)


@login_required(login_url='home:login')
def cadastrar_funcionario(request):

    """ Essa view exibe o formulario de cadastro do funcionario """

    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('funcionario:display_funcionarios')
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('funcionario:display_funcionarios')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'cadastrar',
    }
    return render(request, 'funcionario/cadastro.html', context_)

@login_required(login_url='home:login')
def pesquisar_funcionario(request):

    """ Essa view exibe o resultado da pesquisa pelo paciente """

    search_value = request.GET.get('q', '').strip()
    funcionarios = Funcionario.objects.filter(nome__icontains=search_value).order_by('nome')

    if not funcionarios:
        messages.error(request, 'Funcionário não foi encontrado!')
        return redirect('funcionario:display_funcionarios')
    
    context = {
        'funcionarios': funcionarios,
        'page_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    return render(request, 'funcionario/display.html', context)

@login_required(login_url='home:login')
def editar_funcionario(request, id):

    """ Essa view exibe o formulario de edicao do funcionario """

    funcionario = get_object_or_404(Funcionario, id=id)

    form = FuncionarioForm(instance=funcionario)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario:display_funcionarios')  # redirecionar para página de sucesso após edicao
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'editar',
    }
    return render(request, 'funcionario/cadastro.html', context_)

@login_required(login_url='home:login')
def infos_funcionario(request, id):

    """ Essa view exibe as informações do paciente como nome, idade e endereço """

    funcionario = Funcionario.objects.get(pk=id)

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


    idade_funcionario = calcular_idade(funcionario.data_nascimento)

    endereco_funcionario = ''

    if funcionario.rua and funcionario.numero and funcionario.bairro:
        endereco_funcionario = funcionario.rua + ', No.' + funcionario.numero + ' - ' + funcionario.bairro

    context_ = {
        'data_atual': data_atual,
        'funcionario': funcionario,
        'idade_funcionario': idade_funcionario,
        'endereco_funcionario': endereco_funcionario,
    }

    print(endereco_funcionario)

    return render(request, 'funcionario/infos.html', context_)


@login_required(login_url='home:login')
def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return redirect('funcionario:display_funcionarios')