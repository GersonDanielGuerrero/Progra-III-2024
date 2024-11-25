from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ChatSerializer
from rest_framework.response import Response
from .models import Mensaje
from usuarios.models import Usuario
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ChatView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        usuario = request.user
        id_cliente = request.query_params.get('id_cliente')
        version_ia = request.query_params.get('version_ia')
        tipo_usuario = 'cliente' if usuario.roles.filter(nombre='Cliente').exists() else 'empleado' if usuario.roles.filter(nombre='Atención al cliente').exists() else None
        if not tipo_usuario:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'mensaje': 'No tienes permisos para realizar esta acción'})
        serializer = ChatSerializer(instance=usuario, context={'id_cliente': id_cliente, 'version_ia': version_ia, 'tipo_usuario': tipo_usuario})
        return Response(serializer.data)