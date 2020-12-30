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

class prestamo(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO SOLICITADO'}))
    TIPOS_PRESTAMO = [('', 'SELECCIONAR PLAZO EN EL QUE DECEA PAGAR'), ('12 MESES', '12 MESES'), ('24 MESES', '24 MESES'), ('36 MESES', '36 MESES'), ('48 MESES', '48 MESES')]
    tipo_prestamo = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_PRESTAMO)
    descripcion = forms.CharField(required = True, max_length=200, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'DESCRIPCION DEL POR QUE QUIERE EL PRESTAMO', 'class': 'text_box'}))

    class Meta:
        fields = ("monto","tipo_prestamo", "descripcion")

class buscar_prestamo(forms.Form):
    prestamos = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Prestamo.objects.all(), empty_label="SELECCIONE NUMERO DE PRESTAMO QUE DECEA", to_field_name="id_prestamo")

    class Meta:
        fields = ("prestamos")

class prestamo_automatico(forms.Form):
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO SOLICITADO'}))
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA REALIZAR LOS PAGOS", to_field_name="id_cuenta")
    prestamos = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Prestamo.objects.all(), empty_label="SELECCIONE NUMERO DE PRESTAMO QUE DECEA", to_field_name="id_prestamo")

    class Meta:
        fields = ("monto","cuenta", "prestamos")

class proveedor(forms.Form):
    nombre = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DEL PROVEEDOR', 'class': 'text_box'}))
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO A PAGAR'}))
    TIPOS_PAGO = [('', 'SELECCIONAR TIPO DE PAGOS'), ('MENSUAL', 'MENSUAL'), ('QUINCENAL', 'QUINCENAL')]
    tipo_pago = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_PAGO)
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA REALIZAR LOS PAGOS", to_field_name="id_cuenta")

    class Meta:
        fields = ("nombre","monto", "tipo_pago", "cuenta")

class pagar_provee(forms.Form):
    nombre_usuario = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DE USUARIO', 'class': 'text_box'}))
    contrasena = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.PasswordInput(attrs={'placeholder': 'CONTRASEÑA', 'class': 'text_box'}))
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA REALIZAR LOS PAGOS", to_field_name="id_cuenta")

    class Meta:
        fields = ("nombre_usuario","contrasena", "cuenta")


class planilla(forms.Form):
    nombre = forms.CharField(required = True, max_length=20, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'NOMBRE DEL EMPLEADO', 'class': 'text_box'}))
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO A PAGAR'}))
    TIPOS_PAGO = [('', 'SELECCIONAR TIPO DE PAGOS'), ('MENSUAL', 'MENSUAL'), ('QUINCENAL', 'QUINCENAL')]
    tipo_pago = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_PAGO)
    cuenta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Cuenta.objects.all(), empty_label="SELECCIONE NUMERO DE CUENTA PARA REALIZAR LOS PAGOS", to_field_name="id_cuenta")

    class Meta:
        fields = ("nombre","monto", "tipo_pago", "cuenta")

class evento_planilla(forms.Form):
    planilla = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Planilla.objects.all(), empty_label="SELECCIONAR PLANILLA", to_field_name="id_planilla")
    TIPOS_EVENTO = [('', 'SELECCIONAR TIPO DE EVENTO'), ('ELIMINAR', 'ELIMINAR'), ('EDITAR', 'EDITAR')]
    evento = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_EVENTO)

    class Meta:
        fields = ("planilla","evento")

