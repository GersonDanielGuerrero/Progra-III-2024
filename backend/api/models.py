from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Usuario(AbstractBaseUser):
    correo = models.EmailField(max_length=200, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    contraseña = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono','contraseña']
    