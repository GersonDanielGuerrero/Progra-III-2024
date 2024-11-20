from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre','url_foto']
        
class ProductoListaSerializer(serializers.ModelSerializer):
    #Estos valores pueden ser nulos
    valor_descuento = serializers.CharField(source='descuento.valor', allow_null=True)
    tipo_descuento = serializers.CharField(source='descuento.tipo', allow_null=True)
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion','precio', 'valor_descuento', 'tipo_descuento', 'url_foto']