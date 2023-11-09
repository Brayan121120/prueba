from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from gil import views
from gil.views import mi_vista


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls"),name="login"),
    path('registro/', views.registro, name='registro'),
    path('', views.registro, name='HOME'),
    path("base", TemplateView.as_view(template_name="index.html"), name="base"),# new
    path('tablas/', views.tablas, name='tablas'),
    
]
