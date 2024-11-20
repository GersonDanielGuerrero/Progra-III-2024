from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistroSerializer, DireccionSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Direccion
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'El usuario ha sido registrado con exito'})
    
class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        usuario = self.obtener_usuario(request.data)
        if usuario is not None:
            respuesta = super().post(request, *args, **kwargs)
            
            respuesta.data['usuario'] = {
                'nombre': usuario.nombre,
                'roles': usuario.roles.values_list('nombre', flat=True)
            }
            print(respuesta.data['usuario'])
            return respuesta
    def obtener_usuario(self, data):
        from django.contrib.auth import get_user_model
        Usuario = get_user_model()
        correo = data.get('correo')
        try:
            return Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            return None
            
    
class DireccionesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        usuario = request.user
        direcciones = Direccion.objects.filter(usuario=usuario)
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data)