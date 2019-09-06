from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from my_app.forms import UserForm, TarefaForm
from my_app.models import Tarefa


# Create your views here.


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

    if __is_post_(request.method):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('my_app:login')
    else:
        form = UserForm()

    dados['form'] = form
    return render(request, 'my_app/auth/cadastro.html', dados)


@login_required(login_url='my_app:login')
def logout(request):
    django_logout(request)
    return redirect('my_app:login')


@login_required(login_url='my_app:login')
def home(request):
    return render(request, 'my_app/home/home.html')


@login_required(login_url='my_app:login')
def ajax_tabela_ativa(request):
    tarefas = Tarefa.objects.filter(user=request.user, terminado=False)

    dados = {
        'tarefas': tarefas
    }
    return render(request, 'my_app/home/ajax/ajax_tabela_ativas.html', dados)


@login_required(login_url='my_app:login')
def ajax_tabela_todos(request):
    tarefas = Tarefa.objects.filter(user=request.user)

    dados = {
        'tarefas': tarefas
    }
    return render(request, 'my_app/home/ajax/ajax_tabela_todos.html', dados)


@login_required(login_url='my_app:login')
def ajax_tabela_concluida(request):
    tarefas = Tarefa.objects.filter(user=request.user, terminado=True)

    dados = {
        'tarefas': tarefas
    }
    return render(request, 'my_app/home/ajax/ajax_tabela_concluidas.html', dados)


@login_required(login_url='my_app:login')
def cadastro_tarefa(request):
    dados = {}

    if __is_post_(request.method):
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('my_app:home')
    else:
        form = TarefaForm()
    dados['form'] = form

    return render(request, 'my_app/tarefa/cadastro_tarefa.html', dados)


def excluir_tarefa(request, id_tarefa):
    if __is_post_(request.method):
        tarefa = Tarefa.objects.get(id=id_tarefa)
        tarefa.delete()

    return redirect('my_app:home')
