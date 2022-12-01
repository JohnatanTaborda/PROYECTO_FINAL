from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('usuario/', usuario, name="usuario"),
    path('analista/', analista, name="analista"),
    path('mensaje/', mensaje, name="mensaje"),
    path('vacante/', vacante, name="vacante"),
    
]
