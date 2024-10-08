from django.db import models
import enum
# Create your models here.

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
    TIPO_CHOICES = [
        ('porcentaje', 'Porcentaje'),
        ('fijo', 'Fijo'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='porcentaje')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    frecuencia = enum.Enum('diario', 'semanal', 'mensual')
    productos = models.ManyToManyField(Producto, related_name='descuentos')
    
    class Meta:
        db_table = 'descuentos'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
        
class Extras(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'extras'
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'

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
    
    class Meta:
        db_table = 'ingredientes'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        
        
        

