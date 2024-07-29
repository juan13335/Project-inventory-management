from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=15, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=15, null=False)
    descripcion = models.TextField(blank=True, null=True)
    stock_actual = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(null=False)
    f_creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nombre


class Precio(models.Model):
    cantidad = models.PositiveIntegerField(null=True, blank=True) 
    precio_uni = models.PositiveIntegerField(null=True, blank=True)
    precio_total = models.PositiveIntegerField(null=True, blank=True)
    f_actualizado = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar
        self.precio_total = self.cantidad * self.precio_uni
        super(Precio, self).save(*args, **kwargs)

    def __str__(self):
        return self.producto.nombre
    

class Venta(models.Model):
    pass