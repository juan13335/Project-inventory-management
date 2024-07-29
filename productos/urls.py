from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('producto/registrar', views.crearproducto, name='crearproducto'),
    path('categoria/registrar', views.crearcategoria, name='crearcategoria'),
    path('producto/compra/', views.crearcompra, name='compra'),
]