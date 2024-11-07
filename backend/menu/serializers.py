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
        fields = ['id', 'nombre', 'precio', 'valor_descuento', 'tipo_descuento', 'url_foto']

class ProductoDetalleSerializer(serializers.ModelSerializer):
    precio = serializers.SerializerMethodField()
    precio_anterior = serializers.SerializerMethodField()
    categoria = serializers.SerializerMethodField()
    imagen = serializers.CharField(source='url_foto')
    class Meta:
        model = Producto
        fields = ['id', 'nombre','descripcion', 'categoria', 'precio', 'precio_anterior','imagen']

    def get_precio(self, obj):
        if obj.descuento:
            if obj.descuento.tipo == 'porcentaje':
                return obj.precio - (obj.precio * obj.descuento.valor / 100)
            return obj.precio - obj.descuento.valor
        return obj.precio
    
    def get_precio_anterior(self, obj):
        if obj.descuento:
            return obj.precio
        return None
    
    def get_categoria(self, obj):
        return obj.categoria.nombre