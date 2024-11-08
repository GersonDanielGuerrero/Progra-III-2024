from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# importar modelo producto
from menu.models import Producto
from usuarios.models import Usuario, Direccion
from .models import Carrito, Carrito_Producto, Carrito_Producto_Extra, Venta, Venta_Producto
from rest_framework import status
from .serializers import CarritoSerializer

class CarritoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        usuario = request.user
        carrito = usuario.carrito
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)
    
    def put(self, request):
        usuario = request.user
        productos = request.data.get('productos')
        tipo_entrega = request.data.get('tipo_entrega')
        metodo_pago = request.data.get('metodo_pago')
        id_direccion = request.data.get('id_direccion')
        
        carrito = usuario.carrito
        for producto in productos:
            #Obtener el carrito_producto correspondiente si existe y modificarlo, si no, devolver error
            producto_guardado = Producto.objects.get(id=producto['id'])
            carrito_producto = carrito.productos.filter(producto=producto_guardado).first()
            if carrito_producto:
                carrito_producto.cantidad = producto['cantidad']
                
                carrito_producto.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'mensaje': 'El producto no está en el carrito'})
            carrito.tipo_entrega = tipo_entrega
            carrito.metodo_pago = metodo_pago
            if id_direccion:
                carrito.direccion = Direccion.objects.get(id=id_direccion)
            carrito.save()
            return Response(status=status.HTTP_200_OK, data={'mensaje': 'Carrito actualizado correctamente'})
    
    def delete(self, request):
        usuario = request.user
        carrito = Carrito.objects.filter(usuario=usuario)
        ids = request.data.get('ids')
        productos_a_eliminar = []
        for id in ids:
            carrito_producto = Carrito_Producto.objects.get(id=id)
            if carrito_producto:
                productos_a_eliminar.append(carrito_producto)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'mensaje': f'No se encontró el producto con id {id}'})
        for producto in productos_a_eliminar:
            producto.delete()
        return Response(status=status.HTTP_200_OK, data={'mensaje': 'Productos eliminados correctamente'})

class VentaView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        usuario = request.user
        carrito = usuario.carrito
        productos = request.data.get('productos')
        tipo_entrega = request.data.get('tipo_entrega')
        id_direccion = request.data.get('id_direccion')
        metodo_pago = request.data.get('metodo_pago')
        if not productos:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'mensaje': 'No se enviaron productos'})
        direccion = Direccion.objects.get(id=id_direccion)
        venta = Venta()
        venta.usuario = usuario
        venta.tipo_entrega = tipo_entrega
        venta.metodo_pago = metodo_pago
        venta.direccion = direccion
        venta.save()
        
        for producto in productos:
            producto_guardado = Producto.objects.get(id=producto['id'])
            venta_producto = Venta_Producto()
            venta_producto.venta = venta
            venta_producto.producto = producto_guardado
            venta_producto.cantidad = producto['cantidad']
            venta_producto.precio_compra = producto_guardado.precio
            venta_producto.save()
        return Response(status=status.HTTP_201_CREATED, data={'mensaje': 'Venta realizada correctamente'})
            
        