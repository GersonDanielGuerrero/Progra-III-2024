from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistroSerializer, DireccionSerializer
from rest_framework.response import Response
from .models import Direccion, Usuario
# Create your views here.

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'El usuario ha sido registrado con exito'})
    
class DireccionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        usuario = request.user
        direccion = usuario.direcciones.get(id=id)
        if not direccion:
            return Response({'mensaje': 'La dirección no existe dentro de tus direcciones'}, status=404)
        serializer = DireccionSerializer(direccion)
        return Response(serializer.data)
        
    