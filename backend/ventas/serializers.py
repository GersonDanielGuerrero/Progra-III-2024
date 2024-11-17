from rest_framework import serializers
from .models import Carrito, Carrito_Producto, Carrito_Producto_Extra, Venta, Venta_Producto
from menu.models import Producto


class CarritoSerializer(serializers.ModelSerializer):
    id_direccion = serializers.IntegerField(source='direccion.id', required=False)
    productos = serializers.SerializerMethodField()
    class Meta:
        model = Carrito
        fields = ['productos', 'tipo_entrega', 'metodo_pago', 'id_direccion']
    def get_productos(self, obj):
        carrito_productos = obj.productos.all()
        if not carrito_productos:
            return []
        productos = []
        for carrito_producto in carrito_productos:
            id = carrito_producto.id
            nombre = carrito_producto.producto.nombre
            imagen = carrito_producto.producto.url_foto
            precio = carrito_producto.producto.precio
            cantidad = carrito_producto.cantidad
            seleccionado = carrito_producto.seleccionado
            
            productos.append({
                'id': id,
                'nombre': nombre,
                'imagen': imagen,
                'precio': precio,
                'cantidad': cantidad,
                'seleccionado': seleccionado
            })
        return productos
    
class ListaPedidosClientesSerializer(serializers.ModelSerializer):
    cantidad_productos = serializers.SerializerMethodField()
    nombre_cliente = serializers.SerializerMethodField()
    direccion = serializers.SerializerMethodField()