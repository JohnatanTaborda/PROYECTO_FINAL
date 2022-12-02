from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('usuario/', usuario, name="usuario"),
    path('analista/', analista, name="analista"),
    path('mensaje/', mensaje, name="mensaje"),
    path('vacante/', vacante, name="vacante"),
    path('usuario_form/', usuario_form, name="usuario_form"),
    path('analista_form/', analista_form, name="analista_form"),
    path('mensaje_form/', mensaje_form, name="mensaje_form"),
    path('vacante_form/', vacante_form, name="vacante_form"),
]
