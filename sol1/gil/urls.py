from django.contrib import admin
from django.urls import include, path
from sol1.views import mi_vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_vista/', mi_vista),  # Reemplaza 'mi_app' con el nombre de tu aplicación
]