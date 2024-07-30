from produtos.models import Produto
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

@login_required(login_url='home:login')
def display_produtos(request):

    """ Essa view exibe os pacientes cadastrados """
    
    produtos = Produto.objects.all()

    context_ = {
        'data_atual': data_atual,
        'produtos': produtos,
    }


    return render(request, 'produtos/display.html', context_)