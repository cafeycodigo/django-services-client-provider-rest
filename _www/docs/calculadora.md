---
title: "6. Calculadora distribuida"
sidebar_position: 8
---

## Proveedor y cliente

El proveedor `api_calculadora` lee `numero_1` y `numero_2` por GET o POST JSON. Cada operación tiene su ruta y su función. El cliente `api_calculo` recibe parámetros GET y los reenvía con `requests.get(params=...)`.

En este checkout ambos módulos están en B y el cliente apunta a B. La calculadora React también apunta directamente a B. El ejercicio `api_test` demuestra el trayecto entre procesos A y B.

```powershell
curl.exe 'http://localhost:8001/api/calculadora/suma/?numero_1=10&numero_2=5'
curl.exe 'http://localhost:8001/api/calculo/suma/?numero_1=10&numero_2=5'
```

Espera `{"operacion":"suma","resultado":15.0}`. Prueba `resta`, `multiplicacion`, `division` y `test`. Verifica 400 en división por cero.

## Ampliación entre A y B

Crea en A una app cliente siguiendo `sistema_b/api_calculo`. Registra sus URLs en A y configura su destino como `http://localhost:8001/api/calculadora`. Prueba `/api/calculo/suma/` en el puerto 8000 con ambos procesos activos. Detén B y agrega un manejo de timeout y de conexión con una respuesta 502 que el frontend pueda mostrar.

## Código del repositorio

```python title="sistema_b/api_calculadora/views.py"
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def obtener_numeros(request):
    datos = request.GET if request.method == 'GET' else json.loads(request.body or '{}')
    return float(datos['numero_1']), float(datos['numero_2'])

def responder(request, operacion, funcion):
    try:
        numero_1, numero_2 = obtener_numeros(request)
        return JsonResponse({'operacion': operacion, 'resultado': funcion(numero_1, numero_2)})
    except (KeyError, TypeError, ValueError, json.JSONDecodeError, ZeroDivisionError) as error:
        return JsonResponse({'error': str(error)}, status=400)

@csrf_exempt
def suma(request):
    return responder(request, 'suma', lambda a, b: a + b)

@csrf_exempt
def resta(request):
    return responder(request, 'resta', lambda a, b: a - b)

@csrf_exempt
def multiplicacion(request):
    return responder(request, 'multiplicacion', lambda a, b: a * b)

@csrf_exempt
def division(request):
    return responder(request, 'division', lambda a, b: a / b)

def test(request):
    return JsonResponse({'mensaje': 'API calculadora funcionando'})
```

## Código del repositorio

```python title="sistema_b/api_calculo/views.py"
import requests
from django.conf import settings
from django.http import JsonResponse

def enviar_a_calculadora(request, operacion):
    numero_1 = request.GET.get('numero_1')
    numero_2 = request.GET.get('numero_2')
    respuesta = requests.get(f'{settings.SYSTEM_B_CALCULADORA_URL}/{operacion}/', params={'numero_1': numero_1, 'numero_2': numero_2}, timeout=5)
    return JsonResponse(respuesta.json(), status=respuesta.status_code)

def suma(request):
    return enviar_a_calculadora(request, 'suma')

def resta(request):
    return enviar_a_calculadora(request, 'resta')

def multiplicacion(request):
    return enviar_a_calculadora(request, 'multiplicacion')

def division(request):
    return enviar_a_calculadora(request, 'division')

def test(request):
    return enviar_a_calculadora(request, 'test')
```
