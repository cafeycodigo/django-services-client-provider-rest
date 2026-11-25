---
title: "5. Consumo con requests"
sidebar_position: 7
---

El cliente de prueba de A recibe dos valores y envía un POST JSON al proveedor de B. `json=payload` serializa el diccionario y configura el tipo de contenido. `timeout` limita la espera de red y `raise_for_status()` convierte respuestas HTTP de error en excepciones.

## Ejercicio

Con B activo, abre el shell de A y prueba el proveedor mediante el cliente de Django apuntando a la ruta de A.

```python
from django.test import Client

respuesta = Client(HTTP_HOST="localhost").post(
    "/api/test/client/",
    {"valor_1": 10, "valor_2": 5, "operacion": "suma"},
    content_type="application/json",
)
print(respuesta.status_code, respuesta.content.decode())
```

El resultado esperado del proveedor es 15 y viene anidado en la respuesta del cliente. Si B devuelve 403 por CSRF, revisa el middleware y el contrato de autenticación servicio a servicio. Para aislar la lógica del proveedor puedes probar `/api/test/provider/` con el cliente de pruebas en el shell de B. Como ampliación, mueve la URL a una variable de entorno y devuelve mensajes de error específicos para timeout y estados HTTP del proveedor.

## Código del repositorio

```python title="sistema_a/api_test/views.py"
import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def cliente(request):
    try:
        datos = json.loads(request.body or '{}')
        payload = {'valor_1': datos['valor_1'], 'valor_2': datos['valor_2'], 'operacion': datos.get('operacion', 'suma')}
        respuesta = requests.post(settings.SYSTEM_B_TEST_API_URL, json=payload, timeout=5)
        respuesta.raise_for_status()
        resultado = respuesta.json()
        return JsonResponse({'cliente': 'sistema_a', 'proveedor': 'sistema_b', 'resultado': resultado})
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        return JsonResponse({'error': str(error)}, status=400)
    except requests.RequestException as error:
        return JsonResponse({'error': f'No fue posible contactar al proveedor: {error}'}, status=502)
```

## Código del repositorio

```python title="sistema_b/api_test/views.py"
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def proveedor(request):
    try:
        datos = json.loads(request.body or '{}')
        valor_1 = float(datos['valor_1'])
        valor_2 = float(datos['valor_2'])
        operacion = datos.get('operacion', 'suma')
        operaciones = {'suma': valor_1 + valor_2, 'resta': valor_1 - valor_2, 'multiplicacion': valor_1 * valor_2}
        if operacion == 'division':
            if valor_2 == 0:
                return JsonResponse({'error': 'No se puede dividir por cero.'}, status=400)
            resultado = valor_1 / valor_2
        elif operacion in operaciones:
            resultado = operaciones[operacion]
        else:
            return JsonResponse({'error': 'Operación no soportada.'}, status=400)
        return JsonResponse({'valor_1': valor_1, 'valor_2': valor_2, 'operacion': operacion, 'resultado': resultado})
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        return JsonResponse({'error': str(error)}, status=400)
```
