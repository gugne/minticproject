from django.contrib import admin
from .models import Condicion, Producto, Fabricante, Categoria, Ubicacion

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display= ('id', 'titulo', 'es_listado', 'fecha_listado', 'fabricante', 'precio' )
    list_display_links= ('id', 'titulo' )
    list_filter= ('fabricante', 'categoria', 'ubicacion', 'condicion')   
    list_editable= ('es_listado',) 
    search_fields= ( 'titulo', 'condicion__condicion', 'transmision', 'combustible', 'fabricante__fabricante' )
    list_per_page= (25)
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Ubicacion)
admin.site.register(Condicion)
    
