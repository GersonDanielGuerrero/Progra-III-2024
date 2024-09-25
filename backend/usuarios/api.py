from usuarios.models import Usuario, Direccion, Rol
from rest_framework import viewsets, permissions
from .serializers import RegistroSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer = RegistroSerializer(data=request.data)
        