from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistroSerializer
from rest_framework.response import Response
# Create your views here.

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'El usuario ha sido registrado con exito'})