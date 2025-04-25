from django.urls import path
from home.views import inicio, agregar_producto, listado_productos, detalle_producto, VistaDetalleProducto, VistaModificarProducto, VistaEliminarProducto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto/', listado_productos, name='listado_productos'),
    path('producto/agregar/', agregar_producto, name='agregar_producto'),
    path('producto/<int:pk>/', VistaDetalleProducto.as_view(), name='detalle_producto'),
    path('producto/<int:pk>/modificar/', VistaModificarProducto.as_view(), name='modificar_producto'),
    path('producto/<int:pk>/eliminar/', VistaEliminarProducto.as_view(), name='eliminar_producto'),    
]