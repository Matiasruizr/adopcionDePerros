
from django import forms
from .models import Perros

class PerrosForm(forms.ModelForm):

    class Meta:
        model = Perros
        fields = ('nombre_mascota','raza_predominante','descripcion','foto_mascota','estado' )