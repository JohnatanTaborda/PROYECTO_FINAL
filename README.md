#README PROYECTO FINAL

# AppMensajes
## Proyecto final - Primera entrega (Curso de Python - Coderhouse)
AppMensajes es una web en la que puedes registrar información sobre los Analistas, los Usuarios, las Vacantes y los Mensajes de un proceso de selección. 

## Features

- Registre información sobre Usuarios, Analistas, Vacantes y  Mensajes.
- Haga búsquedas de información sobre Usuarios inscritos


## Tech

AppeMensajes utiliza:

- Pytho
- Visual Estudio Code
- Django
- GitHub

## Installation

- Clona el proyecto del [repositorio de GitHub](https://github.com/JohnatanTaborda/PROYECTO_FINAL.git )  con el comando git clone en la terminal
- En la terminal, situarse en la carpeta /ProyectoFinal/
- Correr el servidor con runserver en la terminal: python manage.py runserver

## Contenido

URL:

```sh
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
    path('buscarusuario/', buscarusuario, name="buscarusuario"),
    path('buscar/', buscar, name="buscar"),
]
```

Clases en models:

```sh
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
```

Apps:

```sh
class AppmensajesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppMensajes'

```

