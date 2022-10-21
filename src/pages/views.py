from django.shortcuts import render
from django.http import HttpResponse
from listado.models import Producto
from listado.choices import condiciones, ubicaciones, fabricantes, categorias, precios

def index(request):
    listados= Producto.objects.order_by('-fecha_listado').filter(es_listado=True)[:4]
    context= {
        'listados' : listados,
        'condiciones' : condiciones,
        'ubicaciones' : ubicaciones,
        'fabricantes' : fabricantes,
        'categorias' : categorias,
        'precios' : precios,
    }
    return render(request, 'pages/index.html', context) #'pages/index.html -> locación del template

def comparar(request):
    return render(request, 'pages/comparar.html')
