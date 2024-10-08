from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategoriaSerializer, ProductoListaSerializer
from rest_framework.response import Response
from .models import Categoria, Producto, Descuento
from rest_framework import status

# Create your views here.
class CategoriaView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
class ListaProductosView(APIView):
    def get(self, request):
        categoria = request.query_params.get('categoria')
        filtro = request.query_params.get('filtro')
        
        productos = Producto.objects.all()
        if categoria:
            productos = productos.filter(categoria__nombre=categoria)
        if filtro:
            productos = productos.filter(nombre__icontains=filtro)
        serializer = ProductoListaSerializer(productos, many=True)
        return Response(serializer.data)