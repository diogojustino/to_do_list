from datetime import date

from django.urls import path
from django.utils import timezone

from my_app import views

app_name = 'my_app'

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),

]