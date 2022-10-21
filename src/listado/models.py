from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Producto(models.Model):
    fabricante= models.ForeignKey('Fabricante', on_delete=models.CASCADE )
    ubicacion= models.ForeignKey('Ubicacion', on_delete=models.CASCADE )
    categoria= models.ForeignKey('Categoria', on_delete=models.CASCADE )
    condicion= models.ForeignKey('Condicion', on_delete=models.CASCADE )
    titulo= models.CharField (max_length=200 )
    descripcion= models.TextField( blank=True )
    modelo= models.IntegerField()
    precio= models.IntegerField()
    transmision= models.CharField( max_length=200 )
    kilometraje= models.IntegerField()
    combustible= models.CharField( max_length=200 )
    color= models.CharField( max_length=200 )
    foto_principal= models.ImageField( upload_to='photos/%Y%m%d/', height_field=None, width_field=None, max_length=None )
    foto_dos= models.ImageField( upload_to='photos/%Y%m%d/', blank=True )
    foto_tres= models.ImageField( upload_to='photos/%Y%m%d/', blank=True )
    foto_cuatro= models.ImageField( upload_to='photos/%Y%m%d/', blank=True )
    foto_cinco= models.ImageField( upload_to='photos/%Y%m%d/', blank=True )
    es_listado= models.BooleanField(default=True)
    fecha_listado= models.DateTimeField( default=datetime.now, blank=True )
    
    def __str__(self):
        return self.titulo
    
class Fabricante(models.Model):
    fabricante=models.CharField(max_length=50)
    def __str__(self):
        return self.fabricante   

class Categoria(models.Model):
    categoria=models.CharField( max_length=50)
    def __str__(self):
        return self.categoria

class Ubicacion(models.Model):
    ubicacion=models.CharField( max_length=50)
    def __str__(self):
        return self.ubicacion

class Condicion(models.Model):
    condicion=models.CharField( max_length=50)
    def __str__(self):
        return self.condicion
    
    
    


    
    
    