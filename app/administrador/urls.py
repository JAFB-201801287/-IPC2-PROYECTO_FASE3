"""banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('administrador/login/', views.login, name='admistrador_login'),
    path('administrador/cliente/', views.lista_cliente, name='admistrador_cliente'),
    path('administrador/cliente/agregar/', views.agregar_cliente, name='admistrador_agregar_cliente'),
    path('administrador/empresa/', views.lista_empresa, name='admistrador_empresa'),
    path('administrador/empresa/agregar/', views.agregar_empresa, name='admistrador_agregar_empresa'),
    path('administrador/cuenta/', views.lista_cuenta, name='admistrador_cuenta'),
    path('administrador/cuenta/agregar/', views.agregar_cuenta, name='admistrador_agregar_cuenta'),
    path('administrador/cuenta/deposito/', views.deposito, name='admistrador_deposito_cuenta'),
    path('administrador/chequera/', views.agregar_chequera, name='admistrador_agregar_chequera'),
    path('administrador/usuario/activar', views.activar_usuario, name='admistrador_activar_usuario'),
    path('administrador/usuario/', views.lista_usuarios, name='admistrador_usuario'),
    path('administrador/cheque/', views.cobrar_cheque, name='admistrador_cobro_cheque'),
]
