from django import forms

class CreacionProducto(forms.Form):
    tipo_de_producto = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    codigo = forms.CharField(max_length=20)
    fecha_carga = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))