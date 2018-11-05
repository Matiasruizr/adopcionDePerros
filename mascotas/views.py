
from django.shortcuts import render
from django.http import HttpRequest
# from . import models
from datetime import datetime
from .models import Perros

Perros = Perros.objects.all()


def mascotas(request):
    return render(request, 'mascotas/mascotas.html', {'Perros': Perros})