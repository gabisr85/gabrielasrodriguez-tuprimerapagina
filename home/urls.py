from django.urls import path
from home.views import inicio, agregar_producto, listado_productos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto/', listado_productos, name='listado_productos'),
    path('producto/agregar/', agregar_producto, name='agregar_producto')
]