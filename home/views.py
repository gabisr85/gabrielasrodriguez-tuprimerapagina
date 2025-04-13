from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionProducto
from home.models import Producto

def inicio(request):
    return render(request, 'home/inicio.html')

def agregar_producto(request):
    print("Estos son los datos del GET", request.GET)
    print("Estos son los datos del POST", request.POST)
    if request.method == "POST":
        formulario = CreacionProducto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(tipo_de_producto=info.get('tipo_de_producto'), marca=info.get('marca'), codigo=info.get('codigo'))
            producto.save()
            return redirect('inicio')
    else:
        formulario = CreacionProducto()

    return render(request, 'home/agregar_producto.html', {'formulario' : formulario})

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'home/listado_productos.html', {"productos" : productos})