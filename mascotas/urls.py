from django.urls import path
from mascotas import views as mascota_views
from .forms import PerrosForm

urlpatterns = [
    path('',mascota_views.mascotas, name="mascotas"),
    path('new',mascota_views.new, name="registro_mascota"),
]
