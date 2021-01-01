from django import forms
from .models import *
from django.db.models import Q

class tienda(forms.Form):
    
    tarjeta = forms.ModelChoiceField(required = True, help_text='', label='', queryset=Tarjeta.objects.all().select_related('id_usuario'), empty_label="SELECCIONE LA TARJETA DE USUARIO", to_field_name="id_tarjeta")
    TIPOS_MONEDA = [('', 'SELECCIONAR TIPO DE MONEDA'), ('QUETZAL', 'QUETZAL'), ('DOLLAR', 'DOLLAR')]
    tipo_moneda = forms.ChoiceField(required = True, help_text='', label='', choices=TIPOS_MONEDA)
    monto = forms.FloatField(required = True, help_text='', label='', widget=forms.NumberInput(attrs={'placeholder': 'MONTO'}))
    descripcion = forms.CharField(required = True, max_length=200, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'DESCRIPCION DE VENTA'}))
    
    class Meta:
        fields = ("tarjeta","tipo_moneda", "monto", "descripcion")