
from django.shortcuts import render






def inicio(request):
    return render(request,  'inicio.html', {})

def quienes(request):
    return render(request,  'quienes_somos.html', {})

def contacto(request):
    return render(request,  'contacto.html', {})
    