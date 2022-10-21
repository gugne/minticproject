from ast import keyword
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import condiciones, ubicaciones, fabricantes, categorias, precios
# Create your views here.
def index(request):
    listados= Producto.objects.order_by('-fecha_listado').filter(es_listado=True)
    #variable |Nombre modelo
    paginator= Paginator(listados, 6)
    page = request.GET.get('page')
    pagina_listada = paginator.get_page(page)
    
    context= {
        'listados': pagina_listada
    }
    
    
    return render (request, 'listado/listados.html', context)
    
def listado(request, listado_id ):
    listado= get_object_or_404(Producto, pk=listado_id)
    context= {
        'listado' : listado
    }
    return render (request, 'listado/listado.html', context)

    
def buscar(request):
    queryset_list= Producto.objects.order_by('-fecha_listado')
        
    #Condición: Nuevo/Usado
    if 'condicion' in request.GET:
        condicion = request.GET['condicion']
        if condicion:
            queryset_list = queryset_list.filter(condicion__condicion__iexact=condicion)
            
            
    #Ubicación: País
    if 'ubicacion' in request.GET:
        ubicacion = request.GET['ubicacion']
        if ubicacion:
            queryset_list = queryset_list.filter(ubicacion__ubicacion__iexact=ubicacion)
            #ubicacion__ubicacion(Foreingkey)__ixact= campo en Producto = ubicaiones (campo en)
            
     #Fabricante: Marca
    if 'fabricante' in request.GET:
        fabricante = request.GET['fabricante']
        if fabricante:
            queryset_list = queryset_list.filter(fabricante__fabricante__iexact=fabricante)

     #Fabricante: Marca
    if 'categoria' in request.GET:
        categoria = request.GET['categoria']
        if categoria:
            queryset_list = queryset_list.filter(categoria__categoria__iexact=categoria)
            
    #Precio: $$
    if 'precio' in request.GET:
        precio = request.GET['precio']
        if precio:
            queryset_list = queryset_list.filter(precio__lte=precio)
    

    context={
        'condiciones' : condiciones,
        'ubicaciones' : ubicaciones,
        'fabricantes' : fabricantes,
        'categorias' : categorias,
        'precios' : precios,
        'listados' : queryset_list,
        'values' : request.GET,
    }
    return render (request, 'listado/buscar.html', context)