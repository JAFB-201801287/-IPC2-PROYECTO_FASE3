from django import forms
from .models import *
from django.db.models import Q

class inicio_sesion(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO', 'class': 'text_box'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA', 'class': 'text_box'}))

    class Meta:
        fields = ("nombre_usuario","contrasena")

class cliente(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA'}))
    cui = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'CUI'}))
    nit = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NIT'}))
    nombre = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE'}))
    apellido = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'APELLIDO'}))
    fecha_nacimiento = forms.CharField(required = True, help_text='', label='FECHA DE NACIMIENTO', widget=forms.SelectDateWidget(years=range(1950, 2021), attrs={'class': 'date'}))


    class Meta:
        fields = ("nombre_usuario","contrasena", "cui","nit", "nombre", "apellido", "fecha_nacimiento")

class empresa(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA'}))
    nombre = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE EMPRESA'}))
    nombre_comercial = forms.CharField(required = True, max_length=100, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE COMERCIAL'}))
    nombre_representante = forms.CharField(required = True, max_length=150, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DEL REPRESENTANTE'}))
    tipo_empresa = forms.CharField(required = True, max_length=150, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'TIPO DE EMPRESA'}))


    class Meta:
        fields = ("nombre_usuario","contrasena", "nombre", "nombre_comercial", "nombre_representante", "tipo_empresa")

class cuenta(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    TIPOS_CUENTA = [('', 'SELECCIONAR TIPO DE CUENTA'), ('MONETARIA', 'MONETARIA'), ('CUENTA DE AHORRO', 'CUENTA DE AHORRO'), ('CUENTA DE AHORRO A PLAZO FIJO', 'CUENTA DE AHORRO A PLAZO FIJO')]
    tipo_cuenta = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_CUENTA)
    TIPOS_MONEDA = [('', 'SELECCIONAR TIPO DE MONEDA'), ('QUETZAL', 'QUETZAL'), ('DOLLAR', 'DOLLAR')]
    tipo_moneda = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_MONEDA)
    usuario = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Usuario.objects.all(), empty_label="SELECCIONE UN USUARIO", to_field_name="id_usuario")

    class Meta:
        fields = ("monto","tipo_cuenta", "tipo_moneda", "usuario")

class transaccion(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    TIPOS_MONEDA = [('', 'SELECCIONAR TIPO DE MONEDA'), ('QUETZAL', 'QUETZAL'), ('DOLLAR', 'DOLLAR')]
    tipo_moneda = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_MONEDA)
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all().filter(estado='ACTIVA'), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("monto", "tipo_moneda", "cuenta")

class chequera(forms.Form):
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all().filter(tipo_cuenta="MONETARIA").filter(estado='ACTIVA'), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("cuenta")

class usuario(forms.Form):
    usuario = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Usuario.objects.all(), empty_label="SELECCIONE UN USUARIO", to_field_name="id_usuario")

    class Meta:
        fields = ("usuario")

class a_correlativo(forms.Form):
    correlativo = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'CORRELATIVO DE CHEQUE'}))

    class Meta:
        fields = ("correlativo")

