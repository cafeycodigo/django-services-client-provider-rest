---
title: "3. API REST con DRF · API v2"
sidebar_position: 5
---

## Construir el CRUD desde el modelo

1. En `settings.py` de B registra `rest_framework` y `api_v2` en `INSTALLED_APPS`.
2. En `api_v2/serializers.py` define los campos públicos y sus reglas. `ViviendaSerializer` incluye los vehículos para lectura.
3. En `views.py` conecta el queryset a su serializer mediante `ModelViewSet`.
4. En `api_v2/urls.py` registra cada recurso en `DefaultRouter`. El URLconf del proyecto incluye ese router bajo `api/v2/`.

| URL | Métodos |
| --- | --- |
| `/api/v2/viviendas/` | GET, POST |
| `/api/v2/viviendas/{id}/` | GET, PUT, PATCH, DELETE |
| `/api/v2/vehiculos/` y su detalle | Rutas equivalentes |

Abre la colección de viviendas y sigue un ID real en el detalle. Un ID inexistente devuelve 404. El serializer de vehículo actual omite la vivienda obligatoria. Como práctica de ampliación, incluye `vivienda` en sus campos y comprueba que POST acepte un ID de vivienda válido y rechace uno inexistente. Revisa los permisos del ViewSet antes de exponerlo fuera del laboratorio.

## Código del repositorio

```python title="sistema_b/api_v2/serializers.py"
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
```

## Código del repositorio

```python title="sistema_b/api_v2/views.py"
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
```

## Código del repositorio

```python title="sistema_b/api_v2/urls.py"
from rest_framework.routers import DefaultRouter

from .views import VehiculoViewSet, ViviendaViewSet

router = DefaultRouter()
router.register('viviendas', ViviendaViewSet, basename='api-v2-vivienda')
router.register('vehiculos', VehiculoViewSet, basename='api-v2-vehiculo')

urlpatterns = router.urls
```
