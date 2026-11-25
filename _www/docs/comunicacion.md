---
title: "2. Comunicación entre A y B"
sidebar_position: 4
---

## Contrato del flujo vehicular

1. A recibe `POST /api/v1/access/` con JSON como `{"plate":"ABCD12","movement":"entrada"}`.
2. A normaliza la patente y valida el movimiento. Usa `SYSTEM_B_API_URL` y `urllib` para consultar B.
3. B busca la patente activa con `patente__iexact`. Responde 200 con `authorized`, `house` y `vehicle`, o 404.
4. A registra el movimiento y responde 201 si lo autoriza o 403 si lo deniega. Un cuerpo inválido produce 400 antes de guardar.

## Verificación reproducible

```powershell
# Sustituye ABCD12 por una patente activa de tu base.
curl.exe -i http://localhost:8001/api/v1/vehicles/ABCD12/
```

Para probar el POST sin gestionar cookies en PowerShell, abre `manage.py shell` de A y usa el cliente de Django de abajo mientras B está encendido. El cliente de pruebas omite la comprobación CSRF por defecto. El navegador sí está sujeto al middleware.

```python
from django.test import Client
respuesta = Client(HTTP_HOST="localhost").post(
    "/api/v1/access/",
    {"plate": "ABCD12", "movement": "entrada"},
    content_type="application/json",
)
print(respuesta.status_code, respuesta.json())
```

Repite con una patente inexistente y con B apagado. El manejo actual agrupa los dos fallos en la misma respuesta. Una extensión consiste en capturar el 404 y las fallas de red por separado y guardar la causa de la decisión.

## Código del repositorio

```python title="sistema_b/api_v1/views.py"
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from core.models import Vehiculo


@require_GET
def vehicle_lookup(request, plate):
    vehiculo = Vehiculo.objects.select_related('vivienda').filter(
        patente__iexact=plate.strip(), activo=True
    ).first()
    if vehiculo is None:
        return JsonResponse({'authorized': False, 'detail': 'Vehículo no registrado'}, status=404)
    return JsonResponse({
        'authorized': True,
        'plate': vehiculo.patente,
        'house': {
            'floor': vehiculo.vivienda.piso,
            'number': vehiculo.vivienda.numero,
            'owner': vehiculo.vivienda.propietario,
        },
        'vehicle': {
            'brand': vehiculo.marca,
            'model': vehiculo.modelo,
            'color': vehiculo.color,
        },
    })
```
