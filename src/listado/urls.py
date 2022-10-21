from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="listados"), #este es /listados
    path("<int:listado_id>", views.listado, name="listado"),
    path("buscar", views.buscar, name="buscar"),
]
