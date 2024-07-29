from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Precio)
def actualizar_stock(sender, instance, created, **kwargs):
    if created: # Determina si al instancia fue creada o no 
        producto = instance.producto
        producto.stock_actual += instance.cantidad
        producto.save()

