from django.shortcuts import render, redirect
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