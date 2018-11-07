from django.urls import path
from mascotas import views as mascota_views
from .forms import PerrosForm

urlpatterns = [
    path('mascotas/',mascota_views.mascotas, name="mascotas"),
    path('mascotas/new',mascota_views.new),
]
