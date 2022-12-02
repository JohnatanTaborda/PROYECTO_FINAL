from django.db import models

class Usuario (models.Model):
    
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Identificacion = models.IntegerField()
    Email = models.EmailField()
    
    
class Analista (models.Model):
    
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Rol = models.CharField(max_length=50)
    Identificacion = models.IntegerField()
    Email = models.EmailField()
    

class Mensaje (models.Model):
    
    Asunto = models.CharField(max_length=200)
    Cuerpo = models.CharField(max_length=500)
    Para = models.EmailField()

class Vacante (models.Model):
    
    Nom_Vacante = models.CharField(max_length=80)
    Id_Vacante = models.IntegerField()