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
    PASSWORD_FIELD = 'contraseña'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono','contraseña']
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(Usuario, related_name='roles')
    
    class Meta:
        db_table = 'roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
class Direccion(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    indicaciones = models.TextField(null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')
    
    class Meta:
        db_table = 'direcciones'
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
