from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200, default='')
    fecha_hora = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='eventos', null=True, blank=True) 
    valor = models.PositiveIntegerField(default=0)
    plazas_disponibles = models.PositiveIntegerField(default=0)
    asistentes = models.ManyToManyField(User, related_name='eventos_inscritos', blank=True)

    def __str__(self):
        return self.titulo