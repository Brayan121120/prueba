# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Ingrese un correo válido.')
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        
