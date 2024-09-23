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

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(Usuario, related_name='roles')
    
class Direccion(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    indicaciones = models.TextField(null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')

class Anuncio(models.Model):
    url_foto = models.URLField(max_length=256)
    url_redireccion = models.URLField(max_length=256)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    url_foto = models.URLField(max_length=256)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    url_foto = models.URLField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    combos = models.ManyToManyField('self', through='Combo_Producto', symmetrical=False)
    
class Combo_Producto(models.Model):
    combo = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='combos')
    cantidad = models.IntegerField()
    
class Descuento(models.Model):
    tipo = models.enums.Enum('porcentaje', 'fijo')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    frecuencia = models.enums.Enum('diario', 'semanal', 'mensual', 'anual')
    productos = models.ManyToManyField(Producto, related_name='descuentos')
    
class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')
    
class Carrito_Producto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='carritos')
    cantidad = models.IntegerField()
    detalles = models.TextField(null=True)
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_ingrediente = models.ForeignKey('Tipo_Ingrediente', on_delete=models.CASCADE, related_name='ingredientes')
    carrito_productos = models.ManyToManyField(Carrito_Producto, related_name='ingredientes')
    
class Tipo_Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    
class Extras(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    
class Carrito_Producto_Extra(models.Model):
    carrito_producto = models.ForeignKey(Carrito_Producto, on_delete=models.CASCADE, related_name='extras')
    extra = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name='carrito_productos')
    cantidad = models.IntegerField()
    