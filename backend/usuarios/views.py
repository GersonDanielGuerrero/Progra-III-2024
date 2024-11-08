from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistroSerializer, DireccionSerializer
from rest_framework.response import Response
from .models import Direccion
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'El usuario ha sido registrado con exito'})
class DireccionesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        usuario = request.user
        direcciones = Direccion.objects.filter(usuario=usuario)
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data)