from django import forms
from .models import *
from django_select2.forms import ModelSelect2Widget
# Formularios

class CrearProductoform(forms.ModelForm):
    categoria = forms.ModelChoiceField( # Obtener los registros nombres
        queryset = Categoria.objects.all(),
        empty_label = "Seleccionar categoria",
        widget = forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'categoria',
            'stock_minimo',
            'descripcion',
        ]
        labels = {
            'nombre': 'Nombre de producto',
            'stock_minimo': 'Stock minimo',
            'descripcion': 'Observacion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el producto'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el minimo de stock'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Alguna observacion del producto'}),
        }

class CrearCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'descripcion',
        ]
        labels = {'descripcion': 'Observacion'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'})
        }


class Compraproducto(forms.ModelForm):
    class Meta:
        model = Precio
        fields = [
            'producto',
            'cantidad', 
            'precio_uni',
        ]
        labels = {
            'producto': 'Nombre de producto',
            'cantidad': 'Cantidad de producto',
            'precio_uni': 'Precio por unidad',
        }
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese cantidad comprada'}),
            'precio_uni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese precio por uinidad'}),
        }


        def clean(self):
            cleaned_data = super().clean()
            cantidad = cleaned_data.get('cantidad')
            precio_uni = cleaned_data.get('precio_uni')
            if cantidad and precio_uni:
                cleaned_data['precio_total'] = cantidad * precio_uni
            return cleaned_data