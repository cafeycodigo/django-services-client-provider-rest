import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calcular(request, operacion):
    try:
        datos = request.GET if request.method == 'GET' else json.loads(request.body or '{}')
        a, b = float(datos['numero_1']), float(datos['numero_2'])
        if operacion == 'suma': resultado = a + b
        elif operacion == 'resta': resultado = a - b
        elif operacion == 'multiplicacion': resultado = a * b
        elif operacion == 'division': resultado = a / b
        elif operacion == 'test': resultado = 'API funcionando'
        else: return JsonResponse({'error': 'Operación no válida'}, status=404)
        return JsonResponse({'operacion': operacion, 'resultado': resultado})
    except (KeyError, TypeError, ValueError, ZeroDivisionError, json.JSONDecodeError) as error:
        return JsonResponse({'error': str(error)}, status=400)
