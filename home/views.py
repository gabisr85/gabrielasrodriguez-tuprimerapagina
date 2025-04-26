from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionProducto
from home.models import Producto
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'home/inicio.html')

@login_required
def agregar_producto(request):
    print("Estos son los datos del GET", request.GET)
    print("Estos son los datos del POST", request.POST)
    if request.method == "POST":
        formulario = CreacionProducto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(tipo_de_producto=info.get('tipo_de_producto'), marca=info.get('marca'), codigo=info.get('codigo'), fecha_carga=info.get('fecha_carga'))
            producto.save()
            return redirect('inicio')
    else:
        formulario = CreacionProducto()

    return render(request, 'home/agregar_producto.html', {'formulario' : formulario})

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'home/listado_productos.html', {"productos" : productos})

def detalle_producto(request, producto_especifico):
    producto = Producto.objects.get(id=producto_especifico)
    return render(request, 'home/detalle_producto.html', {'producto' : producto})

class VistaDetalleProducto(DetailView):
    model = Producto
    template_name = 'home/detalle_producto.html'

class VistaModificarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'home/modificar_producto.html'
    fields = ["tipo_de_producto", "marca", "codigo"]
    success_url = reverse_lazy('listado_productos')

class VistaEliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'home/eliminar_producto.html'
    success_url = reverse_lazy('listado_productos') 