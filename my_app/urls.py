from datetime import date

from django.urls import path
from django.utils import timezone

from my_app import views

app_name = 'my_app'

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('cadastro_tarefa', views.cadastro_tarefa, name='cadastro_tarefa'),
    path('<int:id_tarefa>/excluir_tarefa/', views.excluir_tarefa, name='excluir_tarefa'),
    #ajax
    path('ajax_tabela_ativa/', views.ajax_tabela_ativa, name='ajax_tabela_ativa'),
    path('ajax_tabela_todos/', views.ajax_tabela_todos, name='ajax_tabela_todos'),
    path('ajax_tabela_concluida/', views.ajax_tabela_concluida, name='ajax_tabela_concluida'),
]