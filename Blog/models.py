from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class POST(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre} ####### Apellido:{self.apellido} ####### contenido:{self.contenido}"
    
    titulo = models.CharField(max_length=30, default="-")
    subtitulo = models.CharField(max_length=50, default="-")
    nombre = models.CharField(max_length=20, default="-")
    apellido = models.CharField(max_length=20, default="-")
    contenido = models.CharField(max_length=250, default="-")
    
class Modelo2(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre} ####### Apellido:{self.apellido} ####### Edad:{self.edad}"
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()

class Modelo3(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre} ####### Apellido:{self.apellido} ####### Edad:{self.edad}"
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    
class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)