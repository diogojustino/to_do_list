from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu login aqui'
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu nome aqui',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu sobrenome aqui',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Digite sua senha aqui',
                    'type': 'password'
                }
            ),

        }

        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )

        labels = {
            'username': 'Login',
            'first_name': 'Nome',
            'password': 'Senha',
            'last_name': 'Sobrenome',
        }
