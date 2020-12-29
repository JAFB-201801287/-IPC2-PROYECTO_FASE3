from django import forms
from .models import *
from django.db.models import Q 

class inicio_sesion(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO', 'class': 'text_box'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA', 'class': 'text_box'}))

    class Meta:
        fields = ("nombre_usuario","contrasena")

class transaccion(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    TIPOS_MONEDA = [('', 'SELECCIONAR TIPO DE MONEDA'), ('QUETZAL', 'QUETZAL'), ('DOLLAR', 'DOLLAR')]
    tipo_moneda = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_MONEDA)
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("monto", "tipo_moneda", "cuenta")


class estado(forms.Form):
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA", to_field_name="id_cuenta")

    class Meta:
        fields = ("cuenta")

class cuentas_propias(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    cuenta1 = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA TRASFERIR", to_field_name="id_cuenta")
    cuenta2 = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA DEPOSITAR", to_field_name="id_cuenta")

    class Meta:
        fields = ("monto", "tipo_moneda", "cuenta1" , "cuenta2")

class cuentas_terceros(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    cuenta1 = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA TRASFERIR", to_field_name="id_cuenta")
    no_cuenta = forms.IntegerField(required = True, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NUMERO DE CUENTA PARA DEPOSITAR'}))

    class Meta:
        fields = ("monto", "tipo_moneda", "cuenta1" , "no_cuenta")

class c_chequera(forms.Form):
    chequera = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Chequera.objects.all(), empty_label="SELECCIONE NUMERO DE CHEQUERA", to_field_name="id_chequera")

    class Meta:
        fields = ("chequera")

class c_cheque(forms.Form):
    cheque = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cheque.objects.all(), empty_label="SELECCIONE NUMERO DE CHEQUE", to_field_name="id_cheque")

    class Meta:
        fields = ("cheque")

class c_cheque1(forms.Form):
    cheque = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cheque.objects.all(), empty_label="SELECCIONE NUMERO DE CHEQUE", to_field_name="id_cheque")

    class Meta:
        fields = ("cheque")

class c_monto(forms.Form):
    nombre = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE RECEPTOR', 'class': 'text_box'}))
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO DEL CHEQUE'}))

    class Meta:
        fields = ("monto", "nombre")