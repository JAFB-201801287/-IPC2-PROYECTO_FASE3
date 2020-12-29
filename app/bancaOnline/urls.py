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
    path('', views.index, name='home'),
    path('cliente/login/', views.login, name='cliente_login'),
    path('cliente/inicio/', views.inicio, name='cliente_inicio'),
    path('cliente/transaccion/deposito', views.deposito, name='cliente_deposito'),
    path('cliente/transaccion/activar', views.activar_cuenta, name='activar_cuenta'),
    path('cliente/transaccion/suspender', views.suspender_cuenta, name='suspender_cuenta'),
    path('cliente/transaccion/propia', views.transferencia_propias, name='trasnferencias_propias'),
    path('cliente/transaccion/terceros', views.transferencia_terceros, name='trasnferencias_terceros'),
    path('cliente/chequera/', views.cliente_chequera, name='cliente_chequera'),
    path('cliente/chequera1/', views.cliente_chequera1, name='cliente_chequera1'),
    path('cliente/chequera2/', views.cliente_chequera2, name='cliente_chequera2'),
    path('cliente/cheque/', views.cliente_cheque, name='cliente_cheque'),
]
