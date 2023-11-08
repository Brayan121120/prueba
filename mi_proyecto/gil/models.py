from django.contrib.auth.models import AbstractUser
from django.db import models

  #campos personales
    
class UsuarioPersonalizado(AbstractUser):
    fields = ('username', 'email', 'first_name','last_name', 'password1', 'password2')

    def __str__(self):
        return self.username