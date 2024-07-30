from produtos.forms import ProdutoForm
from produtos.models import Produto
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display_produtos(request):

    """ Essa view exibe os produtos cadastrados """
    
    produtos = Produto.objects.all()

    context_ = {
        'data_atual': data_atual,
        'produtos': produtos,
    }


    return render(request, 'produtos/display.html', context_)

def cadastrar_produto(request):

    """ Essa view exibe o formulario de cadastro do produto """

    form = ProdutoForm()

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('produtos:display_produtos')
        else:
            messages.error(request, 'As informações não foram cadastradas corretamente!')
            return redirect('produtos:display_produtos')
       

    context_ = {
        'data_atual': data_atual,
        'form': form,
        'page_title': 'Cadastro - ',
        'funcionalidade': 'cadastrar',
    }
    return render(request, 'produtos/cadastro.html', context_)