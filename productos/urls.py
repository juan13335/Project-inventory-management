from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('producto/registrar', views.crearproducto, name='crearproducto'),
    path('categoria/registrar', views.crearcategoria, name='crearcategoria'),
    path('producto/compra/', views.crearcompra, name='compra'),
    path('producto/listar/', views.listar_producto, name='listarproducto'),
    path('categoria/listar/', views.listar_categoria, name='listarcategoria'),
    path('categoria/listar/eliminado/<int:categoria_id>', views.eliminar_categoria, name='eliminarcategoria'),
    path('producto/listar/eliminado/<int:producto_id>', views.eliminar_producto, name='eliminarproducto')
]