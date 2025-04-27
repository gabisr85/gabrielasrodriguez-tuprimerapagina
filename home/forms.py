from django import forms
from django.db import models
from home.models import Producto


class CreacionProducto(forms.Form):
    tipo_de_producto = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    codigo = forms.CharField(max_length=20)
    fecha_carga = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)

class ProductoForm(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ["tipo_de_producto", "marca", "codigo", "fecha_carga", "imagen"]        