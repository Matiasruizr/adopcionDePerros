
from django.shortcuts import render
from .forms import UserForm


def inicio(request):
    return render(request,  'inicio.html', {})

def quienes(request):
    return render(request,  'quienes_somos.html', {})

def contacto(request):
    return render(request,  'contacto.html', {})

def login(request):
    return render(request,  'login.html', {})

def registro_usuario(request):
    form = UserForm()
    return render(request,  'registro.html', {'form': form})