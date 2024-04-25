from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from .forms import CadastrarUsuarioForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

data_atual = datetime.now().strftime('%d/%m/%Y')

def first_page(request):
    
    context_ = {
        'data_atual': data_atual,
    }

    return render(request, 'home/inicio.html', context_)

def login_view(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:navegacao')
        else:
            messages.error(request, 'Usuario ou senha invalidos')

    context_ = {
        'form': form,
        'data_atual': data_atual,
        'page_title': 'Login - '
    }

    return render(request, 'home/login.html', context_)


def logout_view(request):
    auth.logout(request)
    return redirect('home:login')  # Redireciona para a página de login após o logout


@login_required
def navigation_page(request):

    nome_do_usuario = request.user.username if request.user.is_authenticated else None

    context_ = {
        'data_atual': data_atual,
        'page_title': 'Navegação - ',
        'nome_do_usuario': nome_do_usuario
    }

    return render(request, 'home/navegacao.html', context_)

@login_required
def create_user(request):

    form = CadastrarUsuarioForm()

    if request.method == 'POST':
        form = CadastrarUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:login')  # redirecionar para página de sucesso após cadastro
        

    context_ = {
        'form': form,
        'data_atual': data_atual
    }

    return render(request, 'home/cadastro.html', context_)
