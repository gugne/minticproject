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
    listados= Producto.objects.filter(es_listado=True).order_by('titulo')
    queryset_list= Producto.objects.filter(es_listado=True)
    fabricante1= None
    vehiculo1= None
    vehiculo2= None
    
    
    # if 'fabricante1' in request.GET:
    #     fabricante1 = request.GET['fabricante1']
    #     if fabricante1:
    #         queryset_list = queryset_list.filter(fabricante__fabricante__iexact=fabricante1)
    #         print (fabricante1)
            
    if 'vehiculo1' in request.GET:
        vehiculo1 = request.GET['vehiculo1']
        if vehiculo1:
            queryset_list = queryset_list.filter(titulo__iexact=vehiculo1)
            print (vehiculo1)
            
    if 'vehiculo2' in request.GET:
        vehiculo2 = request.GET['vehiculo2']
        if vehiculo2:
            queryset_list = queryset_list.filter(titulo__iexact=vehiculo2)
            print (vehiculo2)
            
    context= {
        'listados' : listados,
        'fabricante1' : fabricante1,
        'vehiculo1' : vehiculo1,
        'vehiculo2' : vehiculo2,
        
    }
    return render(request, 'pages/comparar.html', context)
