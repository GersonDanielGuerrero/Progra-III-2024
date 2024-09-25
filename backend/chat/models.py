from django.db import models
from usuarios.models import Usuario
import enum

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