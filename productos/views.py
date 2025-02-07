from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
# Create your views here.

def main(request):
    return render(request, 'main.html')


def crearproducto(request):
    if request.method == 'POST':
        form = CrearProductoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return render(request, 'crearproducto.html', {
                'form': form,
                'error': 'Datos ingresados no son validos'
            })
    else:
        form = CrearProductoform()
        return render(request, 'crearproducto.html', {
            'form': form,
        })

def crearcategoria(request):
    if request.method == 'POST':
        form = CrearCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return render(render, 'crearcategoria.html', {
                'form': form,
                'error': 'Los datos ingresados no son validos'
            })
    else:
        form = CrearCategoria(request.POST)
        return render(request, 'crearcategoria.html', {
            'form': form
        })

def crearcompra(request):
    if request.method == 'POST':
        form = Compraproducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return render(request, 'c_producto.html', {
                'form': form,
                'error': 'Los datos ingresados no son validos'
            })
    else:
        form = Compraproducto(request.POST)
        return render(request, 'c_producto.html', {
            'form': form,
        })
    
def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {
        'productos': productos
    })

def eliminar_producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return redirect('listarproducto')

def eliminar_categoria(request, categoria_id):
    if request.method == 'POST':
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        categoria.delete()
        return redirect('listarcategoria')

def modificar_producto(request, producto_id):
    pass
        

def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categoria.html', {
        'categorias': categorias
    })