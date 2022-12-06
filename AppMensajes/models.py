from django.db import models

class Usuario (models.Model):
    
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Identificacion = models.IntegerField()
    Email = models.EmailField()
    
    def __str__(self):
        return self.Nombre+" "+self.Apellido+" "+str(self.Identificacion)+" "+self.Email
    
    
class Analista (models.Model):
    
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Rol = models.CharField(max_length=50)
    Identificacion = models.IntegerField()
    Email = models.EmailField()
    
    def __str__(self):
        return self.Nombre+" "+self.Apellido+" "+self.Rol+" "+str(self.Identificacion)+" "+self.Email
    

class Mensaje (models.Model):
    
    Asunto = models.CharField(max_length=200)
    Cuerpo = models.CharField(max_length=500)
    Para = models.EmailField()
    
    def __str__(self):
        return self.Asunto+" "+self.Cuerpo+" "+self.Para


class Vacante (models.Model):
    
    Nom_Vacante = models.CharField(max_length=80)
    Id_Vacante = models.IntegerField()
    
    def __str__(self):
        return self.Nom_Vacante+" "+str(self.Id_Vacante)