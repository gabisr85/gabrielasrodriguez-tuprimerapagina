from django.db import models

class Producto(models.Model):
    tipo_de_producto = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    fecha_carga = models.DateField(null=True)

    def __str__(self):
        return f'{self.tipo_de_producto} - {self.marca} - {self.codigo}'