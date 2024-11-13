from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistroSerializer, DireccionSerializer, CuentaSerializer, UsuarioUpdateSerializer
from rest_framework.response import Response
from .models import Direccion, Usuario
# Create your views here.

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'El usuario ha sido registrado con exito'})

class CuentaView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        usuario = request.user
        serializer = CuentaSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request):
        usuario = request.user
        serializer = UsuarioUpdateSerializer(usuario, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()