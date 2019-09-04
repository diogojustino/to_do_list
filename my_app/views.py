from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse

from my_app.forms import UserForm


def __usuario_logado_(user):
    return user.__str__() != 'AnonymousUser'


def __autenticar_(request):
    login = request.POST.get('login')
    senha = request.POST.get('senha')

    return authenticate(username=login, password=senha)


def __is_post_(method):
    return method == 'POST'


def login(request):
    dados = {}

    if __usuario_logado_(request.user):
        return redirect('my_app:home')

    if __is_post_(request.method):
        usuario = __autenticar_(request)
        if usuario:
            django_login(request, usuario)
            return redirect('my_app:home')

        dados['mensagem'] = 'Login e senha invalido.'
    return render(request, 'my_app/auth/login.html', dados)


def cadastro(request):
    if __usuario_logado_(request.user):
        return redirect('my_app:home')

    dados = {}

    form = UserForm(request.POST)

    if __is_post_(request.method):
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('my_app:login')
    dados['form'] = form
    return render(request, 'my_app/auth/cadastro.html', dados)

def logout(request):
    django_logout(request)
    return redirect('my_app:login')

@login_required(login_url='my_app:login')
def home(request):
    return render(request, 'my_app/home/home.html')


def ajax_tabela_ativa(request):
    return render(request, 'my_app/home/ajax/ajax_tabela_ativas.html')


def ajax_tabela_todos(request):
    return render(request, 'my_app/home/ajax/ajax_tabela_todos.html')


def ajax_tabela_concluida(request):
    return render(request, 'my_app/home/ajax/ajax_tabela_concluidas.html')