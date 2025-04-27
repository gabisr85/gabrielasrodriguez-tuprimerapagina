from django.db import models

class Producto(models.Model):
    tipo_de_producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    fecha_carga = models.DateField(null=True)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)  


    def __str__(self):
        return f'{self.tipo_de_producto} - {self.marca} - {self.codigo} - {self.imagen}'