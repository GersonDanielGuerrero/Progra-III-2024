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
        