from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, loader
# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def usuario(request):
    return render (request, "usuario.html")

def analista(request):
    return render (request, "analista.html")

def mensaje(request):
    return render (request, "mensaje.html")

def vacante(request):
    return render (request, "vacante.html")
