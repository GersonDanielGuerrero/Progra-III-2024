from rest_framework import serializers
from .models import Categoria, Producto, Descuento

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre','url_foto']
        
class ProductoListaSerializer(serializers.ModelSerializer):
    descuento = serializers.CharField(source='descuento.valor')
    tipo_descuento = serializers.CharField(source='descuento.tipo')
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descuento', 'tipo_descuento', 'url_foto']