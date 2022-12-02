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

def usuario_form(request):
    
    if request.method=="POST":
        
        nombreusuario =request.POST["nombre"]
        apellidousuario = request.POST["apellido"]
        identifacionusuario = request.POST["identificacion"]
        emailusuario = request.POST["email"]
       
        usuario1 = Usuario(Nombre=nombreusuario, Apellido=apellidousuario, Identificacion=identifacionusuario, Email=emailusuario)
        usuario1.save()
        
        return render(request, "usuario.html")
    
    return render (request, "usuario_form.html")


def analista_form(request):
    
    if request.method=="POST":
        
        nombreanalista =request.POST["nombre"]
        apellidoanalista = request.POST["apellido"]
        rolanalista = request.POST["rol"]
        identifacionanalista = request.POST["identificacion"]
        emailanalista = request.POST["email"]
       
        analista1 = Analista(Nombre=nombreanalista, Apellido=apellidoanalista, Rol=rolanalista, Identificacion=identifacionanalista, Email=emailanalista)
        analista1.save()
        
        return render(request, "analista.html")
    
    return render (request, "analista_form.html")


def mensaje_form(request):
    
    if request.method=="POST":
        
        mensaje_mensaje =request.POST["mensaje"]
        cuerpo_mensaje = request.POST["cuerpo"]
        para_mensaje = request.POST["para"]
       
        mensaje1 = Mensaje(Asunto=mensaje_mensaje, Cuerpo=cuerpo_mensaje, Para=para_mensaje)
        mensaje1.save()
        
        return render(request, "mensaje.html")
    
    return render (request, "mensaje_form.html")


def vacante_form(request):
    
    if request.method=="POST":
        
        nombre_vacanteVac =request.POST["vacante"]
        id_vacanteVac = request.POST["id"]
       
        vacante1 = Vacante(Nom_Vacante=nombre_vacanteVac, Id_Vacante=id_vacanteVac)
        vacante1.save()
        
        return render(request, "vacante.html")
    
    return render (request, "vacante_form.html")