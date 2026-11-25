from rest_framework import viewsets

from core.models import Vehiculo, Vivienda
from .serializers import VehiculoSerializer, ViviendaSerializer


class ViviendaViewSet(viewsets.ModelViewSet):
    """CRUD de viviendas para el proyecto React."""
    queryset = Vivienda.objects.prefetch_related('vehiculos').all()
    serializer_class = ViviendaSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    """CRUD de vehículos administrados desde React."""
    queryset = Vehiculo.objects.select_related('vivienda').all()
    serializer_class = VehiculoSerializer
