from django.db import models
from usuarios.models import Usuario, Direccion
from menu.models import Producto, Extras, Ingrediente
import enum

# Create your models here.
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
    ingredientes = models.ManyToManyField(Ingrediente, related_name='carritos_productos')
    
    class Meta:
        db_table = 'carritos_productos'
        verbose_name = 'Carrito_Producto'
        verbose_name_plural = 'Carritos_Productos'
    

    
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
    ingredientes = models.ManyToManyField(Ingrediente, related_name='ventas_productos')
    
    class Meta:
        db_table = 'ventas_productos'
        verbose_name = 'Venta_Producto'
        verbose_name_plural = 'Ventas_Productos'


class Venta_Producto_Extra(models.Model):
    
    venta_producto = models.ForeignKey(Venta_Producto, on_delete=models.CASCADE, related_name='extras')
    extra = models.ForeignKey(Extras, on_delete=models.CASCADE, related_name='venta_productos')
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'ventas_productos_extras'
        verbose_name = 'Venta_Producto_Extra'
        verbose_name_plural = 'Ventas_Productos_Extras'
