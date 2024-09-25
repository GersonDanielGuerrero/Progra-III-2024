from rest_framework import serializers
from .models import Usuario, Direccion, Rol

class DireccionRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['nombre', 'direccion', 'lat', 'lon', 'indicaciones']
class RegistroSerializer(serializers.ModelSerializer):
    direcciones = DireccionRegistroSerializer(many=True)
    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Rol.objects.all())
    class Meta:
        model = Usuario
        fields = ['correo','nombre', 'apellido', 'telefono', 'contraseña', 'confirmar_contraseña', 'direcciones', 'roles']
        extra_kwargs = {'contraseña': {'write_only': True}, 'confirmar_contraseña': {'write_only': True}}
        
    def create(self, validated_data):
        
        contraseña = validated_data.pop('contraseña')
        confirmar_contraseña = validated_data.pop('confirmar_contraseña')
        
        
        if contraseña != confirmar_contraseña:
            raise serializers.ValidationError({'contraseña': 'Las contraseñas no coinciden'})
        
        if(Usuario.objects.filter(correo=validated_data['correo']).exists()):
            raise serializers.ValidationError({'correo': 'Ya existe una cuenta registrada con este correo'})
        
        usuario = Usuario(**validated_data)
        usuario.set_password(contraseña)
        usuario.save()
        return usuario
        