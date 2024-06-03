from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_hora_inicio = models.DateTimeField()
    data_hora_termino = models.DateTimeField()
    local = models.CharField(max_length=200)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo