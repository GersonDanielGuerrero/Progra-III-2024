from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import enum
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

class Anuncio(models.Model):
    url_foto = models.URLField(max_length=256)
    url_redireccion = models.URLField(max_length=256)
    
    class Meta:
        db_table = 'anuncios'
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    url_foto = models.URLField(max_length=256)
    
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    url_foto = models.URLField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
class Combo_Producto(models.Model):
    combo = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='combos')
    cantidad = models.IntegerField()
    
    class Meta:
        db_table = 'combos_productos'
        verbose_name = 'Combo_Producto'
        verbose_name_plural = 'Combos_Productos'
    
class Descuento(models.Model):
    tipo = enum.Enum('porcentaje', 'fijo')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    frecuencia = enum.Enum('diario', 'semanal', 'mensual')
    productos = models.ManyToManyField(Producto, related_name='descuentos')
    
    class Meta:
        db_table = 'descuentos'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
    
class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')
    
    class Meta:
        db_table = 'carritos'
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
    
class Carrito_Producto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='carritos')
    cantidad = models.IntegerField()
    detalles = models.TextField(null=True)
    
    class Meta:
        db_table = 'carritos_productos'
        verbose_name = 'Carrito_Producto'
        verbose_name_plural = 'Carritos_Productos'
    
class Extras(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'extras'
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'
    
class Carrito_Producto_Extra(models.Model):
    carrito_producto = models.ForeignKey(Carrito_Producto, on_delete=models.CASCADE, related_name='extras')
    extra = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name='carrito_productos')
    cantidad = models.IntegerField()
    
    class Meta:
        db_table = 'carritos_productos_extras'
        verbose_name = 'Carrito_Producto_Extra'
        verbose_name_plural = 'Carritos_Productos_Extras'
    
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = enum.Enum('tarjeta', 'efectivo')
    tipo_entrega = enum.Enum('domicilio', 'local')
    costo_envio = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, related_name='ventas',null=True)
    
    class Meta:
        db_table = 'ventas'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class Venta_Producto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    detalles = models.TextField(null=True)
    
    class Meta:
        db_table = 'ventas_productos'
        verbose_name = 'Venta_Producto'
        verbose_name_plural = 'Ventas_Productos'
class Tipo_Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table = 'tipo_ingredientes'
        verbose_name = 'Tipo_Ingrediente'
        verbose_name_plural = 'Tipos_Ingrediente'
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_ingrediente = models.ForeignKey(Tipo_Ingrediente, on_delete=models.CASCADE, related_name='ingredientes')
    carrito_productos = models.ManyToManyField(Carrito_Producto, related_name='ingredientes')
    venta_productos = models.ManyToManyField(Venta_Producto, related_name='ingredientes')
    
    class Meta:
        db_table = 'ingredientes'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
class Venta_Producto_Extra(models.Model):
    
    venta_producto = models.ForeignKey(Venta_Producto, on_delete=models.CASCADE, related_name='extras')
    extra = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name='venta_productos')
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'ventas_productos_extras'
        verbose_name = 'Venta_Producto_Extra'
        verbose_name_plural = 'Ventas_Productos_Extras'
class Pregunta_Frecuente(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()
    
    class Meta:
        db_table = 'preguntas_frecuentes'
        verbose_name = 'Pregunta_Frecuente'
        verbose_name_plural = 'Preguntas_Frecuentes'
    
class Mensaje(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes')
    por = enum.Enum('cliente', 'empleado')
    tipo = enum.Enum('texto', 'imagen')
    modo = enum.Enum ('empleado', 'bot')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'mensajes'
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'