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
