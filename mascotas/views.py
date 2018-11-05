
from django.shortcuts import render
from django.http import HttpRequest

def mascota(request):
    return render(request, 'mascotas/signup.html', {})
    # return render(request, 'index.html', {} )