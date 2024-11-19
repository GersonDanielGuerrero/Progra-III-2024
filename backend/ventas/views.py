from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# importar modelo producto
from menu.models import Producto
from .models import Carrito, Carrito_Producto, Venta, Venta_Producto, Ingrediente, Carrito_Producto_Ingrediente
from rest_framework import status

class CarritoProductoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        usuario = request.user
        carrito = usuario.carrito
        detalles = request.data.get('detalles')
        cantidad = request.data.get('cantidad')
        ingredientes_obtenidos = request.data.get('ingredientes')
        id = request.data.get('id')
        producto = Producto.objects.filter(id=id).first()

        if not producto:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'mensaje': 'Producto no encontrado'})
        carrito_producto = Carrito_Producto.objects.create(
            carrito=carrito,
            producto=producto,
            cantidad=cantidad,
            detalles=detalles
        )
        carrito_producto.save()
        
        if ingredientes_obtenidos:
            for i in ingredientes_obtenidos:
                ingrediente = Ingrediente.objects.filter(id=i['id']).first()
                carrito_producto_ingrediente = Carrito_Producto_Ingrediente.objects.create(
                    carrito_producto=carrito_producto,
                    Ingrediente=ingrediente,
                    cantidad=i['cantidad']
                )
                carrito_producto_ingrediente.save()

        return Response(status=status.HTTP_201_CREATED)