from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from gil.views import prede
from gil import views


urlpatterns = [
    path("Inicio", prede, name="default"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls"),name="login"),
    path('registro/', views.registro, name='registro'),
    path("base", TemplateView.as_view(template_name="index.html"), name="base"),# new
    path('tablas/', views.tablas, name='tablas'),
    
]
