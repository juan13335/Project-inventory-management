from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('producto/registrar', views.crearproducto, name='crearproducto'),
    path('categoria/registrar', views.crearcategoria, name='crearcategoria'),
    path('producto/compra/', views.crearcompra, name='compra'),
    path('producto/listar/', views.listar_producto, name='listarproducto'),
    path('producto/listar/eliminado/<int:producto_id>', views.eliminar_producto, name='eliminarproducto')
]