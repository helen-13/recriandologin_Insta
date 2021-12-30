from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    local_evento = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

class Meta:
    db_table = 'evento'

def _str_(self):
    return self.titulo
def get_data_evento(self):
    return self.data_evento.strtime('%d/%m/%y%H Hrs:%M min')

def get_data_input_evento(self):
    return self.data_evento.strtime('%Y-%m-%dT-%H:%M')