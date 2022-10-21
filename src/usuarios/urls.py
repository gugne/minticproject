from django.urls import path
from .import views

urlpatterns = [
    path("ingresar", views.ingresar, name="ingresar"),
    path("salir", views.salir, name="salir"), 
    path("registrarse", views.registrarse, name="registrarse"),
    path("dashboard", views.dashboard, name="dashboard"),
]
