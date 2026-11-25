---
title: "Crear una API REST con Django"
sidebar_position: 2
---

**Meta.** Explicar y reproducir la cadena URL → ViewSet → serializer → modelo.

## Ejemplo resuelto con viviendas

En [API v2](../drf.md) están los archivos completos del repositorio. Este montaje mínimo muestra la porción de viviendas. Si sigues el ejercicio sobre este checkout, compara con los archivos existentes antes de editar.

1. Instala las dependencias de B usando [la preparación del laboratorio](../inicio.md). Comprueba que `rest_framework` y `api_v2` estén en `INSTALLED_APPS`.
2. Define los campos públicos. El modelo representa la tabla. El serializer convierte los registros a datos de respuesta y valida datos de escritura.

```python title="sistema_b/api_v2/serializers.py · versión mínima"
from rest_framework import serializers
from core.models import Vivienda

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = ("id", "piso", "numero", "propietario")
        read_only_fields = ("id",)
```

3. Conecta el serializer y los registros al ViewSet. DRF implementa las operaciones estándar.

```python title="sistema_b/api_v2/views.py"
from rest_framework import viewsets
from core.models import Vivienda
from .serializers import ViviendaSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
```

4. Registra `router.register("viviendas", ViviendaViewSet)` en el router de `api_v2/urls.py` y exporta `urlpatterns = router.urls`. En `sistema_b/sistema_b/urls.py` incluye `path("api/v2/", include("api_v2.urls"))`. Si cambias el modelo, ejecuta `makemigrations` y `migrate`. Un cambio exclusivo del serializer no modifica la tabla.

**Práctica guiada.** Envía el JSON del capítulo [CRUD](../crud.md). Localiza el ID de la respuesta `201` y úsalo en una consulta de detalle.

**Reto.** Omite propietario. Guarda el `400` y explica qué capa rechazó la escritura. El serializer es la primera capa que valida campos requeridos. [Tutorial oficial de DRF](https://www.django-rest-framework.org/tutorial/quickstart/)
