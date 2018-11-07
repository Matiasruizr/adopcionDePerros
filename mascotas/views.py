
from django.shortcuts import render
# from django.http import HttpRequest
# from . import models
# from datetime import datetime
from .models import Perros
from .forms import PerrosForm

Perros = Perros.objects.all()


def mascotas(request):
    return render(request, 'mascotas/mascotas.html', {'Perros': Perros})
    
def new(request):
    form = PerrosForm()
    if request.user.is_superuser:
        return render(request, 'mascotas/new.html', {'form': form})
    else:
        return render(request, 'mascotas/errorpermisos.html', {})
  