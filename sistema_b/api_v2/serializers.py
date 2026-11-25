from rest_framework import serializers

from core.models import Vehiculo, Vivienda


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('id', 'patente', 'marca', 'modelo', 'color', 'activo')


class ViviendaSerializer(serializers.ModelSerializer):
    vehiculos = VehiculoSerializer(many=True, read_only=True)

    class Meta:
        model = Vivienda
        fields = ('id', 'piso', 'numero', 'propietario', 'vehiculos')
