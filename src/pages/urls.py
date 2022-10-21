from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),#vacío porque es elhomepage
    path('comparar', views.comparar, name='comparar'),
    #vies.index -> trae el metodo index del views de esta app, name='index' es el nombre para acceder a este path.
]
