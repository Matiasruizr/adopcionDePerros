from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):

       class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )
        labels = {
            'username':'Nombre de usuario',
            'email': 'Correo',
            'first_name':'Nombre',
            'last_name':'Apellidos',
        }