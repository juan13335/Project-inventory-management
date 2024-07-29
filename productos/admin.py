from django.contrib import admin
from .models import *

class Productofecha(admin.ModelAdmin):
    readonly_fields = ('f_creado', )

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto, Productofecha)
admin.site.register(Precio)