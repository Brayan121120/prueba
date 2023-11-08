from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

# Registra el modelo de usuario personalizado
admin.site.register(UsuarioPersonalizado, UserAdmin)
