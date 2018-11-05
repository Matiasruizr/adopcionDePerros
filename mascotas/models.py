# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.


class Perros(models.Model):
    nombre_mascota = models.CharField(max_length=200)
    raza_predominante = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000)
    foto_mascota = models.ImageField(upload_to='static/img/perros_subidos')
    estado = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
    )
    estado = models.CharField(max_length=10, choices=estado)
