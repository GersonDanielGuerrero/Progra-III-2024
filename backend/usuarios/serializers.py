from rest_framework import serializers
from .models import Usuario, UserManager, Direccion, Rol

class RegistroSerializer(serializers.ModelSerializer):
    confirmar_contraseña = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    contraseña = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Usuario
        fields = ['correo','nombre', 'apellido', 'telefono', 'contraseña', 'confirmar_contraseña']
        extra_kwargs = {'contraseña': {'write_only': True}}
    
    def validate_contraseña(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('La contraseña debe tener al menos 6 caracteres')
        if not any(char.isdigit() for char in value) or not any(char.isupper() for char in value):
            raise serializers.ValidationError('La contraseña debe contener al menos un número y una letra mayúscula')
        return value
    def validate(self, data):
        if data['contraseña'] != data.pop('confirmar_contraseña'):
            raise serializers.ValidationError({'contraseña': 'Las contraseñas no coinciden'})
        return data
    def create(self, validated_data):
        contraseña = validated_data.pop('contraseña')
        usuario = Usuario(
            correo=validated_data['correo'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            telefono=validated_data['telefono']
        )
        usuario.set_password(contraseña)
        usuario.save()
        return usuario

class DireccionesListaSerializer(serializers.ModelSerializer):
    predeterminada = serializers.BooleanField(default=False)
    class Meta:
        model = Direccion
        fields = ['id', 'nombre', 'direccion', 'predeterminada']

class UsuarioCuentaSerializer(serializers.ModelSerializer):
    direcciones = DireccionesListaSerializer(many=True)
    class Meta:
        model = Usuario
        nombres = serializers.CharField(source='nombre')
        apellidos = serializers.CharField(source='apellido')
        fields = ['id', 'correo', 'nombres', 'apellidos', 'telefono']

class RolListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        usuario = UsuarioCuentaSerializer()
        direcciones = DireccionesListaSerializer(many=True)
        roles = RolListaSerializer(many=True)
        fields = ['usuario', 'direcciones', 'roles']
    
class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        nombres = serializers.CharField(source='nombre')
        apellidos = serializers.CharField(source='apellido')
        fields = ['correo', 'nombres', 'apellidos', 'telefono']
        
