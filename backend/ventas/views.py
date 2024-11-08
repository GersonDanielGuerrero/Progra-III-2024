from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# importar modelo producto
from menu.models import Producto
from .models import Carrito, Carrito_Producto, Carrito_Producto_Extra, Venta, Venta_Producto
from rest_framework import status

class CarritoProductoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        usuario = request.user
        carrito = usuario.carrito
        producto = Producto.objects.get(id=request.data.get('producto'))
        detalles = request.data.get('detalles')
        cantidad = request.data.get('cantidad')

        if not producto:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'mensaje': 'Producto no encontrado'})
            
        carrito_producto = Carrito_Producto.objects.create(
            carrito=carrito,
            producto=producto,
            cantidad=cantidad,
            detalles=detalles
        )
        carrito_producto.save()
        return Response(status=status.HTTP_201_CREATED)