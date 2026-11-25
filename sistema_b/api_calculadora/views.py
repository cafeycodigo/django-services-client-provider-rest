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
