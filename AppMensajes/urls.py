from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('', inicio),
    path('usuario/', usuario),
    path('analista/', analista),
    path('mensaje/', mensaje),
    path('vacante/', vacante),
    
]
