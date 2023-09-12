"""
URL configuration for sol1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""

from django.contrib import admin
from django.urls import include, path
from sol1.views import mi_vista
from sol1.views import mi_vistaroja

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_vista/', mi_vista),  
    path('mi_vista123/', mi_vistaroja), 
]