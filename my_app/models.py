from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    terminado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
